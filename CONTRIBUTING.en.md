# Contributing

[简体中文](CONTRIBUTING.md) | **English**

## Privacy comes first

Read the [privacy policy](PRIVACY.en.md). Never submit personal information, credentials, or confidential organizational material, including in commit identities, Issues, PRs, attachments, or logs. Use fictional examples; remove identifying details and metadata before upload. Use a GitHub-provided noreply email for commits.

Run `python3 scripts/check_privacy.py --staged` before committing and `python3 scripts/check_privacy.py --history` before pushing. Enable the provided local hooks with `git config core.hooksPath .githooks`. Hooks apply only to the current clone and can be bypassed; CI runs after upload. Neither replaces human review.

## Record the problem

Check the [topic backlog](docs/en/topic-backlog.md) and existing Issues before starting a duplicate discussion. Describe the context, people affected by role rather than identity, desired improvement, and available evidence. Separate facts from assumptions when data is missing.

## Propose a change

1. Create a short-lived branch from current `main`, such as `docs/review-process`.
2. Use the [management idea template](templates/en/management-idea.md), or revise the existing article.
3. Update both language editions, README navigation, and the topic backlog. Check relative links.
4. Open a PR describing the problem, change, limits, and validation, and link the discussion Issue.
5. Invite an appropriate reviewer when collaborators are available. A sole maintainer must identify self-review as such, not as independent review.
6. If a trial is planned after merging, separately record its owner, scope, and review date using non-identifying information.

The initial repository was created directly on its default branch. Subsequent changes should use PRs. This convention does not itself configure required approvals or branch protection in GitHub.

## Writing and evidence

- Maintain equivalent Chinese and English guidance. Keep technical terms where helpful, and use descriptive titles.
- If translation cannot be completed in the same PR, explicitly mark the affected page and explain the gap in the PR; do not silently let versions diverge.
- Give actionable steps, including costs, exceptions, and conditions for stopping a trial.
- Prefer primary sources, link them, and record access dates. Recheck platform behavior when it changes.
- Do not invent team members, current conditions, interviews, metrics, or trial results.
- Do not rank individuals directly by commit counts, lines of code, or time online.

## Status labels

Use **To discuss, In writing, Documented, In trial, Reviewed after trial, Deferred**. “Documented” means an article exists, not that it works in practice. Use the two trial-related statuses only when an actual record exists. Explain revisions in PRs and retain links for substantial changes in conclusions.
