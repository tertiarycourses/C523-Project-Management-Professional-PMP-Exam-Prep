# Lab 24 - Capstone: Integrated Project Management Plan and Mock Exam

| Field | Value |
| --- | --- |
| Topic | 6 - Close the Project |
| ECO 2026 task | All domains - People, Process, Business Environment |
| WSQ learning outcome | LO1 to LO5 - the full outcome set, assessed integratively |
| Duration | 120 minutes (Part A 50 minutes, Part B 70 minutes) |
| Consumes | Every artifact produced in Labs 01 to 23 |
| Produces | `artifacts/24-project-management-plan.md`, `artifacts/24-mock-exam-answers.md`, `artifacts/24-score-analysis.md`, `artifacts/24-exam-readiness-plan.md` |

## Objectives

- Assemble twenty-three labs of artifacts into one integrated project management plan with a complete index.
- Explain the three baselines and the performance measurement baseline, and locate each in your own work.
- Run a consistency audit that proves the numbers agree across artifacts, and record the discrepancies you find.
- Sit a 30-question mock exam in ECO 2026 format under real time pressure.
- Score by domain, compare against the published weights, and convert weakness into a specific remediation plan.
- Finalise exam-day logistics, pacing and answer-selection strategy.

---

# PART A - Consolidate the plan (50 minutes)

## The project management plan is a plan of plans

```text
WHAT THE PROJECT MANAGEMENT PLAN IS

  It is the INTEGRATED document that says how the project will be
  executed, monitored, controlled and closed. It is not one of the
  subsidiary plans; it CONTAINS them.

  It is approved by the sponsor and, once approved, it is BASELINED.
  Changing it after that requires a change request through the CCB.
  This is the difference between a plan and a document: a plan is
  change-controlled.

  Contrast with the CHARTER (Lab 06): the charter AUTHORISES and is high
  level and rarely changes. The plan DESCRIBES HOW and is detailed and
  changes through formal control.

THE THREE BASELINES - know these cold

  SCOPE BASELINE     = Scope statement + WBS + WBS dictionary
                       (Lab 06 scope boundaries, Lab 11 WBS and dictionary)
                       NOTE: three components. The commonest exam error is
                       answering "the WBS" alone.

  SCHEDULE BASELINE  = The approved version of the schedule model, with
                       approved start and finish dates
                       (Lab 12 network, CPM and approved dates)

  COST BASELINE      = The approved time-phased budget, EXCLUDING
                       management reserve but INCLUDING contingency reserve
                       (Lab 13 time-phased budget, SGD 480,000)

THE PERFORMANCE MEASUREMENT BASELINE (PMB) - heavily tested

  PMB = SCOPE baseline + SCHEDULE baseline + COST baseline, INTEGRATED.

  It is what you measure actual performance AGAINST. It is the source of
  PV in earned value management - which is why Lab 20's PV curve could
  only exist once all three baselines were approved.

  PMB INCLUDES contingency reserve. It EXCLUDES management reserve.
  Total project budget = PMB + management reserve.
  Using management reserve therefore CHANGES the PMB and requires a
  baseline change. Using contingency reserve does not.

  Memory hook, and it is worth memorising the shape:

     Total project budget
       = Management reserve
       + Cost baseline (= PMB in money terms)
           = Contingency reserve
           + Control account budgets
               = Work package budgets
                   = Activity cost estimates
```

## Steps

### Step 1 - Build the plan index

Create `artifacts/24-project-management-plan.md`. Every component must trace to the lab that produced it. Mark any component you have not produced as a gap.

| # | Plan component | Type | What it contains | Produced in | Artifact | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Project charter | Authorising document (not part of the plan, but its input) | Purpose, SC-1 to SC-8, authority, exclusions | Lab 06 | `06-project-charter.md` | |
| 2 | Development approach | Plan component | Hybrid decision with tailoring criteria | Lab 06 | `06-approach-decision.md` | |
| 3 | Scope management plan | Subsidiary plan | How scope is defined, validated and controlled | Labs 06, 11 | `11-wbs.md` | |
| 4 | Requirements management plan | Subsidiary plan | Elicitation, traceability, prioritisation | Lab 09 | `09-rtm.md` | |
| 5 | Schedule management plan | Subsidiary plan | Estimating method, network, CPM, float rules | Lab 12 | `12-network-diagram.md` | |
| 6 | Cost management plan | Subsidiary plan | Estimating, budgeting, EVM rules, reserve control | Labs 13, 20 | `13-cost-baseline.md` | |
| 7 | Quality management plan | Subsidiary plan | Standards, metrics, control charts, cost of quality | Labs 21, 22 | `22-control-chart.md` | |
| 8 | Resource management plan | Subsidiary plan | RACI, histograms, levelling/smoothing, team charter | Labs 08, 15 | `15-resource-plan.md` | |
| 9 | Communications management plan | Subsidiary plan | Channels, cadence, formats, escalation reporting | Lab 18 | `18-communication-plan.md` | |
| 10 | Risk management plan | Subsidiary plan | Categories, P-I matrix, EMV, responses, thresholds | Lab 14 | `14-risk-register.md` | |
| 11 | Procurement management plan | Subsidiary plan | Make-or-buy, contract types, vendor management | Lab 13 (vendor and non-labour cost lines), Lab 14 (gateway v2 decision tree) | `13-cost-estimates.md`, `14-emv-analysis.md` | |
| 12 | Stakeholder engagement plan | Subsidiary plan | Register, power/interest, salience, engagement matrix | Lab 07 | `07-engagement-matrix.md` | |
| 13 | Change management plan | Subsidiary plan | CCB, thresholds, change log, integrated change control | Lab 03 (bodies and thresholds), Lab 20 (CR-14 scope reduction) | `03-governance-model.md`, `03-escalation-thresholds.md` | |
| 14 | Configuration management plan | Subsidiary plan | Version control, configuration items, baselining | Lab 11 | `11-scope-baseline.md` | |
| 15 | **Scope baseline** | **Baseline** | Scope statement + WBS + WBS dictionary | Labs 06, 11 | `11-scope-baseline.md` | |
| 16 | **Schedule baseline** | **Baseline** | Approved schedule model and dates | Lab 12 | `12-schedule-baseline.md` | |
| 17 | **Cost baseline** | **Baseline** | Time-phased budget, SGD 480,000 | Lab 13 | `13-cost-baseline.md` | |
| 18 | **Performance measurement baseline** | **Integrated baseline** | Scope + schedule + cost integrated; source of PV | Labs 13, 20 | `20-evm-calculations.md` | |
| 19 | Benefits management plan | Companion document | B1-B4, owners, realisation schedule | Labs 05, 23 | `23-benefits-realisation.md` | |
| 20 | Compliance and sustainability register | Companion document | 13 requirements, PDPA, SSG, AI governance | Lab 04 | `04-compliance-register.md` | |
| 21 | Assumption and constraint log | Project document | A-01 to A-07, CON-1 to CON-6 | Lab 06 | `06-assumption-log.md` | |
| 22 | Lessons learned register | Project document | Live throughout; repository at closure | Lab 23 | `23-lessons-learned.md` | |
| 23 | Team charter | Project document | Ground rules, shared vision, working agreements | Lab 08 | `08-team-charter.md` | |
| 24 | Product backlog | Adaptive artifact | MoSCoW, Kano, story points, sprint plan | Lab 10 | `10-product-backlog.md` | |
| 25 | Closure documentation | Project document | Checklist, final report, transition plan | Lab 23 | `23-closure-checklist.md` | |

```text
THE ADAPTIVE COMPONENTS ARE PART OF THE PLAN, NOT AN ALTERNATIVE TO IT

  Contoso is HYBRID. The product backlog (Lab 10), the sprint cadence and
  the Kanban WIP limits (Lab 19) sit INSIDE this plan alongside the three
  baselines. That is what hybrid means in practice - not "some agile
  somewhere" but a documented interface between the two, which the Lab 06
  approach decision defined: the scope BASELINE is fixed at Must-have level
  and change controlled, while PRIORITY and SEQUENCE within it are the
  product owner's to change each sprint without a change request.

  If your plan index treats the backlog as outside the plan, you have
  described two projects rather than one hybrid project.
```

### Step 2 - Run the consistency audit

This is the highest-value 15 minutes in Part A. A plan whose numbers disagree with each other is not a plan; it is a folder. Check each assertion and record the result honestly.

