# Lab 11 - Work Breakdown Structure and WBS Dictionary

| Field | Value |
| --- | --- |
| Topic | 3 - Plan the Project |
| ECO 2026 task | Process T2 - Develop and manage project scope (break down scope); Process T1 - Develop an integrated project management plan |
| WSQ learning outcome | LO1 - Scope medium-scale project requirements to drive timely completions; LO2 - Develop project schedules and budgets |
| Duration | 75 minutes |
| Consumes | Lab 09 requirements register and RTM; Lab 10 product backlog; Lab 06 scope boundaries IN-1 to IN-10 and OUT-1 to OUT-7 |
| Produces | `artifacts/11-wbs.md`, `artifacts/11-wbs-dictionary.md`, `artifacts/11-scope-baseline.md` |

## Objectives

- State and apply the 100% rule, the single principle that makes a WBS correct or incorrect.
- Decompose the Contoso scope into a deliverable-oriented WBS to three levels.
- Apply the 8/80 rule and the estimate-and-assign test to decide when to stop decomposing.
- Write WBS dictionary entries detailed enough for someone else to execute the work package.
- Assemble the scope baseline and state exactly what it contains.
- Place control accounts and planning packages, and use rolling wave planning for work that is not yet knowable.
- Explain how a WBS and a product backlog coexist in a hybrid project without duplicating each other.

## The 100% rule and the decomposition rules

```text
THE 100% RULE - state it precisely, because the exam tests the precision

  The WBS includes 100% of the work defined by the project scope statement,
  and captures 100% of the deliverables - internal, external and interim -
  including project management.

  At EVERY level of decomposition, the sum of the work at the CHILD level
  must equal 100% of the work of the PARENT.

  Three consequences, each independently testable:
    NOTHING OUTSIDE   Work not in the WBS is not in the project. If it is
                      not in the WBS it is not funded, not scheduled and
                      not assigned. This is what makes the WBS a scope
                      control instrument.
    NOTHING MISSING   If a child level omits work the parent requires, the
                      parent is under-estimated and the gap surfaces later
                      as an overrun that looks like poor performance but
                      was actually poor decomposition.
    NO OVERLAP        Two elements must not contain the same work. Overlap
                      produces double-counted cost and disputed ownership.

DECOMPOSITION RULES

  DELIVERABLE-ORIENTED, NOT ACTIVITY-ORIENTED.  The classic exam trap.
    WBS elements are NOUNS - things that exist when the work is done.
    Activities are VERBS - and they belong in the ACTIVITY LIST in Lab 12,
    derived FROM the WBS, not in the WBS itself.
      CORRECT   1.4.1 Notification engine and templates
      WRONG     1.4.1 Build the notification engine
      CORRECT   1.9.1 Automated regression suite
      WRONG     1.9.1 Write automated tests
    Quick test: can you put "the completed" in front of it and have it
    make sense? "The completed notification engine" works. "The completed
    build the notification engine" does not.

  THE 8/80 RULE.  A work package should require between 8 and 80 hours of
    effort - roughly one day to two weeks.
      Under 8 hours   -> you are managing at task level; the overhead of
                         tracking exceeds the value of the control.
      Over 80 hours   -> too coarse to estimate accurately or to detect
                         slippage before it is expensive.
    It is a heuristic, not a law. Some organisations use 40/160. What is
    not optional is having a stated threshold and applying it consistently.

  THE "CAN I ESTIMATE AND ASSIGN IT" TEST.  Stop decomposing when:
      - the work can be realistically estimated for cost and duration,
      - it can be assigned to a single accountable owner,
      - progress against it can be measured,
      - and further breakdown would add control cost without control value.

  WHEN TO STOP - and when NOT to.  Different branches decompose to
    different depths. A WBS is not obliged to be symmetrical, and forcing
    every branch to level 4 for tidiness is a real error.

  ROLLING WAVE PLANNING.  Near-term work is decomposed to work-package
    detail; far-term work is left at a higher level as a PLANNING PACKAGE
    and decomposed as it approaches and becomes knowable. This is a form of
    progressive elaboration, and it is the honest response to the fact that
    detailed planning of week-22 work in week 1 produces detail, not
    accuracy.
```

## Steps

### Step 1 - Confirm the inputs and the boundary

The WBS decomposes the scope statement. Before decomposing, confirm what the boundary is, because the 100% rule is meaningless without a defined 100%.

