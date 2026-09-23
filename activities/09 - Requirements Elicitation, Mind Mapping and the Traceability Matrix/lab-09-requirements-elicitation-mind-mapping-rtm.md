# Lab 09 - Requirements Elicitation, Mind Mapping and the Traceability Matrix

| Field | Value |
| --- | --- |
| Topic | 3 - Plan the Project |
| ECO 2026 task | Process T2 - Develop and manage project scope; Process T1 - Develop an integrated project management plan |
| Learning outcome | LO1 - Scope medium-scale project requirements to drive timely completions |
| Duration | 90 minutes |
| Consumes | Lab 06 charter high-level requirements R-1 to R-6 and scope boundaries; Lab 07 stakeholder register; Lab 04 compliance requirements C-01 to C-13 |
| Produces | `artifacts/09-requirements-mindmap.md`, `artifacts/09-requirements-register.md`, `artifacts/09-rtm.md` |

## Objectives

- Select the right elicitation technique for each stakeholder group rather than defaulting to interviews for everything.
- Use a mind map to decompose the charter's six high-level requirements into a structured requirement set.
- Write a requirements register in which every requirement is testable, sourced and prioritised.
- Write non-functional requirements with numbers attached, because an unmeasurable NFR cannot be accepted or rejected.
- Build a bidirectional requirements traceability matrix that will carry the compliance evidence to the Lab 04 gate.
- Establish requirement attributes, versioning and the route by which a baselined requirement changes.

## What a requirement is, and the categories the exam tests

```text
A REQUIREMENT is a condition or capability that is necessary in a product,
service or result to satisfy a business need. The test of a good requirement:

  UNAMBIGUOUS  Two readers reach the same interpretation.
  TESTABLE     You can state, before building it, what evidence proves it met.
  NECESSARY    Removing it means a stated need goes unmet.
  TRACEABLE    It links backwards to a business need and forwards to a test.
  CONSISTENT   It does not contradict another requirement.
  ATOMIC       One requirement, one capability. "and" is a warning sign.

REQUIREMENT CATEGORIES - the exam expects you to classify correctly

  BUSINESS        The higher-level need of the ORGANISATION.
                  "Reduce registration abandonment to under 15%."
  STAKEHOLDER     The need of a specific stakeholder or group.
                  "The DPO requires evidence of consent capture at the gate."
  SOLUTION        What the product must do or be. Splits into:
     FUNCTIONAL      Behaviour. "The system shall email a confirmation."
     NON-FUNCTIONAL  Quality of that behaviour. "...within 60 seconds."
  TRANSITION      Temporary, needed only to get from as-is to to-be.
                  Data migration, training, parallel running. Once you are
                  transitioned, the requirement stops applying. This category
                  is the one candidates forget.
  PROJECT         Requirements on the project itself, not the product.
                  "Fortnightly earned value reporting."
  QUALITY         The condition that validates successful completion.

Exam traps:  "The system shall be user-friendly" is not a requirement -
             it is not testable. Convert it or delete it.
             A solution stated as a requirement is a design decision in
             disguise. "The system shall use PostgreSQL" is a constraint,
             not a requirement, unless a stakeholder genuinely requires it.
             Gold plating is adding requirements no stakeholder asked for.
```

## Steps

### Step 1 - Choose elicitation techniques deliberately

There is no single best technique. Each buys different information at a different cost, and the exam tests whether you can match technique to situation.

