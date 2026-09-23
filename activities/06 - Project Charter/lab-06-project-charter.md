# Lab 06 - Project Charter

| Field | Value |
| --- | --- |
| Topic | 2 - Start the Project |
| ECO 2026 task | Process T1 - Develop an integrated project management plan and plan delivery; Process T2 - Develop and manage project scope |
| Learning outcome | LO1 - Scope medium-scale project requirements to drive timely completions |
| Duration | 75 minutes |
| Consumes | Lab 03 governance model and escalation thresholds; Lab 04 compliance requirements; Lab 05 business case, benefits and financials |
| Produces | `artifacts/06-project-charter.md`, `artifacts/06-approach-decision.md`, `artifacts/06-assumption-log.md` |

## Objectives

- Write a complete project charter that authorises the project and names the PM's authority.
- Set measurable success criteria distinct from deliverables.
- Justify the hybrid development approach with a documented tailoring decision rather than a preference.
- Establish the assumption and constraint log that later labs test against.
- Define scope boundaries explicitly, including what is out.

## What a charter is, and what it is not

```text
THE CHARTER
  - Is issued by the SPONSOR, not written by the PM alone. The PM drafts;
    the sponsor signs. Only the sponsor's signature creates authority.
  - AUTHORISES the project to exist and to consume resources.
  - NAMES the project manager and states their authority level.
  - Is HIGH LEVEL. Milestones, not a schedule. Budget order of magnitude,
    not a cost baseline.
  - Is rarely changed. Changing the charter means re-authorising the project.

THE CHARTER IS NOT
  - The project management plan. The plan comes later and is far more detailed.
  - The business case. The business case justifies; the charter authorises.
    The business case can exist without a project. The charter cannot.
  - A scope statement. The charter gives boundaries; the detailed scope
    statement and WBS come in Lab 11.

Exam tell: if a question asks what you need before you can begin planning, or
who authorises the project, or where the PM's authority comes from - the answer
is the charter.
```

## Steps

### Step 1 - Assemble the charter inputs

Everything in a charter comes from somewhere. Confirm you have each input before drafting.

| Charter input | Source | Have it? |
| --- | --- | --- |
| Business case with financials | Lab 05 - NPV SGD 795,425, payback 1.26 yrs, BCR 2.45 | |
| Benefits management approach | Lab 05 benefits map, B1-B4 with owners | |
| Success metrics and baselines | Lab 03 governance model | |
| Governance structure and thresholds | Lab 03 | |
| Compliance obligations | Lab 04 register, 13 requirements | |
| Environmental constraints | Lab 02 ranked factors | |
| Agreements | None - internal project, no external contract at charter stage | |
| EEFs and OPAs | Lab 03 inventory | |

### Step 2 - Write the charter header and purpose

Create `artifacts/06-project-charter.md`.

```text
PROJECT CHARTER

  Project name          Contoso Training Portal Upgrade
  Project ID            CTP-2026-01
  Sponsor               Priya Nathan, Chief Operating Officer
  Project Manager       [your name]
  Date authorised       [date]
  Charter version       1.0

PURPOSE

  Contoso's course registration portal is nine years old. Registration takes a
  median of 11 minutes and 34% of attempts are abandoned. Learner
  communications consume 24 staff-hours per week of manual effort across three
  administrators. The portal is not responsive, while 62% of learner traffic is
  now mobile. Legacy consent screens do not meet current PDPA requirements.

  This project will modernise course registration and learner communications to
  reduce registration abandonment, automate learner communications, achieve
  mobile parity, and bring learner data handling into PDPA compliance, in time
  for the July intake enrolment window.
```

### Step 3 - State measurable success criteria

Deliverables are what you build. Success criteria are how anyone knows it worked. Keep them separate and make every criterion numeric.

| # | Success criterion | Baseline | Target | Measured by | When judged |
| --- | --- | --- | --- | --- | --- |
| SC-1 | Registration completion time | 11 min median | Under 4 min median | Portal analytics over 30 days | 30 days post-launch |
| SC-2 | Registration abandonment rate | 34% | Under 15% | Funnel analytics | 30 days post-launch |
| SC-3 | Manual communications effort | 24 hrs/week | Under 5 hrs/week | Ops time log | 30 days post-launch |
| SC-4 | Mobile completion rate | 41% | Above 80% | Analytics, mobile segment | 30 days post-launch |
| SC-5 | Compliance clearance | Legacy screens non-compliant | Pass with zero major findings | DPO assessment | At gate G3 |
| SC-6 | Delivered within budget | - | At or under SGD 480,000 | Finance ledger | At closure |
| SC-7 | Delivered by launch date | - | Live on 30 June | Go-live record | 30 June |
| SC-8 | Escaped defects, first 30 days | 19 last release | Under 8 | Defect log | 30 days post-launch |

