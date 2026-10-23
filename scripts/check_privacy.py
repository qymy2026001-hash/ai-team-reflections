#!/usr/bin/env python3
"""Conservative, dependency-free checks. Never print matched sensitive values."""
import argparse
import io
import ipaddress
from pathlib import PurePosixPath
import re
import subprocess
import sys
import zipfile


def git(*args):
    return subprocess.check_output(['git', *args], stderr=subprocess.PIPE)


EMAIL = re.compile(r'[A-Z0-9.!#$%&*+/=?^_`{|}~-]+@[A-Z0-9.-]+\.[A-Z]{2,}', re.I)
RULES = {
    'private-key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
    'common-token': re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|sk-[A-Za-z0-9_-]{24,}|xox[baprs]-[A-Za-z0-9-]{20,})'),
    'credential-url': re.compile(r'\b[a-z][a-z0-9+.-]*://[^\s/:]+:[^\s/@]+@', re.I),
    'credential-assignment': re.compile(r'''(?im)^\s*["']?(?:password|passwd|api[_-]?key|access[_-]?token|secret|authorization)["']?\s*[:=]\s*["']?([A-Za-z0-9_+/=.-]{8,})'''),
    'signed-url': re.compile(r'[?&](?:X-Amz-Signature|X-Goog-Signature|access_token|token|sig)=[^\s&<>]{8,}', re.I),
    'personal-path': re.compile(r'(?:/Users/|/home/|[A-Z]:\\Users\\)[\w.-]+(?:[/\\]|$)', re.I),
    'phone-cn': re.compile(r'(?<![\w])(?:\+?86[ -]?)?1[3-9]\d{9}(?![\w])'),
    'identity-number-cn': re.compile(r'(?<!\w)[1-9]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[0-9Xx](?!\w)'),
}
PLACEHOLDERS = {'redacted', 'changeme', 'placeholder', 'example', 'example_value'}
TEXT_SUFFIXES = {'.md', '.txt', '.py', '.yml', '.yaml', '.json', '.toml', '.sh'}


def safe_email(value):
    domain = value.rsplit('@', 1)[1].lower()
    return domain in {'example.com', 'example.org', 'example.net', 'users.noreply.github.com'}


def text_findings(text):
    found = set()
    if any(not safe_email(m.group()) for m in EMAIL.finditer(text)):
        found.add('non-example-email')
    for name, pattern in RULES.items():
        for match in pattern.finditer(text):
            if name == 'credential-assignment' and match.group(1).lower() in PLACEHOLDERS:
                continue
            found.add(name)
    for match in re.finditer(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])', text):
        try:
            address = ipaddress.ip_address(match.group())
            documented = any(address in ipaddress.ip_network(n) for n in ['192.0.2.0/24', '198.51.100.0/24', '203.0.113.0/24'])
            if not address.is_global and not documented:
                found.add('non-public-ip')
        except ValueError:
            pass
    return found