| Technique | What it is good for | Weakness | Contoso application |
| --- | --- | --- | --- |
| Interviews (one-to-one) | Depth, sensitive topics, individual expertise | Slow; one perspective at a time; interviewer bias | 45 min each with Priya Nathan (S-01), Marcus Tan (S-03) and the DPO (S-04). The DPO interview must be one-to-one - compliance concerns get softened in groups |
| Focus groups | Reactions of a defined user segment; hearing disagreement surface | Dominant voices skew it; needs a skilled moderator | Two groups of 8 learners each, one mobile-first segment, one desktop segment, on the current abandonment pain |
| Facilitated workshop (JAD) | Fast convergence, cross-functional trade-offs, decisions made in the room | Expensive in senior time; fails without preparation | One-day JAD in week 2 with Marcus Tan, the BA, UX lead, dev lead and two admin staff to fix the registration flow scope |
| Questionnaires and surveys | Large populations, statistical weight, geographically spread | No follow-up questions; low response rates; you only learn what you thought to ask | Survey to 14,000 learners on abandonment reasons; target 400 responses for a usable sample |
| Observation / job shadowing | Reveals what people actually do rather than what they say they do | Time-consuming; the Hawthorne effect changes behaviour | Shadow the three admin staff (S-06) for a full day each on the 24 hrs/week of manual communications. They cannot describe the workarounds they no longer notice |
| Prototypes | Feedback on something concrete; surfaces misunderstandings early | Stakeholders mistake the prototype for a finished product | Clickable registration prototype in sprint 1, tested with 8 real learners in sprint 3 per assumption A-01 |
| Benchmarking | External comparison; realistic targets | Comparators may not be comparable | Compare registration step counts against three competitor training providers to validate the under-4-minute target |
| Document analysis | Cheap; captures existing rules nobody remembers | Documents are often stale or aspirational | Analyse the legacy portal's 1,900 annual support tickets, PDPA guidance, and the accreditation compliance-claim data specification |
| Brainstorming | Volume and breadth of ideas; good starting divergence | Produces unfiltered noise; needs a convergence step | Opens the JAD workshop; feeds directly into the mind map in Step 2 |

```text
SELECTION LOGIC the exam rewards

  Need DEPTH from few people        -> interview
  Need BREADTH from many people     -> questionnaire
  Need a DECISION between parties   -> facilitated workshop
  Need the TRUTH about current work -> observation
  Need REACTION to a proposal       -> prototype
  Need to know what "good" is       -> benchmarking

Note the specific reason observation is right for the admin staff: they are
the S-06 DEPENDENT stakeholders from Lab 07. Interviewing people who fear
redundancy about how much of their work could be automated produces
unreliable data. Watching the work does not.
```

### Step 2 - Build the requirements mind map in the live tool