| Input | Source | Effect on the WBS |
| --- | --- | --- |
| In-scope items IN-1 to IN-10 | Lab 06 charter | Every one must appear somewhere in the WBS, or the rule is broken |
| Out-of-scope items OUT-1 to OUT-7 | Lab 06 charter | None may appear anywhere in the WBS |
| Requirements REQ-001 to REQ-031 | Lab 09 register | Each traces to a WBS element via the RTM |
| Product backlog US-01 to US-24 | Lab 10 | Maps into the build branches, not alongside them |
| Compliance requirements C-01 to C-13 | Lab 04 register | Drives the existence of branch 1.8 |
| Environmental factor L1 | Lab 02 scan | The regulatory driver behind branch 1.8 |

```text
BOUNDARY CHECK before decomposing

  IN-1  responsive registration flow      -> 1.3
  IN-2  automated learner communications  -> 1.4
  IN-3  learner self-service              -> 1.5
  IN-4  PDPA consent and data rights      -> 1.8
  IN-5  SSG NRIC attendance, 7-yr retain  -> 1.8
  IN-6  payment gateway v2 integration    -> 1.6
  IN-7  data migration                    -> 1.7
  IN-8  automated regression suite        -> 1.9
  IN-9  WCAG 2.1 AA accessibility         -> 1.3
  IN-10 admin training and transition     -> 1.10

  All ten in-scope items have a home. No WBS element below corresponds to
  any of OUT-1 to OUT-7. The boundary holds.
```

### Step 2 - Build the WBS to three levels

Create `artifacts/11-wbs.md`. Render it as an indented tree with numbered codes.

```text
1.0  CONTOSO TRAINING PORTAL UPGRADE
     |
     +-- 1.1  Project Management
     |        +-- 1.1.1  Project management plan and governance
     |        +-- 1.1.2  Stakeholder engagement and communications
     |        +-- 1.1.3  Risk and issue management
     |        +-- 1.1.4  Gate reviews G1, G2, G3
     |        +-- 1.1.5  Project closure and lessons learned
     |
     +-- 1.2  Requirements and Design
     |        +-- 1.2.1  Requirements register and traceability matrix
     |        +-- 1.2.2  UX research, wireframes and design system
     |        +-- 1.2.3  Solution architecture and data model
     |        +-- 1.2.4  Design baseline package for G1
     |
     +-- 1.3  Registration Flow
     |        +-- 1.3.1  Course search and selection
     |        +-- 1.3.2  Responsive registration flow
     |        +-- 1.3.3  Accessibility WCAG 2.1 AA conformance
     |        +-- 1.3.4  Registration performance and capacity
     |
     +-- 1.4  Communications Engine
     |        +-- 1.4.1  Notification engine and delivery
     |        +-- 1.4.2  Communication template management
     |        +-- 1.4.3  Communication content set
     |
     +-- 1.5  Self-Service
     |        +-- 1.5.1  Booking view and history
     |        +-- 1.5.2  Reschedule and cancellation
     |        +-- 1.5.3  Learner profile and records download
     |
     +-- 1.6  Payments Integration
     |        +-- 1.6.1  Gateway v2 API integration
     |        +-- 1.6.2  Refund and payment failure handling
     |        +-- 1.6.3  Receipt and reconciliation output
     |
     +-- 1.7  Data Migration
     |        +-- 1.7.1  Legacy data profiling and cleansing
     |        +-- 1.7.2  Migration scripts and mapping
     |        +-- 1.7.3  Migration rehearsal and reconciliation report
     |
     +-- 1.8  Compliance and Security
     |        +-- 1.8.1  PDPA consent and purpose limitation
     |        +-- 1.8.2  SSG attendance data and 7-year retention
     |        +-- 1.8.3  Access audit logging and encryption
     |        +-- 1.8.4  Compliance evidence pack
     |        +-- 1.8.5  Penetration test and remediation
     |
     +-- 1.9  Quality and Test Automation
     |        +-- 1.9.1  Automated regression suite
     |        +-- 1.9.2  Performance and load test assets
     |        +-- 1.9.3  User acceptance test execution
     |        +-- 1.9.4  Defect management and resolution
     |
     +-- 1.10 Training and Transition
     |        +-- 1.10.1  Administrator training materials and delivery
     |        +-- 1.10.2  Learner communications and launch messaging
     |        +-- 1.10.3  Support desk handover and runbooks
     |
     +-- 1.11 Deployment and Launch
              +-- 1.11.1  Environment build and release pipeline
              +-- 1.11.2  Cutover plan and rollback position
              +-- 1.11.3  Go-live execution and hypercare
```

