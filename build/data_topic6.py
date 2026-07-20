"""Topic 6 — Close the Project."""
import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

P10 = cd.eco("Process", 10)
P3 = cd.eco("Process", 3)
P5 = cd.eco("Process", 5)
B6 = cd.eco("Business Environment", 6)
PE7 = cd.eco("People", 7)
PE4 = cd.eco("People", 4)

E = cd.ECO_EXAM


def build(prs, n):
    X.section(
        prs, 6, "Close the Project",
        "Closure is a process, not an event. You obtain formal acceptance, transition "
        "the deliverable into operations, settle every contract and account, harvest "
        "the knowledge, and confirm the benefits the business case promised — then "
        "you turn to the exam itself.",
        ["Close Project or Phase and the closure criteria",
         "Acceptance, transition and readiness for handover",
         "Contracts, procurement and financial closure",
         "Lessons learned, retrospectives and knowledge transfer",
         "Benefits realisation and confirming delivered value",
         "PMP exam structure, question types and study strategy"],
        n)
    n += 1

    X.statement(
        prs, "Why closure matters",
        "A project that is not formally closed never stops consuming the organisation's money, attention and risk.",
        [("Acceptance ends ambiguity",
          "Formal sign-off is the point at which 'nearly done' becomes contractually and legally done."),
         ("Transition protects benefits",
          "Value is realised in operations, not in delivery — a poor handover destroys the business case."),
         ("Knowledge outlives the team",
          "Lessons learned move into the repository so the next project starts from your experience.")],
        n, kicker=P10, accent=BLUE)
    n += 1

    X.cards(
        prs, "Three Threads of Closing",
        [("Project or phase closure", "Complete every activity, obtain acceptance, settle "
                                      "contracts and accounts, release resources and archive."),
         ("Benefits realisation", "Confirm the value the business case promised is being "
                                  "measured and delivered, and hand ownership of that measurement over."),
         ("Knowledge transfer", "Move explicit and tacit knowledge from the team into the "
                                "organisation before the team disbands."),
         ("Phase gate closure", "Closing a phase uses the same process — acceptance, "
                                "lessons learned, archive — before the next phase is authorised."),
         ("Administrative closure", "Financial accounts closed, purchase orders settled, "
                                    "systems access revoked, facilities returned."),
         ("Celebration and recognition", "Recognising the team's contribution is a genuine "
                                         "closure activity, not a nicety — it shapes future engagement.")],
        n, kicker=P10, accent=TEAL)
    n += 1

    X.itto(
        prs, "Close Project or Phase — ITTO",
        ["Project charter",
         "Project management plan (all components)",
         "Project documents: assumption log, basis of estimates, "
         "change log, issue log, lessons learned register, "
         "milestone list, project communications, quality control "
         "measurements, quality reports, requirements documentation, "
         "risk register, risk report",
         "Accepted deliverables",
         "Business documents: business case, benefits management plan",
         "Agreements and procurement documentation",
         "Organizational process assets"],
        ["Expert judgement in management control, audit, "
         "legal and procurement closure",
         "Data analysis: document analysis, regression analysis, "
         "trend analysis, variance analysis",
         "Meetings: closeout reporting, lessons learned sessions, "
         "retrospectives, celebration"],
        ["Project documents updates (lessons learned register finalised)",
         "Final product, service or result transition",
         "Final report",
         "Organizational process assets updates: project files, "
         "project or phase closure documents, historical information, "
         "lessons learned repository"],
        n, kicker=P10,
        purpose="Purpose: finalise all activities for the project, phase or contract. "
                "This is the only process whose output is the formal, archived record "
                "that the project ever happened.")
    n += 1

    X.compare(
        prs, "Project Closure vs Phase Closure",
        ("Project closure", "The whole endeavour ends",
         ["Performed once, when all phases are complete or the project is terminated",
          "Releases all resources, closes all contracts and all financial accounts",
          "Transitions the final product, service or result to operations or the customer",
          "Produces the final report summarising performance against every baseline",
          "Archives the complete project record into the organisational process assets"]),
        ("Phase closure", "A gate between stages",
         ["Performed at the end of each phase in a predictive or hybrid life cycle",
          "Confirms phase deliverables are accepted before the next phase is authorised",
          "Resources may be released, retained or reassigned depending on the next phase",
          "Produces a phase-end report and a go / no-go / hold recommendation",
          "Captures lessons learned while they are fresh, not at the very end"]),
        n, kicker=P10, lc=BLUE, rc=VIOLET,
        footer_note="Both use the same process. A phase gate is the cheapest place to kill "
                    "a project that has lost its business case — which is precisely why "
                    "governance defines phase-end criteria in advance.")
    n += 1

    X.cards(
        prs, "Why Projects or Phases Close",
        [("Deliverables accepted", "Stakeholders accept deliverables against acceptance "
                                   "criteria established in the project management plan."),
         ("Criteria may evolve", "Acceptance criteria can legitimately be modified during "
                                 "the life cycle — through change control, never informally."),
         ("Traceability confirms completion", "The requirements traceability matrix proves "
                                              "every requirement was completed and approved."),
         ("Iteration assessment", "At the end of an iteration, team and stakeholders assess "
                                  "the product against their mutually agreed Definition of Done."),
         ("Phase gate reached", "The phase's exit criteria are met and governance authorises "
                                "moving to the next phase."),
         ("Termination", "The business case has failed, funding is withdrawn, or the need "
                         "has disappeared — closure still applies in full.")],
        n, kicker=P10, accent=AMBER)
    n += 1

    X.process(
        prs, "Close Project or Phase — the Activity Sequence",
        [("Confirm completion", "Verify all work in the scope baseline is complete and all deliverables verified."),
         ("Obtain acceptance", "Secure formal, documented customer acceptance against the acceptance criteria."),
         ("Transition", "Hand the product to operations or the customer with training and documentation."),
         ("Close contracts", "Settle claims, finalise payments, close purchase orders and archive agreements."),
         ("Close financials", "Notify enterprise functions, close accounts, and release remaining budget."),
         ("Archive and release", "Archive all project information into OPAs and release the team and facilities.")],
        n, kicker=P10, accent=BLUE,
        note="Conclude external obligations including legal, regulatory and contractual "
             "matters — transfer of liability and closure of all accounts in the financial "
             "system are frequently forgotten and frequently examined.")
    n += 1

    X.cards(
        prs, "Acceptance of Deliverables",
        [("Acceptance criteria first", "Criteria are agreed at the start, in the "
                                       "requirements documentation and the scope baseline."),
         ("Verified before accepted", "Control Quality produces verified deliverables; "
                                      "Validate Scope converts them into accepted deliverables."),
         ("Formal and documented", "Acceptance must be written and signed by an authorised "
                                   "stakeholder — verbal approval is not acceptance."),
         ("Traceability matrix", "Use the requirements traceability matrix to prove every "
                                 "requirement reached completion and approval."),
         ("Partial acceptance", "Where some deliverables fail, accept what passes and raise "
                                "change requests for the remainder — do not stall everything."),
         ("Conditional acceptance", "Acceptance with a punch list must carry named owners "
                                    "and dates, or the residual work is never done.")],
        n, kicker=P10, accent=TEAL)
    n += 1

    X.cards(
        prs, "Transition and Handover to Operations",
        [("Adoption drives benefits", "Effective transitions enable end-user awareness, "
                                      "increasing adoption and therefore benefits realisation."),
         ("Training", "Users and operators need training on the new product or service "
                      "before, not after, they depend on it."),
         ("Documentation", "Operating manuals, as-built documentation and troubleshooting "
                           "guides transfer with the deliverable."),
         ("Communication", "Sustained communication between the project team and the "
                           "receiving organisation prevents the classic silent handover."),
         ("Post-implementation support", "Agree the hypercare period, the support model and "
                                         "who pays for it, before the team disbands."),
         ("Warranty and defect window", "Define the warranty period and the process for "
                                        "defects discovered after acceptance.")],
        n, kicker=P10, accent=VIOLET)
    n += 1

    X.matrix2x2(
        prs, "Readiness for Transition",
        "Operational readiness of the receiving organisation",
        "Product readiness of the deliverable",
        [("Delay the handover",
          "The product works but operations cannot run it. Invest in training, runbooks "
          "and support staffing before transitioning.", AMBER),
         ("Transition now",
          "Product and operations are both ready. Execute the handover, start hypercare "
          "and begin measuring benefits.", TEAL),
         ("Not ready — hold",
          "Neither side is ready. Do not transition; a forced handover here converts a "
          "project problem into an operational crisis.", ROSE),
         ("Fix defects first",
          "Operations are prepared but the product fails acceptance. Complete defect "
          "repair and re-validate scope.", VIOLET)],
        n, kicker=P10, accent=BLUE,
        note="ECO Process T10 asks you to validate readiness for transition — to "
             "operations or the next phase. Readiness is two-sided.")
    n += 1

    X.cards(
        prs, "Contents of the Final Report",
        [("Summary-level description", "What the project was, what it delivered, and the "
                                       "period over which it ran."),
         ("Scope objectives", "The scope objectives, the criteria used to evaluate them, "
                              "and evidence that they were met."),
         ("Quality objectives", "Quality objectives, the criteria applied, and the actual "
                                "quality achieved against them."),
         ("Cost and schedule performance", "The acceptable variance ranges, the actual "
                                           "variances, and the reason for each."),
         ("Benefits and business case", "Whether the intended benefits were achieved, and "
                                        "if not, when they are expected to be."),
         ("Risks, issues and recommendations", "Summary of how risks and issues were "
                                               "managed and what future projects should do differently.")],
        n, kicker=P10, accent=CYAN)
    n += 1

    X.cards(
        prs, "Finalising Contracts and Procurement Documentation",
        [("Contract schedule and scope", "Collect, index and file the contractual schedule "
                                         "and the final agreed statement of work."),
         ("Quality and cost performance", "File the supplier's quality records and the cost "
                                          "performance data against the agreement."),
         ("Change documentation", "Every contract change, modification and supplemental "
                                  "agreement is archived with its authorisation."),
         ("Payment and financial records", "Payment records, invoices and financial "
                                           "documents complete the commercial audit trail."),
         ("Inspection results", "Inspection and acceptance test results evidence that the "
                                "supplier met the agreed standard."),
         ("As-built documentation", "'As-built' or 'as-developed' documents, manuals and "
                                    "troubleshooting and technical documentation.")],
        n, kicker=P5, accent=AMBER)
    n += 1

    X.process(
        prs, "Procurement Closure Sequence",
        [("Verify delivery", "Confirm all contracted work and deliverables have been received and inspected."),
         ("Resolve claims", "Settle any open claims or disputes through negotiation or the contract's ADR method."),
         ("Final payment", "Release final payment and retention once the acceptance conditions are satisfied."),
         ("Formal notice", "Issue written notice of contract completion as required by the agreement."),
         ("Archive", "Index and file the complete procurement file for audit and future reference."),
         ("Evaluate the vendor", "Record supplier performance so future sourcing decisions are evidence-based.")],
        n, kicker=P5, accent=ROSE,
        note="Early termination is a valid form of procurement closure. The termination "
             "clause defines the rights of both parties and the settlement of costs "
             "already incurred.")
    n += 1

    X.cards(
        prs, "Releasing Resources and Updating OPAs",
        [("Release people", "Return team members to their functional units with a written "
                            "performance summary and a genuine thank you."),
         ("Release physical resources", "Return equipment, facilities and licences; "
                                        "unclaimed assets keep costing the organisation."),
         ("Close financial accounts", "Close cost centres and purchase orders so no further "
                                      "charges can be booked to a finished project."),
         ("Revoke access", "Remove system and data access — an open security question is a "
                           "real compliance finding at audit."),
         ("Update OPA templates", "Push improved templates, checklists and estimating data "
                                  "back into the organisational process assets."),
         ("Update historical databases", "Actual durations and costs make the next project's "
                                         "analogous and parametric estimates better.")],
        n, kicker=B6, accent=BLUE)
    n += 1

    X.compare(
        prs, "Lessons Learned Register vs Repository",
        ("Lessons learned register", "Live, project-level, updated continuously",
         ["A project document created early and updated throughout the whole life cycle",
          "Captures the situation, the impact, and the recommendation as events happen",
          "Owned by the project manager and visible to the whole project team",
          "Feeds every phase gate review, retrospective and status conversation",
          "Its final state is an input to the closure process and the final report"]),
        ("Lessons learned repository", "Organisational, permanent, cross-project",
         ["An organisational process asset holding lessons from all completed projects",
          "Updated at closure when the register's contents are transferred and indexed",
          "Owned by the PMO, searchable by process, phase, risk category and domain",
          "Consulted at the start of new projects to avoid repeating known mistakes",
          "Its value depends entirely on discipline at closure — the register is not enough"]),
        n, kicker=B6, lc=TEAL, rc=VIOLET,
        footer_note="Exam cue: 'during the project' or 'the team recorded' points to the "
                    "register. 'For future projects' or 'the organisation' points to the "
                    "repository.")
    n += 1

    X.cards(
        prs, "Finalising Lessons Learned for the Final Report",
        [("Scope changes", "What changed, why it changed, and whether the change control "
                           "process caught it early enough."),
         ("Schedule impacts", "Which estimates proved wrong and what the estimating "
                              "assumptions should have been."),
         ("Risks and issues", "Which risks materialised, which responses worked, and which "
                              "risks were never identified at all."),
         ("Stakeholder relationships", "Which engagement strategies built trust and which "
                                       "stakeholders were persistently misjudged."),
         ("Vendor relationships", "Supplier performance, contract type fit, and what to "
                                  "negotiate differently next time."),
         ("Artifacts and recommendations", "Which artifacts earned their keep, and specific "
                                           "recommendations for comparable future projects.")],
        n, kicker=B6, accent=AMBER)
    n += 1

    X.cards(
        prs, "Conducting the Project Retrospective",
        [("Internalise learning", "The goal is that the team internalises learning about "
                                  "both the work product and the process used to build it."),
         ("Capture successes and challenges", "Record what went well as deliberately as what "
                                              "went badly — repeatable success is a finding."),
         ("Qualitative data", "How people felt — morale, safety, frustration — is real data "
                              "and often explains the numbers."),
         ("Quantitative data", "Measurements: velocity, defect escape rate, cycle time, "
                               "variance against baseline."),
         ("Root cause to action plan", "Use the data to find root causes, design "
                                       "countermeasures and build an action plan for next time."),
         ("Praise and motivate", "Praise, congratulate and motivate the team — closure is "
                                 "the last chance to reinforce what you want repeated.")],
        n, kicker=B6, accent=CYAN)
    n += 1

    X.cards(
        prs, "Knowledge Transfer Before the Team Disbands",
        [("Identify critical knowledge", "Decide what knowledge is genuinely critical to "
                                         "operating and evolving the deliverable."),
         ("Gather it deliberately", "Interviews, documentation sprints and recorded "
                                    "walkthroughs capture what people carry in their heads."),
         ("Foster the environment", "People share tacit knowledge when they trust the "
                                    "audience and have time set aside to do it."),
         ("Explicit to the repository", "Codified knowledge goes into searchable, indexed "
                                        "assets with clear ownership after the project ends."),
         ("Tacit through people", "Pairing, shadowing and communities of practice are the "
                                  "only reliable transfer mechanisms for judgement."),
         ("Name the successor", "Every critical knowledge area needs a named operational "
                                "owner before the last team member leaves.")],
        n, kicker=PE7, accent=TEAL)
    n += 1

    X.cards(
        prs, "Benefits Realisation and Confirming Value",
        [("Benefits outlive the project", "Most benefits are realised in operations, months "
                                          "after the project team has been released."),
         ("Benefits management plan", "It names each benefit, its metric, its target, its "
                                      "timeframe and its accountable owner."),
         ("Verify the measurement system", "ECO Process T3 requires you to verify a system "
                                           "is actually in place to track the benefits."),
         ("Hand over the measurement", "Transfer benefit tracking to a business owner with "
                                       "the authority and budget to act on the readings."),
         ("Compare to the business case", "Report actual against the promised business case "
                                          "— honestly, including where it fell short."),
         ("Value in adaptive delivery", "Adaptive projects confirm value every increment, so "
                                        "closure confirms cumulative rather than deferred value.")],
        n, kicker=P3, accent=VIOLET)
    n += 1

    X.cards(
        prs, "Premature and Terminated Project Closure",
        [("Termination is legitimate", "Stopping a project whose business case has failed "
                                       "protects the organisation — it is not a personal failure."),
         ("Common triggers", "Funding withdrawn, strategy changed, technology superseded, "
                             "regulator intervened, or the benefit disappeared."),
         ("Closure still applies fully", "Every closure activity is performed: acceptance of "
                                         "partial work, contract settlement, archiving, release."),
         ("Document the reason", "Record precisely why the project was terminated — this is "
                                 "among the most valuable lessons in the repository."),
         ("Salvage the value", "Completed components, research and built assets may be "
                               "reusable elsewhere; identify them before archiving."),
         ("Manage the team", "Termination hits morale hardest. Communicate early, honestly, "
                             "and support each member's next assignment.")],
        n, kicker=P10, accent=ROSE)
    n += 1

    X.exam(
        prs, "Exam Traps — Closing",
        [("The customer has stopped responding and will not sign acceptance",
          "Follow the escalation path in the communications and governance plans; do not "
          "close the project without documented formal acceptance."),
         ("The project is cancelled halfway through by the sponsor",
          "Perform Close Project or Phase in full — acceptance of partial work, contract "
          "closure, lessons learned and archiving all still apply."),
         ("A team member asks to move to a new project before closure is complete",
          "Complete knowledge transfer and lessons learned capture before releasing them; "
          "resource release is a closure activity, not a favour."),
         ("The benefits will not be measurable for another twelve months",
          "Hand the benefits management plan and its measurement system to an accountable "
          "business owner; the project still closes.")],
        n, kicker="EXAM FOCUS · CLOSING", accent=ROSE)
    n += 1

    X.recap(
        prs, "Closing Recap",
        [("Accept before you close", "Formal, documented acceptance against agreed criteria "
                                     "is the gateway to every other closure activity."),
         ("Verified then accepted", "Control Quality verifies; Validate Scope accepts; Close "
                                    "Project archives. Learn that sequence."),
         ("Transition is two-sided", "Readiness means the product works and operations can "
                                     "actually run it — check both."),
         ("Close every contract", "Claims settled, payments made, procurement file archived, "
                                  "vendor performance recorded."),
         ("Register to repository", "The lessons learned register becomes part of the "
                                    "organisational lessons learned repository at closure."),
         ("Benefits need an owner", "Hand measurement to an accountable business owner — the "
                                    "project ends, the benefits do not."),
         ("Termination closes fully", "A cancelled project runs the complete closure process, "
                                      "including documenting why it was stopped."),
         ("Update the OPAs", "Templates, estimating data and historical records are the "
                             "organisation's return on your experience.")],
        n, kicker="RECAP · CLOSING", accent=CYAN)
    n += 1

    # ------------------------------------------------------ exam preparation
    X.statement(
        prs, "PMP exam preparation",
        "The exam does not test what you memorised. It tests what you would do next, in a situation described in four lines.",
        [("Situational by design",
          "Most items describe a scenario and ask for the best next action, not a definition."),
         ("Approach-agnostic",
          "Predictive, adaptive and hybrid appear throughout all three domains, not in separate sections."),
         ("Mindset over method",
          "PMI rewards the servant leader who investigates, communicates and follows the process.")],
        n, kicker="PMP EXAM PREPARATION", accent=BLUE)
    n += 1

    X.table(
        prs, "PMP Exam Structure — July 2026 Content Outline",
        ["Element", "Specification", "What it means for you"],
        [["Total questions", f"{E['questions']} questions",
          "Every item is presented; you cannot tell which ones count"],
         ["Scored questions", f"{E['scored']} scored items",
          "Your result is calculated from these alone"],
         ["Pretest questions", f"{E['pretest']} unscored pretest items",
          "Trialled for future forms — never leave one blank"],
         ["Time allowed", f"{E['minutes']} minutes (4 hours)",
          "About 80 seconds per question including reading time"],
         ["Breaks", "Two 10-minute breaks",
          E["breaks"]],
         ["Approach mix", "About 40% predictive",
          E["approach_mix"]],
         ["Tutorial and survey", "Outside the 240 minutes",
          "The tutorial and the closing survey do not consume exam time"],
         ["Attempts", "Up to three within the one-year eligibility period",
          "After three attempts you must wait before reapplying"]],
        n, kicker="PMP EXAM PREPARATION", accent=VIOLET, widths=[2.2, 3.4, 5.4],
        note="Once you review your responses and start a break, you cannot return to the "
             "questions in the section you have just completed.")
    n += 1

    X.chart(
        prs, "Domain Weighting — Where the Questions Come From",
        "pie",
        [f"{name} {pct}%" for _, name, pct, _ in cd.ECO_DOMAINS],
        [("Percentage of items", [pct for _, _, pct, _ in cd.ECO_DOMAINS])],
        n, kicker="PMP EXAM PREPARATION", accent=TEAL,
        insight=["Process at 41% is the largest single domain — roughly 70 of the 170 scored items.",
                 "People at 33% means leadership and stakeholder items outnumber pure Business Environment items.",
                 "Business Environment at 26% covers governance, compliance, change, risk and improvement.",
                 "Weighting applies to items, not to study hours — weak areas deserve disproportionate time.",
                 "Every domain contains predictive, adaptive and hybrid scenarios; none is 'the agile domain'."])
    n += 1

    X.chart(
        prs, "Study Effort vs Domain Weight — Plan Your Revision",
        "column",
        ["People", "Process", "Business Environment"],
        [("Exam weight (%)", [33, 41, 26]),
         ("Suggested revision hours", [24, 32, 20])],
        n, kicker="PMP EXAM PREPARATION", accent=AMBER,
        insight=["Allocate revision roughly in proportion to domain weight, then adjust for your mock results.",
                 "Process carries the formulas and the process anatomy — it needs the most contact hours.",
                 "People is high weight and highly situational; practice questions beat re-reading notes.",
                 "Business Environment is compact but dense in compliance and governance vocabulary.",
                 "Re-plan after every mock exam: the domain you scored worst on gets the next block."])
    n += 1

    X.table(
        prs, "The Six Question Types",
        ["Type", "How it works", "Strategy"],
        [[t[0], t[1], s] for t, s in zip(
            E["question_types"],
            ["Eliminate two options first, then choose between the remaining pair using the PMI mindset.",
             "Read the stem for how many answers are required and select exactly that number.",
             "Do the pairs you are certain of first; the remaining items are constrained by elimination.",
             "Study the image before reading the options — the diagram usually resolves the ambiguity.",
             "Extract the specific data point the question asks for; do not interpret the whole chart.",
             "Read the full scenario once, then answer each linked question referring back to the exhibit."])],
        n, kicker="PMP EXAM PREPARATION", accent=ROSE, widths=[2.2, 5.0, 3.8],
        note="Graphic-based questions are NEW in the July 2026 outline — expect to read "
             "control charts, network diagrams, burndowns and EVM S-curves directly.")
    n += 1

    X.table(
        prs, "PMP Certification Eligibility",
        ["Educational background", "Project management experience", "Training"],
        [["Upper-secondary / secondary school completion (EQF Level 4 / ISCED 3-4)",
          "Minimum 60 months (5 years) of non-overlapping experience leading projects in the past 10 years",
          "35 hours of commercial project management training"],
         ["Recognised associate-level, higher-certificate or advanced vocational programme (EQF Level 5 / ISCED 5)",
          "Minimum 48 months (4 years) of non-overlapping experience leading projects in the past 10 years",
          "35 hours of commercial project management training"],
         ["Bachelor's degree or higher, or a qualification mapped to EQF Level 6 / ISCED 6",
          "Minimum 36 months (3 years) of non-overlapping experience leading projects in the past 10 years",
          "35 hours of commercial project management training"],
         ["Bachelor's or postgraduate degree from a PMI GAC-accredited programme",
          "Minimum 24 months (2 years) of non-overlapping experience leading projects in the past 10 years",
          "35 hours of commercial project management training"]],
        n, kicker="PMP EXAM PREPARATION", accent=CYAN, widths=[4.0, 4.6, 2.4],
        note="Experience must be in leading and directing projects, accrued within the last "
             "10 years. Applications may be audited — keep contact details for verifiers.")
    n += 1

    X.process(
        prs, "How to Read a Situational Question",
        [("Read the last line first", "The actual question is at the end; knowing it changes how you read the stem."),
         ("Identify the process group", "Are you planning, executing, monitoring or closing? It narrows the answers."),
         ("Find what already happened", "Past-tense facts tell you which steps are done and cannot be the answer."),
         ("Spot the real problem", "The scenario's noise is deliberate; name the single issue being asked about."),
         ("Eliminate two options", "Remove anything reactive, blaming, escalating too early or bypassing process."),
         ("Choose the PMI answer", "Prefer investigating, communicating and following the documented process.")],
        n, kicker="PMP EXAM PREPARATION", accent=BLUE,
        note="'Best', 'first', 'next' and 'most likely' are not decoration. 'First' usually "
             "means gather information; 'next' means the step after what was described; "
             "'best' means the most complete and process-compliant option.")
    n += 1

    X.table(
        prs, "Common Distractor Patterns",
        ["Distractor", "Why it looks right", "Why it is wrong"],
        [["Escalate to the sponsor immediately",
          "Escalation is a real governance tool and sounds decisive",
          "PMI expects you to gather facts and act within your authority first"],
         ["Ask the team to work overtime",
          "It appears to solve a schedule problem directly",
          "It ignores root cause, damages the team, and skips impact analysis"],
         ["Update the plan / baseline directly",
          "The plan clearly needs to change",
          "Baselines change only through approved change requests"],
         ["Do nothing and continue monitoring",
          "Sometimes genuinely correct in risk acceptance scenarios",
          "Usually a trap when the scenario describes an active impact"],
         ["Remove the team member",
          "It removes the visible symptom quickly",
          "Conflict and performance are addressed through coaching first"],
         ["Add the change because the customer asked",
          "Customer satisfaction sounds like the PMI value",
          "Every scope change requires impact analysis and change control"]],
        n, kicker="PMP EXAM PREPARATION", accent=ROSE, widths=[3.0, 3.6, 4.4])
    n += 1

    X.formula(
        prs, "Formula Sheet Recap — Earned Value",
        [("Cost Variance", "CV = EV - AC",
          "Negative means over budget. Every variance is EV minus something."),
         ("Schedule Variance", "SV = EV - PV",
          "Negative means behind schedule. Always zero at project completion."),
         ("Cost Performance Index", "CPI = EV / AC",
          "Below 1.0 means you earn less than a dollar of value per dollar spent."),
         ("Schedule Performance Index", "SPI = EV / PV",
          "Below 1.0 means work is arriving slower than the plan assumed."),
         ("Estimate at Completion", "EAC = BAC / CPI",
          "The default forecast when current cost performance is expected to continue.")],
        n, kicker="FORMULA SHEET · EVM", accent=AMBER,
        note="Also carry: ETC = EAC - AC, VAC = BAC - EAC, and "
             "TCPI = (BAC - EV) / (BAC - AC).")
    n += 1

    X.formula(
        prs, "Formula Sheet Recap — Estimating, Float and Risk",
        [("PERT triangular", "(O + M + P) / 3",
          "Simple average of optimistic, most likely and pessimistic estimates."),
         ("PERT beta", "(O + 4M + P) / 6",
          "Weighted average giving the most likely estimate four times the weight."),
         ("PERT standard deviation", "(P - O) / 6",
          "The spread of the estimate; a proxy for how uncertain the activity is."),
         ("Total float", "LS - ES  or  LF - EF",
          "Delay available without delaying project completion. Zero float = critical path."),
         ("Expected Monetary Value", "EMV = Probability x Impact",
          "Sum the EMV of every branch to value a decision tree; threats are negative."),
         ("Communication channels", "n(n-1) / 2",
          "Channels grow quadratically with people — the case for smaller teams.")],
        n, kicker="FORMULA SHEET · ESTIMATING & RISK", accent=TEAL,
        note="Point of confusion to settle now: total float belongs to a path; free float "
             "is the delay available without delaying the very next activity.")
    n += 1

    X.cards(
        prs, "Exam Day Strategy",
        [("Pace deliberately", "180 questions in 240 minutes is about 80 seconds each. "
                               "Check your position at every 45-question mark."),
         ("Answer everything", "There is no penalty for a wrong answer, and 10 items do not "
                               "count anyway — never leave a blank."),
         ("Mark and move on", "If an item takes more than two minutes, choose your best "
                              "option, flag it and move on."),
         ("Use the breaks", "Take both 10-minute breaks even if you feel fine — fatigue "
                            "damages accuracy far more than it damages speed."),
         ("Case study section first", "The case-study section comes before the first break; "
                                      "read the exhibit carefully once rather than repeatedly."),
         ("Trust your first instinct", "Change an answer only when you find a specific fact "
                                       "in the stem that you missed the first time.")],
        n, kicker="PMP EXAM PREPARATION", accent=VIOLET)
    n += 1

    X.cards(
        prs, "The PMI Mindset — the Tiebreaker on Every Item",
        [("Be proactive", "Prevent problems rather than react to them; the answer that "
                          "anticipates usually beats the answer that responds."),
         ("Gather facts first", "Understand the situation before acting, escalating or "
                                "blaming — 'analyse the impact' is rarely wrong."),
         ("Serve the team", "Remove impediments, empower and coach; do not command, punish "
                            "or reassign as a first response."),
         ("Follow the process", "Use the documented change, risk, quality and escalation "
                                "processes — never bypass governance for speed."),
         ("Communicate directly", "Talk to the person concerned before involving their "
                                  "manager or the sponsor."),
         ("Deliver value", "When options conflict, choose the one that protects the "
                           "business value and the customer's real need.")],
        n, kicker="PMP EXAM PREPARATION", accent=CYAN)
    n += 1

    X.timeline(
        prs, "Your Study Plan After This Course",
        [("Week 1", "Consolidate notes; review every ITTO and the formula sheet from memory."),
         ("Week 2", "Complete the PMI Study Hall or equivalent domain quizzes; log weak areas."),
         ("Week 3", "First full 180-question timed mock; analyse every wrong answer's reason."),
         ("Week 4", "Targeted revision on the two weakest domains plus formula drills."),
         ("Week 5", "Second full timed mock; target above 70% in all three domains."),
         ("Week 6", "Light review, sleep, and sit the exam — do not cram the final 48 hours.")],
        n, kicker="PMP EXAM PREPARATION", accent=BLUE,
        note="Submit your PMI application early — it can take up to five business days to "
             "review, and audited applications take longer. Your one-year eligibility "
             "period starts when the application is approved.")
    n += 1

    X.cards(
        prs, "The 35 PDUs and Maintaining Your Certification",
        [("This course = 35 contact hours", "It satisfies PMI's requirement for 35 hours of "
                                            "commercial project management training."),
         ("Keep your evidence", "Retain the certificate of completion and the course "
                                "outline in case your application is audited."),
         ("CCR cycle", "Once certified you must earn 60 PDUs every three years to maintain "
                       "the PMP credential."),
         ("Education PDUs", "Minimum 35 of the 60 must be education PDUs across the PMI "
                            "Talent Triangle."),
         ("Talent Triangle", "Ways of Working, Power Skills, and Business Acumen — at least "
                             "8 PDUs in each per cycle."),
         ("Giving back PDUs", "Up to 25 PDUs may come from volunteering, creating content "
                              "or working as a practitioner.")],
        n, kicker="PMP EXAM PREPARATION", accent=AMBER)
    n += 1

    X.exam(
        prs, "Final Exam Traps — Whole-Course Review",
        [("A risk you identified has now occurred and is delaying the team",
          "It is now an issue. Move it to the issue log, implement the planned response, "
          "and reassess the remaining risk exposure."),
         ("CPI is 0.85 and the sponsor asks whether you will finish within budget",
          "Calculate EAC. At BAC/CPI the forecast exceeds BAC, so report the forecast "
          "overrun and present recovery options."),
         ("A stakeholder was never identified and now objects to a delivered feature",
          "Update the stakeholder register, analyse their influence and interest, and "
          "revise the engagement plan before negotiating scope."),
         ("The team wants to add a nice extra feature at no cost to the customer",
          "That is gold plating. Deliver to the acceptance criteria; route any genuine "
          "addition through integrated change control.")],
        n, kicker="EXAM FOCUS · WHOLE COURSE", accent=ROSE)
    n += 1

    X.recap(
        prs, "Topic 6 Recap — Close the Project and Exam Readiness",
        [("Closure is a process", "Acceptance, transition, contract and financial closure, "
                                  "archiving and release — performed in full, every time."),
         ("Formal acceptance is required", "Written sign-off against agreed acceptance "
                                           "criteria is what makes a project complete."),
         ("Transition drives benefits", "Training, documentation and support determine "
                                        "adoption, and adoption determines value."),
         ("Register becomes repository", "Lessons learned move from a project document into "
                                         "an organisational process asset at closure."),
         ("Retrospectives use both data types", "Qualitative feelings and quantitative "
                                                "measures together produce real root causes."),
         ("Benefits need an accountable owner", "Hand over the measurement system; most "
                                                "benefits arrive after the team has gone."),
         ("Exam: 180 in 240 minutes", "170 scored plus 10 pretest items, with two 10-minute "
                                      "breaks and roughly 80 seconds per question."),
         ("Exam: 33 / 41 / 26", "People, Process and Business Environment weighting — with "
                                "about 40% predictive and 60% adaptive or hybrid."),
         ("Six question types", "Including the new graphic-based items and the case-study "
                                "section that precedes the first break."),
         ("Answer with the PMI mindset", "Investigate first, follow the process, serve the "
                                         "team, and protect the business value.")],
        n, kicker="RECAP · TOPIC 6", accent=CYAN)
    n += 1

    return n
