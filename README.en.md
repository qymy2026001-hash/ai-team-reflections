# AI Team Reflections

[简体中文](README.md) | **English**

**Engineering, management, and independent thinking in human–AI collaboration**

AI Team Reflections records questions, hypotheses, experiments, and evolving judgments about working with AI. It explores engineering workflows and team management, including the decisions and responsibilities people should retain when using AI.

This repository contains selected reflections and methods suitable for public sharing. Existing workflow analysis and templates are starting points for discussion, not proven management answers; the practice log has no trial results yet. Open questions are welcome, but assumptions must not be presented as facts or outcomes.

## How we think through problems

1. State a concrete problem, your current judgment, and the reasons behind it.
2. Use AI to break down the problem, find counterexamples, and compare alternatives, separating sources from inference.
3. Make the decision yourself in light of real constraints, retaining responsibility for validation and action.
4. After a trial, record outcomes, costs, and limits, then decide what merits publication.

Not every discussion needs an article, and publication counts are not a measure of value. Real people's details, internal business context, and unpublished material stay out of this repository. Public examples must comply with the privacy policy.

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

Updates happen on demand, without scheduled publishing or automatic publication of conversations. Record problems suitable for public discussion in Issues, develop proposals in documentation PRs, and publish safe observations if a team tries them. Explain why conclusions change and link to previous discussions.

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

The project evolved from We Are a Team and was renamed AI Team Reflections on 2026-10-24, retaining its existing documents, bilingual structure, and privacy checks.