Check the 100% rule at each level before continuing:

```text
100% RULE VERIFICATION

  Level 1 -> Level 2:  Do 1.1 through 1.11 together constitute all of the
    work of 1.0? Test by asking what is left over. Project management is
    present (1.1) - the most commonly omitted branch, because it is work
    that produces no product feature but consumes real cost. Requirements
    and design are present (1.2). Every in-scope item IN-1 to IN-10 mapped
    in Step 1. Nothing remains. PASSES.

  Level 2 -> Level 3, checking 1.3:  Do 1.3.1 to 1.3.4 constitute all of
    the registration flow? Search and selection, the flow itself,
    accessibility, and performance. A learner searches, registers, does so
    accessibly, and does so fast. Nothing remains. PASSES.

  OVERLAP CHECK:  1.3.3 accessibility and 1.9.1 regression suite both
    involve testing. Is that overlap? No - 1.3.3 is the accessibility
    CONFORMANCE of the product, 1.9.1 is the automated regression ASSET.
    Distinguishing them requires the WBS dictionary, which is exactly why
    a WBS alone is not sufficient and why the dictionary is part of the
    scope baseline.

  ORPHAN CHECK:  Is any element present that traces to no requirement and
    no in-scope item? Run the check against the Lab 09 RTM. Any WBS element
    with no requirement behind it is either a missing RTM row or gold
    plating in the plan.
```

### Step 3 - Trace the compliance workstream to its origin

Branch 1.8 deserves a specific note, because it is the branch most likely to be questioned as overhead.

```text
WHY 1.8 COMPLIANCE AND SECURITY EXISTS - the full trace

  Lab 02, PESTLE/TECOP scan, factor L1
    "Legal - PDPA enforcement activity has increased; personal data
     handling in learner registration is directly exposed, and SSG
     funding data carries a statutory retention obligation."
    L1 scored high on both probability and impact in the scan.
                                |
                                v
  Lab 04, compliance register
    L1 decomposed into 13 specific compliance requirements C-01 to C-13,
    each with an owner and a measurement method. The DPO owns the gate.
                                |
                                v
  Lab 06, charter
    IN-4 (PDPA consent) and IN-5 (SSG attendance with 7-year retention)
    became explicit scope items. SC-5 made compliance clearance a
    measurable success criterion: pass with zero major findings at G3.
                                |
                                v
  Lab 09, requirements register and RTM
    C-01..C-13 traced to REQ-018, REQ-019, REQ-021, REQ-025, REQ-026,
    REQ-027 and their test cases. Coverage measured at 9/13, with four
    gaps identified and closed before baseline.
                                |
                                v
  Lab 11, THIS WBS
    Branch 1.8 exists so that compliance work is DECOMPOSED, ESTIMATED,
    SCHEDULED, ASSIGNED and FUNDED like every other deliverable.

  WHY THIS MATTERS. Compliance work that is not in the WBS is not in the
  budget and not on the schedule. It then gets done in whatever time is
  left, which on a fixed-date project is no time at all. Lab 03's
  lessons-learned entry recorded exactly this failure on the previous
  release. Putting compliance in the WBS as a first-class branch, with
  1.8.4 producing an evidence pack as a named deliverable, is the
  structural fix for that lesson.
```

### Step 4 - Write the WBS dictionary

Create `artifacts/11-wbs-dictionary.md`. A WBS code and a name are not enough to execute work. The dictionary entry is what a person who was not in the planning session needs.

Effort and cost figures below are the source data for Lab 13's bottom-up estimate - they must reconcile.

| Field | 1.3.2 |
| --- | --- |
| WBS code | 1.3.2 |
| Name | Responsive registration flow |
| Description | The learner-facing course registration flow, responsive across mobile, tablet and desktop, from course selection through to payment handoff. Includes single-form layout with a maximum of 12 input fields, client and server validation, save-and-resume state, and error recovery paths |
| Deliverable | A working, deployed registration flow meeting REQ-010 and REQ-011 |
| Acceptance criteria | Maximum 12 input fields verified; median completion under 4:00 in usability testing with 8 real learners; save-and-resume works from the same step within 7 days; zero critical defects at G2 |
| Responsible role | Development team lead |
| Effort estimate | 70 person-days (developer) |
| Cost estimate | 70 x SGD 620 = SGD 43,400 |
| Predecessor | 1.2.2 UX wireframes and design system; 1.2.3 solution architecture |
| Quality requirement | Meets REQ-022 performance budget; covered by 1.9.1 regression suite |
| Stories | US-02, US-05 |
| Control account | CA-3 Registration |

