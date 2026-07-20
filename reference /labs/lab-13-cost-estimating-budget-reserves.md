# Lab 13 - Cost Estimating, Budget and Reserves

| Field | Value |
| --- | --- |
| Topic | 3 - Plan the Project |
| ECO 2026 task | Process T6 - Plan and manage finance; Process T1 - Develop an integrated project management plan |
| WSQ learning outcome | LO2 - Develop project schedules and budgets |
| Duration | 90 minutes |
| Consumes | Lab 11 WBS work packages and effort estimates; Lab 12 schedule; Lab 05 business case; Lab 06 budget summary |
| Produces | `artifacts/13-cost-estimates.md`, `artifacts/13-cost-baseline.md`, `artifacts/13-reserve-analysis.md` |

## Objectives

- Select the right estimating technique for the information you actually have, and state its accuracy range.
- Build a bottom-up estimate from the Lab 11 work packages that reconciles to the charter.
- Distinguish contingency reserve from management reserve precisely enough to answer any exam question on either.
- Size the contingency reserve by expected monetary value rather than by a percentage guess.
- Build a time-phased cost baseline as an S-curve that Lab 20's earned value analysis will measure against.
- Analyse the cost of quality, and demonstrate that prevention is cheaper than failure with real figures.

## The estimating techniques and their accuracy ranges

```text
ANALOGOUS (top-down)
  Uses the actual cost of a SIMILAR PAST project as the basis for this one,
  adjusted for known differences. Draws on historical OPA data.
    ACCURACY   -25% to +75%
    SPEED      Fastest. Hours, not weeks.
    COST       Cheapest.
    USE WHEN   Early. Little detail available. A go/no-go decision is
               needed before detailed planning is justified.
    WEAKNESS   Only as good as the comparability of the analogue, and
               "similar" is doing a great deal of work in that sentence.
    A form of EXPERT JUDGEMENT.

PARAMETRIC
  Uses a statistical relationship between historical data and variables.
  Cost = rate x quantity.
    ACCURACY   Varies with the quality of the model - can be very high.
    SCALES     Well. Doubling the quantity doubles the estimate.
    USE WHEN   A reliable, calibrated model exists and the work is
               quantifiable in the model's units.
    EXAMPLE    Contoso: developer day rate SGD 620 x person-days. This is
               parametric estimating, and it is the engine underneath the
               bottom-up estimate below.
    WEAKNESS   A model calibrated on different work gives confident,
               precise, wrong answers.

BOTTOM-UP
  Estimate each work package individually, then aggregate up the WBS.
    ACCURACY   -5% to +10%. The most accurate technique available.
    EFFORT     The most expensive and slowest. It requires a complete WBS,
               which is why Lab 11 had to come first.
    USE WHEN   Detail exists and accuracy matters - which is now, at
               baseline.
    STRENGTH   Also produces the cost of each work package, which is what
               makes control accounts and earned value possible.

THREE-POINT / PERT
  Applied to cost exactly as Lab 12 applied it to duration.
    cE = (cO + 4cM + cP) / 6      SD = (cP - cO) / 6
    USE WHEN   Uncertainty needs to be expressed as a range rather than
               concealed in a single number.

ESTIMATE CLASSES - the two the exam names

  ROM (Rough Order of Magnitude)   -25% to +75%
    Produced at initiation, from analogous estimating.
  DEFINITIVE (or budget) ESTIMATE  -5% to +10%
    Produced at baseline, from bottom-up estimating.

  The ranges are ASYMMETRIC and the asymmetry is deliberate. Projects
  overrun far more often than they underrun, so the upside tail is longer.
  If you see a symmetric "+/- 50%" offered as a ROM range, be suspicious.
```

```text
APPLIED TO CONTOSO'S SGD 480,000

  As a ROM estimate (-25% to +75%):
    Lower bound   480,000 x 0.75  =  SGD 360,000
    Upper bound   480,000 x 1.75  =  SGD 840,000
    RANGE: SGD 360,000 to 840,000. A spread of SGD 480,000 - as wide as
    the estimate itself. This is why you cannot commit to a board-approved
    ceiling on a ROM.

  As a DEFINITIVE estimate (-5% to +10%):
    Lower bound   480,000 x 0.95  =  SGD 456,000
    Upper bound   480,000 x 1.10  =  SGD 528,000
    RANGE: SGD 456,000 to 528,000.

  THE PROBLEM THIS EXPOSES, and it is a real one at Contoso:
    Even at definitive accuracy, the upper bound of SGD 528,000 EXCEEDS
    the board-approved ceiling of SGD 480,000 by SGD 48,000. The ceiling
    sits at the CENTRE of the definitive range, not above it. There is no
    room in the estimate for the estimate to be normal.

    That is a structural finding, and it belongs in the reserve analysis
    in Step 4 rather than being quietly ignored. The charter fixed the
    ceiling before the bottom-up estimate existed - which is normal
    practice and normally survivable, but it must be stated rather than
    assumed away.
```

