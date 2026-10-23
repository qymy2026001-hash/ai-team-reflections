# Privacy and submission policy

[简体中文](PRIVACY.md) | **English**

## Mandatory rule

**Do not submit private personal information, active credentials, or internal material that is not authorized for public release.** This applies to files, Git content and history, commit identities, branch and tag descriptions, Issues, PRs, comments, screenshots, attachments, logs, and automation output. A private repository, later deletion, or demonstration purpose is not an exception.

Prohibited content includes:

- Real people's private email addresses, phone numbers, addresses, identity documents, account identifiers, precise locations, and other identifying details.
- Compensation, performance reviews, hiring assessments, health or financial information, customer orders, and other person-level or customer-level records.
- Passwords, API keys, access tokens, session cookies, private keys, database credentials, and signed links.
- Private network addresses, personal filesystem paths, internal topology, unpublished contracts, business data, source code, or incident details.
- Any of these within screenshots, chats, database exports, configuration, logs, document metadata, comments, or revision history.

GitHub usernames, project links, and GitHub noreply commit emails needed for public collaboration are permitted. This does not permit publishing private contact details. Do not collect irrelevant personal information merely because a source is public.

## Safe examples and anonymization

Prefer entirely fictional examples, role labels, and placeholders such as “Developer A,” “Example Customer,” `person@example.com`, and `<REDACTED>`. A real case may be rewritten for public use only with appropriate authorization, removal of identifying and confidential details, and confirmation that context cannot re-identify those involved.

Removing a name, partially masking an email, hashing an identifier, or renaming a file does not establish anonymity. Roles, dates, amounts, project names, and events can identify a person or organization in combination. When unsure, use a fictional example instead of submitting the source material.

## Before submission

1. Inspect filenames, text, URL parameters, images, attachments, and metadata for personal or internal details.
2. Inspect staged changes and commit records. Use a GitHub-provided noreply email so a private address does not appear in author or committer fields.
3. Run `python3 scripts/check_privacy.py --staged`; before pushing, run `python3 scripts/check_privacy.py --history`.
4. Optionally enable this repository's commit and push hooks with `git config core.hooksPath .githooks`. Hooks are not automatically enabled in a new clone.
5. Complete the PR privacy checklist. Reviewers must examine context rather than relying only on automated results.

The script checks tracked or staged content, common credential patterns, emails, some personal identifiers, private addresses, personal paths, and high-risk filenames. It scans Word XML and metadata and rejects embedded content it cannot inspect. `--history` also checks file content, commit messages, and identities reachable from the current HEAD. It does not cover every remote hidden ref, cached view, Issue, or attachment.

## Limits of enforcement

GitHub Actions runs after push or PR upload and cannot undo disclosure. Local hooks apply only to clones where enabled and may be bypassed. Pattern checks cannot recognize all HR, business, or contextual privacy risks, or prove that an image is safely anonymized. Human review before public submission remains necessary. A passing check does not authorize prohibited content.

## If information is accidentally submitted

Stop further distribution. Do not copy the information into a public Issue or PR. Revoke or rotate exposed credentials immediately. Notify the maintainer through an existing trusted private channel, providing only enough information to locate the exposure. Assess files, history, attachments, logs, and copies; contact GitHub Support about cached references when needed. Deleting the latest file or rewriting history does not guarantee that remote caches or other people's copies are cleared.

Do not merge or publish affected changes until safe. Never upload the original sensitive material as a “sample of the leak.”

Reference: [GitHub guide to removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Accessed 2026-10-23.