| Field | 1.3.1 |
| --- | --- |
| WBS code | 1.3.1 |
| Name | Course search and selection |
| Description | Course search, filtering and detail views, available to guest users without authentication. Filters on title, category, date and location |
| Deliverable | Deployed guest-accessible search and course detail pages |
| Acceptance criteria | Guest user retrieves a target course within 3 interactions; no login prompt before the registration step; results return within the REQ-022 performance budget |
| Responsible role | Development team lead |
| Effort estimate | 56 person-days (developer) |
| Cost estimate | 56 x SGD 620 = SGD 34,720 |
| Predecessor | 1.2.2 UX wireframes; 1.2.3 solution architecture |
| Quality requirement | REQ-022 page load; covered by 1.9.1 |
| Stories | US-01 |
| Control account | CA-3 Registration |

| Field | 1.3.3 |
| --- | --- |
| WBS code | 1.3.3 |
| Name | Accessibility WCAG 2.1 AA conformance |
| Description | Accessibility conformance work across all learner-facing pages: semantic markup, ARIA labelling, keyboard navigation, focus management, colour contrast at 4.5:1, and text resize to 200% without loss of function |
| Deliverable | Learner-facing pages conforming to WCAG 2.1 level AA, with an audit report |
| Acceptance criteria | Automated scan plus manual audit return zero level A and zero level AA failures; keyboard-only completion of the full registration flow demonstrated |
| Responsible role | UX designer with development team lead |
| Effort estimate | 20 person-days (developer) |
| Cost estimate | 20 x SGD 620 = SGD 12,400 |
| Predecessor | 1.2.2 UX design system |
| Quality requirement | REQ-025, compliance requirement C-11 |
| Stories | US-04 |
| Control account | CA-3 Registration |
| Note | Built in, not retrofitted. Lab 04 costed retrofit at SGD 40,000 against SGD 8,000 of incremental design cost when built in. This entry is the plan's commitment to the cheaper path |

| Field | 1.4.1 |
| --- | --- |
| WBS code | 1.4.1 |
| Name | Notification engine and delivery |
| Description | The engine that generates and dispatches learner communications on booking, reminder, reschedule, cancellation and completion events, including delivery tracking, retry on failure, and bounce handling |
| Deliverable | Deployed notification engine with the five event types operational |
| Acceptance criteria | Confirmation delivered within 60 seconds at the 95th percentile over 100 test bookings; reminder dispatched between 47 and 49 hours before session start; retry on transient failure verified |
| Responsible role | Development team lead |
| Effort estimate | 52 person-days (developer) |
| Cost estimate | 52 x SGD 620 = SGD 32,240 |
| Predecessor | 1.2.3 solution architecture; 1.3.2 registration flow (booking events originate there) |
| Quality requirement | REQ-012, REQ-013, REQ-014; covered by 1.9.1 |
| Stories | US-06, US-07, US-08 |
| Control account | CA-4 Communications |

| Field | 1.5.1 |
| --- | --- |
| WBS code | 1.5.1 |
| Name | Booking view, reschedule and cancellation |
| Description | Learner self-service functions: view all past and upcoming bookings with status, reschedule to another session of the same course, and cancel with refund initiation per the cancellation policy |
| Deliverable | Deployed self-service booking management area |
| Acceptance criteria | A learner completes a reschedule and a cancellation unaided in usability testing; refund initiated within the policy window; all bookings display with correct status |
| Responsible role | Development team lead |
| Effort estimate | 58 person-days (developer) |
| Cost estimate | 58 x SGD 620 = SGD 35,960 |
| Predecessor | 1.3.2 registration flow; 1.6.2 refund handling |
| Quality requirement | REQ-015, REQ-016, REQ-017; covered by 1.9.1 |
| Stories | US-09, US-10, US-12 |
| Control account | CA-5 Self-Service |