## Steps

### Step 1 - Build the bottom-up estimate from the WBS

Create `artifacts/13-cost-estimates.md`. Take effort from the Lab 11 WBS dictionary and apply the differentiated resource rates.

**Resource rates** - from the historical OPA:

| Role | Day rate (SGD) |
| --- | --- |
| Developer | 620 |
| UX designer | 680 |
| QA lead | 590 |
| Business analyst | 640 |
| DevOps engineer | 700 |
| Content lead | 480 |

**Labour estimate against the charter's development line:**

| WBS | Work package | Role | Effort (days) | Rate | Cost (SGD) |
| --- | --- | --- | --- | --- | --- |
| 1.1.1 | Project management and governance | BA | 42 | 640 | 26,880 |
| 1.2.1 | Requirements register and RTM | BA | 34 | 640 | 21,760 |
| 1.3.1 | Course search and selection | Developer | 56 | 620 | 34,720 |
| 1.3.2 | Responsive registration flow | Developer | 70 | 620 | 43,400 |
| 1.3.3 | Accessibility WCAG 2.1 AA | Developer | 20 | 620 | 12,400 |
| 1.4.1 | Notification engine and delivery | Developer | 52 | 620 | 32,240 |
| 1.5.1 | Booking view, reschedule, cancel | Developer | 58 | 620 | 35,960 |
| 1.6.1 | Gateway v2 API integration | Developer | 46 | 620 | 28,520 |
| 1.7.1 | Data profiling and migration scripts | DevOps | 30 | 700 | 21,000 |
| 1.8.1 | PDPA consent and data rights | Developer | 38 | 620 | 23,560 |
| 1.9.1 | Automated regression suite | QA lead | 86 | 590 | 50,740 |
| 1.11.1 | Release engineering and cutover | DevOps | 24 | 700 | 16,800 |
| | **Total labour** | | **556 days** | | **347,980** |

```text
RECONCILIATION TO THE CHARTER

  Bottom-up labour estimate            SGD 347,980
  Charter development team line        SGD 348,000
  VARIANCE                             SGD      20   (0.006%)

  The bottom-up estimate reconciles to the charter's order-of-magnitude
  figure within SGD 20. State this explicitly in your estimate document,
  because the reconciliation is the evidence that the detailed plan and
  the authorised budget describe the same project.

  A WORD ON WHAT THIS RECONCILIATION MEANS - and does not mean.
  Reconciling does NOT prove the estimate is right. It proves the
  bottom-up estimate and the charter estimate agree, which is reassuring
  but could equally mean both used the same optimistic assumptions. The
  independent checks are the accuracy range in Step 5 and the reserve
  analysis in Step 4.

  A NOTE ON THE OTHER ROLES. The UX designer's and content lead's effort
  is NOT in the table above, because their cost is funded from separate
  charter lines (UX design SGD 34,000 and training and change management
  SGD 18,000). Every person is funded once and only once. Double-counting
  a role across two budget lines is a common and expensive estimating
  error - it inflates the total and then hides the inflation.
```

**Non-labour and separately funded lines:**

| Category | Content | Cost (SGD) | Basis |
| --- | --- | --- | --- |
| UX design | UX designer 50 days at 680 = 34,000 | 34,000 | Parametric, rate x quantity |
| Compliance review and pen test | DPO review time plus external penetration test vendor | 28,000 | Analogous - previous release cost 26,000, adjusted for wider scope |
| Infrastructure and migration | Environments, hosting during build, migration tooling, licences | 26,000 | Parametric, from the IT Ops rate card |
| Training and change management | Content lead 30 days at 480 = 14,400 plus materials and facilitation 3,600 | 18,000 | Bottom-up |
| **Total non-labour** | | **106,000** | |