def file_findings(path, data, mode='100644'):
    p = PurePosixPath(path)
    found = text_findings(path)
    if mode == '120000':
        found.add('symlink-not-supported')
    if (p.name == '.env' or (p.name.startswith('.env.') and p.name != '.env.example')
            or p.name in {'id_rsa', 'id_ed25519', '.netrc', '.npmrc', 'credentials.json'}
            or any(part in {'private', 'local-only', 'secrets', '.ssh'} for part in p.parts)
            or p.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.log', '.sql', '.dump', '.sqlite', '.db'}):
        found.add('restricted-filename')
    if len(data) > 2_000_000:
        return found | {'file-too-large-for-review'}
    if p.suffix.lower() == '.docx':
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                if sum(i.file_size for i in archive.infolist()) > 8_000_000:
                    return found | {'archive-too-large-for-review'}
                for item in archive.infolist():
                    if item.filename.startswith(('word/media/', 'word/embeddings/')):
                        found.add('embedded-media-needs-removal')
                    if item.filename.endswith(('.xml', '.rels')):
                        found |= text_findings(archive.read(item).decode('utf-8', errors='strict'))
        except (zipfile.BadZipFile, UnicodeError, RuntimeError):
            found.add('unreadable-document')
    elif p.suffix.lower() in TEXT_SUFFIXES or p.name in {'.gitignore', '.env.example', 'pre-commit', 'pre-push'}:
        try:
            found |= text_findings(data.decode('utf-8', errors='strict'))
        except UnicodeError:
            found.add('non-text-content')
    else:
        found.add('unsupported-file-type')
    return found


def scan(staged=False, history=False):
    failures = []
    seen = set()
    def check(path, oid, mode):
        key = (path, oid, mode)
        if key in seen:
            return
        seen.add(key)
        issues = file_findings(path, git('cat-file', 'blob', oid), mode)
        if issues:
            # Do not log names, paths, email addresses, excerpts, or values.
            failures.append(', '.join(sorted(issues)))
    if staged:
        entries = git('ls-files', '--stage', '-z')
        for entry in entries.split(b'\0'):
            if not entry:
                continue
            meta, path = entry.split(b'\t', 1)
            mode, oid, stage = meta.decode().split()
            if stage != '0':
                failures.append('unresolved-index')
                continue
            check(path.decode(), oid, mode)
        email = git('config', 'user.email').decode().strip()
        if not email.endswith('@users.noreply.github.com'):
            failures.append('commit-email-must-use-github-noreply')
    else:
        commits = git('rev-list', 'HEAD').decode().splitlines() if history else ['HEAD']
        for commit in commits:
            if history:
                metadata = git('show', '-s', '--format=%an%n%ae%n%cn%n%ce%n%B', commit).decode()
                failures.extend(sorted(text_findings(metadata)))
                emails = git('show', '-s', '--format=%ae%n%ce', commit).decode().splitlines()
                if any(not e.endswith('@users.noreply.github.com') for e in emails):
                    failures.append('historical-email-must-use-github-noreply')
            for entry in git('ls-tree', '-rz', commit).split(b'\0'):
                if not entry:
                    continue
                meta, path = entry.split(b'\t', 1)
                mode, kind, oid = meta.decode().split()
                if kind != 'blob':
                    failures.append('uninspectable-git-object')
                    continue
                check(path.decode(), oid, mode)
    return failures, len(seen)


def self_test():
    import tempfile
    from pathlib import Path
    import os
    fake_mail = 'tester' + '@' + 'mail.invalid'
    cases = [
        (fake_mail, 'non-example-email'),
        ('gh' + 'p_' + 'A' * 36, 'common-token'),
        ('-----BEGIN ' + 'PRIVATE KEY-----', 'private-key'),
        ('/Users/' + 'example-person/private', 'personal-path'),
        ('10.' + '20.30.40', 'non-public-ip'),
        ('138' + '00123456', 'phone-cn'),
        ('password' + '=not-a-real-password', 'credential-assignment'),
    ]
    for value, rule in cases:
        assert rule in text_findings(value), rule
    assert not text_findings('person@example.com <REDACTED>')
    assert not text_findings('123+example@users.noreply.github.com')
    assert 'restricted-filename' in file_findings('.env', b'')
    assert 'unsupported-file-type' in file_findings('screenshot.png', b'PNG')
    blob = io.BytesIO()
    with zipfile.ZipFile(blob, 'w') as z:
        z.writestr('docProps/core.xml', '<author>' + fake_mail + '</author>')
    assert 'non-example-email' in file_findings('test.docx', blob.getvalue())
    previous = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        try:
            os.chdir(tmp)
            git('init', '-q', '-b', 'main')
            git('config', 'user.name', 'Test contributor')
            git('config', 'user.email', '123+example@users.noreply.github.com')
            Path('note.md').write_text(fake_mail)
            git('add', 'note.md')
            assert scan(staged=True)[0]
            # A clean worktree must not hide sensitive content already staged.
            Path('note.md').write_text('Safe example')
            assert scan(staged=True)[0]
            git('commit', '-qm', 'Test initial fixture')
            git('add', 'note.md')
            assert not scan(staged=True)[0]
            git('commit', '-qm', 'Clean fixture')
            assert not scan()[0]
            assert scan(history=True)[0]
        finally:
            os.chdir(previous)
    print('Privacy checker self-tests passed (patterns, metadata, index, and history).')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--staged', action='store_true', help='Scan the entire index and configured commit email')
    group.add_argument('--history', action='store_true', help='Scan every commit reachable from HEAD')
    group.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    failures, count = scan(args.staged, args.history)
    if failures:
        print('Privacy check FAILED. Rule categories only; sensitive values are not printed.')
        for issue in sorted(set(failures)):
            print('- ' + issue)
        print('Inspect local staged content/history privately. Read PRIVACY.md / PRIVACY.en.md.')
        return 1
    print(f'Privacy check passed for {count} file versions. Human review is still required.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (subprocess.CalledProcessError, UnicodeError, ValueError, OSError):
        print('Privacy check could not complete; no content was logged. Check Git and file encoding locally.')
        sys.exit(2)