| Field | 1.6.1 |
| --- | --- |
| WBS code | 1.6.1 |
| Name | Gateway v2 API integration |
| Description | Integration with the payment gateway v2 API supporting card and PayNow methods, including tokenisation, 3-D Secure handling, and the payment status callback path |
| Deliverable | Deployed payment integration operating against gateway v2 in production |
| Acceptance criteria | End-to-end payment succeeds in both methods against the v2 sandbox and against production; failure paths return the learner to a recoverable state; no card data stored on Contoso infrastructure |
| Responsible role | Development team lead |
| Effort estimate | 46 person-days (developer) |
| Cost estimate | 46 x SGD 620 = SGD 28,520 |
| Predecessor | 1.2.3 solution architecture; sprint 1 spike validating assumption A-03 |
| Quality requirement | REQ-020, compliance requirement C-05 |
| Stories | US-11 |
| Control account | CA-6 Payments |
| Note | Assumption A-03 (v2 API stable and documented) is validated by a sprint 1 spike. Lab 14 carries the decision tree for v2-now versus v1-and-migrate-later |

| Field | 1.7.1 |
| --- | --- |
| WBS code | 1.7.1 |
| Name | Legacy data profiling, migration scripts and reconciliation |
| Description | Profiling of legacy learner and booking data, cleansing and de-duplication rules, migration scripts for active learner profiles and bookings within 24 months, and the reconciliation report proving completeness |
| Deliverable | Migrated data set in production with a signed reconciliation report |
| Acceptance criteria | Record counts match within zero variance; every exception individually explained and dispositioned; bookings older than 24 months correctly excluded per OUT-6; rehearsed at least once before cutover |
| Responsible role | DevOps engineer with business analyst |
| Effort estimate | 30 person-days (DevOps) |
| Cost estimate | 30 x SGD 700 = SGD 21,000 |
| Predecessor | 1.2.3 data model; 1.8.2 retention rules |
| Quality requirement | REQ-027, REQ-008, compliance requirement C-12 |
| Stories | US-19 |
| Control account | CA-7 Migration |
| Note | Assumption A-04 (legacy data clean enough to migrate) is unvalidated at plan time. Profiling in sprint 2 is the validation, and risk R-04 in Lab 14 carries the exposure if it proves false |

| Field | 1.8.1 |
| --- | --- |
| WBS code | 1.8.1 |
| Name | PDPA consent, purpose limitation and data rights |
| Description | Consent capture at the point of personal data collection with the purpose stated, versioned consent records, purpose limitation enforcement, and the learner-facing data access and correction request path |
| Deliverable | Deployed consent and data rights capability with the DPO's written acceptance |
| Acceptance criteria | Consent record stored with timestamp, consent text version and stated purpose; access and correction requests fulfilled within the statutory window in a scripted test; DPO reviews and accepts with zero major findings |
| Responsible role | Business analyst with development team lead; DPO approves |
| Effort estimate | 38 person-days (developer) |
| Cost estimate | 38 x SGD 620 = SGD 23,560 |
| Predecessor | 1.2.3 data model; must be built WITH 1.3.2, not after it |
| Quality requirement | REQ-018, REQ-021, compliance requirements C-01, C-02, C-09 |
| Stories | US-13, US-15 |
| Control account | CA-8 Compliance |
| Note | Sequenced into sprint 2 alongside the registration form deliberately. Privacy by design was the Lab 07 engagement action for the DPO and the Lab 03 lesson - consent bolted onto a finished form is rework |

| Field | 1.9.1 |
| --- | --- |
| WBS code | 1.9.1 |
| Name | Automated regression suite |
| Description | An automated regression test suite covering the registration and communications paths, integrated into the continuous integration pipeline and executing on every build |
| Deliverable | A regression suite running in CI with a published coverage report |
| Acceptance criteria | Suite executes on every build; covers all paths in REQ-009 to REQ-017; run completes within the CI time budget; coverage report published to the team |
| Responsible role | QA lead |
| Effort estimate | 86 person-days (QA lead) |
| Cost estimate | 86 x SGD 590 = SGD 50,740 |
| Predecessor | 1.3.2, 1.4.1, 1.5.1 - tests follow the features they cover |
| Quality requirement | REQ-030, REQ-031 |
| Stories | US-21 |
| Control account | CA-9 Quality |

