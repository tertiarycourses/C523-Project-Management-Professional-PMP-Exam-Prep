# Lab 21 - Root Cause Analysis with 5 Whys, Fishbone and Pareto

| Field | Value |
| --- | --- |
| Topic | 5 - Monitor and Control the Project |
| ECO 2026 task | Business Env T4 - Remove impediments and manage issues; Process T7 - Plan and optimize quality; Business Env T6 - Continuous improvement |
| Duration | 60 minutes |
| Consumes | Lab 20 CPI decline and its systemic signal; Lab 08 definition of done; Lab 03 issue path |
| Produces | `artifacts/21-pareto-analysis.md`, `artifacts/21-fishbone.md`, `artifacts/21-5whys.md`, `artifacts/21-corrective-actions.md` |
| Live tools | [Pareto Chart](https://alfredang.github.io/paretochart/), [Fishbone Diagram](https://alfredang.github.io/fishbone/), [5 Whys](https://alfredang.github.io/5whys/) |

## Objectives

- Use Pareto analysis to find the vital few defect categories driving most of the pain.
- Use a fishbone diagram to generate candidate causes across all six categories rather than the first one that comes to mind.
- Use 5 Whys to drive from a symptom to an actionable root cause.
- Distinguish root cause from symptom, and corrective from preventive action.
- Close the loop on the Lab 20 finding: explain *why* CPI declined for seven consecutive periods.

## The sequence matters

These three tools are not alternatives. They run in order, and each answers a different question.

```text
PARETO    "WHERE should we look?"
          Quantitative. Ranks categories by frequency or cost.
          Narrows a large problem space to the vital few.
          Runs FIRST, because effort spent on the trivial many is wasted.

FISHBONE  "WHAT could be causing it?"
          Divergent and qualitative. Generates candidate causes across six
          categories so you do not stop at the first plausible explanation.
          Runs SECOND, on the top Pareto category only.

5 WHYS    "WHY does that happen, really?"
          Convergent. Drills one branch of the fishbone down to an
          actionable root cause.
          Runs THIRD, on the most likely fishbone branch.

The failure mode of skipping Pareto is fixing something real that does not
matter. The failure mode of skipping the fishbone is fixing the first cause
you thought of. The failure mode of skipping 5 Whys is fixing a symptom.
```

## Steps

### Step 1 - Take the defect data

This is the real defect log for the Contoso Training Portal Upgrade, covering sprints 1 to 7 - the same period over which Lab 20 showed CPI declining from 1.022 to 0.919. Every defect here was found after the developer marked the story done.

| Defect category | Count | Rework hours | Cost at SGD 620/day (8h) |
| --- | --- | --- | --- |
| Incomplete or ambiguous acceptance criteria | 47 | 188 | 14,570 |
| Browser/device compatibility failures | 38 | 133 | 10,304 |
| Data validation errors on registration form | 22 | 66 | 5,115 |
| Integration failures with learner database | 16 | 96 | 7,440 |
| Accessibility (WCAG AA) violations | 14 | 42 | 3,255 |
| Payment gateway v2 API handling | 9 | 54 | 4,185 |
| Performance under concurrent load | 7 | 35 | 2,713 |
| Email template rendering | 6 | 12 | 930 |
| Session/timeout handling | 4 | 16 | 1,240 |
| Reporting and export | 3 | 9 | 698 |
| Miscellaneous / could not reproduce | 2 | 4 | 310 |
| **Total** | **168** | **655** | **50,760** |

```text
Note the scale before going further. 655 rework hours is 81.9 person-days.
At the blended rate that is SGD 50,760 of unplanned effort inside a project
whose forecast overrun (Lab 20 VAC) is SGD 42,420.

The rework alone is larger than the overrun. This is not a coincidence, and
by the end of this lab you will be able to state the causal chain.
```

### Step 2 - Build the Pareto chart

Open [Pareto Chart](https://alfredang.github.io/paretochart/).

Enter these category/count pairs exactly:

```text
Incomplete or ambiguous acceptance criteria    47
Browser/device compatibility failures          38
Data validation errors                         22
Integration failures with learner database     16
Accessibility (WCAG AA) violations             14
Payment gateway v2 API handling                 9
Performance under concurrent load               7
Email template rendering                        6
Session/timeout handling                        4
Reporting and export                            3
Miscellaneous / could not reproduce             2
```

Compute the cumulative percentages yourself and verify against the tool's output:

| Rank | Category | Count | % of total | Cumulative % |
| --- | --- | --- | --- | --- |
| 1 | Incomplete/ambiguous acceptance criteria | 47 | 27.98% | 27.98% |
| 2 | Browser/device compatibility | 38 | 22.62% | 50.60% |
| 3 | Data validation errors | 22 | 13.10% | 63.69% |
| 4 | Integration failures | 16 | 9.52% | 73.21% |
| 5 | Accessibility violations | 14 | 8.33% | **81.55%** |
| 6 | Payment gateway v2 | 9 | 5.36% | 86.90% |
| 7 | Performance under load | 7 | 4.17% | 91.07% |
| 8 | Email template rendering | 6 | 3.57% | 94.64% |
| 9 | Session/timeout | 4 | 2.38% | 97.02% |
| 10 | Reporting and export | 3 | 1.79% | 98.81% |
| 11 | Miscellaneous | 2 | 1.19% | 100.00% |

```text
THE 80/20 CUT

The cumulative line crosses 80% at rank 5.
FIVE categories out of eleven account for 81.55% of all defects.
That is 45% of the categories producing 82% of the defects - close to the
classic 80/20 shape.

VITAL FEW (address these):
  1. Incomplete/ambiguous acceptance criteria    47
  2. Browser/device compatibility                38
  3. Data validation errors                      22
  4. Integration failures                        16
  5. Accessibility violations                    14
                                    subtotal    137  (81.55%)

TRIVIAL MANY (monitor, do not prioritise):
  ranks 6-11                        subtotal     31  (18.45%)
```

### Step 3 - Re-run Pareto by cost, and notice the disagreement

Frequency is not impact. Re-rank the same data by rework hours.

| Rank by hours | Category | Hours | % of total | Cumulative % |
| --- | --- | --- | --- | --- |
| 1 | Incomplete/ambiguous acceptance criteria | 188 | 28.70% | 28.70% |
| 2 | Browser/device compatibility | 133 | 20.31% | 49.01% |
| 3 | Integration failures | 96 | 14.66% | 63.66% |
| 4 | Data validation errors | 66 | 10.08% | 73.74% |
| 5 | Payment gateway v2 | 54 | 8.24% | **81.98%** |
| 6 | Accessibility violations | 42 | 6.41% | 88.40% |
| 7 | Performance under load | 35 | 5.34% | 93.74% |
| 8 | Session/timeout | 16 | 2.44% | 96.18% |
| 9 | Email templates | 12 | 1.83% | 98.02% |
| 10 | Reporting and export | 9 | 1.37% | 99.39% |
| 11 | Miscellaneous | 4 | 0.61% | 100.00% |

```text
WHAT CHANGED

Integration failures move from rank 4 to rank 3, and payment gateway v2
enters the vital few at rank 5, displacing accessibility violations.

Why: integration defects average 6.0 hours each to fix and gateway defects
average 6.0 hours, while accessibility defects average only 3.0 hours.
Low-frequency, high-effort categories hide from a frequency Pareto.

  Average rework hours per defect:
    Integration failures      96 / 16 = 6.00 h
    Payment gateway v2        54 /  9 = 6.00 h
    Performance under load    35 /  7 = 5.00 h
    Acceptance criteria      188 / 47 = 4.00 h
    Data validation           66 / 22 = 3.00 h
    Browser compatibility    133 / 38 = 3.50 h
    Accessibility             42 / 14 = 3.00 h

CONCLUSION: rank 1 and rank 2 are the same on BOTH measures. Acceptance
criteria and browser compatibility are unambiguously the vital few, and
together they account for 49% of all rework hours. Attack rank 1 first.

The exam point: always ask what the Pareto is counting. A Pareto by
frequency and a Pareto by cost can recommend different actions, and the one
that matters depends on what you are trying to reduce.
```

### Step 4 - Fishbone the top category

Open [Fishbone Diagram](https://alfredang.github.io/fishbone/).

Set the problem statement (the fish head) to exactly:

```text
47 defects and 188 rework hours caused by incomplete or ambiguous
acceptance criteria in sprints 1-7
```

Use the six standard categories - the 6Ms, adapted for a software project - and enter these causes. The discipline is to put at least two causes under every category, including the ones that feel unlikely. Categories left empty are usually the ones hiding the real cause.

```text
PEOPLE (Manpower)
  - The BA is the single point of writing for all acceptance criteria
  - The three admin staff SMEs have capped hours and are frequently unavailable
  - Developers do not attend refinement sessions consistently
  - No one is designated to challenge a weak acceptance criterion

PROCESS (Method)
  - Definition of Ready exists but is not enforced at sprint planning
  - Stories enter the sprint without QA having reviewed the criteria
  - Refinement is scheduled for 60 minutes and routinely runs out of time
  - No template or standard for writing acceptance criteria
  - Criteria are written in prose rather than in Given/When/Then form

MACHINE (Tools/Technology)
  - Acceptance criteria live in the ticket description, not as testable items
  - No automated linkage between a criterion and a test case
  - The RTM from Lab 09 is maintained manually and lags by about a sprint

MATERIALS (Inputs)
  - Source requirements from Lab 09 vary in specificity
  - Non-functional requirements are stated at the epic level, not per story
  - Legacy portal behaviour is undocumented, so "same as current" is ambiguous

MEASUREMENT
  - No metric tracks acceptance criteria quality before development starts
  - Defects are counted at test, which is far too late to act
  - Rework hours are recorded but never reviewed at the retrospective

ENVIRONMENT
  - Fixed 30 June launch creates pressure to start coding before refinement
    is complete
  - SME availability constrained by the operational day job (TECOP factor O1)
  - Team is at Tuckman storming stage (Lab 16), so challenge is being avoided
```

Now converge. Rank the branches by likely contribution:

| Branch | Category | Evidence supporting it | Likely contribution |
| --- | --- | --- | --- |
| Definition of Ready not enforced | Process | 47 defects all originated in stories that entered a sprint; DoR exists on paper | **High** |
| SME availability capped | People | Refinement notes show 9 of 14 sessions had no SME present | **High** |
| Schedule pressure to start early | Environment | Sprint start dates fixed regardless of refinement completion | Medium |
| No Given/When/Then standard | Process | Sampled criteria vary from 1 line to 2 pages | Medium |
| No pre-development quality metric | Measurement | Nothing measured until test | Medium |
| Manual RTM lag | Machine | Lags one sprint | Low |

Take the highest-contribution branch - Definition of Ready not enforced - into 5 Whys.

### Step 5 - Drive to root cause with 5 Whys

Open [5 Whys](https://alfredang.github.io/5whys/).

Enter the problem statement:

```text
Stories are entering sprints without meeting the Definition of Ready
```

Then work the chain. Each "why" must be answerable with evidence, not opinion.

```text
PROBLEM: Stories are entering sprints without meeting the Definition of Ready.

WHY 1  Why do stories enter the sprint without meeting the DoR?
       Because sprint planning accepts them even when acceptance criteria
       are incomplete.
       EVIDENCE: 31 of 84 stories in sprints 1-7 were accepted with
       criteria marked "to be confirmed".

WHY 2  Why does sprint planning accept incomplete stories?
       Because if the team only accepted fully-ready stories, there would
       not be enough work to fill the sprint's 34-point capacity.
       EVIDENCE: refinement produced an average of 22 ready points per
       sprint against a 34-point capacity.

WHY 3  Why does refinement produce only 22 ready points against 34 needed?
       Because refinement sessions cannot complete without SME input, and
       SMEs attended only 5 of 14 sessions.
       EVIDENCE: refinement attendance log.

WHY 4  Why are SMEs absent from two-thirds of refinement sessions?
       Because the three admin staff who are the SMEs are still performing
       24 hours a week of manual learner communications - the very work
       this project exists to automate - and operational work always wins.
       EVIDENCE: Lab 02 TECOP factor O1 predicted exactly this. Lab 06
       assumption A-07 assumed capped SME hours would be agreed by week 2.

WHY 5  Why was no backfill or capped SME allocation ever put in place?
       Because assumption A-07 was recorded in the assumption log with an
       owner and a validation date, and then never validated or escalated
       when it failed.
       EVIDENCE: assumption log shows A-07 still open at week 14, twelve
       weeks past its validation date.

ROOT CAUSE
  The project assumed SME availability that was never secured, and the
  assumption-log control that existed to catch this was not operated.

  Note the shape of a good root cause: it is a PROCESS or SYSTEM failure
  that management can act on, not a person's shortcoming. "The BA writes
  poor criteria" would have been a symptom and a false one - the BA cannot
  write criteria for information she does not have.
```

```text
THE CAUSAL CHAIN, END TO END

  A-07 assumption never validated
    -> SMEs unavailable for refinement (5 of 14 sessions)
    -> refinement yields 22 ready points vs 34 capacity
    -> sprint planning accepts incomplete stories to fill capacity
    -> 47 defects from ambiguous acceptance criteria (Pareto rank 1)
    -> 188 rework hours, SGD 14,570 unplanned effort
    -> plus 133 hours from browser compatibility (rank 2, same root:
       criteria did not state target devices)
    -> 655 total rework hours, SGD 50,760
    -> CPI declines monotonically for 7 periods, 1.022 -> 0.919 (Lab 20)
    -> forecast overrun VAC -SGD 42,420

This is the answer to the question Lab 20 raised and could not answer.
EVM told you THAT performance was degrading and that it was systemic.
It could not tell you WHY. Root cause analysis does that, and the two
techniques are only useful together.
```

### Step 6 - Verify the root cause before acting

A root cause you have not tested is a hypothesis. Apply the two standard tests.

```text
TEST 1 - THE "THEREFORE" TEST (read the chain upward)
  The assumption was not validated,
    THEREFORE SMEs were unavailable,
    THEREFORE refinement under-produced,
    THEREFORE incomplete stories were accepted,
    THEREFORE acceptance criteria defects occurred.
  Each step follows. If any "therefore" does not hold, the chain is broken
  at that point and you have gone too far or jumped a step.

TEST 2 - THE REMOVAL TEST
  If SME availability had been secured at week 2, would the 47 defects have
  occurred?
  Largely no. Refinement would have produced sufficient ready stories, and
  sprint planning would not have needed to accept incomplete ones.

  Would ALL 168 defects have been prevented? No - and this matters. Payment
  gateway defects and performance defects have different causes. Do not
  over-claim. This root cause explains ranks 1 and 2, approximately 49% of
  rework hours. That is enough to act on decisively; it is not everything.

TEST 3 - COUNTER-CHECK
  Does the timing fit? SME attendance was worst in sprints 4-7. CPI declined
  most steeply in periods 4-7 (0.959 -> 0.919). The correlation holds.
```

### Step 7 - Design corrective and preventive actions

The distinction is exam-relevant and practically important.

```text
CORRECTIVE ACTION   Fixes the CURRENT deviation. Brings performance back
                    in line with the plan.
PREVENTIVE ACTION   Stops the cause RECURRING, on this project or the next.
DEFECT REPAIR       Fixes the defective deliverable itself.

All three go through integrated change control if they affect a baseline.
An exam question naming an action that stops a future occurrence is asking
about preventive action, even if the word "corrective" appears in the stem.
```

Create `artifacts/21-corrective-actions.md`:

| # | Action | Type | Addresses | Owner | By when | Success measure |
| --- | --- | --- | --- | --- | --- | --- |
| A-1 | Secure 6 hours/week of guaranteed SME time in writing from the Ops Manager; backfill their operational work with a temporary agency administrator | Corrective | Root cause | PM | Week 15 | SME present at 100% of refinement sessions |
| A-2 | Enforce the Definition of Ready as a hard gate at sprint planning; no story enters without complete Given/When/Then criteria and QA review | Preventive | Why 1 | Product Owner | Sprint 8 | 0 stories accepted with "TBC" criteria |
| A-3 | Accept a lower sprint commitment rather than filling capacity with unready work; plan 26 points until refinement recovers | Corrective | Why 2 | Product Owner | Sprint 8 | Committed points delivered at 95%+ |
| A-4 | Adopt a Given/When/Then template with a mandatory target-device list (fixes Pareto rank 2 at source) | Preventive | Ranks 1 and 2 | BA | Week 15 | Browser defects down 60% by sprint 10 |
| A-5 | Add a pre-development quality metric: percentage of stories meeting DoR at planning, reported at every sprint review | Preventive | Measurement branch | QA Lead | Sprint 8 | Metric reported every sprint, target 100% |
| A-6 | Review all open assumptions from Lab 06 immediately; escalate any past its validation date | Preventive | The control failure itself | PM | Week 15 | All 7 assumptions closed or escalated |
| A-7 | Repair the 47 outstanding acceptance-criteria defects, prioritised by whether they touch charter success criteria | Defect repair | The defects | Dev Lead | Sprint 8-9 | Open defect count under 10 |
| A-8 | Add "assumption log reviewed" as a standing item at every stage gate; update the OPA gate checklist so future projects inherit it | Preventive (organisational) | Systemic | PM | Week 16 | OPA checklist updated |

```text
A-6 AND A-8 ARE THE MOST IMPORTANT ACTIONS ON THIS LIST.

A-1 through A-5 fix the acceptance criteria problem. A-6 asks the obvious
follow-up: if assumption A-07 was left unvalidated for twelve weeks, what
about the other six? A-05 (the DPO can review in three weeks) is on that
same list, and it gates go-live.

A-8 is what makes this a contribution to the organisation rather than a
save on one project. ECO Business Env T6 requires updating OPAs. The lesson
here is not "SMEs should attend refinement" - it is "an assumption log
whose validation dates are not enforced is decoration". That belongs in the
lessons-learned repository (Lab 23) and in the gate checklist for every
future project.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
A Pareto chart of 340 defects shows: category A 118, B 96, C 54, D 31,
E 22, F 12, G 7. Which categories constitute the vital few at the 80% cut?

  A. A only
  B. A and B
  C. A, B and C
  D. A, B, C and D

SCENARIO 2
The team proposes fixing the 47 acceptance-criteria defects by adding a
second QA engineer to catch them in testing. As project manager, what is
your assessment?

  A. Approve it; more testing capacity will reduce escaped defects.
  B. Reject it; it treats the symptom. The defects originate before
     development starts, so detecting them later still incurs the rework.
     Fix the Definition of Ready gate and SME availability instead.
  C. Approve it as a short-term measure while also fixing the root cause.
  D. Reject it; the budget cannot absorb another resource.

SCENARIO 3
Your 5 Whys chain ends at "the developer did not read the acceptance
criteria carefully". What is wrong with this as a root cause?

  A. Nothing; it identifies who is responsible.
  B. It is a person-focused symptom rather than a system cause, so the only
     available action is to tell someone to try harder - which does not
     change the conditions that produced the outcome.
  C. It needs a sixth why.
  D. It should have been found by the fishbone instead.
```

Answer key:

```text
SCENARIO 1 -> C.  Total 340.
            A       118  = 34.7%,  cumulative 34.7%
            A+B     214  = 62.9%,  cumulative 62.9%
            A+B+C   268  = 78.8%,  cumulative 78.8%
            A+B+C+D 299  = 87.9%,  cumulative 87.9%
            The cut is at 80%. C alone reaches 78.8%, D takes it to 87.9%.
            The convention is to take categories UP TO and INCLUDING the one
            that crosses 80%... but note 78.8% has not yet crossed it.
            Adding D crosses it. The defensible answer is C: three categories
            capture 78.8%, essentially the vital few, and D adds 9% for a 33%
            increase in scope of work. If an exam offers both C and D, prefer
            the smaller set that approaches 80% - Pareto is about
            concentrating effort, and 78.8% from three categories is the
            better return. Be ready to justify either; the reasoning is what
            is being tested.

SCENARIO 2 -> B.  Detection is not prevention. The 188 rework hours are
            incurred whether the defect is caught in test or in production -
            the code was still written wrong. Adding QA capacity moves the
            discovery point earlier but does not reduce the rework, and it
            adds cost to a project already forecasting an overrun.
            C is tempting and is sometimes right, but not here: the "short
            term measure" costs money and delivers no reduction in rework,
            so there is nothing to justify it. If the proposal had been
            "add automated regression coverage", C would be defensible.
            D rejects for the right outcome but the wrong reason - budget
            is not the argument; effectiveness is.

SCENARIO 3 -> B.  A root cause must be actionable at the system level.
            "Someone should have been more careful" yields only exhortation,
            and exhortation does not change outcomes - if it did, the problem
            would already be solved. Ask instead why the criteria were hard to
            read, why there was no template, why nothing verified them before
            development began. Person-blaming chains also destroy the
            psychological safety that root cause analysis depends on: the
            next time something goes wrong, nobody will tell you.
            C is wrong because the number five is a guideline, not a rule -
            you stop when you reach an actionable system cause, which may be
            at three whys or at seven.
```

## Deliverable

Submit to `artifacts/`:

- `21-pareto-analysis.md` - the Pareto table by frequency with cumulative percentages, the vital few identified at the 80% cut, plus the second Pareto by rework hours and a written statement of what changed between them and why.
- A screenshot or export of your Pareto Chart tool output.
- `21-fishbone.md` - all six categories populated with at least two causes each, the branches ranked by likely contribution with supporting evidence, and your chosen branch identified.
- A screenshot or export of your Fishbone tool output.
- `21-5whys.md` - the five-why chain with evidence at every level, the stated root cause, and the results of the therefore test and the removal test.
- The end-to-end causal chain linking the root cause to the Lab 20 CPI decline.
- `21-corrective-actions.md` - at least 8 actions, each classified as corrective, preventive or defect repair, with owner, date and success measure.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your cumulative percentages reach exactly 100% and your 80% cut falls at rank 5 with 81.55%.
- You ran the Pareto twice, on frequency and on cost, and you identified that acceptance criteria and browser compatibility rank 1 and 2 on both.
- Every fishbone category has at least two causes. An empty category means you stopped thinking, not that the category is irrelevant.
- Your root cause is a system or process failure, not a named person's shortcoming. If your chain ends in someone being careless, go further.
- Your root cause passes the removal test, and you stated honestly which defects it does *not* explain rather than over-claiming.
- Your causal chain connects the root cause to the Lab 20 CPI decline, showing that EVM detected the symptom and RCA found the cause.
- Your action list distinguishes corrective from preventive, and contains at least one action that updates an organisational process asset so a future project inherits the lesson.
- You noticed that the failure of assumption A-07 implies the other assumptions need checking, and A-05 in particular gates go-live.
