# Lab 03 - EEF/OPA Inventory, Governance and Escalation Thresholds

| Field | Value |
| --- | --- |
| Topic | 1 - Business Environment |
| ECO 2026 task | Business Env T1 - Define and establish project governance; Business Env T4 - Remove impediments and manage issues |
| Duration | 45 minutes |
| Consumes | Lab 02 PESTLE/TECOP scan and ranked factor list |
| Produces | `artifacts/03-eef-opa-inventory.md`, `artifacts/03-governance-model.md`, `artifacts/03-escalation-thresholds.md` |

## Objectives

- Separate Enterprise Environmental Factors (things you must live with) from Organizational Process Assets (things you get to reuse) - a distinction the exam tests constantly.
- Build the Contoso governance model: decision bodies, decision rights, cadence and success metrics.
- Set numeric escalation thresholds so escalation becomes a rule rather than a judgement call.
- Define the change control path and the issue path, and show why they are different.

## Why EEF vs OPA matters on the exam

The exam distinguishes them because they lead to different actions:

```text
EEF - Enterprise Environmental Factor
      Conditions NOT under the project team's control.
      Correct action: ADAPT to it, or manage it as a constraint or risk.
      Examples: regulation, market conditions, organisational culture,
                existing infrastructure, the PMIS you are given.

OPA - Organizational Process Asset
      Plans, processes, templates, and the historical knowledge base of
      the organisation.
      Correct action: USE it, then UPDATE it at closure.
      Examples: templates, lessons-learned repository, estimating databases,
                the change control procedure, configuration management.

The tell:  "Do I have to obey it?"       -> EEF
           "Can I reuse and improve it?" -> OPA
```

## Steps

### Step 1 - Inventory the Contoso EEFs

Create `artifacts/03-eef-opa-inventory.md`. Classify each item as internal or external, and state the constraint it imposes.

| # | Enterprise Environmental Factor | Internal / External | Constraint it imposes on you |
| --- | --- | --- | --- |
| EEF-01 | PDPA and regulatory learner-data obligations | External | Compliance review must pass before go-live; 7-year retention |
| EEF-02 | SGD 480,000 board-approved ceiling | Internal | No budget increase available; reserves must fit inside it |
| EEF-03 | Fixed 30 June launch tied to July intake | Internal | Schedule is a constraint, not a variable |
| EEF-04 | Existing legacy portal architecture (9 years old) | Internal | Integration must work with existing learner database |
| EEF-05 | Incumbent payment gateway and its v1 API EOL | External | Must build against v2; vendor timeline not ours to set |
| EEF-06 | Contoso culture: consensus-seeking, risk-averse | Internal | Decisions take longer; plan for approval lead time |
| EEF-07 | Group net-zero-by-2035 commitment | Internal | Hosting choices need a carbon profile |
| EEF-08 | Available skill base - no in-house ML engineer | Internal | AI recommender cannot be built with current team |
| EEF-09 | Competitor feature set | External | Sets stakeholder expectations we do not control |
| EEF-10 | Corporate L&D market down 8% | External | Benefits case must survive lower enrolment |

Add at least two more from your Lab 02 scan.

### Step 2 - Inventory the Contoso OPAs

| # | Organizational Process Asset | Category | How this project uses it |
| --- | --- | --- | --- |
| OPA-01 | Project charter template | Template | Lab 06 charter is written into it |
| OPA-02 | Change control procedure (CCB, 5-day SLA) | Process | Defines the change path in Step 5 below |
| OPA-03 | Lessons-learned repository from 6 prior IT projects | Knowledge base | Estimating inputs and known failure modes |
| OPA-04 | Estimating database: historical developer day-rate SGD 620 | Knowledge base | Lab 13 cost estimating |
| OPA-05 | Risk register template and category RBS | Template | Lab 14 risk register |
| OPA-06 | Sprint ceremony guide (2-week cadence, definition of done) | Process | Sprint mechanics in Labs 10 and 19 |
| OPA-07 | Vendor pre-qualification list | Process | Any procurement decisions |
| OPA-08 | Status report template, fortnightly | Template | Lab 18 communication plan |
| OPA-09 | PDPA data-handling standard operating procedure | Process | Lab 04 compliance register |
| OPA-10 | Post-implementation review checklist | Template | Lab 23 closure |

The key move: pull one *specific* item from OPA-03. From the lessons-learned repository, the prior portal project recorded:

```text
LESSON, PRJ-2021-114 (previous portal release):
"UAT started before the compliance review was complete. Compliance findings
forced rework of the consent-capture screens after UAT sign-off, costing
11 days and SGD 26,000. Recommendation: sequence compliance review BEFORE
UAT, and gate UAT entry on compliance clearance."
```

