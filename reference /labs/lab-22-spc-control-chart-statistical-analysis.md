# Lab 22 - SPC Control Chart and Statistical Process Analysis

| Field | Value |
| --- | --- |
| Topic | 5 - Monitor and Control the Project |
| ECO 2026 task | Process T7 - Plan and optimize quality of products/deliverables; Process T9 - Evaluate project status |
| WSQ learning outcome | LO5 - Coordinate project deliverables against set objectives, costs and timelines, and implement corrective actions |
| Duration | 60 minutes |
| Consumes | Lab 21 corrective actions and their implementation date; Lab 06 success criterion SC-1; Lab 20 trend analysis method |
| Produces | `artifacts/22-control-chart.md`, `artifacts/22-stability-verdict.md`, `artifacts/22-capability-summary.md` |
| Live tools | [SPC / Control Chart](https://alfredang.github.io/novaspc/), [Statistics](https://alfredang.github.io/novastats/) |

## Objectives

- Plot a real process over time and compute control limits from the data itself.
- Apply the out-of-control rules, including the rule of seven, to detect signals.
- Separate common cause from assignable (special) cause variation, and choose the correct response to each.
- Understand why control limits and specification limits are different things, and why confusing them is expensive.
- Assess process capability against the Contoso charter target.

## The central idea

```text
EVERY PROCESS VARIES. The question is never "did it vary" but "is this
variation normal for this process, or is something new happening?"

COMMON CAUSE VARIATION
  Inherent, random, always present. The natural noise of a stable process.
  The process is PREDICTABLE - you can forecast its future range.
  CORRECT RESPONSE: do not react to individual points. If the average or
  spread is unacceptable, CHANGE THE PROCESS ITSELF. Management owns this.

ASSIGNABLE (SPECIAL) CAUSE VARIATION
  Something specific and identifiable has happened that is not part of the
  normal process. The process is UNPREDICTABLE.
  CORRECT RESPONSE: investigate, find the specific cause, act on it.

TAMPERING - the expensive mistake
  Reacting to common cause variation as if it were assignable. Adjusting a
  stable process in response to random noise. Deming demonstrated that
  tampering INCREASES variation - it makes the process worse, not better.
  A manager who demands an explanation for every point below average is
  tampering, and is actively degrading the process.

CONTROL LIMITS vs SPECIFICATION LIMITS - constantly confused, heavily tested
  CONTROL LIMITS   Calculated FROM THE PROCESS DATA. Usually mean +/- 3 sigma.
                   They tell you what the process IS capable of - the voice
                   of the process. You cannot choose them.
  SPECIFICATION LIMITS  Set by the CUSTOMER or the requirement. They tell you
                   what the process MUST achieve - the voice of the customer.
                   They have nothing to do with the data.

  A process can be perfectly IN CONTROL (stable, predictable) and still
  entirely fail to meet specification. Stable does not mean good.
  Control limits NEVER go on a chart as the spec, and spec limits NEVER
  become control limits.
```

## Steps

### Step 1 - Take the measurement data

Contoso measures median registration completion time every working day. Charter success criterion SC-1 requires the completed system to achieve under 4.0 minutes, down from the 11-minute legacy baseline.

These are 20 consecutive daily measurements taken from the staging environment during sprints 8 to 11, in minutes.

| Day | Median registration time (min) | Day | Median registration time (min) |
| --- | --- | --- | --- |
| 1 | 4.1 | 11 | 4.2 |
| 2 | 3.8 | 12 | 4.0 |
| 3 | 4.3 | 13 | 3.8 |
| 4 | 3.9 | 14 | 4.3 |
| 5 | 4.2 | 15 | 4.1 |
| 6 | 4.0 | 16 | 5.2 |
| 7 | 3.7 | 17 | 5.4 |
| 8 | 4.4 | 18 | 5.1 |
| 9 | 4.1 | 19 | 5.3 |
| 10 | 3.9 | 20 | 5.5 |

```text
IMPORTANT METHOD POINT

Control limits must be computed from a period when the process was STABLE.
Computing limits across a period that already contains a shift will inflate
the limits and hide the very signal you are looking for.

Inspect the data first. Days 1-15 sit in a band around 4.0. Days 16-20 sit
clearly higher, around 5.3. Something changed at day 16.

Therefore: compute the control limits from days 1-15 only, then extend those
limits forward and plot days 16-20 against them. This is the correct
procedure and it is what makes the signal visible.
```

### Step 2 - Compute the centre line and control limits

This is an individuals chart (X-mR), used when each measurement is a single value rather than a subgroup average. The control limits come from the moving range, not from the standard deviation.

```text
STEP 2a - Centre line, from days 1-15
  Sum = 4.1+3.8+4.3+3.9+4.2+4.0+3.7+4.4+4.1+3.9+4.2+4.0+3.8+4.3+4.1
      = 60.8
  X-bar = 60.8 / 15 = 4.0533 minutes

STEP 2b - Moving ranges (absolute difference between consecutive points)
  |3.8-4.1| = 0.3     |4.2-3.9| = 0.3     |4.0-4.2| = 0.2
  |4.3-3.8| = 0.5     |4.0-4.2| = 0.2     |3.8-4.0| = 0.2
  |3.9-4.3| = 0.4     |3.7-4.0| = 0.3     |4.3-3.8| = 0.5
  |4.2-3.9| = 0.3     |4.4-3.7| = 0.7     |4.1-4.3| = 0.2
                      |4.1-4.4| = 0.3
                      |3.9-4.1| = 0.2

  There are 14 moving ranges (n-1 for n=15).
  Sum = 0.3+0.5+0.4+0.3+0.3+0.2+0.3+0.7+0.3+0.2+0.3+0.2+0.2+0.5 = 4.6
  MR-bar = 4.6 / 14 = 0.3286

STEP 2c - Estimate sigma
  For an individuals chart, sigma is estimated from the moving range:
    sigma = MR-bar / d2,  where d2 = 1.128 for a moving range of size 2
    sigma = 0.3286 / 1.128 = 0.2913

STEP 2d - Control limits for the individuals chart
  UCL = X-bar + 3 sigma = 4.0533 + (3 x 0.2913) = 4.0533 + 0.8739 = 4.927
  CL  = X-bar                                                     = 4.053
  LCL = X-bar - 3 sigma = 4.0533 - 0.8739                         = 3.179

STEP 2e - Control limits for the moving range chart
  UCL(MR) = 3.267 x MR-bar = 3.267 x 0.3286 = 1.073
  CL(MR)  = MR-bar                          = 0.329
  LCL(MR) = 0  (a range cannot be negative)
```

Summary of the computed limits:

| Chart | LCL | Centre line | UCL |
| --- | --- | --- | --- |
| Individuals (X) | 3.179 | 4.053 | 4.927 |
| Moving range (mR) | 0 | 0.329 | 1.073 |

### Step 3 - Plot the chart

Open [SPC / Control Chart](https://alfredang.github.io/novaspc/).

Enter the full 20-point series in order:

```text
4.1, 3.8, 4.3, 3.9, 4.2, 4.0, 3.7, 4.4, 4.1, 3.9,
4.2, 4.0, 3.8, 4.3, 4.1, 5.2, 5.4, 5.1, 5.3, 5.5

Chart type:        Individuals (X-mR)
Compute limits from:  points 1-15 only
Extend limits across: all 20 points
```

Verify the tool reproduces your hand calculation. If the tool computes limits across all 20 points instead, you will get inflated limits of roughly 4.365 +/- 3 x 0.44, and the shift will be much less obvious - which is precisely the error Step 1 warned about. Reproduce it deliberately once so you recognise it.

Sketch what you should see:

```text
  5.6 |                                              *   <- 20 (5.5)
  5.4 |                                    *             <- 17 (5.4)
  5.2 |                                *       *         <- 16, 19
  5.0 |                                    *             <- 18 (5.1)
  4.9 |- - - - - - - - - - - - - - - - - - - - - - - -   UCL 4.927
  4.6 |
  4.4 |          *
  4.2 |    *   *     *   *     *
  4.0 |------*-----*-----*---*-----------------------    CL 4.053
  3.8 |  *       *     *   *
  3.6 |      *
  3.4 |
  3.2 |- - - - - - - - - - - - - - - - - - - - - - - -   LCL 3.179
      +--------------------------------------------
       1  3  5  7  9  11 13 15 17 19

All of points 16-20 sit above the UCL of 4.927.
```

### Step 4 - Apply the out-of-control rules

A single point outside the limits is only one of several signals. Apply the full set - these are the Western Electric / Nelson rules, and the exam expects the rule of seven in particular.

| Rule | Signal | Present in this data? |
| --- | --- | --- |
| 1 | Any single point beyond 3 sigma (outside a control limit) | **YES** - points 16, 17, 18, 19, 20 all exceed UCL 4.927 |
| 2 - **Rule of seven** | Seven or more consecutive points all on the same side of the centre line | **NO** - check carefully; see analysis below |
| 3 - Rule of seven (trend) | Seven or more consecutive points steadily increasing or decreasing | **NO** - points 16-20 are high but not monotonically rising |
| 4 | Two of three consecutive points beyond 2 sigma on the same side | **YES** - points 16-18 (a subset of the rule 1 violation) |
| 5 | Four of five consecutive points beyond 1 sigma on the same side | **YES** - points 16-20 |
| 6 | Fourteen consecutive points alternating up and down | NO |
| 7 | Fifteen consecutive points within 1 sigma (unnatural lack of variation) | NO |

Work the rule of seven properly on days 1-15, because it is the rule most often tested and most often applied carelessly:

```text
RULE OF SEVEN CHECK, days 1-15, against CL = 4.053

  Day   Value   Side of centre line
   1     4.1    above
   2     3.8    below
   3     4.3    above
   4     3.9    below
   5     4.2    above
   6     4.0    below
   7     3.7    below
   8     4.4    above
   9     4.1    above
  10     3.9    below
  11     4.2    above
  12     4.0    below
  13     3.8    below
  14     4.3    above
  15     4.1    above

  Longest run on one side: 2 consecutive (days 6-7 below, days 8-9 above,
  days 12-13 below, days 14-15 above).
  Maximum run = 2. Seven is not approached.

  VERDICT on days 1-15: no rule violations of any kind. The process is
  IN CONTROL and STABLE across this period. The variation seen - values
  ranging from 3.7 to 4.4 - is entirely COMMON CAUSE.

  Days 16-20: rule 1 violated five times consecutively. This is an
  ASSIGNABLE CAUSE. The process has SHIFTED.
```

```text
WHY THE RULE OF SEVEN MATTERS

If a process is stable and centred, each point has roughly a 50% chance of
falling on either side of the centre line, independently. The probability of
seven consecutive points on the same side is (0.5)^7 = 0.0078, about 1 in 128.
That is rare enough to be treated as a signal rather than chance.

The value of the rule is that it detects a SUSTAINED SMALL SHIFT that never
breaches a control limit. A process that shifts by 1 sigma may never produce
an out-of-limit point, but it will produce long runs on one side. Rule 1 alone
would miss it entirely.

Exam framing: "seven consecutive points above the mean" - the answer is that
the process is out of control and requires investigation, even though no point
has exceeded a control limit.
```

### Step 5 - Separate the causes and decide the response

```text
DAYS 1-15 - COMMON CAUSE
  The process is stable with a mean of 4.053 minutes and a natural range of
  roughly 3.18 to 4.93 minutes.

  CORRECT RESPONSE: do NOT investigate individual days. Day 7 at 3.7 was
  not a triumph and day 8 at 4.4 was not a failure - both are ordinary
  outputs of the same stable process. Asking the team "what went wrong on
  day 8?" is tampering and will make things worse.

  If 4.053 minutes is not acceptable - and it is not, see Step 6 - the
  answer is to CHANGE THE PROCESS, not to chase individual points.

DAYS 16-20 - ASSIGNABLE CAUSE
  Five consecutive points above the UCL. Something specific happened.

  INVESTIGATION: what changed at day 16? The project records show that
  day 16 corresponds to the deployment of the sprint 11 build, which
  introduced the SSG NRIC-linked attendance capture (compliance requirement
  C-04) into the registration flow. The additional validation call to the
  external funding-eligibility service added approximately 1.2 seconds per
  registration, and the new consent step added a page interaction.

  CONFIRMATION: the shift is 5.3 - 4.05 = 1.25 minutes, and it began on the
  exact day of a known change. Both the magnitude and the timing are
  explained. This is a genuine assignable cause, correctly identified.

  RESPONSE: this is not a defect to be "fixed" by reverting - C-04 is a
  mandatory compliance requirement from Lab 04 and cannot be removed. The
  correct response is to re-engineer the flow so the compliance requirement
  is met WITHIN the performance target: make the eligibility call
  asynchronous, cache eligibility results, and merge the consent step into
  an existing page rather than adding one.
```

### Step 6 - Assess capability against the charter target

Now bring in the specification limit, which has been absent so far and deliberately so.

```text
SPECIFICATION
  Charter success criterion SC-1: registration completion under 4.0 minutes.
  This is an upper specification limit. USL = 4.0.
  There is no lower specification limit - faster is always better.

THE UNCOMFORTABLE COMPARISON

  Process mean (days 1-15)   4.053 minutes
  Specification limit        4.000 minutes

  The process was ALREADY FAILING the specification before the day-16 shift.
  It was stable, predictable, in control - and non-compliant with the
  requirement. Roughly 57% of days exceeded 4.0 minutes even in the stable
  period.

  THIS IS THE KEY LESSON OF THE LAB. "In control" and "meeting requirements"
  are entirely different statements. A stable process is one you can predict;
  it is not necessarily one you can accept. If you had looked only at the
  control chart for days 1-15 you would have reported a healthy process.
  If you had looked only at the specification you would have missed that the
  process was stable and therefore fixable by design rather than by chasing.
  You need both.
```

Compute the capability index using [Statistics](https://alfredang.github.io/novastats/). Enter the days 1-15 series:

```text
4.1, 3.8, 4.3, 3.9, 4.2, 4.0, 3.7, 4.4, 4.1, 3.9, 4.2, 4.0, 3.8, 4.3, 4.1

The tool should return:
  n = 15
  Mean = 4.0533
  Sample standard deviation = 0.2066
  Min = 3.7, Max = 4.4, Range = 0.7

CAPABILITY INDEX for a one-sided upper specification

  Cpk(upper) = (USL - mean) / (3 x sigma)

  Using the within-process sigma estimated from the moving range (0.2913):
    Cpk = (4.000 - 4.053) / (3 x 0.2913) = -0.053 / 0.8739 = -0.061

  A NEGATIVE Cpk means the process mean is on the wrong side of the
  specification limit. The process is not merely incapable - its average
  output fails the requirement.

  INTERPRETATION GUIDE
    Cpk < 1.00   Not capable. Significant output falls outside specification.
    Cpk = 1.00   Marginal. Spec limit sits at exactly 3 sigma.
    Cpk = 1.33   Generally accepted as capable.
    Cpk = 2.00   Six Sigma level capability.
    Cpk < 0      The mean itself violates the specification.

  VERDICT: Cpk = -0.06. The process must be re-centred, not merely
  tightened. Reducing variation alone will not help - halving the standard
  deviation would still leave the mean above the limit. The mean must move.
```

### Step 7 - Write the quality verdict and actions

Create `artifacts/22-stability-verdict.md`:

```text
PROCESS QUALITY VERDICT - Registration completion time
Contoso Training Portal Upgrade, sprints 8-11

STABILITY
  Days 1-15:  IN CONTROL. No rule violations. Mean 4.053 min,
              control limits 3.179 to 4.927. Variation is common cause.
  Days 16-20: OUT OF CONTROL. Five consecutive points above the UCL.
              Assignable cause identified: the sprint 11 deployment of the
              SSG eligibility validation (compliance requirement C-04) added
              approximately 1.25 minutes to the median.

CAPABILITY
  Specification (SC-1): under 4.0 minutes.
  Process mean even in the stable period: 4.053 minutes.
  Cpk = -0.06. NOT CAPABLE. The process failed the requirement before the
  day-16 shift and fails it more badly now.

CONCLUSION
  Two distinct problems requiring two distinct responses:
  1. An assignable cause from a known change (days 16-20) - remove the
     performance cost of the compliance step by re-engineering it.
  2. A capability problem in the underlying stable process - the design
     itself is not fast enough, independent of the day-16 change.
  Fixing only the first would return the process to 4.05 minutes, which
  still fails SC-1. Both must be addressed.

ACTIONS
  Q-1  Make the SSG eligibility validation asynchronous; do not block the
       registration flow on an external call.        Dev Lead, sprint 12
       Expected recovery: 1.2 min
  Q-2  Merge the C-04 consent step into the existing confirmation page
       rather than adding a page.                    UX Lead, sprint 12
       Expected recovery: 0.15 min
  Q-3  Re-engineer the two slowest steps of the base flow, identified by
       the Lab 21 method, to bring the stable-process mean below 3.5 min so
       there is margin against the 4.0 specification.
                                                      Dev Lead, sprint 12
       Expected recovery: 0.6 min
  Q-4  Re-measure for 20 consecutive days after sprint 12 and recompute
       control limits from the new stable period. Do not reuse the old
       limits - the process will have changed.        QA Lead, sprint 13

  Forecast after Q-1 to Q-3: 5.30 - 1.2 - 0.15 - 0.6 = 3.35 min mean,
  giving Cpk = (4.0 - 3.35) / (3 x 0.29) = 0.75. Better, still below the
  1.33 capability threshold, but compliant with SC-1 on the mean with
  reasonable margin. Report this honestly rather than claiming capability.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
A control chart shows nine consecutive points below the centre line, but
every point is comfortably inside both control limits. The team lead says
the process is fine because nothing has breached a limit. What is the
correct interpretation?

  A. The team lead is correct; no points are outside the control limits.
  B. The process is out of control. Nine consecutive points on one side of
     the centre line violates the rule of seven and indicates a sustained
     shift requiring investigation.
  C. The control limits should be recalculated to be tighter.
  D. The process is in control but not capable.

SCENARIO 2
A project manager reviews a stable control chart and demands a written
explanation from the team for every measurement that falls below the
centre line. What is the effect of this practice?

  A. It improves quality by increasing accountability.
  B. It has no effect either way.
  C. It is tampering. Reacting to common cause variation as though it were
     assignable increases process variation and degrades performance.
  D. It correctly applies statistical process control.

SCENARIO 3
Which statement about control limits and specification limits is correct?

  A. Control limits are set by the customer; specification limits are
     calculated from the process data.
  B. Control limits are calculated from process data and describe what the
     process does; specification limits are set by the requirement and
     describe what the process must do. A process can be in control and
     still fail specification.
  C. Control limits and specification limits are the same thing expressed
     in different units.
  D. Specification limits should always be set at 3 sigma from the process
     mean.
```

Answer key:

```text
SCENARIO 1 -> B.  The rule of seven exists precisely to catch this case: a
            sustained shift too small to breach a control limit. Nine
            consecutive points on one side has a probability of about
            (0.5)^9 = 0.002, roughly 1 in 512 - far too unlikely to be
            chance. A applies only rule 1 and misses rules 2 through 7.
            C is actively wrong: you never tighten control limits to
            manufacture a signal - limits are computed from the process,
            not chosen. D is a statement about capability, which the
            question gives no specification data to assess.

SCENARIO 2 -> C.  This is tampering, and Deming's funnel experiment
            demonstrated that it makes variation worse rather than better.
            In a stable process, roughly half the points fall below the
            centre line by definition - demanding explanations for them
            requests explanations for randomness. The team will supply
            explanations, because people always can, and those false
            explanations will drive adjustments that add variation.
            A confuses accountability with statistical understanding.
            D inverts the entire method: SPC exists to tell you when NOT
            to react.

SCENARIO 3 -> B.  Voice of the process versus voice of the customer. The
            Contoso data demonstrates the final sentence exactly: days 1-15
            were perfectly in control with zero rule violations, and the
            process mean of 4.053 still failed the 4.0-minute specification.
            A reverses the two. C is the fundamental confusion the whole
            distinction exists to prevent. D is a serious error in practice -
            setting specifications from your own process performance means
            the requirement changes whenever the process does, and the
            customer's actual need is never represented.
```

## Deliverable

Submit to `artifacts/`:

- `22-control-chart.md` - the centre line, moving ranges, estimated sigma, and both the individuals and moving-range control limits, all computed by hand with the working shown.
- A statement of why limits were computed from days 1-15 rather than all 20, and what happens to the limits if you use all 20.
- A screenshot or export of your SPC tool output showing the 20 plotted points against limits derived from the stable period.
- The out-of-control rules table with each rule assessed, including the explicit rule-of-seven run analysis on days 1-15.
- `22-stability-verdict.md` - the common cause / assignable cause separation, the identified assignable cause with its timing and magnitude evidence, and the correct response to each.
- `22-capability-summary.md` - the Statistics tool output, the Cpk calculation, and the interpretation against the capability bands.
- A written statement of the difference between the stability finding and the capability finding, and why fixing only the day-16 shift would leave SC-1 unmet.
- The four quality actions with expected recovery figures and the honest post-action Cpk forecast.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your centre line is 4.053, MR-bar is 0.3286, sigma is 0.2913, and your limits are 3.179 and 4.927. If your limits are much wider, you computed them across all 20 points and have hidden the signal.
- You used MR-bar / 1.128 to estimate sigma, not the sample standard deviation. Using the sample SD of the stable period (0.2066) would give limits of 3.43 to 4.68 - narrower, and not the standard individuals-chart method.
- You checked the rule of seven explicitly on days 1-15 and found the longest run to be 2, concluding no violation. Simply asserting "no rule violations" without the run analysis is not the check.
- You identified days 16-20 as assignable cause AND named a specific, dated, plausible cause with a magnitude that matches the observed shift.
- You stated that days 1-15 were in control and still failed the specification. If your verdict is "the process was fine until day 16", you have missed the central point of the lab.
- Your Cpk is negative, and you concluded that the process must be re-centred rather than merely tightened.
- Your action list addresses both the assignable cause and the underlying capability problem, and your post-action forecast is stated honestly rather than claimed as capable.
- You can explain why demanding an explanation for a single below-average day in a stable process makes performance worse.