| # | Consistency assertion | Artifact A | Artifact B | Expected | Your finding | Pass? |
| --- | --- | --- | --- | --- | --- | --- |
| A-1 | Total budget agrees | Lab 06 charter | Lab 13 cost baseline | Both SGD 480,000 | | |
| A-2 | Budget agrees with EVM BAC | Lab 13 cost baseline | Lab 20 EVM | BAC = SGD 480,000 | | |
| A-3 | Time-phased PV sums to BAC | Lab 13 | Lab 20 period 12 cumulative | Sum of 12 periods = 480,000 | | |
| A-4 | Contingency reserve consistent | Lab 06 charter | Lab 13 cost baseline | SGD 26,000, held INSIDE the ceiling | | |
| A-5 | Contingency approximates risk exposure | Lab 14 EMV total | Lab 13 contingency | EMV total approx. SGD 26,000 | | |
| A-6 | Critical path identity | Lab 12 critical path | Lab 20 crashed activities | J and O both on the Lab 12 critical path | | |
| A-7 | Crash costs agree | Lab 12 crash table | Lab 20 compression decision | J at 3,000/day, O at 3,500/day, total 15,500 | | |
| A-8 | Reserve after crash | Lab 20 | Lab 23 final report | 26,000 - 15,500 = 10,500 remaining at week 14 | | |
| A-9 | Requirements trace forward | Lab 09 RTM | Lab 10 backlog | Every Must-have requirement has at least one backlog item | | |
| A-10 | Backlog traces to WBS | Lab 10 backlog | Lab 11 WBS | Every backlog epic maps to a WBS branch | | |
| A-11 | WBS traces to RACI | Lab 11 WBS | Lab 15 RACI | Every RACI row cites a real WBS code | | |
| A-12 | Team size consistent | Lab 08 team charter | Lab 15 RACI columns | 9 people; Dev Lead counted within the 4 developers | | |
| A-13 | Sprint capacity consistent | Lab 10 backlog | Lab 06 constraint CON-4 | 34 story points/sprint, 12 sprints | | |
| A-14 | Compliance count consistent | Lab 04 register | Lab 09 RTM | 13 compliance requirements in both | | |
| A-15 | Stakeholder IDs stable | Lab 07 register | Labs 15, 18, 23 | S-01 to S-17 used consistently; no renumbering | | |
| A-16 | Excluded scope stays excluded | Lab 06 OUT-1 | Lab 10 backlog | AI recommender (approx. 55 points) NOT in the sprint plan | | |
| A-17 | Success criteria measured | Lab 06 SC-1 to SC-8 | Lab 23 final report | All 8 reported with an actual figure | | |
| A-18 | Benefits carried through | Lab 05 B1-B4 | Lab 23 benefits handover | Total SGD 736,099 planned; each benefit owned | | |
| A-19 | Gate dates consistent | Lab 06 milestones | Lab 12 schedule | G1 week 6, G2 week 18, G3 week 24, go-live week 26 | | |
| A-20 | Root cause traces to assumption | Lab 21 5 Whys | Lab 06 assumption log | A-07 is the assumption that failed | | |

Worked examples of two audits, so you know the standard expected:

```text
AUDIT A-3 - DOES THE TIME-PHASED PV SUM TO BAC?

  Lab 13 / Lab 20 period PV, in thousands:
    24 + 31 + 38 + 42 + 45 + 44 + 44 + 42 + 40 + 46 + 46 + 38

  Add in pairs to reduce error:
    24 + 31 =  55
    38 + 42 =  80    running 135
    45 + 44 =  89    running 224
    44 + 42 =  86    running 310
    40 + 46 =  86    running 396
    46 + 38 =  84    running 480

  Cumulative PV at period 12 = SGD 480,000 = BAC.  PASS.

  Why this matters more than it looks: PV is the denominator of SPI and the
  basis of every forecast. If this sum were 478 or 483, every SPI in Lab 20
  would be subtly wrong and no one would notice, because the error is
  invisible in any single period.

AUDIT A-5 - DOES THE CONTINGENCY MATCH THE RISK EXPOSURE?

  This is a REASONABLENESS check, not an equality check, and knowing the
  difference is the point.

  Lab 14 computed total EMV across the quantified risks at approximately
  SGD 26,000, and Lab 13 set contingency reserve at SGD 26,000.

  PASS on reasonableness. But interrogate it rather than ticking it:

    - EMV is a probability-weighted EXPECTED value. It is not the amount
      you need if several risks actually occur. A reserve set at exactly
      EMV has roughly even odds of being insufficient.
    - Lab 23 confirms the outcome: the reserve was fully consumed to
      zero (15,500 on the crash, 10,500 on corrective actions) with ten
      weeks still to run.

  So A-5 passes the arithmetic and FAILS the judgement, and the correct
  audit entry says so. That finding is Lab 23's lesson L-10, and it is a
  better answer than a tick.
```

**Record every discrepancy you find:**

| # | Discrepancy found | Artifacts in conflict | Impact | Which is correct | Correction made |
| --- | --- | --- | --- | --- | --- |
| D-1 | | | | | |
| D-2 | | | | | |

```text
EXPECT TO FIND DISCREPANCIES. Everyone does.

  The commonest on this case study, in order of frequency:
    - Reserve arithmetic drifting after Lab 20's crash: learners write
      10,500 remaining in one artifact and 26,000 in another because the
      earlier one was never updated.
    - Story point totals in Lab 10 not matching 34 x 12 = 408 points of
      capacity.
    - RACI rows in Lab 15 citing WBS codes that do not exist in Lab 11,
      usually because a task was invented in the RACI workshop.
    - The descoped SGD 45,000 in Lab 20 not being reflected in the Lab 09
      RTM at closure, so the RTM still shows items as outstanding that
      were formally removed by CR-14.
    - Post-Lab-20 EVM figures computed from BAC 480,000 when the approved
      revised BAC is 435,000.

  Finding these is the exercise. A learner who reports "all 20 assertions
  pass" on first inspection has almost certainly not checked the arithmetic
  and has instead confirmed that both documents contain a number.

  THE PROFESSIONAL POINT: this audit is what a PMO assurance review, a
  funding audit, or a sponsor's sharp finance director does to your plan.
  Discovering the inconsistency yourself is a five-minute correction.
  Having it discovered for you at a gate is a credibility event.
```

### Step 3 - Prepare the 5-minute executive presentation

The sponsor gives you five minutes at the Board. Structure it deliberately: executives need the conclusion first.

```text
5-MINUTE EXECUTIVE PRESENTATION - Contoso Training Portal Upgrade

  SLIDE 1 - THE ANSWER FIRST (45 seconds)
    Delivered live 30 June, SGD 478,900 against a SGD 480,000 ceiling.
    Seven of eight success criteria met, one narrowly missed.
    Benefits tracking to SGD 693,570 per year against a plan of 736,099.
    Do not build to a conclusion. Executives who have to wait four
    minutes for the verdict start reading their phones at minute one.

  SLIDE 2 - PERFORMANCE AGAINST COMMITMENTS (90 seconds)
    The SC-1 to SC-8 table. Show the miss on SC-2 without softening it,
    and give the one-line reason: residual abandonment concentrates in
    the corporate bulk-booking path, which exclusion OUT-4 placed out of
    scope.
    Volunteering the miss buys you credibility for everything else on the
    slide. Being caught minimising it costs you all of it.

  SLIDE 3 - THE FINANCIAL STORY (60 seconds)
    Week 14 forecast a SGD 42,420 overrun. The Board's Option 2 scope
    reduction plus corrective action closed it. Final position 1,100
    inside the ceiling, contingency fully consumed.
    Name the Board's own decision as the cause. It was.

  SLIDE 4 - WHAT WE LEARNED THAT CHANGES THE NEXT PROJECT (60 seconds)
    One lesson, not ten. The assumption-log failure: SGD 50,760 of rework
    from an assumption logged with an owner and a date that was never
    validated. The fix is three template changes, already made.
    A Board remembers one lesson. Give them the expensive one.

  SLIDE 5 - WHAT HAPPENS NEXT AND WHAT WE NEED (45 seconds)
    Benefit owners named, reviews at 30, 90 and 180 days, first review
    30 July chaired by the sponsor.
    The ask: confirm the phase-2 decision date for the 15 descoped items.
    Never end an executive presentation without a specific ask.

  TOTAL 5 minutes. Rehearse it against a clock. Five minutes of material
  delivered in nine minutes is a failure of preparation, and the Board
  will remember the overrun rather than the content.
```

---

# PART B - Mock exam (70 minutes)

## The real exam format

```text
PMP EXAMINATION - ECO 2026 FORMAT

  QUESTIONS      180 total
                 170 SCORED + 10 UNSCORED PRETEST questions.
                 The pretest questions are indistinguishable from scored
                 ones and are scattered throughout. PMI uses them to
                 calibrate future items.
                 Consequence: a question that seems impossible or badly
                 worded may simply not count. Do not let one item derail
                 you - answer it, flag it, move on.

  TIME           240 minutes.
                 240 x 60 / 180 = 80 SECONDS per question, on average.
                 This is your pacing anchor. Memorise it.

  BREAKS         Two optional 10-minute breaks.
                 The FIRST comes after the case-study section.
                 The SECOND comes midway through the independent questions.
                 The clock STOPS during breaks. Take them both. Fatigue
                 costs more marks than ten minutes of question time.
                 You cannot return to a section once you leave it.

  DOMAIN WEIGHTS  People                  33%   (about 56 of 170 scored)
                  Process                 41%   (about 70)
                  Business Environment    26%   (about 44)

  APPROACH MIX    Approximately 40% predictive.
                  The remaining 60% is split between adaptive/agile and
                  hybrid approaches.
                  Read every scenario for its approach signals - "sprint",
                  "backlog", "product owner", "iteration" mean the agile
                  answer is likely correct; "baseline", "change request",
                  "gate", "CCB" mean the predictive answer is likely
                  correct. Contoso is HYBRID and contains both, which is
                  exactly why it is a good rehearsal.

  QUESTION TYPES  1. Multiple choice - one correct answer of four
                  2. Multiple response - "select two" or "select three";
                     NO partial credit, so all selections must be right
                  3. Matching - drag items to categories
                  4. Enhanced matching - more complex, multi-attribute
                  5. Graphic-based (NEW) - interpret a chart, diagram,
                     burndown, control chart or network
                  6. Case study - a scenario followed by several linked
                     questions, presented as a distinct section

  MARKING         No penalty for a wrong answer. NEVER leave a blank.
                  An unanswered question is a guaranteed zero; a guess is
                  a 25% chance.
```

