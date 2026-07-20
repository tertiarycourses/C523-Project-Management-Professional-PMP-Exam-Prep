# Lab 02 - PESTLE and TECOP External Environment Scan

| Field | Value |
| --- | --- |
| Topic | 1 - Business Environment |
| ECO 2026 task | Business Env T8 - Evaluate external business environment changes; Business Env T7 - Support organizational change |
| WSQ learning outcome | LO4 - Analyze program risks and engage stakeholders through scheduled touchpoints |
| Duration | 75 minutes |
| Consumes | Lab 01 Contoso case study briefing |
| Produces | `artifacts/02-pestle-scan.md`, `artifacts/02-tecop-scan.md`, `artifacts/02-backlog-impacts.md` |

## Objectives

- Run a structured PESTLE scan of the environment surrounding the Contoso Training Portal Upgrade.
- Run a TECOP scan to surface risk dimensions PESTLE tends to miss.
- Score each factor for impact and likelihood, and rank them.
- Translate the top-ranked factors into concrete backlog and scope consequences.
- Establish a review cadence, because ECO Business Env T8 requires *continual* review, not a one-off scan.

## Why this comes before the charter

The July 2026 ECO gives Business Environment 26% of the exam - 44 scored questions. A recurring exam pattern is: something changes outside the project, and you are asked what to do. The keyed answer is almost never "carry on as planned" and almost never "cancel the project". It is normally "assess the impact on scope/backlog and take it through the governance process". This lab builds the artifact that lets you do that.

## Steps

### Step 1 - Read the environment briefing

```text
CONTOSO OPERATING ENVIRONMENT - briefing pack, current quarter

Political      SkillsFuture Singapore is reviewing subsidy tiers for
               IT training courses. An announcement is expected in Q3,
               after the portal's fixed 30 June launch.

Economic       Corporate L&D budgets across Contoso's client base are
               down 8% year on year. Contoso's own margin is thin;
               the SGD 480,000 budget is a board-approved hard ceiling.

Social         62% of learner traffic is now mobile, up from 38% three
               years ago. The current portal is not responsive.
               Learners increasingly expect self-service rescheduling.

Technological  Two competitors launched AI course-recommendation
               features this year. Contoso's current portal has none.
               The incumbent payment gateway announces end-of-life for
               its v1 API in 14 months.

Legal          PDPA applies to all learner personal data. SSG funding
               claims require learner NRIC-linked attendance records
               with a 7-year retention obligation. A compliance review
               must pass before go-live.

Environmental  Contoso's parent group has published a net-zero-by-2035
               commitment. New IT procurement must report the carbon
               profile of hosting choices.
```

### Step 2 - Build and score the PESTLE table

Create `artifacts/02-pestle-scan.md`. For each of the six categories, record at least one factor. Score impact 1-5 and likelihood 1-5, then compute Score = Impact x Likelihood.

| # | Category | Factor | Impact (1-5) | Likelihood (1-5) | Score | Threat or opportunity |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | Political | SSG subsidy tier review lands in Q3, after launch | 3 | 4 | 12 | Threat |
| E1 | Economic | Client L&D budgets down 8%; enrolment volume may fall | 4 | 4 | 16 | Threat |
| E2 | Economic | SGD 480,000 is a hard ceiling - no contingency top-up available | 5 | 5 | 25 | Threat |
| S1 | Social | 62% mobile traffic against a non-responsive portal | 5 | 5 | 25 | Both |
| S2 | Social | Learner demand for self-service rescheduling | 3 | 4 | 12 | Opportunity |
| T1 | Technological | Competitors shipped AI recommendations; Contoso has none | 4 | 4 | 16 | Both |
| T2 | Technological | Payment gateway v1 API end-of-life in 14 months | 4 | 5 | 20 | Threat |
| L1 | Legal | PDPA compliance review must pass before go-live | 5 | 5 | 25 | Threat |
| L2 | Legal | SSG 7-year NRIC-linked attendance retention | 4 | 5 | 20 | Threat |
| En1 | Environmental | Group net-zero-by-2035 hosting carbon reporting | 2 | 3 | 6 | Threat |

Add at least two factors of your own. Anything you add must be traceable to the briefing or to a documented assumption - do not invent facts.

