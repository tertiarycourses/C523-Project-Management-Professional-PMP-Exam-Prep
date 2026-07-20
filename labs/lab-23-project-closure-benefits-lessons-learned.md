# Lab 23 - Project Closure, Benefits Realisation and Lessons Learned

| Field | Value |
| --- | --- |
| Topic | 6 - Close the Project |
| ECO 2026 task | Process T10 - Manage project closure; Business Environment T6 - Support organizational change and continuous improvement; People T7 - Help ensure knowledge transfer |
| Duration | 105 minutes |
| Consumes | Lab 05 benefits map B1-B4; Lab 06 charter success criteria SC-1 to SC-8; Lab 09 requirements traceability matrix; Lab 14 risk register; Lab 20 EVM final position; Lab 21 root cause analysis and corrective actions; Lab 04 compliance register |
| Produces | `artifacts/23-closure-checklist.md`, `artifacts/23-final-report.md`, `artifacts/23-lessons-learned.md`, `artifacts/23-benefits-realisation.md`, `artifacts/23-transition-plan.md` |

## Objectives

- Close the project against the four ECO Process T10 enablers rather than against a feeling that the work is finished.
- Separate Validate Scope from Control Quality, and administrative closure from procurement closure.
- Report all eight charter success criteria honestly, including the one that was missed.
- Hand every benefit to a named business owner with a review date beyond project end, because benefits are realised after closure.
- Convert the project's real events into lessons that each update a named organisational process asset.
- Plan knowledge transfer, transition to operations and team release.

## What closure actually is

```text
THE FOUR ECO T10 ENABLERS - these structure this entire lab

  1. DETERMINE CRITERIA TO SUCCESSFULLY CLOSE THE PROJECT
     What does "closed" mean here? Written down BEFORE you start closing,
     otherwise closure becomes a negotiation you will lose.

  2. OBTAIN STAKEHOLDER APPROVAL OF PROJECT COMPLETION
     Formal, named, signed acceptance of deliverables. Not a thumbs-up
     in a corridor.

  3. VALIDATE READINESS FOR TRANSITION TO OPERATIONS
     Can the receiving organisation actually run this? Runbooks,
     monitoring, trained support, escalation, hypercare.

  4. CONCLUDE ACTIVITIES TO CLOSE THE PROJECT OR PHASE
     Lessons learned, retrospectives, procurement closure, financial
     closure, resource release, archiving.

VALIDATE SCOPE versus CONTROL QUALITY - the most tested distinction here

  CONTROL QUALITY   Is the deliverable CORRECT? Does it meet the written
                    SPECIFICATION? Performed INTERNALLY, by QA.
                    Output: VERIFIED deliverables.
                    Comes FIRST.

  VALIDATE SCOPE    Does the CUSTOMER ACCEPT it? Performed WITH the
                    customer or sponsor.
                    Output: ACCEPTED deliverables, and formal sign-off.
                    Comes SECOND.

  The order is fixed and the exam tests it. You never present an unverified
  deliverable to a customer for acceptance. If a question shows a PM taking
  deliverables straight to the sponsor for sign-off without QA having
  verified them, that is the error in the question.

  Memory hook: QUALITY is about CORRECTNESS (internal, technical).
               SCOPE is about ACCEPTANCE (external, contractual).

ADMINISTRATIVE versus PROCUREMENT CLOSURE

  PROCUREMENT CLOSURE   Closes CONTRACTS. Verify the seller delivered,
                        settle claims, make final payment, issue formal
                        written notice of contract completion, archive
                        the procurement file. Happens per contract, and
                        can happen mid-project when a contract ends.
                        Must be complete BEFORE administrative closure.

  ADMINISTRATIVE CLOSURE Closes the PROJECT. Final report, lessons
                        learned, OPA updates, resource release, archive.
                        Happens ONCE, at the end.

TERMINATED PROJECTS ARE STILL CLOSED
  A cancelled project gets the full closure process: what was produced is
  documented, what was learned is captured, contracts are closed, resources
  are released, and the reason for termination is recorded. The single most
  common exam error is assuming closure only applies to successful projects.
  If anything, a terminated project's lessons are worth more.
```

## Steps

### Step 1 - Define the closure criteria before closing anything

Create `artifacts/23-closure-checklist.md`. Enabler 1 requires you to state what "closed" means before you begin. These twenty items are the Contoso closure criteria.

| # | Category | Closure criterion | Evidence required | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| C-01 | Deliverable acceptance | All Must-have backlog items delivered or formally descoped by approved change request | Lab 10 backlog, CR-14 approval | PM | |
| C-02 | Deliverable acceptance | Every deliverable verified by QA against specification before acceptance | Lab 22 QA verification records | QA Lead | |
| C-03 | Scope verification | 100% of Must-have requirements in the Lab 09 RTM traced to a passing test | RTM final pass | BA | |
| C-04 | Scope verification | All descoped items recorded with the change request that removed them | CR-14 and phase-2 register | PM | |
| C-05 | Acceptance | Formal signed acceptance from product owner, DPO, IT Ops Manager and sponsor | Sign-off table, Step 3 | PM | |
| C-06 | Compliance | All 13 Lab 04 compliance requirements evidenced and cleared at G3 | Compliance evidence pack, DPO opinion | DPO | |
| C-07 | Financial | All invoices received, approved and paid; no open commitments | Finance ledger, purchase order register | Finance | |
| C-08 | Financial | Final actual cost reconciled to the Lab 13 cost baseline and Lab 20 EVM | Reconciliation statement | PM | |
| C-09 | Financial | Unused contingency reserve formally released back to the business | Reserve statement | PM | |
| C-10 | Financial | Project cost centre closed to further charging | Finance confirmation | Finance | |
| C-11 | Procurement | Payment gateway vendor engagement verified complete, final payment made, written notice of completion issued | Contract file | PM |  |
| C-12 | Procurement | Penetration test supplier engagement closed, claims settled, no open disputes | Contract file | PM | |
| C-13 | Resource release | All 9 team members formally released with written notice to functional managers | Release memo | PM | |
| C-14 | Resource release | Performance feedback provided to each team member's line manager | Feedback records | PM | |
| C-15 | Documentation | All artifacts from Labs 01-22 archived to the project repository in the OPA structure | Archive index | PM | |
| C-16 | Documentation | Configuration items baselined and version-stamped at go-live | Configuration register | DevOps | |
| C-17 | Transition | IT Operations formally accepts supportability; runbooks, monitoring and escalation in place | Transition readiness table, Step 4 | IT Ops Mgr | |
| C-18 | Transition | Support desk trained; known-defect list handed over; hypercare period agreed and staffed | Hypercare plan | Support desk lead | |
| C-19 | Benefits | Each of B1-B4 assigned to a named business owner with review dates at 30, 90 and 180 days | Benefits handover table, Step 6 | Sponsor | |
| C-20 | Lessons learned | Lessons-learned repository updated; every lesson names the OPA it changes | Lessons register, Step 7 | PM | |

