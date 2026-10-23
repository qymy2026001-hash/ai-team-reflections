# Code review and collaboration

[简体中文](../代码评审与协作效率.md) | **English**

Status: Proposal. For teams with PR queues, repeated arguments, or unclear review responsibility.

## Problem analysis

Completed development can still wait a long time for review. Large PRs, missing context, concentration of reviews among a few people, and feedback without priorities can all cause repeated task switching. More required approvals increase waiting and do not automatically improve judgment.

## Suggested approach

1. Keep each PR focused on one explainable goal. Discuss design and sequencing before large changes.
2. Authors explain the problem, behavioral changes, important decisions, validation, and remaining risks, and complete a self-review first.
3. Assign an appropriate reviewer when ready. Use a draft PR for early design feedback when useful.
4. Distinguish required changes, suggested improvements, and clarification questions. Do not turn personal preferences into unexplained blockers.
5. Automate formatting and static rules so human attention goes to correctness, compatibility, permissions, and maintenance cost.
6. Provide backup reviewers for critical modules. Help clear existing queues before starting more work when reviews are accumulating.

## A starting point for risk-based review

| Change type | Possible review approach |
| --- | --- |
| Documentation and low-risk adjustments | Check accuracy, links, or visual results under the team's agreement |
| Normal features and fixes | Review by an appropriate colleague, supported by relevant test evidence |
| Permissions, billing, migrations, or cross-service changes | Domain-owner involvement, including compatibility, failure paths, and recovery |

Agree on approval counts and response expectations after a trial, rather than imposing universal targets. Reconsider previous approval when substantive code changes arrive.

## Costs and limits

Excessive splitting can obscure overall impact; preserve context through linked PRs or design records. Review rotation does not mean an inexperienced reviewer should approve a critical change alone. A sole maintainer should record self-review and validation limits without claiming independent approval.

## Validation

Measure time from readiness for review to the first substantive human response. Examine long waits and their causes alongside post-merge defects and rework. If waiting improves but production defects rise, change the validation approach instead of pushing for faster approval.

Next action: examine a recent set of PRs to identify whether size, reviewer capacity, or missing context is the main bottleneck, then try one improvement.