### Step 3 - Run the TECOP scan

PESTLE looks outward at the market. TECOP looks at the *risk dimensions of the project itself* and catches things PESTLE misses - particularly operational and organisational exposure.

| Dimension | Prompt question | Contoso factor | Impact | Likelihood | Score |
| --- | --- | --- | --- | --- | --- |
| **T**echnical | What could fail in the technology or architecture? | Legacy portal has no automated test suite; regression risk on every release | 4 | 4 | 16 |
| **E**nvironmental | What in the physical or regulatory setting constrains us? | Hosting carbon reporting is a new, unpractised procurement step | 2 | 3 | 6 |
| **C**ommercial | What in contracts, funding or the market bites us? | Payment gateway contract renews mid-project; pricing not yet fixed | 3 | 3 | 9 |
| **O**perational | What in day-to-day running goes wrong? | The 3 admin staff who send communications manually are also the SMEs; they cannot do both | 4 | 5 | 20 |
| **P**olitical | What internal power and agenda issues exist? | Head of Sales wants the AI recommender in v1; COO wants registration speed only | 4 | 4 | 16 |

Note the difference in what the two tools surfaced. PESTLE found the SSG subsidy review; TECOP found that the admin staff are double-booked as SMEs. Neither tool alone finds both. That is why the ECO expects you to use more than one lens.

### Step 4 - Rank and take the vital few

Combine both tables, sort by score descending, and take everything scoring 16 or above.

| Rank | ID | Factor | Score | Source |
| --- | --- | --- | --- | --- |
| 1 | E2 | Hard budget ceiling of SGD 480,000 | 25 | PESTLE |
| 2 | S1 | 62% mobile traffic, non-responsive portal | 25 | PESTLE |
| 3 | L1 | PDPA review must pass before go-live | 25 | PESTLE |
| 4 | T2 | Payment gateway v1 API end-of-life | 20 | PESTLE |
| 5 | L2 | SSG 7-year retention obligation | 20 | PESTLE |
| 6 | O1 | Admin staff double-booked as SMEs | 20 | TECOP |
| 7 | E1 | Client L&D budgets down 8% | 16 | PESTLE |
| 8 | T1 | Competitor AI recommendations | 16 | PESTLE |
| 9 | Tech1 | No automated test suite on legacy portal | 16 | TECOP |
| 10 | P1-int | Sales vs COO disagreement on v1 scope | 16 | TECOP |

Ten factors is the working set. Anything below 16 goes into a watch list you review at the cadence set in Step 6 - it is recorded, not worked.

### Step 5 - Translate factors into scope and backlog consequences

This is the step most people skip, and it is the step the ECO actually assesses. A scan that changes nothing is decoration. Create `artifacts/02-backlog-impacts.md`:

| Factor | Consequence for the project | Where it lands |
| --- | --- | --- |
| S1 - mobile traffic | Responsive design is not a nice-to-have; it becomes a Must in the Lab 10 MoSCoW cut | Requirements, backlog |
| L1 - PDPA review | A compliance workstream with its own gate, sequenced *before* go-live, not parallel to it | WBS (Lab 11), schedule (Lab 12) |
| L2 - SSG retention | Data-retention and archival requirement with a 7-year horizon; affects storage cost | Requirements, cost (Lab 13) |
| E2 - budget ceiling | Contingency reserve must come out of the 480,000, not on top of it | Cost baseline and reserves (Lab 13) |
| T2 - gateway EOL | Payment integration built against v2 API from the start, not v1 | Architecture, backlog, risk register (Lab 14) |
| O1 - admin as SMEs | Named backfill or capped SME hours per sprint | Resource plan, RACI (Lab 15) |
| T1 - competitor AI | AI recommender is a Could, deferred to phase 2; the AI-governance question is picked up in Lab 04 | Backlog, AI governance register |
| Tech1 - no test suite | Automated regression suite added as an explicit deliverable | WBS, quality plan |
| P1-int - Sales vs COO | Expectation-alignment session; feeds the stakeholder register in Lab 07 | Stakeholder engagement |
| E1 - L&D budgets down | Benefits case sensitivity-tested at lower enrolment volume | Business case (Lab 05) |