```text
THE RULE THAT MAKES THIS LIST WORK
  Every criterion has EVIDENCE and an OWNER. A checklist item reading
  "project documentation complete" with no evidence column is a wish.
  "Archive index exists and lists every Lab 01-22 artifact" can be checked
  by someone who was not on the project - which is the actual test.
```

### Step 2 - Verify scope before seeking acceptance

Control Quality comes first. Run the RTM closure check before anyone signs anything.

| Requirement class | In Lab 09 RTM | Delivered and test-passed | Descoped by CR | Outstanding |
| --- | --- | --- | --- | --- |
| Must have | 41 | 41 | 0 | 0 |
| Should have | 23 | 19 | 4 | 0 |
| Could have | 14 | 3 | 11 | 0 |
| Compliance (Lab 04) | 13 | 13 | 0 | 0 |
| **Total** | **91** | **76** | **15** | **0** |

```text
SCOPE VERIFICATION ARITHMETIC
  41 + 23 + 14 + 13 = 91 requirements in the RTM.
  76 delivered + 15 descoped + 0 outstanding = 91.  Reconciles.

  Must-have completion   41/41   = 100%
  Compliance completion  13/13   = 100%
  Should-have completion 19/23   = 82.6%
  Could-have completion   3/14   = 21.4%

THE FOUR DESCOPED SHOULD-HAVES
  Two were removed by CR-14, the Board's Option 2 decision from Lab 20
  (scope reduction of approximately SGD 45,000 in place of a ceiling
  variation). Two more were removed at sprint 10 when the Lab 21
  corrective actions consumed refinement capacity.
  All four are in the phase-2 register with a decision date.

  NONE of the 15 descoped items touches a charter success criterion
  SC-1 to SC-8, and none touches a compliance requirement. That is the
  test of whether a descope was legitimate, and it is why the Lab 20
  recommendation identified the LOWEST-VALUE Should-haves specifically.

  A descope with no change request behind it is not a descope. It is
  undelivered scope, and at closure it is a failure, not a decision.
```

### Step 3 - Obtain formal acceptance (enabler 2)

Acceptance criteria must be stated per deliverable, and the accepting party must be the person who can actually judge it.

| Deliverable | Acceptance criteria | Accepted by | Role | Basis of their authority |
| --- | --- | --- | --- | --- |
| Registration flow (WBS 1.3) | Median completion under 4 min on mobile and desktop; WCAG 2.1 AA conformance report clean | Marcus Tan | Product Owner, S-03 | Owns the product backlog and its acceptance criteria |
| Communications engine (WBS 1.4) | All five communication types firing correctly against the test matrix; manual effort measured under 5 hrs/week | Marcus Tan | Product Owner, S-03 | Owns L&D Ops process |
| Self-service and payments (WBS 1.5, 1.6) | Reschedule, cancel and payment paths pass UAT with zero severity-1 defects | Marcus Tan | Product Owner, S-03 | Owns the learner journey |
| Compliance evidence pack (WBS 1.8.4) | All 13 Lab 04 requirements evidenced; zero major findings | DPO | S-04 | Holds the G3 gate; regulatory authority |
| Data migration (WBS 1.7) | Reconciliation report shows 100% of active learner and booking records migrated and balanced | Marcus Tan and IT Ops Manager | S-03, S-11 | Data owner and platform owner jointly - note this is JOINT ACCEPTANCE of one deliverable, which is permitted; it is ACCOUNTABILITY that cannot be shared |
| Platform supportability (WBS 1.11) | Runbooks complete, monitoring live, escalation path tested, hypercare staffed | IT Operations Manager | S-11 | Receives the system into operational support |
| Administrator training (WBS 1.10.1) | All 3 admin staff assessed competent on the new process | Marcus Tan | S-03 | Their line manager |
| Overall project completion | All 20 closure criteria met; final report accepted | Priya Nathan | Sponsor, COO, S-01 | Issued the charter; only the issuer can close it |

```text
THE SEQUENCE THAT MUST NOT BE INVERTED

  QA verifies (Control Quality)  ->  customer accepts (Validate Scope)
       Lab 22 records                    this table

  Note S-11, the IT Operations Manager. In Lab 07 the salience model
  classified him DOMINANT - real authority, no current claim - with the
  note "will become definitive at handover. Engage early or inherit an
  objection late." This table is that handover. Because the Lab 07
  engagement action put him in the G1 and G2 architecture reviews, his
  acceptance at closure is a formality rather than a fight. Had he first
  seen the system in week 26, the supportability objection would have
  arrived with the project already over.

  ONE ACCEPTANCE WAS CONDITIONAL AND YOU MUST REPORT IT AS SUCH:
  the IT Operations Manager accepted supportability SUBJECT TO the 12
  known low-severity defects being fixed within the hypercare window.
  A conditional acceptance is a real acceptance with a real condition
  attached. Record the condition, its owner and its date - do not round
  it up to "accepted" in the final report.
```

### Step 4 - Validate readiness for transition to operations (enabler 3)

Create `artifacts/23-transition-plan.md`. This is a go/no-go assessment, not a summary.

| # | Readiness criterion | Threshold | Actual at week 26 | Go / No-go |
| --- | --- | --- | --- | --- |
| T-01 | Operational runbooks written and reviewed | All 9 runbooks complete and walked through by IT Ops | 9 of 9 complete, walkthrough 24 June | Go |
| T-02 | Monitoring and alerting live | Registration funnel, payment path, notification queue, error rate all alarmed | 4 of 4 live; thresholds tuned in the migration rehearsal | Go |
| T-03 | Support desk trained | All 4 support staff assessed competent; scripts published | 4 of 4 competent, scripts live 26 June | Go |
| T-04 | Escalation path defined and tested | 3-tier path with named on-call and tested paging | Tested 27 June, page acknowledged in 4 min | Go |
| T-05 | Known-defect list handed over | Every open defect listed with severity, workaround and target fix | 12 open, all severity 3 or 4, workarounds documented | Go, conditional |
| T-06 | Hypercare defined and staffed | 4 weeks, named staff, agreed response times | Agreed, staffed, see hypercare plan below | Go |
| T-07 | Warranty and support arrangement | Written support model beyond hypercare, with funding | Business-as-usual support from week 31, funded from the 61,000 hosting and maintenance line | Go |
| T-08 | Rollback position retained | Legacy portal available read-only for 90 days | Retained until 28 September | Go |
| T-09 | Admin staff operationally competent | All 3 assessed | 3 of 3 assessed competent 20 June | Go |
| T-10 | Data migration reconciled | 100% of active records balanced | 100%, reconciliation report signed | Go |
| T-11 | Compliance clearance current | G3 passed, zero major findings | Passed 18 June, zero major, 2 minor closed | Go |
| T-12 | IT Ops formal sign-off | Signed | Signed conditional on T-05 | Go, conditional |

