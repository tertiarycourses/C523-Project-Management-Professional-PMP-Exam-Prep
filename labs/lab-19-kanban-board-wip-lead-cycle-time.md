# Lab 19 - Kanban Board with WIP Limits and Lead/Cycle Time

| Field | Value |
| --- | --- |
| Topic | 5 - Monitor and Control the Project |
| ECO 2026 task | Process T9 - Evaluate project status; Business Env T4 - Remove impediments and manage issues |
| Duration | 50 minutes |
| Consumes | Lab 10 product backlog and story points; Lab 08 definition of done; Lab 15 RACI |
| Produces | `artifacts/19-kanban-board.md`, `artifacts/19-flow-metrics.md`, `artifacts/19-bottleneck-analysis.md` |
| Live tool | [Kanban Board](https://alfredang.github.io/kanban/) |

## Objectives

- Build a Kanban board that reflects Contoso's actual workflow rather than a generic three-column template.
- Set and justify WIP limits, and understand why limiting work in progress speeds delivery.
- Measure lead time, cycle time and throughput from real card data.
- Apply Little's Law to predict delivery and to prove the effect of excess WIP.
- Identify the bottleneck from the board and decide the correct intervention.

## The core principles

```text
KANBAN'S SIX PRACTICES
  1. Visualise the workflow      - you cannot manage what you cannot see
  2. Limit work in progress      - the practice that does the actual work
  3. Manage flow                 - optimise for smooth movement, not utilisation
  4. Make policies explicit      - entry/exit criteria per column
  5. Implement feedback loops    - standups, reviews, metrics
  6. Improve collaboratively     - evolve the process with evidence

THE COUNTERINTUITIVE CENTRAL CLAIM
  Starting less work makes work finish faster.

  Why: every item in progress consumes attention, occupies a review slot,
  accrues merge conflicts and holds context in someone's head. Adding a
  second concurrent item does not halve the time for each - it more than
  doubles it, because of switching cost. Work that is started but not
  finished has delivered ZERO value while consuming full cost.

  "Stop starting, start finishing."

THE METRICS - distinguish them precisely, the exam does
  LEAD TIME    From the moment the CUSTOMER REQUESTS an item to delivery.
               Includes all waiting in the backlog. This is what the
               customer experiences.
  CYCLE TIME   From the moment WORK BEGINS on an item to delivery.
               Excludes backlog waiting. This is what the team controls.
  THROUGHPUT   Items completed per unit of time.
  WIP          Items currently started but not finished.

  Lead time is always >= cycle time. If someone quotes a single "cycle time"
  without saying where the clock starts, ask.

LITTLE'S LAW
  Average Cycle Time = Average WIP / Average Throughput

  Rearranged:  Throughput = WIP / Cycle Time
               WIP = Throughput x Cycle Time

  The law holds for any stable queueing system. Its practical consequence:
  with throughput roughly fixed by team capacity, DOUBLING WIP DOUBLES CYCLE
  TIME. It buys you nothing and costs you responsiveness.
```

## Steps

### Step 1 - Design the workflow columns

A three-column To Do / Doing / Done board hides everything interesting. Contoso's real workflow has distinct stages, and the waiting states between them are where the delay actually lives.

| # | Column | Type | Entry policy (definition of ready for this stage) | Exit policy |
| --- | --- | --- | --- | --- |
| 1 | Backlog | Queue | Story exists with a business value statement | Prioritised by product owner |
| 2 | Ready for Dev | Queue | Given/When/Then criteria complete, QA-reviewed, estimated, target devices stated | Developer available and pulls it |
| 3 | In Development | Active | Developer assigned, branch created | Code complete, unit tests pass, self-reviewed |
| 4 | Ready for Review | Queue | Pull request raised | Reviewer available |
| 5 | In Code Review | Active | Reviewer assigned | Approved, comments resolved |
| 6 | Ready for Test | Queue | Merged to the test branch, deployed to staging | QA available |
| 7 | In Test | Active | QA assigned, test cases identified | All acceptance criteria verified, accessibility scan clean |
| 8 | Ready for Acceptance | Queue | Deployed to the demo environment | Product owner available |
| 9 | Done | Terminal | Product owner accepted against acceptance criteria | - |

```text
NOTE THE STRUCTURE: active columns alternate with QUEUE columns.

This separation is the point. A card sitting in "Ready for Review" is not
being worked on - it is waiting. Merging queues into their adjacent active
column ("In Review" covering both waiting and reviewing) makes the board
look busy and hides the delay entirely.

In most knowledge-work systems, items spend far more time WAITING than being
worked on. You cannot find that time unless the board shows the queues.
```

### Step 2 - Set WIP limits

Open [Kanban Board](https://alfredang.github.io/kanban/) and create the columns above with these WIP limits.

```text
TEAM: 4 developers, 1 QA lead, 1 UX designer, 1 BA, 1 DevOps, 1 content lead

COLUMN                  WIP LIMIT   REASONING
  Backlog                  none      A queue of options, not committed work
  Ready for Dev              6       Buffer of about 1.5 sprints of ready work.
                                     Too small starves developers; too large
                                     means refinement effort is wasted on work
                                     that may be reprioritised.
  In Development             4       One per developer. Not 8 - a developer
                                     working on two stories finishes neither
                                     faster and both slower.
  Ready for Review           3       If more than 3 items wait for review, the
                                     team must stop developing and review.
  In Code Review             3       Reviewers are the same 4 developers;
                                     reviewing competes with developing.
  Ready for Test             3       The single QA lead is the constraint here.
  In Test                    2       One QA lead can genuinely hold two items.
  Ready for Acceptance       4       Product owner batches acceptance twice
                                     weekly, so a small queue is expected.
  Done                     none      Terminal state

TOTAL WIP ACROSS ACTIVE AND QUEUE COLUMNS: 6+4+3+3+3+2+4 = 25

THE RULE THAT MAKES IT WORK
  When a column is at its WIP limit, you may NOT pull a new item into it.
  If you cannot pull, you do not start something else - you go and help
  clear the blockage downstream. This is what converts a WIP limit from a
  number on a board into an actual behaviour change.
```

### Step 3 - Load the real card data

These are the 18 stories completed by the Contoso team during sprints 8 and 9, with the dates each card entered the system, started development, and was accepted. All dates are working days measured from the start of sprint 8 as day 1.

| Card | Story | Points | Entered backlog | Work started | Accepted (Done) | Lead time | Cycle time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | Course search by keyword | 3 | 1 | 1 | 5 | 4 | 4 |
| C-02 | Course search filters | 5 | 1 | 2 | 8 | 7 | 6 |
| C-03 | Responsive course list | 5 | 1 | 3 | 9 | 8 | 6 |
| C-04 | Registration step 1 - details | 8 | 1 | 4 | 13 | 12 | 9 |
| C-05 | Registration step 2 - consent | 5 | 2 | 5 | 12 | 10 | 7 |
| C-06 | Email confirmation template | 3 | 2 | 6 | 11 | 9 | 5 |
| C-07 | Reminder email scheduler | 8 | 2 | 7 | 18 | 16 | 11 |
| C-08 | Cancel booking flow | 5 | 3 | 8 | 16 | 13 | 8 |
| C-09 | Reschedule booking flow | 8 | 3 | 9 | 20 | 17 | 11 |
| C-10 | Booking history view | 3 | 4 | 11 | 16 | 12 | 5 |
| C-11 | Mobile nav menu | 3 | 4 | 12 | 17 | 13 | 5 |
| C-12 | Payment v2 - tokenise card | 8 | 5 | 13 | 24 | 19 | 11 |
| C-13 | Payment v2 - capture | 5 | 5 | 14 | 22 | 17 | 8 |
| C-14 | Accessibility - form labels | 2 | 6 | 15 | 19 | 13 | 4 |
| C-15 | Accessibility - contrast fixes | 2 | 6 | 16 | 20 | 14 | 4 |
| C-16 | Download completion record | 3 | 7 | 17 | 23 | 16 | 6 |
| C-17 | Session timeout handling | 3 | 8 | 18 | 25 | 17 | 7 |
| C-18 | Learner data export (PDPA) | 5 | 8 | 19 | 27 | 19 | 8 |

Enter these into the Kanban tool as cards, or work directly from the table.

### Step 4 - Compute the flow metrics

```text
LEAD TIME  =  Accepted - Entered backlog
CYCLE TIME =  Accepted - Work started

LEAD TIMES
  4, 7, 8, 12, 10, 9, 16, 13, 17, 12, 13, 19, 17, 13, 14, 16, 17, 19
  Sum = 236
  Mean lead time = 236 / 18 = 13.11 days

  Sorted: 4, 7, 8, 9, 10, 12, 12, 13, 13, 13, 14, 16, 16, 17, 17, 17, 19, 19
  Median = (13 + 13) / 2 = 13.0 days
  Min 4, Max 19, Range 15

CYCLE TIMES
  4, 6, 6, 9, 7, 5, 11, 8, 11, 5, 5, 11, 8, 4, 4, 6, 7, 8
  Sum = 125
  Mean cycle time = 125 / 18 = 6.94 days

  Sorted: 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 11, 11, 11
  Median = (6 + 7) / 2 = 6.5 days
  Min 4, Max 11, Range 7

THROUGHPUT
  18 cards completed over sprints 8 and 9 = 20 working days
  Throughput = 18 / 20 = 0.9 cards per day
             = 9 cards per sprint (10 working days)

STORY POINTS DELIVERED
  3+5+5+8+5+3+8+5+8+3+3+8+5+2+2+3+3+5 = 81 points over 2 sprints
  = 40.5 points per sprint
```

Now the diagnostic comparison:

```text
Mean lead time   13.11 days
Mean cycle time   6.94 days
DIFFERENCE        6.17 days  -  time spent waiting in the backlog before
                               work ever began

FLOW EFFICIENCY = cycle time / lead time = 6.94 / 13.11 = 52.9%

Only 53% of the time a customer waits is time anyone is working on their
request. The remaining 47% is pure queue.

And note that even the 6.94-day cycle time is not all active work - it
includes waiting in Ready for Review, Ready for Test and Ready for
Acceptance. True touch time is far lower still. If you instrumented the
queue columns you would typically find active work occupying 15-25% of
cycle time in a system like this.
```

### Step 5 - Apply Little's Law

```text
LITTLE'S LAW:  Cycle Time = WIP / Throughput

CHECK IT AGAINST THE OBSERVED DATA
  Throughput  = 0.9 cards/day
  Cycle time  = 6.94 days
  Therefore implied average WIP = 0.9 x 6.94 = 6.25 cards

  Verify directly: count cards in progress on a sample day. On day 12,
  cards started but not accepted were C-04, C-05, C-07, C-08, C-09, C-11
  = 6 cards. The law holds - implied WIP 6.25 against observed 6.

  This agreement is what tells you the system is reasonably STABLE and that
  the law can now be used predictively.

PREDICTIVE USE 1 - what if we start more work?
  Suppose the team, under pressure to "show progress", raises WIP to 12
  cards by starting everything available. Throughput does not rise - the
  team is the same size with the same skills.

    Cycle time = WIP / Throughput = 12 / 0.9 = 13.3 days

  Cycle time nearly DOUBLES, from 6.94 to 13.3 days. Nothing gets delivered
  sooner; everything gets delivered later. The board looks twice as busy and
  the customer waits twice as long.

PREDICTIVE USE 2 - what if we reduce WIP?
  Reduce WIP to 4 cards by enforcing the limits strictly.

    Cycle time = 4 / 0.9 = 4.4 days

  Cycle time falls from 6.94 to 4.4 days, a 37% improvement, with no new
  people, no new tools and no working harder. This is the entire argument
  for WIP limits, and it is arithmetic rather than opinion.

  CAVEAT worth stating: throughput is only fixed if the team is the
  constraint. Cutting WIP too far leaves people idle waiting for work, at
  which point throughput does fall. The optimum is the lowest WIP that
  keeps the constraint fully fed - which for this team is around 4-6.

PREDICTIVE USE 3 - forecasting a release
  22 stories remain for the final release.
    Time = WIP-independent estimate = 22 cards / 0.9 cards per day
         = 24.4 working days = approximately 2.5 sprints

  This forecast uses measured throughput rather than estimated effort, and
  it is usually more reliable than summing story points, because it
  incorporates all the real-world friction the estimates omit.
```

### Step 6 - Find the bottleneck

A bottleneck reveals itself as a queue that grows in front of one stage. Here is the average number of cards in each column, sampled daily across the 20 days.

| Column | Avg cards | WIP limit | Utilisation | Avg time a card spends here |
| --- | --- | --- | --- | --- |
| Ready for Dev | 4.2 | 6 | 70% | 6.2 days |
| In Development | 3.8 | 4 | 95% | 3.1 days |
| Ready for Review | 1.1 | 3 | 37% | 0.9 days |
| In Code Review | 1.4 | 3 | 47% | 1.2 days |
| **Ready for Test** | **2.9** | **3** | **97%** | **2.4 days** |
| **In Test** | **2.0** | **2** | **100%** | **1.9 days** |
| Ready for Acceptance | 1.3 | 4 | 33% | 0.6 days |

```text
BOTTLENECK IDENTIFIED: TEST

Evidence, in order of strength:
  1. "In Test" runs at 100% of its WIP limit - it is never idle and never
     has spare capacity. A stage permanently at its limit is by definition
     the constraint.
  2. "Ready for Test" runs at 97%, meaning a queue is almost always waiting
     to enter test. Work arrives faster than test can absorb it.
  3. Cards spend 2.4 days waiting for test plus 1.9 days in test = 4.3 days
     of the 6.94-day cycle time, which is 62% of cycle time in one stage.
  4. Downstream of test, utilisation collapses to 33%. The product owner is
     starved. That is the signature of an upstream constraint.

ROOT CAUSE: there is ONE QA lead serving four developers. Development
capacity is roughly four times test capacity. The queue is structural, not
a matter of effort.

THE THEORY OF CONSTRAINTS RESPONSE
  1. IDENTIFY the constraint.              Test. Done.
  2. EXPLOIT it - lose no constraint time.
       - The QA lead does no work that someone else could do: no status
         reports, no meeting attendance that is not about quality.
       - Nothing reaches test that is not genuinely ready. A card bounced
         back from test consumes the constraint twice. Enforce the Ready
         for Test entry policy strictly.
  3. SUBORDINATE everything else to it.
       - Developers do not start new work when the test queue is full.
         They pick up testing, write automation, or fix defects.
       - This is counterintuitive: developers will appear less busy, and
         that is correct. Optimising developer utilisation is what created
         the queue.
  4. ELEVATE the constraint - add capacity.
       - Two developers cross-trained to execute test cases.
       - Invest in the automated regression suite (WBS 1.9), which
         permanently reduces the manual test load per card.
  5. REPEAT - once test is no longer the constraint, find the next one.
     Likely candidates: code review, or development itself.

WHAT NOT TO DO
  Do not raise the "In Test" WIP limit. Allowing more cards into test does
  not create test capacity - it converts a visible queue into a hidden one
  and lengthens cycle time by Little's Law. Raising a WIP limit at a
  bottleneck is the single most common Kanban mistake.
```

### Step 7 - Read the cumulative flow diagram

The Kanban tool will render a cumulative flow diagram. Learn to read it, because a CFD is a strong candidate for a graphic-based exam item.

```text
HOW TO READ A CFD

  The chart plots cumulative card counts per column over time, stacked.

  BAND WIDTH (vertical thickness of a band) = the WIP in that stage.
    A widening band = a growing queue = a developing bottleneck.
    In the Contoso CFD, the "Ready for Test" band widens steadily from
    day 6 onward. That is the bottleneck appearing before anyone felt it.

  HORIZONTAL DISTANCE between the top line and the bottom line = LEAD TIME.
  VERTICAL DISTANCE between the top line and the bottom line = total WIP.

  SLOPE of the "Done" line = THROUGHPUT.
    Flattening slope = delivery slowing.
    In the Contoso data the Done line is close to linear at 0.9/day,
    confirming a stable system.

  FLAT BAND = work stalled in that stage, nothing entering or leaving.

  BANDS THAT NEVER CONVERGE = work started far faster than it is finished.
    The gap is your unfinished inventory, and it represents money spent
    with no value delivered.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
A team's average WIP is 20 items and its throughput is 4 items per week.
What is the average cycle time, and what happens if WIP rises to 30 with
throughput unchanged?

  A. 5 weeks; rising to 7.5 weeks
  B. 5 weeks; unchanged at 5 weeks
  C. 0.2 weeks; rising to 0.13 weeks
  D. 80 weeks; rising to 120 weeks

SCENARIO 2
The Contoso "In Test" column is permanently at its WIP limit of 2 and a
queue of cards waits to enter. The QA lead asks to raise the limit to 5 so
that cards stop piling up in "Ready for Test". What should the project
manager do?

  A. Raise the limit to 5; the current limit is clearly too restrictive.
  B. Decline. Raising the limit at the constraint adds no test capacity, it
     only moves the queue inside the column and lengthens cycle time.
     Instead exploit and elevate the constraint: cross-train developers to
     test, enforce the Ready for Test entry policy, and invest in automation.
  C. Remove WIP limits entirely so work flows freely.
  D. Raise the limit on "Ready for Test" instead.

SCENARIO 3
A stakeholder asks how long it takes to get a new feature. The team reports
a cycle time of 6.9 days. The stakeholder replies that their last request
took three weeks. Who is right?

  A. The team; the measurement is objective.
  B. The stakeholder; the team is understating its performance.
  C. Both. The team is quoting CYCLE time, measured from when work starts.
     The stakeholder experiences LEAD time, which includes backlog waiting.
     At Contoso, lead time averages 13.1 days against a 6.9-day cycle time,
     and for a lower-priority item the backlog wait can be far longer.
  D. Neither; both figures are unreliable.
```

Answer key:

```text
SCENARIO 1 -> A.  Little's Law: Cycle Time = WIP / Throughput = 20 / 4 =
            5 weeks. At WIP 30: 30 / 4 = 7.5 weeks.
            C inverts the formula (throughput / WIP). D multiplies instead
            of dividing. B is the intuition the law exists to correct -
            people expect that adding work in parallel is free, and it is
            not: with throughput fixed, cycle time rises in direct
            proportion to WIP.

SCENARIO 2 -> B.  A WIP limit does not cause a bottleneck; it reveals one.
            Raising it hides the queue rather than removing it, and by
            Little's Law raising WIP at the constraint from 2 to 5 would
            increase the time in that stage by roughly 2.5 times. The
            constraint is QA capacity, so the response must add effective
            capacity or reduce demand on it.
            A treats the symptom. C removes the only mechanism making the
            problem visible. D makes the upstream queue formally larger,
            which changes nothing about the rate at which test can absorb
            work - the queue simply has permission to grow.

SCENARIO 3 -> C.  Both figures are correct measurements of different
            things, and this is why the distinction is worth being precise
            about. The team optimises what it controls (cycle time); the
            customer experiences the whole wait (lead time). Reporting
            cycle time to a stakeholder who is asking a lead-time question
            is not dishonest but it is misleading, and it damages trust
            when the gap surfaces. Report lead time to customers, track
            cycle time internally, and reduce the gap by cutting backlog
            queue rather than by re-labelling the metric.
```

## Deliverable

Submit to `artifacts/`:

- `19-kanban-board.md` - the nine-column workflow with entry and exit policies per column and a justified WIP limit for each, with reasoning tied to actual team composition.
- A screenshot or export of your Kanban tool board with the 18 cards loaded.
- `19-flow-metrics.md` - mean and median lead time, mean and median cycle time, throughput per day and per sprint, and the flow efficiency percentage, all with working shown.
- The Little's Law verification against observed WIP on a sample day, plus the three predictive calculations (WIP raised to 12, WIP cut to 4, and the 22-card release forecast).
- `19-bottleneck-analysis.md` - the column utilisation table, the identified bottleneck with at least three pieces of supporting evidence, and the five Theory of Constraints steps applied to it.
- A written statement of why raising the WIP limit at the bottleneck is the wrong response.
- Your reading of the cumulative flow diagram, naming what the widening band indicates.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your board separates active columns from queue columns. A board with only In Progress and Done cannot show you where the waiting happens.
- Your mean lead time is 13.11 days and your mean cycle time is 6.94 days, and you can state why they differ.
- Your flow efficiency is 52.9%, and you interpreted it as "half the customer's wait is pure queue" rather than as a performance grade.
- Your Little's Law check produced an implied WIP of about 6.25 against an observed 6, and you used that agreement to justify using the law predictively.
- You showed arithmetically that doubling WIP roughly doubles cycle time while delivering nothing sooner.
- You identified Test as the bottleneck and cited its 100% utilisation, the 97% queue in front of it, and the collapse to 33% utilisation downstream.
- You explicitly rejected raising the In Test WIP limit and explained why it would make cycle time worse.
- Your constraint response includes subordination - developers stopping new work to help clear test - and you recognised that developers appearing less busy is the correct outcome rather than a problem.
