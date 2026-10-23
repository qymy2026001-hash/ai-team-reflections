# We Are a Team

[简体中文](README.md) | **English**

Document, discuss, and test ways to manage engineering teams, connecting requirements, code, delivery, and professional growth through traceable collaboration.

This is a public engineering management knowledge base. It uses GitHub to maintain process analysis, management ideas, practice reports, and reusable templates. The articles are proposals for teams to evaluate in their own context, not claims of proven results.

## Start here

| What you want to explore | Reading |
| --- | --- |
| Delivery stages, responsibilities, quality, and releases | [Engineering workflow and team management](docs/en/engineering-workflow.md) |
| Principles for managing a team | [Team management principles](docs/en/team-principles.md) |
| Handling changing requirements | [Priorities and scope changes](docs/en/priorities-and-scope.md) |
| Reducing PR waiting time while preserving review quality | [Code review and collaboration](docs/en/code-review.md) |
| Topics to discuss next | [Topic backlog](docs/en/topic-backlog.md) |
| Testing management ideas in practice | [Practice log](docs/en/practice-log.md) |
| Adding and revising material | [Contributing](CONTRIBUTING.en.md) |
| What must never be submitted | [Privacy and submission policy](PRIVACY.en.md) |

## Privacy is a contribution requirement

**Do not submit personal information, credentials, or confidential material.** This applies to files, Git history and commit identities, Issues, PRs, comments, screenshots, attachments, and logs. Use fictional, non-identifying examples. Removing a name alone is not sufficient anonymization. Read the [policy](PRIVACY.en.md) before contributing.

The repository includes a local check, opt-in Git hooks, and a GitHub Actions check. Pattern checks cannot establish that content is safe to publish; contributors and reviewers must also inspect context and metadata. CI runs after upload and cannot prevent initial disclosure.

## How updates work

Updates happen on demand, without scheduled publishing. Record a problem in an Issue, develop a proposal in a documentation PR, and record observations if a team chooses to try it. Explain why conclusions change and link to previous discussions.

```text
Problem or idea → Issue discussion → Documentation PR → Review and merge
                                              ↓
                                  Team decides whether to try it
                                              ↓
                                Observations → Revised guidance
```

Articles should state the context, problem, proposed steps, costs and limits, validation method, and next action. Label untested ideas as proposals; do not present assumptions as results.

## Reusable templates

- [Management idea](templates/en/management-idea.md)
- [Practice retrospective](templates/en/practice-retrospective.md)
- [Requirement record](templates/en/requirement.md)
- [Release record](templates/en/release.md)
- Bilingual Issue and PR templates are available in this repository.

## Maintaining the documents

Chinese and English Markdown documents are maintained together, with language links between matching pages. A substantive change should update both languages or clearly mark the lagging translation in the PR and the affected page.

The [original Chinese Word document](docs/archive/GitHub项目研发流程与团队管理分析.docx) is a historical snapshot dated 2026-10-23. It is not maintained or translated as part of the bilingual Markdown editions.

The project contains management documentation and privacy checks. Recommendations for protecting branches, testing applications, or deploying services do not mean those controls have been configured in anyone's business repositories.