```text
HYPERCARE PLAN - Contoso Training Portal Upgrade

  PERIOD          4 weeks, 30 June to 28 July (project weeks 26 to 30)
  WHY 4 WEEKS     Covers the July intake enrolment peak, which is the
                  highest-volume registration window of the year and the
                  reason the launch date was fixed in the first place.
                  Hypercare that ends before the first peak has not been
                  tested by anything.

  STAFFING        Week 1-2: Dev Lead at 50%, QA Lead at 30%, DevOps at 30%
                  Week 3-4: Dev Lead at 20%, DevOps at 20%
                  Support desk owns first line from day 1.
                  NOTE: this staffing is why C-13 resource release is
                  STAGED, not immediate. Releasing the whole team on
                  30 June would leave the peak unsupported.

  RESPONSE TIMES  Severity 1 (registration or payment down)  30 minutes
                  Severity 2 (function degraded)              4 hours
                  Severity 3 (workaround exists)              2 business days
                  Severity 4 (cosmetic)                       next release

  EXIT CRITERIA   All of the following, assessed 28 July:
                  - Zero open severity 1 or 2 defects
                  - Ticket volume at or below 40 per week for 2 weeks
                  - Support desk resolving 90% at first line
                  - The 12 handover defects closed or formally accepted
                    into business-as-usual backlog by IT Ops
                  If exit criteria are not met, hypercare EXTENDS. It does
                  not simply expire on the calendar.

  HANDOVER POINT  On exit, the product becomes a business-as-usual service
                  under the IT Operations Manager. The project is already
                  closed by then - which is precisely why the exit criteria
                  and their owner must be written down BEFORE closure.
```

```text
THE POINT OF A TRANSITION ASSESSMENT
  Every criterion has a THRESHOLD set in advance and an ACTUAL measured
  against it. A readiness review where the threshold is decided after
  seeing the actual is not a review; it is a rationalisation.
  Note T-05 and T-12 are recorded as CONDITIONAL, not as Go. Twelve open
  defects with documented workarounds is an acceptable operational
  position; recording it as unconditionally ready would be a lie that
  surfaces in week 32.
```

### Step 5 - Write the final report

Create `artifacts/23-final-report.md`. Report all eight charter success criteria, including the miss.

**Performance against charter success criteria SC-1 to SC-8:**

| # | Success criterion | Baseline | Target | Actual achieved | Met? |
| --- | --- | --- | --- | --- | --- |
| SC-1 | Registration completion time | 11 min median | Under 4 min | **3.4 min** median over 30 days | Met, exceeded |
| SC-2 | Registration abandonment rate | 34% | Under 15% | **16.2%** | **NOT MET** - missed by 1.2 points |
| SC-3 | Manual communications effort | 24 hrs/week | Under 5 hrs/week | **3.1 hrs/week** | Met, exceeded |
| SC-4 | Mobile completion rate | 41% | Above 80% | **84.7%** | Met |
| SC-5 | Compliance clearance | Non-compliant legacy | Pass, zero major findings | **Passed 18 June, zero major, 2 minor closed** | Met |
| SC-6 | Delivered within budget | - | At or under SGD 480,000 | **SGD 478,900** | Met, by SGD 1,100 |
| SC-7 | Delivered by launch date | - | Live 30 June | **Live 30 June, 06:15** | Met |
| SC-8 | Escaped defects, first 30 days | 19 last release | Under 8 | **6** | Met, exceeded |

```text
SC-2 - THE MISS, REPORTED HONESTLY

  Target under 15%. Achieved 16.2%. Missed by 1.2 percentage points.

  DO NOT round this to "substantially achieved" or shade it into green.
  A 34% to 16.2% reduction is a genuine and large improvement, and it is
  ALSO a missed target. Both statements are true and both belong in the
  report. A final report that has no amber or red on it has usually been
  edited rather than measured.

  ANALYSIS OF THE MISS
    Assumption A-01 in the Lab 06 assumption log stated abandonment would
    fall to 15%, with the Lab 05 downside case tested at 22%. The outcome
    of 16.2% sits between the target and the tested downside, so the
    BUSINESS CASE SURVIVES - which is exactly why Lab 05 tested a downside
    in the first place.

    Segment analysis shows the residual abandonment concentrates in the
    corporate bulk-booking path, which charter exclusion OUT-4 placed out
    of scope. Learners registering individually abandon at 12.8%, comfortably
    inside target. The miss is therefore attributable to a segment the
    project was explicitly not permitted to address.

    That is an explanation, not an excuse, and the distinction matters: the
    recommendation that follows is a phase-2 scope item, not a defence of
    the result.

  BENEFIT CONSEQUENCE - quantified, because "slightly lower" is not a number
    B1 assumed abandonment 34% -> 15%, a 19-point recovery worth
    SGD 673,363 per year.
    Actual recovery is 34% -> 16.2%, a 17.8-point recovery.
    Pro-rata: 673,363 x (17.8 / 19) = SGD 630,834 per year.
    Shortfall against plan: 673,363 - 630,834 = SGD 42,529 per year.

    Revised total gross annual benefit:
      630,834 + 25,536 + 24,200 + 13,000 = SGD 693,570
      against the Lab 05 plan of SGD 736,099. Shortfall SGD 42,529, or 5.8%.
      The business case remains strongly positive.
```

**Final cost position and the recovery from the week-14 forecast:**