```text
DICTIONARY EFFORT SUMMARY - carried forward to Lab 13

  1.1.1  Project management and governance     42 days   BA      SGD 26,880
  1.2.1  Requirements register and RTM         34 days   BA      SGD 21,760
  1.3.1  Course search and selection           56 days   Dev     SGD 34,720
  1.3.2  Responsive registration flow          70 days   Dev     SGD 43,400
  1.3.3  Accessibility WCAG 2.1 AA             20 days   Dev     SGD 12,400
  1.4.1  Notification engine and delivery      52 days   Dev     SGD 32,240
  1.5.1  Booking view, reschedule, cancel      58 days   Dev     SGD 35,960
  1.6.1  Gateway v2 API integration            46 days   Dev     SGD 28,520
  1.7.1  Data profiling and migration          30 days   DevOps  SGD 21,000
  1.8.1  PDPA consent and data rights          38 days   Dev     SGD 23,560
  1.9.1  Automated regression suite            86 days   QA      SGD 50,740
  1.11.1 Release engineering and cutover       24 days   DevOps  SGD 16,800
                                              ---------          ----------
                                              556 days          SGD 347,980

  This reconciles to the charter's SGD 348,000 development line within
  SGD 20. Lab 13 will explain that reconciliation and add the non-labour
  categories on top.
```

### Step 5 - Place control accounts and planning packages

```text
CONTROL ACCOUNT
  A management control point where scope, budget and schedule are
  integrated and compared to earned value for performance measurement.
  It sits ABOVE work packages in the WBS - one control account contains
  one or more work packages. It is the level at which cost performance is
  MEASURED and REPORTED, and it is the unit Lab 20's earned value analysis
  operates on. Each control account has exactly ONE accountable owner.

PLANNING PACKAGE
  A WBS component BELOW a control account but ABOVE a work package, with
  known work content but no detailed schedule activities yet. It is the
  placeholder for rolling wave planning: the budget is held, the work is
  identified, the decomposition has not happened because the information
  does not yet exist.

  The order is always: control account -> planning package -> work package.
  Planning packages convert into work packages as the wave rolls forward.
```

| Control account | WBS elements | Owner | Budget (SGD) |
| --- | --- | --- | --- |
| CA-1 Project Management | 1.1.1 - 1.1.5 | Project manager | 26,880 |
| CA-2 Requirements and Design | 1.2.1 - 1.2.4 | Business analyst | 55,760 |
| CA-3 Registration | 1.3.1 - 1.3.4 | Development team lead | 90,520 |
| CA-4 Communications | 1.4.1 - 1.4.3 | Development team lead | 32,240 |
| CA-5 Self-Service | 1.5.1 - 1.5.3 | Development team lead | 35,960 |
| CA-6 Payments | 1.6.1 - 1.6.3 | Development team lead | 28,520 |
| CA-7 Migration | 1.7.1 - 1.7.3 | DevOps engineer | 21,000 |
| CA-8 Compliance | 1.8.1 - 1.8.5 | Business analyst, DPO approves | 23,560 |
| CA-9 Quality | 1.9.1 - 1.9.4 | QA lead | 50,740 |
| CA-10 Training and Transition | 1.10.1 - 1.10.3 | Content lead | 17,760 |
| CA-11 Deployment and Launch | 1.11.1 - 1.11.3 | DevOps engineer | 16,800 |

Rolling wave: two branches are deliberately left as planning packages at baseline.

| Planning package | Why it is not yet decomposed | Decompose by |
| --- | --- | --- |
| 1.9.3 User acceptance test execution | UAT scenarios depend on which stories actually shipped by G2. Decomposing in week 1 would produce a plan for a product that does not yet exist | End of sprint 8, week 16 |
| 1.11.3 Go-live execution and hypercare | The cutover runbook depends on the migration rehearsal result from 1.7.3 and the final infrastructure topology | End of sprint 10, week 20 |

```text
The honest reason for rolling wave, stated plainly: decomposing 1.9.3 in
week 1 would produce a detailed and confident plan that is wrong. Holding
the budget at planning-package level and decomposing at week 16 produces a
less impressive-looking plan that is right. The exam prefers the second,
and so does the project.
```

### Step 6 - Assemble the scope baseline