This is exactly what OPAs are for. Carry it into your Lab 12 schedule sequencing - do not re-learn it at Contoso's expense.

### Step 3 - Design the governance model

Create `artifacts/03-governance-model.md`. Governance answers four questions: who decides, on what, how often, and against what measure.

| Body | Membership | Decides | Cadence | Cannot decide |
| --- | --- | --- | --- | --- |
| Project Board | COO (chair), Finance Director, Head of L&D Ops, PM | Budget changes, launch date, phase gate pass/fail, scope changes above threshold | Monthly + at each gate | Day-to-day technical design |
| Change Control Board | PM (chair), BA, QA Lead, Finance rep | Change requests within delegated limits | Weekly, 5-working-day SLA | Anything breaching the 480,000 ceiling |
| Product Owner | Head of L&D Ops | Backlog priority, sprint scope, acceptance of increments | Continuous; formally at sprint review | Budget, contract, launch date |
| Project Manager | You | Work assignment, sequencing, risk responses within reserve, issue resolution | Daily | Baseline changes above threshold |
| Compliance Gate | Data Protection Officer, external PDPA assessor | Go / no-go on data handling before launch | Once, pre-launch; re-run on failure | Anything outside data protection |

Define three stage gates:

| Gate | When | Entry criteria | Exit decision |
| --- | --- | --- | --- |
| G1 - Design baseline | End of week 6 | Requirements signed, WBS and schedule baselined, architecture approved | Proceed to build / rework / stop |
| G2 - Build complete | End of week 18 | All Must-have stories done, regression suite green, defects below threshold | Proceed to compliance and UAT / rework |
| G3 - Pre-launch | Week 24 | Compliance cleared, UAT signed, transition readiness confirmed | Go live / delay / partial launch |

### Step 4 - Define success metrics

ECO Business Env T1 explicitly includes "Define success metrics". Vague metrics are not governance. Each metric needs a baseline, a target, a measurement method and an owner.

| Metric | Baseline (today) | Target | How measured | Owner | Reviewed |
| --- | --- | --- | --- | --- | --- |
| Registration completion time | 11 min | Under 4 min | Portal analytics, median over 30 days | Head of L&D Ops | Monthly post-launch |
| Registration abandonment rate | 34% | Under 15% | Funnel analytics | Head of L&D Ops | Monthly post-launch |
| Manual comms hours per week | 24 hrs (3 staff x 8) | Under 5 hrs | Ops time log | Ops Manager | Monthly post-launch |
| Mobile completion rate | 41% | Above 80% | Analytics, mobile segment | UX Lead | Monthly post-launch |
| Compliance review outcome | n/a | Pass, zero major findings | DPO assessment report | DPO | At G3 |
| Cost performance index (CPI) | n/a | At or above 0.95 | EVM, computed fortnightly | PM | Fortnightly |
| Schedule performance index (SPI) | n/a | At or above 0.95 | EVM, computed fortnightly | PM | Fortnightly |
| Escaped defects in first 30 days | 19 (last release) | Under 8 | Defect log | QA Lead | 30 days post-launch |

You will actually compute CPI and SPI on real Contoso data in Lab 20, and test the defect target against real defect counts in Lab 21.

### Step 5 - Set numeric escalation thresholds

The ECO enabler is "Outline governance escalation paths and thresholds". A threshold without a number is not a threshold. Create `artifacts/03-escalation-thresholds.md`:

| Trigger | Threshold | Escalate to | Within | Decision needed |
| --- | --- | --- | --- | --- |
| Cost variance | CV worse than -5% of BAC (i.e. over SGD 24,000 overrun) | Project Board | 5 working days | Reserve release or scope cut |
| Cost variance | CV worse than -10% of BAC (over SGD 48,000) | Project Board + Finance Director | 2 working days | Formal re-baseline or stop |
| Schedule | Any Must-have story slipping the critical path by 5+ days | Project Board | 5 working days | Crash, fast-track, or de-scope |
| Schedule | Launch date at risk by any amount | COO directly | 24 hours | Options with cost and risk |
| Change request | Cost impact under SGD 10,000 and no critical-path impact | CCB decides | 5 working days | Approve / reject |
| Change request | Cost impact SGD 10,000-50,000, or any critical-path impact | Project Board | Next board or 10 days | Approve / reject / defer |
| Change request | Cost impact above SGD 50,000, or breaches the 480,000 ceiling | Project Board escalates to Group Finance | 15 days | Ceiling variation |
| Risk | Any risk scoring 20+ on the P/I matrix | Project Board | 5 working days | Response funding |
| Risk | A risk becoming an issue with launch-date impact | COO directly | 24 hours | Immediate intervention |
| Compliance | Any major finding from the DPO assessment | Project Board + DPO | 24 hours | Remediation plan; G3 held |
| Impediment | Blocker unresolved for 3+ working days | PM escalates to functional manager | Immediately at 3 days | Resource or authority |
| Impediment | Blocker unresolved for 5+ working days | Project Board | Immediately at 5 days | Executive intervention |

