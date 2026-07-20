# Lab 05 - Business Case and Cost-Benefit Analysis

| Field | Value |
| --- | --- |
| Topic | 2 - Start the Project |
| ECO 2026 task | Process T3 - Help ensure value-based delivery; Process T6 - Plan and manage finance |
| Duration | 50 minutes |
| Consumes | Lab 02 factors E1 and E2; Lab 03 success metrics and baselines; Lab 04 compliance exposure figures |
| Produces | `artifacts/05-business-case.md`, `artifacts/05-cba-model.md`, `artifacts/05-benefits-map.md` |

## Objectives

- Build a quantified benefits model from the Lab 03 baseline metrics.
- Compute payback period, net present value, return on investment and benefit-cost ratio - by hand, so the exam formulas stick.
- Test the case against the Lab 02 downside scenario of an 8% fall in enrolment.
- Select among project options using the financial measures.
- Build a benefits realisation map that Lab 23 will close against.

## The formulas you must know cold

```text
PAYBACK PERIOD    Time until cumulative net cash flow turns positive.
                  Shorter is better. Ignores everything after payback and
                  ignores the time value of money - which is exactly why the
                  exam pairs it with NPV.

NPV               Net Present Value = sum of [ Ct / (1+r)^t ] - initial investment
                  where Ct = net cash flow in period t, r = discount rate.
                  DECISION RULE: NPV > 0, the project creates value. Choose the
                  HIGHER NPV. NPV is the tie-breaker the exam prefers.

ROI               (Total benefit - Total cost) / Total cost x 100%
                  Higher is better.

BCR               Benefit-Cost Ratio = Total benefit / Total cost
                  BCR > 1 means benefits exceed costs. Do NOT confuse with the
                  cost-benefit ratio, which is the inverse and where lower wins.

IRR               The discount rate at which NPV = 0. Higher is better.
                  You will not be asked to compute it by hand.

Exam traps:  A bigger project is not a better project - compare NPV, not size.
             A shorter payback does not beat a higher NPV.
             Sunk cost is never a reason to continue.
```

## Steps

### Step 1 - Quantify the benefits from the Lab 03 baselines

Every benefit must trace to a metric you baselined in Lab 03. Create `artifacts/05-cba-model.md`.

```text
CONTOSO FINANCIAL BASE DATA

  Active learners per year                     14,000
  Registrations per year                       21,500  (learners take >1 course)
  Current registration abandonment rate           34%
  Current registration completion time         11 min
  Average revenue per completed registration  SGD 340
  Average gross margin per registration           32%   = SGD 108.80

  Admin staff doing manual communications           3
  Hours per week each on manual comms                8   = 24 hrs/week total
  Fully loaded admin cost per hour            SGD  28
  Working weeks per year                            48

  Current annual support tickets on registration  1,900
  Average handling cost per ticket            SGD  22

  Current hosting and maintenance cost/year   SGD  74,000
  Projected hosting and maintenance cost/year SGD  61,000
```

Now compute each benefit line. Work these yourself before reading the worked figures.

| # | Benefit | Calculation | Annual value (SGD) |
| --- | --- | --- | --- |
| B1 | Recovered abandoned registrations | Abandonment 34% -> 15%, a 19pp recovery. Completed today = 21,500. Attempts = 21,500 / 0.66 = 32,576. Recovered = 32,576 x 0.19 = 6,189 registrations x SGD 108.80 margin | 673,363 |
| B2 | Admin time released | 24 hrs/wk -> 5 hrs/wk = 19 hrs saved x 48 wks x SGD 28 | 25,536 |
| B3 | Support ticket reduction | 1,900 tickets -> 800, a fall of 1,100 x SGD 22 | 24,200 |
| B4 | Hosting and maintenance saving | 74,000 - 61,000 | 13,000 |
| | **Total gross annual benefit** | | **736,099** |

B1 dominates and is also the least certain, so it must be tested in Step 4. A business case whose entire value sits in one optimistic line is a business case that has not been stress-tested.

Apply a benefit realisation haircut. Benefits do not arrive on day one and rarely arrive in full:

| Year | Realisation factor | Realised benefit (SGD) | Reasoning |
| --- | --- | --- | --- |
| Year 1 | 55% | 404,854 | Launches 30 June, so half a year, plus adoption ramp |
| Year 2 | 90% | 662,489 | Full year, some abandonment stubbornly remains |
| Year 3 | 90% | 662,489 | Steady state |