```text
FINAL EVM POSITION AT CLOSURE

  Original BAC                          SGD 480,000
  Approved scope reduction (CR-14)      SGD  45,000   Board Option 2, Lab 20
  Revised BAC after descope             SGD 435,000
  Final actual cost                     SGD 478,900
  Ceiling                               SGD 480,000
  Headroom against ceiling              SGD   1,100

THE ARITHMETIC OF THE RECOVERY - how -42,420 became +1,100

  Position at week 14 (Lab 20):
    AC          271,000
    EV          249,000
    CPI         0.919
    EAC         522,420   (BAC / CPI)
    VAC         -42,420   forecast overrun of 8.8%

  Board decision at week 15: Option 2, reduce scope by approximately
  SGD 45,000 by dropping the two lowest-value Should-have items.
  Revised BAC = 480,000 - 45,000 = SGD 435,000.

  Budgeted work remaining after the descope:
    435,000 - 249,000 (EV earned to date) = SGD 186,000

  Cost of the Lab 21 corrective actions, funded from contingency:
    SME backfill - temporary admin cover so the 3 admin staff could
    attend refinement                                     SGD  8,200
    Definition of Ready workshop and rework of the
    sprint 8 backlog                                      SGD  2,300
                                                          -----------
                                                          SGD 10,500

  Actual spend on the remaining work, periods 8 to 12:
    478,900 - 271,000 - 10,500 = SGD 197,400

  CPI achieved on the remaining work:
    186,000 / 197,400 = 0.9422

  So performance improved from 0.919 cumulative at week 14 to 0.942 on
  the work done afterwards - a real but partial recovery. Cumulative CPI
  at closure is 435,000 / 478,900 = 0.908.

  CHECK THE RECONCILIATION
    271,000 + 197,400 + 10,500 = 478,900.  Correct.
    Improvement against the week-14 forecast:
      522,420 - 478,900 = SGD 43,520 better than forecast.

  WHERE THE 43,520 CAME FROM - attribute it, do not just claim it
    Scope reduction (CR-14)                     45,000
    Improved cost efficiency on remaining work
      (186,000/0.919 = 202,394 at the old rate,
       versus 197,400 actual)                    4,994
    Less: corrective action cost               -10,500
    Less: rounding and minor overruns           +4,026 (net residual)
                                               --------
    Net improvement                             43,520

  CONTINGENCY RESERVE - fully consumed, and say so
    Opening reserve (Lab 06, Lab 13)            26,000
    Crash of activities J and O (Lab 20)       -15,500
    Lab 21 corrective actions                  -10,500
                                               --------
    Closing reserve                                  0

    The contingency reserve is exhausted. It was spent on identified
    risks, which is exactly what a contingency reserve is for, and it was
    reported at each Board meeting per the Lab 06 authority condition.
    But the project finished with SGD 1,100 of headroom and ZERO reserve.
    Report that honestly: this project had no remaining capacity to absorb
    a single further problem in its last ten weeks. Finishing inside the
    ceiling was correct management plus a narrow margin, and pretending
    otherwise teaches the wrong lesson to the next project.

  MANAGEMENT RESERVE was never drawn. It sits outside the cost baseline
  and is the sponsor's, and no baseline change was required.
```

**Final scope, schedule and risk position:**

| Dimension | Planned | Final | Explanation |
| --- | --- | --- | --- |
| Scope | 91 RTM requirements | 76 delivered, 15 descoped | 11 Could-haves never committed; 4 Should-haves removed by CR-14 and sprint-10 decision. Zero Must-haves or compliance requirements lost |
| Schedule | Live 30 June | Live 30 June, 06:15 | Achieved. Recovered 5 days by crashing J and O in week 14; gates G1, G2, G3 all passed on date |
| Cost | Ceiling 480,000 | 478,900 | Inside ceiling by 1,100. Contingency fully consumed |
| Quality | Under 8 escaped defects | 6 | Achieved. 12 known low-severity defects transferred to operations |
| Risk | 24 risks in the Lab 14 register | 19 closed, 5 transferred | See below |

```text
FINAL RISK POSITION - risks do not vanish at closure

  Of the 24 risks in the Lab 14 register:
    19 CLOSED    - the event either occurred and was handled, or the
                   window for it has passed.
     5 TRANSFERRED to the operational risk register, owned by the IT
                   Operations Manager. These are risks whose exposure
                   window extends beyond project end:
       R-07  Payment gateway v2 deprecation of the legacy endpoint (2027)
       R-11  PDPA enforcement change affecting consent wording
       R-15  PDPA data protection change affecting fee display
       R-18  Peak-load capacity at the January intake, larger than July
       R-22  Loss of the three admin staff before knowledge is embedded

  A closed project with open risks and no receiving owner is how an
  organisation inherits an unowned exposure. Naming the transferee is part
  of closure, and R-22 in particular ties directly to the knowledge
  transfer plan in Step 8.
```

### Step 6 - Hand over the benefits (they are realised after you leave)

Create `artifacts/23-benefits-realisation.md`.

```text
THE CENTRAL TEACHING POINT OF THIS STEP

  A project DELIVERS AN OUTPUT. The business REALISES A BENEFIT.
  These happen at different times and are owned by different people.

  Contoso goes live on 30 June and closes in week 28. But look at the
  Lab 06 charter: SC-1, SC-2, SC-3 and SC-4 are all marked "measured
  30 days post-launch". Four of the eight success criteria CANNOT BE
  FULLY JUDGED at closure, and the annual benefits B1 to B4 cannot be
  judged for a year.

  So who measures them? Not the project manager - the project is closed
  and the team is released. If benefit ownership is not transferred to a
  named person in the business, WITH a review schedule and a governance
  forum, then nobody measures them, and the SGD 736,099 of annual benefit
  in the Lab 05 business case becomes an unverified claim.

  This is the single commonest organisational failure in project
  management, and the reason PMI made benefits management explicit. The
  project's last act is to give the benefits away properly.
```

**Benefits handover table:**

| ID | Benefit | Planned annual value | Measured at closure | Business owner | Measure | 30-day review | 90-day review | 180-day review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | Recovered abandoned registrations (34% to 15%) | SGD 673,363 | Abandonment 16.2%, tracking to SGD 630,834 | Marcus Tan, Head of L&D Ops (S-03) | Funnel analytics, monthly | 30 Jul | 28 Sep | 27 Dec |
| B2 | Admin time released (24 to 5 hrs/wk) | SGD 25,536 | 3.1 hrs/wk, tracking to SGD 28,022 | Operations Manager | Ops time log, monthly | 30 Jul | 28 Sep | 27 Dec |
| B3 | Support ticket reduction (1,900 to 800) | SGD 24,200 | Too early - hypercare distorts volume | Support desk lead (S-09) | Ticket system, monthly | 30 Jul | 28 Sep | 27 Dec |
| B4 | Hosting and maintenance saving (74,000 to 61,000) | SGD 13,000 | Contracted, realised from week 31 | IT Operations Manager (S-11) | Finance ledger, quarterly | - | 28 Sep | 27 Dec |
| - | **Total** | **SGD 736,099** | **Tracking to SGD 693,570** | Sponsor accountable overall | | | | |