Every one of these carries forward. When you build the WBS in Lab 11, the compliance workstream is there because of L1 in this table.

### Step 6 - Set the review cadence

ECO Business Env T8 says "*continually* review the external business environment for impacts". Define who looks, when, and what triggers an out-of-cycle review.

```text
EXTERNAL ENVIRONMENT REVIEW CADENCE - Contoso Training Portal Upgrade

  Scheduled review    Every sprint review (fortnightly), 15-minute standing item
  Owner               Project Manager, with the Business Analyst
  Deep review         At each stage gate (3 gates: design, build complete, pre-launch)
  Escalation          Any factor whose score rises to 20 or above between reviews
                      goes to the sponsor within 2 working days

  OUT-OF-CYCLE TRIGGERS - review immediately if any of these occur:
    - SSG publishes the subsidy tier decision
    - The payment gateway announces an accelerated EOL date
    - A competitor ships a registration feature we do not have
    - PDPA guidance is amended
    - Enrolment volume drops more than 10% against forecast
```

### Step 7 - Answer the exam-style scenarios

```text
SCENARIO 1
Halfway through the build, SkillsFuture Singapore announces the subsidy tier
review will conclude two months EARLIER than expected - one month before your
launch. The outcome could change how course fees are displayed and calculated
on the portal. What do you do FIRST?

  A. Pause the fee-display work until the decision is published.
  B. Assess the impact on the scope and backlog, then take options through
     the change control process.
  C. Escalate to the sponsor that the launch date is now at risk.
  D. Add a risk to the risk register and continue as planned.

SCENARIO 2
The Head of Sales emails the sponsor directly arguing that without the AI
recommender, the portal launches "already obsolete". The sponsor forwards it to
you asking for a view. What is the BEST response?

  A. Add the AI recommender to the current release to protect the relationship.
  B. Tell the sponsor the scope is baselined and cannot change.
  C. Present the environment scan showing the recommender scored 16 against
     mobile responsiveness at 25, with the phase-2 option and its cost.
  D. Ask the Head of Sales to raise a change request and take no further action.

SCENARIO 3
Which of these did the TECOP scan surface that the PESTLE scan did not?

  A. The PDPA compliance obligation.
  B. That the three admin staff are simultaneously the project's subject
     matter experts and cannot do both jobs.
  C. The 8% fall in client L&D budgets.
  D. The group net-zero commitment.
```

Answer key:

```text
SCENARIO 1 -> B.  The ECO enabler is literally "assess and prioritize impact on
                  project scope/backlog". A pauses without analysis. C escalates
                  a problem rather than options. D records but does not act -
                  and this is a live change, not a future risk.

SCENARIO 2 -> C.  Answer with the artifact. You did the scan precisely so that
                  scope arguments are settled with scored evidence rather than
                  with volume. C also gives the sponsor a real option (phase 2)
                  instead of only a refusal, which B is.

SCENARIO 3 -> B.  Operational exposure inside the delivering organisation.
                  A, C and D all came from the PESTLE table.
```

## Deliverable

Submit to `artifacts/`:

- `02-pestle-scan.md` - all six PESTLE categories populated and scored, with at least two factors of your own added.
- `02-tecop-scan.md` - all five TECOP dimensions populated and scored.
- The combined ranked table of factors scoring 16 or above.
- `02-backlog-impacts.md` - one consequence and one destination artifact per top-ranked factor.
- Your review cadence definition including out-of-cycle triggers.
- Written answers to the three scenarios with reasoning.

## Checkpoint

You did this right if:

- Every PESTLE letter (P, E, S, T, L, E) has at least one factor; a scan missing a category is not a PESTLE scan.
- Every score is the product of impact and likelihood, and you can state both numbers for any factor.
- Your TECOP table surfaced at least one factor that does not appear anywhere in your PESTLE table. If the two tables are identical, you used PESTLE twice.
- Every factor scoring 16+ has a named destination artifact in a later lab - not a vague "monitor".
- Your cadence names an owner, a frequency, and at least three out-of-cycle triggers.
- In Scenario 1 you chose B and can explain why "add to risk register and continue" is wrong for an event that has already happened.