```text
TOTAL PROJECT ESTIMATE

  Labour (development line)                     SGD 347,980
  UX design                                     SGD  34,000
  Compliance review and penetration test        SGD  28,000
  Infrastructure and migration                  SGD  26,000
  Training and change management                SGD  18,000
                                                ------------
  TOTAL ESTIMATED WORK COST                     SGD 453,980
                                                ~ SGD 454,000

  Contingency reserve (computed in Step 4)      SGD  26,000
                                                ------------
  COST BASELINE                                 SGD 480,000
  Management reserve                            SGD       0
                                                ------------
  PROJECT BUDGET                                SGD 480,000
```

### Step 2 - Contingency reserve versus management reserve

This is the central concept of the lab and one of the most reliably tested distinctions in the entire cost area. Learn it as a table and be able to reproduce it.

| | Contingency reserve | Management reserve |
| --- | --- | --- |
| Covers | **Known unknowns** - identified risks in the risk register | **Unknown unknowns** - risks not identified and not identifiable |
| Basis | Quantified from the risk register, usually by EMV | Judgement, often a percentage of the baseline |
| Position | **INSIDE** the cost baseline | **OUTSIDE** the cost baseline, **inside** the project budget |
| Controlled by | The **project manager** | The **sponsor** or organisational management |
| To use it | PM releases it against an identified risk that has occurred; reports the release | Requires a **baseline change** - a formal change request |
| In earned value | Included in BAC, so it is measured | Not in BAC; using it changes BAC |
| If unused | Returned at closure | Returned to the organisation |

```text
THE FORMULAS THAT FOLLOW FROM THE TABLE

  COST BASELINE   =  Work package estimates  +  CONTINGENCY reserve
  PROJECT BUDGET  =  Cost baseline           +  MANAGEMENT reserve

  Say them in that order and the position of each reserve is unambiguous.

  Contoso:
    Work package estimates                  SGD 453,980
    Contingency reserve                     SGD  26,000
    COST BASELINE                           SGD 479,980  ~ 480,000
    Management reserve                      SGD       0
    PROJECT BUDGET                          SGD 480,000

  BAC (Budget at Completion) for Lab 20 = the cost baseline = SGD 480,000.
```

```text
THE CONTOSO WRINKLE - analyse this, do not just record it

  From the Lab 06 charter: "The SGD 480,000 is a board-approved ceiling.
  The contingency reserve is held WITHIN it, not in addition to it."
  And from the PM authority table: "Management reserve: None."

  So Contoso has:
    - A contingency reserve of SGD 26,000, which is 5.7% of the
      SGD 453,980 of estimated work.
    - NO management reserve whatsoever.

  WHY THIS IS ITSELF A RISK, and it belongs in the Lab 14 register:

  1. There is NO PROVISION FOR UNKNOWN UNKNOWNS. Every project encounters
     something nobody thought of. On this project, the response to any
     unforeseen event must come from contingency that was sized for
     KNOWN risks - so an unknown unknown consumes the funds allocated to
     risks you have already identified and expect to face.

  2. THE RESERVE IS THIN AGAINST THE ESTIMATE RANGE. Step 1 showed the
     definitive estimate's upper bound at SGD 528,000, which is
     SGD 48,000 above the ceiling. The contingency of SGD 26,000 covers
     just over half of a normal upside estimating variance, before a
     single risk event occurs.

  3. THE ONLY REMAINING LEVER IS SCOPE. With cost fixed at a ceiling and
     the date fixed at 30 June (CON-1), the only variable left is scope -
     which is precisely why the Lab 10 MoSCoW discipline rule mattered so
     much, and why the 42 points of Coulds are the project's real reserve.
     The schedule and cost reserves are thin; the SCOPE reserve is the
     substantial one.

  4. ESCALATION IS PRE-AGREED, WHICH IS THE MITIGATION. Per the Lab 03
     thresholds, a projected ceiling breach goes to Group Finance. The
     professional action is to make that path explicit NOW, at baseline,
     with the trigger defined - a forecast EAC above SGD 470,000 - rather
     than arriving at Group Finance in week 20 with an overrun and no
     warning.

  RECORD THIS AS RISK R-12 IN LAB 14: "As a result of the contingency
  reserve being held inside a fixed ceiling with no management reserve,
  an unforeseen event may exhaust available funds, which would lead to a
  forced scope reduction or a ceiling variation request to Group Finance."
```