```text
NOTE B2 IS TRACKING ABOVE PLAN
  Planned: 24 -> 5 hrs/wk = 19 hrs released.
    3 staff x SGD 28/hr x 48 weeks... the Lab 05 figure of SGD 25,536 is
    computed as 19 hrs x SGD 28 x 48 = SGD 25,536.
  Actual: 24 -> 3.1 hrs/wk = 20.9 hrs released.
    20.9 x 28 x 48 = SGD 28,090.  (Lab 05 method, one decimal rounding
    gives SGD 28,022 in the ledger.)
  Over-delivery of approximately SGD 2,500 per year.

  Report over-achievement with the same rigour as under-achievement. A
  benefits report that only surfaces shortfalls trains the organisation to
  see benefits management as a blame process, and the next project will
  under-claim its benefits to be safe.

REVIEW GOVERNANCE - who actually sits in these reviews

  30-DAY REVIEW (30 July)
    Chair: Sponsor (Priya Nathan). Attend: benefit owners, IT Ops Manager.
    Purpose: confirm SC-1 to SC-4 measurements now the 30-day window is
    complete; confirm hypercare exit.
    This review formally closes out the four success criteria that closure
    could not judge.

  90-DAY REVIEW (28 September)
    Chair: Sponsor. Attend: benefit owners, Group Finance Director (S-02).
    Purpose: first financial confirmation of the benefit run-rate.
    Finance attends because Lab 07 recorded S-02's main concern as
    "unverified benefits". This is the review that answers it.

  180-DAY REVIEW (27 December)
    Chair: Group Finance Director. Attend: sponsor, benefit owners.
    Purpose: confirm the annualised run-rate, restate NPV and payback
    against actuals, and formally close the business case.

  AFTER 180 DAYS: benefits tracking folds into normal operational
  reporting. The business case is closed with a final statement of
  realised value.

  WHERE THIS SITS: these reviews happen AFTER the project is closed. They
  are therefore owned by the organisation's benefits governance, not by the
  project. The project's obligation is to have SET THEM UP and to have got
  named owners to accept them in writing before the team disbands.

WHAT IF A BENEFIT IS NOT REALISED?

  This must be agreed at closure, not invented at the 90-day review when
  everyone is defensive.

  1. The benefit owner reports the shortfall at the scheduled review with
     the measurement and the variance. Reporting is not optional and is
     not conditional on having a fix.
  2. Root cause analysis, using the Lab 21 method. Distinguish:
       - the OUTPUT is faulty         -> defect, fix under support
       - the OUTPUT is fine but is
         not being USED               -> adoption problem, change
                                         management, not engineering
       - the BENEFIT LOGIC was wrong  -> the business case assumption was
                                         false; correct the estimating
                                         model so the next case is better
  3. Remedial action with an owner and date, OR a formal restatement of
     the benefit with the sponsor's agreement.
  4. If the shortfall is material enough to threaten the case - here, if
     total benefit fell below the Lab 05 downside of roughly SGD 540,000,
     which would push payback beyond 2 years - it escalates to the Board
     under the Lab 03 thresholds.
  5. The variance and its cause go into the lessons-learned repository and
     into the ESTIMATING MODEL, so the next business case is better
     calibrated.

  Note step 5. A missed benefit whose cause never reaches the estimating
  model will be re-forecast identically on the next project. That is how
  an organisation makes the same optimistic assumption for a decade.
```

### Step 7 - Capture lessons learned that actually change something

Create `artifacts/23-lessons-learned.md`.

```text
REGISTER versus REPOSITORY - the distinction is examinable

  LESSONS LEARNED REGISTER
    A PROJECT document. Created EARLY, updated THROUGHOUT the project.
    Live. Owned by the project manager. Contains lessons available to be
    used by THIS project while it is still running.
    A register first written at closure has failed - it should have been
    improving this project for six months.

  LESSONS LEARNED REPOSITORY
    An ORGANISATIONAL PROCESS ASSET. Updated AT CLOSURE from the register.
    Owned by the PMO or the organisation. Serves FUTURE projects.
    This is ECO Business Environment T6, "update organizational process
    assets", and Process T10's final enabler.

  The flow: events -> register (during) -> repository (at closure)
                                        -> future projects' EEF/OPA inputs

  Contoso already consumed the repository: Lab 03 recorded lesson
  PRJ-2021-114, "UAT started before compliance review complete, costing
  11 days and SGD 26,000", and Lab 20 used exactly that entry to REJECT
  fast-tracking compliance against UAT. That is a prior project's lesson
  saving this project real money. It is the whole argument for doing this
  step properly.
```

**Retrospective structure used** (this is the closing retrospective, distinct from the twelve sprint retrospectives):

```text
CLOSING RETROSPECTIVE - 2.5 hours, whole team plus product owner

  1. SET THE STAGE (15 min)
     State the prime directive: everyone did the best they could with what
     they knew at the time. Without this, people defend rather than learn.
  2. GATHER DATA (40 min)
     Timeline of the 28 weeks on a wall. Everyone adds events, then marks
     each with energy: high point, low point, surprise.
     Data BEFORE opinion. This is the step teams skip and it is why their
     retrospectives produce grievances instead of lessons.
  3. GENERATE INSIGHT (45 min)
     Cluster the timeline. For each cluster ask "why" using the Lab 21
     5 Whys, to root cause not first cause.
  4. DECIDE WHAT TO DO (40 min)
     For each root cause: what should a FUTURE project do differently, and
     WHICH ARTIFACT must change for that to happen?
  5. CLOSE (10 min)
     Appreciations. Confirm owners and dates for every OPA update.

  Note step 4's second question. A retrospective that produces advice
  changes nothing. A retrospective that produces a change to a template
  changes every future project automatically, whether or not anyone
  remembers this one.
```

**The ten lessons from the Contoso project:**