Note SC-1 to SC-4 cannot be judged at go-live. This matters: the project closes (Lab 23) before its success criteria can be fully assessed, which is precisely why the benefits realisation review extends past closure.

### Step 4 - Define scope boundaries, including exclusions

The exclusions section prevents more disputes than the inclusions section.

**In scope:**

| # | Scope item |
| --- | --- |
| IN-1 | Course search, selection and registration flow, responsive across mobile, tablet and desktop |
| IN-2 | Automated learner communications: confirmation, reminder, reschedule, cancellation, completion |
| IN-3 | Learner self-service: view bookings, reschedule, cancel, download records |
| IN-4 | PDPA-compliant consent capture, purpose limitation, and data access/correction |
| IN-5 | accreditation compliance data capture: NRIC-linked attendance records with 7-year retention |
| IN-6 | Payment integration built against the gateway v2 API |
| IN-7 | Migration of active learner and booking data from the legacy portal |
| IN-8 | Automated regression test suite for the registration and communications paths |
| IN-9 | WCAG 2.1 AA accessibility on all learner-facing pages |
| IN-10 | Training and transition for the three administration staff |

**Explicitly out of scope:**

| # | Exclusion | Rationale |
| --- | --- | --- |
| OUT-1 | AI course recommendation engine | Scored 16 in the Lab 02 scan against 25 for mobile; deferred to phase 2; no in-house ML capability (EEF-08) |
| OUT-2 | Course content management system replacement | Not a source of the stated problems; would break the launch date |
| OUT-3 | Finance and invoicing system replacement | Integration only, not replacement |
| OUT-4 | Corporate client bulk-booking portal | Separate initiative, separate funding |
| OUT-5 | Trainer-facing scheduling tools | Not learner-facing; no benefit in the Lab 05 case |
| OUT-6 | Migration of historical bookings older than 24 months | Archived and accessible; migration cost not justified |
| OUT-7 | Native mobile applications | Responsive web meets the mobile requirement at a fraction of the cost |

Every exclusion carries a rationale. "Out of scope" with no reason invites the argument you were trying to prevent.

### Step 5 - Record high-level requirements, milestones and budget

**High-level requirements** - these seed the Lab 09 elicitation, they do not replace it:

```text
R-1  A learner can find and register for a course in under 4 minutes on a phone.
R-2  A learner receives accurate, timely, automated communications at every
     stage of their booking without administrator intervention.
R-3  A learner can reschedule or cancel without contacting support.
R-4  Personal data is collected with valid consent and used only for the
     purpose stated.
R-5  Attendance records support accreditation compliance claims without manual rework.
R-6  The service performs on mobile devices equivalently to desktop.
```

**Milestone schedule** - milestones only, no activities. Detail comes in Lab 12.

| Milestone | Target date | Gate |
| --- | --- | --- |
| M1 Project authorised | Week 0 | - |
| M2 Requirements baselined | Week 5 | - |
| M3 Design baseline approved | Week 6 | G1 |
| M4 Sprint 1-4 complete, registration flow demonstrable | Week 14 | - |
| M5 Build complete, all Must-have stories done | Week 18 | G2 |
| M6 Compliance review passed | Week 22 | - |
| M7 UAT signed off | Week 23 | - |
| M8 Pre-launch readiness confirmed | Week 24 | G3 |
| M9 Go live | 30 June | - |
| M10 Benefits review and closure | Week 28 | - |

**Budget summary** - order of magnitude at charter stage:

| Category | Amount (SGD) |
| --- | --- |
| Development team | 348,000 |
| UX design | 34,000 |
| Compliance review and penetration test | 28,000 |
| Infrastructure and migration | 26,000 |
| Training and change management | 18,000 |
| Contingency reserve (held by PM) | 26,000 |
| **Total authorised** | **480,000** |

Add the constraint note explicitly:

```text
The SGD 480,000 is a board-approved ceiling. The contingency reserve is held
WITHIN it, not in addition to it. Any requirement beyond this figure is a
ceiling variation requiring Group Finance approval per the Lab 03 thresholds.
```

### Step 6 - Name the project manager's authority

This section is what makes the charter operationally useful, and it is heavily tested. Be specific.