## The mock exam

```text
INSTRUCTIONS - READ BEFORE STARTING

  30 questions. 40 MINUTES. Set a timer and do not stop it.
  That is 80 seconds per question, matching real exam pacing exactly.

  Composition, proportional to the real domain weights:
    People                10 questions   (33.3%, target 33%)
    Process               12 questions   (40.0%, target 41%)
    Business Environment   8 questions   (26.7%, target 26%)
    TOTAL                 30

  Includes 3 multiple-response items, 1 matching item, 1 graphic-based
  item, and a 4-question linked case study (Q27 to Q30).

  Do not look at the answer key until all 30 are answered. Mark any
  question you flagged, so the score analysis can separate "knew it" from
  "guessed it correctly" - those are different results with different
  remediation.
```

### Domain 1 - People (Questions 1-10)

```text
Q1  [People]
The Contoso development team is eight weeks in. Two developers openly
disagree with the Dev Lead's architecture decision in a sprint review, and
the discussion becomes heated. The business analyst tells you privately that
"the team just cannot work together". Using the Tuckman model, what is the
MOST likely stage and the MOST appropriate leadership response?

  A. Forming; provide directive leadership and clarify roles.
  B. Storming; facilitate the conflict openly, reinforce the team charter
     ground rules, and coach the team toward agreed working norms.
  C. Norming; step back and let the team self-organise.
  D. Performing; the disagreement shows a high-functioning team, so no
     action is needed.

Q2  [People] SELECT TWO
The Lab 15 RACI audit shows the business analyst is Responsible on 14 of 24
work packages and is allocated at 139% for four consecutive weeks. Which TWO
actions BEST address this? (Choose two.)

  A. Reassign Responsible designations for work packages where the business
     analyst is coordinating rather than performing analysis.
  B. Mark the business analyst as Accountable rather than Responsible on
     most of those work packages.
  C. Apply resource smoothing within available float and accept whatever
     reduction it achieves.
  D. Instruct the business analyst to prioritise better and work more
     efficiently.
  E. Remove the business analyst from the compliance evidence pack, which
     is the DPO's responsibility.

Q3  [People]
The Head of Sales, who has power and urgency but no legitimate claim on the
excluded AI recommender, emails the sponsor directly accusing the project
team of ignoring market reality. The sponsor forwards it to you asking for
your thoughts. What should you do FIRST?

  A. Reply to the sponsor with the Lab 02 scored factors and the NPV
     comparison, defending the exclusion decision.
  B. Meet the Head of Sales to understand whether anything has changed since
     the exclusion decision, then respond to the sponsor with facts and a
     recommendation.
  C. Add the AI recommender to the backlog at low priority to defuse the
     conflict.
  D. Ask the sponsor to direct the Head of Sales to use the change control
     process.

Q4  [People]
Three admin staff are the primary subject matter experts for the
registration process, and they are also the group whose manual work the
project is automating. They have attended only 5 of 14 refinement sessions.
Which statement BEST describes the project manager's obligation here?

  A. The admin staff report to the Operations Manager, so their attendance
     is not the project manager's concern.
  B. They are dependent stakeholders with a legitimate and urgent claim and
     no power to press it, so the project manager must advocate for them -
     including escalating the capacity conflict that prevents attendance.
  C. Their input should be replaced with documented process maps to avoid
     dependency on unavailable resources.
  D. They should be formally reassigned to the project team full time.

Q5  [People]
A project manager notices that a virtual team member in a different time
zone has stopped contributing in the daily standup and responds to messages
only hours later. What is the BEST first action?

  A. Escalate to the team member's functional manager.
  B. Raise the reduced participation in the next retrospective for the team
     to discuss.
  C. Speak to the team member privately to understand the cause before
     drawing a conclusion about disengagement.
  D. Reassign the team member's work to a co-located member.

Q6  [People] SELECT TWO
Which TWO of the following are characteristics of a servant-leadership
approach as applied on a hybrid project? (Choose two.)

  A. Removing impediments that the team has raised so the team can deliver.
  B. Assigning tasks to individuals daily and tracking their completion.
  C. Coaching the team to make its own decisions within agreed boundaries.
  D. Approving all technical decisions personally to ensure quality.
  E. Escalating every team disagreement to the sponsor for resolution.

Q7  [People]
The QA lead and the Dev Lead disagree on whether a defect is severity 2 or
severity 3. The disagreement has stalled the sprint review for twenty
minutes. The launch date is fixed and the decision affects whether the item
blocks the release. Which conflict resolution approach is MOST appropriate?

  A. Smoothing - emphasise the areas of agreement and move on.
  B. Withdrawal - defer the decision to the next sprint.
  C. Collaborating/problem solving - work through the severity definition
     together and reach a decision both accept on the evidence.
  D. Forcing - the project manager decides, because time is short.

Q8  [People]
During the closing retrospective a team member says the project failed
because "management never gave us the SMEs we needed". Others begin to
agree, and the discussion turns to blame. What should the project manager do?

  A. Agree, since the root cause analysis confirmed SME availability was the
     issue, and record it as management failure.
  B. Restate the retrospective prime directive, redirect the group from
     attribution to root cause using the 5 Whys, and drive toward the
     artifact change that would prevent recurrence.
  C. End the retrospective and reschedule when emotions have settled.
  D. Remind the team that the project finished within budget and on time.

Q9  [People]
A newly assigned team member has strong technical skills but has never
worked on a project with formal compliance gates and is visibly frustrated
by the evidence documentation required. Applying situational leadership,
what is the MOST appropriate approach?

  A. Delegating - the member is technically skilled, so give them autonomy.
  B. Directing/coaching - the member has high competence in the technical
     task but low competence and low commitment in this specific
     compliance context, so provide structure and explain the why.
  C. Supporting - provide encouragement without changing the task.
  D. Reassign the compliance documentation to someone who is willing.

Q10 [People]
The project manager wants to increase the admin staff's engagement level
from Neutral to Supportive. Which action is MOST likely to achieve this?

  A. Send a weekly written update explaining project progress.
  B. Agree and communicate the redeployment plan in writing before the
     automation becomes visible, and involve them as SMEs with protected,
     capped hours so they shape the tool.
  C. Invite them to the sprint review as observers.
  D. Ask the Operations Manager to instruct them to support the project.
```

### Domain 2 - Process (Questions 11-22)

```text
Q11 [Process]
At week 14 the project has BAC 480,000, PV 268,000, EV 249,000 and
AC 271,000. The CPI has declined in every one of the seven reporting
periods. What is the MOST defensible EAC?

  A. 480,000, because corrective action will recover performance.
  B. 502,000, using EAC = AC + (BAC - EV).
  C. 522,420, using EAC = BAC / CPI.
  D. 541,588, using EAC = AC + [(BAC - EV) / (CPI x SPI)].

Q12 [Process]
Using the same data as Q11, the project manager computes TCPI to hit the
original budget as 1.105 against a current CPI of 0.919. What does this
MOST importantly tell the project manager?

  A. The project will finish 10.5% over budget.
  B. Remaining work must be performed 10.5% more efficiently than budgeted,
     against demonstrated efficiency of 0.919, so recovery to the original
     budget is not credible and should not be forecast.
  C. The project should immediately crash the critical path.
  D. The cost baseline should be revised to 522,420.

Q13 [Process]
The project must recover five days on the critical path. Activity F can be
crashed at SGD 1,500 per day and has 20 days of float. Activity J can be
crashed at SGD 3,000 per day for up to 4 days and is on the critical path.
Activity O can be crashed at SGD 3,500 per day for up to 2 days and is on
the critical path. What is the correct action and cost?

  A. Crash F for 5 days at SGD 7,500, the lowest cost option.
  B. Crash J for 4 days and O for 1 day, at SGD 15,500.
  C. Crash J for 4 days and F for 1 day, at SGD 13,500.
  D. Crash O for 2 days and J for 3 days, at SGD 16,000.

Q14 [Process] GRAPHIC-BASED
A project performance chart shows the following two series across eight
reporting periods:

    Period    1     2     3     4     5     6     7     8
    CPI     1.03  0.97  1.04  0.96  1.02  0.98  1.03  0.97
    SPI     1.01  0.99  0.97  0.95  0.93  0.91  0.89  0.87

Both series end below 1.0. What should the project manager conclude?

  A. Both cost and schedule performance are deteriorating and both require
     corrective action.
  B. The cost variation is common-cause variation within a stable process
     and should not be acted upon; the schedule shows a monotonic decline
     that is a systemic signal requiring root cause investigation.
  C. The project should be re-baselined for both cost and schedule.
  D. Cost performance is the more urgent problem because CPI ended at its
     lowest value in the series.

Q15 [Process]
A change request is raised to add a feature valued at SGD 8,000 with no
impact on the critical path. The project manager's charter authority permits
approving changes under SGD 10,000 with no critical-path impact. What should
the project manager do?

  A. Approve it, since it falls within the delegated authority.
  B. Assess the impact across scope, schedule, cost, quality, risk and
     resources; take the decision through the CCB per the change management
     plan; and if approved, update the affected baselines and communicate.
  C. Reject it as scope creep.
  D. Escalate it to the sponsor because all changes require sponsor
     approval.

Q16 [Process] SELECT TWO
Which TWO statements about the performance measurement baseline are
correct? (Choose two.)

  A. The PMB integrates the scope, schedule and cost baselines.
  B. The PMB includes management reserve.
  C. The PMB includes contingency reserve.
  D. The PMB is the same as the cost baseline plus management reserve.
  E. Changes to the PMB may be made by the project manager without a change
     request when contingency is used.

Q17 [Process]
The compliance review is a mandatory predecessor to UAT execution. The
project is five days behind schedule. A team member proposes running the
compliance review in parallel with UAT to recover ten days at no direct
cost. What should the project manager do?

  A. Approve it, since fast-tracking costs nothing and recovers more time
     than crashing.
  B. Refuse it: the dependency is mandatory, and organisational lessons
     learned record that this exact shortcut previously caused 11 days and
     SGD 26,000 of rework.
  C. Approve it but add a risk to the register.
  D. Approve it if the DPO agrees to accept the risk.

Q18 [Process]
Which of the following BEST describes the difference between resource
levelling and resource smoothing?

  A. Levelling is applied to people and smoothing is applied to equipment.
  B. Levelling adjusts activities within available float and cannot change
     the critical path; smoothing may delay activities beyond their float.
  C. Levelling may delay activities beyond their float and can change the
     critical path and the end date; smoothing works only within float and
     does not change the critical path.
  D. Both techniques guarantee that resource over-allocation is eliminated.

Q19 [Process]
Quality control testing confirms all deliverables meet the written
specification. What is the correct NEXT process, and who performs it?

  A. Validate Scope, performed by the customer or sponsor, producing
     accepted deliverables.
  B. Control Quality, performed by QA, producing verified deliverables.
  C. Close Project, performed by the project manager.
  D. Validate Scope, performed by the QA lead, since QA has verified the
     deliverables.

Q20 [Process] MATCHING
Match each artifact to the baseline or plan component it forms part of.
Each item is used once.

  ITEMS
    1. WBS dictionary
    2. Time-phased budget excluding management reserve
    3. Approved schedule model with start and finish dates
    4. Risk probability and impact matrix

  CATEGORIES
    W. Scope baseline
    X. Schedule baseline
    Y. Cost baseline
    Z. Risk management plan

Q21 [Process]
Sprint planning has consistently accepted stories that did not meet
refinement criteria, because refinement sessions produce only 22 ready story
points against a team capacity of 34. Defects and rework are increasing.
What is the MOST effective corrective action?

  A. Increase team capacity by adding developers to the sprint.
  B. Enforce a Definition of Ready so that only refined stories enter the
     sprint, and resolve the refinement capacity constraint causing the
     shortfall.
  C. Reduce the sprint commitment to 22 points to match refinement output.
  D. Increase testing effort to catch the defects before release.

Q22 [Process]
A risk in the register has an EMV of SGD 12,000. The project manager
purchases insurance covering the financial consequence for a premium of
SGD 3,000. Which risk response strategy has been used?

  A. Mitigate
  B. Avoid
  C. Transfer
  D. Accept
```