### Step 2 - Build the cost side

| Cost element | Year 0 (build) | Year 1 | Year 2 | Year 3 |
| --- | --- | --- | --- | --- |
| Development team (from Lab 13 estimate) | 348,000 | - | - | - |
| UX design | 34,000 | - | - | - |
| Compliance review and pen test | 28,000 | - | - | - |
| Infrastructure and migration | 26,000 | - | - | - |
| Training and change management | 18,000 | - | - | - |
| Contingency reserve | 26,000 | - | - | - |
| **Total project cost** | **480,000** | - | - | - |
| Ongoing hosting and maintenance | - | 61,000 | 61,000 | 61,000 |
| Ongoing support and licences | - | 14,000 | 14,000 | 14,000 |
| **Total ongoing** | - | **75,000** | **75,000** | **75,000** |

Note that the total build cost equals the SGD 480,000 ceiling exactly, and that the contingency reserve sits *inside* it - the Lab 02 factor E2 consequence. You will decompose these numbers properly in Lab 13.

### Step 3 - Compute payback, NPV, ROI and BCR

Build the net cash flow table. Use a discount rate of 8%, Contoso's stated cost of capital.

| Year | Benefit | Cost | Net cash flow | Cumulative | Discount factor (8%) | Present value |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 480,000 | -480,000 | -480,000 | 1.0000 | -480,000 |
| 1 | 404,854 | 75,000 | 329,854 | -150,146 | 0.9259 | 305,421 |
| 2 | 662,489 | 75,000 | 587,489 | 437,343 | 0.8573 | 503,655 |
| 3 | 662,489 | 75,000 | 587,489 | 1,024,832 | 0.7938 | 466,349 |

Now the four measures. Compute each before checking:

```text
PAYBACK PERIOD
  Cumulative is -150,146 at end of year 1 and +437,343 at end of year 2.
  Payback occurs during year 2.
  Fraction of year 2 needed = 150,146 / 587,489 = 0.256
  PAYBACK = 1 + 0.26 = 1.26 years, about 15 months.

NPV at 8%
  NPV = -480,000 + 305,421 + 503,655 + 466,349
  NPV = SGD 795,425
  NPV is positive and large -> the project creates value.

ROI over 3 years
  Total benefit  = 404,854 + 662,489 + 662,489 = 1,729,832
  Total cost     = 480,000 + (75,000 x 3)      =   705,000
  ROI = (1,729,832 - 705,000) / 705,000 x 100 = 145.4%

BCR
  BCR = 1,729,832 / 705,000 = 2.45
  Every SGD 1 spent returns SGD 2.45 of benefit.
```

Record the discount factor method so you can reproduce it in the exam:

```text
Discount factor for year t at rate r  =  1 / (1 + r)^t

  Year 1 at 8%:  1 / 1.08      = 0.9259
  Year 2 at 8%:  1 / 1.08^2    = 1 / 1.1664 = 0.8573
  Year 3 at 8%:  1 / 1.08^3    = 1 / 1.2597 = 0.7938

A useful sanity check: at 8%, a dollar three years out is worth about 79 cents
today. If your factor is above 1 or rising with time, you have inverted it.
```

### Step 4 - Stress-test against the Lab 02 downside

Lab 02 factor E1 said client L&D budgets are down 8%. Test the case with 8% lower registration volume *and* a weaker abandonment recovery - 34% down to only 22% rather than 15%.

```text
DOWNSIDE SCENARIO

  Registrations              21,500 x 0.92 = 19,780
  Attempts                   19,780 / 0.66 = 29,970
  Abandonment recovery       34% -> 22% = 12pp
  Recovered registrations    29,970 x 0.12 = 3,596
  B1 downside               3,596 x 108.80 = SGD 391,245  (was 673,363)

  B2 admin saving unchanged                  SGD  25,536
  B3 support tickets, scaled 0.92            SGD  22,264
  B4 hosting saving unchanged                SGD  13,000
  Gross annual benefit, downside             SGD 452,045  (was 736,099)

  Year 1 at 55%   248,625      Net  173,625
  Year 2 at 90%   406,841      Net  331,841
  Year 3 at 90%   406,841      Net  331,841

  NPV = -480,000 + (173,625 x 0.9259) + (331,841 x 0.8573) + (331,841 x 0.7938)
      = -480,000 + 160,750 + 284,487 + 263,415
      = SGD 228,652

  Payback: cumulative -480,000 -> -306,375 -> +25,466
           Payback during year 2 at 306,375 / 331,841 = 0.92
           PAYBACK = 1.92 years, about 23 months.

  CONCLUSION: even on the downside the project has a positive NPV of
  SGD 228,652 and pays back inside two years. The case is robust.
```

