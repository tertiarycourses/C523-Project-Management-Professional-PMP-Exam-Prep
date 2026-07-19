# Project Management Professional (PMP) Exam Prep — Learner Guide

**Course Code:** C523  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 20 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Business Environment](#topic-01--business-environment)
  - [Lab 1 — PMP Exam Orientation and 35 PDU Study Plan](#lab-1--pmp-exam-orientation-and-35-pdu-study-plan)
  - [Lab 2 — PESTLE and TECOP External Environment Scan](#lab-2--pestle-and-tecop-external-environment-scan)
  - [Lab 3 — EEF/OPA Inventory, Governance and Escalation Thresholds](#lab-3--eefopa-inventory-governance-and-escalation-thresholds)
  - [Lab 4 — Compliance, Sustainability and AI-Governance Register](#lab-4--compliance-sustainability-and-ai-governance-register)
- [Topic 02 — Start the Project](#topic-02--start-the-project)
  - [Lab 5 — Business Case and Cost-Benefit Analysis](#lab-5--business-case-and-cost-benefit-analysis)
  - [Lab 6 — Project Charter](#lab-6--project-charter)
  - [Lab 7 — Stakeholder Register, Power/Interest Grid and Salience Model](#lab-7--stakeholder-register-powerinterest-grid-and-salience-model)
  - [Lab 8 — Team Charter, Ground Rules and Shared Vision](#lab-8--team-charter-ground-rules-and-shared-vision)
- [Topic 03 — Plan the Project](#topic-03--plan-the-project)
  - [Lab 9 — Requirements Elicitation, Mind Mapping and the Traceability Matrix](#lab-9--requirements-elicitation-mind-mapping-and-the-traceability-matrix)
  - [Lab 10 — MoSCoW, Kano and the Product Backlog](#lab-10--moscow-kano-and-the-product-backlog)
  - [Lab 11 — Work Breakdown Structure and WBS Dictionary](#lab-11--work-breakdown-structure-and-wbs-dictionary)
  - [Lab 12 — Network Diagram, PERT and the Critical Path](#lab-12--network-diagram-pert-and-the-critical-path)
  - [Lab 13 — Cost Estimating, Budget and Reserves](#lab-13--cost-estimating-budget-and-reserves)
  - [Lab 14 — Risk Register, RBS, EMV and Decision Tree](#lab-14--risk-register-rbs-emv-and-decision-tree)
- [Topic 04 — Lead the Project Team](#topic-04--lead-the-project-team)
  - [Lab 15 — RACI Responsibility Assignment Matrix and Resource Plan](#lab-15--raci-responsibility-assignment-matrix-and-resource-plan)
  - [Lab 16 — Tuckman Diagnosis, Motivation Theory and Leadership Style](#lab-16--tuckman-diagnosis-motivation-theory-and-leadership-style)
  - [Lab 17 — Conflict Resolution: Five Modes, Leas' Levels and Negotiation](#lab-17--conflict-resolution-five-modes-leas-levels-and-negotiation)
  - [Lab 18 — Communication Plan, Channels and Status Reporting](#lab-18--communication-plan-channels-and-status-reporting)
- [Topic 05 — Monitor and Control the Project](#topic-05--monitor-and-control-the-project)
  - [Lab 19 — Kanban Board with WIP Limits and Lead/Cycle Time](#lab-19--kanban-board-with-wip-limits-and-leadcycle-time)
  - [Lab 20 — Earned Value Management and Schedule Compression](#lab-20--earned-value-management-and-schedule-compression)
  - [Lab 21 — Root Cause Analysis with 5 Whys, Fishbone and Pareto](#lab-21--root-cause-analysis-with-5-whys-fishbone-and-pareto)
  - [Lab 22 — SPC Control Chart and Statistical Process Analysis](#lab-22--spc-control-chart-and-statistical-process-analysis)
- [Topic 06 — Close the Project](#topic-06--close-the-project)
  - [Lab 23 — Project Closure, Benefits Realisation and Lessons Learned](#lab-23--project-closure-benefits-realisation-and-lessons-learned)
  - [Lab 24 — Capstone - Integrated Project Management Plan and Mock Exam](#lab-24--capstone---integrated-project-management-plan-and-mock-exam)
- [Wrap-Up and Exam Readiness](#wrap-up-and-exam-readiness)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Project Management Professional (PMP) Exam Prep course. It delivers the 35 contact hours of formal project management education that PMI requires before you may sit the PMP examination, and it is aligned to the PMI PMP Examination Content Outline (ECO) effective July 2026 — People 33%, Process 41%, Business Environment 26%.

The course is built on a single continuous case study, the Contoso Training Portal Upgrade. All 24 hands-on labs work that one project from environment scan through authorisation, planning, delivery, control and closure. Each lab consumes artifacts produced by earlier labs, so by the capstone you hold a complete integrated project management plan you built yourself. The project is deliberately hybrid, because the exam is: roughly 40% of items sit in a predictive context and the rest split between adaptive/agile and hybrid.


## Course Learning Outcomes

- LO1: Scope project requirements and build a business case, charter and traceable scope baseline that authorise delivery.
- LO2: Develop an integrated project plan with realistic schedule, cost and resource baselines using PERT, critical path and reserve analysis.
- LO3: Lead a project team through its development stages, applying leadership style, motivation theory and structured conflict resolution.
- LO4: Analyse project risk quantitatively and engage stakeholders through a planned communication and escalation cadence.
- LO5: Control delivery against baselines with earned value, flow metrics and statistical process control, then close the project and realise benefits.
- LO6: Apply the PMI PMP Examination Content Outline (ECO 2026) across all three domains and sit a full-format mock exam with domain score analysis.


## Before You Start — Preparation

**What you need**

- A laptop with a modern browser (Chrome, Edge, Firefox or Safari).
- A spreadsheet application for the estimating, cost and earned value labs.
- A folder for your lab artifacts — see the structure in labs/tools.md.
- A printed or on-screen copy of the PMI ECO 2026 for reference.
- A pen and paper: the exam gives you no spreadsheet, so practise by hand.

**Verify your setup**

Confirm your setup before Lab 01: create the artifacts folder and open one of the live browser tools to check it loads.

```bash
mkdir -p pmp-labs/artifacts && cd pmp-labs
```

**Conventions used in every lab**

- Placeholders such as <YOUR NAME> are replaced with your own values.
- Artifacts are written to artifacts/NN-name.md, numbered by the lab that produced them.
- Every lab states what it Consumes and what it Produces — check both before starting.
- The live browser tools need no installation, no login, and send no data anywhere.
- 'Exam tell' boxes flag the cue the PMP examination uses for that concept.


## Topic 01 — Business Environment

Foundations · governance · compliance · change · development approaches

**Key concepts**

- A project is a temporary endeavour creating a unique product, service or result — it is bounded in time and delivers change, unlike operations.
- The 12 PMI principles and the triple constraint frame every tailoring decision you make on the exam and on the job.
- Two life cycles, five approaches: the project life cycle is the phases; the development life cycle is predictive, iterative, incremental, agile or hybrid.
- EEFs constrain you and OPAs are reusable assets — you conform to EEFs, you apply and then update OPAs.
- Governance sets escalation thresholds: escalate outside tolerance with options, resolve inside tolerance with the team; phase gates decide go, change, hold or kill.
- Compliance, sustainability and the responsible use of AI are the project manager's own obligations, not someone else's department.


### Lab 1 — PMP Exam Orientation and 35 PDU Study Plan

Learning outcome: Business Env T1 - Define and establish project governance (success metrics).

Goal: Reconstruct the ECO (July 2026) blueprint from its totals - 180 questions, 170 scored, 240 minutes - deriving the per-domain scored counts and the 80-second pacing rule by hand. Catalogue all six question types including graphic-based items, record the 35 contact-hour evidence, and build a six-week study plan weighted to the domain percentages. Test answer-selection heuristics on three Contoso case scenarios.

**What you'll build**

An exam blueprint with derived question counts and pacing figure (artifacts/01-exam-blueprint.md), a 35 contact-hour record (artifacts/01-pdu-log.md), a six-week weighted study plan (artifacts/01-study-plan.md), answer-selection heuristics and a baseline score.   (Tools: Spreadsheet, Markdown editor.)

**Step-by-step**

1. Build the exam blueprint from the ECO 2026 numbers and derive the per-domain scored-question counts
2. Log the six question types and write an approach for each under time pressure
3. Record your 35 contact-hour evidence against the PMP eligibility rule
4. Build a six-week study plan weighted to the blueprint domain percentages
5. Write your answer-selection heuristics: what to eliminate and what to prefer
6. Apply the heuristics to three scenarios, naming the heuristic that decided each
7. Set your baseline score over 20 timed practice questions

**Test it**

The per-domain counts read 56 / 70 / 44 and sum to exactly 170; the pacing figure is 80 seconds per question derived from 240 / 180; the study plan gives Process the largest single hour allocation and contains two full-length timed mocks in the final week; and each scenario answer names a heuristic rather than only a letter.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 2 — PESTLE and TECOP External Environment Scan

Learning outcome: Business Env T8 - Evaluate external business environment changes; Business Env T7 - Support organizational change.

Goal: From the Contoso briefing pack, run a PESTLE scan across all six categories, scoring every factor for impact and likelihood. Run a TECOP scan over the five risk dimensions to surface the operational and political exposure PESTLE misses. Combine and rank both tables, take the vital few scoring 16 or above, and translate each into a scope, backlog or cost consequence with a named destination artifact.

**What you'll build**

A scored six-category PESTLE scan (artifacts/02-pestle-scan.md), a scored five-dimension TECOP scan (artifacts/02-tecop-scan.md), a combined ranked factor table, and a backlog-impact table mapping each top factor to its destination artifact (artifacts/02-backlog-impacts.md).   (Tools: PESTLE, TECOP, Mind Mapping.)

**Step-by-step**

1. Read the Contoso operating-environment briefing pack
2. Build and score the PESTLE table, adding at least two factors of your own
3. Run the TECOP scan across the technical, environmental, commercial, operational and political dimensions
4. Rank the combined factors and take the vital few scoring 16 or above
5. Translate each ranked factor into a scope and backlog consequence with a destination artifact
6. Set the review cadence, owner and out-of-cycle triggers
7. Answer the exam-style scenarios on responding to external change

**Test it**

Every PESTLE letter carries at least one factor, every score is the product of a stated impact and likelihood, the TECOP table surfaced at least one factor absent from the PESTLE table, and every factor scoring 16 or above has a named destination artifact in a later lab rather than a vague instruction to monitor.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 3 — EEF/OPA Inventory, Governance and Escalation Thresholds

Learning outcome: Business Env T1 - Define and establish project governance; Business Env T4 - Remove impediments and manage issues.

Goal: Separate Enterprise Environmental Factors - conditions the project must live with - from Organizational Process Assets, the templates and standards it reuses. Design the Contoso governance model: which body decides what, at which cadence, with what rights. Set numeric escalation thresholds for cost, schedule, risk and issue severity, and separate the change control path from the issue resolution path.

**What you'll build**

A classified EEF/OPA inventory (artifacts/03-eef-opa-inventory.md), a governance model naming decision bodies, rights, cadence and success metrics (artifacts/03-governance-model.md), and a numeric escalation threshold table separating change and issue paths (artifacts/03-escalation-thresholds.md).   (Tools: Spreadsheet, Markdown editor.)

**Step-by-step**

1. Inventory the Contoso Enterprise Environmental Factors
2. Inventory the Contoso Organizational Process Assets
3. Design the governance model: bodies, decision rights and cadence
4. Define the project success metrics and their measurement baselines
5. Set numeric escalation thresholds for cost, schedule, risk and issues
6. Separate the change control path from the issue resolution path
7. Answer the exam-style scenarios on governance and escalation

**Test it**

Every item in the inventory is classified as an EEF or an OPA and the learner can justify each classification; each governance body has a named decision right and cadence; every escalation threshold carries a number rather than a word such as significant; and the change path and the issue path are visibly different routes with different owners.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 4 — Compliance, Sustainability and AI-Governance Register

Learning outcome: Business Env T2 - Plan and manage project compliance; Process T7 - Plan and optimize quality (regulatory compliance, sustainability).

Goal: Classify Contoso's compliance requirements - PDPA personal-data protection, the statutory seven-year attendance retention obligation and the pre-go-live review - then identify the threats to each and quantify the consequences of noncompliance. Decide the actions and how compliance is measured. Add the two areas the July 2026 ECO expects: net-zero hosting, and AI governance for the deferred AI recommender.

**What you'll build**

A compliance register with threats, consequences, actions and measures (artifacts/04-compliance-register.md), a sustainability plan covering the net-zero hosting obligation (artifacts/04-sustainability-plan.md), and an AI-governance register (artifacts/04-ai-governance.md).   (Tools: Spreadsheet, Markdown editor.)

**Step-by-step**

1. Confirm the compliance requirements and classify them by category
2. Identify the threats to each compliance requirement
3. Analyse and quantify the consequences of noncompliance
4. Decide the approach and the specific actions for each requirement
5. Define how compliance is measured, with evidence and a measurement owner
6. Build the sustainability section against the group net-zero obligation
7. Build the AI-governance register for the deferred AI recommender
8. Answer the exam-style scenarios on compliance decisions

**Test it**

Every compliance requirement has a named threat, a quantified consequence, an action and a measurement method with an owner; the sustainability section ties to a reportable hosting carbon figure; and the AI-governance register records data use, human oversight and an accountable owner rather than a general statement of intent.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


## Topic 02 — Start the Project

Business case · charter · stakeholders · team formation

**Key concepts**

- The business case justifies the project; the charter authorises it. The business case can exist without a project — the charter cannot.
- Cost-benefit analysis with NPV, payback and BCR turns a proposal into a defensible investment decision.
- The charter is issued by the sponsor, names the project manager and states their authority level — it is high level and rarely changed.
- Stakeholder identification, power/interest analysis and the salience model determine who gets what engagement and how often.
- The team charter establishes ground rules and a shared vision before the first conflict, not after it.
- The development approach is a documented tailoring decision justified by project context — never a personal preference.


### Lab 5 — Business Case and Cost-Benefit Analysis

Learning outcome: Process T3 - Help ensure value-based delivery; Process T6 - Plan and manage finance.

Goal: Turn the Contoso baseline metrics into a quantified benefits model, then build the cost side against the board-approved SGD 480,000 ceiling. Compute payback, NPV, ROI and benefit-cost ratio by hand, including the year-zero outflow most commonly dropped from NPV. Stress-test against the Lab 02 downside of an 8% fall in enrolment, then choose among options including a costed do-nothing.

**What you'll build**

A quantified cost-benefit model with payback, NPV, ROI and BCR plus a downside sensitivity run (artifacts/05-cba-model.md), a written business case with a recommendation and its deciding measure (artifacts/05-business-case.md), and a benefits realisation map (artifacts/05-benefits-map.md).   (Tools: Statistics, Spreadsheet.)

**Step-by-step**

1. Quantify the benefits from the Lab 03 baseline metrics
2. Build the cost side against the board-approved budget ceiling
3. Compute payback period, NPV, ROI and benefit-cost ratio by hand
4. Stress-test the case against the Lab 02 downside enrolment scenario
5. Choose among the project options, including a costed do-nothing option
6. Write the business case document with a recommendation
7. Build the benefits realisation map for later closure measurement
8. Answer the exam-style scenarios on value and sunk cost

**Test it**

Every benefit line traces to a Lab 03 baseline metric; all discount factors fall below 1 and decrease with time; the NPV subtracts the year-zero investment; the BCR is total benefit over total cost and exceeds 1; the do-nothing option carries a negative number rather than a blank; and the recommendation cites NPV as the deciding measure.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 6 — Project Charter

Learning outcome: Process T1 - Develop an integrated project management plan and plan delivery; Process T2 - Develop and manage project scope.

Goal: Assemble the governance model, compliance requirements and business-case financials into a charter that authorises the project. State success criteria each carrying a numeric baseline and target, and define scope boundaries including exclusions with traceable rationales. Name the PM's procurement and change-approval authority in figures matching the Lab 03 thresholds, and open the assumption log.

**What you'll build**

A project charter with measurable success criteria, scope boundaries, exclusions, milestones, budget and PM authority (artifacts/06-project-charter.md), a development-approach decision (artifacts/06-approach-decision.md) and an assumption log with validation dates (artifacts/06-assumption-log.md).   (Tools: Markdown editor, Spreadsheet.)

**Step-by-step**

1. Assemble the charter inputs from the governance, compliance and business-case artifacts
2. Write the charter header and the purpose statement
3. State measurable success criteria with numeric baselines and targets
4. Define scope boundaries, including exclusions and their rationale
5. Record the high-level requirements, milestones and budget
6. Name the project manager's authority in specific procurement and change-approval figures
7. Document the hybrid development approach as a tailoring decision
8. Build the assumption and constraint log with validation dates
9. Answer the exam-style scenarios on charter authority and scope

**Test it**

Every success criterion carries a numeric baseline and target; the charter has a sponsor signature block; every exclusion has a traceable rationale; the milestone list contains milestones only and no durations; the approach decision names what is predictive, what is adaptive and the interface between them; and every assumption has a validation date before being wrong becomes unrecoverable.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 7 — Stakeholder Register, Power/Interest Grid and Salience Model

Learning outcome: People T4 - Engage stakeholders; People T5 - Align stakeholder expectations; People T6 - Manage stakeholder expectations.

Goal: Identify the full Contoso stakeholder set, including forgotten groups such as the three admin staff who are also subject matter experts. Analyse each on power, interest, attitude and impact, plot the power/interest grid and derive the strategy per quadrant. Where the grid fails, apply the salience model of power, legitimacy and urgency. Build the current-versus-desired engagement matrix and close each gap.

**What you'll build**

A stakeholder register scored on power, interest, attitude and impact (artifacts/07-stakeholder-register.md), a power/interest grid (artifacts/07-power-interest-grid.md), a salience analysis (artifacts/07-salience-model.md) and an engagement matrix (artifacts/07-engagement-matrix.md).   (Tools: Power/Interest Grid, Salience Model, Spreadsheet.)

**Step-by-step**

1. Identify the full stakeholder set, including the groups projects habitually forget
2. Build the stakeholder register with power, interest, attitude and impact
3. Plot the power/interest grid and derive the strategy each quadrant demands
4. Apply the salience model where the grid fails to give a usable answer
5. Build the current-versus-desired engagement matrix
6. Surface and plan to resolve the misaligned stakeholder expectations
7. Set a tailored engagement cadence per stakeholder group
8. Answer the exam-style scenarios on stakeholder engagement

**Test it**

The register includes the three admin staff; every stakeholder has numeric power and interest scores matching their grid position; the salience analysis produced at least one insight the grid did not; every current-to-desired gap has an action with an owner and date; the expectation-conflict plan attaches a trade-off number; and the cadence differs by stakeholder rather than one fortnightly email for everyone.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 8 — Team Charter, Ground Rules and Shared Vision

Learning outcome: People T1 - Develop a common vision; People T3 - Lead the project team.

Goal: Draft a shared vision short enough to recall without reading it, traced to the Lab 06 success criteria. Build the team charter: name all nine members, write the working agreement on core hours and time zones, and set ground rules across six categories, each with an observable violation test. Agree a definition of done separating done from released, and set the decision rule - consent, consensus or command.

**What you'll build**

A vision statement traced to the charter success criteria (artifacts/08-vision-statement.md), a team charter with the working agreement, definition of done, decision-rule table and skills matrix (artifacts/08-team-charter.md), and six ground-rule categories (artifacts/08-ground-rules.md).   (Tools: Team Charter, Definition of Done, Skills Matrix.)

**Step-by-step**

1. Draft the shared vision statement and test it against the criteria
2. Name the team and record each member's role
3. Write the working agreement on core hours, time zones and availability
4. Set ground rules across the six categories, each with an observable standard
5. Agree the definition of done that QA and the developers will both accept
6. Choose the decision-making rule for each class of decision and name the decider
7. Build the skills and capacity matrix and expose the single points of failure
8. Design the graduated response to ground-rule violations
9. Forward-reference the responsibility assignment matrix and set the vision review cadence
10. Answer the exam-style scenarios on team leadership and ground rules

**Test it**

The vision is under 30 words and traces to at least two numbered charter success criteria; every ground rule has a violation test; the definition of done separates done from released; the decision table uses at least two rules and names a decider for every command-rule row; and the skills matrix identifies at least three single points of failure, each with a named owner and dated mitigation.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


## Topic 03 — Plan the Project

Scope · schedule · cost · quality · resources · communications · risk

**Key concepts**

- The integrated project management plan is the sum of subsidiary plans plus the scope, schedule and cost baselines.
- Requirements elicitation feeds a requirements traceability matrix so every deliverable traces back to a business need.
- MoSCoW and Kano prioritise the backlog by value; the WBS decomposes scope to work packages with a WBS dictionary.
- PERT three-point estimating and critical path analysis expose which activities actually drive the finish date and where float exists.
- Cost estimating produces a budget with contingency reserve for known unknowns and management reserve for unknown unknowns.
- Risk identification, qualitative and quantitative analysis with EMV and decision trees produce a risk register with owned responses.


### Lab 9 — Requirements Elicitation, Mind Mapping and the Traceability Matrix

Learning outcome: Process T2 - Develop and manage project scope; Process T1 - Develop an integrated project management plan..

Goal: Turn the six charter requirements into a testable requirement set. Match elicitation techniques to stakeholder groups rather than defaulting to interviews, then expand them into a mind map. From the map write a 31-line register (REQ-001 to REQ-031) across the business, stakeholder, functional, non-functional, transition and quality categories. Build a bidirectional RTM from source to deliverable and test.

**What you'll build**

A requirements mind map, a 31-requirement register with sourced, prioritised and testable entries, and a bidirectional RTM carrying the 13 compliance requirements to the governance gate - artifacts/09-requirements-mindmap.md, artifacts/09-requirements-register.md and artifacts/09-rtm.md.   (Tools: Mind Mapping, Design Thinking (optional).)

**Step-by-step**

1. Choose elicitation techniques deliberately, matching each technique to the stakeholder group and noting its weakness
2. Build the requirements mind map in the live Mind Mapping tool from the six charter requirements
3. Write the requirements register across all six categories, with a source, priority and acceptance criterion per line
4. Set requirement attributes and versioning, and define the route by which a baselined requirement changes
5. Build the bidirectional requirements traceability matrix from source through deliverable to test
6. Work through what bidirectional traceability buys you when a requirement is challenged or dropped
7. Answer the exam-style scenarios on elicitation choice, requirement quality and traceability

**Test it**

Every requirement in the register has a unique ID, a named source, a MoSCoW priority and an acceptance criterion stated as a number or a pass/fail condition; no non-functional requirement is left unmeasurable. Each of the 13 compliance requirements C-01 to C-13 can be traced forward from the RTM to a deliverable and a test, and every requirement traces backward to a charter item or stakeholder.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 10 — MoSCoW, Kano and the Product Backlog

Learning outcome: Process T3 - Help ensure value-based delivery; Process T2 - Develop and manage project scope..

Goal: Prioritise the Lab 09 requirements with two models that deliberately disagree. Apply MoSCoW under discipline rules - legally required, contractually required, or non-viable without it - to separate Musts from wishes. Classify the same features on Kano as basic, performance, excitement, indifferent or reverse, and resolve each conflict. Write a story backlog in points and a capacity-based release plan.

**What you'll build**

A MoSCoW classification, a Kano classification of 14 features, a 21-plus story backlog with points and traces to REQ IDs, and a capacity-based release plan - artifacts/10-moscow.md, artifacts/10-kano.md, artifacts/10-product-backlog.md and artifacts/10-release-plan.md.   (Tools: Scrum Simulator.)

**Step-by-step**

1. Apply MoSCoW to the Lab 09 requirements using the legal, contractual and viability discipline tests
2. Classify the features on Kano as basic, performance, excitement, indifferent or reverse
3. Examine where MoSCoW and Kano disagree, and resolve each conflict with a stated rule
4. Write the product backlog as user stories with acceptance criteria and traces to requirement IDs
5. Estimate with story points rather than hours, and justify relative sizing
6. Build the release plan against real team capacity and verify the Must-haves land before the gate
7. Make the AI recommender trade-off numeric using story points against benefit value
8. Answer the exam-style scenarios on prioritisation, value delivery and backlog management

**Test it**

Every Must in the MoSCoW list survives the three discipline tests, and no more than the agreed share of total story points sits in Must. The release plan arithmetic reconciles: summed Must-have points divided by measured team velocity fits inside the sprints available before the gate, with the shortfall or slack stated explicitly. Each Kano basic is also a MoSCoW Must.

> **Note:** Full commands and screenshots are in labs/lab-10-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 11 — Work Breakdown Structure and WBS Dictionary

Learning outcome: Process T2 - Develop and manage project scope (break down scope); Process T1 - Develop an integrated project management plan..

Goal: Decompose the Contoso scope into a deliverable-oriented WBS to three levels under the 100% rule, using the 8/80 rule and the estimate-and-assign test to decide when to stop. Every charter in-scope item must appear in the tree, no out-of-scope item anywhere. Write dictionary entries carrying effort in person-days, cost, predecessors, acceptance criteria and a control account, then assemble the scope baseline.

**What you'll build**

A three-level deliverable-oriented WBS, a WBS dictionary with costed and estimated work-package entries, and the assembled scope baseline - artifacts/11-wbs.md, artifacts/11-wbs-dictionary.md and artifacts/11-scope-baseline.md.   (Tools: WBS decomposition, 8/80 rule, Rolling wave planning.)

**Step-by-step**

1. Confirm the inputs and the scope boundary from the charter, register and backlog
2. Build the WBS to three levels, deliverable-oriented, under the 100% rule
3. Trace the compliance workstream back to the environmental factor that created it
4. Write the WBS dictionary entries with effort, cost, predecessors and acceptance criteria
5. Place control accounts and planning packages for the work not yet knowable
6. Assemble the scope baseline and state exactly what it contains
7. Reconcile the WBS with the product backlog so the two do not duplicate each other
8. Answer the exam-style scenarios on decomposition, the 100% rule and baseline control

**Test it**

Roll the work-package effort and cost estimates up each branch and confirm they sum to the level-2 and level-1 totals with no orphan work and no double counting - this is the 100% rule proved arithmetically. Check every charter in-scope item appears exactly once in the tree, that no out-of-scope item appears at all, and that each work package sits inside the 8/80 hour band and can be assigned to one owner.

> **Note:** Full commands and screenshots are in labs/lab-11-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 12 — Network Diagram, PERT and the Critical Path

Learning outcome: Process T8 - Plan and manage schedule..

Goal: Convert the Lab 11 work packages into an activity list, sequence them with the four dependency types, and draw the precedence network. Compute the forward and backward pass by hand for early/late start and finish, total and free float, taking the critical path as the zero-float chain. Apply three-point estimating with the triangular and PERT beta formulas, then compare crashing against fast-tracking on cost per day.

**What you'll build**

An activity list, a precedence network, a critical path with float per activity, PERT durations with variance, a costed compression analysis and the schedule baseline - artifacts/12-activity-list.md, artifacts/12-network-diagram.md, artifacts/12-critical-path.md, artifacts/12-schedule-baseline.md.   (Tools: PERT, Critical Path Method, Forward and backward pass, Crashing and fast-tracking.)

**Step-by-step**

1. Derive the activity list from the WBS work packages, converting deliverables into activities
2. Understand the dependencies just declared, separating mandatory from discretionary logic
3. Draw the precedence network diagram with the four dependency types
4. Compute the forward and backward pass, then total float and free float per activity
5. Apply three-point estimating with both formulas and compute the project confidence range from variance
6. Compress the schedule by comparing crashing and fast-tracking on cost per day saved
7. Apply the lessons-learned constraint that compliance review precedes UAT, and price the parallel alternative
8. Build the schedule baseline from the accepted network and durations
9. Answer the exam-style scenarios on float, critical path and compression

**Test it**

The backward pass must reproduce the forward pass: project late finish equals early finish, and every critical-path activity shows zero total float. Confirm the PERT roll-up - expected duration near 123 days, standard deviation about 4.73 days, a 95.45% range of roughly 113.5 to 132.5 days - by summing critical-path variances. The compression must shorten the critical path, not a float-bearing chain.

> **Note:** Full commands and screenshots are in labs/lab-12-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 13 — Cost Estimating, Budget and Reserves

Learning outcome: Process T6 - Plan and manage finance; Process T1 - Develop an integrated project management plan..

Goal: Select estimating techniques against the information available and state each one's accuracy range, then build a bottom-up estimate from the Lab 11 work packages and reconcile it to the charter budget. Separate contingency from management reserve - who authorises release, which sits in the cost baseline - and size contingency by expected monetary value. Time-phase into a cost baseline S-curve.

**What you'll build**

A bottom-up cost estimate reconciled to the charter, an EMV-sized contingency reserve, a time-phased cost baseline S-curve with the funding requirement above it, and a cost-of-quality analysis - artifacts/13-cost-estimates.md, artifacts/13-cost-baseline.md and artifacts/13-reserve-analysis.md.   (Tools: Statistics, Bottom-up estimating, Expected Monetary Value.)

**Step-by-step**

1. Build the bottom-up estimate from the WBS work packages and reconcile it to the charter budget
2. Distinguish contingency reserve from management reserve, including authority and baseline placement
3. Size the contingency reserve by expected monetary value rather than by percentage
4. Build the time-phased cost baseline as an S-curve
5. Perform funding limit reconciliation against the cash-flow profile
6. Analyse the cost of quality across prevention, appraisal, internal failure and external failure
7. Answer the exam-style scenarios on estimating accuracy, reserves and baseline versus budget

**Test it**

The money must add up both ways: work-package estimates plus contingency equals the cost baseline, and cost baseline plus management reserve equals the total budget. Confirm the EMV sizing by recomputing probability times impact per priced risk. The cumulative S-curve must end at the cost baseline total, and funding limit reconciliation must show no period where planned spend exceeds the authorised tranche.

> **Note:** Full commands and screenshots are in labs/lab-13-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 14 — Risk Register, RBS, EMV and Decision Tree

Learning outcome: Business Environment T5 - Plan and manage risk; Business Environment T4 - Support organisational change..

Goal: Build a risk breakdown structure and use it to identify risks systematically, tracing them from the Lab 02 environment scan and the Lab 06 assumption log - every assumption is a latent risk. Write each in cause-event-effect form, then assess the register on a probability/impact matrix and by expected monetary value. Give each a response from the ten strategies and solve a decision tree on EMV.

**What you'll build**

A risk breakdown structure, a risk register with cause-event-effect statements and owners, a plotted probability/impact matrix, a full EMV analysis and a solved decision tree - artifacts/14-risk-register.md, artifacts/14-rbs.md, artifacts/14-pi-matrix.md and artifacts/14-emv-analysis.md.   (Tools: System Thinking, EMV, Decision Tree, Probability/Impact Matrix.)

**Step-by-step**

1. Build the risk breakdown structure and use it to drive systematic identification
2. Trace risks from the Lab 02 PESTLE/TECOP factors and the Lab 06 assumption log
3. Write risk statements in cause-event-effect form
4. Build the risk register with probability, impact, owner and trigger per risk
5. Plot the probability/impact matrix and rank the risks by score
6. Apply all ten response strategies - five for threats and five for opportunities
7. Compute expected monetary value for each priced risk and for the portfolio
8. Build and solve a decision tree for a real Contoso decision and defend the recommendation
9. Distinguish qualitative from quantitative analysis, and a risk from an issue
10. Answer the exam-style scenarios on response strategy selection, EMV and secondary risk

**Test it**

Recompute each risk's EMV as probability times impact, summing threats and opportunities separately - the net portfolio EMV must reconcile with the contingency reserve sized in Lab 13. Solve the decision tree by rolling values back from the leaves; the recommended branch must have the highest expected value net of cost. Every register row carries an owner, a trigger and one of the ten strategies.

> **Note:** Full commands and screenshots are in labs/lab-14-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


## Topic 04 — Lead the Project Team

Leadership · motivation · conflict · coaching · communication

**Key concepts**

- Tuckman's forming, storming, norming, performing and adjourning gives you a diagnosis, and each stage calls for a different leadership response.
- Situational leadership, servant leadership and motivation theory (Maslow, Herzberg, McClelland, Theory X/Y) drive team performance.
- RACI removes ambiguity: exactly one Accountable per work package, Responsible parties who do the work.
- The five conflict modes — collaborate, compromise, smooth, force, withdraw — are chosen by context; collaborate/problem-solve is preferred.
- The channels formula n(n-1)/2 shows why communication complexity grows faster than team size.
- A communication plan defines who needs what information, in what format, how often, and through which channel.


### Lab 15 — RACI Responsibility Assignment Matrix and Resource Plan

Learning outcome: People T3 - Lead the project team (establish clear roles and responsibilities within the team); Process T4 - Plan and manage resources..

Goal: Build a RACI matrix from the Lab 11 WBS work packages, defending every assignment against the one-accountable rule. The supplied draft carries five deliberate defects - missing accountability, two accountables on a row, over-consultation, an unassigned role and an unowned work package - which you audit out and fix. Build the resource histogram and distinguish levelling from smoothing.

**What you'll build**

A defect-free RACI matrix over the WBS work packages, a documented audit of the five structural defects with fixes, and a resource plan with a levelled histogram - artifacts/15-raci-matrix.md, artifacts/15-resource-plan.md and artifacts/15-raci-issues.md.   (Tools: RACI Matrix.)

**Step-by-step**

1. Assemble the inputs from the WBS dictionary, team charter and stakeholder register
2. Draft the matrix, accepting that the supplied draft contains deliberate defects
3. Enter the matrix in the live RACI Matrix tool
4. Audit the matrix and find the five structural defects
5. Compare before and after in numbers, counting assignments per row and per role
6. Build the resource plan and the resource histogram
7. Level or smooth the over-allocation, and state which technique can move the critical path
8. Connect the RACI to the communication plan so the C and I entries drive the distribution list
9. Answer the exam-style scenarios on accountability, over-consultation and levelling versus smoothing

**Test it**

Audit the corrected matrix row by row and column by column: every work-package row shows exactly one A and at least one R, no row is empty, and no role column is empty. Compare the histogram before and after: levelling must remove every allocation above 100%, and the learner must state whether the end date moved (levelling) or held (smoothing).

> **Note:** Full commands and screenshots are in labs/lab-15-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 16 — Tuckman Diagnosis, Motivation Theory and Leadership Style

Learning outcome: People T3 - Lead the project team; People T1 - Develop a common vision..

Goal: Diagnose the team's Tuckman stage from the sprint 3 behavioural evidence rather than elapsed time, naming structural causes not personalities, then select the leader actions that move a team out of storming. Apply six motivation theories - Maslow, Herzberg, McGregor, McClelland, Vroom and Self-Determination - for one action each. Compute a Vroom score as expectancy times instrumentality times valence.

**What you'll build**

A Tuckman diagnosis with structural causes and leader actions, per-member motivation profiles with one action from each of the six theories, and a leadership style map - artifacts/16-tuckman-diagnosis.md, artifacts/16-motivation-plan.md and artifacts/16-leadership-style-plan.md.   (Tools: Tuckman model, Situational Leadership, Vroom Expectancy calculation.)

**Step-by-step**

1. Read the sprint 3 evidence and record the observed behaviours without interpreting them yet
2. Diagnose the Tuckman stage and name the structural causes behind it
3. Choose the leader actions that move a team out of storming
4. Apply the six motivation theories, producing one specific action from each
5. Build per-member motivation profiles, computing the Vroom expectancy score numerically
6. Map a situational leadership style to each member's competence and commitment
7. Distinguish servant leadership from laissez-faire behaviourally and by outcome
8. Answer the exam-style scenarios on stage diagnosis, Herzberg and style selection

**Test it**

The diagnosis cites at least three observed sprint 3 behaviours and does not rest on how long the team has existed. Each Vroom score is computed as expectancy times instrumentality times valence, with the lowest factor identified as the one to fix - a low score with high valence and instrumentality points at expectancy - and the action must target that factor. Every member carries a different style justification.

> **Note:** Full commands and screenshots are in labs/lab-16-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 17 — Conflict Resolution: Five Modes, Leas' Levels and Negotiation

Learning outcome: People T2 - Manage conflicts..

Goal: Place the five conflict-handling modes on the assertiveness and cooperativeness axes, state each one's legitimate use, and identify the cases where collaborate - usually the keyed answer - is wrong. Diagnose intensity on Leas' five levels from the language people use. Run four Contoso role-plays, recording each in a conflict log. Close on negotiation: positions versus interests, BATNA and ZOPA.

**What you'll build**

A conflict log recording level, mode, intervention and outcome per incident, observer notes and debriefs for the four role-plays, and a resolution plan with a BATNA and ZOPA analysis - artifacts/17-conflict-log.md, artifacts/17-roleplay-notes.md and artifacts/17-resolution-plan.md.   (Tools: Thomas-Kilmann five modes, Leas' Levels, BATNA and ZOPA analysis.)

**Step-by-step**

1. Build the conflict log with columns for level, mode, intervention and outcome
2. Run role-play 1: two developers on architecture at Leas' level 1 to 2
3. Run role-play 2: Head of Sales versus product owner on scope at level 3
4. Run role-play 3: QA lead versus dev lead on the definition of done at level 2 to 3
5. Run role-play 4: admin staff versus Ops Manager on redundancy, escalating and high emotion
6. Build the resolution plan from the four logged conflicts
7. Apply negotiation: separate positions from interests, and compute BATNA and ZOPA
8. Answer the exam-style scenarios on mode selection and escalation thresholds

**Test it**

Every conflict log row names a Leas' level, the mode chosen, and why that mode beat collaborate - a level 4 or 5 entry that still selects collaborate is a failed diagnosis. The negotiation analysis states each party's BATNA explicitly and shows the ZOPA as a numeric range between the two reservation points, or states that no ZOPA exists and no deal is available.

> **Note:** Full commands and screenshots are in labs/lab-17-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 18 — Communication Plan, Channels and Status Reporting

Learning outcome: People T8 - Plan and manage communication; People T4 - Engage stakeholders..

Goal: Compute the communication channels with N(N-1)/2 and derive the implication of its superlinear growth. Select push, pull or interactive per stakeholder, place communications in the formal/informal by written/verbal grid, and build a plan where every row carries a feedback loop. Write the week-14 status three ways for three audiences, noticing that a CPI of 0.919 breaches the governance threshold.

**What you'll build**

A communication plan with computed channel counts, a push/pull/interactive assignment and a named feedback loop per stakeholder row, plus three audience-specific week-14 status reports written from one set of numbers - artifacts/18-communication-plan.md and artifacts/18-status-reports.md.   (Tools: N(N-1)/2 channels formula, Sender-receiver model, Status reporting.)

**Step-by-step**

1. Compute the communication channels with N(N-1)/2 and derive the growth implication
2. Choose push, pull or interactive for each stakeholder and justify the choice
3. Place communications in the formal/informal by written/verbal grid
4. Build the communication plan with a named feedback loop on every row
5. Trace a message through the sender-receiver model and name the real noise sources
6. Work through the week-14 status data and compute the performance indices
7. Write the same status three ways for three different audiences from one set of numbers
8. Compare a bad status report with a good one and name what makes the difference
9. Answer the exam-style scenarios on channels, communication method and escalation

**Test it**

Recompute N(N-1)/2 before and after the proposed additions and confirm the channel count grows superlinearly - state the delta, not just the totals. Every plan row names a sender, audience, method, frequency and feedback loop. The three status reports reconcile to identical figures despite differing in emphasis, and the CPI of 0.919 is flagged against the governance cost variance threshold with the escalation named.

> **Note:** Full commands and screenshots are in labs/lab-18-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


## Topic 05 — Monitor and Control the Project

Earned value · flow metrics · quality control · change control · issues

**Key concepts**

- Earned value management combines scope, schedule and cost into CPI, SPI, EAC and VAC — it tells you THAT something is wrong, not why.
- Schedule compression is a choice between crashing (adds cost) and fast-tracking (adds risk); both must be justified against the baseline.
- Kanban flow metrics — WIP limits, lead time and cycle time — expose bottlenecks that a Gantt chart hides.
- Root cause analysis with 5 Whys, fishbone and Pareto finds the vital few causes behind most of the pain.
- Statistical process control separates assignable causes from common-cause noise, and a stable process can still fail its specification.
- Integrated change control evaluates every change against all baselines before approval — the change control board decides, the PM does not.


### Lab 19 — Kanban Board with WIP Limits and Lead/Cycle Time

Learning outcome: Process T9 - Evaluate project status; Business Environment T4 - Remove impediments and manage issues..

Goal: Build a nine-column Kanban board mirroring Contoso's workflow, separating active from queue columns so waiting time becomes visible. Set a justified WIP limit per column, load 18 story cards with backlog-entry, work-start and acceptance dates, and compute lead time, cycle time, throughput and flow efficiency. Apply Little's Law, then find the bottleneck and apply the five Theory of Constraints steps.

**What you'll build**

artifacts/19-kanban-board.md with the nine-column workflow and WIP limits; artifacts/19-flow-metrics.md with lead and cycle time, throughput, flow efficiency and the Little's Law verification; artifacts/19-bottleneck-analysis.md with the utilisation table and Theory of Constraints response.   (Tools: Kanban Board.)

**Step-by-step**

1. Design the workflow columns, separating active stages from queue stages
2. Set and justify a WIP limit for every column against the team composition
3. Load the 18 real cards with backlog-entry, work-start and acceptance dates
4. Compute the flow metrics - lead time, cycle time, throughput and flow efficiency
5. Apply Little's Law to verify stability and forecast the remaining release
6. Find the bottleneck from column utilisation and apply the Theory of Constraints steps
7. Read the cumulative flow diagram and interpret band width, slope and convergence
8. Answer the exam-style scenarios on Little's Law, WIP limits and lead versus cycle time

**Test it**

Mean lead time comes to 13.11 days against a mean cycle time of 6.94 days, a flow efficiency of 52.9%; Little's Law implies a WIP of about 6.25 against an observed 6 on day 12; Test is the bottleneck on its 100% utilisation, the 97% queue in front of it and the collapse to 33% downstream; and the learner rejects raising the In Test WIP limit, explaining why it would lengthen cycle time.

> **Note:** Full commands and screenshots are in labs/lab-19-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 20 — Earned Value Management and Schedule Compression

Learning outcome: Process T9 - Evaluate project status; Process T6 - Plan and manage budget and resources..

Goal: From the SGD 480,000 Contoso cost baseline, validate that cumulative planned value at the final period equals BAC, then compute CV, SV, CPI and SPI at the week-14 status date. Calculate all three EAC variants, choose the defensible one on evidence, and derive ETC, VAC and both TCPI figures. Analyse the seven-period CPI/SPI trend and choose between crashing and fast-tracking from the crash-cost table.

**What you'll build**

artifacts/20-evm-calculations.md with CV, SV, CPI and SPI plus the seven-period trend table; artifacts/20-forecast.md with all three EAC variants, ETC, VAC and both TCPI figures; artifacts/20-compression-decision.md with the five-day crash recovery, its cost and the rejection of fast-tracking.   (Tools: Statistics.)

**Step-by-step**

1. Take the cost baseline and actuals, and validate that cumulative PV equals BAC
2. Compute the variances and indices at week 14 - CV, SV, CPI and SPI
3. Forecast the outcome with all three EAC variants, plus ETC, VAC and TCPI
4. Analyse the seven-period CPI/SPI trend rather than the single snapshot
5. Check the result against the escalation thresholds and decide whether to escalate
6. Decide between crashing and fast-tracking using the crash-cost table
7. Write the variance report in sponsor format with three costed options and a recommendation
8. Answer the exam-style scenarios on EAC selection, EVM reading and trend interpretation

**Test it**

Cumulative PV at period 12 equals SGD 480,000; CV = -22,000 and SV = -19,000 are in dollars not days; CPI = 0.919 and SPI = 0.929, CPI carried to four decimals into EAC = SGD 522,420 and VAC = -SGD 42,420; the TCPI of 1.105 against CPI 0.919 makes recovery not credible; the crash selects J and O for SGD 15,500, rejecting non-critical F; and escalation is raised on the forecast, not the actual variance.

> **Note:** Full commands and screenshots are in labs/lab-20-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 21 — Root Cause Analysis with 5 Whys, Fishbone and Pareto

Learning outcome: Business Environment T4 - Remove impediments and manage issues; Process T7 - Plan and manage quality of products and deliverables; Business Environment T6 - Support continuous improvement..

Goal: Take the defect log for sprints 1 to 7 - the period over which CPI declined monotonically - and run the three root cause tools in sequence. Pareto on defect frequency isolates the vital few inside the 80% cut; a second Pareto by rework hours reveals where frequency and cost disagree. A fishbone generates causes across the six categories, and 5 Whys drives from symptom to root cause, verified with the removal test.

**What you'll build**

artifacts/21-pareto-analysis.md with the frequency and cost rankings and cumulative percentages; artifacts/21-fishbone.md with two causes per category; artifacts/21-5whys.md with the causal chain; artifacts/21-corrective-actions.md separating corrective from preventive action.   (Tools: Pareto Chart, Fishbone Diagram, 5 Whys.)

**Step-by-step**

1. Take the defect data covering sprints 1 to 7 with counts, rework hours and cost
2. Build the Pareto chart on defect frequency and locate the 80% cut
3. Re-run Pareto by rework cost and notice where the two rankings disagree
4. Fishbone the top category across all six cause categories
5. Drive from symptom to root cause with 5 Whys
6. Verify the root cause with the therefore test and the removal test before acting
7. Design corrective, preventive and defect-repair actions and assign owners
8. Answer the exam-style scenarios on root cause versus symptom and action type

**Test it**

Cumulative percentages reach 100% with the 80% cut at rank 5 on 81.55%; both Pareto runs rank acceptance criteria and browser compatibility first and second; every fishbone category carries two causes; the root cause is a system or process failure rather than an individual's shortcoming and passes the removal test; and the causal chain connects it back to the CPI decline found by earned value analysis.

> **Note:** Full commands and screenshots are in labs/lab-21-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 22 — SPC Control Chart and Statistical Process Analysis

Learning outcome: Process T7 - Plan and manage quality of products and deliverables; Process T9 - Evaluate project status..

Goal: Plot 20 daily measurements of median registration completion time and compute the centre line and control limits from the data itself, using the moving-range method rather than the sample standard deviation. Apply the out-of-control rules including the rule of seven and identify where the process shifts. Separate common from assignable cause, then assess capability - the process is in control yet fails specification.

**What you'll build**

artifacts/22-control-chart.md with the individuals chart, centre line and control limits; artifacts/22-stability-verdict.md with the rule-by-rule out-of-control analysis and the named assignable cause; artifacts/22-capability-summary.md with the capability indices against the charter target.   (Tools: SPC / Control Chart, Statistics.)

**Step-by-step**

1. Take the 20 daily measurements of median registration completion time
2. Compute the centre line and control limits from the moving ranges
3. Plot the individuals chart against the computed limits
4. Apply the out-of-control rules, including the rule of seven, run by run
5. Separate common cause from assignable cause and decide the response to each
6. Assess capability against the charter success criterion and distinguish control from specification limits
7. Write the quality verdict and the corrective actions
8. Answer the exam-style scenarios on tampering, signals and capability

**Test it**

The centre line comes to 4.053 with MR-bar 0.3286, sigma 0.2913 and limits of 3.179 and 4.927, computed from the stable period not all 20 points; sigma is MR-bar divided by 1.128; the rule of seven is checked on days 1 to 15, longest run 2; days 16 to 20 are assignable cause with a dated explanation matching the shift; and the negative Cpk leads to re-centring rather than tightening.

> **Note:** Full commands and screenshots are in labs/lab-22-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


## Topic 06 — Close the Project

Acceptance · transition · benefits realisation · lessons learned · exam strategy

**Key concepts**

- Closure requires formal stakeholder acceptance against documented criteria, not merely the end of the work.
- Transition readiness moves the deliverable to operations with the support, documentation and training that make it sustainable.
- Benefits realisation is measured after go-live against the business case — the project ends, the benefits do not.
- Lessons learned only count when they update an organisational process asset that the next project inherits.
- Knowledge transfer protects the organisation from the loss of the team that built the thing.
- Exam strategy: read the last sentence first, identify the development approach in play, and eliminate answers that bypass the process.


### Lab 23 — Project Closure, Benefits Realisation and Lessons Learned

Learning outcome: Process T10 - Manage project closure and transitions; Business Environment T6 - Support organizational change and continuous improvement; People T7 - Help ensure knowledge transfer..

Goal: Close the Contoso project against the four closure enablers. Define closure criteria first, run Control Quality against specification before seeking acceptance through Validate Scope, then validate operational readiness. Write the final report against all eight charter success criteria - including the one missed - and reconcile the final cost. Hand every benefit to a named owner with a post-closure review date.

**What you'll build**

artifacts/23-closure-checklist.md separating procurement from administrative closure; artifacts/23-final-report.md with the eight criteria and cost reconciliation; artifacts/23-lessons-learned.md; artifacts/23-benefits-realisation.md handing B1 to B4 to named owners; artifacts/23-transition-plan.md.   (Tools: Closure checklist, Benefits realisation register, Lessons learned register.)

**Step-by-step**

1. Define the closure criteria before closing anything
2. Verify scope with Control Quality before seeking acceptance
3. Obtain formal acceptance from the customer through Validate Scope
4. Validate readiness for transition to operations
5. Write the final report against all eight charter success criteria
6. Hand over the benefits to named owners with review dates beyond project end
7. Capture lessons learned that each update a named organisational process asset
8. Plan the knowledge transfer and release the team
9. Answer the exam-style scenarios on closure sequence, acceptance and benefits ownership

**Test it**

Control Quality verifies against specification first, Validate Scope obtains acceptance second; the checklist separates procurement from administrative closure; SC-2 is reported NOT MET with its consequence quantified as a SGD 42,529 annual benefit shortfall; the final cost reconciles to SGD 478,900 with contingency closing at zero exposure; and every benefit B1 to B4 has a named owner who is not the project manager.

> **Note:** Full commands and screenshots are in labs/lab-23-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


### Lab 24 — Capstone - Integrated Project Management Plan and Mock Exam

Learning outcome: All domains - People, Process and Business Environment across the full ECO 2026 task list..

Goal: Part A assembles twenty-three labs of artifacts into one integrated project management plan: a component index mapping all 25 components to the lab that produced each, the three baselines and the PMB accounted separately, and a twenty-assertion consistency audit. Part B is a 30-question mock practice exam in ECO 2026 format under a 40-minute timer, scored by domain against the published weights.

**What you'll build**

artifacts/24-project-management-plan.md with the component index and twenty-assertion audit; artifacts/24-mock-exam-answers.md with all 30 answers recorded before the key was read; artifacts/24-score-analysis.md; artifacts/24-exam-readiness-plan.md with a dated plan for every domain below 70%.   (Tools: Project management plan index, Consistency audit, Mock practice exam, Score analysis.)

**Step-by-step**

1. Build the plan index mapping all 25 components to the lab and artifact that produced each
2. Account for the three baselines and the performance measurement baseline separately
3. Run the twenty-assertion consistency audit and record every discrepancy found
4. Prepare the five-minute executive presentation outline with timings per slide
5. Sit the 30-question mock practice exam in ECO 2026 format under a 40-minute timer
6. Score the mock practice exam by domain against the 33/41/26 weights
7. Separate confident correct answers from flagged guesses and identify the weakest domain
8. Write the remediation plan naming specific labs, ECO tasks, a dated action and a re-test date
9. Complete the exam-day readiness checklist covering eligibility, pacing and answer selection

**Test it**

The plan index accounts for the three baselines plus the PMB, and the learner explains why management reserve requires a baseline change while contingency does not; the audit PV sum comes to SGD 480,000 with at least one genuine discrepancy recorded; the mock exam was taken in 40 minutes without looking at the key; and per-domain scores are compared against 33%, 41% and 26%.

> **Note:** Full commands and screenshots are in labs/lab-24-*.md. The Contoso Training Portal Upgrade is a fictional case study created for this course. Use only accounts and data you are authorised to use.

---


## Wrap-Up and Exam Readiness

You have worked one project end to end and produced every artifact the ECO expects a project manager to own. What remains is converting that into a passing exam performance.

**What you built**

- An environment scan, governance model and compliance register.
- A business case, project charter, stakeholder analysis and team charter.
- A requirements traceability matrix, prioritised backlog, WBS, critical path schedule, cost baseline with reserves, and a quantified risk register.
- A RACI, communication plan, Kanban flow metrics and an earned value analysis.
- A root cause analysis, control chart, closure pack and benefits realisation review.

**Applying for the exam**

- This course provides the 35 contact hours of project management education PMI requires.
- Confirm you also meet PMI's experience requirement for your education level.
- Submit your application at pmi.org; applications are subject to audit, so keep evidence.
- Book your exam only once your practice scores are consistently above target.

**Study plan after the course**

- Review your Lab 24 domain score analysis and rank your three weakest ECO tasks.
- Work full 180-question timed mocks — stamina is a real exam variable.
- Re-derive the EVM formulas by hand until they need no lookup.
- For every wrong answer, write why the correct answer is correct; that is the learning.

---


## Next Steps

- Complete your PMI membership and PMP application with your 35 contact hours.
- Schedule a full timed mock exam within two weeks while the material is fresh.
- Re-run Labs 12, 13 and 20 without the guide to confirm the calculations are automatic.
- Join a study group or PMI chapter to keep exposure to scenario discussion.
- Plan your PDU strategy early — the PMP requires 60 PDUs every three years to maintain.


## Glossary

- **Adaptive approach** — A development approach delivering in short iterations with evolving requirements; agile is an adaptive approach.
- **Assumption log** — The record of what is believed true without proof, with an owner and a validation date; unvalidated assumptions become risks.
- **BAC — Budget at Completion** — The total authorised cost baseline for the project work.
- **Benefits realisation** — The measurement, after delivery, of whether the business case benefits actually materialised.
- **Contingency reserve** — Budget held for identified risks (known unknowns); inside the cost baseline and controlled by the project manager.
- **CPI — Cost Performance Index** — EV divided by AC. Below 1.0 means the work cost more than planned.
- **Critical path** — The longest sequence of dependent activities, determining the shortest possible project duration; activities on it have zero float.
- **EAC — Estimate at Completion** — The forecast total cost of the project given performance to date.
- **EEF — Enterprise Environmental Factor** — A condition outside the team's control that constrains the project; you conform to EEFs.
- **EMV — Expected Monetary Value** — Probability multiplied by impact, used to compare risk responses and decision-tree branches.
- **EV — Earned Value** — The budgeted value of the work actually completed.
- **Float (slack)** — The time an activity can slip without delaying the project finish.
- **Hybrid approach** — A deliberate combination of predictive governance with adaptive delivery.
- **Kano model** — A prioritisation model classifying features as basic, performance or delighter.
- **Lead time / cycle time** — Lead time is request to delivery; cycle time is work start to delivery — flow metrics that expose bottlenecks.
- **Management reserve** — Budget held for unknown unknowns; outside the cost baseline and released only by management.
- **MoSCoW** — Prioritisation into Must have, Should have, Could have and Won't have.
- **OPA — Organisational Process Asset** — A reusable plan, process, template or lesson from prior work; you apply OPAs and then update them.
- **PERT** — Three-point estimating: (Optimistic + 4 × Most Likely + Pessimistic) ÷ 6.
- **Predictive approach** — A development approach where scope, schedule and cost are defined early and changed through formal change control.
- **Project charter** — The document issued by the sponsor that authorises the project and names the project manager's authority.
- **RACI** — A responsibility assignment matrix: Responsible, Accountable, Consulted, Informed — exactly one Accountable per work package.
- **Risk register** — The record of identified risks with probability, impact, owned responses and residual risk.
- **RTM — Requirements Traceability Matrix** — The linkage from business need through requirement to deliverable and test.
- **Salience model** — Stakeholder classification by power, urgency and legitimacy.
- **SPC — Statistical Process Control** — Control charts separating assignable causes from common-cause variation.
- **SPI — Schedule Performance Index** — EV divided by PV. Below 1.0 means work is behind schedule.
- **Tuckman model** — Team development stages: forming, storming, norming, performing, adjourning.
- **WBS — Work Breakdown Structure** — The hierarchical decomposition of total scope into deliverables and work packages.
- **WIP limit** — A cap on work in progress that forces finishing over starting.