### Step 3 - Size the contingency reserve by expected monetary value

A reserve set as "10% because that is what we always do" is not an estimate; it is a habit. Size it from the risk register.

```text
EMV  =  Probability  x  Impact

  Threats are NEGATIVE (a cost to the project).
  Opportunities are POSITIVE (a saving).
  The contingency reserve is sized on the RESIDUAL EMV - the exposure that
  REMAINS AFTER the planned risk responses have been applied. Sizing on
  the gross, pre-response EMV double-counts, because you are paying for
  the response AND reserving against the risk the response removes.
```

Risk data from the Lab 14 register. Impacts are cost impacts in SGD.

| Risk | Description (abbreviated) | Pre-response P | Impact | Gross EMV | Post-response P | Residual EMV |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Gateway v2 API unstable, integration rework | 0.35 | 42,000 | 14,700 | 0.15 | 6,300 |
| R-02 | Legacy data quality worse than assumed | 0.25 | 18,000 | 4,500 | 0.15 | 2,700 |
| R-03 | Key developer unavailable during build | 0.30 | 15,000 | 4,500 | 0.20 | 3,000 |
| R-04 | Migration volume exceeds estimate | 0.20 | 22,000 | 4,400 | 0.10 | 2,200 |
| R-05 | Scope creep via unmanaged backlog additions | 0.40 | 9,000 | 3,600 | 0.25 | 2,250 |
| R-06 | DPO review exceeds 3 weeks (assumption A-05) | 0.15 | 30,000 | 4,500 | 0.10 | 3,000 |
| R-07 | Performance target missed, optimisation rework | 0.25 | 12,000 | 3,000 | 0.15 | 1,800 |
| R-08 | Penetration test finds a major vulnerability | 0.10 | 35,000 | 3,500 | 0.05 | 1,750 |
| R-09 | Admin SMEs unavailable (assumption A-07) | 0.30 | 8,000 | 2,400 | 0.20 | 1,600 |
| R-10 | Accessibility failures found late | 0.20 | 14,000 | 2,800 | 0.10 | 1,400 |
| R-11 | Velocity below 34 points per sprint | 0.45 | 6,000 | 2,700 | 0.25 | 1,500 |
| R-12 | No management reserve; unforeseen event | 0.15 | 20,000 | 3,000 | 0.10 | 2,000 |
| R-13 | Requirements churn after baseline | 0.25 | 7,000 | 1,750 | 0.15 | 1,050 |
| R-14 | SSG funding data specification changes | 0.10 | 26,000 | 2,600 | 0.05 | 1,300 |
| R-15 | Third-party hosting or environment delay | 0.35 | 5,000 | 1,750 | 0.20 | 1,000 |
| R-16 | Admin staff attrition before handover | 0.20 | 9,000 | 1,800 | 0.15 | 1,350 |
| | **Threat subtotal** | | | **55,900** | | **34,200** |
| O-01 | Reusable component from a prior project cuts build | 0.30 | -12,000 | -3,600 | 0.40 | -4,800 |
| O-02 | Pen test vendor early availability avoids delay cost | 0.25 | -8,000 | -2,000 | 0.35 | -2,800 |
| | **Opportunity subtotal** | | | **-5,600** | | **-7,600** |
| | **NET EMV** | | | **50,300** | | **26,600** |

```text
THE RESERVE ARITHMETIC - verify it yourself

  Gross threat EMV (before responses)              SGD  55,900
  Gross opportunity EMV                            SGD  -5,600
  GROSS NET EMV                                    SGD  50,300

  Residual threat EMV (after responses)            SGD  34,200
  Residual opportunity EMV                         SGD  -7,600
  RESIDUAL NET EMV                                 SGD  26,600

  CONTINGENCY RESERVE REQUIRED                     SGD  26,600
  CHARTER CONTINGENCY RESERVE                      SGD  26,000
  SHORTFALL                                        SGD     600  (2.3%)

  CONCLUSION: the charter's SGD 26,000 contingency reserve is
  substantiated by the risk register. The EMV-derived requirement of
  SGD 26,600 exceeds it by SGD 600, which is 2.3% - well inside estimating
  tolerance and not worth reopening the charter for. Record the SGD 600
  variance explicitly rather than rounding it away, and note that it
  consumes part of the SGD 20 headroom found in Step 1.

  WHY THE OPPORTUNITY PROBABILITIES ROSE AFTER RESPONSE:
  Opportunity responses are designed to make good outcomes MORE likely.
  O-01's probability rises from 0.30 to 0.40 because the ENHANCE response
  allocates two days to assess and adapt the reusable component. Threat
  responses reduce probability or impact; opportunity responses increase
  them. If your post-response opportunity numbers went down, you applied
  a threat response to an opportunity.

  WHAT WOULD BE WRONG:
    Reserving the gross EMV of SGD 50,300 double-counts. You have already
    committed effort to the mitigations that reduce the exposure to
    SGD 26,600; reserving as though those mitigations do not exist funds
    the same risk twice and inflates the baseline.
    Reserving a flat 10% (SGD 45,400) would be arbitrary, unsupportable
    at a board challenge, and in this case wrong by SGD 18,800.
```