### Domain 3 - Business Environment (Questions 23-26 and case study 27-30)

```text
Q23 [Business Environment]
An assumption was recorded in the assumption log with a named owner and a
validation date, and was never validated or escalated. It later caused
SGD 50,760 of rework. Which organisational process asset change would MOST
effectively prevent recurrence?

  A. Instruct project managers to take assumption validation more seriously.
  B. Add an overdue-assumption validation section to the standard status
     report template and an assumption-validation question to the gate
     review checklist, so overdue items become visible automatically.
  C. Remove assumptions from the project documentation set, since they are
     unreliable.
  D. Require all assumptions to be converted into risks at project start.

Q24 [Business Environment]
The project delivered every deliverable on time and within budget, and the
final report was accepted. Six months later the expected annual savings
cannot be traced in the operating budget. What is the MOST likely failure?

  A. The deliverables were defective.
  B. Benefits were not transferred to named business owners with a
     measurement method and scheduled reviews extending beyond closure.
  C. The project manager should have remained assigned until benefits were
     realised.
  D. The business case was fraudulent.

Q25 [Business Environment] SELECT TWO
The Contoso project must comply with PDPA requirements for learner personal
data and with SSG requirements for funding claim records. Which TWO actions
BEST demonstrate appropriate compliance management? (Choose two.)

  A. Involve the Data Protection Officer in privacy-by-design workshops
     during early sprints rather than presenting finished screens at the
     compliance gate.
  B. Complete all development first, then allocate a compliance remediation
     sprint before go-live.
  C. Maintain a compliance register mapping each of the 13 requirements to
     the specific evidence and the test that demonstrates it.
  D. Delegate all compliance decisions to the legal department to remove
     the burden from the project team.
  E. Treat compliance requirements as Should-have items so they can be
     traded if the schedule comes under pressure.

Q26 [Business Environment]
A PESTLE and TECOP environment scan performed in week 1 correctly identified
that the project's subject matter experts were already fully committed to
existing operational work. No action was taken, and this factor later became
the project's largest source of rework. What does this MOST indicate about
the organisation's process?

  A. The scan was performed incorrectly and the finding was invalid.
  B. Environment scanning produces findings but the process lacks a
     mandatory disposition step requiring each significant factor to become
     a risk, an assumption with a validation date, or a documented
     acceptance.
  C. Environment scans are of limited value and should be discontinued.
  D. The project manager should have escalated the scan to the Board.

CASE STUDY - Questions 27 to 30
Read the scenario, then answer the four linked questions.

  Contoso Learning is at week 15 of the 28-week Training Portal Upgrade.
  At week 14 earned value analysis showed CPI 0.919 and SPI 0.929, with a
  forecast EAC of SGD 522,420 against a board-approved ceiling of
  SGD 480,000 - a forecast overrun of SGD 42,420, or 8.8%.

  The escalation thresholds require Board escalation when cost variance is
  worse than -5% of BAC. The actual cost variance is -SGD 22,000, which is
  -4.58% - just inside the threshold. The project manager escalated anyway,
  on the forecast, presenting three costed options: a ceiling variation of
  SGD 42,420; a scope reduction of approximately SGD 45,000 by dropping the
  two lowest-value Should-have items; or accepting the overrun and
  re-baselining.

  Root cause analysis has identified that assumption A-07, that three admin
  staff would be available as subject matter experts, was recorded with an
  owner and a validation date and was never validated. The SMEs attended 5
  of 14 refinement sessions because they remained committed to 24 hours per
  week of manual communications work. Refinement produced 22 ready story
  points against a capacity of 34, sprint planning accepted incomplete
  stories, and the resulting defects consumed 655 rework hours costing
  SGD 50,760.

  The launch date of 30 June is fixed by the July intake enrolment window.
  The contingency reserve stood at SGD 26,000 and SGD 15,500 has already
  been committed to crashing two critical path activities.

Q27 [Case study]
Was the project manager's decision to escalate on the forecast variance,
rather than waiting for the actual variance to breach the threshold,
appropriate?

  A. No. The threshold is defined on actual cost variance and had not been
     breached, so escalating early undermines the governance process.
  B. Yes. The threshold exists to give the Board time to act, and waiting
     until the actual variance breached -5% would have removed options that
     were still available at week 14.
  C. No. The project manager should first have attempted recovery within
     their own authority and escalated only if that failed.
  D. Yes, but only because the forecast exceeded -5%; had it been -4.9% the
     correct action would have been to say nothing.

Q28 [Case study]
Which of the three options should the project manager RECOMMEND to the
Board, and why?

  A. The ceiling variation, because it preserves all agreed scope and the
     benefits case depends on full delivery.
  B. The scope reduction, because it protects both the ceiling and the fixed
     launch date, and the affected Should-have items do not touch any of the
     eight charter success criteria or any compliance requirement.
  C. Accepting the overrun and re-baselining, because the variance is
     systemic and the baseline is therefore no longer realistic.
  D. Present the three options without a recommendation, since the decision
     belongs to the Board.

Q29 [Case study]
Given the root cause finding, which corrective action addresses the ROOT
CAUSE rather than a symptom?

  A. Increase testing coverage to detect the defects earlier.
  B. Secure protected SME availability by backfilling the admin staff's
     manual communications workload, and enforce a Definition of Ready so
     unrefined stories cannot enter a sprint.
  C. Reduce the sprint commitment from 34 to 22 story points to match the
     refinement output.
  D. Add a developer to the team to absorb the rework hours.

Q30 [Case study]
The Board approves the scope reduction. The revised BAC becomes
SGD 435,000. EV at week 14 was SGD 249,000 and AC was SGD 271,000. The
corrective actions will cost SGD 10,500 from the remaining contingency
reserve. If the team achieves a CPI of 0.9422 on the remaining budgeted
work, what is the approximate final actual cost, and does it meet success
criterion SC-6?

  A. SGD 457,000; SC-6 met.
  B. SGD 478,900; SC-6 met, with SGD 1,100 of headroom against the ceiling.
  C. SGD 489,400; SC-6 not met, requiring a ceiling variation.
  D. SGD 522,420; SC-6 not met.
```

## Answer key with full rationale