Open the mind mapping tool: [Mind Mapping](https://alfredang.github.io/mindmapping/)

A mind map is the right tool at this moment because requirements arrive unordered from nine different stakeholder groups, and the map imposes structure without forcing premature sequencing. It is a decomposition aid, not a deliverable in itself.

Create the central node exactly as written, then add the eight branches, then the sub-branch leaves under each.

```text
CENTRAL NODE
  Contoso Training Portal Upgrade

BRANCH 1  Registration
    Course search and filter
    Guest browse before login
    Single-page registration form
    Save and resume incomplete registration
    Under 4 minutes end to end

BRANCH 2  Communications
    Booking confirmation
    Course reminder 48 hours before
    Reschedule and cancellation notices
    Completion and certificate notice
    Template management without developer

BRANCH 3  Self-Service
    View my bookings
    Reschedule a booking
    Cancel a booking
    Download attendance record
    Update my own contact details

BRANCH 4  Compliance and Data
    PDPA consent capture at collection
    Purpose limitation statement
    Data access and correction request
    identity-linked attendance record
    Seven-year retention and disposal

BRANCH 5  Payments
    Gateway v2 API integration
    Card and PayNow methods
    Refund on cancellation
    Payment failure recovery
    Receipt generation

BRANCH 6  Migration
    Active learner profiles
    Bookings within 24 months
    Data cleansing and de-duplication
    Reconciliation report
    Rollback position

BRANCH 7  Accessibility
    WCAG 2.1 AA on learner pages
    Keyboard-only navigation
    Screen reader labels
    Colour contrast 4.5 to 1
    Text resize to 200 percent

BRANCH 8  Non-Functional
    Page load under 2.0 seconds
    400 concurrent registrations
    99.5 percent uptime in enrolment window
    Browser and device support matrix
    Audit logging of data access
```

Export or screenshot the finished map into `artifacts/09-requirements-mindmap.md`.

Note what the map has already told you. Branch 4 and Branch 7 exist only because of Lab 04's compliance register and Lab 02's factor L1 - no learner asked for either. Branches that arise from obligation rather than from user demand are exactly the branches that get cut under schedule pressure, which is why they need requirement IDs and traceability before the pressure arrives.

### Step 3 - Write the requirements register

Create `artifacts/09-requirements-register.md`. Priority uses MoSCoW, which Lab 10 will formalise and challenge.

**Business requirements** - these restate the Lab 05 benefits as requirements on the organisation.

| ID | Requirement | Source | Category | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- | --- |
| REQ-001 | Reduce registration abandonment from 34% to under 15% | S-01 COO, Lab 05 B1 | Business | Must | Funnel analytics over 30 days post-launch show abandonment below 15% |
| REQ-002 | Reduce median registration completion time from 11 minutes to under 4 minutes | S-01 COO, charter SC-1 | Business | Must | Portal analytics median across 30 days is under 4:00 |
| REQ-003 | Reduce manual communications effort from 24 to under 5 staff-hours per week | S-03 Marcus Tan, Lab 05 B2 | Business | Must | Ops time log over 4 consecutive weeks averages under 5 hrs/wk |
| REQ-004 | Raise mobile registration completion from 41% to above 80% | S-01 COO, charter SC-4 | Business | Must | Analytics mobile segment completion above 80% over 30 days |

**Stakeholder requirements**

| ID | Requirement | Source | Category | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- | --- |
| REQ-005 | The DPO shall receive a complete evidence pack for each of the 13 compliance requirements before gate G3 | S-04 DPO | Stakeholder | Must | Evidence pack indexed to C-01..C-13, accepted by DPO with zero major findings |
| REQ-006 | Administration staff shall be able to create and edit communication templates without developer involvement | S-06 Admin staff | Stakeholder | Should | An admin creates, previews and publishes a new template in a usability test without assistance |
| REQ-007 | IT Operations shall receive runbook, monitoring and alerting documentation before handover | S-11 IT Ops | Stakeholder | Should | IT Ops signs the supportability checklist at the G3 review |
| REQ-008 | Corporate clients' existing bulk bookings shall remain visible and unaltered through cutover | S-17 Corporate clients | Stakeholder | Must | Reconciliation report shows 100% of in-scope corporate bookings present and matching post-migration |

**Solution requirements - functional**

| ID | Requirement | Source | Category | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- | --- |
| REQ-009 | A learner shall search and filter courses by title, category, date and location without logging in | Learner focus group, R-1 | Functional | Must | A guest user retrieves a target course within 3 interactions |
| REQ-010 | A learner shall complete registration for one course in a single form with no more than 12 input fields | JAD workshop, R-1 | Functional | Must | Field count verified at 12 or fewer; usability test completes in under 4 minutes |
| REQ-011 | The system shall save an incomplete registration and allow resumption within 7 days | Support ticket analysis | Functional | Should | An abandoned registration is resumable from the same step after re-login within 7 days |
| REQ-012 | The system shall send a booking confirmation within 60 seconds of successful payment | R-2 | Functional | Must | 100 test bookings; 95th percentile delivery under 60 seconds |
| REQ-013 | The system shall send a course reminder 48 hours before the session start | S-03, R-2 | Functional | Must | Reminder dispatched between 47 and 49 hours before start for all sessions in a 2-week test |
| REQ-014 | The system shall send reschedule and cancellation notices automatically on the triggering event | R-2 | Functional | Must | Each of the two events produces a notice within 60 seconds |
| REQ-015 | A learner shall view all their bookings, past and upcoming, on one page | R-3 | Functional | Must | All bookings for a test learner appear with correct status |
| REQ-016 | A learner shall reschedule a booking to another session of the same course without contacting support | R-3 | Functional | Must | A learner completes a reschedule unaided in usability testing |
| REQ-017 | A learner shall cancel a booking and receive a refund per the cancellation policy without contacting support | R-3 | Functional | Must | Cancellation processed and refund initiated within the policy window |
| REQ-018 | The system shall capture explicit PDPA consent, with purpose stated, at the point of personal data collection | S-04 DPO, C-01 | Functional | Must | Consent record stored with timestamp, version and purpose text; DPO reviews and accepts |
| REQ-019 | The system shall record NRIC-linked attendance in the accreditation compliance claim format | S-15 Regulator, C-06 | Functional | Must | A generated claim file validates against the Authority specification without manual rework |
| REQ-020 | The system shall process payments through the gateway v2 API including card and PayNow | R-1, IN-6 | Functional | Must | End-to-end payment succeeds in both methods against the v2 sandbox and production |
| REQ-021 | The system shall log every access to learner personal data with actor, timestamp and purpose | S-04 DPO, C-09 | Functional | Must | Audit log entry produced for 100% of access events in a scripted test |

**Solution requirements - non-functional**

Every one of these carries a number. An NFR without a number is an opinion, and it will be argued about at the gate rather than tested.

| ID | Requirement | Source | Category | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- | --- |
| REQ-022 | Learner-facing pages shall load in under 2.0 seconds at the 95th percentile on a 4G connection | UX lead, R-6 | Non-functional | Must | Synthetic monitoring over 7 days; 95th percentile under 2.0s on the throttled 4G profile |
| REQ-023 | The system shall support 400 concurrent registration sessions with no degradation of REQ-022 | S-11 IT Ops, enrolment peak data | Non-functional | Must | Load test at 400 concurrent sessions holds the 2.0s 95th percentile |
| REQ-024 | The system shall maintain 99.5% uptime during the enrolment window | S-01, S-11 | Non-functional | Must | Monitoring over the enrolment window shows availability at or above 99.5% |
| REQ-025 | All learner-facing pages shall conform to WCAG 2.1 level AA | C-11, IN-9 | Non-functional | Must | Automated scan plus manual audit return zero level A or AA failures |
| REQ-026 | Learner personal data shall be encrypted at rest and in transit using current approved algorithms | S-04 DPO, C-04 | Non-functional | Must | Penetration test confirms TLS 1.2 or above in transit and encryption at rest |

**Transition requirements** - these apply only during the move from as-is to to-be, then cease.

| ID | Requirement | Source | Category | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- | --- |
| REQ-027 | Active learner profiles and bookings within 24 months shall be migrated with a reconciliation report | IN-7, OUT-6 | Transition | Must | Reconciliation shows record counts matching within zero variance; exceptions individually explained |
| REQ-028 | The three administration staff shall be trained on the new administrative functions before go-live | IN-10, S-06 | Transition | Must | All three complete training and pass a scripted competency check before 30 June |
| REQ-029 | A documented rollback position shall exist and be tested before cutover | S-11 IT Ops, Lab 03 lessons | Transition | Must | Rollback rehearsed in the pre-launch dry run and completed within the agreed window |

**Quality requirements**

| ID | Requirement | Source | Category | Priority | Acceptance criterion |
| --- | --- | --- | --- | --- | --- |
| REQ-030 | An automated regression suite shall cover the registration and communications paths | IN-8, Lab 03 lessons | Quality | Must | Suite executes in CI on every build; covers all REQ-009 to REQ-017 paths |
| REQ-031 | Escaped defects in the first 30 days after launch shall number fewer than 8 | Charter SC-8 | Quality | Must | Defect log at day 30 shows fewer than 8 production defects attributable to this release |

That is 31 requirements from 6 charter statements. The expansion ratio is normal and is the reason the charter says its high-level requirements "seed the elicitation, they do not replace it".

### Step 4 - Set requirement attributes and versioning

A requirement is not just a sentence. Each one carries attributes that make it manageable. Record these for every requirement in the register.

| Attribute | Purpose | Example for REQ-022 |
| --- | --- | --- |
| Unique ID | Permanent identity; never reused even if the requirement is deleted | REQ-022 |
| Description | The requirement statement itself | Pages load under 2.0s at 95th percentile on 4G |
| Category | Business / stakeholder / solution / transition / project / quality | Solution - non-functional |
| Source | The named stakeholder or document it came from | UX lead; charter R-6 |
| Priority | MoSCoW; revisited in Lab 10 | Must |
| Owner | Who decides if it changes | Marcus Tan, product owner |
| Status | Proposed / approved / baselined / implemented / verified / deferred / cancelled | Baselined |
| Version | Increments on every approved change | 1.1 |
| Acceptance criterion | The evidence that proves it met | 95th percentile under 2.0s over 7 days |
| Complexity / effort | Rough size, feeding Lab 10 story points | 8 points |
| Stability | How likely it is to change; unstable requirements are candidates for rolling wave | Stable |
| Verification method | Test / inspection / demonstration / analysis | Test - synthetic monitoring |

```text
VERSIONING AND CHANGE AFTER BASELINE

  BEFORE baseline (week 5, milestone M2):
    Requirements are drafted, refined, added and deleted freely. Version
    stays at 0.x. No change request needed. This is the cheap window and
    it is deliberately short.

  AT baseline:
    The requirements register version 1.0 is approved by the product owner
    and the sponsor. It becomes part of the scope baseline with the WBS
    and WBS dictionary from Lab 11.

  AFTER baseline, to change a requirement:
    1. Raise a change request describing the change and its reason.
    2. Perform impact analysis - and this is where the RTM earns its keep:
       trace the requirement forward to every WBS element, story, test
       case and compliance requirement it touches, so the impact is
       computed rather than guessed.
    3. CCB decides per the Lab 03 thresholds. The PM may approve changes
       under SGD 10,000 with no critical-path impact; above that escalates.
    4. If approved, increment the requirement version, update the RTM,
       and update every downstream artifact the trace identified.
    5. If the change alters a Must-have, the scope baseline changes and
       the cost and schedule baselines are re-examined.

  THE HYBRID NUANCE from the Lab 06 approach decision:
    Re-PRIORITISING or re-SEQUENCING backlog items inside the baselined
    Must-have envelope is the product owner's call, every sprint, with no
    change request. Adding, removing or materially altering a Must-have
    requires the change request above. Confusing these two is how hybrid
    projects either freeze solid or lose all control.
```

### Step 5 - Build the requirements traceability matrix

Create `artifacts/09-rtm.md`. The RTM is the single artifact that connects the business need at one end to the test evidence at the other. Build it as a table with a column for every link in that chain.

Columns forward-reference Lab 11 (WBS element) and Lab 10 (story), which you will complete after those labs. Populate them now with the expected element so the trace is visible.

| REQ ID | Business need | Charter req | WBS element (Lab 11) | Story (Lab 10) | Design artifact | Test case | Compliance req (Lab 04) | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-009 | Reduce abandonment | R-1 | 1.3.1 Course search and selection | US-01 | Search wireframe SR-02 | TC-101 search and filter | - | Baselined |
| REQ-010 | Reduce abandonment, reduce time | R-1 | 1.3.2 Responsive registration flow | US-02 | Registration flow RF-01 | TC-110 single-form registration | - | Baselined |
| REQ-011 | Reduce abandonment | R-1 | 1.3.2 Responsive registration flow | US-05 | Save-resume state model | TC-114 resume within 7 days | - | Baselined |
| REQ-012 | Automate communications | R-2 | 1.4.1 Notification engine and templates | US-06 | Notification sequence NS-01 | TC-201 confirmation under 60s | - | Baselined |
| REQ-013 | Automate communications | R-2 | 1.4.1 Notification engine and templates | US-07 | Notification sequence NS-02 | TC-203 reminder at 48 hrs | - | Baselined |
| REQ-016 | Reduce support tickets | R-3 | 1.5.1 Booking view, reschedule, cancel | US-09 | Self-service flow SS-01 | TC-301 unaided reschedule | - | Baselined |
| REQ-017 | Reduce support tickets | R-3 | 1.5.1 Booking view, reschedule, cancel | US-10 | Self-service flow SS-02 | TC-305 cancel and refund | - | Baselined |
| REQ-018 | PDPA lawful basis | R-4 | 1.8.1 PDPA consent and retention build | US-13 | Consent model CM-01 | TC-401 consent record integrity | C-01, C-02 | Baselined |
| REQ-019 | accredited-course claim validity | R-5 | 1.8.1 PDPA consent and retention build | US-14 | Claim file spec CF-01 | TC-410 claim file validation | C-06, C-07 | Baselined |
| REQ-020 | Enable payment | R-1 | 1.6.1 Gateway v2 integration | US-11 | Payment sequence PS-01 | TC-501 card and PayNow end to end | C-05 | Baselined |
| REQ-021 | PDPA accountability | R-4 | 1.8.1 PDPA consent and retention build | US-15 | Audit log design AL-01 | TC-420 access log completeness | C-09 | Baselined |
| REQ-022 | Mobile parity | R-6 | 1.3.2 Responsive registration flow | US-03 | Performance budget PB-01 | TC-601 4G 95th percentile load | - | Baselined |
| REQ-023 | Enrolment peak survival | R-6 | 1.3.2 Responsive registration flow | US-03 | Capacity model CP-01 | TC-605 400 concurrent load test | - | Baselined |
| REQ-025 | Accessibility obligation | R-6 | 1.3.3 Accessibility WCAG 2.1 AA build-in | US-04 | Accessibility spec AC-01 | TC-701 WCAG 2.1 AA audit | C-11 | Baselined |
| REQ-026 | Data protection | R-4 | 1.8.1 PDPA consent and retention build | US-16 | Encryption standard ES-01 | TC-430 pen test encryption check | C-04 | Baselined |
| REQ-027 | Continuity of service | R-1, R-3 | 1.7.1 Data profiling and migration scripts | US-19 | Migration mapping MM-01 | TC-801 reconciliation zero variance | C-12 | Baselined |
| REQ-030 | Defect reduction | Quality | 1.9.1 Automated regression suite | US-21 | Test strategy TS-01 | TC-900 suite coverage report | - | Baselined |

### Step 6 - Understand what bidirectional traceability actually buys you

```text
FORWARD TRACEABILITY   business need -> requirement -> design -> build -> test
  Answers: "Have we built everything the business asked for?"
  A business need with no requirement beneath it is an UNMET NEED.
  A requirement with no test case is an UNVERIFIABLE requirement.

BACKWARD TRACEABILITY  test -> build -> design -> requirement -> business need
  Answers: "Why does this exist, and who asked for it?"
  A requirement that traces back to no business need is GOLD PLATING.
  Deleting it is a saving, not a loss.

BIDIRECTIONAL = both directions maintained, continuously, on the same matrix.

WHAT THE RTM IS ACTUALLY FOR - three uses, in order of exam frequency:

  1. IMPACT ANALYSIS. When a change request arrives, the RTM turns "what
     does this affect?" from a meeting into a query. Change REQ-018 and the
     matrix immediately names WBS 1.8.1, story US-13, design CM-01, test
     TC-401 and compliance requirements C-01 and C-02. Without the RTM this
     is guesswork, and guesswork is how you miss the compliance link.

  2. COMPLIANCE EVIDENCE. This is the one that matters most at Contoso.
     Lab 04 gave you 13 compliance requirements and the instruction that
     coverage must be MEASURED, not asserted. The RTM is the measurement.
     For every C-nn, the matrix names the requirement that implements it and
     the test case that proves it. Compliance coverage fraction = number of
     C-nn with a passing linked test / 13. That single fraction is what the
     DPO is shown at the gate. An assertion that "we are compliant" without
     the matrix behind it is not evidence and will not clear G3.

  3. SCOPE CONTROL. Anything being built that has no row in the matrix is,
     by definition, not in scope. This is how you detect scope creep in the
     build rather than in the budget three months later.
```

Compute the current compliance coverage from the matrix above and record it:

```text
COMPLIANCE COVERAGE FROM THE RTM

  Compliance requirements from Lab 04                        13
  C-nn appearing in the RTM with a linked requirement:
    C-01, C-02  -> REQ-018  consent capture
    C-04        -> REQ-026  encryption
    C-05        -> REQ-020  payment data handling
    C-06, C-07  -> REQ-019  accredited-course claim data
    C-09        -> REQ-021  access audit logging
    C-11        -> REQ-025  accessibility
    C-12        -> REQ-027  migration and retention
                                                Covered:      9
  NOT YET COVERED: C-03, C-08, C-10, C-13       Gap:          4

  COVERAGE = 9 / 13 = 69%

  This is the number that goes to the DPO now, in week 5 - not at G3. Four
  compliance requirements have no requirement implementing them, which means
  either they need requirements written, or they are satisfied by process
  rather than product and need a documented process control instead.
  Discovering that in week 5 is a task. Discovering it at G3 is the Lab 01
  scenario.
```

Close the gap before you baseline. Four additional requirements are needed - draft them and add them to the register as REQ-032 to REQ-035, each traced to its C-nn.

### Step 7 - Answer the exam-style scenarios

```text
SCENARIO 1
During the JAD workshop the Head of Sales states that the registration page
"must be modern and engaging". The BA writes this down as REQ-036. At the
requirements review, what is the correct action?

  A. Accept it; the Head of Sales is a senior stakeholder and it reflects a
     genuine concern.
  B. Reject it outright as out of scope.
  C. Return to the Head of Sales and convert it into testable requirements -
     what specifically would make it modern and engaging, and how would we
     know it had been achieved - or drop it if no testable statement emerges.
  D. Assign it a Could priority so it does not block the baseline.

SCENARIO 2
Three sprints after the requirements baseline, a developer notices that the
booking confirmation email also includes a marketing footer promoting other
courses. No requirement covers this. It took two days to build. What is this,
and what should the PM do?

  A. Nothing - it adds value to the learner at no extra cost.
  B. It is gold plating. It traces back to no business need and no
     stakeholder request, and it introduces a PDPA question about marketing
     consent that no requirement addresses. Remove it or, if it is genuinely
     wanted, put it through the change request process where its consent
     implications get assessed.
  C. Add a requirement retrospectively so the RTM is complete.
  D. Ask the product owner to accept it into the sprint.

SCENARIO 3
At gate G3 the DPO asks how you know that all 13 compliance requirements are
satisfied. Which response constitutes evidence?

  A. The compliance workstream 1.8 was completed and signed off by the dev lead.
  B. All 13 requirements were included in the requirements register at baseline.
  C. The RTM shows, for each of the 13 compliance requirements, the requirement
     that implements it and the test case that verifies it, with the test
     result attached - a coverage fraction of 13/13 with passing evidence.
  D. The penetration test returned no findings.
```

Answer key:

```text
SCENARIO 1 -> C.  "Modern and engaging" fails the testable criterion, so it is
            not yet a requirement. But the concern behind it may be real -
            the 34% abandonment suggests the current design genuinely fails
            users. The professional action is elicitation, not adjudication:
            go back and ask what specifically, and how we would know. This
            usually produces something usable ("registration on a phone
            without pinch-zoom", "no more than 12 fields") or reveals there
            was nothing behind it. A is wrong because seniority does not make
            a statement testable. B refuses without eliciting. D is the worst
            answer in practice - it parks an ambiguous requirement in the
            backlog where it will be argued about later at higher cost.

SCENARIO 2 -> B.  Gold plating is defined by the backward trace: work that
            traces to no requirement and no business need. The definitive
            detail here is the PDPA exposure - marketing content in a
            transactional email raises a consent question that REQ-018's
            purpose limitation does not cover. Unrequested work is not free
            even when it looks like a gift; it consumed two days of a
            capacity-constrained team and created compliance risk. C is
            precisely backwards - writing a requirement to justify work
            already done corrupts the RTM into a record of what was built
            rather than what was needed.

SCENARIO 3 -> C.  Evidence is a trace with a result attached. A is an
            assertion by a person. B shows intent at baseline but says
            nothing about what was actually built or verified. D is real
            evidence but covers only the subset of requirements a pen test
            exercises - it says nothing about consent capture, retention or
            accessibility. Only C measures coverage across all 13 and links
            each to verification, which is exactly the measurement Lab 04
            required and the reason the RTM was built.
```

## Deliverable

Submit to `artifacts/`:

- `09-requirements-mindmap.md` - the exported or screenshotted mind map with the central node, all eight branches and at least four sub-branch leaves each.
- `09-requirements-register.md` - at least 22 numbered requirements spanning business, stakeholder, functional, non-functional, transition and quality categories, each with source, priority and a testable acceptance criterion.
- The requirement attribute set completed for at least five requirements, including status and version.
- `09-rtm.md` - at least 12 populated rows tracing business need, charter requirement, requirement ID, WBS element, story, design artifact, test case and compliance requirement.
- The compliance coverage fraction computed from the RTM, with the uncovered C-nn named and the closing requirements drafted.
- The elicitation technique selection table with the technique chosen for each stakeholder group and the reason.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every non-functional requirement in your register contains a number and a measurement method. If any NFR reads "fast", "reliable" or "user-friendly", it is not finished.
- Every requirement has an acceptance criterion that could be handed to a tester who was not in the room.
- You used observation rather than interviews for the admin staff, and you can state why.
- Your register contains at least three transition requirements. If it has none, you have confused the product with the project.
- Your RTM traces in both directions, and you can demonstrate an impact analysis by naming every downstream artifact affected by a change to REQ-018.
- You computed a compliance coverage fraction as a number, found it was below 13/13, and drafted the requirements to close the gap - rather than assuming coverage.
- You can state what happens to a requirement after baseline and what does not require a change request in the hybrid model.
- No requirement in your register specifies a technology choice unless a named stakeholder genuinely requires that technology.