Note that the two lines "cost impact under SGD 10,000 -> CCB" and "above SGD 50,000 -> Group Finance" are what make this usable. When a change lands, nobody debates who decides.

### Step 6 - Separate the change path from the issue path

These are different processes and the exam tests whether you know which one applies.

```text
CHANGE PATH - something wants the baseline to be different
  Raise change request -> log it -> impact analysis (scope, cost, schedule,
  risk, quality) -> CCB or Board per threshold -> decision -> if approved,
  update the baseline AND all affected documents -> communicate status
  to the requester and stakeholders.
  KEY: no work starts before the decision. Updating the baseline without
  approval is the classic wrong answer.

ISSUE PATH - something has already gone wrong inside the baseline
  Log in the issue log -> assign an owner and a due date -> resolve within
  the PM's authority -> escalate only on the threshold above -> close and
  record. No baseline change unless the resolution requires one, at which
  point it becomes a change request too.
  KEY: an issue is a present-tense problem. A risk is future-tense. When a
  risk materialises it becomes an issue and moves to the issue log.
```

Fill in this routing exercise:

| Situation | Change, issue, or risk? | Where does it go? |
| --- | --- | --- |
| The payment gateway v1 API might be retired early | | |
| A developer resigned yesterday | | |
| Head of Sales asks to add the AI recommender | | |
| The compliance review found a major PDPA gap | | |
| The team may not have PDPA testing skills | | |
| Sponsor asks to bring the launch forward two weeks | | |

### Step 7 - Answer the exam-style scenarios

```text
SCENARIO 1
A change request arrives with a cost impact of SGD 38,000 and it extends the
critical path by 4 days. Under the Contoso thresholds, who decides, and what
must you produce first?

SCENARIO 2
Which of these is an OPA rather than an EEF?

  A. The PDPA regulation the project must comply with.
  B. The board-approved SGD 480,000 ceiling.
  C. The lessons-learned repository from six prior IT projects.
  D. The organisation's risk-averse, consensus-seeking culture.

SCENARIO 3
A blocker has stopped two developers for four working days. The PM has been
chasing the infrastructure team daily by email. What should the PM do NEXT?

  A. Continue chasing daily; the team has promised to look at it.
  B. Reassign the two developers to other backlog items and let the blocker sit.
  C. Escalate to the infrastructure functional manager, as the 3-day
     impediment threshold has been passed.
  D. Escalate directly to the COO.
```

Answer key:

```text
SCENARIO 1  The CCB cannot decide this: SGD 38,000 falls in the 10,000-50,000
            band AND it touches the critical path. Either condition alone sends
            it to the Project Board. First produce the impact analysis - scope,
            cost, schedule, risk and quality - because the Board cannot decide
            without it. Presenting a change request with no impact analysis is
            the common wrong answer.

SCENARIO 2 -> C.  A lessons-learned repository is knowledge you reuse and
            update: an OPA. A is external regulation, B is an imposed
            constraint, D is culture - all EEFs, all things you adapt to.

SCENARIO 3 -> C.  The threshold table says 3+ working days escalates to the
            functional manager. It has been four. A ignores your own governance.
            B hides the problem and leaves the blocker live. D skips a level -
            escalating to the COO before the functional manager has been asked
            is both premature and damaging to the relationship.
```

## Deliverable

Submit to `artifacts/`:

- `03-eef-opa-inventory.md` - at least 12 EEFs and 10 OPAs, each classified and with its constraint or use stated.
- The specific lesson you extracted from the lessons-learned repository and where it changes your plan.
- `03-governance-model.md` - decision bodies with membership, decision rights, cadence, and explicit "cannot decide" limits; plus the three stage gates with entry criteria.
- The success metrics table, every row with a baseline, target, method and owner.
- `03-escalation-thresholds.md` - numeric thresholds for cost, schedule, change, risk, compliance and impediments.
- The completed change/issue/risk routing exercise.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- No item appears in both your EEF and OPA lists, and you can state the "must I obey it / can I reuse it" test for any row.
- Every escalation threshold has a number and a time limit. If any row says "significant" or "major" without a figure, it is not finished.
- Every governance body has an explicit "cannot decide" entry - governance is defined as much by limits as by powers.
- Every success metric has a baseline value, not just a target. A target without a baseline cannot be shown to have been met.
- In the routing exercise you classified the resigned developer as an issue (it has happened) and the possible early API retirement as a risk (it has not).
- You can explain why a change request never starts work before the decision.