```text
Q1 -> B.  STORMING. The identifying markers are open disagreement about
      approach and interpersonal friction emerging after the initial polite
      phase. The response is to facilitate rather than suppress: conflict
      in storming is normal and necessary, and a team that never storms
      usually has not engaged with the hard questions.
      A is wrong: forming is characterised by politeness, dependence on the
      leader and uncertainty about roles - not open confrontation. Eight
      weeks in with an established team, forming has passed.
      C is wrong and would be harmful: stepping back in storming leaves the
      conflict to resolve itself, which is how a storming team becomes a
      permanently dysfunctional one.
      D misreads the situation. Performing teams do disagree productively,
      but a heated exchange that requires a third party to report "the team
      cannot work together" is not productive disagreement.

Q2 -> A and C.  This is the Lab 15 sequence. A attacks the demand side by
      removing Responsible designations where the analyst is coordinating
      rather than performing - which is what actually resolved the Contoso
      over-allocation. C is the correct schedule-side technique given a
      fixed launch date, and the answer's phrasing "accept whatever
      reduction it achieves" is deliberately honest: smoothing is permitted
      to fail, and on Contoso it reduced the peak from 139% to 128% without
      eliminating it.
      B is wrong and makes it worse: converting R to A leaves 14 rows with
      an Accountable party and no one doing the work, which is the "no R"
      defect. It also violates the one-A-per-row rule across many rows.
      D is wrong: 320 hours of demand against 288 hours of capacity is an
      arithmetic impossibility, not an efficiency problem. Telling a person
      to work more efficiently when the plan asks for hours that do not
      exist is a failure of analysis dressed as management.
      E is wrong: the compliance evidence pack assembly is legitimately the
      analyst's work with the PM accountable, and the DPO's accountability
      is for the assessment, which is a different task after the split.

Q3 -> B.  Engage the stakeholder before responding about them. Something may
      genuinely have changed - a competitor launch, a lost contract - which
      would be new information legitimately worth assessing, and you cannot
      know without asking.
      A responds without checking, and risks defending a decision against
      facts you have not seen.
      C concedes scope quietly, which is the worst outcome: quiet acceptance
      into the backlog is still scope creep, and it rewards the escalation.
      D asks the sponsor to manage a relationship that is the project
      manager's to manage. The change control process is the right route,
      but you propose it after engaging, not instead of engaging.

Q4 -> B.  This is the salience model's dependent classification: legitimacy
      plus urgency, no power. The defining feature is that they cannot press
      their own claim, so it goes unaddressed unless someone with access
      acts for them. Note the answer includes escalating the capacity
      conflict - advocacy without action is sentiment.
      A is an abdication. Reporting lines determine who instructs them; they
      do not determine whose problem the project's SME starvation is.
      C treats a symptom and loses the tacit knowledge that is precisely
      what SMEs are for. Process maps document what people say they do, not
      the exceptions that generate the requirements.
      D is disproportionate, is not within the project manager's authority,
      and ignores that their operational work still has to be done by
      someone - which is the actual constraint.

Q5 -> C.  Understand before acting. Reduced participation has many causes -
      workload, time zone burden, illness, unclear tasks, or genuine
      disengagement - and the appropriate response differs completely
      depending on which it is.
      A escalates before you have any facts, and damages trust with a team
      member who may simply have been ill.
      B exposes an individual's performance in a group forum before you
      know the cause. Retrospectives address team process, not individual
      performance concerns.
      D solves your delivery problem while confirming the team member's
      exclusion, making the disengagement permanent.

Q6 -> A and C.  Servant leadership inverts the traditional model: the
      leader's job is to enable the team's work rather than to direct it.
      Removing impediments (A) and coaching the team to decide within
      boundaries (C) are its two most characteristic behaviours.
      B is directive command-and-control task assignment, the opposite of
      a self-organising team.
      D centralises technical authority in the project manager, which both
      removes team ownership and makes the PM a bottleneck.
      E escalates team disagreements outward rather than building the
      team's capacity to resolve them, which is the reverse of coaching.

Q7 -> C.  Collaborating/problem solving produces a decision both parties
      accept and, importantly here, clarifies the severity definition so
      the disagreement does not recur every sprint. It is the only approach
      that yields a durable win-win.
      A, smoothing, papers over a substantive technical disagreement that
      determines whether the release is blocked. The disagreement is real
      and must be resolved, not de-emphasised.
      B, withdrawal, defers a decision that gates the release. Time
      pressure makes deferral more costly, not less.
      D, forcing, is the tempting answer because the launch date is fixed.
      It resolves this instance in twenty seconds and guarantees the same
      argument next sprint, because the underlying definition remains
      ambiguous. Forcing is legitimate for genuine emergencies; a
      twenty-minute review overrun is not one.

Q8 -> B.  The prime directive - everyone did the best they could with what
      they knew - exists precisely for this moment. The retrospective's
      output must be a change to an artifact, not an attribution of fault.
      A accepts a first cause as a root cause and converts the
      retrospective into a grievance record. It also stops short: even if
      management were culpable, "management failure" changes no template
      and prevents no recurrence.
      C avoids the conversation the retrospective exists to have, and
      rescheduling rarely reduces the emotion.
      D deflects with unrelated good news, which the team will correctly
      read as the project manager refusing to engage with the problem.

Q9 -> B.  Situational leadership matches style to the follower's
      development level FOR THE SPECIFIC TASK, not to the person in
      general. High technical competence does not transfer to a compliance
      documentation task they have never done and are visibly frustrated
      by - that is low competence and low commitment, which calls for
      structure plus explanation of the rationale.
      A is the trap, and it is the commonest real-world error: judging
      development level by the person's overall seniority rather than by
      the task in front of them. Delegating here produces poor compliance
      evidence and a more frustrated engineer.
      C provides encouragement but not the structure or context the person
      actually lacks.
      D removes a development opportunity, concentrates compliance
      knowledge in fewer people, and rewards the frustration.

Q10 -> B.  The engagement gap is caused by uncertainty about job security
      and by a capacity conflict. B addresses both directly: the written
      redeployment plan removes the fear, and protected capped SME hours
      give them genuine influence over the tool. Involvement before the
      decision is what moves people from neutral to supportive; being
      informed after it does not.
      A is one-way communication about progress, which does not address
      either cause. The Lab 07 lesson is explicit that "keep informed" is
      an active strategy, and a progress email is not it.
      C offers passive observation with no influence, which can worsen
      matters by displaying the automation without addressing the
      consequence.
      D compels attendance and produces compliance, not support. Instructed
      engagement is the definition of a stakeholder who is present and
      unhelpful.

Q11 -> C.  A seven-period monotonic decline with no recovery is the
      definition of a TYPICAL variance - a systemic condition, not an
      accident - so EAC = BAC / CPI = 480,000 / 0.9188 = SGD 522,420.
      A is a hope, not a forecast. Corrective action that has not yet been
      taken and has never once produced CPI above 1.0 in seven periods is
      not a basis for a forecast.
      B applies the ATYPICAL formula, which requires you to name a
      specific one-off cause that has been closed out. There is none here,
      and choosing B is the commonest way project managers quietly
      under-report a forecast overrun.
      D is the most pessimistic formula and applies when you must hit the
      original DATE and both cost and schedule pressure persist. It is
      defensible only when schedule recovery is being forced; it is not the
      default and the question gives no such requirement.

Q12 -> B.  TCPI is the efficiency required on all REMAINING work. 1.105
      means you must be 10.5% more efficient than budgeted, having
      demonstrated 0.919 and never having reached 1.0. The rule of thumb is
      that a TCPI exceeding CPI by more than about 0.10 makes recovery not
      credible; the gap here is 0.186.
      A misreads TCPI as a completion variance. The forecast overrun is
      given by VAC = -42,420, or 8.8%, which is a different figure derived
      differently.
      C acts before the cause is known, and crashing spends money on the
      schedule when the question is about cost recovery credibility.
      D is a possible eventual consequence, but re-baselining is a last
      resort and is not what TCPI tells you. TCPI tells you whether the
      current target is achievable, not what to replace it with.

Q13 -> B.  Rank the genuine options by cost per day and buy cheapest first:
      4 days from J at 3,000 = 12,000, plus 1 day from O at 3,500 = 3,500,
      totalling SGD 15,500 for 5 days. Any substitution replaces a 3,000 or
      3,500 day with something dearer.
      A is the classic distractor and the reason this question exists: F is
      the cheapest per day and is completely useless, because with 20 days
      of float it is not on the critical path. Crashing a non-critical
      activity shortens nothing and buys only cost.
      C makes the same error for one of its five days, and its total of
      13,500 is therefore a lower price for four days of actual recovery.
      D uses J and O in the wrong proportions - it buys 2 days of the dearer
      O and only 3 of the cheaper J, costing 16,000 for the same 5 days. It
      is a valid recovery, just SGD 500 more expensive, which is exactly
      what makes it a good distractor.

Q14 -> B.  Two different signals demanding two different responses, which is
      what the graphic is testing. The CPI series oscillates around 1.0 with
      no direction - common-cause variation in a stable process. Acting on
      it is tampering, and tampering makes a stable process worse. The SPI
      series declines monotonically across all eight periods with no
      recovery, which is a systemic signal warranting root cause
      investigation.
      A treats both series identically and would trigger corrective action
      on a stable cost process.
      C re-baselines to make a variance disappear rather than to understand
      it. Re-baselining is a last resort, never a first response, and here
      it would conceal a schedule problem that is still diagnosable.
      D is the trap for anyone reading the last data point instead of the
      series. CPI's 0.97 in period 8 is within the range it has occupied
      throughout - it was 0.97 in period 2 as well. Trend, not snapshot.

Q15 -> B.  Having delegated authority does not mean bypassing integrated
      change control. Every change request is assessed for impact across all
      constraints and processed through the defined change process; the
      authority level determines WHO APPROVES, not WHETHER THE PROCESS RUNS.
      The final clauses matter too: approved changes update baselines and
      are communicated.
      A is the seductive wrong answer. It reads the authority correctly and
      skips the impact assessment, which is where you discover that a
      change with no critical-path impact still consumes sprint capacity,
      touches personal data, or affects the regression suite.
      C rejects without assessment. A change request is not scope creep;
      unassessed uncontrolled change is.
      D is factually wrong given the stated charter authority, and
      escalating everything renders delegated authority meaningless.

Q16 -> A and C.  The PMB integrates the scope, schedule and cost baselines
      (A) and includes contingency reserve (C), because contingency is part
      of the cost baseline.
      B is wrong: management reserve sits OUTSIDE the PMB. Total project
      budget = PMB + management reserve.
      D inverts the relationship it should describe and also mislabels
      management reserve as being inside.
      E is wrong on the mechanism. Using contingency reserve does NOT
      require a baseline change precisely because contingency is already
      inside the baseline - but E's claim is that the PMB is being changed,
      which is the error. Using MANAGEMENT reserve is what changes the PMB
      and requires a change request.

Q17 -> B.  Two independently sufficient reasons, and the question supplies
      both. A mandatory dependency cannot be fast-tracked - that is its
      definition, not a preference. And the organisational lessons learned
      repository records this exact shortcut costing 11 days and SGD 26,000,
      which is more than the alternative recovery would cost.
      A treats "no direct cost" as "no cost". Fast-tracking always increases
      risk and typically causes rework, and here the rework is documented
      rather than hypothetical.
      C records the risk while accepting it anyway, which converts a known
      documented failure into an accepted one. A risk register entry is not
      a mitigation.
      D asks the DPO to accept a risk on behalf of a regulator. The DPO
      cannot waive the requirement that validation occurs against a design
      the regulator has cleared, and asking them to is a governance failure.

Q18 -> C.  Levelling protects the RESOURCE and may cost you the DATE:
      activities may be delayed beyond their float, so the critical path and
      end date can change. Smoothing protects the DATE and may fail to fix
      the RESOURCE: it works only within float, so the critical path is
      preserved and the over-allocation may persist.
      A invents a distinction that does not exist. Both apply to any
      resource type.
      B states the two definitions correctly but assigns them to the wrong
      terms - it is exactly inverted, which makes it the most dangerous
      distractor for anyone who half-remembers the concepts.
      D is false for smoothing, which is explicitly permitted to leave an
      over-allocation unresolved. Recognising that smoothing can fail is a
      substantial part of understanding it.

Q19 -> A.  Control Quality has produced VERIFIED deliverables. The next
      process is Validate Scope, performed with the customer or sponsor, and
      it produces ACCEPTED deliverables plus formal sign-off. The order is
      fixed: correctness first, acceptance second.
      B describes the process that has just been completed.
      C jumps a step. Closure cannot proceed on verified-but-unaccepted
      deliverables; formal acceptance is a precondition of administrative
      closure.
      D names the right process and the wrong performer, which is the key
      distinction being tested. QA verifies against specification; QA cannot
      decide that the customer is satisfied. Acceptance authority belongs to
      the customer or sponsor.

Q20 -> 1-W, 2-Y, 3-X, 4-Z.
      1 to W: the scope baseline has THREE components - scope statement,
      WBS and WBS dictionary. Answering "the WBS" alone is the standard
      error; the dictionary is what makes the WBS executable.
      2 to Y: the cost baseline is the time-phased budget EXCLUDING
      management reserve and INCLUDING contingency reserve. The exclusion
      is the discriminating detail.
      3 to X: the schedule baseline is the approved schedule model with
      approved start and finish dates - approved being the operative word.
      An unapproved schedule is a schedule model, not a baseline.
      4 to Z: the probability and impact matrix is a component of the risk
      MANAGEMENT PLAN, which defines how risk will be managed. It is not
      the risk register, which is the output, and it is not a baseline at
      all - the common error here is assuming every listed artifact must
      belong to one of the three baselines.

Q21 -> B.  This is the Contoso root cause and its corrective action. The
      Definition of Ready gates work ENTERING the sprint, and the second
      clause resolves the refinement capacity constraint that created the
      shortfall. Addressing only one of the two would leave the cause in
      place.
      A adds capacity to a process whose constraint is upstream. More
      developers consuming 22 ready points faster does not create ready
      points, and Brooks' law suggests it makes matters worse.
      C is the plausible trap: matching commitment to refinement output
      does stop unrefined stories entering sprints, and it institutionalises
      a 35% capacity loss as permanent. It treats the constraint as a fact
      of nature rather than a problem to solve.
      D catches defects later instead of preventing them, which is the most
      expensive point in the cost-of-quality curve at which to intervene.

Q22 -> C.  TRANSFER moves the financial consequence of the risk to a third
      party, and insurance is the archetypal example. Note that transfer
      almost always carries a premium and does not reduce the probability
      of the event occurring.
      A, mitigate, reduces probability or impact through action. Buying
      insurance changes neither; the event is equally likely and equally
      damaging, it is simply someone else's bill.
      B, avoid, eliminates the threat entirely by changing the plan so the
      risk cannot occur. The risk here remains fully live.
      D, accept, means taking no action beyond possibly setting aside
      contingency. Paying a SGD 3,000 premium is an action, so this is not
      acceptance.

Q23 -> B.  A lesson changes nothing unless it changes an artifact. Making
      overdue assumptions visible automatically in the standard status
      report and the gate checklist means every future project is affected
      whether or not anyone remembers this one. That is the definition of
      an effective OPA update.
      A is an exhortation. "Take it more seriously" depends on individual
      memory and diligence, which is exactly what failed here - the
      assumption already had an owner and a date.
      C removes the control rather than fixing it, and would eliminate the
      documentation that at least made the failure diagnosable.
      D confuses two different tools. Assumptions and risks serve different
      purposes; converting all assumptions to risks floods the risk
      register and loses the validation-date mechanism that is precisely
      what needs enforcing.

Q24 -> B.  Projects deliver OUTPUTS; the business realises BENEFITS, and it
      does so after the project has closed. Without a named benefit owner,
      a measurement method and scheduled reviews beyond closure, nobody
      measures anything - and the savings may well be real but untraced.
      A does not follow: on-time, on-budget delivery of accepted
      deliverables is entirely compatible with benefits never being
      harvested. They are separate things.
      C misunderstands what a project is. Projects are temporary; the
      mechanism is transferring ownership to the permanent organisation,
      not keeping a project manager assigned for a year.
      D leaps to a conclusion with no measurement behind it. You cannot
      judge an estimate before measuring the actual.

Q25 -> A and C.  A moves compliance from an adversarial gate to a
      collaborative design input, which is both cheaper and more likely to
      pass first time. C is the traceability that makes compliance
      demonstrable - each requirement mapped to specific evidence and the
      test that proves it, which is what an assessor actually asks for.
      B is the sequence that produces late, expensive rework, and Contoso's
      own lessons repository records this pattern costing 11 days and
      SGD 26,000 on a prior project.
      D abdicates rather than delegates. Legal advises; the project team
      remains responsible for building compliant software, and a legal
      department cannot make design decisions it does not see.
      E is the most serious error offered. Regulatory requirements are not
      tradeable priorities. Classifying them as Should-have means that
      under schedule pressure - which always arrives - the project can
      legally expose the organisation by following its own prioritisation
      rules.

Q26 -> B.  The scan worked; the process around it did not. A finding with
      no mandatory disposition creates no obligation on anyone, so a
      correctly identified factor can sit in a document while the risk it
      describes materialises. The fix is a required disposition column:
      every significant factor becomes a risk, an assumption with a
      validation date, or a documented acceptance.
      A is contradicted by the facts. The scan identified the exact factor
      that later caused the largest source of rework - it was accurate.
      C draws precisely the wrong conclusion, discarding a tool that
      demonstrated its predictive value. The failure was downstream of the
      scan.
      D is too narrow and misplaces the level. Board escalation of every
      environmental factor is unworkable; the missing control is a
      systematic disposition step, not an escalation.

Q27 -> B.  The threshold exists to give the Board time to act. At week 14
      the SGD 45,000 scope reduction was still available because the
      affected items had not yet been built. Waiting one or two periods for
      the actual variance to breach -5% would have destroyed that option.
      A reads the threshold literally and misses its purpose. A project
      manager who reports "within threshold" while holding a seven-period
      monotonic decline and an -8.8% forecast is technically compliant and
      professionally negligent.
      C describes what the project manager DID do - the crash of J and O
      was recovery within their own authority - but presents it as an
      alternative to escalation. It is not either/or, and a forecast
      overrun of 8.8% of the total budget is beyond what any within-
      authority action could absorb, with only SGD 10,500 of reserve left.
      D accepts the right answer for a mechanical reason and then draws a
      false conclusion. Judgement about materiality and trend does not
      switch off at 4.9%; the seven-period decline would still warrant
      reporting.

Q28 -> B.  The scope reduction protects the two things the charter fixed -
      the SGD 480,000 ceiling and the 30 June date - and the affected items
      were specifically identified as the lowest-value Should-haves that
      touch no success criterion and no compliance requirement. That last
      test is what makes a descope legitimate rather than merely convenient.
      A protects scope at the expense of the ceiling, which constraint
      CON-2 declares to be the hard limit, and requires Group Finance
      approval for a ceiling variation. It also overstates the benefits
      dependency: the descoped items are Should-haves, and the benefits
      case rests on the Must-haves.
      C accepts an 8.8% overrun and re-baselines when a viable alternative
      preserving both the ceiling and the date exists. Re-baselining is a
      last resort.
      D is the trap that catches conscientious candidates. Presenting
      options is necessary but insufficient. The Board is entitled to the
      judgement of the person closest to the work, and options without a
      recommendation is not project management - the decision remains the
      Board's either way.

Q29 -> B.  This addresses both links in the causal chain the analysis
      identified: SME unavailability caused by the 24 hours per week of
      manual work, and the absence of an entry gate that let unrefined
      stories into sprints. Backfilling the manual work is what actually
      frees the SMEs; a Definition of Ready is what stops the consequence
      recurring while that takes effect.
      A detects defects rather than preventing them, and does nothing about
      the ambiguous acceptance criteria that generate them. It is the
      textbook symptom-level response.
      C matches commitment to the constrained output, permanently
      institutionalising a 35% loss of capacity rather than removing the
      constraint.
      D adds capacity downstream of the bottleneck. More developers
      consuming 22 ready points does not produce more ready points, and it
      increases the coordination overhead.

Q30 -> B.  Work the arithmetic:
        Revised BAC                                   435,000
        Less EV already earned at week 14            -249,000
        Budgeted work remaining                       186,000
        Actual spend on it at CPI 0.9422:
            186,000 / 0.9422                        = 197,400
        Add actual cost to date                      +271,000
        Add corrective action cost                    +10,500
        Final actual cost                             478,900

      Against the SGD 480,000 ceiling that is SGD 1,100 of headroom, so
      SC-6 ("delivered at or under SGD 480,000") is MET.
      A, 457,000, is what you get by omitting the corrective action cost
      and assuming CPI 1.0 on remaining work - the optimistic error.
      C, 489,400, comes from applying the CPI to the full revised BAC
      rather than to the REMAINING budgeted work, double-counting the work
      already earned. This is the commonest arithmetic error in EVM
      forecasting and is why the distractor is placed on the wrong side of
      the ceiling.
      D is the original week-14 EAC, which is the position BEFORE any
      corrective action - the answer for a candidate who did not notice the
      question asks for the outcome after the Board's decision.
```