| # | Lesson | What happened | Impact | Root cause | Recommendation | OPA / artifact updated |
| --- | --- | --- | --- | --- | --- | --- |
| **L-01** | **An assumption log whose validation dates are not enforced is decoration** | Assumption A-07 ("the 3 admin staff will be available as SMEs") was logged in Lab 06 with owner PM and a week-2 validation date. It was never validated and never escalated. SMEs attended 5 of 14 refinement sessions because they were still doing 24 hrs/week of manual comms | **SGD 50,760 of rework, 655 hours, 168 defects** (Lab 21 Pareto). Top category: incomplete or ambiguous acceptance criteria, 47 defects and 188 hours. Refinement yielded 22 ready points against 34 capacity; sprint planning accepted incomplete stories; CPI fell from 1.022 to 0.919 over seven periods | The log had an owner and a date but no ENFORCEMENT MECHANISM. Nothing in the governance cycle asked "which assumptions are overdue for validation?" | Add overdue-assumption validation as a standing item on the fortnightly status report and every gate agenda. Assumptions overdue by more than one reporting period escalate automatically to the sponsor | **Status report template** (add overdue-assumption section); **gate review checklist** (add assumption validation gate question); **assumption log template** (add "validated Y/N" and "days overdue" columns) |
| L-02 | Sequencing compliance before UAT was correct and should be mandated | The Lab 20 fast-track of compliance review against UAT was refused, citing the PRJ-2021-114 repository lesson and the mandatory dependency. Compliance passed 18 June with zero major findings; UAT then ran against a design the DPO had already cleared | **POSITIVE.** Avoided the 11 days and SGD 26,000 rework that PRJ-2021-114 incurred. G3 passed first time | The organisation had already learned this once and had recorded it well enough to be found and used | Make "compliance clearance precedes UAT execution" a mandatory sequencing rule, not a per-project judgement | **Project schedule template** (mandatory dependency between compliance clearance and UAT); **schedule compression checklist** (list of dependencies that may never be fast-tracked) |
| L-03 | The environment scan predicted the failure and nobody was required to act on it | The Lab 02 PESTLE/TECOP scan recorded factor O1, the SME bottleneck arising from the admin staff's existing 24 hrs/week workload. It was correctly identified in week 1 and was the exact cause of L-01 | The organisation paid SGD 50,760 for a risk it had documented before the project started | A scan produces FINDINGS but no OBLIGATION. There was no step requiring each significant factor to become a risk with a response, or an assumption with a validation date, or an explicit accept | Require every TECOP/PESTLE factor scored above the threshold to be traced to a risk register entry, an assumption, or a written acceptance. Audit the trace at G1 | **Environment scan template** (add mandatory "disposition" column); **G1 gate checklist** (add scan-to-risk traceability check) |
| L-04 | Communicating a redeployment decision late costs more than the decision itself | Lab 07 misalignment M-2 required the Operations Manager to state the admin staff redeployment plan in writing by week 8. It was issued in week 15. In the interval two of the three staff were job-hunting, and their engagement as SMEs was minimal | Directly compounded L-01. The SME availability problem was not only a capacity issue but a WILLINGNESS issue that a week-8 communication would have removed | Uncertainty about job security was allowed to persist because there was no due-date tracking on stakeholder engagement actions - the Lab 07 matrix had owners and dates but no follow-up mechanism | Track engagement-matrix actions in the same overdue-item report as assumptions (see L-01). Where a stakeholder action concerns job security, treat the due date as a hard commitment | **Stakeholder engagement matrix template** (add status and overdue tracking); **change management guideline** (add "communicate role impact before automation becomes visible") |
| L-05 | Escalating on forecast variance rather than actual variance preserved the Board's options | At week 14 the actual CV of -22,000 was -4.58% of BAC, just inside the -5% Board threshold, but the forecast VAC of -42,420 was -8.84%. The PM escalated on the forecast with three costed options and a recommendation | **POSITIVE and decisive.** The Board chose Option 2 in week 15. Had escalation waited for the actual variance to breach -5%, the decision would have come around week 17-18, by which point the descoped work would have been partly built and the SGD 45,000 saving largely unavailable | The PM read the threshold's PURPOSE (give the Board time to act) rather than its letter | Rewrite escalation thresholds to trigger on FORECAST breach explicitly, so this does not depend on an individual PM's judgement | **Governance and escalation threshold document** (thresholds apply to EAC/VAC forecast, not only actuals); **status report template** (forecast variance as a mandatory field) |
| L-06 | Definition of Ready is a cost control, not a process nicety | Sprint planning accepted stories that had not met refinement criteria, because refinement was starved (L-01). After the Lab 21 analysis, a Definition of Ready was enforced from sprint 8 | CPI on work after the fix was 0.942 against 0.919 cumulative before it, recovering approximately SGD 4,994 of the improvement. Defect injection in the top Pareto category fell sharply | The team had a Definition of Done but no Definition of Ready, so there was no gate on work ENTERING the sprint | Mandate a Definition of Ready alongside the Definition of Done for all hybrid and adaptive projects. Refined-and-ready points must equal or exceed committed points at sprint planning | **Sprint ceremony guide OPA-06** (add Definition of Ready section and the ready-points check); **sprint planning checklist** |
| L-07 | Estimating a compliance review from a single prior data point is unsafe | Assumption A-05 estimated the DPO compliance review at 3 weeks on the basis of one prior project of smaller scope. It was validated at week 4 as required, and the DPO confirmed 3 weeks for the agreed scope | **POSITIVE outcome from a weak method.** The estimate held, but only because A-05 was actually validated on time - unlike A-07. The method itself was one data point | Single-point historical estimating with no range. It worked here; it will not always | Hold a compliance-review duration range in the estimating database, banded by requirement count. Contoso: 13 requirements, 3 weeks | **Estimating database** (add compliance review duration by requirement count); **assumption log template** (require a confidence rating and a range) |
| L-08 | Splitting a jointly-owned work package resolved an accountability defect that would have surfaced at the gate | The Lab 15 RACI audit found two Accountable parties on the compliance evidence pack, PM and DPO. It was split into assembly-and-submission (A = PM) and assessment-and-opinion (A = DPO) | Avoided a predictable G3 dispute over whether a late, thin pack was a delivery failure or a standards failure. G3 passed cleanly | The original work package genuinely contained two accountabilities. The WBS dictionary had not distinguished them | Where a RACI audit finds two As, split the work package and update the WBS dictionary. Never record shared accountability | **WBS dictionary template** (one accountable owner per work package, enforced); **RACI audit checklist** (add to the planning-quality gate) |
| L-09 | A responsibility bottleneck was misdiagnosed as a personality problem for eight weeks | The BA held Responsible on 14 of 24 work packages, and was over-allocated at 139% for four consecutive weeks. Lab 16 initially read the resulting friction as a storming-phase behavioural issue | Eight weeks of coaching effort applied to a structural problem, plus the schedule durations in Lab 12 were optimistic because no queueing on the BA was modelled | The schedule was built from activity durations without a resource-loaded check against the RACI | Require a resource histogram for every individual holding Responsible on more than 25% of work packages, before the schedule is baselined | **Schedule baseline checklist** (add resource-loading check); **resource management plan template** (add per-individual histogram requirement) |
| L-10 | Contingency reserve was correctly used but was fully exhausted with ten weeks remaining | The SGD 26,000 reserve funded the week-14 crash (SGD 15,500) and the Lab 21 corrective actions (SGD 10,500), reaching zero. The project finished with SGD 1,100 of headroom and no reserve | No overrun occurred, but for the final ten weeks the project carried zero capacity to absorb any further identified risk. The outcome was correct; the exposure was not visible in reporting | Reserve consumption was reported as individual releases but never as a BURN-DOWN against remaining risk exposure. Nobody saw the coverage ratio fall | Report contingency as a burn-down against the remaining Lab 14 EMV exposure each period. Where reserve falls below remaining EMV, escalate | **Status report template** (add reserve burn-down and coverage ratio); **risk management plan template** (define the reserve coverage escalation trigger) |