| Authority area | Level granted |
| --- | --- |
| Staff assignment | May assign and re-assign work within the allocated 9-person team without approval |
| Procurement | May commit up to SGD 15,000 per engagement within the approved budget |
| Contingency reserve | May release the SGD 26,000 contingency reserve for identified risks without further approval; must report each release at the next board |
| Management reserve | None. Held by the sponsor outside the project budget |
| Change approval | May approve changes under SGD 10,000 with no critical-path impact, via the CCB; above that per the Lab 03 thresholds |
| Schedule | May resequence work within milestones; may not move M9 |
| Scope | May not change the in-scope or out-of-scope lists without a change request |
| Escalation | Direct access to the sponsor within 24 hours for launch-date threats |

```text
The distinction to remember for the exam:

  CONTINGENCY RESERVE  - for KNOWN risks (identified in the risk register).
                         Part of the cost BASELINE. The PM controls it.
  MANAGEMENT RESERVE   - for UNKNOWN risks. OUTSIDE the cost baseline but
                         inside the project budget. The sponsor controls it.
                         Using it requires a baseline change.

You will build both numerically in Lab 13.
```

### Step 7 - Document the development approach decision

Create `artifacts/06-approach-decision.md`. The ECO enabler is "Recommend a development approach (predictive, adaptive/agile, or hybrid)". A recommendation needs criteria, not taste.

| Criterion | Assessment for Contoso | Points toward |
| --- | --- | --- |
| Requirements stability | Registration flow requirements are well understood; communications content and UX detail will evolve with user feedback | Mixed |
| Delivery date | Fixed and immovable, tied to the July intake | Predictive |
| Budget | Fixed ceiling, board-approved | Predictive |
| Compliance | Formal gate, documented evidence, defined stage sign-off | Predictive |
| Stakeholder feedback need | High - 34% abandonment means the current design is wrong in ways we cannot fully predict; we need to see real users on real increments | Adaptive |
| Technical uncertainty | Moderate - gateway v2 integration and data migration are unknowns best de-risked early | Adaptive |
| Team experience with agile | Team has run 2-week sprints on two prior projects; OPA-06 sprint ceremony guide exists | Adaptive |
| Regulatory audit trail | Required - traceability from requirement to test to evidence | Predictive |

```text
DECISION: HYBRID

  PREDICTIVE ELEMENTS
    - Three stage gates (G1 design, G2 build complete, G3 pre-launch)
    - Baselined scope, schedule and cost, with formal change control
    - Requirements traceability matrix maintained end to end (Lab 09)
    - Compliance evidence pack assembled to a fixed structure
    - Earned value measurement fortnightly (Lab 20)

  ADAPTIVE ELEMENTS
    - Product backlog owned by the Head of L&D Ops (Lab 10)
    - Two-week sprints producing demonstrable increments
    - Sprint review with real learners from sprint 3 onward
    - Retrospectives feeding continuous improvement
    - Kanban WIP limits on the build flow (Lab 19)

  HOW THEY MEET
    The scope BASELINE is fixed at the Must-have level and change-controlled.
    Within that envelope, the PRIORITY and SEQUENCE of backlog items is the
    product owner's to change every sprint without a change request. A change
    request is required only to add, remove or materially alter a Must-have,
    or to breach cost or schedule thresholds.

  WHY NOT PURE PREDICTIVE
    A fully specified design would repeat the mistake that produced 34%
    abandonment: designing the flow without watching learners use it.

  WHY NOT PURE AGILE
    A fixed date, a fixed ceiling and a formal compliance gate cannot be
    accommodated by a purely emergent scope. Something must be fixed, and
    here the date and cost are fixed while detailed scope flexes.
```

### Step 8 - Build the assumption and constraint log

Create `artifacts/06-assumption-log.md`. Assumptions are things you have taken as true without proof - each one is a latent risk, which is why Lab 14 revisits this log.

| ID | Assumption | Basis | If false, impact | Validate by | Owner |
| --- | --- | --- | --- | --- | --- |
| A-01 | Registration abandonment will fall to 15% with the new flow | UX benchmarks; Lab 05 downside tested at 22% | B1 benefit falls; case survives to 22% | Sprint 3 usability test with 8 real learners | UX Lead |
| A-02 | The full 9-person team is available for the whole 6 months | Verbal commitment from functional managers | Schedule slips; critical path exposed | Written resource commitment by week 2 | PM |
| A-03 | The gateway v2 API is stable and documented | Vendor announcement | Integration rework | Spike in sprint 1 | Dev Lead |
| A-04 | Legacy learner data is clean enough to migrate | No formal profiling done | Migration effort could double | Data profiling in sprint 2 | BA |
| A-05 | The DPO can complete the compliance review in 3 weeks | Prior project took 3 weeks | The Lab 01 scenario - 6 weeks against a fixed date | Confirm booking and scope with DPO by week 4 | PM |
| A-06 | accreditation tiers will not change before launch | Announcement expected Q3, after launch | Fee display rework | Monitored per Lab 02 cadence | BA |
| A-07 | The three admin staff will be available as SMEs | Assumed by the plan | Requirements starved; TECOP factor O1 | Agree capped SME hours per sprint by week 2 | PM |