## Score analysis

Create `artifacts/24-score-analysis.md`.

| Domain | Question numbers | Questions | Your correct | Your % | Real exam weight | Gap |
| --- | --- | --- | --- | --- | --- | --- |
| People | 1-10 | 10 | | | 33% | |
| Process | 11-22 | 12 | | | 41% | |
| Business Environment | 23-26, 27-30 | 8 | | | 26% | |
| **Total** | 1-30 | **30** | | | 100% | |

Track your flagged questions separately — a guess that happened to be right is not knowledge:

| Category | Count | What it means |
| --- | --- | --- |
| Correct and confident | | Genuine knowledge |
| Correct but flagged/guessed | | Fragile - treat as a gap |
| Incorrect | | Clear gap |
| Ran out of time | | Pacing problem, not a knowledge problem |

```text
PMI PROFICIENCY BANDS

  PMI does NOT publish a percentage pass mark. It reports performance per
  domain in four bands, against a psychometrically determined standard:

    ABOVE TARGET       Performance exceeds the minimum requirement
    TARGET             Performance meets the minimum requirement
    BELOW TARGET       Performance is below the minimum requirement
    NEEDS IMPROVEMENT  Performance is substantially below

  Anyone quoting "you need 61%" or "you need 175 out of 200" is repeating
  an obsolete figure from a much older exam form. There is no published
  cut score, and the pass standard is set by item difficulty rather than
  by a fixed percentage.

  PRACTICAL INTERPRETATION FOR THIS MOCK - a rough working guide only:

    80% or above    Comfortable. Likely Above Target on that domain.
    70% to 79%      Probably Target. Solid but revise the misses.
    60% to 69%      Borderline. Below Target is a real possibility.
    Below 60%       Needs Improvement. This domain needs structured work,
                    not just re-reading.

  A CAUTION THAT MATTERS MORE THAN THE BANDS
  Do not chase a single overall percentage. The exam reports by DOMAIN,
  and a candidate at 85% People, 85% Business Environment and 55% Process
  is in far more danger than the 75% average suggests - Process is 41% of
  the exam. Read your weakest domain, not your mean.

EXTRAPOLATING TO THE FULL EXAM

  Expected full-exam performance = (your 30-question score / 30) x 170
  scored questions.

  Worked example: 22 correct out of 30.
    22 / 30 = 73.3%
    0.733 x 170 = approximately 125 of 170 scored questions.

  THE SMALL-SAMPLE CAUTION - read this before you take the number seriously

  30 questions is a SMALL SAMPLE and this extrapolation is far less
  precise than the arithmetic makes it look.

    - The 95% confidence interval on a 73% score from 30 items is roughly
      plus or minus 16 percentage points. Your true ability could be
      anywhere from about 57% to 89%. That range spans Needs Improvement
      to Above Target.
    - The per-domain samples are worse. Eight Business Environment
      questions means each single question moves the domain score by 12.5
      percentage points. Getting one unlucky item wrong drops you a band.
    - Question difficulty here is not psychometrically calibrated against
      the real item bank.

  USE THIS SCORE DIAGNOSTICALLY, NOT PREDICTIVELY. It is good for
  identifying which topics you cannot reason about. It is poor at
  predicting your result. A learner scoring 60% who reads every rationale
  carefully will outperform one scoring 80% who reads only the score.

  If you want a predictive estimate, sit at least three full 180-question
  mocks under timed conditions and look at the trend across them - which
  is the same principle as Lab 20's trend-not-snapshot rule, applied to
  your own performance.
```

