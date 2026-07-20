"""Topic 5 — Monitor and Control the Project."""
import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

P9 = cd.eco("Process", 9)
P7 = cd.eco("Process", 7)
B3 = cd.eco("Business Environment", 3)
B4 = cd.eco("Business Environment", 4)
B5 = cd.eco("Business Environment", 5)
B6 = cd.eco("Business Environment", 6)
P8 = cd.eco("Process", 8)
P6 = cd.eco("Process", 6)
P5 = cd.eco("Process", 5)
P4 = cd.eco("Process", 4)
PE8 = cd.eco("People", 8)
PE7 = cd.eco("People", 7)


def build(prs, n):
    # ------------------------------------------------------------- opening
    X.section(
        prs, 5, "Monitor and Control the Project",
        "Monitoring and controlling is where the plan meets reality. You measure "
        "actual performance against the baselines, decide whether the variance "
        "matters, and act — through change control, corrective action, quality "
        "control, risk response and impediment removal.",
        ["Monitor and control project work and report performance",
         "Evaluate progress with earned value management",
         "Control quality with the seven basic statistical tools",
         "Run integrated change control and the change control board",
         "Manage risks, issues and impediments to resolution",
         "Control procurements and scale agile beyond one team"],
        n)
    n += 1

    X.statement(
        prs, "The controlling mindset",
        "You cannot manage what you do not measure — and you must not measure what you will not act on.",
        [("Measure against baseline",
          "Variance only has meaning when compared to an approved scope, schedule and cost baseline."),
         ("Decide with thresholds",
          "Governance sets the variance thresholds that trigger escalation, a change request or acceptance."),
         ("Act, then update artifacts",
          "Every accepted variance ends in an updated plan, log or register so the record stays truthful.")],
        n, kicker=P9, accent=BLUE)
    n += 1

    X.cards(
        prs, "What Monitoring and Controlling Actually Involves",
        [("Track", "Collect work performance data from the work itself — hours booked, "
                   "defects raised, stories done, invoices received."),
         ("Review", "Convert raw data into work performance information by comparing it "
                    "to the baseline and asking what the gap means."),
         ("Regulate", "Take corrective or preventive action so future performance moves "
                      "back toward the approved plan."),
         ("Report", "Package information into work performance reports that a sponsor or "
                    "steering committee can act on."),
         ("Change", "Route anything that alters a baseline through integrated change "
                    "control — never adjust a baseline informally."),
         ("Improve", "Feed what you learn into process updates and OPAs so the next "
                     "phase or project starts better than this one did.")],
        n, kicker=P9, accent=TEAL)
    n += 1

    X.itto(
        prs, "Monitor and Control Project Work — ITTO",
        ["Project management plan (all components)",
         "Project documents: assumption log, basis of estimates",
         "Cost and schedule forecasts",
         "Issue log, lessons learned register, risk register",
         "Milestone list and quality reports",
         "Work performance information",
         "Agreements and EEFs/OPAs"],
        ["Expert judgement on earned value and forecasting",
         "Data analysis: alternatives, cost-benefit analysis",
         "Earned value analysis and root cause analysis",
         "Trend analysis and variance analysis",
         "Decision making: voting on options",
         "Meetings: status reviews and steering committees"],
        ["Work performance reports",
         "Change requests",
         "Project management plan updates",
         "Project document updates: cost and schedule forecasts",
         "Issue log and lessons learned register updates",
         "Risk register updates"],
        n, kicker=P9,
        purpose="Purpose: track, review and report overall progress so stakeholders "
                "understand true status and the team can forecast where the project "
                "will land if nothing changes.")
    n += 1

    X.table(
        prs, "Data to Information to Reports — the Performance Chain",
        ["Stage", "What it is", "Example", "Who consumes it"],
        [["Work performance data",
          "Raw, unanalysed observations and measurements taken during execution",
          "42 hours booked; 3 defects logged; 5 of 8 stories done",
          "Project team, delivery leads"],
         ["Work performance information",
          "Data analysed in context against the baseline to give it meaning",
          "CPI 0.92, SPI 1.04 — over budget but slightly ahead of schedule",
          "Project manager, functional managers"],
         ["Work performance reports",
          "Information packaged physically or electronically to drive decisions",
          "Status report, dashboard, milestone schedule, EVM S-curve",
          "Sponsor, steering committee, PMO"],
         ["Change requests",
          "Formal proposals to alter a baseline, document or deliverable",
          "Add two developers to recover the critical path",
          "Change control board"]],
        n, kicker=P9, accent=VIOLET, widths=[2.0, 3.4, 3.3, 2.0],
        note="Exam cue: 'raw' or 'measurements taken' = data. 'Compared to plan' = "
             "information. 'Presented to the sponsor' = report.")
    n += 1

    X.cards(
        prs, "Report on Performance — the Reporting Toolkit",
        [("Milestone schedule", "High-level visualisation of progress against planned "
                                "milestone dates — the sponsor's favourite one-pager."),
         ("Quality reports", "Charts and narrative built from collected quality metrics, "
                             "defect counts and improvement recommendations."),
         ("EVM reports", "Graphs and computed values from the earned value equations, "
                         "including the PV/EV/AC S-curve and index trends."),
         ("Variance analysis reports", "Graphs and commentary comparing actual results to "
                                       "expected results, with root causes for each gap."),
         ("Status reports", "Period snapshot of scope, schedule, cost, risk and issues, "
                            "usually with a RAG rating per dimension."),
         ("Dashboards", "Information radiators refreshed automatically so stakeholders "
                        "self-serve status instead of requesting it.")],
        n, kicker=PE8, accent=AMBER)
    n += 1

    X.cards(
        prs, "Developing Project Metrics and Reconciliation",
        [("Choose metrics that drive action", "A metric no one would act on is overhead. "
                                              "Tie each measure to a decision it informs."),
         ("Baseline and threshold", "Define the target and the tolerance band before "
                                    "measuring so variance is judged, not debated."),
         ("Leading and lagging", "Lagging metrics (CPI, defects escaped) confirm; leading "
                                 "metrics (velocity trend, blocker age) warn early."),
         ("Reconcile the sources", "Timesheets, finance ledger and the schedule tool "
                                   "disagree — reconcile them before publishing a number."),
         ("Cadence and ownership", "Every metric needs an owner, a refresh cadence and a "
                                   "documented calculation method."),
         ("Review effectiveness", "ECO 2026 asks you to continually assess whether your "
                                  "metrics and artifacts are still worth maintaining.")],
        n, kicker=P9, accent=CYAN)
    n += 1

    X.cards(
        prs, "Artifact Management Effectiveness (ECO 2026 Emphasis)",
        [("Identify and tailor artifacts", "Select only the registers, logs and plans this "
                                           "project's complexity actually justifies."),
         ("Create, review, update", "An artifact that is not maintained is worse than none "
                                    "— it misleads people who trust it."),
         ("Ensure accessibility", "Stakeholders must be able to find the current version "
                                  "without asking the project manager for it."),
         ("Single source of truth", "One authoritative location per artifact; everything "
                                    "else links to it rather than copying it."),
         ("Version and configuration", "Configuration management controls the deliverable; "
                                       "change control governs the baseline."),
         ("Assess continually", "Retire artifacts that no longer inform a decision and add "
                                "ones the team keeps recreating informally.")],
        n, kicker=P9, accent=ROSE)
    n += 1

    # ------------------------------------------------- continuous improvement
    X.compare(
        prs, "Continuous Improvement — Incremental vs Breakthrough",
        ("Small incremental improvement", "Kaizen-style, team-owned, low risk",
         ["Many small changes made continuously by the people doing the work",
          "Low cost, low risk, and reversible if the change does not help",
          "Driven by retrospectives, suggestion systems and daily problem solving",
          "Compounds over time — 1% per sprint is transformational over a year",
          "Typical vehicles: Agile retrospectives, Lean waste reduction"]),
        ("Large breakthrough improvement", "Re-engineering, sponsor-owned, high risk",
         ["A step change that redesigns a process, technology or operating model",
          "High cost, high disruption, needs executive sponsorship and funding",
          "Usually triggered by a strategic threat or a persistent capability gap",
          "Delivers a large gain at once but risks organisational rejection",
          "Typical vehicles: Six Sigma DMAIC projects, business process reengineering"]),
        n, kicker=B6, lc=TEAL, rc=VIOLET,
        footer_note="Continuous improvement is a business strategy set at the "
                    "organisational level and adopted by projects — usually implemented "
                    "by the PMO through a structured framework such as Agile, Lean or "
                    "Six Sigma.")
    n += 1

    X.process(
        prs, "The Continuous Improvement Loop on a Live Project",
        [("Observe", "Collect metrics, defect data and team feedback from the current period."),
         ("Analyse", "Use root cause analysis to find why the outcome differed from intent."),
         ("Design", "Propose a countermeasure with a clear hypothesis of the effect."),
         ("Trial", "Run the change for one iteration or reporting period only."),
         ("Adopt or drop", "Keep what measurably helped; discard what did not, and record why."),
         ("Update OPAs", "Push proven improvements into templates and process assets.")],
        n, kicker=B6, accent=CYAN,
        note="ECO Business Environment T6 asks you to utilise lessons learned, ensure "
             "improvement processes are updated, and update organisational process "
             "assets — improvement is not real until the OPA changes.")
    n += 1

    X.cards(
        prs, "Curate Knowledge as an Asset",
        [("Document explicit knowledge", "Write down what can be written down — decisions, "
                                         "configurations, runbooks — and archive it where "
                                         "others will look."),
         ("Surface tacit knowledge", "Experience and judgement live in people. Pair work, "
                                     "shadowing and communities of practice move it."),
         ("Treat knowledge as an asset", "Knowledge outlives the team. It belongs to the "
                                         "organisation, not to whoever happened to learn it."),
         ("Build psychological safety", "People only share what did not work if admitting "
                                        "failure is safe. Blameless review is the enabler."),
         ("Make it findable", "A lessons learned repository nobody can search has zero "
                              "value; tag entries by process, phase and risk category."),
         ("Capture continuously", "Record lessons as they occur, not at closure when the "
                                  "detail and the people have already gone.")],
        n, kicker=PE7, accent=BLUE)
    n += 1

    X.cards(
        prs, "Realign Team Efforts with Value During Change",
        [("Prioritise team cohesion", "When members join or depart, the team must re-form. "
                                      "Protect cohesion before chasing velocity."),
         ("Support realignment", "Revisit working agreements, roles and the Definition of "
                                 "Done whenever the team's composition changes."),
         ("Welcome new members", "Treat each joiner as a source of new knowledge and "
                                 "motivation, not simply as extra capacity."),
         ("Restate shared goals", "Re-establish shared understanding of project goals and "
                                  "agreements so nobody optimises the wrong thing."),
         ("Collaborate on value", "Ask each member explicitly how their work adds value; "
                                  "the answer often exposes hidden waste."),
         ("Navigate disruption", "Expect a dip in performance after disruption; coach "
                                 "through it rather than escalating immediately.")],
        n, kicker=cd.eco("People", 3), accent=AMBER)
    n += 1

    # ------------------------------------------------ integrated change control
    X.itto(
        prs, "Perform Integrated Change Control — ITTO",
        ["Project management plan: change management plan, "
         "configuration management plan, baselines",
         "Project documents: basis of estimates, requirements traceability matrix",
         "Risk report",
         "Work performance reports",
         "Change requests",
         "Enterprise environmental factors and OPAs"],
        ["Expert judgement and change control tools",
         "Data analysis: alternatives analysis, cost-benefit analysis",
         "Decision making: voting, autocratic decision making, "
         "multicriteria decision analysis",
         "Meetings: change control board meetings",
         "Configuration management system"],
        ["Approved change requests",
         "Project management plan updates",
         "Project document updates",
         "Change log (records every request and its disposition)",
         "Updated baselines where the change was approved"],
        n, kicker=B3,
        purpose="Purpose: review, approve or reject every change request, manage changes "
                "to deliverables and baselines, and communicate the decision. This process "
                "is performed from project start to finish.")
    n += 1

    X.cards(
        prs, "Causes of Project Changes",
        [("Inaccurate initial estimates", "Estimates made with the least information ever "
                                          "available prove wrong as detail emerges."),
         ("New regulations", "External legal, tax or safety requirements arrive mid-flight "
                             "and are non-negotiable."),
         ("Missed requirements", "Elicitation never reached a stakeholder group whose "
                                 "needs surface during review or UAT."),
         ("Specification changes", "The business changes its mind because the market, "
                                   "competitor or strategy changed."),
         ("Risk response", "An identified risk occurs and the agreed response requires a "
                           "baseline change to implement."),
         ("Technology and vendor shifts", "A supplier discontinues a component or a "
                                          "platform version reaches end of support.")],
        n, kicker=B3, accent=VIOLET)
    n += 1

    X.table(
        prs, "The Four Change Request Types — Know These Cold",
        ["Type", "Definition", "Trigger", "Example"],
        [["Corrective action",
          "Realigns the performance of the project work with the project management plan",
          "Performance has already deviated from plan",
          "Add a second tester because the defect backlog is growing"],
         ["Preventive action",
          "Ensures the future performance of project work aligns with the plan",
          "A deviation is forecast but has not yet occurred",
          "Book contractor capacity now because a resource gap is predicted"],
         ["Defect repair",
          "Modifies a nonconforming product, deliverable or component",
          "A deliverable failed inspection or test",
          "Rework a module that failed the acceptance test"],
         ["Update",
          "Modifies formally controlled project documents or a baseline",
          "Approved content changes require the record to change",
          "Revise the scope baseline after an approved scope addition"]],
        n, kicker=B3, accent=ROSE, widths=[1.7, 3.3, 2.5, 3.0],
        note="Corrective = fix the present. Preventive = protect the future. Defect "
             "repair = fix the product. Update = fix the document or baseline.")
    n += 1

    X.compare(
        prs, "Corrective vs Preventive Action",
        ("Corrective action", "Reactive — the variance already happened",
         ["Triggered by measured performance that is already off plan",
          "Aim is to bring future performance back onto the approved baseline",
          "Usually discovered through variance analysis or an EVM index below 1.0",
          "Example: CPI has dropped to 0.85, so rescope low-value work",
          "Does not by itself change the baseline — it changes how work is done"]),
        ("Preventive action", "Proactive — the variance is only forecast",
         ["Triggered by a forecast, trend or identified risk, not by actual damage",
          "Aim is to stop the deviation ever appearing in the actuals",
          "Usually discovered through trend analysis, risk review or reserve analysis",
          "Example: cross-train a second engineer before the specialist goes on leave",
          "Closely related to risk response — prevention is mitigation applied to work"]),
        n, kicker=B3, lc=AMBER, rc=TEAL,
        footer_note="Exam cue: 'has fallen behind' or 'is over budget' points to "
                    "corrective action. 'May', 'is expected to', or 'trend suggests' "
                    "points to preventive action.")
    n += 1

    X.process(
        prs, "The Change Request Flow",
        [("Identify and raise", "Anyone may raise a change; it must be written, not verbal."),
         ("Log the request", "Record it in the change log with a unique ID, requester and date."),
         ("Assess the impact", "Analyse impact on scope, schedule, cost, quality, risk and resources."),
         ("Decide", "The PM, CCB or sponsor approves, rejects or defers per the approval levels."),
         ("Communicate", "Tell the requester and affected stakeholders the decision and the reason."),
         ("Implement and update", "Execute the approved change, update baselines and all documents.")],
        n, kicker=B3, accent=BLUE,
        note="Rejected changes are still logged. The change log is the audit trail proving "
             "that governance was followed — an exam favourite.")
    n += 1

    X.cards(
        prs, "Change Control Systems and the Change Control Board",
        [("Change control system", "The forms, tracking methods, processes and approval "
                                   "levels required to authorise or reject a requested change."),
         ("Change control board (CCB)", "A formally chartered group that reviews, evaluates, "
                                        "approves, defers or rejects changes and records decisions."),
         ("Approval levels", "The change management plan defines what the PM may approve "
                             "alone and what must escalate to the CCB or the sponsor."),
         ("Configuration management system", "Controls the product itself — versions, "
                                             "specifications and physical characteristics."),
         ("Change log", "The register of every request with status, decision, decision date "
                        "and rationale; shared with stakeholders."),
         ("Emergency change procedure", "A documented fast path for urgent changes, with "
                                        "retrospective CCB ratification.")],
        n, kicker=B3, accent=CYAN)
    n += 1

    X.exam(
        prs, "Exam Traps — Integrated Change Control",
        [("A stakeholder asks you to add a small feature; there is budget available",
          "Do not agree on the spot. Assess the impact and submit a change request "
          "through integrated change control."),
         ("A change was already implemented by a team member without approval",
          "Determine the impact first, then process it through change control and update "
          "the affected documents and baselines."),
         ("The sponsor demands an urgent change during a steering meeting",
          "Analyse impact on all baselines and present options; the CCB — not the "
          "sponsor's verbal instruction — authorises the baseline change."),
         ("A change request is rejected",
          "Record the rejection and rationale in the change log and communicate it to "
          "the requester — rejected changes are still documented.")],
        n, kicker="EXAM FOCUS · CHANGE CONTROL", accent=ROSE)
    n += 1

    X.cards(
        prs, "Agile Consideration — Handling Change",
        [("Change is expected", "Adaptive approaches assume requirements will change; the "
                                "process is designed to absorb rather than resist change."),
          ("Product Owner authority", "The Product Owner holds autocratic decision-making "
                                      "power over scope — others must convince them."),
         ("Backlog is the change log", "New or updated features enter the Product Backlog; "
                                       "updated user stories join the next Sprint Backlog."),
         ("Sprint scope is protected", "Change is welcomed between iterations; the current "
                                       "sprint's committed scope stays fixed."),
         ("Scope evolves in layers", "Roadmap to release backlog to iteration backlog — "
                                     "each layer reprioritised as needs are learned."),
         ("Validate against feedback", "Check user stories and the Definition of Done "
                                       "against customer feedback and product requirements.")],
        n, kicker=B3, accent=VIOLET)
    n += 1

    # ------------------------------------------ stakeholder engagement + scope
    X.itto(
        prs, "Monitor Stakeholder Engagement — ITTO",
        ["Project management plan: resource, communications and "
         "stakeholder engagement management plans",
         "Project documents: issue log, lessons learned register",
         "Project communications",
         "Risk register and stakeholder register",
         "Work performance data",
         "Enterprise environmental factors and OPAs"],
        ["Data analysis: alternatives analysis, root cause analysis, "
         "stakeholder engagement assessment matrix",
         "Decision making: multicriteria decision analysis, voting",
         "Data representation: stakeholder engagement assessment matrix",
         "Communication skills: feedback and presentations",
         "Interpersonal and team skills: active listening, "
         "cultural awareness, leadership, networking",
         "Meetings"],
        ["Work performance information",
         "Change requests",
         "Project management plan updates",
         "Project document updates: issue log, lessons learned register, "
         "stakeholder register, risk register"],
        n, kicker=cd.eco("People", 4),
        purpose="Purpose: monitor project stakeholder relationships and tailor strategies "
                "to engage stakeholders through modification of engagement strategies "
                "and plans.")
    n += 1

    X.itto(
        prs, "Validate Scope — ITTO",
        ["Project management plan: scope management plan, "
         "requirements management plan, scope baseline",
         "Project documents: lessons learned register, "
         "quality reports, requirements documentation",
         "Requirements traceability matrix",
         "Verified deliverables (output of Control Quality)",
         "Work performance data"],
        ["Inspection: measuring, examining and validating deliverables "
         "against acceptance criteria",
         "Walkthroughs, reviews, audits and product demonstrations",
         "Decision making: voting to reach agreement on acceptance",
         "User acceptance testing (UAT)"],
        ["Accepted deliverables (signed off by the customer)",
         "Work performance information",
         "Change requests (for deliverables not accepted)",
         "Project document updates: lessons learned register, "
         "requirements documentation, traceability matrix"],
        n, kicker=cd.eco("Process", 2),
        purpose="Purpose: formalise acceptance of completed deliverables. Control Quality "
                "verifies correctness internally; Validate Scope obtains the customer's "
                "formal acceptance.")
    n += 1

    X.compare(
        prs, "Control Quality vs Validate Scope",
        ("Control Quality", "Internal — is it built right?",
         ["Performed by the project team and quality function, usually before handover",
          "Checks the deliverable against the quality requirements and specifications",
          "Uses inspection, testing, measurement and the seven basic quality tools",
          "Key output: verified deliverables plus quality control measurements",
          "Nonconformance produces a defect repair change request"]),
        ("Validate Scope", "External — is it the right thing?",
         ["Performed with the customer or sponsor, taking verified deliverables as input",
          "Checks the deliverable against the agreed acceptance criteria",
          "Uses inspection, demonstration, walkthroughs, UAT and formal sign-off",
          "Key output: accepted deliverables recorded as formal acceptance",
          "Non-acceptance produces a change request, not a silent rework"]),
        n, kicker=P7, lc=BLUE, rc=TEAL,
        footer_note="Sequence to remember: Control Quality produces verified deliverables, "
                    "which become the input to Validate Scope, which produces accepted "
                    "deliverables, which become the input to Close Project or Phase.")
    n += 1

    X.table(
        prs, "Acceptance Criteria, Definition of Ready, Definition of Done",
        ["Concept", "Scope of application", "Who owns it", "What it prevents"],
        [["Acceptance criteria",
          "Specific to one requirement, user story or deliverable",
          "Product Owner / customer, agreed with the team",
          "Arguing about 'finished' after the work is already built"],
         ["Definition of Ready (DoR)",
          "Applies to every item before it may enter an iteration",
          "The team, agreed with the Product Owner",
          "Starting work on an item too vague to estimate or complete"],
         ["Definition of Done (DoD)",
          "Applies to every increment the team produces",
          "The whole delivery team",
          "Hidden work — untested, undocumented, undeployed 'done'"],
         ["Requirements traceability matrix",
          "Links every requirement to its deliverable, test and acceptance",
          "Project manager / business analyst",
          "Requirements silently dropped between plan and delivery"]],
        n, kicker=cd.eco("Process", 2), accent=AMBER, widths=[2.2, 3.2, 2.6, 3.0],
        note="Acceptance criteria may legitimately be modified during the life cycle — "
             "but only through the change control process.")
    n += 1

    X.itto(
        prs, "Control Scope — ITTO",
        ["Project management plan: scope, requirements and change "
         "management plans; scope and performance measurement baselines",
         "Project documents: lessons learned register, "
         "requirements documentation, traceability matrix",
         "Work performance data",
         "Organizational process assets"],
        ["Data analysis: variance analysis comparing actual to baseline",
         "Data analysis: trend analysis of scope growth over time",
         "Inspection of the delivered scope against the WBS",
         "Requirements traceability review"],
        ["Work performance information (scope variance)",
         "Change requests including corrective and preventive action",
         "Project management plan updates: scope baseline, "
         "schedule baseline, cost baseline",
         "Project document updates"],
        n, kicker=cd.eco("Process", 2),
        purpose="Purpose: monitor the status of the project and product scope and manage "
                "changes to the scope baseline — this is where scope creep is caught.")
    n += 1

    X.compare(
        prs, "Scope Creep vs Gold Plating",
        ("Scope creep", "Uncontrolled expansion, usually customer-driven",
         ["Requirements added without corresponding schedule, cost or resource change",
          "Each addition feels small — the cumulative effect destroys the baseline",
          "Root causes: weak scope baseline, no change control, eager-to-please PM",
          "Control: a documented scope baseline plus enforced integrated change control",
          "Detect it with trend analysis on requirement count and story point totals"]),
        ("Gold plating", "Unrequested extras, usually team-driven",
         ["The team adds features the customer never asked for and will not pay for",
          "Consumes budget and introduces risk with zero measured business value",
          "Root causes: engineer enthusiasm, misread of what 'delighting the customer' means",
          "Control: Definition of Done tied strictly to acceptance criteria",
          "PMI's position is unambiguous — gold plating is never acceptable"]),
        n, kicker=cd.eco("Process", 2), lc=ROSE, rc=VIOLET,
        footer_note="Both are scope control failures. The response is the same: bring it "
                    "back to the baseline, and route any genuine addition through a change "
                    "request with a full impact assessment.")
    n += 1

    X.cards(
        prs, "Monitor the External Business Environment",
        [("Change cuts both ways", "External change brings opportunities to add or extend "
                                   "value, not only threats to defend against."),
         ("Survey the environment", "Track regulatory, technology, geopolitical and market "
                                    "changes on a defined cadence, not ad hoc."),
         ("Stay vigilant for threats", "A competitor launch or a regulation can invalidate "
                                       "the business case even while delivery is green."),
         ("Update the risk register", "New external factors become new risks with new "
                                      "probability, impact and threshold values."),
         ("Reprioritise scope", "Assess the impact on scope or backlog and reprioritise "
                                "so the project still delivers the intended value."),
         ("Use structured tools", "PESTLE, SWOT and horizon scanning give the scan "
                                  "discipline rather than relying on the PM's news feed.")],
        n, kicker=cd.eco("Business Environment", 8), accent=CYAN)
    n += 1

    # ------------------------------------------------------- schedule and EVM
    X.itto(
        prs, "Control Schedule — ITTO",
        ["Project management plan: schedule management plan, "
         "schedule baseline, scope baseline, "
         "performance measurement baseline",
         "Project documents: lessons learned register, "
         "project calendars, project schedule",
         "Resource calendars and schedule data",
         "Work performance data",
         "Organizational process assets"],
        ["Data analysis: earned value analysis, iteration burndown chart, "
         "performance reviews, trend analysis, variance analysis, "
         "what-if scenario analysis",
         "Critical path method",
         "Project management information system (PMIS)",
         "Resource optimisation",
         "Leads and lags",
         "Schedule compression: crashing and fast tracking"],
        ["Work performance information: SV and SPI",
         "Schedule forecasts",
         "Change requests",
         "Project management plan updates: schedule baseline, "
         "cost baseline, performance measurement baseline",
         "Project document updates"],
        n, kicker=P8,
        purpose="Purpose: monitor the status of the project to update the schedule and "
                "manage changes to the schedule baseline. Determining the current status "
                "and influencing the factors that create schedule change are the core work.")
    n += 1

    X.statement(
        prs, "Earned Value Management",
        "EVM answers three questions with one integrated set of numbers: where should we be, where are we, and what did it cost?",
        [("Planned Value (PV)",
          "The authorised budget assigned to the work scheduled to be complete by now."),
         ("Earned Value (EV)",
          "The measure of work actually performed, expressed in the budget authorised for that work."),
         ("Actual Cost (AC)",
          "The realised cost actually incurred for the work performed in the period measured.")],
        n, kicker=P6, accent=BLUE)
    n += 1

    X.table(
        prs, "EVM Variable Glossary",
        ["Symbol", "Name", "Meaning in plain language", "Units"],
        [["PV", "Planned Value", "The value of work you planned to have finished by the measurement date", "Currency"],
         ["EV", "Earned Value", "The budgeted value of the work you actually finished", "Currency"],
         ["AC", "Actual Cost", "What you actually spent to finish that work", "Currency"],
         ["BAC", "Budget at Completion", "The total approved budget for the whole project", "Currency"],
         ["CV", "Cost Variance", "How much more or less you spent than the work was worth", "Currency"],
         ["SV", "Schedule Variance", "How much work you are ahead of or behind, valued in money", "Currency"],
         ["CPI", "Cost Performance Index", "Value earned per dollar spent — efficiency of spend", "Ratio"],
         ["SPI", "Schedule Performance Index", "Rate of progress against the planned rate", "Ratio"],
         ["EAC", "Estimate at Completion", "Forecast total cost when the project finishes", "Currency"],
         ["ETC", "Estimate to Complete", "Forecast cost of the remaining work only", "Currency"],
         ["VAC", "Variance at Completion", "Forecast overrun or underrun against BAC", "Currency"]],
        n, kicker=P6, accent=VIOLET, widths=[1.0, 2.4, 5.6, 1.4])
    n += 1

    X.formula(
        prs, "EVM Formulas — Variance and Index",
        [("Cost Variance", "CV = EV - AC",
          "Negative means you have spent more than the work was worth. Positive is good."),
         ("Schedule Variance", "SV = EV - PV",
          "Negative means less work is done than planned. Reaches zero at project end."),
         ("Cost Performance Index", "CPI = EV / AC",
          "Above 1.0 is under budget; below 1.0 means you get less than a dollar per dollar."),
         ("Schedule Performance Index", "SPI = EV / PV",
          "Above 1.0 is ahead of schedule; below 1.0 means work is arriving slower than planned."),
         ("Percent Complete", "EV / BAC",
          "The proportion of total authorised budget that has been earned so far.")],
        n, kicker="KEY FORMULAS · VARIANCE & INDEX", accent=AMBER,
        note="Memory aid: every variance is EV minus something and every index is EV "
             "divided by something. If the answer is negative or below 1.0, it is bad.")
    n += 1

    X.formula(
        prs, "EVM Formulas — Forecasting",
        [("EAC — typical variance", "EAC = BAC / CPI",
          "Use when current cost performance is expected to continue for the rest of the project."),
         ("EAC — atypical variance", "EAC = AC + (BAC - EV)",
          "Use when the variance was a one-off and remaining work will run at the budgeted rate."),
         ("EAC — schedule constrained", "EAC = AC + (BAC-EV)/(CPI x SPI)",
          "Use when the remaining work must absorb both the cost and the schedule performance."),
         ("Estimate to Complete", "ETC = EAC - AC",
          "The forecast cost of the work that still remains after money already spent."),
         ("Variance at Completion", "VAC = BAC - EAC",
          "Forecast overrun (negative) or underrun (positive) measured at project completion.")],
        n, kicker="KEY FORMULAS · FORECASTING", accent=TEAL,
        note="Read the question for the phrase that selects the formula: 'rate will "
             "continue' = BAC/CPI; 'atypical / one-off' = AC + BAC - EV; 'must meet the "
             "deadline too' = the CPI x SPI form.")
    n += 1

    X.formula(
        prs, "EVM Formulas — To-Complete Performance Index",
        [("TCPI against BAC", "TCPI = (BAC-EV)/(BAC-AC)",
          "The cost efficiency the remaining work must achieve to finish within the original budget."),
         ("TCPI against EAC", "TCPI = (BAC-EV)/(EAC-AC)",
          "Use once the original budget is no longer achievable and a new EAC has been approved."),
         ("Interpretation above 1.0", "TCPI > 1.0",
          "You must perform better than you have been performing — the target is harder than the past."),
         ("Interpretation below 1.0", "TCPI < 1.0",
          "You may perform slightly worse than before and still hit the target — you have slack.")],
        n, kicker="KEY FORMULAS · TCPI", accent=ROSE,
        note="TCPI and CPI move in opposite directions. A CPI of 0.80 with plenty of work "
             "left implies a TCPI well above 1.0 — a warning that recovery is unrealistic.")
    n += 1

    X.cards(
        prs, "Interpreting the Indices — Above 1.0 vs Below 1.0",
        [("CPI above 1.0", "Cost efficient. You earned more value than you spent. "
                           "Confirm it is real progress, not under-reported costs."),
         ("CPI below 1.0", "Cost inefficient. Every dollar buys less than a dollar of "
                           "value. Investigate rate, rework and scope leakage."),
         ("SPI above 1.0", "Ahead of plan. Check whether easy work was pulled forward, "
                           "leaving the hard work still ahead."),
         ("SPI below 1.0", "Behind plan. Look at the critical path first — non-critical "
                           "lateness may not delay the project at all."),
         ("CPI low, SPI high", "You are buying speed with money — typically overtime or "
                               "extra resources. Confirm the trade was authorised."),
         ("CPI high, SPI low", "You are underspending because too little work is happening "
                               "— usually a resource or blocker problem, not thrift.")],
        n, kicker=P6, accent=CYAN)
    n += 1

    X.process(
        prs, "Worked Example — Ten Printer Drivers",
        [("The task", "Develop and install ten printer drivers, one per week, over ten weeks."),
         ("The budget", "BAC is $100,000 — exactly $10,000 per printer driver."),
         ("Status at week 5", "Four drivers are developed and installed; $47,500 has been spent."),
         ("PV = $50,000", "Five drivers were scheduled by week 5: 5 x $10,000 of planned value."),
         ("EV = $40,000", "Four drivers are genuinely complete: 4 x $10,000 of earned value."),
         ("AC = $47,500", "The actual cost incurred to date, taken straight from the ledger.")],
        n, kicker=P6, accent=BLUE,
        note="Golden rule: EV is always the budgeted value of completed work — count the "
             "deliverables finished, then multiply by their budget. Never use actual cost "
             "to compute EV.")
    n += 1

    X.formula(
        prs, "Worked Example — Running the Numbers",
        [("Cost Variance", "CV = 40,000-47,500 = -7,500",
          "Negative: $7,500 more was spent than the completed work was actually worth."),
         ("Schedule Variance", "SV = 40,000-50,000 = -10,000",
          "Negative: one full driver's worth of work — $10,000 — is behind schedule."),
         ("Cost Performance Index", "CPI = 40,000/47,500 = 0.84",
          "Only 84 cents of value is earned per dollar spent — a serious cost problem."),
         ("Schedule Performance Index", "SPI = 40,000/50,000 = 0.80",
          "Work is arriving at 80% of the planned rate — four drivers where five were due."),
         ("Estimate at Completion", "EAC = 100,000/0.84 = 118,750",
          "If this rate continues the project finishes at $118,750, not $100,000.")],
        n, kicker=P6, accent=AMBER,
        note="Follow through: ETC = 118,750 - 47,500 = $71,250 still to spend, and "
             "VAC = 100,000 - 118,750 = -$18,750, a forecast overrun of $18,750.")
    n += 1

    X.chart(
        prs, "The EVM S-Curve — PV, EV and AC Over Ten Weeks",
        "line",
        ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10"],
        [("Planned Value (PV)", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
         ("Earned Value (EV)", [9, 18, 27, 34, 40, None, None, None, None, None]),
         ("Actual Cost (AC)", [11, 22, 32, 40, 47.5, None, None, None, None, None])],
        n, kicker=P6, accent=BLUE,
        insight=["PV is the straight planned baseline — $10K of value per week for ten weeks.",
                 "EV sits below PV, so the project is behind schedule (negative SV).",
                 "AC sits above EV, so the project is over budget (negative CV).",
                 "The gap between AC and EV widens each week — the trend, not the point, is the warning.",
                 "Extrapolating AC at the current CPI gives an EAC of roughly $119K against a $100K BAC."])
    n += 1

    X.chart(
        prs, "CPI and SPI Trend — Is the Project Recovering?",
        "line",
        ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"],
        [("CPI", [0.82, 0.82, 0.84, 0.85, 0.84, 0.87, 0.90, 0.93]),
         ("SPI", [0.90, 0.88, 0.84, 0.85, 0.80, 0.83, 0.88, 0.91])],
        n, kicker=P9, accent=TEAL,
        insight=["A single index reading is a snapshot; the trend line tells you whether corrective action worked.",
                 "Both indices bottom out around week 5, the point at which corrective action was taken.",
                 "The recovery from week 6 onward suggests the added resources are earning value.",
                 "Neither index has yet reached 1.0, so the project is still both late and over budget.",
                 "Report the trend to the sponsor — 'improving but not recovered' is a defensible status."])
    n += 1

    X.exam(
        prs, "Exam Traps — Earned Value",
        [("You are given AC and percent complete and asked for EV",
          "EV = BAC x percent complete. Actual cost never enters the earned value calculation."),
         ("CPI is 0.9 and the question says the variance was atypical",
          "Use EAC = AC + (BAC - EV). The atypical wording rules out the BAC/CPI form."),
         ("SPI is 0.85 but the project manager says the deadline is safe",
          "Check the critical path. SPI aggregates all work, so non-critical lateness can leave the finish date intact."),
         ("The question asks what to do about a negative CV of significant size",
          "Perform variance and root cause analysis first, then raise a change request for corrective action.")],
        n, kicker="EXAM FOCUS · EVM", accent=ROSE)
    n += 1

    X.compare(
        prs, "Schedule Compression — Crashing vs Fast Tracking",
        ("Crashing", "Buy time with money",
         ["Shortens duration for the least incremental cost by adding resources",
          "Typical actions: approve overtime, add staff, pay a supplier to expedite",
          "Works only on activities that lie on the critical path",
          "Always increases cost and may increase risk through onboarding and rework",
          "Does not always produce a viable alternative — some work cannot be parallelised"]),
        ("Fast tracking", "Buy time with risk",
         ["Performs activities or phases in parallel that were planned in sequence",
          "Typical action: start construction before the design is fully approved",
          "Costs nothing directly but consumes contingency through rework",
          "May result in rework, increased risk and ultimately increased cost",
          "Only applies where the dependency is discretionary, not mandatory"]),
        n, kicker=P8, lc=AMBER, rc=ROSE,
        footer_note="Both techniques apply to the critical path only. Try fast tracking "
                    "first if the budget is fixed and the dependencies are discretionary; "
                    "crash first if the risk appetite is low and money is available.")
    n += 1

    X.itto(
        prs, "Control Costs — ITTO",
        ["Project management plan: cost management plan, "
         "cost baseline, performance measurement baseline",
         "Project documents: lessons learned register",
         "Project funding requirements",
         "Work performance data",
         "Organizational process assets"],
        ["Expert judgement",
         "Data analysis: earned value analysis, variance analysis, "
         "trend analysis, reserve analysis",
         "To-complete performance index (TCPI)",
         "Project management information system (PMIS)"],
        ["Work performance information: CV, CPI, EAC, VAC, TCPI",
         "Cost forecasts (EAC and ETC)",
         "Change requests",
         "Project management plan updates: cost baseline, "
         "performance measurement baseline",
         "Project document updates: assumption log, "
         "basis of estimates, cost estimates, risk register"],
        n, kicker=P6,
        purpose="Purpose: monitor the status of the project to update project costs and "
                "manage changes to the cost baseline. Any increase over authorised funding "
                "requires a change request.")
    n += 1

    X.cards(
        prs, "Reserve Analysis in Control",
        [("Contingency reserve", "Funds and time set aside for identified risks — the "
                                 "'known unknowns'. The PM controls and draws on it."),
         ("Management reserve", "Held for unidentified risk — the 'unknown unknowns'. "
                                "Only management releases it, and it sits outside the baseline."),
         ("Burn rate check", "Compare reserve consumed against risk retired. Burning 60% "
                             "of reserve at 20% complete is a red flag."),
         ("Release the surplus", "When a risk passes without occurring, release its "
                                 "contingency back — do not silently absorb it as slack."),
         ("Cost baseline vs budget", "Cost baseline = estimates plus contingency reserve. "
                                     "Project budget = cost baseline plus management reserve."),
         ("Reserve in adaptive work", "Agile teams reserve capacity rather than money — a "
                                      "percentage of each sprint held for emergent work.")],
        n, kicker=P6, accent=VIOLET)
    n += 1

    # ------------------------------------------------------------- quality
    X.itto(
        prs, "Control Quality — ITTO",
        ["Project management plan: quality management plan",
         "Project documents: lessons learned register, "
         "quality metrics, test and evaluation documents",
         "Approved change requests",
         "Deliverables",
         "Work performance data",
         "Enterprise environmental factors and OPAs"],
        ["Data gathering: checklists, check sheets, "
         "statistical sampling, questionnaires and surveys",
         "Data analysis: performance reviews, root cause analysis",
         "Inspection and testing / product evaluations",
         "Data representation: cause-and-effect diagrams, "
         "control charts, histograms, scatter diagrams, Pareto charts",
         "Meetings: approved change request review, retrospectives"],
        ["Quality control measurements",
         "Verified deliverables",
         "Work performance information",
         "Change requests (defect repair)",
         "Project management plan updates",
         "Project document updates: issue log, "
         "lessons learned register, risk register, test documents"],
        n, kicker=P7,
        purpose="Purpose: monitor and record the results of executing quality activities "
                "to assess performance and ensure the project outputs are complete, "
                "correct and meet customer expectations.")
    n += 1

    X.cards(
        prs, "What Quality Control Does",
        [("Assess project approaches", "Judge whether the way the work is being done can "
                                       "produce a conforming result at all."),
         ("Evaluate deliverables", "Inspect and test the product against its quality "
                                   "requirements before it reaches the customer."),
         ("Review processes", "Evaluate the quality of project activities and processes "
                              "through structured reviews and audits."),
         ("Detect and prevent", "Focus on both detecting defects that exist and preventing "
                                "the causes that keep producing them."),
         ("Measure, do not guess", "Quality control is quantitative — the seven basic "
                                   "tools turn opinion into evidence."),
         ("Feed improvement", "Every defect analysed is a candidate process improvement, "
                              "not simply a task to rework.")],
        n, kicker=P7, accent=TEAL)
    n += 1

    X.compare(
        prs, "Prevention vs Inspection — and the Cost of Quality",
        ("Cost of conformance", "Money spent to prevent failure",
         ["Prevention costs: training, documented process, right equipment, time to do it right",
          "Appraisal costs: testing, destructive test loss, inspection and audit effort",
          "Spent proactively during the project, inside the approved budget",
          "PMI's position: prevention is preferred over inspection — quality is planned in",
          "A dollar spent on prevention typically saves many dollars of failure cost"]),
        ("Cost of nonconformance", "Money spent because of failure",
         ["Internal failure costs: rework and scrap found before the customer sees it",
          "External failure costs: liabilities, warranty work, lost business, reputation",
          "Spent reactively, usually outside the plan and outside the contingency estimate",
          "External failure is by far the most expensive category and the hardest to reverse",
          "Rises exponentially the later in the life cycle the defect is discovered"]),
        n, kicker=P7, lc=TEAL, rc=ROSE,
        footer_note="Quality is planned in, not inspected in. Inspection keeps defects "
                    "away from the customer but does nothing to stop the process producing "
                    "them — that requires prevention and root cause analysis.")
    n += 1

    X.cards(
        prs, "Quality Audits",
        [("What it is", "A structured, independent review to determine whether project "
                        "activities comply with organisational and project policies."),
         ("When it happens", "May be scheduled at defined milestones or conducted ad hoc "
                             "when performance triggers concern."),
         ("Quality policy", "Confirms the quality management policy is understood and "
                            "genuinely applied, not merely published."),
         ("Information and methods", "Examines how quality information is collected and "
                                     "which analytical methods are used on it."),
         ("Cost of quality", "Reviews whether prevention, appraisal and failure costs are "
                             "tracked and are trending in the right direction."),
         ("Process design", "Assesses whether the quality processes themselves are fit for "
                            "the complexity and risk of this project.")],
        n, kicker=P7, accent=AMBER)
    n += 1

    X.table(
        prs, "The Seven Basic Quality Tools",
        ["Tool", "What it shows", "Use it when", "Key reading"],
        [["Check sheet",
          "Tally of occurrences by category, collected at the point of work",
          "You need to gather defect data consistently in the first place",
          "Which category is being tallied most often"],
         ["Histogram",
          "Distribution and spread of a measured variable across bins",
          "You want to see the shape, centre and spread of the data",
          "Skew, outliers and whether the process is centred on target"],
         ["Pareto chart",
          "Ranked bar chart of defect categories with a cumulative line",
          "You must decide which few problems to attack first",
          "The 80/20 rule — roughly 80% of effects from 20% of causes"],
         ["Cause-and-effect (fishbone)",
          "Candidate causes grouped into categories around one problem",
          "You need to explore why a defect keeps recurring",
          "Which branch holds the most plausible root causes"],
         ["Scatter diagram",
          "Correlation between two variables plotted against each other",
          "You suspect one factor drives a quality defect",
          "Direction and tightness of the relationship, not causation"],
         ["Control chart",
          "A process plotted over time against mean, UCL and LCL",
          "You must judge whether a process is stable and predictable",
          "Points outside limits or non-random patterns within them"],
         ["Flowchart",
          "The sequence of steps and decision points in a process",
          "You need to see where handoffs, loops and waste occur",
          "Rework loops, unnecessary approvals and unclear ownership"]],
        n, kicker=P7, accent=VIOLET, widths=[2.0, 3.2, 3.0, 2.8])
    n += 1

    X.process(
        prs, "The Control Quality Analysis Sequence",
        [("Collect", "Use check sheets to gather defect data consistently at the source."),
         ("Distribute", "Plot the data on a histogram to see spread, centre and outliers."),
         ("Prioritise", "Build a Pareto chart to find the vital few categories driving the pain."),
         ("Diagnose", "Run cause-and-effect analysis on the top categories to find root causes."),
         ("Correlate", "Use a scatter diagram to test whether a suspected factor really drives the defect."),
         ("Monitor", "Track the fixed process on a control chart to confirm the improvement holds.")],
        n, kicker=P7, accent=CYAN,
        note="This sequence turns raw complaints into a defensible improvement case. "
             "Skipping straight to a solution without the Pareto and root cause steps is "
             "the most common quality mistake — and a common exam distractor.")
    n += 1

    X.chart(
        prs, "Pareto Chart — Defect Categories on a Software Release",
        "column",
        ["Requirements gaps", "Integration errors", "UI defects",
         "Data migration", "Performance", "Documentation"],
        [("Defect count", [58, 34, 21, 12, 7, 4])],
        n, kicker=P7, accent=AMBER,
        insight=["The two leading categories account for roughly 66% of all defects raised.",
                 "The 80/20 rule says fix the vital few, not the trivial many — start left.",
                 "Requirements gaps are an upstream failure; fixing them prevents downstream rework.",
                 "The long tail on the right rarely justifies dedicated corrective action.",
                 "Rebuild the chart after the fix — the ranking should visibly change."])
    n += 1

    X.chart(
        prs, "Histogram — Defect Resolution Time Distribution",
        "column",
        ["0-2 days", "3-5 days", "6-8 days", "9-11 days", "12-14 days", "15+ days"],
        [("Number of defects", [12, 31, 24, 15, 9, 21])],
        n, kicker=P7, accent=VIOLET,
        insight=["The histogram shows shape and spread; unlike Pareto it is not ranked by size.",
                 "The peak at 3-5 days is the typical resolution time for routine defects.",
                 "The second cluster at 15+ days is a warning of a distinct second population.",
                 "That long tail is usually a different root cause — escalated or vendor-dependent items.",
                 "Investigate the tail separately; averaging the two populations hides both problems."])
    n += 1

    X.chart(
        prs, "Control Chart — Is the Process In Control?",
        "line",
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        [("Measured value", [50, 53, 48, 51, 49, 52, 54, 55, 56, 57, 58, 66]),
         ("Mean", [52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52]),
         ("Upper control limit", [62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62]),
         ("Lower control limit", [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42])],
        n, kicker=P7, accent=BLUE,
        insight=["Control limits are set by the process itself (usually plus or minus three sigma).",
                 "Specification limits come from the customer — a process can be in control and still fail spec.",
                 "Point 12 breaches the UCL: an assignable cause that must be investigated.",
                 "Points 5 to 11 rise for seven consecutive readings — the rule of seven flags a trend.",
                 "A process is out of control if a point breaches a limit OR shows a non-random pattern."])
    n += 1

    X.compare(
        prs, "Common Cause vs Assignable (Special) Cause",
        ("Common cause variation", "The noise the process always has",
         ["Natural, random variation inherent in the way the process is designed",
          "Produces points that fall randomly within the upper and lower control limits",
          "Present all the time — it is the process behaving exactly as built",
          "Reducing it requires redesigning the process, which is a management decision",
          "Reacting to individual common-cause points is 'tampering' and increases variation"]),
        ("Assignable cause variation", "A signal that something changed",
         ["A specific, identifiable event that is not part of normal process behaviour",
          "Produces a point outside the control limits or a non-random pattern within them",
          "Examples: a new supplier batch, an untrained operator, a changed tool setting",
          "Must be investigated and eliminated — this is where corrective action belongs",
          "The rule of seven catches it even when every point is still inside the limits"]),
        n, kicker=P7, lc=TEAL, rc=ROSE,
        footer_note="Exam cue: 'a point outside the control limits', 'seven consecutive "
                    "points rising', or 'a sudden shift' all mean assignable cause — "
                    "investigate. Random scatter within limits means leave it alone.")
    n += 1

    X.chart(
        prs, "Scatter Diagram — Correlation Between Two Variables",
        "line",
        ["10", "20", "30", "40", "50", "60", "70", "80"],
        [("Defects found", [4, 6, 9, 11, 15, 18, 22, 27]),
         ("Overtime hours worked", [5, 8, 11, 16, 19, 24, 29, 35])],
        n, kicker=P7, accent=CYAN,
        insight=["A scatter diagram shows the relationship between two variables on two axes.",
                 "Here defect count rises steadily with overtime hours — a positive correlation.",
                 "Tight clustering along a line implies a strong relationship worth acting on.",
                 "Correlation is not causation — confirm with root cause analysis before acting.",
                 "Use it to test a hypothesis produced by a fishbone diagram, not to generate one."])
    n += 1

    X.cards(
        prs, "Statistical Sampling and Inspection",
        [("Why sample", "Testing every unit is often impossible or destructive; a valid "
                        "sample infers population quality at a fraction of the cost."),
         ("Sample size and frequency", "Both are determined during Plan Quality Management "
                                       "and documented in the quality management plan."),
         ("Attribute sampling", "The result is binary — the unit conforms or it does not. "
                                "Used for pass/fail inspection."),
         ("Variable sampling", "The result is measured on a continuous scale, which is "
                               "what makes control charts possible."),
         ("Tolerance vs control limit", "Tolerance is the customer's acceptable range; "
                                        "control limits describe the process's own behaviour."),
         ("Inspection outcome", "Inspection produces verified deliverables and, where the "
                                "unit fails, a defect repair change request.")],
        n, kicker=P7, accent=AMBER)
    n += 1

    # -------------------------------------------- resources and communications
    X.itto(
        prs, "Control Resources — ITTO",
        ["Project management plan: resource management plan",
         "Project documents: issue log, lessons learned register, "
         "physical resource assignments, project schedule, "
         "resource breakdown structure, resource requirements, risk register",
         "Work performance data",
         "Agreements",
         "Organizational process assets"],
        ["Data analysis: alternatives analysis, cost-benefit analysis, "
         "performance reviews, trend analysis",
         "Problem solving",
         "Interpersonal and team skills: negotiation, influencing",
         "Project management information system (PMIS)"],
        ["Work performance information",
         "Change requests",
         "Project management plan updates: resource management plan, "
         "schedule baseline, cost baseline",
         "Project document updates: assumption log, issue log, "
         "lessons learned register, resource breakdown structure, risk register"],
        n, kicker=P4,
        purpose="Purpose: ensure the physical resources assigned to the project are "
                "available as planned, and monitor planned versus actual utilisation, "
                "taking corrective action where they diverge.")
    n += 1

    X.itto(
        prs, "Monitor Communications — ITTO",
        ["Project management plan: resource, communications and "
         "stakeholder engagement management plans",
         "Project documents: issue log, lessons learned register, "
         "project communications",
         "Work performance data",
         "Enterprise environmental factors and OPAs"],
        ["Expert judgement on communication effectiveness",
         "Project management information system (PMIS)",
         "Data representation: stakeholder engagement assessment matrix",
         "Interpersonal and team skills: observation and conversation",
         "Meetings including retrospectives and status reviews"],
        ["Work performance information",
         "Change requests",
         "Project management plan updates: communications management plan, "
         "stakeholder engagement plan",
         "Project document updates: issue log, "
         "lessons learned register, stakeholder register"],
        n, kicker=PE8,
        purpose="Purpose: ensure the information needs of the project and its stakeholders "
                "are met — the right information, to the right people, in the right format, "
                "at the right time.")
    n += 1

    # ------------------------------------------------------ risk and issues
    X.itto(
        prs, "Monitor Risks — ITTO",
        ["Project management plan: risk management plan",
         "Project documents: issue log, lessons learned register, "
         "risk register, risk report",
         "Work performance data",
         "Work performance reports"],
        ["Data analysis: technical performance analysis, reserve analysis",
         "Audits: risk audits examining risk process effectiveness",
         "Meetings: risk reviews as a standing agenda item",
         "Risk reassessment and reprioritisation"],
        ["Work performance information",
         "Change requests including corrective and preventive action",
         "Project management plan updates",
         "Project document updates: assumption log, issue log, "
         "lessons learned register, risk register, risk report",
         "Organizational process assets updates"],
        n, kicker=B5,
        purpose="Purpose: monitor implementation of agreed risk responses, track identified "
                "risks, identify and analyse new risks, and evaluate risk process "
                "effectiveness throughout the project.")
    n += 1

    X.cards(
        prs, "Monitor Risks — What You Are Actually Doing",
        [("Enable decisions", "Give decision-makers current information on overall risk "
                              "exposure and on the individual risks that matter."),
         ("Track status continuously", "Monitor each risk's status, probability and impact "
                                       "— all three change as the project moves."),
         ("Identify new risks", "New risks emerge from every change, every phase gate and "
                                "every shift in the external environment."),
         ("Reassess current risks", "Re-score existing risks; yesterday's low probability "
                                    "risk may now be nearly certain."),
         ("Close outdated risks", "Retire risks whose window has passed and release their "
                                  "contingency reserve back to the project."),
         ("Improve the process", "Risk audits ask whether the risk process itself is "
                                 "working, not just whether individual risks are managed.")],
        n, kicker=B5, accent=VIOLET)
    n += 1

    X.compare(
        prs, "When a Risk Becomes an Issue",
        ("Risk", "A future uncertain event",
         ["Has not happened yet; described with a probability and an impact",
          "Lives in the risk register with an owner and an agreed response strategy",
          "Managed proactively — avoid, transfer, mitigate, accept, escalate",
          "Funded from the contingency reserve if it is an identified risk",
          "Language cue: 'may', 'could', 'if this occurs'"]),
        ("Issue", "A present certain condition",
         ["Has already happened and is affecting the project right now",
          "Lives in the issue log with an owner, an action and a target resolution date",
          "Managed reactively — resolve, escalate, or accept a workaround",
          "Consumes real budget and schedule, not contingency probability",
          "Language cue: 'has occurred', 'is blocking', 'the team cannot proceed'"]),
        n, kicker=B4, lc=TEAL, rc=ROSE,
        footer_note="ECO Business Environment T4 explicitly requires you to recognise when "
                    "a risk becomes an issue. The moment it occurs, move it from the risk "
                    "register to the issue log — the response strategy becomes an action plan.")
    n += 1

    X.process(
        prs, "Issue and Impediment Resolution",
        [("Capture", "Log the issue with a clear statement of impact, owner and raise date."),
         ("Evaluate impact", "Quantify the effect on schedule, cost, quality and the team's flow."),
         ("Prioritise", "Rank against other impediments; highlight the ones blocking the critical path."),
         ("Intervene", "Apply an intervention strategy within your authority to remove or minimise it."),
         ("Escalate if needed", "Use the governance escalation path when the block is outside your control."),
         ("Reassess", "Continually review open items to confirm blockers are actually being addressed.")],
        n, kicker=B4, accent=AMBER,
        note="An impediment that stays open past its target date is itself a risk. Ageing "
             "reports on the issue log are one of the most useful leading indicators a "
             "project manager has.")
    n += 1

    X.matrix2x2(
        prs, "Prioritising Impediments — Impact vs Ability to Resolve",
        "Ability to resolve within the team",
        "Impact on delivery",
        [("Escalate immediately",
          "High impact, outside your authority. Use the governance escalation path with a "
          "clear ask, a deadline and the consequence of inaction.", ROSE),
         ("Remove now",
          "High impact and within your control. Swarm the team on it today; this is the "
          "highest-value use of the project manager's time.", TEAL),
         ("Monitor and log",
          "Low impact, outside your control. Keep it visible on the issue log and watch "
          "for it growing rather than spending effort now.", AMBER),
         ("Delegate and track",
          "Low impact and resolvable locally. Assign an owner and a due date; do not "
          "consume leadership attention on it.", BLUE)],
        n, kicker=B4, accent=VIOLET,
        note="Impediment removal is the project manager's and scrum master's signature "
             "servant-leadership act. Speed matters more than elegance.")
    n += 1

    X.cards(
        prs, "Sustainability and Security Risk Monitoring (ECO 2026)",
        [("IT security risk", "The ECO explicitly names poor IT security as a risk register "
                              "entry — monitor vulnerabilities, access and vendor posture."),
         ("Security response execution", "Executing the risk management plan includes "
                                         "delivering security risk responses, not merely logging them."),
         ("Sustainability risk", "Environmental, energy and lifecycle impacts of the "
                                 "deliverable are now monitored risks with real thresholds."),
         ("Regulatory drift", "Compliance obligations change mid-project; a control that "
                              "was adequate at planning may not be at delivery."),
         ("Compliance measurement", "Measure the extent to which the project is in "
                                    "compliance rather than assuming it is."),
         ("Communicate risk status", "The ECO requires you to communicate the status of a "
                                     "risk's impact — silence is not a risk response.")],
        n, kicker=B5, accent=CYAN)
    n += 1

    X.cards(
        prs, "Manage Compliance During Control",
        [("Test and validate", "Validate deliverables against compliance requirements "
                               "continuously and at every phase end, not only at closure."),
         ("Identify approvers", "Know which authorised stakeholders can sign a compliance "
                                "acceptance before you need the signature."),
         ("Remediate early", "Unresolved compliance issues cause timeline damage, cost "
                             "overruns and increased risk exposure."),
         ("Early warning", "A compliance review programme gives early warning of potential "
                           "threats before an external auditor finds them."),
         ("Capture variances", "Structured checks let you capture variances and take "
                               "action while remediation is still cheap."),
         ("Analyse consequences", "Document what noncompliance would actually cost — it is "
                                  "what unlocks the funding to fix it.")],
        n, kicker=cd.eco("Business Environment", 2), accent=BLUE)
    n += 1

    X.cards(
        prs, "Agile Consideration — Risk and Team in Control",
        [("Risks as user stories", "Risks are raised as user stories carrying probability "
                                   "and impact ratings so they compete for capacity."),
         ("Prioritised in the backlog", "Risk stories are prioritised alongside value "
                                        "features — risk work becomes visible, funded work."),
         ("Retrospective as risk review", "Each retrospective doubles as a risk "
                                          "reassessment for the coming iteration."),
         ("T-shaped teams", "Agile teams prefer dedicated, T-shaped members — broad "
                            "capability with one deep specialism."),
         ("Skills over roles", "Specific job titles matter less than having every skill "
                               "needed to complete the feature inside the team."),
         ("Osmotic communication", "Co-located teams learn quickly by osmosis; distributed "
                                   "teams must engineer that flow deliberately.")],
        n, kicker=B5, accent=TEAL)
    n += 1

    # ------------------------------------------------------------ procurement
    X.itto(
        prs, "Control Procurements — ITTO",
        ["Project management plan: requirements, risk, procurement "
         "and change management plans; schedule baseline",
         "Project documents: assumption log, lessons learned register, "
         "milestone list, quality reports, requirements documentation, "
         "risk register, stakeholder register",
         "Agreements and procurement documentation",
         "Approved change requests",
         "Work performance data"],
        ["Expert judgement in contract administration and claims",
         "Claims administration",
         "Data analysis: performance reviews, earned value analysis, "
         "trend analysis",
         "Inspection and audits",
         "Procurement performance reviews"],
        ["Closed procurements",
         "Work performance information",
         "Procurement documentation updates",
         "Change requests",
         "Project management plan updates: risk management plan, "
         "procurement management plan, schedule and cost baselines",
         "Project document updates and OPA updates"],
        n, kicker=P5,
        purpose="Purpose: manage procurement relationships, monitor contract performance, "
                "make changes and corrections as appropriate, and close out contracts "
                "correctly.")
    n += 1

    X.table(
        prs, "Types of Contract Change",
        ["Change type", "Definition", "Typical trigger", "Handling"],
        [["Administrative change",
          "Non-substantive change, usually to the contract administration method",
          "New invoicing address, changed contract officer",
          "Documented by the contracts function; no renegotiation"],
         ["Contract modification",
          "Substantive change to the contract requirements or product requirements",
          "Approved scope change affecting the vendor's deliverable",
          "Formal, signed by both parties, priced before work starts"],
         ["Supplemental agreement",
          "An additional agreement related to the contract but negotiated separately",
          "Extra work outside the original statement of work",
          "Negotiated as a separate instrument with its own terms"],
         ["Constructive change",
          "A change made by the buyer through action or inaction, not by formal order",
          "Buyer directs extra work verbally, or delays an approval",
          "Frequently disputed; the source of most claims"],
         ["Termination",
          "Ending the contract before completion, for cause or for convenience",
          "Vendor default, or the buyer no longer needs the deliverable",
          "Follows the termination clause; settlement of costs incurred"]],
        n, kicker=P5, accent=VIOLET, widths=[1.9, 3.2, 2.9, 3.0],
        note="Constructive change is the exam's favourite: the buyer never issued a change "
             "order, but their behaviour effectively directed extra work — and they may "
             "still be liable for it.")
    n += 1

    X.cards(
        prs, "Managing Disputes and Contract Problems",
        [("Warranty", "A promise, explicit or implied, that goods or services will meet a "
                      "standard covering reliability, fitness for use and safety."),
         ("Waiver", "A binding provision where one party forfeits a claim without the "
                    "other becoming liable — waivers can be granted inadvertently."),
         ("Breach of contract", "Failure to meet some or all obligations of a contract, "
                                "which may entitle the other party to remedy or damages."),
         ("Work with the vendor first", "Most contract problems are solved commercially "
                                        "with the supplier before they become legal ones."),
         ("Work with your organisation", "Engage procurement, finance and functional "
                                         "departments; act within your documented threshold."),
         ("Get expert help early", "Legal problems serious enough to cause project issues "
                                   "need specialist help before positions harden.")],
        n, kicker=P5, accent=ROSE)
    n += 1

    X.process(
        prs, "Claims Administration and Dispute Escalation",
        [("Claim raised", "A contested change or potential constructive change is formally asserted."),
         ("Document the facts", "Assemble the evidence: correspondence, records, inspection results."),
         ("Negotiate", "Settlement through direct negotiation is always the preferred route."),
         ("Mediation", "A neutral third party helps the parties reach their own agreement."),
         ("Arbitration", "The ADR method named in the contract; a neutral issues a binding decision."),
         ("Litigation", "The last resort — slow, public, expensive and relationship-ending.")],
        n, kicker=P5, accent=AMBER,
        note="Claims usually arise from a lack of agreement on compensation for a change, "
             "or a lack of agreement that a change occurred at all. If unresolved, handle "
             "through the alternative dispute resolution method established in the contract.")
    n += 1

    X.cards(
        prs, "The Contract Change Control System",
        [("Purpose", "A system specifically dedicated to controlling changes to contracts "
                     "and the resulting product requirements."),
         ("Relationship to ICC", "May be a component of integrated change control or a "
                                 "separate organisational system, depending on the OPAs."),
         ("Documentation", "Specifies exactly how a contract change is requested, priced, "
                           "authorised and recorded."),
         ("Dispute resolution", "Includes the dispute-resolution process and the ADR method "
                                "that applies when the parties disagree."),
         ("Approval levels", "Defines who may sign a contract change at each value band — "
                             "rarely the project manager alone."),
         ("Audit trail", "Every change instruction must be traceable to an authorised "
                         "signature; verbal direction creates constructive change risk.")],
        n, kicker=P5, accent=CYAN)
    n += 1

    # -------------------------------------------------------- scaling agile
    X.statement(
        prs, "Scaling agile",
        "One Scrum team is a delivery method. Many teams on one product is an organisational design problem.",
        [("Coordination overhead",
          "Dependencies between teams grow faster than team count — coordination becomes the constraint."),
         ("Shared definition of done",
          "Multiple teams must agree what 'done' and 'integrated' mean or the increment never assembles."),
         ("Value stream focus",
          "Scaling frameworks organise around products and value streams rather than functional silos.")],
        n, kicker=cd.eco("Process", 1), accent=VIOLET)
    n += 1

    X.cards(
        prs, "eXtreme Programming (XP)",
        [("Five core values", "Communication, Simplicity, Feedback, Respect and Courage — "
                              "the behavioural foundation the practices rest on."),
         ("Four core activities", "Coding, Testing, Listening and Designing — the only "
                                  "activities XP considers essential to producing software."),
         ("Whole team", "Everyone needed to do the work sits within the team, including "
                        "the on-site customer representative."),
         ("Planning game", "Planning Poker on user stories: the team estimates, high and "
                           "low estimators explain, and the team re-estimates to consensus."),
         ("Pair programming", "Two developers on one workstation — continuous review that "
                              "spreads knowledge and catches defects at the keystroke."),
         ("Test-driven development", "Write the failing test first, then the code that "
                                     "passes it, then refactor — quality is built in.")],
        n, kicker=cd.eco("Process", 1), accent=BLUE)
    n += 1

    X.cards(
        prs, "Feature Driven Development (FDD)",
        [("Feature teams", "Small teams dedicated to delivering one client-valued feature "
                           "at a time, rather than one technical layer."),
         ("Develop by feature", "Work is decomposed into features small enough to be "
                                "completed in about two weeks and demonstrated."),
         ("Individual class ownership", "One named owner is responsible for each group of "
                                        "code, giving clear accountability for quality."),
         ("Domain object modelling", "Sequence and context diagrams describe how the code "
                                     "interacts before it is written."),
         ("Inspections", "Formal inspection of both the code and the result — FDD is more "
                         "document-friendly than most agile methods."),
         ("Regular builds and CM", "Configuration management maintains versions of every "
                                   "change; regular builds merge to the main branch.")],
        n, kicker=cd.eco("Process", 1), accent=TEAL)
    n += 1

    X.cards(
        prs, "Crystal",
        [("Technologies change techniques", "There is no one method — the right practices "
                                            "depend on the technology being used."),
         ("Cultures change norms", "What works in one organisation's culture will not "
                                   "transplant unchanged into another."),
         ("Distances change communication", "Co-location changes what communication "
                                            "mechanisms are necessary and sufficient."),
         ("Sized by team and criticality", "Crystal grades a project by team size and "
                                           "criticality — Clear, Yellow, Orange, Red."),
         ("More governance when riskier", "Larger and riskier projects need more "
                                          "governance; small teams need very little."),
         ("Agile favours the small", "Because agile favours small teams, Crystal Clear and "
                                     "Crystal Yellow are the commonly used variants.")],
        n, kicker=cd.eco("Process", 1), accent=VIOLET)
    n += 1

    X.cards(
        prs, "Crystal Core Properties and Techniques",
        [("Frequent delivery", "Ship working software to real users regularly — the single "
                               "most important property in Crystal."),
         ("Reflective improvement", "Reflection workshops — Crystal's name for the "
                                    "retrospective — adjust the method as you go."),
         ("Close communication", "Osmotic communication in a shared space, plus easy access "
                                 "to expert users when questions arise."),
         ("Personal safety and focus", "People must be able to speak up without fear, and "
                                       "have protected time to concentrate."),
         ("Methodology shaping", "Deliberately tailor the method to this project and team "
                                 "rather than adopting a framework unmodified."),
         ("Blitz planning and Wideband Delphi", "Group planning and group estimation where "
                                                "outliers explain before re-estimating.")],
        n, kicker=cd.eco("Process", 1), accent=AMBER)
    n += 1

    X.cards(
        prs, "Dynamic Systems Development Method (DSDM)",
        [("The inverted triangle", "DSDM is where the alternate constraints triangle comes "
                                   "from: time and cost are fixed, scope is variable."),
         ("Focus on the business need", "Every decision is tested against whether it serves "
                                        "a real, agreed business need."),
         ("Build on firm foundations", "Build incrementally, but only after enough "
                                       "foundation work to know the architecture is sound."),
         ("Never compromise quality", "Quality is fixed alongside time and cost — scope is "
                                      "the only variable DSDM allows you to flex."),
         ("Timeboxing", "Short fixed iterations, plus timeboxed spikes for research or "
                        "problem solving that would otherwise expand indefinitely."),
         ("MoSCoW prioritisation", "Must have, Should have, Could have, Won't have this "
                                   "time — the mechanism that makes scope flexible.")],
        n, kicker=cd.eco("Process", 1), accent=ROSE)
    n += 1

    X.table(
        prs, "Scaling Frameworks Compared",
        ["Framework", "Core idea", "Coordination mechanism", "Best fit"],
        [["Scrum of Scrums",
          "A representative from each team attends a shared stand-up",
          "Program and ultimately portfolio Scrums report progress and cross-team blockers",
          "A handful of teams on one product, minimal added structure"],
         ["LeSS (Large Scale Scrum)",
          "Large Scale Scrum is Scrum — treat many teams as one team",
          "One Product Owner, one backlog, one sprint; transparency via Kanban and radiators",
          "Several teams that can genuinely share a single product backlog"],
         ["SAFe",
          "Organise around value streams — the products and services themselves",
          "Agile Release Trains: teams of teams pulling in anyone needed to deliver value",
          "Large enterprises needing portfolio-level funding and governance alignment"],
         ["Disciplined Agile",
          "A decision framework rather than a prescribed method",
          "Guided choices on lifecycle and practices per team context",
          "Organisations with genuinely heterogeneous delivery contexts"]],
        n, kicker=cd.eco("Process", 1), accent=CYAN, widths=[2.0, 3.0, 3.5, 2.5])
    n += 1

    X.compare(
        prs, "LeSS vs SAFe",
        ("LeSS — Large Scale Scrum", "Descale the organisation",
         ["Applies Scrum ways of working to programs and portfolios only when necessary",
          "Empirical process control: update and improve the process as you go",
          "Manages through transparency — Kanban boards and information radiators",
          "'More with LeSS': more ownership with fewer roles, more learning with less defined process",
          "Keeps one Product Owner and one product backlog across all teams"]),
        ("SAFe — Scaled Agile Framework", "Add structure to the enterprise",
         ["Organises project teams around value streams — products or services, not functions",
          "Agile Release Trains are teams of teams, adding anyone needed to deliver the value",
          "Each value stream carries OKRs: written objectives and measurable key results",
          "Uses human-centred design and Lean portfolio management above the team level",
          "Prescriptive: defined roles, cadences and planning events at every level"]),
        n, kicker=cd.eco("Process", 1), lc=TEAL, rc=VIOLET,
        footer_note="LeSS reduces organisational structure to let Scrum work at scale; SAFe "
                    "adds structure to connect agile teams to enterprise funding and "
                    "governance. Neither is 'more agile' — they solve different constraints.")
    n += 1

    X.chart(
        prs, "Iteration Burndown — Reading Adaptive Progress",
        "line",
        ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10"],
        [("Ideal remaining", [40, 36, 32, 28, 24, 20, 16, 12, 8, 0]),
         ("Actual remaining", [40, 39, 37, 36, 30, 29, 22, 15, 9, 3])],
        n, kicker=P9, accent=BLUE,
        insight=["A burndown is the adaptive equivalent of an EVM S-curve — remaining work over time.",
                 "The flat stretch on days 2-4 signals a blocker, not slow work.",
                 "The steep drop from day 6 is typical of stories finishing in a batch at the end.",
                 "Ending above zero means committed scope was not completed — carry it to the next sprint.",
                 "Trend across several sprints matters more than any one sprint's line."])
    n += 1

    X.exam(
        prs, "Exam Traps — Monitoring, Quality and Issues",
        [("A team member reports a problem that is already affecting the schedule",
          "It is an issue, not a risk. Record it in the issue log, assign an owner, and "
          "determine the impact before escalating."),
         ("Seven consecutive control chart points fall above the mean, all inside the limits",
          "The rule of seven signals an assignable cause. Investigate — do not wait for a "
          "point to breach the control limit."),
         ("A deliverable passed the team's testing but the customer refuses to sign",
          "Control Quality verified it, but Validate Scope has failed. Raise a change "
          "request and review the acceptance criteria with the customer."),
         ("The vendor performed extra work because you delayed an approval",
          "That is a constructive change. Assess the claim, document the facts, and "
          "negotiate before invoking the contract's ADR clause.")],
        n, kicker="EXAM FOCUS · CONTROL", accent=ROSE)
    n += 1

    X.recap(
        prs, "Topic 5 Recap — Monitor and Control the Project",
        [("Data becomes decisions", "Work performance data becomes information becomes "
                                    "reports becomes change requests — that chain is the whole domain."),
         ("EVM is one integrated system", "PV, EV and AC generate every variance, index and "
                                          "forecast. Learn EV first; everything else follows."),
         ("Indices below 1.0 are bad", "CPI and SPI below 1.0 mean over budget and behind "
                                       "schedule. Trends matter more than single readings."),
         ("Choose the right EAC", "'Rate continues' uses BAC/CPI. 'Atypical' uses AC+BAC-EV. "
                                  "'Must hit the date' uses the CPI x SPI form."),
         ("Every change is a request", "Nothing changes a baseline without integrated change "
                                       "control — and rejected changes are still logged."),
         ("Corrective vs preventive", "Corrective fixes a variance that happened. Preventive "
                                      "stops one that is only forecast."),
         ("Quality is planned in", "Prevention beats inspection. The seven basic tools turn "
                                   "defect opinion into a defensible improvement case."),
         ("Control chart signals", "A breach of the limits or seven consecutive points one "
                                   "side means assignable cause — investigate it."),
         ("Risk becomes issue", "The moment a risk occurs, move it to the issue log and "
                                "switch from response strategy to resolution action."),
         ("Scaling is organisational", "LeSS descales structure; SAFe adds it. Both exist to "
                                       "manage dependencies, not to make teams more agile.")],
        n, kicker="RECAP · TOPIC 5", accent=CYAN)
    n += 1

    return n