| ID | Constraint | Type | Consequence |
| --- | --- | --- | --- |
| CON-1 | Launch 30 June, immovable | Schedule | Scope flexes, date does not |
| CON-2 | SGD 480,000 ceiling, reserve inside it | Cost | Trade-offs come from scope |
| CON-3 | Compliance gate must pass before go-live | Quality/regulatory | Cannot be run in parallel with go-live |
| CON-4 | Team of 9, no additional headcount | Resource | Capacity is fixed at approx. 34 story points/sprint |
| CON-5 | Must integrate with the existing learner database | Technical | Architecture options limited |
| CON-6 | No in-house ML capability | Resource | AI recommender not feasible in this release |

Note A-05. It is the same situation as the Lab 01 Scenario 2 exam question. Having it in the assumption log with a validation date of week 4 is how you avoid discovering it in week 20.

### Step 9 - Answer the exam-style scenarios

```text
SCENARIO 1
You have a signed business case and an approved budget, but the sponsor has not
yet signed the charter. The functional manager asks you to start assigning
developers to the project. What should you do?

  A. Start assigning; the budget is approved, which is the substantive approval.
  B. Start assigning but do not commit any spend until the charter is signed.
  C. Explain that the charter is what authorises the project and names your
     authority to assign resources, and obtain the sponsor's signature first.
  D. Ask the functional manager to confirm the assignment in writing instead.

SCENARIO 2
Three weeks into the project, the Head of Sales insists the AI recommender was
"always understood to be part of this". What is your BEST first response?

  A. Add it to the backlog as a low priority to keep the peace.
  B. Show the charter's exclusion OUT-1 with its documented rationale, and
     explain the change request route if he wishes to pursue it.
  C. Tell him it is out of scope and cannot be discussed.
  D. Escalate to the sponsor.

SCENARIO 3
The team wants to run the project in pure Scrum with no fixed scope baseline,
arguing that stage gates are "waterfall thinking". How do you respond?

  A. Agree; the team knows best how to work.
  B. Refuse; the organisation requires stage gates.
  C. Walk through the approach decision: the date, the ceiling and the
     compliance gate are fixed EEFs, so the flexibility has to sit in detailed
     scope - which is exactly what the hybrid model gives them within the
     Must-have envelope.
  D. Compromise by removing gate G2.
```

Answer key:

```text
SCENARIO 1 -> C.  The charter is the authorising document and the source of the
            PM's authority over resources. A business case justifies a project;
            it does not authorise one. B is a half-measure that still commits
            people without authority.

SCENARIO 2 -> B.  This is why exclusions carry rationales. B answers the
            substance, cites the artifact, and offers a legitimate route
            rather than a wall. C is a refusal with no path forward. D
            escalates before you have engaged the stakeholder yourself.
            A is the worst option: quietly accepting scope creep into the
            backlog is still scope creep.

SCENARIO 3 -> C.  Answer with the tailoring criteria. The team's instinct is
            reasonable and the response is not to overrule it but to show
            where the fixed constraints genuinely are and how much freedom
            remains inside them. B is authority without explanation, and D
            trades away a compliance-relevant control to win an argument.
```

## Deliverable

Submit to `artifacts/`:

- `06-project-charter.md` containing: purpose, measurable success criteria with baselines, in-scope list, out-of-scope list with rationales, high-level requirements, milestone schedule, budget summary, PM authority levels, sponsor signature block.
- `06-approach-decision.md` - the criteria table, the hybrid decision, what is predictive, what is adaptive, how they meet, and why not each pure approach.
- `06-assumption-log.md` - at least 7 assumptions each with a validation method, date and owner, plus the constraint list.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every success criterion has a numeric baseline and a numeric target. "Improved registration" is not a success criterion.
- Your charter has a sponsor signature block, and you can explain why the PM's signature alone would not authorise anything.
- Every exclusion has a rationale traceable to an earlier lab's evidence.
- Your milestone list contains milestones only - if it contains activities with durations, that belongs in Lab 12.
- Your PM authority section states specific figures for procurement and change approval, consistent with the Lab 03 thresholds.
- Your approach decision names both what is predictive and what is adaptive, and explains the interface between them. "Hybrid" alone is not a decision.
- Every assumption has a validation date earlier than the point at which being wrong would be unrecoverable. Check A-05 in particular.
- You can state the difference between contingency reserve and management reserve, and who controls each.