### Step 4 - Build the time-phased cost baseline

A total budget is not a baseline. A baseline is time-phased - it says how much should have been spent by any given date, which is what makes variance measurable. Plotted cumulatively it produces the characteristic S-curve: slow at the start while the team ramps and designs, steep through the build, flattening at the end as work completes.

Create `artifacts/13-cost-baseline.md`. Twelve two-week sprint periods across the 24-week schedule.

| Period | Sprint | Week ending | Planned spend (SGD) | Cumulative PV (SGD) | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | S1 | 2 | 22,000 | 22,000 | Ramp-up, requirements, spikes |
| 2 | S2 | 4 | 26,000 | 48,000 | Design, consent build begins |
| 3 | S3 | 6 | 32,000 | 80,000 | **G1 design gate** |
| 4 | S4 | 8 | 38,000 | 118,000 | Build accelerating |
| 5 | S5 | 10 | 42,000 | 160,000 | Full build velocity |
| 6 | S6 | 12 | 52,000 | 212,000 | Peak build, all roles engaged |
| 7 | S7 | 14 | 56,000 | **268,000** | Peak spend period |
| 8 | S8 | 16 | 54,000 | 322,000 | Migration and self-service |
| 9 | S9 | 18 | 50,000 | 372,000 | **G2 build complete** |
| 10 | S10 | 20 | 48,000 | 420,000 | Compliance review, pen test |
| 11 | S11 | 22 | 34,000 | 454,000 | UAT, training; work cost complete |
| 12 | S12 | 24 | 26,000 | 480,000 | **G3**, cutover, contingency drawdown |
| | | **Total** | **480,000** | | |

```text
READ THE SHAPE OF THE CURVE - it should look like this

  Cumulative PV (SGD 000)
  480 |                                                        *
  454 |                                                  *
  420 |                                            *
  372 |                                      *
  322 |                                *
  268 |                          *       <-- WEEK 14, PV = 268,000
  212 |                    *
  160 |               *
  118 |          *
   80 |      *
   48 |   *
   22 | *
    0 +---+---+---+---+---+---+---+---+---+---+---+---+
      0   2   4   6   8  10  12  14  16  18  20  22  24   weeks

  Shallow start, steep middle, flattening finish. If your curve is a
  straight line, you have divided the budget by twelve rather than phased
  it against the actual plan - and a straight line will produce false
  schedule variance in Lab 20 every single period.

TWO CRITICAL VALUES TO CARRY FORWARD TO LAB 20

  BAC (Budget at Completion)            =  SGD 480,000
  PV at week 14 (end of sprint 7)       =  SGD 268,000

  Lab 20's earned value analysis measures actual performance against these
  exact figures. PV at week 14 is 55.8% of BAC, which is the planned
  percentage complete at that point.

THE CONTINGENCY WITHIN THE CURVE - be explicit about this

  Work cost completes at week 22:            SGD 454,000
  Contingency reserve                        SGD  26,000
  Cost baseline total                        SGD 480,000

  Note that the final period's SGD 26,000 is NOT twelve weeks of work - it
  is the cutover and hypercare cost together with the drawdown of whatever
  contingency remains committed. Two presentational conventions exist and
  you must choose one and be consistent:

    CONVENTION A (used here): distribute the contingency into the periods
      where the risks it covers actually sit, so the baseline curve
      reaches SGD 480,000 and BAC = 480,000. This is what Lab 20 assumes.

    CONVENTION B: show the work-cost curve reaching SGD 454,000 and hold
      the SGD 26,000 as a separate line above it.

  Convention B is arguably clearer for reporting; Convention A is what
  earned value requires, because contingency is inside the cost baseline
  and therefore inside BAC. Mixing them - reporting a 454,000 curve while
  computing EAC against a 480,000 BAC - produces a permanent phantom
  favourable variance of SGD 26,000, and it is a genuinely common error.
```

