# Priorities and scope changes

[简体中文](../优先级与需求变更.md) | **English**

Status: Proposal. For teams whose plans frequently change because of new requirements, fixes, or cross-team dependencies.

## Problem analysis

New requests combined with unchanged commitments create task switching and hidden queues. Asking people to work more efficiently does not resolve insufficient capacity or conflicting priorities. Priority decisions should explain the benefit, urgency, implementation cost, and work being displaced.

## Suggested approach

1. Use one intake process to record goals, requester roles, reasons for deadlines, acceptance criteria, and impact.
2. Product proposes the order; engineering provides effort ranges, dependencies, and risk. Use time-limited investigation when unknowns are substantial.
3. Include review, testing, maintenance, and collaboration in capacity planning. Adjust from observed workloads instead of inventing a fixed allocation.
4. When a new request arrives, choose to defer, replace, reduce scope, or add specific support. Record changes to previous commitments.
5. Use an expedited path only for agreed emergency conditions, such as a serious ongoing service outage. Record the reasons and impact after recovery.

## Decision record

| Field | Question |
| --- | --- |
| Goal | What problem does the change address? |
| Urgency | Why must it happen in this cycle? |
| Cost and uncertainty | How much capacity is needed, and what remains unknown? |
| Tradeoff | What is deferred or reduced, and who agrees? |
| Delivery evidence | What demonstrates completion? |

## Costs and limits

Excessively detailed scoring creates false precision. A short written decision may be enough for a small task; cross-team or high-risk changes need more analysis. Decision owners must make tradeoffs promptly, or intake becomes another queue.

## Validation

Try the approach for one cycle. Record planned deliveries, unplanned additions, displaced tasks, and reasons. Check whether unfinished work mainly reflects scope changes or other blockers. Review outcomes alongside scope changes; do not evaluate individuals using an isolated on-time delivery percentage.

Next action: identify a priority decision owner and record one actual change in the [practice log](practice-log.md), using only information permitted by the privacy policy.