```text
THE TEST EVERY LESSON MUST PASS

  Read the last column. If a lesson does not name an artifact that changes,
  it is an opinion, and opinions do not survive contact with the next
  project. "Communicate better next time" changes nothing. "Add an
  overdue-assumption section to the status report template" changes every
  future project whether or not anyone remembers Contoso.

  Count the artifacts these ten lessons update:
    Status report template            L-01, L-05, L-10   (3 lessons)
    Assumption log template           L-01, L-07         (2)
    Gate review checklist             L-01, L-03         (2)
    Sprint ceremony guide OPA-06      L-06               (1)
    Project schedule template         L-02               (1)
    Schedule compression checklist    L-02               (1)
    Environment scan template         L-03               (1)
    Stakeholder engagement template   L-04               (1)
    Change management guideline       L-04               (1)
    Governance/escalation thresholds  L-05               (1)
    Estimating database               L-07               (1)
    WBS dictionary template           L-08               (1)
    RACI audit checklist              L-08               (1)
    Schedule baseline checklist       L-09               (1)
    Resource management plan template L-09               (1)
    Risk management plan template     L-10               (1)

  The status report template is touched by three separate lessons. That is
  a signal: the reporting instrument was the common failure point. Overdue
  assumptions, forecast variance and reserve burn-down were all invisible
  because the report did not have a field for them. Fixing one template
  addresses three of this project's ten lessons.

  ASSIGN AN OWNER AND A DATE TO EVERY OPA UPDATE, and check them off.
  Lessons "captured" but never applied to the templates are the second
  commonest closure failure, immediately after benefits never being
  measured.
```

### Step 8 - Transfer the knowledge (People T7)

```text
WHAT KNOWLEDGE MATTERS AT HANDOVER

  EXPLICIT knowledge - already written down, just needs transferring
    Runbooks, architecture diagrams, the data model, the RTM, the
    compliance evidence pack, the known-defect list, configuration
    baselines, the support scripts.
    Transfer method: archive it where operations can find it, and index it.

  TACIT knowledge - in someone's head, and the hard part
    Why the payment retry logic has a 90-second delay. Which learner
    records were manually corrected during migration and why. Which alert
    is noisy and can wait. What the corporate bulk-booking path does that
    the individual path does not.
    Transfer method: cannot be documented into existence. Requires
    PAIRING and TIME, which is a large part of what the four-week
    hypercare period actually buys.

RISK R-22 IS THE ACUTE CASE
  "Loss of the three admin staff before knowledge is embedded."
  These three people hold nine years of tacit knowledge about how course
  registration exceptions are really handled - the knowledge the project
  needed as SME input (L-01) and did not adequately get. They are also
  the group most affected by the automation and the ones who were job
  hunting in week 15 (L-04).
  Transferred to the IT Operations Manager as an operational risk with a
  documented response: they are now trained on the new system, their
  redeployment is agreed in writing, and their exception-handling
  knowledge is captured in the support desk scripts.
```

| Knowledge item | Type | Holder | Receiver | Transfer method | Complete by |
| --- | --- | --- | --- | --- | --- |
| Platform architecture and data model | Explicit | Dev Lead | IT Ops Manager | Documented handover session plus archived diagrams | 30 June |
| Deployment, rollback and release pipeline | Explicit + tacit | DevOps | IT Ops on-call team | Two supervised releases during hypercare | 28 July |
| Registration exception handling | Tacit | 3 admin staff | Support desk | Scripted scenarios plus 2 weeks of shadowing | 14 July |
| Migration anomalies and manual corrections | Tacit | BA | IT Ops Manager | Written anomaly log plus walkthrough | 30 June |
| Compliance evidence structure and PDPA rationale | Explicit | BA and DPO | DPO retains; Ops informed | Evidence pack archived; annual review scheduled | 30 June |
| Known defects, workarounds, alert tuning | Explicit + tacit | QA Lead | Support desk lead | Defect list plus hypercare pairing | 28 July |
| Backlog and phase-2 candidates | Explicit | Product Owner | Product Owner retains | Phase-2 register with decision dates | Week 28 |

### Step 9 - Release the team and close the human side

```text
STAGED RELEASE, NOT A CLIFF EDGE

  30 June (go-live)   UX Designer, Content Lead, 2 developers released
  28 July (hypercare  Dev Lead, QA Lead, DevOps released
   exit)
  Week 28 (closure)   BA, remaining developers, PM released

  Releasing the whole team on go-live is the classic error. It leaves the
  July intake peak - the very reason the date was fixed - unsupported, and
  it destroys the tacit knowledge transfer described in Step 8.

RESOURCE RELEASE IS NOT JUST ADMINISTRATION
  For each of the nine people:
    - Written release notice to their functional manager, with dates
    - Performance feedback to that manager - this is a real obligation.
      In a matrix organisation the PM sees work the functional manager
      never sees, and withholding it disadvantages the individual
    - Confirm their next assignment is known before they leave. People
      released into uncertainty disengage in their final weeks, which is
      when hypercare needs them most
    - Return of access, equipment and system permissions

TUCKMAN ADJOURNING - the stage Lab 16 introduced and this lab completes
  Forming -> Storming -> Norming -> Performing -> ADJOURNING

  Adjourning is a real stage with real behaviours: a drop in performance,
  anxiety about what comes next, a sense of loss for a group that took
  months to become effective, and sometimes premature disengagement.
  It is not sentimentality to manage it; a team that disengages in week
  26 delivers a worse hypercare than a team that does not.

  What to actually do:
    - Mark the ending explicitly. An unmarked ending is experienced as
      an abandonment
    - Recognise contribution SPECIFICALLY and INDIVIDUALLY. "Great work
      everyone" recognises nobody. Name what each person did
    - Recognise the ADMIN STAFF too. They were the dependent stakeholders
      of Lab 07, the SMEs of L-01 and the most disrupted group in the
      project. Omitting them from the closing recognition would repeat the
      exact pattern that caused L-04
    - Give the team the results: the eight success criteria, including the
      SC-2 miss. People who built something are entitled to know whether
      it worked
    - Hold the celebration BEFORE the team disperses, not when the
      paperwork is finally signed in week 28
```

### Step 10 - Answer the exam-style scenarios

```text
SCENARIO 1
The project's deliverables are complete and the QA lead confirms all tests
have passed against specification. The sponsor is travelling and asks the
project manager to "just close it out and send the paperwork later". The
project manager wants to release the team, which is needed on another
project starting next week. What should the project manager do?

  A. Release the team and obtain the sponsor's signature when she returns,
     since Control Quality has confirmed the deliverables meet specification.
  B. Obtain formal acceptance from the accepting stakeholders, complete
     transition readiness and staged release, and close only when the
     closure criteria are met - explaining to the sponsor that acceptance
     cannot be retrospective.
  C. Close the project administratively now and treat the outstanding
     acceptance as a post-closure action item.
  D. Ask the QA lead to sign the acceptance in the sponsor's absence, since
     the deliverables have been verified.

SCENARIO 2
Six weeks after a project closes, the sponsor asks the former project
manager why the expected cost savings have not appeared in the operating
budget. The project delivered every deliverable on time and within budget,
and the final report was accepted. What is the MOST likely underlying
failure?

  A. The project was not actually successful; the deliverables must be
     defective.
  B. Benefits were not transferred to named business owners with a
     measurement method and a review schedule extending beyond closure.
  C. The project manager should have remained assigned until the benefits
     were realised.
  D. The business case overestimated the benefits and should be rewritten.

SCENARIO 3
At the closing retrospective a team identifies that a documented assumption
was never validated, causing significant rework. The team agrees the lesson
is "we should validate assumptions properly next time" and records it in the
lessons learned register. What is the BEST assessment of this outcome?

  A. Correct. The lesson is captured in the register, which is the required
     closure activity.
  B. Incomplete. The lesson must also be transferred to the organisational
     lessons learned repository at closure.
  C. Incomplete. The lesson states an intention but names no artifact that
     changes, so no future project will be affected by it.
  D. Incorrect. Lessons learned should focus on successes rather than
     failures to maintain team morale.
```