This is the paragraph that gets a business case approved. Anyone can build a base case; showing that the decision survives the pessimistic scenario is what earns trust.

### Step 5 - Choose among options

The sponsor asks you to compare three options before committing. Complete the comparison and make a recommendation.

| | Option A: Do nothing | Option B: Full rebuild | Option C: Targeted upgrade (proposed) |
| --- | --- | --- | --- |
| Description | Keep the legacy portal, add staff to absorb volume | Replace the entire platform including CMS and finance integration | Modernise registration and communications only |
| Investment | 0 | 1,150,000 | 480,000 |
| Duration | - | 18 months | 6 months |
| Annual benefit (yr 2 full) | 0 | 812,000 | 736,099 |
| Ongoing cost/year | 74,000 + 2 extra staff at 58,000 = 190,000 | 88,000 | 75,000 |
| 3-year NPV at 8% | -489,860 | 421,900 | **795,425** |
| Payback | Never | 2.9 years | **1.26 years** |
| Meets fixed 30 June launch? | n/a | No - 18 months | **Yes** |
| Meets compliance gate? | No - legacy consent screens fail PDPA | Yes | **Yes** |

```text
RECOMMENDATION: Option C.

Option A is not a null option - it costs money. Doing nothing carries an
NPV of -489,860 because volume growth forces extra headcount while the
legacy consent screens still fail PDPA. "Do nothing" is a decision with a
price, and quantifying it is often the strongest argument in a business case.

Option B produces the largest gross benefit but the lowest NPV of the two
viable options, because the extra SGD 670,000 of investment buys only
SGD 76,000 of extra annual benefit, and it cannot meet the fixed launch date.

Option C has the highest NPV, the shortest payback, and is the only option
that satisfies the immovable constraints. Higher NPV wins - not the biggest
project, and not merely the fastest payback.
```

### Step 6 - Write the business case document

Create `artifacts/05-business-case.md` using this structure:

| Section | Content required |
| --- | --- |
| 1. Problem statement | The 34% abandonment, 11-minute registration, 24 hours/week manual comms, and the PDPA exposure of legacy consent screens |
| 2. Strategic alignment | How this supports Contoso's stated goals; link to the Lab 02 environment scan |
| 3. Options considered | The three-option table with the do-nothing cost quantified |
| 4. Recommended option | Option C with the reasoning above |
| 5. Benefits | The B1-B4 table with baselines, targets and owners from Lab 03 |
| 6. Costs | Build cost, ongoing cost, and the reserve sitting inside the ceiling |
| 7. Financial analysis | Payback 1.26 yrs, NPV SGD 795,425, ROI 145.4%, BCR 2.45 |
| 8. Sensitivity | The downside scenario and its NPV of SGD 228,652 |
| 9. Key risks to the case | The three below |
| 10. Recommendation and ask | Approve SGD 480,000, launch 30 June |

The three risks to the *business case* specifically - distinct from project delivery risks, which go in Lab 14:

| Risk to the case | Effect | Mitigation |
| --- | --- | --- |
| Abandonment does not fall to 15% | B1 is 91% of the benefit; a shortfall dominates the case | Measure abandonment weekly from launch; the downside scenario shows the case survives 22% |
| Regulator fee-grant tier change reduces enrolment | Volume assumption falls further | Sensitivity already run at -8%; monitor per Lab 02 cadence |
| Benefits are claimed but never measured | Value assumed, never confirmed | Lab 03 metrics have owners; Lab 23 benefits review is scheduled at 30, 90 and 180 days |

### Step 7 - Build the benefits realisation map

Create `artifacts/05-benefits-map.md`. This is what Lab 23 will formally close against, so make it verifiable.

