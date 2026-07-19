# Lab 20 - Earned Value Management and Schedule Compression

| Field | Value |
| --- | --- |
| Topic | 5 - Monitor and Control the Project |
| ECO 2026 task | Process T9 - Evaluate project status; Process T6 - Plan and manage finance |
| Duration | 55 minutes |
| Consumes | Lab 13 cost baseline and time-phased PV; Lab 12 critical path and crash costs; Lab 03 escalation thresholds; Lab 18 status report formats |
| Produces | `artifacts/20-evm-calculations.md`, `artifacts/20-forecast.md`, `artifacts/20-compression-decision.md` |
| Live tool | [Statistics](https://alfredang.github.io/novastats/) for trend analysis of the CPI series |

## Objectives

- Compute every core EVM measure from the real Contoso cost baseline: CV, SV, CPI, SPI.
- Forecast completion four different ways - EAC, ETC, VAC, TCPI - and know which EAC formula applies to which situation.
- Read the CPI/SPI trend over seven periods rather than judging from a single snapshot.
- Decide between crashing and fast-tracking using the Lab 12 crash-cost data.
- Trigger the correct Lab 03 escalation and write the variance explanation.

## The formulas

Learn these as three groups. Everything in EVM is built from just PV, EV and AC.

```text
THE THREE INPUTS
  PV   Planned Value      Budgeted cost of work SCHEDULED. From the baseline.
  EV   Earned Value       Budgeted cost of work PERFORMED. What you actually
                          delivered, valued at BASELINE prices. EV is the
                          measure people get wrong - it is NOT what you spent.
  AC   Actual Cost        What you actually spent to earn that EV.
  BAC  Budget at Completion   Total PV for the whole project.

VARIANCES - a difference, in dollars. Negative is bad.
  CV = EV - AC            Cost variance
  SV = EV - PV            Schedule variance (in DOLLARS, not days)

INDICES - a ratio, dimensionless. Below 1.0 is bad.
  CPI = EV / AC           Cost performance index. "Value per dollar spent."
  SPI = EV / PV           Schedule performance index. "Progress vs plan."

FORECASTS
  EAC = BAC / CPI         Use when current variances are TYPICAL and will
                          continue. This is the default and the most tested.
  EAC = AC + (BAC - EV)   Use when the variance is ATYPICAL, a one-off that
                          will not recur. Remaining work at budgeted rate.
  EAC = AC + [(BAC - EV) / (CPI x SPI)]
                          Use when you must hit the original DATE and both
                          cost and schedule pressure persist. Most pessimistic.
  ETC = EAC - AC          Estimate to complete. What is still to be spent.
  VAC = BAC - EAC         Variance at completion. Negative = overrun forecast.

  TCPI = (BAC - EV) / (BAC - AC)    to hit the ORIGINAL budget
  TCPI = (BAC - EV) / (EAC - AC)    to hit the CURRENT forecast
         Efficiency you must achieve on remaining work.
         TCPI above 1.0 means you must perform BETTER than planned to recover.
         Compare TCPI to current CPI: if TCPI is far above CPI, recovery is
         not credible and you should re-baseline or cut scope.

MEMORY AID
  Everything starts with EV. If the formula is a variance, SUBTRACT. If it is
  an index, DIVIDE. AC goes with cost, PV goes with schedule - in both.
```

## Steps

### Step 1 - Take the Contoso baseline and actuals

This is the real time-phased cost baseline from Lab 13, together with the measured EV and AC at each fortnightly reporting point. The project is at the end of week 14, which is the end of sprint 7 of 12.

```text
BAC (Budget at Completion)  =  SGD 480,000
Status date                 =  End of week 14 (end of sprint 7)
Reporting period            =  Fortnightly, aligned to sprint boundaries
```

| Period | Week | PV this period | Cumulative PV | EV this period | Cumulative EV | AC this period | Cumulative AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 24,000 | 24,000 | 23,000 | 23,000 | 22,500 | 22,500 |
| 2 | 4 | 31,000 | 55,000 | 30,000 | 53,000 | 30,000 | 52,500 |
| 3 | 6 | 38,000 | 93,000 | 37,000 | 90,000 | 39,000 | 91,500 |
| 4 | 8 | 42,000 | 135,000 | 40,000 | 130,000 | 44,000 | 135,500 |
| 5 | 10 | 45,000 | 180,000 | 41,000 | 171,000 | 47,500 | 183,000 |
| 6 | 12 | 44,000 | 224,000 | 40,000 | 211,000 | 46,000 | 229,000 |
| 7 | 14 | 44,000 | **268,000** | 38,000 | **249,000** | 42,000 | **271,000** |
| 8 | 16 | 42,000 | 310,000 | | | | |
| 9 | 18 | 40,000 | 350,000 | | | | |
| 10 | 20 | 46,000 | 396,000 | | | | |
| 11 | 22 | 46,000 | 442,000 | | | | |
| 12 | 24 | 38,000 | 480,000 | | | | |

Confirm the baseline is sound before you compute anything:

```text
Sum of all PV periods = 24 + 31 + 38 + 42 + 45 + 44 + 44 + 42 + 40 + 46 + 46 + 38
                      = 480  (thousand)
Cumulative PV at period 12 = BAC = SGD 480,000.  Correct.

If cumulative PV at the end does not equal BAC, your baseline is broken and
every forecast built on it is meaningless. Always check this first.
```

### Step 2 - Compute the variances and indices at week 14

Work these by hand before checking. Use the cumulative figures - EVM is always cumulative unless a question explicitly says "this period".

```text
GIVEN at week 14:   PV = 268,000    EV = 249,000    AC = 271,000    BAC = 480,000

COST VARIANCE
  CV = EV - AC = 249,000 - 271,000 = -SGD 22,000
  Negative: we have spent SGD 22,000 more than the work delivered was worth.

SCHEDULE VARIANCE
  SV = EV - PV = 249,000 - 268,000 = -SGD 19,000
  Negative: we have delivered SGD 19,000 less work than was scheduled.

COST PERFORMANCE INDEX
  CPI = EV / AC = 249,000 / 271,000 = 0.9188  ->  0.919
  Every SGD 1.00 spent is buying SGD 0.92 of work.

SCHEDULE PERFORMANCE INDEX
  SPI = EV / PV = 249,000 / 268,000 = 0.9291  ->  0.929
  We are progressing at 93% of the planned rate.
```

Interpret before forecasting:

| Measure | Value | Reading |
| --- | --- | --- |
| CV | -22,000 | Over budget |
| SV | -19,000 | Behind schedule |
| CPI | 0.919 | 8.1% cost inefficiency |
| SPI | 0.929 | 7.1% behind planned progress |

```text
Both negative, both indices below 1.0. This is the "over budget AND behind
schedule" quadrant - the worst of the four combinations.

A caution the exam tests: SV and SPI are measured in DOLLARS, not time.
SV = -19,000 does NOT mean "19,000 days late". It means the work delivered is
worth 19,000 less than the work scheduled. To convert to time you need the
schedule itself, or earned schedule analysis. And note that SPI always drifts
back to 1.0 at project completion, because at the end EV = PV = BAC by
definition - which is why SPI is unreliable late in a project and the critical
path (Lab 12) is the better late-stage schedule measure.
```

### Step 3 - Forecast the outcome

Compute all three EAC variants, then choose the defensible one.

```text
EAC 1 - variances are TYPICAL (the default)
  EAC = BAC / CPI = 480,000 / 0.9188 = SGD 522,420
  (Using the unrounded CPI. With CPI rounded to 0.919: 522,307. Carry at least
   four decimal places - rounding CPI early is a common source of error.)

EAC 2 - variance is ATYPICAL, a one-off that will not recur
  EAC = AC + (BAC - EV) = 271,000 + (480,000 - 249,000)
      = 271,000 + 231,000 = SGD 502,000

EAC 3 - must hit the original date, both pressures persist
  EAC = AC + [(BAC - EV) / (CPI x SPI)]
      = 271,000 + [231,000 / (0.9188 x 0.9291)]
      = 271,000 + [231,000 / 0.8537]
      = 271,000 + 270,588 = SGD 541,588

ETC (using EAC 1)
  ETC = EAC - AC = 522,420 - 271,000 = SGD 251,420

VAC (using EAC 1)
  VAC = BAC - EAC = 480,000 - 522,420 = -SGD 42,420
  A forecast overrun of SGD 42,420.

TCPI to hit the ORIGINAL budget of 480,000
  TCPI = (BAC - EV) / (BAC - AC) = (480,000 - 249,000) / (480,000 - 271,000)
       = 231,000 / 209,000 = 1.1053

TCPI to hit the CURRENT forecast EAC of 522,420
  TCPI = (BAC - EV) / (EAC - AC) = 231,000 / 251,420 = 0.9188
```

Now the judgement, which matters more than the arithmetic:

```text
WHICH EAC DO WE USE?

Look at the CPI trend in Step 4 before deciding. If CPI has been declining
steadily for six periods, the variance is plainly TYPICAL - it is a systemic
condition, not an accident. EAC 1 (522,420) is the defensible forecast.

EAC 2 (502,000) would only be justified if you could name a specific one-off
cause that has been closed out. "We hope it improves" is not a cause.
Choosing EAC 2 without that evidence is the most common way project managers
under-report a forecast overrun.

THE TCPI REALITY CHECK
  To finish at the original SGD 480,000 we must run at TCPI = 1.105 for all
  remaining work - that is, 10.5% MORE efficient than budgeted.
  Our demonstrated efficiency to date is CPI = 0.919.
  We are being asked to improve performance by 20 percentage points, having
  never once hit 1.0 in seven periods.

  RULE OF THUMB: if TCPI exceeds CPI by more than about 0.10, recovery to the
  original budget is not credible. Here the gap is 0.186. Recovery is not
  credible. Say so plainly rather than promising it.
```

### Step 4 - Analyse the trend, not the snapshot

A single period tells you little. Compute CPI and SPI for every period and look at the direction.

| Period | Week | Cum PV | Cum EV | Cum AC | CPI | SPI |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 24,000 | 23,000 | 22,500 | 1.022 | 0.958 |
| 2 | 4 | 55,000 | 53,000 | 52,500 | 1.010 | 0.964 |
| 3 | 6 | 93,000 | 90,000 | 91,500 | 0.984 | 0.968 |
| 4 | 8 | 135,000 | 130,000 | 135,500 | 0.959 | 0.963 |
| 5 | 10 | 180,000 | 171,000 | 183,000 | 0.934 | 0.950 |
| 6 | 12 | 224,000 | 211,000 | 229,000 | 0.921 | 0.942 |
| 7 | 14 | 268,000 | 249,000 | 271,000 | 0.919 | 0.929 |

Open the [Statistics](https://alfredang.github.io/novastats/) tool and enter the CPI series to confirm the trend:

```text
Enter this data series, labelled "CPI by period":
  1.022, 1.010, 0.984, 0.959, 0.934, 0.921, 0.919

Ask the tool for:
  - Mean and standard deviation
  - A linear trend line and its slope

What you should observe:
  The series declines monotonically across all seven periods. There is not a
  single period of recovery. The slope is approximately -0.018 per period.

  Naive extrapolation to period 12 (five more periods):
    0.919 + (5 x -0.018) = 0.829
  If nothing changes, CPI heads toward 0.83, giving
    EAC = 480,000 / 0.829 = SGD 579,000
  which is far worse than the 522,420 forecast from today's CPI.
```

```text
THE MANAGEMENT POINT

A monotonic seven-period decline with no recovery is not noise. It is a
systemic cause, and it will not fix itself. This is exactly the signal that
Lab 21 root cause analysis and Lab 22 control charts exist to investigate.

Contrast: had CPI gone 1.02, 0.94, 1.01, 0.97, 1.03, 0.95, 0.92 - the same
endpoint but oscillating - that would be common-cause variation and the
correct response would be to leave the process alone. Reacting to a single bad
period in a stable process is tampering, and Lab 22 shows it makes things
worse. Trend, not snapshot.
```

### Step 5 - Check the escalation threshold

Go back to your Lab 03 escalation thresholds and apply them. This is the step that converts analysis into required action.

```text
LAB 03 THRESHOLD:
  "Cost variance worse than -5% of BAC (i.e. over SGD 24,000 overrun)
   -> escalate to Project Board within 5 working days"
  "Cost variance worse than -10% of BAC (over SGD 48,000)
   -> Project Board + Finance Director within 2 working days"

CURRENT POSITION
  CV = -22,000, which is -4.58% of BAC.  Just UNDER the -5% trigger.
  BUT the FORECAST VAC = -42,420, which is -8.84% of BAC.

THE DECISION
  A literal reading says no escalation is required yet: the actual CV has not
  breached -5%.

  That reading is wrong, and knowing why is the point of this step. The
  threshold exists to give the Board time to act. Waiting until the actual
  variance breaches -5% - which the trend says happens within one period -
  removes the Board's ability to do anything useful. The forecast breaches the
  -5% level already and approaches the -10% level.

  CORRECT ACTION: escalate now, on the FORECAST, with the trend evidence and
  a set of options. A project manager who reports "we are within threshold"
  while holding a seven-period monotonic decline and a -8.84% forecast is
  technically compliant and professionally negligent.
```

### Step 6 - Decide: crash or fast-track

The Board asks how the schedule position (SPI 0.929) will be recovered. You have two levers, and they fail in different ways.

```text
CRASHING
  Add resources to critical path activities to shorten duration.
  ALWAYS increases cost. Often increases risk mildly.
  Only works on the CRITICAL PATH - adding people to a non-critical activity
  buys nothing but cost. (Lab 12 gave you the critical path; use it.)
  Subject to diminishing returns and Brooks' law: adding people to a late
  task makes it later, because of ramp-up and communication overhead
  (Lab 18's N(N-1)/2).
  Choose the activity with the LOWEST COST PER DAY SAVED.

FAST-TRACKING
  Perform sequential activities in parallel or overlap them.
  Usually costs little or nothing directly.
  ALWAYS increases RISK, and typically causes REWORK.
  Only possible where the dependency is DISCRETIONARY (soft logic).
  You cannot fast-track a MANDATORY dependency - that is physics or law,
  not preference.
```

Here are the crash options for the remaining critical path activities, from the Lab 12 network:

| Activity | Normal duration | Crash duration | Max days saved | Normal cost | Crash cost | Cost per day saved | On critical path? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| J - Communications engine build | 20 d | 16 d | 4 | 62,000 | 74,000 | **3,000** | Yes |
| L - Payments v2 integration | 15 d | 12 d | 3 | 48,000 | 61,500 | **4,500** | Yes |
| M - Data migration | 12 d | 9 d | 3 | 34,000 | 46,000 | **4,000** | Yes |
| N - Compliance review | 15 d | 15 d | 0 | 28,000 | - | Cannot crash | Yes |
| O - UAT | 10 d | 8 d | 2 | 18,000 | 25,000 | **3,500** | Yes |
| F - Trainer briefing pack | 8 d | 5 d | 3 | 9,000 | 13,500 | 1,500 | No - 20 d float |

Work the decision:

```text
TASK: recover 5 days on the critical path at minimum cost.

STEP A - eliminate the non-options.
  F is cheapest per day at 1,500 - and completely useless. It has 20 days of
  float and is not on the critical path. Crashing it shortens nothing.
  This is the classic distractor: the cheapest option is not on the
  critical path.

  N (compliance review) cannot be crashed. The DPO review is a fixed external
  process; adding money does not make the regulator faster.

STEP B - rank the genuine options by cost per day saved.
  J   3,000/day   up to 4 days
  O   3,500/day   up to 2 days
  M   4,000/day   up to 3 days
  L   4,500/day   up to 3 days

STEP C - buy the 5 days cheapest first.
  4 days from J  @ 3,000 = 12,000
  1 day  from O  @ 3,500 =  3,500
  TOTAL          5 days  = SGD 15,500

  Check: is there a cheaper combination? Any substitution replaces a
  3,000 or 3,500 day with a 4,000 or 4,500 day. No. 15,500 is optimal.

STEP D - the trap. After crashing J by its full 4 days, RE-CHECK the network.
  Shortening the critical path by 4 days may make a near-critical path
  become critical. From Lab 12, path 2 had only 8 days of float. Crashing 5
  days off the critical path leaves that path with 3 days of float - it is
  now near-critical and must be monitored. Crash 9 days and path 2 becomes
  the new critical path, at which point further crashing of J buys nothing.
  ALWAYS recompute the critical path after every crash decision.
```

Now the fast-tracking option, and why it is refused here:

```text
FAST-TRACK CANDIDATE
  Run the compliance review (N) in parallel with UAT (O), saving 10 days
  at no direct cost.

  REJECT. Two reasons, and the first is decisive:

  1. Lab 03's lessons-learned entry, from project PRJ-2021-114, records
     exactly this being done before: "UAT started before the compliance
     review was complete. Compliance findings forced rework of the
     consent-capture screens after UAT sign-off, costing 11 days and
     SGD 26,000." Fast-tracking here has a documented failure history at
     this organisation, with a cost larger than the 15,500 crash.

  2. The dependency is MANDATORY, not discretionary. The compliance gate G3
     governs go-live. You cannot validate against a design the DPO may
     require you to change.

  RECOMMENDATION: crash J by 4 days and O by 1 day for SGD 15,500, funded
  from the SGD 26,000 contingency reserve, which the PM controls under the
  Lab 06 charter authority. Do not fast-track the compliance dependency.

  Note the reserve consequence: this consumes 15,500 of the 26,000
  contingency, leaving 10,500 for all remaining risk. Report that.
```

### Step 7 - Write the variance report

Use the Lab 18 sponsor format. State the position, the cause, the action and the ask.

```text
COST AND SCHEDULE VARIANCE REPORT - Week 14 (end of sprint 7)
Contoso Training Portal Upgrade

POSITION
  Budget at completion            SGD 480,000
  Spent to date                   SGD 271,000
  Value of work delivered         SGD 249,000
  Cost variance                   -SGD 22,000  (-4.6% of budget)
  Schedule variance               -SGD 19,000
  Cost performance index          0.919
  Schedule performance index      0.929
  Forecast final cost (EAC)       SGD 522,420
  Forecast overrun (VAC)          -SGD 42,420  (-8.8% of budget)

TREND - the material point
  CPI has declined in every one of the seven reporting periods, from 1.022
  to 0.919, with no period of recovery. This is a systemic condition, not a
  one-off. Root cause analysis is scheduled this week (Lab 21 method) with
  early indications pointing to rework arising from defect density in the
  registration module.

CREDIBILITY OF RECOVERY
  Finishing at the original SGD 480,000 requires efficiency of TCPI = 1.105
  on all remaining work. Demonstrated efficiency to date is 0.919. We have
  not achieved 1.0 in any period. Recovery to the original budget is not
  credible and I am not going to forecast it.

ACTION TAKEN WITHIN MY AUTHORITY
  Crashing activity J by 4 days and activity O by 1 day, recovering 5 days
  on the critical path at SGD 15,500, funded from contingency reserve. This
  leaves SGD 10,500 of the SGD 26,000 reserve.
  Fast-tracking the compliance review against UAT was considered and
  rejected: the dependency is mandatory, and the same shortcut on project
  PRJ-2021-114 cost 11 days and SGD 26,000 in rework.

ESCALATION AND ASK
  The forecast variance of -8.8% exceeds the -5% Board threshold, although
  the actual variance has not yet done so. I am escalating on the forecast
  rather than waiting, so that options remain open.
  DECISION REQUIRED from the Board, by [date]:
    Option 1  Approve a ceiling variation of SGD 42,420 to Group Finance.
    Option 2  Reduce scope by approximately SGD 45,000. The two lowest-value
              Should-have items in the Lab 10 backlog are identified and
              would not affect the launch commitments or compliance.
    Option 3  Accept the overrun and re-baseline at SGD 522,420.
  My recommendation is Option 2. It protects both the ceiling and the launch
  date, and the affected scope does not touch any of the eight charter
  success criteria.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
A project has BAC 200,000, PV 90,000, EV 80,000, AC 100,000. The overrun was
caused by an emergency airfreight charge that will not recur. What is the
most appropriate EAC?

  A. 250,000
  B. 220,000
  C. 200,000
  D. 225,000

SCENARIO 2
At week 14 on Contoso, which statement is correct?

  A. The project is 19,000 dollars behind schedule, meaning about 19 days late.
  B. SPI of 0.929 means 92.9% of the project is complete.
  C. The project has delivered 249,000 of budgeted value having spent 271,000,
     and is behind the 268,000 of value it planned to have delivered.
  D. CPI of 0.919 means the project has spent 91.9% of its budget.

SCENARIO 3
A graphic-based item shows two lines over eight periods. CPI oscillates
between 0.96 and 1.04 with no direction. SPI declines steadily from 1.01 to
0.88. What should the project manager do?

  A. Investigate the cost process for a systemic problem.
  B. Investigate the schedule for a systemic problem; treat the cost
     variation as common-cause and leave it alone.
  C. Crash the critical path immediately.
  D. Re-baseline both cost and schedule.
```

Answer key:

```text
SCENARIO 1 -> B.  The variance is explicitly ATYPICAL - a one-off that will
            not recur - so use EAC = AC + (BAC - EV) = 100,000 + (200,000 -
            80,000) = 100,000 + 120,000 = 220,000.
            A is the trap: EAC = BAC/CPI = 200,000/0.8 = 250,000, which is the
            TYPICAL formula and is wrong here because the question told you the
            cause will not recur. The exam signals which formula it wants with
            the words "typical", "atypical", "will not recur", or "expected to
            continue". Read for those words before computing.
            C ignores the overrun entirely; D is not any EAC formula.

SCENARIO 2 -> C.  This is simply the correct reading of EV, AC and PV.
            A commits the standard error: SV is in DOLLARS, not days. You
            cannot convert without the schedule.
            B misreads SPI as percent complete. Percent complete is EV/BAC =
            249,000/480,000 = 51.9%, a different figure entirely.
            D misreads CPI as budget consumed. Budget consumed is AC/BAC =
            271,000/480,000 = 56.5%. Note that the project has consumed 56.5%
            of its budget to deliver 51.9% of its value - which is the overrun,
            expressed a third way.

SCENARIO 3 -> B.  Two different signals requiring two different responses.
            The CPI oscillation around 1.0 with no direction is common-cause
            variation - a stable process. Acting on it would be tampering
            (Lab 22), and would make performance worse rather than better.
            The SPI decline is monotonic across eight periods, which is a
            systemic signal warranting investigation.
            A investigates the wrong one. C acts before knowing the cause, and
            crashing costs money to fix a problem you have not diagnosed.
            D re-baselines to hide a variance rather than to understand it -
            re-baselining is a last resort, not a first response.
```

## Deliverable

Submit to `artifacts/`:

- `20-evm-calculations.md` - CV, SV, CPI and SPI at week 14 with the working shown, plus the full seven-period CPI/SPI trend table.
- The baseline validation check proving cumulative PV at period 12 equals BAC.
- `20-forecast.md` - all three EAC variants computed, a reasoned choice of which applies with justification from the trend, plus ETC, VAC and both TCPI figures.
- Your Statistics tool output for the CPI series: mean, standard deviation, trend slope, and the extrapolated period-12 CPI.
- The escalation decision with the threshold arithmetic, stating whether you escalate on actual or forecast variance and why.
- `20-compression-decision.md` - the crash analysis identifying the optimal 5-day recovery, its cost, the reserve consequence, and the documented reason for rejecting the fast-track option.
- The full variance report in sponsor format with three costed options and a recommendation.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your cumulative PV at period 12 equals SGD 480,000 exactly. If it does not, stop - every forecast downstream is invalid.
- CV = -22,000 and SV = -19,000, both negative, and you described SV in dollars rather than days.
- CPI = 0.919 and SPI = 0.929, and you carried CPI to at least four decimal places before computing EAC.
- You computed all three EAC variants and *chose* one with a stated reason drawn from the trend, rather than defaulting to the first formula you remembered.
- Your TCPI of 1.105 is compared against your CPI of 0.919, and you concluded in writing that recovery to the original budget is not credible.
- You identified the seven-period monotonic CPI decline as systemic, not noise.
- Your crash decision selected J and O for SGD 15,500, and you explicitly rejected activity F despite it being the cheapest per day - because it is not on the critical path.
- You rejected fast-tracking the compliance review and cited both the mandatory dependency and the SGD 26,000 historical rework cost.
- You stated the remaining contingency balance after the crash (SGD 10,500).
- Your escalation decision recognises that the forecast breaches the Board threshold even though the actual variance has not yet, and escalates on the forecast.
- Your variance report contains a recommendation, not just three options. Presenting options without a recommendation is not project management.