```text
THE SCOPE BASELINE - memorise these three components

  SCOPE BASELINE  =  PROJECT SCOPE STATEMENT
                  +  WBS
                  +  WBS DICTIONARY

  All three. Not the WBS alone. This is directly and frequently tested.

  Why all three are necessary:
    The SCOPE STATEMENT gives the narrative boundary - deliverables,
      acceptance criteria, exclusions, assumptions and constraints. It is
      the document the 100% rule measures the WBS against.
    The WBS gives the structure - the hierarchical decomposition that
      makes the scope countable and assignable.
    The WBS DICTIONARY gives the detail - without it, two people read
      "1.3.3 Accessibility conformance" and plan different work. The
      overlap check in Step 2 could not be resolved by the WBS alone.

  The scope baseline is an approved version. It changes ONLY through
  formal change control - the Lab 03 thresholds and the CCB. Together with
  the SCHEDULE BASELINE (Lab 12) and the COST BASELINE (Lab 13), it forms
  the PERFORMANCE MEASUREMENT BASELINE that Lab 20 measures against.
```

Create `artifacts/11-scope-baseline.md` containing all three components with a version number and an approval block.

### Step 7 - Reconcile the WBS with the product backlog

This is the real hybrid tailoring question, and it is the one most often answered badly - usually by maintaining both artifacts as duplicates and letting them drift apart.

| | WBS | Product backlog |
| --- | --- | --- |
| Structure | Hierarchical decomposition | Flat ordered list |
| Orientation | Deliverable-oriented, nouns | Value-oriented, user outcomes |
| Contains | 100% of project work, including project management, training, migration, compliance evidence | Product functionality the product owner prioritises |
| Stability | Baselined; changes via change control | Reordered every sprint by the product owner without change control |
| Estimating unit | Person-days and cost | Story points |
| Time horizon | Whole project | Next few sprints in detail, rest coarse |
| Primary purpose | Scope control, cost baseline, earned value measurement | Prioritisation and sprint planning |
| Who owns it | Project manager | Product owner |

```text
HOW BOTH COEXIST AT CONTOSO - the tailoring decision

  The WBS is the SUPERSET. It contains everything, including a great deal
  of work that will never appear in the backlog: gate reviews, the
  compliance evidence pack, administrator training, the migration
  reconciliation report, release engineering, project management itself.
  A backlog of user stories cannot express "produce the G3 evidence pack",
  because no user wants it - the regulator does.

  The BACKLOG decomposes only the BUILD branches - 1.3, 1.4, 1.5, 1.6 and
  parts of 1.8 and 1.9 - into user-valued increments that can be
  prioritised and reordered.

  THE MAPPING RULE that keeps them consistent:
    Every user story maps to exactly ONE work package.
    A work package may contain MANY stories.
    No story exists without a work package - if one appears that maps to
    nothing, either the WBS is incomplete or the story is out of scope.

    Examples from the dictionary above:
      1.3.2 Responsive registration flow   <-  US-02, US-05
      1.4.1 Notification engine            <-  US-06, US-07, US-08
      1.5.1 Booking view and reschedule    <-  US-09, US-10, US-12
      1.8.1 PDPA consent and data rights   <-  US-13, US-15
      1.9.1 Automated regression suite     <-  US-21
      1.1.4 Gate reviews                   <-  NO STORIES. Correct - this
                                               is project work, not
                                               product functionality.

  WHERE THE CONTROL BOUNDARY SITS:
    Changing the ORDER of stories within a work package     -> product
      owner, any sprint, no change request.
    Changing the SIZE or CONTENT of a work package          -> change
      request, because it moves the cost baseline.
    Adding a story that maps to no existing work package    -> change
      request, because it is new scope by definition.

  This is the operational expression of the Lab 06 sentence "the scope
  BASELINE is fixed at the Must-have level and change-controlled; within
  that envelope, priority and sequence are the product owner's to change".
  The WBS is the envelope. The backlog moves inside it.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
A team member submits this level-3 WBS element for review:
    1.4.2  Write and test the email template code
What is wrong with it, and what should it be?

  A. Nothing; it is specific and clear.
  B. It is activity-oriented. WBS elements are deliverables expressed as
     nouns; verbs belong in the Lab 12 activity list. It should read
     "1.4.2 Communication template management", with "write" and "test"
     appearing as activities derived from it.
  C. It is too small and breaches the 8/80 rule.
  D. It belongs under 1.9 Quality because it mentions testing.

SCENARIO 2
During execution, the team discovers that a required data cleansing step
was never included anywhere in the WBS. It will take 12 person-days. What
does this tell you, and what is the correct response?

  A. Absorb it into 1.7.1, since it is clearly migration work.
  B. The 100% rule was broken - work required by the scope statement was
     missing from the WBS, which means it was never estimated, scheduled
     or funded. Raise it as a change request with its cost and schedule
     impact, assess it against the Lab 03 thresholds, and update the WBS,
     the dictionary and the cost baseline if approved.
  C. Add it to the WBS quietly and continue; the WBS is a living document.
  D. Treat it as a risk and fund it from the contingency reserve.

SCENARIO 3
The product owner reorders the backlog mid-sprint-planning, moving US-17
(administrator template editing, a Should) ahead of US-12 (booking view, a
Must). Both map to work packages already in the scope baseline. Does this
require a change request?

  A. Yes - any change to planned sequence requires change control.
  B. Yes - moving a Should ahead of a Must changes the scope baseline.
  C. No - reordering backlog items inside the baselined scope envelope is
     the product owner's authority under the hybrid model, because no work
     package is being added, removed or resized. But the PM should confirm
     the Must-haves still complete before G2, since that commitment is a
     baseline commitment.
  D. No - the product owner has unlimited authority over the backlog.
```