### Step 5 - Funding limit reconciliation and cash flow

```text
FUNDING LIMIT RECONCILIATION
  Comparing the planned expenditure against any LIMIT on funding
  commitments. Funds are rarely released as one lump sum; they arrive in
  tranches, and the baseline must fit inside them.

  Where planned spend exceeds the funding available in a period, the work
  must be RESCHEDULED to level the expenditure. Note the direction: the
  funding constraint changes the SCHEDULE, not the other way round. This
  is why funding limit reconciliation is a planning activity and not a
  reporting one.
```

Contoso's board releases funds quarterly:

| Quarter | Weeks | Funding released (SGD) | Cumulative funding | Cumulative PV | Headroom |
| --- | --- | --- | --- | --- | --- |
| Q1 | 1-12 | 220,000 | 220,000 | 212,000 | 8,000 |
| Q2 | 13-24 | 260,000 | 480,000 | 480,000 | 0 |

```text
RECONCILIATION RESULT

  Q1: planned cumulative spend of SGD 212,000 against SGD 220,000
      released. Headroom SGD 8,000. FITS, but only just - 3.6%.
  Q2: the remaining SGD 260,000 exactly covers the remaining
      SGD 268,000 of planned spend... except it does not.
      480,000 - 212,000 = 268,000 required in Q2, against 260,000
      released. SHORTFALL of SGD 8,000 in Q2.

  This is exactly what funding limit reconciliation exists to catch, and
  it is catchable only because the baseline is time-phased. The SGD 8,000
  of unused Q1 headroom must be confirmed as carrying forward into Q2. If
  it does not carry forward, SGD 8,000 of work must move from Q2 into Q1 -
  or the schedule breaches the funding limit in week 20 with no warning.

  ACTION: confirm carry-forward with Group Finance before baselining.
  Record it as an assumption if it cannot be confirmed in time.

CASH FLOW versus COST
  These are different and the exam distinguishes them. COST is incurred
  when work is performed. CASH FLOW is when money actually leaves the
  organisation. A pen test invoiced in week 20 on 30-day terms is a week
  20 COST and a week 24 CASH OUTFLOW. The cost baseline tracks cost; the
  finance department tracks cash. Both are correct and they do not match.
```

### Step 6 - Analyse the cost of quality

```text
COST OF QUALITY (COQ) = the total cost of conformance plus the total cost
of non-conformance, across the whole product life cycle - not just the
project.

  COST OF CONFORMANCE - money spent to PREVENT failure
    PREVENTION COSTS   Stop defects occurring at all.
                       Training, design reviews, coding standards,
                       accessibility built into the design system,
                       privacy by design.
    APPRAISAL COSTS    Find defects before the customer does.
                       Testing, inspections, audits, the penetration
                       test, the compliance review.

  COST OF NON-CONFORMANCE - money spent BECAUSE failure occurred
    INTERNAL FAILURE   Found BEFORE the customer sees it.
                       Rework, scrap, re-testing, defect fixing in build.
    EXTERNAL FAILURE   Found AFTER the customer sees it.
                       Production defects, support tickets, regulatory
                       penalties, lost business, reputational damage.
                       ALWAYS the most expensive category, often by an
                       order of magnitude.

  THE PRINCIPLE: spending on prevention and appraisal is cheaper than
  paying for failure. The exam phrases this as "the cost of quality is
  lower when quality is planned in rather than inspected in".
```