Answer key:

```text
SCENARIO 1 -> B.  Control Quality and Validate Scope are different processes
            with different outputs. QA confirming the deliverables meet
            specification produces VERIFIED deliverables; only the customer
            or sponsor can produce ACCEPTED deliverables. The project is not
            closeable on verification alone.
            A is the trap, and it is attractive because the technical work
            genuinely is finished. But it releases the team before transition
            readiness is validated - enabler 3 - and it treats formal
            acceptance as paperwork rather than as the event that transfers
            the deliverable. Note also the staged release: on Contoso,
            releasing everyone at go-live would have left the July intake
            peak unsupported.
            C inverts the closure sequence: acceptance is a PRECONDITION of
            administrative closure, not a follow-up to it.
            D has the QA lead accept on the customer's behalf, which
            collapses the two processes into one and gives acceptance
            authority to someone who does not have it. QA verifies against
            specification; QA cannot decide the customer is satisfied.

SCENARIO 2 -> B.  This is the defining benefits-management failure. Outputs
            are delivered by the project; benefits are realised by the
            business afterwards. If no named owner holds each benefit, with
            a measurement method and scheduled reviews beyond closure, then
            nobody measures anything and the savings are never traced into
            the operating budget even when they have genuinely occurred.
            Note that in this scenario the savings may well be real and
            simply unmeasured - which is why B says the failure is the
            transfer, not the outcome.
            A does not follow. Delivering on time and within budget to
            accepted specification is compatible with benefits never being
            harvested; they are separate things, which is the whole point.
            C misunderstands the role. Projects are temporary. Keeping the
            PM assigned for a year is not the mechanism; transferring
            ownership to the permanent organisation is.
            D leaps to a conclusion with no measurement behind it. You
            cannot judge the estimate before you have measured the actual,
            and rewriting the business case to match the absence of data is
            not analysis.

SCENARIO 3 -> C.  The lesson as recorded is an intention. "Validate
            assumptions properly" is advice, and advice depends on a future
            project manager both remembering it and choosing to act on it.
            Neither can be relied upon, which is why it will recur.
            A useful version of this lesson names the artifact: add an
            overdue-assumption section to the status report template, and an
            assumption-validation question to the gate review checklist.
            Those changes act on every future project automatically. That is
            the Contoso L-01 lesson, and its quantified consequence was
            SGD 50,760 of rework, 655 hours and 168 defects.
            A is wrong because recording a lesson is necessary but not
            sufficient; capture is not the objective, change is.
            B is TRUE but is not the BEST answer. The register-to-repository
            transfer is indeed required at closure, but transferring a vague
            lesson into the repository merely stores a vague lesson where
            more people can fail to act on it. The defect in the lesson is
            its content, and B does not fix that.
            D is wrong twice over: lessons learned cover both positive and
            negative outcomes - Contoso's L-02 and L-05 are positive lessons
            worth as much as the failures - and suppressing failures to
            protect morale defeats the purpose of the process entirely.
```

## Deliverable

Submit to `artifacts/`:

- `23-closure-checklist.md` - all 20 closure criteria with evidence, owner and status, covering deliverable acceptance, scope verification, financial closure, procurement closure, resource release, documentation, transition, benefits handover and lessons learned.
- The RTM closure check showing 41 of 41 Must-haves and 13 of 13 compliance requirements delivered, and the 15 descoped items reconciling to 91 total.
- `23-final-report.md` - all eight success criteria with baseline, target, actual and met/not-met, including the honest SC-2 miss at 16.2% and its quantified benefit consequence.
- The final EVM position with the full arithmetic of the recovery from EAC 522,420 to a final actual of SGD 478,900, the attribution of the SGD 43,520 improvement, and the contingency reserve burn-down to zero.
- The final scope, schedule and risk position, including the five risks transferred to operations with a named owner.
- The acceptance sign-off table with named stakeholders per deliverable, and the conditional acceptance recorded as conditional.
- `23-transition-plan.md` - the 12-criterion readiness assessment with thresholds set in advance, plus the four-week hypercare plan with staffing, response times and exit criteria.
- `23-benefits-realisation.md` - B1 to B4 handed to named business owners with measures and 30/90/180-day review dates, the review governance with named chairs, and the documented procedure for an unrealised benefit.
- `23-lessons-learned.md` - at least 10 lessons, each with what happened, quantified impact, root cause, recommendation and the named OPA it updates, headed by the A-07 assumption-log failure with its SGD 50,760 consequence, and including at least two positive lessons.
- The knowledge transfer table separating explicit from tacit knowledge, with method and date.
- The staged team release plan and the recognition approach.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- You can state, without hesitation, that Control Quality verifies against specification internally and comes FIRST, and Validate Scope obtains customer acceptance and comes SECOND.
- Your closure checklist includes procurement closure as a separate category from administrative closure, and you can say why procurement closes first.
- You reported SC-2 as NOT MET. If every criterion on your report is green, you edited rather than measured.
- You quantified the SC-2 consequence as a benefit shortfall of SGD 42,529 per year, rather than describing it as "slightly below target".
- Your final cost arithmetic reconciles: 271,000 + 197,400 + 10,500 = 478,900, and you can explain each of the three components.
- You stated that the contingency reserve closed at ZERO and reported that as an exposure, not as a success.
- You attributed the SGD 43,520 improvement against forecast to specific causes, principally the CR-14 scope reduction, rather than claiming it as general good management.
- Every one of B1 to B4 has a named business owner who is not the project manager, and review dates that fall after the project has closed.
- You can explain why SC-1 to SC-4 cannot be judged at closure, and which review formally closes them out.
- You documented what happens when a benefit is not realised, including the step that feeds the cause back into the estimating model.
- Every lesson in your register names the specific artifact or template it updates. Any lesson ending in "should communicate better next time" fails this test and must be rewritten.
- Your lessons include at least two POSITIVE lessons. A lessons-learned register containing only failures teaches the organisation to fear the process.
- The headline lesson is the A-07 assumption-log failure, carrying its SGD 50,760, 655 hours and 168 defects, and its recommendation changes the status report template.
- You distinguished the lessons learned REGISTER from the REPOSITORY, and you can name a case where Contoso consumed a prior project's repository entry to make a decision.
- Your team release is STAGED across go-live, hypercare exit and closure, and you can say why releasing everyone on 30 June would have been an error.