## Remediation plan

Create `artifacts/24-exam-readiness-plan.md`. Map every incorrect or flagged question to a lab and an ECO task.

| Q# | Domain | Topic tested | Correct? | Flagged? | Lab to revisit | ECO task to study |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | People | Tuckman stages, leadership response | | | Lab 16 | People T3, T6 |
| 2 | People | RACI defects, resource optimisation | | | Lab 15 | People T3, Process T4 |
| 3 | People | Salience, dangerous stakeholder | | | Lab 07 | People T4, T5 |
| 4 | People | Dependent stakeholders, advocacy | | | Lab 07 | People T4 |
| 5 | People | Virtual teams, engagement | | | Lab 08, Lab 16 | People T3, T11 |
| 6 | People | Servant leadership | | | Lab 08, Lab 16 | People T2, T3 |
| 7 | People | Conflict resolution modes | | | Lab 17 | People T1 |
| 8 | People | Retrospective facilitation | | | Lab 17, Lab 23 | People T1, BE T6 |
| 9 | People | Situational leadership | | | Lab 16 | People T3 |
| 10 | People | Engagement level movement | | | Lab 07, Lab 18 | People T5, T6 |
| 11 | Process | EAC selection, typical vs atypical | | | Lab 20 | Process T9, T6 |
| 12 | Process | TCPI and recovery credibility | | | Lab 20 | Process T9 |
| 13 | Process | Crashing, critical path, cost per day | | | Lab 12, Lab 20 | Process T5, T9 |
| 14 | Process | Trend analysis, common vs special cause | | | Lab 20, Lab 22 | Process T9, T8 |
| 15 | Process | Integrated change control | | | Lab 19 | Process T3, T10 |
| 16 | Process | PMB, reserves, baselines | | | Lab 13, Lab 20 | Process T1, T6 |
| 17 | Process | Fast-tracking, mandatory dependency | | | Lab 12, Lab 20 | Process T5 |
| 18 | Process | Levelling vs smoothing | | | Lab 15 | Process T4, T5 |
| 19 | Process | Validate Scope vs Control Quality | | | Lab 22, Lab 23 | Process T8, T10 |
| 20 | Process | Baseline composition (matching) | | | Lab 11, Lab 12, Lab 13 | Process T1, T2 |
| 21 | Process | Definition of Ready, flow constraint | | | Lab 19, Lab 21 | Process T7, T8 |
| 22 | Process | Risk response strategies | | | Lab 14 | Process T3 |
| 23 | Business Env | OPA updates, lessons that change artifacts | | | Lab 23 | BE T6 |
| 24 | Business Env | Benefits realisation ownership | | | Lab 05, Lab 23 | BE T1, Process T10 |
| 25 | Business Env | Compliance management | | | Lab 04 | BE T2 |
| 26 | Business Env | Environment scanning disposition | | | Lab 02 | BE T4 |
| 27 | Business Env | Escalation on forecast variance | | | Lab 03, Lab 20 | BE T3, Process T9 |
| 28 | Business Env | Options and recommendation to governance | | | Lab 20 | BE T3, Process T6 |
| 29 | Business Env | Root cause vs symptom | | | Lab 21 | BE T6, Process T8 |
| 30 | Business Env | EVM arithmetic after re-baseline | | | Lab 13, Lab 20, Lab 23 | Process T6, T9 |