| Category | Contoso item | Cost (SGD) | Note |
| --- | --- | --- | --- |
| **Prevention** | Accessibility built into the design system (WBS 1.3.3 incremental design cost) | 8,000 | Against SGD 40,000 to retrofit - Lab 04 figure |
| Prevention | Privacy by design - consent built with the registration form in sprint 2 | 6,000 | Avoids rework of accepted screens |
| Prevention | Coding standards, design reviews, definition of ready | 5,000 | Team time |
| Prevention | Team training on gateway v2 and PDPA obligations | 4,000 | |
| | **Total prevention** | **23,000** | |
| **Appraisal** | Automated regression suite (WBS 1.9.1) | 50,740 | Also a prevention asset for future releases |
| Appraisal | Penetration test and compliance review (WBS 1.8.4, 1.8.5) | 28,000 | |
| Appraisal | Performance and load testing (WBS 1.9.2) | 9,000 | |
| Appraisal | User acceptance testing (WBS 1.9.3) | 7,000 | |
| | **Total appraisal** | **94,740** | |
| **Internal failure** | Defect fixing during build, budgeted allowance | 14,000 | Some rework is normal and should be budgeted, not hoped away |
| Internal failure | Migration rehearsal failures and re-runs | 4,000 | |
| | **Total internal failure** | **18,000** | |
| **External failure** | Production defects in the first 30 days (SC-8 target: under 8) | 12,000 | Estimated at the target level |
| External failure | Launch-period support ticket spike | 6,000 | |
| | **Total external failure** | **18,000** | |
| | **TOTAL COST OF QUALITY** | **153,740** | 32% of the SGD 480,000 budget |

```text
THE ACCESSIBILITY CASE - the clearest demonstration in the project

  Accessibility BUILT IN     (prevention)
    Incremental design and development cost         SGD  8,000
    Detected by: nothing - the defect never exists.

  Accessibility RETROFITTED  (external failure)
    Rework of completed learner-facing pages
    plus re-testing, re-audit and re-acceptance     SGD 40,000
    Detected by: the compliance audit at G3, or worse, a complaint
    after launch.

  RATIO  40,000 / 8,000  =  5 : 1

  Every SGD 1 spent preventing the accessibility defect avoids SGD 5 of
  failure cost. And the SGD 40,000 figure is optimistic, because it prices
  only the rework - it does not price the schedule impact of discovering
  it at G3 against a fixed 30 June launch, nor the regulatory exposure
  under C-11, nor the learners excluded in the meantime.

  This is why WBS 1.3.3 exists as a work package built alongside the
  registration flow rather than as a remediation activity after it. The
  cost of quality analysis is the justification for that sequencing
  decision, and it is the argument to use when someone proposes deferring
  accessibility to "after launch, when there is time".

  THE GENERAL SHAPE, worth carrying into the exam:
    Prevention + appraisal at Contoso    =  SGD 117,740
    Internal + external failure          =  SGD  36,000
  A healthy ratio. Projects in trouble show the reverse - low prevention,
  low appraisal, and failure costs consuming the budget. If a question
  describes a project cutting testing to save money, the correct answer
  almost always involves the failure costs that decision creates.
```

### Step 7 - Answer the exam-style scenarios

```text
SCENARIO 1
In week 16, a risk in the register materialises: the legacy data proves
dirtier than assumed (R-02) and cleansing will cost an additional
SGD 14,000. What is the correct funding route?

  A. Request a management reserve release from the sponsor.
  B. Release SGD 14,000 from the contingency reserve, since R-02 is an
     identified risk in the register, and report the release at the next
     board per the Lab 06 PM authority table.
  C. Raise a change request to increase the cost baseline by SGD 14,000.
  D. Absorb it within the migration work package budget.

SCENARIO 2
In week 19, an unforeseen regulatory change requires a data residency
control nobody anticipated, costing SGD 30,000. Contingency has
SGD 9,000 remaining. What is the correct action?

  A. Release the remaining SGD 9,000 of contingency and absorb the rest
     within work package budgets.
  B. This is an unknown unknown, which is what management reserve exists
     for - but Contoso has none. Escalate to the sponsor and Group Finance
     per the Lab 03 thresholds with the options costed: a ceiling
     variation, or a scope reduction drawn from the Lab 10 Coulds.
  C. Release the SGD 9,000 and raise a change request for the balance.
  D. Defer the control until after launch.

SCENARIO 3
A team member proposes reducing the automated regression suite scope to
save SGD 20,000, arguing that manual testing can cover the gap. What is
the cost of quality argument against this?

  A. There is none; a saving of SGD 20,000 within a fixed ceiling is
     valuable and manual testing is a legitimate alternative.
  B. It converts an appraisal cost into a probable external failure cost.
     The suite is the control on SC-8 (fewer than 8 escaped defects) and
     on the Lab 03 lesson about regression gaps. External failure costs
     exceed appraisal costs by a large multiple, and the SGD 20,000 saved
     is set against SGD 18,000 of already-budgeted external failure that
     would rise substantially - plus a compliance evidence gap, since the
     suite is the verification evidence for REQ-030 in the RTM.
  C. It is a schedule risk rather than a cost issue.
  D. Accept it but increase the contingency reserve by SGD 20,000.
```