| Benefit | Output that enables it | Baseline | Target | Measured by | Owner | First review |
| --- | --- | --- | --- | --- | --- | --- |
| B1 Recovered registrations | Streamlined responsive registration flow | 34% abandonment | Under 15% | Funnel analytics | Head of L&D Ops | 30 days post-launch |
| B2 Admin time released | Automated learner communications engine | 24 hrs/week | Under 5 hrs/week | Ops time log | Ops Manager | 30 days post-launch |
| B3 Fewer support tickets | Self-service rescheduling and status | 1,900/year | Under 800/year | Helpdesk system | Support Lead | 90 days post-launch |
| B4 Lower running cost | Decommission legacy infrastructure | SGD 74,000/yr | SGD 61,000/yr | Finance ledger | Finance Director | 180 days post-launch |

Note the chain the exam expects: **output enables outcome, outcome delivers benefit**. A responsive registration flow is an output. Lower abandonment is an outcome. SGD 673,363 of recovered margin is the benefit. Confusing the three is a reliable way to lose marks.

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
Two projects are competing for the same funding.
  Project X: NPV SGD 240,000, payback 1.1 years, investment SGD 200,000
  Project Y: NPV SGD 610,000, payback 2.4 years, investment SGD 900,000
Which should the organisation select, all else equal?

  A. Project X, because payback is faster.
  B. Project X, because it needs less investment.
  C. Project Y, because its NPV is higher.
  D. Cannot decide without the IRR.

SCENARIO 2
Contoso has spent SGD 180,000 on the project when a competitor releases a free
tool that delivers most of the same registration benefit. Re-running the case
with the reduced remaining benefit gives an NPV of -SGD 90,000 for the work
still to come. The sponsor says "we've already spent 180,000, we can't stop
now." How should you respond?

  A. Agree; abandoning it would waste the investment already made.
  B. Explain that the SGD 180,000 is sunk and irrecoverable either way, so the
     only relevant question is whether the REMAINING investment produces
     positive value - and on current figures it does not.
  C. Continue but reduce scope to spend less.
  D. Escalate to the board without a recommendation.

SCENARIO 3
Using the Contoso base case, if the discount rate rose from 8% to 12%, what
happens to the NPV, and does the decision change?
```

Answer key:

```text
SCENARIO 1 -> C.  Higher NPV wins. Payback ignores everything after the payback
            point and ignores the time value of money entirely. Smaller
            investment is not itself a benefit. This is one of the most reliably
            tested points in the whole finance area.

SCENARIO 2 -> B.  Sunk cost is never a reason to continue. The SGD 180,000 is
            gone under every option, so it cannot differentiate them. The
            forward-looking NPV is negative, which argues for stopping or
            re-scoping - and note that C might be right in substance but B is
            the reasoning that has to come first. You cannot choose a response
            before correcting the sponsor's decision frame.

SCENARIO 3   Discount factors at 12% become 0.8929, 0.7972, 0.7118.
             PV = (329,854 x 0.8929) + (587,489 x 0.7972) + (587,489 x 0.7118)
                = 294,527 + 468,346 + 418,174 = 1,181,047
             NPV = 1,181,047 - 480,000 = SGD 701,047
             The NPV falls from 795,425 to 701,047 - a higher discount rate
             always reduces NPV, because future money is discounted harder.
             The decision does NOT change: NPV remains strongly positive.
             A well-built case should be robust to the discount rate; if a
             4-point change flips your decision, the case was marginal.
```

## Deliverable

Submit to `artifacts/`:

- `05-cba-model.md` - the benefits quantification B1-B4 traced to Lab 03 baselines, the cost table, and the discounted cash flow table with all discount factors shown.
- All four financial measures computed with working shown: payback period, NPV, ROI, BCR.
- The downside sensitivity scenario with its recomputed NPV and payback.
- The three-option comparison including the quantified cost of doing nothing.
- `05-business-case.md` - all ten sections.
- `05-benefits-map.md` - each benefit traced output -> outcome -> benefit, with baseline, target, owner and review date.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every benefit line traces to a Lab 03 baseline metric. A benefit with no baseline cannot be proven in Lab 23.
- Your discount factors decrease with time and are below 1. If any factor exceeds 1, you have inverted the formula.
- Your NPV subtracts the initial investment. Forgetting the year-0 outflow is the single most common arithmetic error here.
- Your BCR is above 1 and equals total benefit divided by total cost - not the inverse.
- Your do-nothing option has a *negative* number attached, not a blank. Do-nothing is never free.
- Your recommendation cites NPV as the deciding measure, not payback or project size.
- Your downside scenario still shows a positive NPV, and you stated that conclusion explicitly.
- In Scenario 2 you named the SGD 180,000 as sunk before discussing what to do next.