```text
BUILD YOUR PERSONAL REMEDIATION PLAN

  For each domain scoring below 70%, write:

    DOMAIN:              [People / Process / Business Environment]
    SCORE:               __ / __  = __%
    QUESTIONS MISSED:    Q__, Q__, Q__
    COMMON THREAD:       What connects them? Is it one topic, or is it a
                         reading problem - answering the question you
                         expected rather than the one asked?
    LABS TO REVISIT:     Lab __, Lab __
    ECO TASKS TO STUDY:  ____ T__, ____ T__
    ACTION:              Specific and dated. "Rework Lab 20 Steps 3 and 4
                         by Friday and recompute all three EAC variants
                         without looking at the answers" is an action.
                         "Revise EVM" is not.
    RE-TEST:             Date you will re-attempt those question types.

  THE COMMON-THREAD QUESTION IS THE IMPORTANT ONE. Missing Q11, Q12 and
  Q30 is not three gaps - it is one gap in EVM forecasting. Missing Q3,
  Q4 and Q10 is one gap in stakeholder analysis. Treating a single gap as
  three separate ones wastes revision time; treating three gaps as one
  leaves two unaddressed.
```

## Exam-day readiness

```text
BEFORE THE EXAM - APPLICATION AND SCHEDULING

  ELIGIBILITY   Either a four-year degree plus 36 months of project
                leadership experience plus 35 hours of project management
                education, OR a secondary diploma plus 60 months of
                experience plus the same 35 hours. This course supplies
                the 35 contact hours.
  APPLICATION   Submitted online. PMI reviews within about 5 business
                days. Once approved you have one year of eligibility and
                up to three attempts within it.
  AUDIT         Applications are randomly selected for audit. If audited,
                you must supply evidence of your education, your
                experience with a signature from each supervisor listed,
                and your training certificate. Keep your certificate and
                your experience records now, not when you are selected.
                An audit does not mean you have done anything wrong, and
                you have 90 days to respond.
  SCHEDULING    After approval, schedule via the test delivery provider.
                Choose a TEST CENTRE or ONLINE PROCTORED.
  ID            Government-issued photo identification with a signature,
                and the name must match your PMI application EXACTLY.
                A mismatch between "Tan Wei Ming" and "Wei Ming Tan" can
                end the appointment before it starts. Check this today.

  TEST CENTRE versus ONLINE PROCTORED
    Test centre    Controlled environment, provided materials, no
                   responsibility for your own technology. Travel time
                   and a fixed location.
    Online         No travel. You must supply a private room, a clear
                   desk, an acceptable webcam and stable internet. The
                   room is scanned before you start and you may not be
                   interrupted at any point. Nobody may enter the room.
    Choose the test centre if there is ANY doubt about your home
    environment. A single interruption can void the attempt.

ON THE DAY

  Arrive or log in 30 minutes early. Late arrival forfeits the
  appointment and the fee.
  Bring the ID. Nothing else is required or permitted beyond what the
  centre provides.
  Eat properly beforehand. It is a four-hour exam and you are permitted
  only two 10-minute breaks.

THE FIRST FIVE MINUTES

  1. Complete the tutorial calmly. It is not timed against your 240
     minutes, so use it to settle rather than rushing through.
  2. BRAIN DUMP onto the provided note board or digital whiteboard, in
     this order of value:
       - The EVM formulas: CV, SV, CPI, SPI, the three EACs, ETC, VAC,
         both TCPIs
       - Levelling versus smoothing in one line each
       - The three baselines and the PMB composition
       - Contingency versus management reserve, and who controls each
       - Tuckman's five stages
       - The conflict resolution modes
       - The four risk response strategies for threats and for
         opportunities
     Keep it to 3 minutes. A brain dump that eats 15 minutes has cost you
     11 questions.
  3. Write your pacing checkpoints: at 60 minutes you should be near
     question 45; at 120 minutes near question 90; at 180 minutes near
     question 135. Check against these three times only - constant clock
     watching costs more than it saves.

PACING AND FLAGGING

  80 seconds per question, on average. Some take 20 seconds and some take
  three minutes; the average is what matters.
  If a question is still unclear after 90 seconds: choose your best
  answer, FLAG IT, and move on. Never leave it blank - there is no
  penalty for a wrong answer, so an unanswered question is a guaranteed
  zero.
  Return to flagged questions only after completing the section. You
  cannot return to a section after leaving it, so use your review time
  within the section.
  When you return to a flagged item, change your answer only if you can
  articulate a SPECIFIC reason. Changing on a vague feeling is more often
  wrong than right.

BREAK MANAGEMENT

  Take both breaks. The clock stops.
  The first comes after the case study section; the second midway through
  the independent questions.
  Stand up, drink water, look at something more than two metres away.
  Do not use the break to review questions - you cannot access them, and
  ruminating on an item you have already submitted only raises anxiety
  for the questions still ahead.

ANSWER-SELECTION HEURISTICS - from Lab 01, and they work

  1. ANSWER AS THE PMI-MINDED PROJECT MANAGER, not as you would in your
     current organisation. Assume you have authority, a functioning
     process, and a team you can talk to.
  2. UNDERSTAND BEFORE ACTING. If one option gathers information or
     engages the person concerned and another takes immediate action,
     the information-gathering option is usually correct - unless there
     is a safety or legal emergency.
  3. NEVER escalate first if you have not yet engaged the party yourself.
     Escalation is correct AFTER you have exhausted your own role.
  4. NEVER choose the option that ignores a process, hides information,
     or quietly accepts scope change.
  5. PROACTIVE beats reactive. Prevention beats detection. Root cause
     beats symptom.
  6. Watch for the words that select the formula or the approach:
     "typical", "atypical", "will not recur", "must hit the original
     date", "sprint", "backlog", "baseline", "change request".
  7. Read the LAST LINE of the question first when the stem is long. It
     tells you what is actually being asked, and long scenarios often
     contain deliberately irrelevant detail.
  8. Eliminate two options quickly, then read the remaining two against
     each other word by word. The difference between the final two is
     usually a single qualifier - "first", "best", "most likely" - and
     that qualifier is the question.
  9. On SELECT TWO items there is no partial credit. Verify both choices
     independently; a correct first choice does not make the second one
     right.
  10. If genuinely stuck, choose the option that involves the team,
      respects the process, and produces information. It is the highest
      base-rate correct answer on this exam.

FINAL READINESS CHECKLIST

  [ ] 35 contact hours certificate saved and retrievable
  [ ] Experience records documented with supervisor contacts, in case
      of audit
  [ ] PMI application submitted and approved
  [ ] Exam scheduled; date and time confirmed in writing
  [ ] Photo ID checked against the application name, character by
      character
  [ ] Test centre route timed, or online environment tested with the
      provider's system check
  [ ] At least three full 180-question timed mocks completed, with the
      score trend improving
  [ ] Every domain at Target or above on your most recent mock
  [ ] Brain dump content rehearsed to under 3 minutes
  [ ] Pacing checkpoints memorised: q45 at 60 min, q90 at 120 min,
      q135 at 180 min
  [ ] All 24 lab artifacts complete and reviewed
```

## Deliverable

Submit to `artifacts/`:

- `24-project-management-plan.md` - the complete plan index mapping all 25 components to the lab and artifact that produced each, with gaps marked, including all three baselines and the performance measurement baseline.
- A written explanation of the three baselines, the PMB, and where contingency and management reserve sit relative to each.
- The completed 20-assertion consistency audit with a pass/fail result for every row, including your own arithmetic for A-3 and your judgement on A-5.
- The discrepancy table listing every inconsistency you found, which artifact was correct, and the correction made. An audit reporting zero discrepancies must be accompanied by your shown working.
- The 5-minute executive presentation outline with timings per slide.
- `24-mock-exam-answers.md` - your answers to all 30 questions, recorded BEFORE reading the key, with flags marked.
- `24-score-analysis.md` - the per-domain scoring table with percentages, the comparison against the 33/41/26 domain weights, your confidence breakdown, and the extrapolation to 170 scored questions with the small-sample caution stated in your own words.
- `24-exam-readiness-plan.md` - the per-question remediation table completed, plus a personal remediation plan for every domain below 70% naming specific labs, specific ECO tasks, a dated action and a re-test date.
- The completed final readiness checklist.

## Checkpoint

You did this right if:

- Your plan index accounts for all three baselines separately AND the performance measurement baseline, and you did not confuse the cost baseline with the PMB.
- You can state that the scope baseline has three components, and name all three.
- You can state that the PMB includes contingency reserve and excludes management reserve, and explain why using management reserve requires a baseline change while using contingency does not.
- You actually computed the PV sum in audit A-3 rather than asserting it, and got SGD 480,000.
- Your audit of A-5 goes beyond ticking the equality and observes that a reserve set at exactly EMV was fully consumed with ten weeks remaining.
- You found and recorded at least one genuine discrepancy across your own 23 labs of artifacts. Finding none almost always means you compared the presence of numbers rather than the numbers themselves.
- You took the mock exam in 40 minutes with a timer, without stopping, and without looking at the key.
- Your answers were recorded before you read any rationale.
- You computed a per-domain percentage and compared it against 33%, 41% and 26%, rather than looking only at your overall score.
- You identified your weakest DOMAIN rather than your overall percentage, and you understand why a Process weakness is more dangerous than a People weakness of the same size.
- You can explain why extrapolating 30 questions to 180 carries a confidence interval of roughly plus or minus 16 points, and why the score is diagnostic rather than predictive.
- Your remediation plan names specific labs, specific ECO tasks, a dated action and a re-test date. "Revise EVM" is not a remediation plan.
- You identified the COMMON THREAD across your missed questions rather than treating each as a separate gap.
- You read the rationale for every question, including the ones you answered correctly - the distractor explanations are where most of the learning in this lab is.