Answer key:

```text
SCENARIO 1 -> B.  R-02 is an IDENTIFIED risk carried in the register with a
            residual EMV of SGD 2,700, which is precisely what contingency
            reserve funds - known unknowns. The PM controls it and may
            release it without further approval per the Lab 06 authority
            table, with an obligation to report. A confuses the two
            reserves and, at Contoso, requests a reserve that does not
            exist. C is wrong because using contingency does NOT change
            the cost baseline - the contingency is already inside it, so
            there is nothing to change. D is the quietly damaging answer:
            hiding a risk event inside a work package corrupts that
            package's cost performance in Lab 20's earned value data and
            makes the migration team appear to have overrun when in fact
            a registered risk occurred.

SCENARIO 2 -> B.  A regulatory change nobody anticipated is the textbook
            unknown unknown, and unknown unknowns are funded by management
            reserve, which requires a baseline change and sponsor
            authority. Contoso has no management reserve - which is why
            the Step 2 analysis flagged that absence as risk R-12. The
            correct action is escalation with options costed, not
            improvisation. A hides a baseline breach inside work packages
            and will surface as an unexplained overrun. C is partially
            right in mechanism but omits the escalation that the Lab 03
            thresholds require, and it treats a ceiling breach as routine.
            D defers a regulatory control, which trades a cost problem for
            a compliance failure at the G3 gate.

SCENARIO 3 -> B.  This is the cost of quality principle applied directly.
            Cutting appraisal does not remove the defects; it removes the
            means of finding them before learners do, converting a known
            appraisal cost into an uncertain and larger external failure
            cost. The compliance dimension is what makes it decisive: the
            suite is the linked verification evidence for REQ-030 in the
            Lab 09 RTM, so reducing it also reduces demonstrable coverage
            at the G3 gate. A prices the saving without pricing the
            consequence. D is incoherent - reserving SGD 20,000 against a
            SGD 20,000 saving nets to zero while leaving the quality
            exposure in place, and contingency is for identified risks,
            not for funding the consequences of a deliberate decision.
```

## Deliverable

Submit to `artifacts/`:

- `13-cost-estimates.md` - the bottom-up estimate from the Lab 11 work packages with role, effort, rate and cost per package; the reconciliation to the charter's SGD 348,000 development line with the variance stated; the non-labour categories with their estimating basis named.
- The ROM and definitive ranges applied to SGD 480,000, with the finding that the definitive upper bound exceeds the ceiling.
- `13-reserve-analysis.md` - the contingency versus management reserve table; the EMV computation across at least 16 risks showing gross and residual exposure; the reconciliation to SGD 26,000 with the variance stated; the analysis of the no-management-reserve condition as a risk in itself.
- `13-cost-baseline.md` - the 12-period time-phased baseline with planned spend and cumulative PV per period, summing to SGD 480,000, with PV at week 14 equal to SGD 268,000; the S-curve plotted; the convention for contingency stated explicitly.
- The funding limit reconciliation with the Q2 shortfall identified and an action recorded.
- The cost of quality analysis across all four categories with real figures, including the accessibility prevention-versus-retrofit ratio.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your bottom-up labour total is SGD 347,980 and reconciles to the charter's SGD 348,000 within SGD 20.
- No role is funded from two budget lines. Check the UX designer and content lead in particular.
- You can state, without hesitating, that the cost baseline equals work plus contingency and the project budget equals cost baseline plus management reserve - and which reserve the PM controls.
- Your contingency reserve is derived from residual EMV, not from a percentage, and you can show why using gross EMV would double-count.
- Your residual net EMV is approximately SGD 26,600 and you stated the SGD 600 variance against the charter rather than rounding it away.
- Your cumulative PV at week 14 is exactly SGD 268,000 and your periods sum to exactly SGD 480,000. Lab 20 depends on both figures.
- Your S-curve is shallow, then steep, then flattening. A straight line means you divided rather than phased.
- You chose one contingency convention and applied it consistently, and can explain the phantom variance that mixing them produces.
- You identified the absence of a management reserve as a risk and traced it to a Lab 14 register entry.
- Your cost of quality analysis shows prevention plus appraisal exceeding failure costs, and you can quote the 5:1 accessibility ratio.