Answer key:

```text
SCENARIO 1 -> B.  The deliverable-versus-activity distinction is the most
            heavily tested WBS point. Apply the "the completed" test:
            "the completed write and test the email template code" is not
            English, which tells you it is not a deliverable. C is wrong
            because the 8/80 rule governs effort, and nothing here states
            the effort. D is wrong because testing performed as part of
            producing a deliverable belongs with that deliverable - only
            the regression suite as an ASSET belongs under 1.9.

SCENARIO 2 -> B.  Missing work is a 100% rule failure, and naming it as
            such matters more than the 12 days. A hides a baseline defect
            inside an existing work package, which corrupts that package's
            cost performance in Lab 20's earned value and makes it look
            like the migration team overran when in fact the plan was
            incomplete. C is the same error stated more honestly - a
            baselined WBS is precisely NOT a document you update quietly.
            D is the most tempting wrong answer and worth understanding:
            contingency reserve funds identified RISKS that may or may not
            occur. This is not a risk. It is certain, required work that
            was omitted. Funding known scope from contingency depletes the
            reserve that real risks need and disguises a planning error as
            a risk event.

SCENARIO 3 -> C.  This is the hybrid control boundary in operation. No
            work package changes size, content or existence, so the scope
            baseline is untouched and no change request is required - that
            flexibility is exactly what the Lab 06 approach decision
            granted. But the answer is not simply "no": the PM retains the
            baseline commitment that all Must-haves complete before G2, so
            the correct response includes verifying that this reordering
            does not put that commitment at risk. D is wrong for the same
            reason - the product owner's authority is real but bounded by
            the baselined envelope.
```

## Deliverable

Submit to `artifacts/`:

- `11-wbs.md` - the full WBS to three levels as an indented numbered tree, covering all eleven level-2 branches, with the 100% rule verified at each level and the overlap and orphan checks recorded.
- The trace showing why branch 1.8 exists, from Lab 02 factor L1 through Lab 04, Lab 06 and Lab 09 to this WBS.
- `11-wbs-dictionary.md` - at least 8 fully populated entries, each with WBS code, name, description, deliverable, acceptance criteria, responsible role, effort estimate, cost estimate, predecessor and quality requirement.
- The control account table with owners and budgets, and at least two planning packages with their decomposition dates and the reason they are not yet decomposed.
- `11-scope-baseline.md` - scope statement plus WBS plus WBS dictionary, versioned and with an approval block.
- The WBS-versus-backlog comparison, the mapping rule, and the statement of where the change control boundary sits.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every WBS element is a noun phrase. If any element begins with a verb, it is an activity and belongs in Lab 12.
- Your WBS contains a project management branch. A WBS with no 1.1 does not include 100% of the work, because managing the project is work that consumes budget.
- Every one of IN-1 to IN-10 maps to a WBS element, and none of OUT-1 to OUT-7 appears anywhere.
- You verified the 100% rule at each level by asking what is left over, not by assuming.
- Your work package efforts sum to SGD 347,980, reconciling to the charter's SGD 348,000 development line. If they do not, Lab 13 will not reconcile either.
- Every dictionary entry has acceptance criteria that someone outside the planning session could apply without asking a question.
- You can state the three components of the scope baseline without hesitating, and explain why the WBS alone is insufficient.
- You have at least one planning package, and you can explain why decomposing it now would produce detail rather than accuracy.
- You can state which backlog changes require a change request and which do not, and locate the boundary at the work package.
