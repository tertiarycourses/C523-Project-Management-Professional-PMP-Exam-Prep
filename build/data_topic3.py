"""Topic 3 — Plan the Project."""
import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

P1 = cd.eco("Process", 1)
P2 = cd.eco("Process", 2)
P4 = cd.eco("Process", 4)
P5 = cd.eco("Process", 5)
P6 = cd.eco("Process", 6)
P7 = cd.eco("Process", 7)
P8 = cd.eco("Process", 8)
B5 = cd.eco("Business Environment", 5)
B3 = cd.eco("Business Environment", 3)
PE8 = cd.eco("People", 8)
PE4 = cd.eco("People", 4)


# ===================================================== the integrated plan
def _plan(prs, n):
    X.statement(
        prs, "Why planning is the heart of the Process domain",
        "A plan is a decision record, not a document",
        [("Reduces rework", "Decisions made deliberately up front cost a fraction of "
          "the same decisions made reactively during delivery."),
         ("Creates alignment", "A shared plan lets thirty people make consistent "
          "choices without asking the project manager each time."),
         ("Enables control", "You cannot detect variance without a baseline to "
          "measure the actual result against.")],
        n, kicker=P1, accent=BLUE); n += 1

    X.itto(
        prs, "Develop Project Management Plan — ITTO",
        ["Project charter — the authorised high-level boundaries",
         "Outputs from other planning processes (all subsidiary plans)",
         "Enterprise environmental factors (EEFs)",
         "Organisational process assets (OPAs), templates, standards"],
        ["Expert judgment from PMO, SMEs and delivery leads",
         "Data gathering: brainstorming, checklists, focus groups",
         "Interpersonal and team skills: conflict management, facilitation",
         "Meetings — notably the project kick-off meeting"],
        ["Project management plan — the integrated, approved artefact",
         "Contains all subsidiary plans plus the three baselines",
         "Contains the development approach and life cycle description"],
        n, kicker=P1,
        purpose="Integration is the only knowledge area whose job is to reconcile "
                "the other twelve — the PM owns the seams between the plans."); n += 1

    X.cards(
        prs, "What the project management plan actually enables", [
            ("Execute", "Tells the team what work to do, in what order, with which "
             "resources and to which acceptance criteria."),
            ("Monitor", "Defines the metrics, the reporting cadence and the "
             "thresholds that trigger a management conversation."),
            ("Control", "Establishes the baselines against which variance is "
             "measured and the change control process that protects them."),
            ("Close", "Defines the exit criteria, handover conditions and the "
             "evidence needed for formal acceptance of deliverables."),
            ("Guardrails", "Sets the boundaries inside which the team may act "
             "autonomously without escalating every decision upward."),
            ("Tailoring", "Records what was deliberately omitted or simplified for "
             "this project's size, risk and regulatory profile."),
        ], n, kicker=P1, accent=TEAL); n += 1

    X.cards(
        prs, "The subsidiary plans inside the integrated plan", [
            ("Scope management plan", "How scope is defined, validated and "
             "controlled, and how the WBS will be produced and maintained."),
            ("Schedule management plan", "The scheduling method, tool, units of "
             "measure, accuracy thresholds and control rules."),
            ("Cost management plan", "Estimating accuracy, units, control "
             "thresholds, earned value rules and reporting formats."),
            ("Quality management plan", "Standards to be met, quality roles, "
             "review activities and the improvement approach."),
            ("Resource management plan", "How people and physical resources are "
             "identified, acquired, developed and released."),
            ("Communications plan", "Who needs what information, in what format, "
             "how often, and through which channel."),
            ("Risk management plan", "Methodology, roles, budgeting, timing, "
             "categories, probability and impact definitions."),
            ("Procurement plan", "What is bought versus built, contract types, "
             "and how sellers are selected and managed."),
            ("Stakeholder engagement plan", "The strategies used to move each "
             "stakeholder from current to desired engagement level."),
        ], n, kicker=P1, accent=VIOLET); n += 1

    X.compare(
        prs, "Plan-driven versus collaborative planning",
        ("PLAN-DRIVEN (PREDICTIVE)",
         "The plan is authored, then approved, then followed",
         ["The project manager drafts the plan and seeks formal sign-off",
          "Detail is pushed as far forward as the information allows",
          "Change after baseline requires a formal change request",
          "Strong on auditability, regulatory evidence and contract control",
          "Risk: the plan ages badly when the environment moves fast"]),
        ("COLLABORATIVE (ADAPTIVE)",
         "The plan is co-created continuously by those doing the work",
         ["The product owner sets objectives from customer needs and value",
          "The team estimates and sequences its own work each iteration",
          "Team members are the local domain experts on how work gets done",
          "The PM or scrum master facilitates rather than dictates",
          "Risk: without discipline, planning degrades into improvisation"]),
        n, kicker=P1, lc=BLUE, rc=TEAL,
        footer_note="Most real projects are hybrid: governance-level milestones are "
                    "plan-driven while the work inside each milestone is planned "
                    "collaboratively by the delivery team."); n += 1

    X.process(
        prs, "Rolling wave planning — progressive elaboration in practice", [
            ("Plan the horizon", "Decompose only the near-term work to work-package "
             "detail; leave later work as planning packages."),
            ("Execute the wave", "Deliver the detailed work while the longer-term "
             "scope stays deliberately coarse."),
            ("Learn", "Capture actuals, estimating error and emerging risks from "
             "the wave just completed."),
            ("Elaborate next", "Decompose the next horizon using what you just "
             "learned, not what you guessed at the start."),
            ("Re-baseline", "Fold the newly detailed work into the baseline through "
             "the agreed change control route."),
        ], n, kicker=P1, accent=AMBER,
        note="Rolling wave applies to BOTH predictive and adaptive approaches — it "
             "is applied to work packages, planning packages and release planning, "
             "and is the standard answer when a question says 'not enough "
             "information is available to plan the later phases'."); n += 1

    X.itto(
        prs, "Plan Stakeholder Engagement — ITTO",
        ["Project charter and project management plan",
         "Project documents: stakeholder register, issue log, change log",
         "Agreements with contracting parties",
         "EEFs — organisational culture, political climate, regulation"],
        ["Expert judgment on politics and organisational power",
         "Data gathering: benchmarking against comparable projects",
         "Data analysis: assumption/constraint and root cause analysis",
         "Decision making: prioritisation and ranking of stakeholders",
         "Data representation: mind mapping, engagement assessment matrix"],
        ["Stakeholder engagement plan — the strategies and actions needed",
         "Defines required involvement level per stakeholder group",
         "Feeds directly into the communications management plan"],
        n, kicker=PE4,
        purpose="Engagement is planned, not improvised: you decide deliberately who "
                "must be moved from resistant to supportive, and how."); n += 1

    X.table(
        prs, "Stakeholder Engagement Assessment Matrix (SEAM)",
        ["Level", "What it looks like", "Typical intervention"],
        [["Unaware", "Does not know the project exists or that it will affect them",
          "Awareness communication; briefing pack; named contact point"],
         ["Resistant", "Aware of the project and actively opposed to the change",
          "Surface the objection, negotiate, find the win, escalate if needed"],
         ["Neutral", "Aware but neither supportive nor opposed; will not help",
          "Show the personal and unit-level benefit; invite to a demo"],
         ["Supportive", "Aware and in favour, will speak well of the project",
          "Keep informed, use as a reference and as an internal advocate"],
         ["Leading", "Actively engaged in ensuring the project succeeds",
          "Give real influence: steering seat, sponsorship of a workstream"]],
        n, kicker=PE4, accent=CYAN, widths=[1.1, 2.6, 2.9],
        note="Mark C for the CURRENT level and D for the DESIRED level in each row. "
             "Where C and D differ you have an engagement gap that needs a named "
             "action and an owner — not a hope."); n += 1

    X.exam(
        prs, "Exam focus — planning and stakeholder engagement", [
            ("A stakeholder is surprised by a project decision that affected them",
             "Review and update the stakeholder engagement plan and the "
             "communications plan — the omission is a planning defect"),
            ("Later phases cannot be planned in detail yet",
             "Apply rolling wave planning; use planning packages now and elaborate "
             "them when information becomes available"),
            ("The team asks who decides how the work will be done",
             "The team members do — they are the local domain experts; the PM "
             "facilitates and removes impediments"),
            ("Sponsor asks 'what is the project management plan for?'",
             "It is the approved basis for executing, monitoring, controlling and "
             "closing the work — not a status report"),
        ], n, accent=ROSE); n += 1
    return n


# ================================================================== scope
def _scope(prs, n):
    X.statement(
        prs, "Knowledge area 1 of 8 in the planning block",
        "Scope: agree what is in, and prove what is out",
        [("Product scope", "The features and functions that characterise the "
          "product, service or result being delivered."),
         ("Project scope", "The work that must be performed to deliver that "
          "product with the specified features and functions."),
         ("Why it matters", "Every schedule, cost, quality and risk number in the "
          "plan is derived from the agreed scope.")],
        n, kicker=P2, accent=TEAL); n += 1

    X.itto(
        prs, "Plan Scope Management — ITTO",
        ["Project charter — high-level requirements and boundaries",
         "Project management plan: quality and life cycle descriptions",
         "EEFs — organisational culture, infrastructure, marketplace",
         "OPAs — policies, historical scope statements, lessons learned"],
        ["Expert judgment from prior similar projects",
         "Data analysis — alternatives analysis on how to collect requirements",
         "Meetings with sponsor, selected stakeholders and the team"],
        ["Scope management plan — how scope will be defined and controlled",
         "Requirements management plan — how requirements are gathered, "
         "analysed, documented and traced"],
        n, kicker=P2,
        purpose="These two plans are process documents: they describe how you will "
                "do scope work, not what the scope actually is."); n += 1

    X.cards(
        prs, "What the scope management plan must specify", [
            ("Scope statement preparation", "The process used to prepare a detailed "
             "project scope statement from the charter and requirements."),
            ("WBS creation", "How the WBS will be created from the detailed scope "
             "statement, and the decomposition rules to apply."),
            ("Baseline approval", "How the scope baseline will be reviewed, "
             "approved and subsequently maintained."),
            ("Deliverable acceptance", "How formal acceptance of completed "
             "deliverables will be obtained and evidenced."),
            ("Change control", "How change requests to the scope statement are "
             "raised, assessed, and routed for a decision."),
            ("Tailoring decisions", "Which scope activities are simplified or "
             "omitted given this project's size and risk."),
        ], n, kicker=P2, accent=BLUE); n += 1

    X.table(
        prs, "Scope planning analysis techniques",
        ["Technique", "What it does", "When you reach for it"],
        [["Document analysis", "Derives requirements from existing documents such "
          "as contracts, SOPs, regulations and prior project files",
          "A predecessor system or process already exists on paper"],
         ["Alternatives analysis", "Evaluates possible options or approaches for "
          "executing and performing the project work",
          "More than one credible way to deliver the same outcome"],
         ["Product analysis", "Asks questions about a product and forms answers "
          "describing its use, characteristics and value",
          "The deliverable is a product rather than a service"],
         ["Product breakdown", "Splits a product and its requirements into "
          "components to gain a clear understanding of the work",
          "Complex physical or software product with many subsystems"],
         ["Systems engineering", "Approaches design, integration, management and "
          "the life cycle of complex systems in a multidisciplinary way",
          "Highly interdependent, safety- or mission-critical systems"]],
        n, kicker=P2, accent=VIOLET, widths=[1.3, 3.0, 2.4]); n += 1

    X.compare(
        prs, "Scope in predictive versus agile delivery",
        ("PREDICTIVE SCOPE",
         "Fixed early, defended by change control",
         ["Scope is planned in full at the start of the project",
          "Captured in a detailed project scope statement and WBS",
          "Baselined once approved by the sponsor or change board",
          "Any change during delivery requires a formal change request",
          "Time and cost flex; scope is held constant wherever possible"]),
        ("AGILE SCOPE",
         "Fixed in the sprint, variable across the release",
         ["Product owner determines and prioritises the product backlog",
          "Scope may legitimately change between every sprint",
          "Detail is added just in time, at backlog refinement",
          "Time (the sprint) and cost (the team) are fixed instead",
          "Value delivered per iteration is the control mechanism"]),
        n, kicker=P2, lc=BLUE, rc=TEAL,
        footer_note="Exam cue: 'requirements are expected to evolve' points to "
                    "adaptive; 'requirements are stable and the contract is fixed "
                    "price' points to predictive."); n += 1

    X.cards(
        prs, "Agile scope artefacts", [
            ("Product roadmap", "Envisions and plans the big picture — product "
             "strategy, direction and the value to be delivered over time."),
            ("Themes and goals", "Groups related features under overarching goals "
             "so structure and association are visible to stakeholders."),
            ("Milestones", "Dates when major items will occur or be delivered — "
             "the fixed points a fluid backlog must still respect."),
            ("Story map", "Organises user stories into functional groups within a "
             "narrative flow, so the whole product is visible at once."),
            ("Product backlog", "The single ordered list of everything that might "
             "be built, owned and prioritised by the product owner."),
            ("Increment", "The working, potentially releasable slice of product "
             "produced by each iteration and inspected at review."),
        ], n, kicker=P2, accent=AMBER); n += 1


    X.itto(
        prs, "Collect Requirements — ITTO",
        ["Project charter and business documents (business case)",
         "Project management plan: scope, requirements and stakeholder plans",
         "Project documents: assumption log, lessons learned, stakeholder register",
         "Agreements and enterprise environmental factors"],
        ["Data gathering: brainstorming, interviews, focus groups, "
         "questionnaires and surveys, benchmarking",
         "Data analysis: document analysis",
         "Decision making: voting, multi-criteria decision analysis",
         "Data representation: affinity diagram, mind mapping",
         "Interpersonal and team skills: nominal group technique, "
         "observation/conversation, facilitation",
         "Context diagram and prototypes"],
        ["Requirements documentation — grouped, unambiguous, testable",
         "Requirements traceability matrix (RTM)"],
        n, kicker=P2,
        purpose="Requirements are the bridge between stakeholder need and "
                "deliverable — every later baseline traces back to them."); n += 1

    X.cards(
        prs, "The requirements management plan", [
            ("What it is", "The defined process for how requirements will be "
             "gathered, analysed, documented, managed and controlled."),
            ("Also called", "The business analysis plan — in organisations with a "
             "formal BA function it is owned jointly with the BA."),
            ("Configuration", "States how requirement changes are initiated, "
             "analysed, traced, tracked and approved."),
            ("Prioritisation", "Records the prioritisation method that will be "
             "used, such as MoSCoW or a weighted scoring model."),
            ("Traceability", "Defines the traceability structure — which "
             "attributes are recorded against each requirement."),
            ("Metrics", "Defines the product metrics that will be used and the "
             "rationale for choosing them."),
        ], n, kicker=P2, accent=ROSE); n += 1

    X.table(
        prs, "Requirements Traceability Matrix — what each column proves",
        ["Column", "Contents", "Question it answers"],
        [["Requirement ID", "Unique persistent identifier for the requirement",
          "Can I refer to this unambiguously in every other artefact?"],
         ["Business need", "The business case objective or benefit it supports",
          "Why are we building this at all?"],
         ["Project objective", "The charter objective the requirement serves",
          "Is this in scope or is it somebody's pet feature?"],
         ["WBS deliverable", "The work package that produces it",
          "Who is building it and where is it in the schedule?"],
         ["Product design", "The design element or component that realises it",
          "Has anyone actually designed a solution for this?"],
         ["Test case", "The verification or acceptance test",
          "How will we prove it works before handover?"],
         ["Status", "Active, cancelled, deferred, added, approved, assigned",
          "Is this still live and who signed it off?"]],
        n, kicker=P2, accent=TEAL, widths=[1.2, 2.6, 2.9]); n += 1

    X.table(
        prs, "Requirement gathering techniques compared",
        ["Technique", "How it works", "Best for"],
        [["Brainstorming", "Relaxed informal group idea generation using lateral "
          "thinking; quantity first, judgement deferred", "Wide divergent option "
          "generation early in discovery"],
         ["Interviews", "Structured or unstructured one-to-one questioning of "
          "stakeholders and SMEs", "Sensitive, political or expert-held detail"],
         ["Focus groups", "Moderated discussion with pre-qualified stakeholders "
          "and subject matter experts", "Attitudes, expectations and reactions"],
         ["Questionnaires/surveys", "Written question sets to large or "
          "geographically dispersed audiences", "Statistically meaningful breadth"],
         ["Benchmarking", "Compares practices against other organisations to "
          "identify best practice", "Setting a performance bar to meet or exceed"],
         ["Nominal group technique", "Brainstorm, then rank ideas by individual "
          "vote to produce a prioritised list", "Converging a large idea pool"],
         ["Observation (job shadowing)", "Watch people do the work in situ",
          "Tacit process detail people cannot articulate"],
         ["Facilitation", "Focused workshops (JAD, QFD) that cross functions",
          "Reconciling conflicting cross-department requirements"]],
        n, kicker=P2, accent=BLUE, widths=[1.4, 2.8, 2.3]); n += 1


    X.table(
        prs, "Requirement prioritisation techniques",
        ["Technique", "Mechanics", "Benefit"],
        [["MoSCoW (Dai Clegg)", "Sort into Must have, Should have, Could have, "
          "Won't have this time", "Reaches shared understanding of importance fast"],
         ["Kano model", "Classify features as Basic, Performance, Delighter, "
          "Indifferent or Reverse", "Separates satisfiers from mere expectations"],
         ["100-point method", "Each stakeholder distributes 100 points across the "
          "candidate requirements", "Forces trade-offs; exposes true preference"],
         ["Weighted/multi-criteria", "Score each requirement against weighted "
          "criteria and rank the totals", "Defensible, auditable decision trail"],
         ["Paired comparison", "Compare requirements two at a time and tally the "
          "wins", "Works when stakeholders cannot rank a long list"],
         ["Value/effort matrix", "Plot benefit against cost of delivery on a 2x2",
          "Surfaces the quick wins and the money pits"]],
        n, kicker=P2, accent=AMBER, widths=[1.4, 2.8, 2.3]); n += 1

    X.matrix2x2(
        prs, "MoSCoW as a decision grid", "URGENCY OF NEED",
        "IMPACT IF ABSENT",
        [("MUST HAVE", "Non-negotiable for this release; without it the delivery "
          "has no legal, safety or business viability.", ROSE),
         ("SHOULD HAVE", "Important and painful to omit, but a workaround exists "
          "for the duration of this release.", AMBER),
         ("COULD HAVE", "Desirable and included only if time and cost allow; the "
          "first thing dropped when the sprint is tight.", CYAN),
         ("WON'T HAVE (THIS TIME)", "Explicitly agreed as out of scope now — "
          "recorded, not forgotten, and revisited next release.", BLUE)],
        n, kicker=P2, accent=AMBER,
        note="The discipline is in the W: writing down what you are NOT doing is "
             "what stops scope creep later. Cap Must-haves at roughly 60% of "
             "capacity so there is room to absorb reality."); n += 1

    X.cards(
        prs, "Backlog and backlog refinement", [
            ("Product backlog", "A single ordered list of everything that might be "
             "built; the product owner owns its content and order."),
            ("User stories", "Work items describing desired functionality from the "
             "user's point of view, with acceptance criteria attached."),
            ("Refinement (grooming)", "Continual work by the product owner before "
             "iteration planning to add detail, estimates and order."),
            ("Joint refinement", "Team and product owner refine together during "
             "the sprint so the next sprint starts with ready items."),
            ("Reprioritisation", "Allows reorganisation so higher-value items are "
             "completed first as the market and feedback change."),
            ("Emergent detail", "Only the top of the backlog needs full detail — "
             "the bottom stays coarse until it approaches delivery."),
        ], n, kicker=P2, accent=TEAL); n += 1

    X.table(
        prs, "Relative sizing techniques",
        ["Technique", "Scale", "How to use it"],
        [["T-shirt sizing", "XS, S, M, L, XL", "Fast, coarse sizing of a large "
          "backlog or a roadmap before any detail exists"],
         ["Story points", "Fibonacci: 1, 2, 3, 5, 8, 13, 21", "Relative measure "
          "of difficulty, effort, volume and uncertainty combined"],
         ["Planning poker", "Simultaneous reveal of point cards", "Removes anchoring "
          "bias; the discussion of outliers is the real value"],
         ["Ideal days", "Uninterrupted working days", "Intuitive for new teams but "
          "invites confusion with calendar duration"],
         ["Affinity estimation", "Silent sorting of cards by size", "Sizing 100+ "
          "backlog items in under an hour"]],
        n, kicker=P8, accent=CYAN, widths=[1.4, 1.9, 3.2],
        note="Points are relative and team-specific: 8 points on one team is not 8 "
             "points on another. Never use velocity to compare teams."); n += 1

    X.itto(
        prs, "Define Scope — ITTO",
        ["Project charter with the high-level boundaries",
         "Project management plan — the scope management plan",
         "Project documents: assumption log, requirements documentation, "
         "risk register",
         "EEFs and OPAs including prior scope statements"],
        ["Expert judgment on comparable deliverables",
         "Data analysis — alternatives analysis",
         "Decision making — multi-criteria decision analysis",
         "Interpersonal and team skills — facilitation workshops",
         "Product analysis: product breakdown, systems analysis, "
         "value engineering, value analysis"],
        ["Project scope statement — the detailed description",
         "Project document updates: assumption log, requirements "
         "documentation, RTM, stakeholder register"],
        n, kicker=P2,
        purpose="Define Scope converts a long list of requirements into a single "
                "agreed statement of what will and will not be delivered."); n += 1

    X.cards(
        prs, "Anatomy of the project scope statement", [
            ("Product scope description", "Progressively elaborated description of "
             "the characteristics of the product, service or result."),
            ("Deliverables", "Every unique verifiable product or capability "
             "required, including project management reports and documents."),
            ("Acceptance criteria", "The conditions that must be met before the "
             "deliverables will be formally accepted by the customer."),
            ("Exclusions", "Explicitly identifies what is out of scope, so "
             "stakeholder expectations are managed before delivery starts."),
            ("Constraints", "Limiting factors — fixed budget, imposed dates, "
             "mandated technology, contractual provisions."),
            ("Assumptions", "Factors treated as true without proof; each one is a "
             "risk with a friendlier name and belongs in the risk register."),
        ], n, kicker=P2, accent=BLUE); n += 1

    X.cards(
        prs, "Baselines — the approved versions you measure against", [
            ("Scope baseline", "Approved project scope statement + WBS + WBS "
             "dictionary; changed only via approved change request."),
            ("Schedule baseline", "The approved version of the schedule model, "
             "with baseline start and finish dates for each activity."),
            ("Cost baseline", "The approved time-phased budget excluding "
             "management reserve; the S-curve you track EV against."),
            ("Performance measurement baseline", "Scope + schedule + cost combined; "
             "the single reference for earned value analysis."),
            ("Why baseline at all", "Variance is meaningless without a fixed "
             "reference; an un-baselined project cannot be controlled."),
            ("Changing a baseline", "Only through integrated change control — "
             "never by quietly editing the file to match the actual."),
        ], n, kicker=P1, accent=VIOLET); n += 1

    X.process(
        prs, "Changing a baselined item — the change request route", [
            ("Raise", "Any stakeholder may raise a change request; it is logged "
             "the moment it is raised, not after it is approved."),
            ("Analyse impact", "Assess the effect on scope, schedule, cost, "
             "quality, resources and risk — never on one dimension alone."),
            ("Record", "Enter it in the change log with the impact analysis and "
             "the recommended disposition."),
            ("Decide", "The change control board approves, defers or rejects; "
             "the decision and its rationale are recorded."),
            ("Implement/update", "If approved, update the baselines and all "
             "affected documents, then communicate the change."),
        ], n, kicker=B3, accent=ROSE,
        note="A rejected change request is still a valuable artefact: it records "
             "that the request was considered, so it does not resurface as an "
             "informal expectation later in the project."); n += 1

    X.compare(
        prs, "Scope creep versus gold plating",
        ("SCOPE CREEP",
         "Uncontrolled expansion without approval",
         ["Scope or features added that were not planned or approved",
          "Usually requested by stakeholders, accepted informally by the team",
          "Impacts cost and schedule that nobody has funded",
          "Root cause is a weak or bypassed change control process",
          "Cure: an explicit scope statement plus disciplined change control"]),
        ("GOLD PLATING",
         "Extra work nobody asked for",
         ["The team delivers features the customer did not need or request",
          "Motivated by pride, boredom or a wish to delight the customer",
          "Consumes budget and introduces untested, unrequested risk",
          "Never adds value the customer will pay for or thank you for",
          "Cure: definition of done, and acceptance criteria as the ceiling"]),
        n, kicker=P2, lc=ROSE, rc=AMBER,
        footer_note="Both destroy the baseline, but the direction differs: creep "
                    "comes from outside the team, gold plating comes from inside."); n += 1

    X.compare(
        prs, "Definition of Ready versus Definition of Done",
        ("DEFINITION OF READY (DoR)",
         "What must be true before work may START",
         ["Story is written from the user's perspective with clear value",
          "Acceptance criteria are written and agreed with the product owner",
          "Dependencies identified and either resolved or scheduled",
          "The story is small enough to complete inside one iteration",
          "The team has estimated it and understands what 'done' means"]),
        ("DEFINITION OF DONE (DoD)",
         "What must be true before work is COMPLETE",
         ["Code written, peer reviewed and merged to the mainline",
          "Unit, integration and acceptance tests written and passing",
          "Documentation updated; no known defects above agreed severity",
          "Deployed to the agreed environment and demonstrated",
          "Accepted by the product owner against the acceptance criteria"]),
        n, kicker=P7, lc=CYAN, rc=TEAL,
        footer_note="DoD is the team's quality contract with itself and is the "
                    "single most effective agile defence against gold plating and "
                    "against carrying unfinished work between sprints."); n += 1

    X.itto(
        prs, "Create WBS — ITTO",
        ["Project management plan — the scope management plan",
         "Project documents: project scope statement, requirements "
         "documentation",
         "EEFs — industry-specific WBS standards",
         "OPAs — WBS templates from prior similar projects"],
        ["Expert judgment on how far to decompose",
         "Decomposition — dividing and subdividing scope into "
         "smaller, more manageable parts"],
        ["Scope baseline — scope statement + WBS + WBS dictionary",
         "Project document updates: assumption log and "
         "requirements documentation"],
        n, kicker=P2,
        purpose="The WBS is deliverable-oriented, not activity-oriented: its "
                "elements are nouns (things produced), not verbs."); n += 1

    X.process(
        prs, "Decomposition — from deliverable to work package", [
            ("Identify deliverables", "Take the deliverables and related work from "
             "the approved project scope statement."),
            ("Structure the WBS", "Organise by phase, by major deliverable, or by "
             "subproject — pick one logic and stay consistent."),
            ("Decompose downward", "Break upper components into lower-level, more "
             "detailed components with the team, not alone."),
            ("Assign codes", "Give every element a unique code of accounts "
             "identifier so cost and schedule can roll up cleanly."),
            ("Verify sufficiency", "Confirm the degree of decomposition is enough "
             "to estimate, assign and control — then stop."),
        ], n, kicker=P2, accent=BLUE,
        note="Over-decomposition is a real defect: it produces inefficient use of "
             "resources, decreased efficiency in performing the work, and a "
             "schedule so granular nobody maintains it."); n += 1

    X.cards(
        prs, "Work packages, planning packages and the 100% rule", [
            ("Work package", "The lowest level of the WBS — small enough to "
             "estimate cost and duration reliably and assign to one owner."),
            ("Control account", "A management control point where scope, budget "
             "and schedule are integrated and compared to earned value."),
            ("Planning package", "A control account component with known work but "
             "no detailed activities yet — rolling wave's placeholder."),
            ("The 100% rule", "The WBS includes 100% of the work defined by the "
             "scope, and captures all deliverables — internal and external."),
            ("Nothing extra", "Work not in the WBS is outside the project scope; "
             "this is what makes the WBS a scope-creep detector."),
            ("8/80 heuristic", "A common rule of thumb: a work package should be "
             "between 8 and 80 hours of effort. It is guidance, not doctrine."),
        ], n, kicker=P2, accent=TEAL); n += 1

    X.table(
        prs, "WBS dictionary — the detail behind each work package",
        ["Field", "Why it is there"],
        [["WBS code identifier", "Links the package to the code of accounts so cost "
          "and schedule data roll up to the right control account"],
         ["Description of work", "Removes ambiguity about what the package includes "
          "and, critically, what it excludes"],
         ["Assumptions and constraints", "Records the conditions the estimate "
          "depends on so the estimate can be challenged fairly"],
         ["Responsible organisation", "Names the accountable unit or person for the "
          "package — no orphan work"],
         ["Schedule milestones/activities", "Connects the package to the schedule "
          "model and its associated activities"],
         ["Resources required", "States the people, equipment and materials the "
          "package consumes"],
         ["Cost estimates", "The package-level cost that bottom-up rolls into the "
          "project budget"],
         ["Quality requirements and acceptance criteria", "Defines what 'complete "
          "and correct' means for this package"],
         ["Technical references / agreement information", "Points to the standards, "
          "drawings or contract clauses that govern the work"]],
        n, kicker=P2, accent=VIOLET, widths=[1.7, 4.3]); n += 1

    X.exam(
        prs, "Exam focus — scope", [
            ("A stakeholder asks for a small extra feature mid-sprint",
             "Predictive: raise a change request. Agile: add it to the product "
             "backlog for the product owner to prioritise — never mid-sprint"),
            ("The team added a feature the customer never asked for",
             "That is gold plating; it is not a benefit, it is an unapproved "
             "scope change consuming budget"),
            ("You need to know if a requirement was delivered and tested",
             "Consult the requirements traceability matrix — it links need to "
             "deliverable to test to acceptance"),
            ("A question mentions 'approved scope statement + WBS + dictionary'",
             "That combination is the definition of the scope baseline"),
            ("Work is not shown anywhere in the WBS",
             "It is out of scope. The 100% rule means the WBS contains all of the "
             "work and only the work of the project"),
        ], n, accent=ROSE); n += 1

    X.recap(
        prs, "Recap — scope planning", [
            ("Two plans first", "Plan Scope Management yields the scope management "
             "plan and the requirements management plan — process, not content."),
            ("Collect then define", "Requirements documentation and the RTM come "
             "before the project scope statement can be written."),
            ("The RTM is the spine", "It traces need to objective to deliverable "
             "to test to acceptance and status."),
            ("Prioritise explicitly", "MoSCoW, Kano and the 100-point method turn "
             "'everything is critical' into a defensible order."),
            ("The WBS is deliverables", "Decompose to work packages; the WBS "
             "dictionary carries the detail; obey the 100% rule."),
            ("Baseline and defend", "Scope baseline changes only by approved change "
             "request; watch for creep from outside and gold plating from inside."),
        ], n, accent=CYAN); n += 1
    return n


# =============================================================== schedule
def _schedule(prs, n):
    X.statement(
        prs, "Knowledge area 2 of 8 in the planning block",
        "Schedule: sequence the work, then face the maths",
        [("Derived, not chosen", "A credible schedule is calculated from scope, "
          "dependencies and resources — it is not a date you were told."),
         ("The constraint", "The critical path defines the shortest possible "
          "duration; everything else has float to spend."),
         ("Adaptive equivalent", "Agile replaces the Gantt with cadence, velocity "
          "and a prioritised backlog — but still forecasts.")],
        n, kicker=P8, accent=VIOLET); n += 1

    X.itto(
        prs, "Plan Schedule Management — ITTO",
        ["Project charter — summary milestone schedule and approval "
         "requirements",
         "Project management plan: scope baseline, development approach",
         "EEFs — organisational culture, scheduling software availability",
         "OPAs — historical schedules, templates, scheduling policies"],
        ["Expert judgment on scheduling methodology and tooling",
         "Data analysis — alternatives analysis on scheduling approaches, "
         "level of detail, durations and rolling wave horizons",
         "Meetings with the team, sponsor and the PMO"],
        ["Schedule management plan — establishes criteria and activities "
         "for developing, monitoring and controlling the schedule",
         "Defines the units of measure, accuracy, control thresholds and "
         "the rules of performance measurement"],
        n, kicker=P8,
        purpose="This plan may be formal or informal, broadly framed or highly "
                "detailed — tailored to the needs of the project."); n += 1

    X.cards(
        prs, "What the schedule management plan specifies", [
            ("Scheduling method", "Critical path method, critical chain, or an "
             "iteration-based cadence — chosen deliberately, stated explicitly."),
            ("Scheduling tool", "The software of record; if two tools exist you "
             "will eventually have two conflicting truths."),
            ("Level of accuracy", "The acceptable range for activity duration "
             "estimates, including a contingency amount."),
            ("Units of measure", "Hours, days or weeks for time; staff hours for "
             "effort — mixing them silently is a classic estimating error."),
            ("Control thresholds", "The variance that may be tolerated before an "
             "action is required — for example ±10% of planned duration."),
            ("Reporting formats", "The formats and frequency of schedule reports, "
             "and the maintenance process for the schedule model."),
        ], n, kicker=P8, accent=BLUE); n += 1

    X.compare(
        prs, "Predictive versus adaptive scheduling",
        ("PREDICTIVE (WATERFALL) SCHEDULING",
         "Activities decomposed from work packages, then sequenced",
         ["Activities broken down from work packages and put in order",
          "Dependencies, durations and resources drive the calculated dates",
          "The critical path determines the shortest possible duration",
          "Once approved and baselined, changes need a change request",
          "Presented as a Gantt chart, milestone chart or network diagram"]),
        ("ADAPTIVE (AGILE) SCHEDULING",
         "Fixed cadence, variable content, forecast by velocity",
         ["Product owner owns the product backlog and the product roadmap",
          "The roadmap shows the order features are expected to be delivered",
          "Iteration length is fixed; the content of each iteration varies",
          "Forecasts come from measured velocity, not from imposed dates",
          "Presented as a roadmap, Kanban board, burndown or burnup chart"]),
        n, kicker=P8, lc=BLUE, rc=TEAL,
        footer_note="Both start from benchmarking and historical data: comparing "
                    "against a similar product or service schedule gives a "
                    "defensible starting point before detailed analysis."); n += 1

    X.cards(
        prs, "Schedule presentation formats — choose to fit the audience", [
            ("Roadmap", "High-level, time-boxed view of themes and releases for "
             "executives who want direction rather than detail."),
            ("Gantt chart", "Bar chart of activities against a calendar; shows "
             "duration, overlap and progress at a glance."),
            ("Milestone chart", "Only zero-duration events on a timeline — the "
             "right artefact for a steering committee."),
            ("Network diagram", "Nodes and arrows showing logical dependencies; "
             "the only format that reveals the critical path."),
            ("Kanban board", "Columns per workflow stage with WIP limits — for "
             "continuous flow rather than time-boxed work."),
            ("Burndown/burnup", "Work remaining or work completed over time, "
             "compared with the ideal line for the iteration or release."),
        ], n, kicker=P8, accent=AMBER); n += 1


    X.cards(
        prs, "Kanban board mechanics", [
            ("Visualise", "Organise work into tasks on cards so the whole flow is "
             "visible to everyone, including stakeholders."),
            ("Columns as stages", "Each column is a workflow stage; tailor the "
             "stages to your actual process, not a textbook one."),
            ("Card information", "Display owner, size, blocked status and age at "
             "every stage so the board answers questions without a meeting."),
            ("WIP limits", "Cap the number of items allowed in a column; the cap "
             "is what converts a to-do list into a flow system."),
            ("Pull, not push", "Work is pulled when capacity frees up, rather than "
             "pushed onto a team already saturated."),
            ("Expose bottlenecks", "The column that keeps hitting its WIP limit is "
             "the constraint — improve there, nowhere else."),
        ], n, kicker=P8, accent=TEAL); n += 1

    X.chart(
        prs, "Burndown chart — work remaining against the ideal line",
        "line", ["Day 0", "Day 2", "Day 4", "Day 6", "Day 8", "Day 10"],
        [("Ideal remaining", [80, 64, 48, 32, 16, 0]),
         ("Actual remaining", [80, 78, 66, 55, 30, 8])],
        n, kicker=P8, accent=BLUE,
        insight=["Tracks the work to be completed in the current iteration, "
                 "measured in story points or hours.",
                 "Used to analyse variance against the ideal burndown of work "
                 "committed to during iteration planning.",
                 "A flat start then a cliff usually means work was integrated late "
                 "— a definition-of-done problem, not a capacity problem.",
                 "A line above ideal at mid-sprint is the trigger for a scope "
                 "conversation with the product owner, not overtime."]); n += 1

    X.chart(
        prs, "Burnup chart — completed work against total scope",
        "line", ["Iter 1", "Iter 2", "Iter 3", "Iter 4", "Iter 5", "Iter 6"],
        [("Total scope", [100, 100, 112, 112, 120, 120]),
         ("Work completed", [18, 39, 57, 74, 95, 118])],
        n, kicker=P8, accent=TEAL,
        insight=["Shows accumulated progress of completed work, updated after "
                 "each iteration.",
                 "Unlike a burndown, it separates the two causes of a slipping "
                 "date: slower delivery versus growing scope.",
                 "A rising top line is scope growth made visible — the single "
                 "most useful chart in a scope-creep conversation.",
                 "The intersection of the two lines is the forecast completion "
                 "point for the release."]); n += 1

    X.chart(
        prs, "Velocity — the team's measured rate of progress",
        "column", ["Iter 1", "Iter 2", "Iter 3", "Iter 4", "Iter 5", "Iter 6"],
        [("Story points completed", [18, 21, 18, 24, 22, 23])],
        n, kicker=P8, accent=VIOLET,
        insight=["Velocity is the number of story points completed during an "
                 "iteration, counted only for items meeting the definition of done.",
                 "Estimate it initially, then modify it using actuals from "
                 "subsequent iterations — never negotiate it upward.",
                 "The goal is a constant, predictable velocity from one iteration "
                 "to the next, not a rising one.",
                 "Forecast: remaining backlog points divided by average velocity "
                 "gives the number of iterations still required."]); n += 1

    X.table(
        prs, "Continuous flow metrics",
        ["Metric", "Definition", "What it tells you"],
        [["WIP (work in progress)", "Measure of work started but not yet completed",
          "High WIP means context switching and delayed value"],
         ["Lead time", "Length of time a work item takes to go through the entire "
          "process, from request to delivery", "What the customer actually "
          "experiences as responsiveness"],
         ["Cycle time", "Length of time a work item is actively being worked on",
          "Your team's execution speed once work truly starts"],
         ["Throughput", "Number of items entering or exiting the system per unit "
          "of time", "Delivery capacity — the basis for flow forecasting"],
         ["Queue time", "Lead time minus cycle time", "The waiting; usually the "
          "largest and most ignored part of lead time"]],
        n, kicker=P8, accent=CYAN, widths=[1.4, 2.7, 2.4]); n += 1

    X.formula(
        prs, "Little's Law and flow arithmetic", [
            ("Little's Law", "L = λ × W", "Average work in progress equals arrival "
             "rate times average lead time — cut WIP and lead time falls."),
            ("Average cycle time", "WIP ÷ Throughput", "If 12 items are in progress "
             "and you finish 3 per week, each takes about 4 weeks."),
            ("Flow efficiency", "Cycle time ÷ Lead time", "Typically 5-15% in "
             "knowledge work; the rest is queueing, not working."),
            ("Iterations remaining", "Backlog points ÷ Velocity", "The agile "
             "forecast — a range, using best and worst recent velocity."),
        ], n, kicker=P8, accent=AMBER,
        note="Little's Law is why WIP limits work: with throughput roughly fixed by "
             "team capacity, the only lever you control for faster delivery is "
             "starting less work at once."); n += 1

    X.itto(
        prs, "Define Activities — ITTO",
        ["Project management plan: schedule management plan, scope baseline",
         "EEFs — organisational structure, published commercial information",
         "OPAs — activity lists from prior projects, standard templates"],
        ["Expert judgment from those who will perform the work",
         "Decomposition of work packages into schedule activities",
         "Rolling wave planning for the later horizons",
         "Meetings — including team planning sessions"],
        ["Activity list — all schedule activities with scope of work",
         "Activity attributes — predecessors, successors, leads, lags, "
         "resource requirements, constraints and assumptions",
         "Milestone list — mandatory and optional milestones",
         "Change requests and plan updates"],
        n, kicker=P8,
        purpose="Work packages are nouns; activities are verbs. Define Activities "
                "is where the deliverable-oriented WBS becomes executable work."); n += 1

    X.process(
        prs, "The schedule development sequence", [
            ("Define activities", "Break each work package into the activities "
             "required to produce it."),
            ("Sequence", "Determine dependencies and precedence relationships "
             "between the activities."),
            ("Estimate durations", "Estimate each activity based on the resources "
             "assumed to be assigned to it."),
            ("Analyse the network", "Run forward and backward passes to find float "
             "and the critical path."),
            ("Optimise and baseline", "Level resources, compress if needed, then "
             "baseline the approved schedule model."),
        ], n, kicker=P8, accent=BLUE,
        note="Every one of these steps is iterative: over-allocated resources or a "
             "date constraint will send you back to re-sequence and re-estimate "
             "before you can baseline anything."); n += 1

    X.table(
        prs, "Activity dependency types",
        ["Type", "Meaning", "Action by the project manager"],
        [["Mandatory (hard logic)", "Contractually required or inherent in the "
          "nature of the work — concrete must cure before you build on it",
          "Must schedule it; there is no way around this sequence"],
         ["Discretionary (soft logic)", "Established because of best practice or "
          "because a specific sequence is preferred",
          "Can be changed; the first place to look when compressing"],
         ["External", "Relationship between a project activity and a non-project "
          "activity, such as a regulator's approval",
          "Outside your control; manage as a risk and monitor closely"],
         ["Internal", "Relationship between two project activities, generally "
          "inside the team's control",
          "Within the team's control; re-sequence freely if it helps"]],
        n, kicker=P8, accent=VIOLET, widths=[1.5, 2.7, 2.3],
        note="Dependencies combine: a dependency can be mandatory-external "
             "(a legally required inspection) or discretionary-internal "
             "(a preferred build order). Name both attributes."); n += 1

    X.itto(
        prs, "Sequence Activities — ITTO",
        ["Project management plan: schedule management plan, scope baseline",
         "Project documents: activity list and attributes, assumption log, "
         "milestone list",
         "EEFs — government standards, scheduling tools, PMIS",
         "OPAs — existing schedule methodology and network templates"],
        ["Precedence diagramming method (PDM)",
         "Dependency determination and integration — mandatory, "
         "discretionary, external, internal",
         "Leads and lags",
         "Project management information system (PMIS)"],
        ["Project schedule network diagram — the logical flow",
         "Project document updates: activity attributes, activity list, "
         "assumption log, milestone list"],
        n, kicker=P8,
        purpose="Sequencing produces logic, not dates. Dates only appear after "
                "durations are estimated and the network is analysed."); n += 1

    X.table(
        prs, "Precedence relationships in the PDM",
        ["Relationship", "Rule", "Everyday example"],
        [["Finish-to-Start (FS)", "The successor cannot start until the predecessor "
          "finishes", "Testing cannot start until the build is finished — by far "
          "the most common"],
         ["Start-to-Start (SS)", "The successor cannot start until the predecessor "
          "starts", "Pouring concrete starts once levelling starts, running in "
          "parallel behind it"],
         ["Finish-to-Finish (FF)", "The successor cannot finish until the "
          "predecessor finishes", "Document writing cannot finish until testing "
          "finishes"],
         ["Start-to-Finish (SF)", "The successor cannot finish until the "
          "predecessor starts", "The old shift cannot end until the new shift "
          "starts — rare, appears on the exam"]],
        n, kicker=P8, accent=TEAL, widths=[1.5, 2.3, 2.7],
        note="Memory aid: name the PREDECESSOR's end first, then the SUCCESSOR's "
             "end. Start-to-Finish is the only one that feels backwards, which is "
             "exactly why it is examined."); n += 1

    X.compare(
        prs, "Leads versus lags",
        ("LEAD — BRING IT FORWARD",
         "Accelerates the successor; shown as a negative value",
         ["The amount of time a successor activity can be advanced",
          "Example: start writing training material two weeks before build ends",
          "Written as FS minus 2 weeks on the network diagram",
          "Used to compress a schedule by overlapping activities",
          "Adds risk: you are working on an unfinished predecessor"]),
        ("LAG — DELAY IT",
         "Delays the successor; shown as a positive value",
         ["The amount of time a successor activity must be delayed",
          "Example: concrete must cure for 7 days before the next activity",
          "Written as FS plus 7 days on the network diagram",
          "Represents mandatory waiting, not slack or float",
          "Cannot usually be removed — it is physics or contract, not choice"]),
        n, kicker=P8, lc=CYAN, rc=AMBER,
        footer_note="Do not confuse lag with float. Lag is designed waiting inside "
                    "the logic; float is calculated flexibility that falls out of "
                    "the network analysis."); n += 1

    X.itto(
        prs, "Estimate Activity Durations — ITTO",
        ["Project management plan: schedule management plan, scope baseline",
         "Project documents: activity list and attributes, assumption log, "
         "lessons learned register, milestone list, resource requirements, "
         "resource calendars, risk register",
         "EEFs — productivity metrics, published commercial information",
         "OPAs — historical duration information, calendars, scheduling method"],
        ["Expert judgment from the people doing the work",
         "Analogous estimating — top-down from a similar past activity",
         "Parametric estimating — a rate times a quantity",
         "Three-point estimating — optimistic, most likely, pessimistic",
         "Bottom-up estimating — aggregate the detailed components",
         "Data analysis: alternatives analysis, reserve analysis",
         "Decision making and meetings"],
        ["Duration estimates — quantitative assessments, with ranges",
         "Basis of estimates — assumptions, constraints, confidence level",
         "Project document updates"],
        n, kicker=P8,
        purpose="Duration is not effort: 40 hours of effort by one half-time person "
                "is a two-week duration."); n += 1

    X.table(
        prs, "Duration and cost estimating techniques compared",
        ["Technique", "How it works", "Accuracy and cost"],
        [["Expert judgment", "Ask the team or the people who will do the work, "
          "using their experience of similar tasks", "Fast; quality depends "
          "entirely on the expert's relevance"],
         ["Analogous (top-down)", "Use a similar past project, product or system as "
          "the analogy and scale it", "Fast and cheap; lowest accuracy — used "
          "early when little detail exists"],
         ["Parametric", "Multiply a unit rate by a quantity — $55 per metre, "
          "8 hours per drawing", "More accurate than analogous if the historical "
          "data is genuinely comparable"],
         ["Three-point (PERT)", "Weighted average of optimistic, most likely and "
          "pessimistic estimates", "Accounts for uncertainty and reduces "
          "single-point optimism bias"],
         ["Bottom-up", "Estimate each work package and aggregate upward through "
          "the WBS", "Most accurate but the most time-consuming and costly"]],
        n, kicker=P8, accent=BLUE, widths=[1.4, 2.7, 2.4]); n += 1

    X.formula(
        prs, "Three-point estimating — PERT arithmetic", [
            ("Triangular (simple average)", "(O + M + P) / 3", "Equal weight to all "
             "three points; used when the distribution is genuinely unknown."),
            ("Beta / PERT", "(O + 4M + P) / 6", "Weights the most likely estimate "
             "four times; the PMI default for three-point estimating."),
            ("Standard deviation", "(P - O) / 6", "The spread of the estimate — a "
             "large sigma is a signal to decompose further."),
            ("Variance", "((P - O) / 6)²", "Variances are additive along a path; "
             "standard deviations are not. Sum variances, then square-root."),
        ], n, kicker=P8, accent=AMBER,
        note="O = optimistic, M = most likely, P = pessimistic. Worked example: "
             "O=6, M=10, P=20 gives PERT = (6 + 40 + 20)/6 = 11 days, with "
             "sigma = (20-6)/6 = 2.33 days."); n += 1


    X.itto(
        prs, "Develop Schedule — ITTO",
        ["Project management plan: schedule management plan, scope baseline",
         "Project documents: activity list and attributes, assumption log, "
         "basis of estimates, duration estimates, milestone list, network "
         "diagram, resource calendars and requirements, risk register",
         "Agreements, EEFs and OPAs"],
        ["Schedule network analysis",
         "Critical path method (CPM)",
         "Resource optimisation — levelling and smoothing",
         "Data analysis: what-if scenario analysis, simulation (Monte Carlo)",
         "Leads and lags",
         "Schedule compression — crashing and fast tracking",
         "PMIS and agile release planning"],
        ["Schedule baseline — the approved version of the schedule model",
         "Project schedule — with planned dates for each activity",
         "Schedule data and project calendars",
         "Change requests and project document updates"],
        n, kicker=P8,
        purpose="Develop Schedule is iterative — you will loop through analysis, "
                "optimisation and compression before anything is baselined."); n += 1

    X.formula(
        prs, "Float and critical path arithmetic", [
            ("Total float", "LS − ES  (or LF − EF)", "How long an activity can slip "
             "without delaying the project end date."),
            ("Free float", "ES(successor) − EF(activity) − 1", "How long an activity "
             "can slip without delaying its earliest successor."),
            ("Critical path", "The path with zero total float", "The longest path "
             "through the network and therefore the shortest project duration."),
            ("Project float", "Imposed date − Calculated finish", "Slack against an "
             "externally imposed deadline; can be negative."),
        ], n, kicker=P8, accent=CYAN,
        note="Negative total float means the network cannot meet the imposed date "
             "as sequenced — the trigger for schedule compression, not for "
             "quietly changing the finish date in the tool."); n += 1

    X.process(
        prs, "Forward and backward pass — calculating the network", [
            ("Forward pass", "Move left to right computing Early Start and Early "
             "Finish: EF = ES + Duration − 1."),
            ("Take the maximum", "Where paths merge, the successor's ES is the "
             "LARGEST EF of its predecessors — the latest gate governs."),
            ("Backward pass", "Move right to left computing Late Finish and Late "
             "Start: LS = LF − Duration + 1."),
            ("Take the minimum", "Where paths diverge, the predecessor's LF is the "
             "SMALLEST LS of its successors."),
            ("Compute float", "Total float = LS − ES. Activities with zero float "
             "form the critical path."),
        ], n, kicker=P8, accent=ROSE,
        note="Exam discipline: a network can have more than one critical path, and "
             "the critical path can change during execution as actuals come in. "
             "Recalculate; never assume it is fixed."); n += 1

    X.compare(
        prs, "Schedule compression — crashing versus fast tracking",
        ("CRASHING",
         "Add resources to critical path activities",
         ["Adds cost to buy back duration on the critical path only",
          "Overtime, extra staff, paying to expedite deliveries",
          "Subject to diminishing returns — nine women, one month",
          "Always increases cost; may increase risk through fatigue",
          "Choose the activity with the lowest cost per day saved"]),
        ("FAST TRACKING",
         "Overlap activities normally done in sequence",
         ["Converts finish-to-start logic into overlap or start-to-start",
          "Costs nothing directly — you pay in risk instead",
          "Only discretionary dependencies can be fast tracked",
          "Increases rework risk: the predecessor may still change",
          "Try fast tracking first, then crash what remains"]),
        n, kicker=P8, lc=AMBER, rc=CYAN,
        footer_note="Neither technique changes scope. If compression cannot recover "
                    "the date, the correct move is to escalate the trade-off, not "
                    "to silently reduce quality."); n += 1

    X.exam(
        prs, "Exam focus — schedule", [
            ("The question gives a network diagram and asks for the shortest "
             "duration", "That is the critical path — the longest path through "
             "the network, with zero float"),
            ("You need to shorten the schedule without adding cost",
             "Fast track by overlapping discretionary dependencies; crashing "
             "always costs money"),
            ("An activity has 5 days of total float and slips 3 days",
             "The project end date is unaffected; only floats downstream change"),
            ("Concrete must cure for 7 days before the next activity",
             "That is a mandatory dependency with a 7-day lag, not float"),
            ("The team's velocity is 20 points and 100 points remain",
             "Forecast roughly 5 more iterations — express it as a range using "
             "best and worst recent velocity"),
        ], n, accent=ROSE); n += 1

    X.recap(
        prs, "Recap — schedule planning", [
            ("Six processes", "Plan Schedule Management, Define Activities, "
             "Sequence, Estimate Durations, Develop Schedule, Control Schedule."),
            ("Logic before dates", "Sequencing produces a network diagram; dates "
             "only exist after durations and network analysis."),
            ("Four dependencies", "Mandatory, discretionary, external, internal — "
             "and they combine into pairs."),
            ("Four relationships", "FS is the default; SS and FF enable overlap; "
             "SF is rare and examined."),
            ("Float is calculated", "Total float protects the end date; free float "
             "protects the successor; zero float is critical."),
            ("Agile still forecasts", "Velocity, burndown, burnup and flow metrics "
             "replace the Gantt but do the same forecasting job."),
        ], n, accent=CYAN); n += 1
    return n


# =================================================================== cost
def _cost(prs, n):
    X.statement(
        prs, "Knowledge area 3 of 8 in the planning block",
        "Cost: estimate honestly, then fund the uncertainty",
        [("Estimate", "Determine the approximate monetary resources needed to "
          "complete each activity and work package."),
         ("Budget", "Aggregate those estimates into an authorised, time-phased "
          "cost baseline you can measure against."),
         ("Reserve", "Fund the known-unknowns and the unknown-unknowns "
          "separately — they have different owners.")],
        n, kicker=P6, accent=AMBER); n += 1

    X.itto(
        prs, "Plan Cost Management — ITTO",
        ["Project charter — summary budget and approval requirements",
         "Project management plan: schedule and risk management plans",
         "EEFs — exchange rates, market conditions, financial controls",
         "OPAs — financial policies, historical cost data, estimating templates"],
        ["Expert judgment on financial management and estimating",
         "Data analysis — alternatives analysis on funding, make-or-buy, "
         "and on how to acquire project resources",
         "Meetings with sponsor, finance and the PMO"],
        ["Cost management plan — units of measure, precision, accuracy, "
         "organisational procedure links (control accounts / code of accounts)",
         "Control thresholds and rules of performance measurement (EVM)",
         "Reporting formats and process descriptions"],
        n, kicker=P6,
        purpose="Set the rules of the money before you produce a number — "
                "otherwise nobody agrees what the number means."); n += 1

    X.itto(
        prs, "Estimate Costs — ITTO",
        ["Project management plan: cost and quality management plans, "
         "scope baseline",
         "Project documents: lessons learned register, project schedule, "
         "resource requirements, risk register",
         "EEFs — market conditions, published commercial information",
         "OPAs — cost estimating policies and templates, historical data"],
        ["Expert judgment",
         "Analogous estimating",
         "Parametric estimating",
         "Bottom-up estimating",
         "Three-point estimating",
         "Data analysis: alternatives analysis, reserve analysis, "
         "cost of quality",
         "Project management information system and decision making (voting)"],
        ["Cost estimates for each activity, including contingency",
         "Basis of estimates — assumptions, constraints, range, confidence",
         "Project document updates"],
        n, kicker=P6,
        purpose="Cost estimates are a prediction with a range and a confidence "
                "level, never a single number stated as fact."); n += 1

    X.cards(
        prs, "The four cost estimating methods in detail", [
            ("Analogous estimating", "Uses historical information and expert "
             "judgment from a previous similar project; pick the next closest "
             "project when an exact match does not exist."),
            ("When to use analogous", "Low cost and quick — the right choice very "
             "early when detail is scarce and a rough order of magnitude is "
             "all that is needed."),
            ("Parametric estimating", "Takes variables from historical data and "
             "applies them: cost = number of resistors × cost per resistor, or "
             "rate per operator × number of operators."),
            ("When to use parametric", "When there is a genuine linear driver and "
             "credible historical data; scales far better than analogous."),
            ("Bottom-up estimating", "Rolls costs up from the smallest activity "
             "upward, using the WBS to structure the estimates."),
            ("When to use bottom-up", "The most accurate method but the most time "
             "consuming and costly; used once the WBS is complete."),
            ("Three-point estimating", "Uses a weighted average of three estimates "
             "to reduce bias and represent uncertainty explicitly."),
            ("When to use three-point", "Whenever a single number would hide real "
             "uncertainty — especially for novel or high-risk work."),
        ], n, kicker=P6, accent=BLUE, cols=4); n += 1

    X.formula(
        prs, "Three-point cost estimating", [
            ("Beta / PERT cost", "Ce = (Co + 4Cm + Cp) / 6", "Ce estimated cost, Co "
             "optimistic, Cm most likely, Cp pessimistic."),
            ("Triangular cost", "Ce = (Co + Cm + Cp) / 3", "Used when there is no "
             "reason to weight the most likely value more heavily."),
            ("Cost standard deviation", "σ = (Cp − Co) / 6", "The spread; quote "
             "Ce ± 2σ to give the sponsor a 95% range."),
            ("Range example", "O=80k, M=100k, P=180k", "PERT = (80 + 400 + 180)/6 = "
             "$110k, σ = $16.7k, so 95% range is roughly $77k to $143k."),
        ], n, kicker=P6, accent=TEAL); n += 1

    X.itto(
        prs, "Determine Budget — ITTO",
        ["Project management plan: cost management plan, resource management "
         "plan, scope baseline",
         "Project documents: basis of estimates, cost estimates, project "
         "schedule, risk register",
         "Business documents: business case and benefits management plan",
         "Agreements, EEFs and OPAs"],
        ["Expert judgment",
         "Cost aggregation — roll work package costs to control accounts",
         "Data analysis — reserve analysis",
         "Historical information review",
         "Funding limit reconciliation",
         "Financing"],
        ["Cost baseline — the approved time-phased budget, excluding "
         "management reserve",
         "Project funding requirements — total and periodic, including "
         "expected expenditure and liabilities",
         "Project document updates"],
        n, kicker=P6,
        purpose="The cost baseline is the S-curve. Management reserve sits above "
                "it and forms the total project budget."); n += 1

    X.chart(
        prs, "The cost baseline S-curve and the funding steps",
        "line", ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8"],
        [("Cumulative cost baseline", [40, 110, 230, 420, 640, 810, 910, 950]),
         ("Funding requirements", [200, 200, 400, 600, 800, 1000, 1000, 1000])],
        n, kicker=P6, accent=VIOLET,
        insight=["The cost baseline is time-phased: it says not only how much, but "
                 "when the money is expected to be spent.",
                 "Cumulative spend follows an S-curve — slow at first, steep in "
                 "execution, flattening at closure.",
                 "Funding arrives in steps, usually quarterly; funding limit "
                 "reconciliation aligns the smooth curve to the steps.",
                 "The gap between the funding line and the baseline is the "
                 "management reserve plus the funding buffer."]); n += 1

    X.compare(
        prs, "Contingency reserve versus management reserve",
        ("CONTINGENCY RESERVE",
         "For identified risks — the known-unknowns",
         ["Set aside to deal with identified risks should they occur",
          "Calculated from quantitative risk analysis or EMV of the register",
          "INCLUDED in the cost baseline and in the schedule baseline",
          "The project manager may spend it without a change request",
          "Reserve analysis reports risk remaining versus contingency remaining"]),
        ("MANAGEMENT RESERVE",
         "For unidentified risks — the unknown-unknowns",
         ["Set aside for unforeseen work that is still within project scope",
          "Typically a management-set percentage of the total baseline",
          "EXCLUDED from the cost baseline; part of the total project budget",
          "Requires management approval to access — usually a change request",
          "Using it changes the cost baseline; using contingency does not"]),
        n, kicker=P6, lc=TEAL, rc=ROSE,
        footer_note="Total project budget = cost baseline + management reserve. "
                    "Cost baseline = work package costs + contingency reserve. "
                    "This distinction is examined heavily."); n += 1

    X.cards(
        prs, "ECO 2026 emphasis — managing financial reserves", [
            ("Quantify allocations", "Quantify risk and contingency financial "
             "allocations explicitly rather than adding a round percentage."),
            ("Plan spend tracking", "Design how spend will be tracked across the "
             "whole life cycle before the first invoice arrives."),
            ("Plan financial reporting", "Agree the format, frequency and audience "
             "of financial reporting with finance and the sponsor."),
            ("Anticipate challenges", "Look ahead for funding gaps, exchange rate "
             "exposure, and cost inflation on long-lead procurement."),
            ("Monitor variation", "Work with the governance process when financial "
             "variations exceed the agreed control threshold."),
            ("Release unused reserve", "Reserves for risks that have passed should "
             "be returned, not quietly absorbed into the project."),
        ], n, kicker=P6, accent=AMBER); n += 1


    X.exam(
        prs, "Exam focus — cost", [
            ("A risk in the register occurs and you need funds",
             "Use the contingency reserve — no change request needed, it is "
             "already inside the cost baseline"),
            ("Unforeseen in-scope work appears that nobody identified",
             "Request management reserve through management approval; this "
             "changes the cost baseline"),
            ("You need a quick figure with almost no detail available",
             "Analogous estimating — fast and cheap, lowest accuracy"),
            ("The question gives O, M and P values",
             "Apply (O + 4M + P) / 6 unless the question explicitly says "
             "triangular or simple average"),
            ("You are asked for the total project budget",
             "Cost baseline plus management reserve — the baseline alone is "
             "not the budget"),
        ], n, accent=ROSE); n += 1

    X.recap(
        prs, "Recap — cost planning", [
            ("Rules first", "The cost management plan sets units, precision, "
             "thresholds and the EVM rules before any number is produced."),
            ("Four methods", "Analogous, parametric, bottom-up and three-point — "
             "trading speed against accuracy."),
            ("PERT", "(O + 4M + P) / 6 with σ = (P − O) / 6 turns a guess into a "
             "range with a stated confidence."),
            ("Aggregate to baseline", "Work packages roll to control accounts, then "
             "to the time-phased cost baseline S-curve."),
            ("Two reserves", "Contingency is inside the baseline for known risks; "
             "management reserve sits outside it for unknown ones."),
            ("Reconcile funding", "Funding limit reconciliation aligns the smooth "
             "spend curve to the stepped release of actual funds."),
        ], n, accent=CYAN); n += 1
    return n


# ================================================================ quality
def _quality(prs, n):
    X.statement(
        prs, "Knowledge area 4 of 8 in the planning block",
        "Quality: how well deliverables meet requirements",
        [("Quality vs grade", "Quality is conformance to requirements; grade is the "
          "category of features. Low grade can be acceptable; low quality never is."),
         ("Prevention over inspection", "It is always cheaper to design defects out "
          "than to inspect and rework them later."),
         ("Everyone's job", "In agile the whole team owns quality, from writing "
          "correct requirements to automated testing.")],
        n, kicker=P7, accent=ROSE); n += 1

    X.compare(
        prs, "Quality in predictive versus agile delivery",
        ("PREDICTIVE QUALITY",
         "Build, then test — usually in large batches",
         ["The product is developed and then tested in sequential order",
          "Testing is a distinct phase performed by a separate QA function",
          "Defects are found late, when they are most expensive to fix",
          "Formal quality audits and phase gate reviews provide assurance",
          "Acceptance is a single formal event near the end"]),
        ("AGILE QUALITY",
         "Build quality in, continuously",
         ["Quality is everyone's responsibility, from requirement to release",
          "Test-driven development and automated regression on every commit",
          "Definition of done enforces quality before a story is accepted",
          "Continuous integration finds integration defects within hours",
          "Acceptance happens every iteration at the review"]),
        n, kicker=P7, lc=BLUE, rc=TEAL,
        footer_note="Both approaches tie quality to the product acceptance criteria "
                    "described in the statement of work or design documents — "
                    "update those criteria as experimentation and prioritisation "
                    "occur, then validate them at acceptance."); n += 1

    X.itto(
        prs, "Plan Quality Management — ITTO",
        ["Project charter — high-level requirements and success criteria",
         "Project management plan: requirements, risk and stakeholder "
         "engagement plans, and the scope baseline",
         "Project documents: assumption log, requirements documentation, "
         "RTM, risk register, stakeholder register",
         "EEFs — regulations, rules, standards and geographic conditions",
         "OPAs — quality policy, historical databases, lessons learned"],
        ["Expert judgment on quality assurance and control",
         "Data gathering: benchmarking, brainstorming, interviews",
         "Data analysis: cost-benefit analysis, cost of quality",
         "Decision making: multi-criteria decision analysis",
         "Data representation: flowcharts, logical data model, matrix "
         "diagrams, mind mapping",
         "Test and inspection planning; meetings"],
        ["Quality management plan — how standards will be implemented",
         "Quality metrics — the specific attribute and how it is measured",
         "Project management plan updates and document updates"],
        n, kicker=P7,
        purpose="Plan Quality Management defines what good looks like and how it "
                "will be proven, before any deliverable exists."); n += 1

    X.cards(
        prs, "The quality management plan and its benefits", [
            ("What it contains", "The activities and resources that will achieve "
             "the quality objectives, and who is accountable for each."),
            ("How formal", "May be formal or informal, highly detailed or broadly "
             "framed — tailored to the project's risk and regulatory context."),
            ("Living document", "Reviewed throughout the project as the product and "
             "the risk profile change."),
            ("Sharper value focus", "Forces the team to state what the customer "
             "actually values, rather than what is easy to measure."),
            ("Cost reduction", "Prevention and appraisal spend consistently costs "
             "less than the failure costs it avoids."),
            ("Fewer schedule overruns", "Most predictive schedule overrun is "
             "rework; designing rework out protects the date."),
        ], n, kicker=P7, accent=VIOLET); n += 1

    X.table(
        prs, "Cost of Quality (CoQ) — the four categories",
        ["Category", "Definition", "Typical spend"],
        [["Prevention (conformance)", "The cost to prevent future defects or errors "
          "in the product", "Training, prototypes, code refactoring, design "
          "reviews, standards, tooling"],
         ["Appraisal (conformance)", "The cost to find defects or errors in the "
          "product", "Testing, quality audits, inspections, the sprint review, "
          "destructive test loss"],
         ["Internal failure (non-conformance)", "Failure found by the project, "
          "before the customer sees it", "Rework, scrap, re-testing, defect "
          "triage, schedule slip"],
         ["External failure (non-conformance)", "Failure found by the customer, "
          "after delivery", "Warranty work, recalls, liability, lost business, "
          "reputational damage"]],
        n, kicker=P7, accent=AMBER, widths=[1.7, 2.4, 2.4],
        note="Cost of conformance (prevention + appraisal) is money spent during "
             "the project to avoid failure. Cost of non-conformance is money spent "
             "during and after the project because you did not."); n += 1

    X.chart(
        prs, "The cost of change curve — quality is cheapest early",
        "column", ["Requirements", "Design", "Build", "System test", "Production"],
        [("Relative cost to fix one defect", [1, 5, 10, 25, 100])],
        n, kicker=P7, accent=ROSE,
        insight=["Quality is more expensive to fix the closer it gets to the "
                 "customer — the classic 1:100 relationship.",
                 "This curve is the economic justification for prevention spend, "
                 "code review and test automation.",
                 "It is also the argument for short iterations: shorter feedback "
                 "loops keep you at the cheap end of the curve.",
                 "Project risk follows exactly the same curve — early treatment "
                 "is dramatically cheaper than late response."]); n += 1

    X.process(
        prs, "PDCA — the Deming/Shewhart improvement cycle", [
            ("Plan", "Review real data or go and see the problem directly; find "
             "the root cause, then brainstorm and prioritise solutions with "
             "the team."),
            ("Do", "Put the plan into action as a pilot or test in a small area "
             "first, so a failed idea is cheap."),
            ("Check", "Check the results against what you predicted, using the "
             "same measure you baselined."),
            ("Act", "Adopt, adapt or abandon — standardise what worked, then "
             "start the next turn of the cycle."),
        ], n, kicker=P7, accent=TEAL,
        note="PDCA is a cycle, not a project: the value comes from turning it "
             "repeatedly and quickly, not from executing it perfectly once."); n += 1

    X.process(
        prs, "DMAIC — the Six Sigma improvement framework", [
            ("Define", "Define the problem clearly, as the gap between where you "
             "are and where you want to be."),
            ("Measure", "Measure the current problem with real data, not with "
             "opinion or recollection."),
            ("Analyse", "Analyse the data, find the root cause, then brainstorm "
             "and prioritise solutions with the team."),
            ("Improve", "Put the plan into action and measure whether the gap "
             "actually closed."),
            ("Control", "Lock the gain in with standards, monitoring and control "
             "charts so the problem cannot quietly return."),
        ], n, kicker=P7, accent=BLUE,
        note="Six Sigma focuses on removing variation and waste. Kaizen — 'change "
             "for better' — is the complementary philosophy of many small "
             "continuous improvements made by the people doing the work."); n += 1

    X.cards(
        prs, "Root cause analysis toolkit", [
            ("Fishbone / Ishikawa", "A cause-and-effect diagram grouping candidate "
             "causes into categories around a single problem statement."),
            ("The 6M categories", "Manpower, Method, Machine, Material, "
             "Measurement, Mother Nature — the classic manufacturing spine."),
            ("Five Whys", "Ask 'why' repeatedly to drill from the visible symptom "
             "down to the systemic cause that actually needs fixing."),
            ("Pareto chart", "Ranks defect categories by frequency to find the "
             "vital few driving most of the pain."),
            ("Six Thinking Hats", "De Bono's method: examine a situation "
             "deliberately from six distinct thinking modes in turn."),
            ("Control chart", "Plots a process against control limits over time to "
             "separate special-cause signal from common-cause noise."),
        ], n, kicker=P7, accent=VIOLET); n += 1


    X.chart(
        prs, "Pareto chart — the vital few defect categories",
        "column", ["Data entry", "Interface", "Validation", "Timeout",
                   "Formatting", "Other"],
        [("Defect count", [88, 54, 31, 14, 9, 4])],
        n, kicker=P7, accent=AMBER,
        insight=["The 80/20 rule: roughly 80% of the defects come from roughly "
                 "20% of the causes.",
                 "Directs improvement effort where it makes the biggest impact, "
                 "instead of spreading it evenly across every category.",
                 "Takes a big vague problem ('quality is poor') and breaks it into "
                 "actionable, countable pieces.",
                 "Re-run after the improvement: the bars should shrink and the "
                 "ranking should change."]); n += 1

    X.cards(
        prs, "Quality standards, regulations and compliance", [
            ("ASQ", "The American Society for Quality — steward of the ISO 9000 "
             "series quality management standards."),
            ("Chartered Quality Institute", "The UK professional body for quality "
             "practitioners and quality management systems."),
            ("ASTM International", "Publishes technical standards for materials, "
             "products, systems and services across industries."),
            ("Government regulation", "Appropriate government regulations are "
             "mandatory inputs, not optional quality aspirations."),
            ("Organisational policies", "Internal quality policy and product "
             "standards constrain what 'acceptable' can mean."),
            ("Compliance actions", "Classify compliance categories, determine "
             "threats to compliance, analyse the consequences of non-compliance."),
        ], n, kicker=cd.eco("Business Environment", 2), accent=TEAL); n += 1

    X.cards(
        prs, "ECO 2026 emphasis — sustainability in quality planning", [
            ("Sustainability as a requirement", "Environmental and social criteria "
             "are gathered as quality requirements, not treated as PR."),
            ("Measure it", "Define metrics — energy per transaction, waste "
             "diverted, carbon per deliverable — and baseline them like any other."),
            ("Cost of quality extension", "Environmental failure cost (remediation, "
             "penalties, disposal) belongs in the non-conformance column."),
            ("Design out waste", "Prevention applies to material and energy waste "
             "exactly as it applies to defects."),
            ("Regulatory exposure", "Sustainability reporting obligations are "
             "compliance requirements with real legal consequence."),
            ("AI-assisted review", "AI tools can scan designs and specifications "
             "for waste and compliance gaps — the human still decides."),
        ], n, kicker=P7, accent=BLUE); n += 1

    X.exam(
        prs, "Exam focus — quality", [
            ("The team wants to inspect more to raise quality",
             "Prefer prevention over inspection — the cheapest defect is the one "
             "never created"),
            ("A customer reports a defect after handover",
             "That is an external failure cost — the most expensive category of "
             "cost of non-conformance"),
            ("You must find why a defect keeps recurring",
             "Root cause analysis: five whys or an Ishikawa diagram — treat the "
             "cause, not the symptom"),
            ("Many defect categories; limited improvement budget",
             "Build a Pareto chart and attack the vital few that produce most of "
             "the defects"),
            ("The product meets all specifications but is low-featured",
             "That is low grade with high quality — acceptable if agreed; low "
             "quality never is"),
        ], n, accent=ROSE); n += 1

    X.recap(
        prs, "Recap — quality planning", [
            ("Quality is conformance", "How well the deliverable meets the "
             "requirement — distinct from grade, which is feature category."),
            ("Plan it", "The quality management plan states standards, metrics, "
             "roles and review activity before delivery starts."),
            ("Four CoQ buckets", "Prevention and appraisal are conformance; "
             "internal and external failure are non-conformance."),
            ("Cost of change curve", "Defect fix cost rises roughly 1:100 from "
             "requirements to production — buy prevention."),
            ("Improvement cycles", "PDCA and DMAIC give a repeatable structure; "
             "Kaizen supplies the culture of small continuous change."),
            ("RCA toolkit", "Fishbone, five whys, Pareto, Six Thinking Hats and "
             "control charts — pick the tool that fits the data you have."),
        ], n, accent=CYAN); n += 1
    return n


# ============================================================== resources
def _resources(prs, n):
    X.statement(
        prs, "Knowledge area 5 of 8 in the planning block",
        "Resources: people and things, planned deliberately",
        [("Team resources", "The people who will do the work, their roles, "
          "authority, responsibility and required competency."),
         ("Physical resources", "Materials, equipment, facilities and "
          "infrastructure that must be acquired and released."),
         ("The constraint", "Resource availability, not activity duration, is "
          "what most often determines the real schedule.")],
        n, kicker=P4, accent=CYAN); n += 1

    X.itto(
        prs, "Plan Resource Management — ITTO",
        ["Project charter — high-level roles and sponsor commitment",
         "Project management plan: quality management plan, scope baseline",
         "Project documents: project schedule, requirements documentation, "
         "risk register, stakeholder register",
         "EEFs — organisational structure, existing resources, marketplace",
         "OPAs — HR policies, safety policies, templates, historical data"],
        ["Expert judgment on resourcing and organisational design",
         "Data representation: hierarchical charts, responsibility "
         "assignment matrix (RAM/RACI), text-oriented formats",
         "Organisational theory (Tuckman, Maslow, Herzberg, McGregor)",
         "Meetings with functional managers and the team"],
        ["Resource management plan — how resources are identified, "
         "acquired, managed and released",
         "Team charter — team values, agreements and operating guidelines",
         "Project document updates: assumption log, risk register"],
        n, kicker=P4,
        purpose="This plan covers physical resources and team resources — most "
                "exam errors come from forgetting the physical half."); n += 1

    X.table(
        prs, "Role definition — the four attributes",
        ["Attribute", "Definition", "What goes wrong if it is vague"],
        [["Role", "A person's designated function on the project — business "
          "analyst, test lead, architect", "People duplicate work or assume "
          "someone else is covering a gap"],
         ["Authority", "The right to apply resources, make decisions, sign "
          "approvals and accept deliverables", "Decisions stall waiting for "
          "someone who never had the mandate"],
         ["Responsibility", "The assigned duties a role must perform to complete "
          "project activities", "Work is 'everybody's job' and therefore "
          "nobody's job"],
         ["Competency", "The skill and capacity required to complete the assigned "
          "activities within the constraints", "Work is assigned to people who "
          "cannot succeed at it — a schedule risk, not a people problem"]],
        n, kicker=P4, accent=BLUE, widths=[1.2, 2.7, 2.6]); n += 1

    X.compare(
        prs, "Resource optimisation — levelling versus smoothing",
        ("RESOURCE LEVELLING",
         "Fix over-allocation; the end date may move",
         ["Applied when shared resources are over-allocated",
          "Or when a resource is assigned to two or more activities in the "
          "same period",
          "Adjusts start and finish dates based on resource constraints",
          "CAN change the critical path — usually extending it",
          "Use when the resource limit is genuinely hard (one specialist)"]),
        ("RESOURCE SMOOTHING",
         "Even out demand; the end date is protected",
         ["Adjusts activities only within their free and total float",
          "The critical path is NOT changed by smoothing",
          "Cannot fully resolve a genuine over-allocation",
          "Produces a more even resource demand profile over time",
          "Use when the date is fixed and float is available to spend"]),
        n, kicker=P4, lc=TEAL, rc=VIOLET,
        footer_note="Memory hook: LEVELLING may LENGTHEN the project; SMOOTHING "
                    "Stays inside Slack. If the question says the end date must "
                    "not move, the answer is smoothing."); n += 1

    X.itto(
        prs, "Estimate Activity Resources — ITTO",
        ["Project management plan: resource management plan, scope baseline",
         "Project documents: activity attributes and list, assumption log, "
         "cost estimates, resource calendars, risk register",
         "EEFs — resource location, availability, skills, marketplace",
         "OPAs — policies on staffing and equipment, historical information"],
        ["Expert judgment on resource types and quantities",
         "Bottom-up estimating from activity level upward",
         "Analogous and parametric estimating",
         "Data analysis — alternatives analysis (make/rent/buy, skill mix)",
         "Project management information system and meetings"],
        ["Resource requirements — types and quantities per work package",
         "Basis of estimates — method, assumptions, confidence level",
         "Resource breakdown structure (RBS) by category and type",
         "Project document updates"],
        n, kicker=P4,
        purpose="Estimate Activity Resources runs closely with Estimate Activity "
                "Durations — the two are mutually dependent."); n += 1

    X.table(
        prs, "RACI — the responsibility assignment matrix",
        ["Letter", "Meaning", "Rule"],
        [["R — Responsible", "The person or people who actually perform the work",
          "At least one per activity; more than one is fine"],
         ["A — Accountable", "The single person answerable for the outcome, who "
          "approves the work", "EXACTLY ONE per activity — two means nobody"],
         ["C — Consulted", "People whose input is sought before the work is done; "
          "two-way communication", "Keep the list short; every C is a delay"],
         ["I — Informed", "People told about progress or outcomes; one-way "
          "communication", "Cheap to add, so it is where over-communication "
          "usually hides"]],
        n, kicker=P4, accent=AMBER, widths=[1.3, 3.0, 2.2],
        note="A responsibility assignment matrix shows which team members are "
             "responsible for which work packages. Read the ROWS to find "
             "unassigned work; read the COLUMNS to find overloaded people."); n += 1

    X.cards(
        prs, "Co-location, osmotic communication and the team charter", [
            ("Co-location", "Agile teams prefer to sit together so that "
             "coordination happens continuously rather than in scheduled meetings."),
            ("Osmotic communication", "Team members absorb useful information from "
             "overheard conversations without anyone having to brief them."),
            ("Information radiator", "A large visible display of project "
             "information in the team area — status without a status meeting."),
            ("Team charter", "Created WITH the team; it establishes values, "
             "agreements and operating guidelines the team owns."),
            ("Ground rules", "Explicit agreements on meetings, decisions, conflict "
             "and communication — enforced by the team, not just the PM."),
            ("Virtual co-location", "Persistent video rooms and shared boards "
             "recreate some osmotic benefit for distributed teams."),
        ], n, kicker=P4, accent=ROSE); n += 1

    X.exam(
        prs, "Exam focus — resources", [
            ("A key specialist is booked on two activities at the same time",
             "Resource levelling — and accept that the end date may move"),
            ("Demand is uneven but the finish date is fixed and float exists",
             "Resource smoothing — adjust only within free and total float"),
            ("Two people are marked Accountable for the same deliverable",
             "That is the defect: RACI allows exactly one Accountable per row"),
            ("The team keeps rediscovering the same information late",
             "Co-locate or add an information radiator; osmotic communication "
             "solves this without adding meetings"),
        ], n, accent=ROSE); n += 1
    return n


# ========================================================== communications
def _comms(prs, n):
    X.statement(
        prs, "Knowledge area 6 of 8 in the planning block",
        "Communication: the PM's largest single time cost",
        [("The 90% figure", "Project managers spend the overwhelming majority of "
          "their time communicating — plan it like any other work."),
         ("Planned, not ad hoc", "Who needs what, in what format, how often, "
          "through which channel, and why."),
         ("Two-way by design", "Communication without a feedback loop is "
          "broadcasting, and broadcasting is not engagement.")],
        n, kicker=PE8, accent=BLUE); n += 1

    X.itto(
        prs, "Plan Communications Management — ITTO",
        ["Project charter — key stakeholders and their roles",
         "Project management plan: resource management plan, stakeholder "
         "engagement plan",
         "Project documents: requirements documentation, stakeholder register",
         "EEFs — organisational culture, geographic distribution, "
         "regulatory and legal reporting requirements",
         "OPAs — historical information, lessons learned, templates"],
        ["Expert judgment on politics, media and cross-cultural nuance",
         "Communication requirements analysis",
         "Communication technology, models and methods",
         "Interpersonal and team skills: communication styles assessment, "
         "political awareness, cultural awareness",
         "Data representation — stakeholder engagement assessment matrix",
         "Meetings"],
        ["Communications management plan",
         "Project management plan updates and document updates "
         "(stakeholder register, project schedule)"],
        n, kicker=PE8,
        purpose="The plan defines the strategy; execution is Manage "
                "Communications and Monitor Communications."); n += 1

    X.cards(
        prs, "What the communications management plan records", [
            ("Roles", "Identifies team members and stakeholders as senders, "
             "receivers, and the authorising person for confidential information."),
            ("Type of information", "What is communicated — status, decisions, "
             "risks, escalations, financials."),
            ("Reason for communication", "Why the communication exists; a report "
             "nobody can justify is a report you can stop producing."),
            ("Language, format, detail", "Written in the audience's language and "
             "at the level of detail their decision actually requires."),
            ("Time frame and frequency", "When and how often, including "
             "escalation-triggered rather than calendar-triggered messages."),
            ("Method and technology", "The channel: meeting, dashboard, email, "
             "report — chosen for urgency and richness, not habit."),
            ("Escalation process", "The route and the thresholds for escalating "
             "an issue when the normal channel fails."),
            ("Glossary and constraints", "Common terminology, plus any legal or "
             "regulatory reporting constraints that apply."),
        ], n, kicker=PE8, accent=TEAL, cols=4); n += 1

    X.process(
        prs, "The communication model — where meaning goes missing", [
            ("Encode", "The sender converts thought into a message using words, "
             "images or gestures — meaning is already partly lost here."),
            ("Transmit", "The message travels through a medium: speech, email, "
             "chat, video, document."),
            ("Noise", "Anything distorting the signal — jargon, poor connection, "
             "cultural difference, distraction, emotion, fatigue."),
            ("Decode", "The receiver converts the message back into thought using "
             "their own frame of reference, not the sender's."),
            ("Acknowledge/feedback", "The receiver confirms receipt and "
             "understanding; only now is communication actually complete."),
        ], n, kicker=PE8, accent=VIOLET,
        note="On the exam, if a message was sent but not confirmed, communication "
             "has NOT occurred. The sender is responsible for making the message "
             "clear, complete and understood."); n += 1

    X.formula(
        prs, "Communication channels", [
            ("Channels formula", "N × (N − 1) / 2", "N is the number of people; the "
             "result is the number of potential communication paths."),
            ("Team of 10", "10 × 9 / 2 = 45", "Ten people generate forty-five "
             "possible two-way channels to keep coherent."),
            ("Adding one person", "From 10 to 11: 45 → 55", "One extra person adds "
             "ten new channels — complexity grows quadratically."),
            ("Team of 50", "50 × 49 / 2 = 1225", "Why large teams need structure, "
             "sub-teams and a plan rather than goodwill."),
        ], n, kicker=PE8, accent=AMBER,
        note="Exam trap: read carefully whether the question includes the project "
             "manager in N. If it says 'you have a team of 8', N is usually 9. If "
             "it asks for ADDITIONAL channels, subtract the original count."); n += 1

    X.table(
        prs, "Push, pull and interactive communication",
        ["Method", "How it works", "Use it for"],
        [["Interactive", "Multi-directional real-time exchange between two or more "
          "parties — meetings, calls, video, workshops",
          "Complex, sensitive, ambiguous or urgent topics needing agreement"],
         ["Push", "Sent to specific recipients who need the information — email, "
          "memos, reports, letters, voicemail",
          "Distribution where receipt matters but discussion does not"],
         ["Pull", "Recipients access the information at their discretion — "
          "intranets, dashboards, knowledge repositories, wikis",
          "Large volumes of information for large, self-serving audiences"]],
        n, kicker=PE8, accent=CYAN, widths=[1.2, 3.0, 2.4],
        note="Push guarantees distribution but NOT understanding. Only interactive "
             "communication closes the loop, which is why bad news is always "
             "delivered interactively first."); n += 1

    X.cards(
        prs, "The Five Cs of written communication", [
            ("Correct", "Correct grammar and spelling — errors undermine "
             "credibility before the content is even read."),
            ("Concise", "Concise expression with excess words eliminated; length "
             "is not a measure of thoroughness."),
            ("Clear", "Clear purpose and expression directed towards the needs of "
             "the reader, not the convenience of the writer."),
            ("Coherent", "A logical flow of ideas so the reader can follow the "
             "argument without re-reading."),
            ("Controlling", "Controlled flow of words and ideas — structure, "
             "headings and emphasis that guide attention."),
            ("Applied where", "Status reports, escalations, meeting minutes, "
             "change requests and every stakeholder email."),
        ], n, kicker=PE8, accent=ROSE); n += 1

    X.cards(
        prs, "Active listening, feedback and non-verbal signals", [
            ("Listen actively", "Stay engaged with the speaker, show interest, and "
             "summarise or repeat the message back to check understanding."),
            ("Seek feedback", "Listen to written, verbal and non-verbal feedback to "
             "ensure your message and others' were heard correctly."),
            ("Read non-verbals", "Body language, tone and gesture carry a large "
             "share of the meaning, especially in conflict."),
            ("Ask open questions", "Questions that cannot be answered yes or no "
             "surface the concern behind the objection."),
            ("Paraphrase, don't parrot", "Restating in your own words proves you "
             "understood; repeating words only proves you heard."),
            ("Manage your own bias", "The receiver decodes through their own frame "
             "of reference; assume misunderstanding, then verify."),
        ], n, kicker=PE8, accent=BLUE); n += 1

    X.compare(
        prs, "Virtual versus co-located teams",
        ("VIRTUAL TEAM",
         "Now normal in most workplaces",
         ["Access to better skills at lower cost across geographies",
          "Avoids relocation expense and widens the talent pool",
          "Supports work/life balance and inclusion of remote members",
          "Relies entirely on communication technology to function",
          "May have bonding challenges and slower trust formation"]),
        ("CO-LOCATED TEAM",
         "Everyone in one team space",
         ["Interaction is easy and unplanned — questions cost seconds",
          "Bonding and trust are facilitated by informal contact",
          "Osmotic communication and information radiators work naturally",
          "Non-verbal signals are visible, so conflict surfaces earlier",
          "Constrained to the talent available in one location"]),
        n, kicker=PE8, lc=VIOLET, rc=TEAL,
        footer_note="For virtual teams, invest deliberately in what co-location "
                    "gives you free: explicit working agreements, a persistent "
                    "shared board, video-on norms and scheduled social contact."); n += 1

    X.exam(
        prs, "Exam focus — communication", [
            ("You have 8 team members and 3 new people join",
             "Channels go from 9×8/2 = 36 to 12×11/2 = 66 — read whether the PM "
             "is counted in N"),
            ("A stakeholder says they were never informed of a decision",
             "Review the communications management plan; the omission is a "
             "planning defect, not a personal failing"),
            ("You must deliver bad news to a sponsor",
             "Use interactive communication — face-to-face or a call — never a "
             "push email as the first contact"),
            ("Large volumes of reference material for many stakeholders",
             "Pull communication: publish to a repository or dashboard they "
             "access at their own discretion"),
        ], n, accent=ROSE); n += 1
    return n


# =================================================================== risk
def _risk(prs, n):
    X.statement(
        prs, "Knowledge area 7 of 8 in the planning block",
        "Risk: uncertainty that matters, managed on purpose",
        [("Both directions", "Risks can be negative (threats) or positive "
          "(opportunities) — PMI expects you to plan for both."),
         ("Known causes", "Risk originates from known and unknown causes inside "
          "and outside the business environment."),
         ("Trigger conditions", "Risk development is signalled by a trigger — "
          "identify the trigger, not just the risk.")],
        n, kicker=B5, accent=ROSE); n += 1

    X.itto(
        prs, "Plan Risk Management — ITTO",
        ["Project charter — high-level risks and success criteria",
         "Project management plan — all subsidiary plans",
         "Project documents: stakeholder register",
         "EEFs — organisational risk thresholds and appetite",
         "OPAs — risk policy, risk categories, templates, lessons learned"],
        ["Expert judgment on risk methodology",
         "Data analysis — stakeholder risk appetite analysis",
         "Meetings — the risk planning meeting with the team, sponsor "
         "and selected stakeholders"],
        ["Risk management plan — methodology, roles and responsibilities, "
         "funding, timing, risk categories (RBS)",
         "Stakeholder risk appetite, probability and impact definitions",
         "Probability and impact matrix, reporting formats, tracking"],
        n, kicker=B5,
        purpose="Plan Risk Management defines HOW risk work will be done — the "
                "definitions of 'high probability' and 'high impact' are set here."); n += 1

    X.compare(
        prs, "Risk versus issue",
        ("RISK",
         "An uncertain future event",
         ["Focused on the FUTURE — it may or may not happen",
          "Can be positive (opportunity) or negative (threat)",
          "Documented in the RISK REGISTER",
          "The reaction is called a RISK RESPONSE, planned in advance",
          "Has a probability, an impact, an owner and a trigger condition"]),
        ("ISSUE",
         "A present condition already affecting the project",
         ["Focused on the PRESENT — it has already occurred",
          "Will always be negative",
          "Documented in the ISSUE LOG",
          "The reaction is called a WORKAROUND, produced reactively",
          "Has an owner, a target resolution date and an escalation path"]),
        n, kicker=B5, lc=BLUE, rc=ROSE,
        footer_note="When a risk becomes an issue you must act: implement the "
                    "planned response, log it in the issue log, and update the "
                    "risk register status. Recognising that transition is an "
                    "explicit ECO enabler."); n += 1

    X.cards(
        prs, "Risk attitude, appetite, tolerance and threshold", [
            ("Risk attitude", "The organisation's or individual's disposition "
             "toward uncertainty — averse, neutral or seeking."),
            ("Risk appetite", "The degree of uncertainty the organisation is "
             "willing to accept in anticipation of a reward."),
            ("Risk tolerance", "The measurable degree of variation around an "
             "objective that is acceptable — for example ±10% of budget."),
            ("Risk threshold", "The specific point at which a risk becomes "
             "unacceptable and a response or escalation is mandatory."),
            ("Why it matters", "Thresholds turn a subjective conversation into an "
             "automatic, auditable trigger for action."),
            ("Where captured", "Stakeholder risk appetite is analysed in Plan Risk "
             "Management and recorded in the risk management plan."),
        ], n, kicker=B5, accent=VIOLET); n += 1

    X.itto(
        prs, "Identify Risks — ITTO",
        ["Project management plan — all subsidiary plans and baselines",
         "Project documents: assumption log, cost and duration estimates, "
         "issue log, lessons learned register, requirements documentation, "
         "resource requirements, stakeholder register",
         "Agreements, procurement documentation, EEFs and OPAs"],
        ["Expert judgment",
         "Data gathering: brainstorming, checklists, interviews",
         "Data analysis: root cause analysis, assumption and constraint "
         "analysis, SWOT analysis, document analysis",
         "Interpersonal and team skills — facilitation",
         "Prompt lists (RBS, PESTLE, TECOP, VUCA)",
         "Meetings"],
        ["Risk register — the master list of identified risks",
         "Risk report — sources of overall project risk and summary "
         "information on identified individual risks",
         "Project document updates"],
        n, kicker=B5,
        purpose="Identify Risks is iterative — new risks emerge throughout the "
                "project, so the register is never finished."); n += 1

    X.table(
        prs, "Risk identification techniques",
        ["Technique", "How it works", "Strength"],
        [["Risk breakdown structure", "Hierarchical list of risk categories used "
          "as a checklist when brainstorming", "Systematic coverage; exposes "
          "categories the team never thought about"],
         ["Brainstorming", "Facilitated group generation of candidate risks with "
          "judgement deferred", "Volume and diversity of ideas early"],
         ["SWOT analysis", "Examine strengths, weaknesses, opportunities and "
          "threats of the project and organisation", "Systematically surfaces "
          "OPPORTUNITIES, not just threats"],
         ["Assumption analysis", "Test the validity and stability of each "
          "documented assumption and constraint", "Every assumption is an "
          "unregistered risk until tested"],
         ["Delphi technique", "Anonymous rounds of expert input, summarised and "
          "recirculated until consensus", "Removes dominance and groupthink from "
          "expert judgement"],
         ["Document review", "Structured review of plans, contracts, prior "
          "project files and lessons learned", "Cheap and finds risks the "
          "organisation has already met before"],
         ["Nominal group technique", "Brainstorm then vote to rank the risks",
          "Produces a prioritised list in one session"],
         ["Interviews", "One-to-one questioning of experienced participants",
          "Surfaces political or commercially sensitive risks"]],
        n, kicker=B5, accent=BLUE, widths=[1.5, 2.7, 2.3]); n += 1

    X.cards(
        prs, "Common project risk categories", [
            ("Financial", "Benefit shortfall, budget overrun, exchange rate "
             "movement, funding withdrawal, cost inflation on long-lead items."),
            ("Technical", "Design risk, project complexity, integration failure, "
             "unproven technology, technical debt accumulation."),
            ("Commercial", "Supplier failure, procurement delay, contract dispute, "
             "vendor lock-in, insolvency of a key partner."),
            ("Compliance", "Regulatory change, legal risk, health and safety, data "
             "protection, security and IT security exposure."),
            ("Requirements", "Scope creep, requirement volatility, poor estimates, "
             "unclear acceptance criteria, quality risk."),
            ("Organisational", "Resistance to change, resource unavailability, "
             "programme dependency, reputation risk, key person dependency."),
        ], n, kicker=B5, accent=AMBER); n += 1

    X.process(
        prs, "Building a Risk Breakdown Structure (RBS)", [
            ("Start with categories", "Take the organisation's standard top-level "
             "risk categories — external, technical, organisational, PM."),
            ("Decompose one level", "Break each into sub-categories: external "
             "becomes regulatory, market, competitor, weather."),
            ("Decompose again", "Continue until the category is specific enough to "
             "prompt a concrete risk in a brainstorm."),
            ("Use as a checklist", "Walk the team down the RBS branch by branch "
             "and ask what could go wrong or go unusually well here."),
            ("Feed the register", "Record each identified risk against its RBS "
             "code so you can see which categories dominate."),
        ], n, kicker=B5, accent=TEAL,
        note="The RBS also answers a management question the register cannot: "
             "which category of risk carries most of our exposure, and is that "
             "where our mitigation money is actually going?"); n += 1

    X.itto(
        prs, "Perform Qualitative Risk Analysis — ITTO",
        ["Project management plan — risk management plan",
         "Project documents: assumption log, risk register, "
         "stakeholder register",
         "EEFs — industry studies of similar projects, published material",
         "OPAs — information from prior similar completed projects"],
        ["Expert judgment",
         "Data gathering — interviews",
         "Data analysis: risk data quality assessment, risk probability "
         "and impact assessment, assessment of other risk parameters "
         "(urgency, proximity, dormancy, manageability, controllability)",
         "Interpersonal and team skills — facilitation",
         "Risk categorisation, data representation (probability and impact "
         "matrix, hierarchical charts), meetings"],
        ["Project document updates: risk register with priority ratings, "
         "risk report, assumption log, issue log"],
        n, kicker=B5,
        purpose="Perform the subjective qualitative assessment FIRST to prioritise "
                "risks; only escalate to quantitative analysis if further support "
                "is required."); n += 1

    X.matrix2x2(
        prs, "Probability and impact matrix", "IMPACT IF IT OCCURS",
        "PROBABILITY OF OCCURRING",
        [("HIGH P / LOW I", "Frequent nuisances. Mitigate through process change "
          "or accept actively with a small contingency.", AMBER),
         ("HIGH P / HIGH I", "Red zone. Escalate, avoid or transfer. Needs a named "
          "owner, a funded response and board visibility.", ROSE),
         ("LOW P / LOW I", "Watch list. Record in the register, review "
          "periodically, spend nothing on them now.", CYAN),
         ("LOW P / HIGH I", "Insurable catastrophes. Transfer, or fund a "
          "contingency plan with a defined trigger condition.", VIOLET)],
        n, kicker=B5, accent=ROSE,
        note="Priority score = probability × impact, using the numeric scales "
             "defined in the risk management plan. The matrix converts subjective "
             "judgement into a consistent, comparable ranking."); n += 1

    X.cards(
        prs, "Other risk parameters beyond probability and impact", [
            ("Urgency", "How soon a response must be implemented for it to be "
             "effective — a short period indicates high urgency."),
            ("Proximity", "How soon the risk itself is likely to occur — a short "
             "period means the risk is imminent."),
            ("Dormancy", "The period between the risk occurring and the project "
             "discovering it — long dormancy is dangerous."),
            ("Manageability", "How easily the risk owner can actually manage the "
             "occurrence or impact of the risk."),
            ("Controllability", "The degree to which the organisation is able to "
             "control the risk outcome at all."),
            ("Connectivity", "How strongly the risk is linked to other risks — "
             "clustered risks fail together."),
        ], n, kicker=B5, accent=CYAN); n += 1

    X.table(
        prs, "Risk register — the fields that matter",
        ["Field", "Why it is there"],
        [["Risk ID and title", "A unique persistent reference used in reporting and "
          "in every escalation"],
         ["Category (RBS code)", "Lets you analyse where exposure is concentrated "
          "rather than only listing items"],
         ["Risk description", "Written as cause → event → effect, so the response "
          "can target the cause"],
         ["Probability and impact", "Rated on the scales defined in the risk "
          "management plan; produces the priority score"],
         ["Risk score / priority", "The ranking that decides where analysis and "
          "money go next"],
         ["Risk owner", "One named person accountable for monitoring and "
          "implementing the response — never a team"],
         ["Planned response", "The chosen strategy and the specific actions, with "
          "cost and schedule impact"],
         ["Trigger condition", "The observable signal that the risk is "
          "materialising and the response should be executed"],
         ["Residual and secondary risk", "What remains after the response, and what "
          "the response itself creates"],
         ["Status", "Open, occurred, closed, or retired — with the date"]],
        n, kicker=B5, accent=BLUE, widths=[1.7, 4.3]); n += 1

    X.itto(
        prs, "Perform Quantitative Risk Analysis — ITTO",
        ["Project management plan: risk management plan, scope, schedule "
         "and cost baselines",
         "Project documents: assumption log, basis of estimates, cost and "
         "duration estimates, milestone list, risk register and report, "
         "resource requirements, schedule",
         "EEFs and OPAs — industry studies and historical databases"],
        ["Expert judgment",
         "Data gathering — interviews to quantify probability and impact",
         "Interpersonal and team skills — facilitation",
         "Representations of uncertainty (probability distributions)",
         "Data analysis: simulation (Monte Carlo), sensitivity analysis, "
         "decision tree analysis, influence diagrams, EMV"],
        ["Project document updates — risk report with a quantified "
         "assessment of overall project risk exposure, probabilistic "
         "analysis of the project and a prioritised list of individual risks"],
        n, kicker=B5,
        purpose="Quantitative analysis is optional and usually reserved for large, "
                "complex or high-value projects where the modelling pays for itself."); n += 1

    X.chart(
        prs, "Tornado chart — sensitivity analysis",
        "bar", ["Regulatory delay", "Vendor lead time", "Labour rate",
                "Scope volatility", "FX movement", "Site access"],
        [("Downside impact on project NPV ($k)", [420, 310, 240, 180, 120, 70])],
        n, kicker=B5, accent=VIOLET,
        insight=["Sensitivity analysis shows which individual risks have the "
                 "greatest potential impact on the project outcome.",
                 "Bars are sorted longest at the top, producing the tornado shape "
                 "that gives the chart its name.",
                 "Bars show the size of the downside swing in NPV when that one "
                 "input is varied and all others are held constant.",
                 "Management action: fund mitigation for the top two or three "
                 "bars; the tail rarely justifies the spend."]); n += 1

    X.formula(
        prs, "Expected Monetary Value and decision trees", [
            ("EMV of a risk", "EMV = P × I", "Probability times impact. Threats "
             "are negative, opportunities positive."),
            ("EMV of a branch", "Σ (P × I) for all outcomes", "Sum the expected "
             "values of every outcome on that decision branch."),
            ("Decision value", "Branch EMV − Cost of branch", "Choose the path "
             "with the best net expected value, not the best best-case."),
            ("Worked example", "0.3 × (−$200k) = −$60k", "A 30% chance of a $200k "
             "loss carries $60k of contingency, not $200k."),
        ], n, kicker=B5, accent=AMBER,
        note="Decision trees show the decisions and their impacts (costs or "
             "benefits) along each path, together with their probabilities, "
             "producing an expected monetary value for each branch outcome."); n += 1

    X.cards(
        prs, "Monte Carlo simulation", [
            ("What it does", "Runs the schedule or cost model thousands of times, "
             "sampling each uncertain input from its distribution."),
            ("What you supply", "Three-point estimates or distributions for the "
             "uncertain activities, plus the network logic."),
            ("What you get", "An S-curve of possible outcomes with a confidence "
             "level attached to every date or cost."),
            ("The P-values", "P50 is the median outcome; P80 is the value you have "
             "an 80% chance of meeting — commit to P80, not P50."),
            ("Criticality index", "How often each activity lands on the critical "
             "path across all runs — a better target list than one static CPM."),
            ("The limitation", "Output quality is bounded by input quality; "
             "precise-looking numbers from guessed inputs are still guesses."),
        ], n, kicker=B5, accent=TEAL); n += 1

    X.itto(
        prs, "Plan Risk Responses — ITTO",
        ["Project management plan: resource, risk and cost management plans, "
         "and the cost baseline",
         "Project documents: lessons learned register, project schedule, "
         "project team assignments, resource calendars, risk register, "
         "risk report, stakeholder register",
         "EEFs — risk appetite and thresholds; OPAs — historical responses"],
        ["Expert judgment",
         "Data gathering — interviews",
         "Interpersonal and team skills — facilitation",
         "Strategies for threats, opportunities and overall project risk",
         "Contingent response strategies",
         "Data analysis: alternatives analysis, cost-benefit analysis",
         "Decision making — multi-criteria decision analysis"],
        ["Change requests",
         "Project management plan updates: schedule, cost, quality, "
         "resource, procurement plans, scope/schedule/cost baselines",
         "Project document updates: risk register, risk report, "
         "assumption log, lessons learned register, project schedule"],
        n, kicker=B5,
        purpose="Every response must be timely, cost-effective, agreed by all "
                "parties and owned by one named person."); n += 1

    X.table(
        prs, "Threat response strategies",
        ["Strategy", "What it means", "Example"],
        [["Escalate", "The threat is outside the project's scope or authority; "
          "hand it to the programme or portfolio level",
          "A regulatory change affecting the whole business unit"],
         ["Avoid", "Eliminate the threat entirely by removing its cause or "
          "changing the plan", "Drop the risky feature, or change to proven "
          "technology"],
         ["Transfer", "Shift the impact and ownership of the threat to a third "
          "party — the threat still exists", "Insurance, warranties, performance "
          "bonds, fixed-price contracts"],
         ["Mitigate", "Reduce the probability or impact of the threat to an "
          "acceptable level", "Prototype early, add redundancy, run more tests"],
         ["Accept", "Acknowledge the threat and take no proactive action. ACTIVE "
          "acceptance funds a contingency reserve; PASSIVE does nothing but "
          "document it", "Minor weather delay risk with a small time buffer"]],
        n, kicker=B5, accent=ROSE, widths=[1.2, 3.0, 2.4]); n += 1

    X.table(
        prs, "Opportunity response strategies",
        ["Strategy", "What it means", "Example"],
        [["Escalate", "The opportunity is outside the project's authority to "
          "pursue; raise it to programme or portfolio",
          "A reusable component that benefits the entire portfolio"],
         ["Exploit", "Ensure the opportunity definitely happens — remove all "
          "uncertainty from it", "Assign your best people to guarantee an early "
          "finish that unlocks a bonus"],
         ["Share", "Allocate ownership to a third party best able to capture the "
          "benefit", "Joint venture, partnership, risk-sharing consortium"],
         ["Enhance", "Increase the probability or the positive impact of the "
          "opportunity", "Add resource to a task whose early finish would pull "
          "in the whole schedule"],
         ["Accept", "Take advantage of it if it arises but do not actively pursue "
          "it", "Note a possible favourable exchange rate movement, take no action"]],
        n, kicker=B5, accent=TEAL, widths=[1.2, 3.0, 2.4],
        note="Mirror pairs: Avoid ↔ Exploit, Transfer ↔ Share, Mitigate ↔ Enhance, "
             "and Escalate and Accept appear on both sides. Learning them as pairs "
             "halves the memorisation."); n += 1

    X.cards(
        prs, "Secondary risk, residual risk and contingency plans", [
            ("Trigger condition", "The observable signal that a risk is about to "
             "develop — the cue for the team to implement the response."),
            ("Secondary risk", "A new risk that arises as a direct result of "
             "implementing a risk response — always re-assess after responding."),
            ("Residual risk", "The risk that remains after responses have been "
             "implemented; it is accepted knowingly and stays in the register."),
            ("Contingency plan", "The prepared response executed if the risk "
             "occurs, funded from the contingency reserve."),
            ("Fallback plan", "The backup executed if the contingency plan itself "
             "proves inadequate — plan B for plan B."),
            ("Risk owner", "One named individual accountable for watching the "
             "trigger and executing the response — never a committee."),
        ], n, kicker=B5, accent=VIOLET); n += 1

    X.cards(
        prs, "ECO 2026 emphasis — AI-assisted risk detection", [
            ("Pattern detection", "AI can scan issue logs, commit history and "
             "supplier data to surface risk signals a human would not spot."),
            ("Estimation support", "Models trained on historical project data "
             "produce range estimates and challenge optimistic single points."),
            ("Register hygiene", "Language models can cluster duplicate risks and "
             "rewrite vague entries as cause–event–effect statements."),
            ("Early warning", "Sentiment and cadence signals from team "
             "communication can flag emerging delivery risk earlier than reports."),
            ("Human accountability", "The risk owner remains a named human; AI "
             "output is an input to judgement, never the decision itself."),
            ("New risk category", "AI use introduces its own risks: data privacy, "
             "hallucinated output, model bias and vendor dependency."),
        ], n, kicker=B5, accent=BLUE); n += 1

    X.exam(
        prs, "Exam focus — risk", [
            ("A risk has occurred and is now affecting the project",
             "It is an issue: implement the planned response, record it in the "
             "issue log and update the risk register"),
            ("You buy insurance against a possible loss",
             "That is transfer, not mitigate — the risk still exists, only the "
             "impact ownership moved"),
            ("You cancel the risky component of the scope entirely",
             "That is avoid — the only strategy that removes the risk rather than "
             "reducing or moving it"),
            ("A new risk appears because of the response you implemented",
             "That is a secondary risk; add it to the register and analyse it "
             "like any other"),
            ("The question asks what remains after you respond",
             "Residual risk — knowingly accepted and still tracked in the register"),
        ], n, accent=ROSE); n += 1

    X.recap(
        prs, "Recap — risk planning", [
            ("Five planning processes", "Plan Risk Management, Identify, "
             "Qualitative, Quantitative, Plan Responses — in that order."),
            ("Definitions come first", "The risk management plan sets the "
             "probability and impact scales everything else uses."),
            ("Qualitative before quantitative", "Prioritise subjectively first; "
             "model numerically only where it pays for itself."),
            ("Ten strategies", "Five for threats and five for opportunities, "
             "learned as mirror pairs."),
            ("Register discipline", "Cause–event–effect wording, one named owner, "
             "a trigger condition and a status on every row."),
            ("Never finished", "Identification is iterative; the register is "
             "reviewed at every status cycle for the life of the project."),
        ], n, accent=CYAN); n += 1
    return n


# ============================================================ procurement
def _procurement(prs, n):
    X.statement(
        prs, "Knowledge area 8 of 8 in the planning block",
        "Procurement: what you buy, and who carries the risk",
        [("Make or buy", "The first decision is whether the work should be done "
          "internally at all."),
         ("Agreement vs contract", "You can have an agreement without a contract, "
          "but you cannot have a contract without an agreement."),
         ("Risk allocation", "Contract type is not an administrative detail — it "
          "decides who absorbs cost overrun.")],
        n, kicker=P5, accent=TEAL); n += 1

    X.itto(
        prs, "Plan Procurement Management — ITTO",
        ["Project charter and business documents (business case, benefits plan)",
         "Project management plan: scope, quality, resource management plans "
         "and the scope baseline",
         "Project documents: milestone list, project team assignments, "
         "requirements documentation, RTM, resource requirements, "
         "risk register, stakeholder register",
         "EEFs — marketplace conditions, legal jurisdiction, contract "
         "management systems; OPAs — pre-qualified seller lists, policies"],
        ["Expert judgment on contracting and the relevant market",
         "Data gathering — market research",
         "Data analysis — make-or-buy analysis",
         "Source selection analysis (least cost, qualifications only, "
         "quality-based, quality and cost-based, sole source, fixed budget)",
         "Meetings with prospective sellers and internal stakeholders"],
        ["Procurement management plan and procurement strategy",
         "Bid documents (RFI, RFP, RFQ, IFB) and procurement SOW",
         "Source selection criteria, make-or-buy decisions",
         "Independent cost estimates, change requests, document updates"],
        n, kicker=P5,
        purpose="Procurement planning decides what to buy, how to buy it, how much "
                "to buy and when — before any seller is contacted."); n += 1

    X.cards(
        prs, "Procurement strategy fundamentals", [
            ("What procurement covers", "Any resource external to your company — "
             "a vendor, contractors, consultants or any other outside resource."),
            ("Agreement without contract", "The project charter can agree the use "
             "of internal resources without any contract existing."),
            ("Contract needs agreement", "You cannot have a contract without an "
             "underlying agreement between the parties."),
            ("Delivery method", "Decide turnkey, design-build, design-bid-build or "
             "staff augmentation before writing the bid documents."),
            ("Payment approach", "Choose the contract payment type that matches "
             "how well the scope is actually defined."),
            ("Procurement phases", "Sequence the procurement across the life cycle "
             "so long-lead items are ordered early enough to arrive."),
        ], n, kicker=P5, accent=BLUE); n += 1

    X.process(
        prs, "The procurement process end to end", [
            ("Plan", "Make-or-buy analysis, procurement strategy, bid documents, "
             "procurement SOW and source selection criteria."),
            ("Advertise", "Advertise in specialty trade publications or websites "
             "to invite more bids and grow the pre-qualified seller list."),
            ("Bidder conference", "Meet all prospective sellers together before "
             "bidding so every seller has the same information."),
            ("Evaluate and select", "Score proposals against the published source "
             "selection criteria; negotiate the agreement."),
            ("Administer and close", "Manage seller performance against the "
             "contract, then close the procurement formally."),
        ], n, kicker=P5, accent=VIOLET,
        note="Bidder conferences (also vendor or pre-bid conferences) exist to "
             "ensure no seller receives preferential treatment — every question and "
             "answer is shared with all prospective sellers."); n += 1

    X.table(
        prs, "Bid documents — pick the right instrument",
        ["Document", "Use it when", "What you get back"],
        [["Request for Information (RFI)", "You need more information about what "
          "sellers can provide before you can even specify",
          "Capability statements that shape your requirements"],
         ["Request for Proposal (RFP)", "There is a problem and the solution is "
          "not obvious — you need someone to propose an approach",
          "Technical solutions with methodology, team and price"],
         ["Request for Quote (RFQ)", "You know exactly what you need and just "
          "require the cost from the seller",
          "Prices for a clearly specified item or service"],
         ["Invitation for Bid (IFB)", "A well-defined scope where price is the "
          "deciding factor, often in public sector",
          "Sealed price bids against an identical specification"]],
        n, kicker=P5, accent=AMBER, widths=[1.7, 2.6, 2.2],
        note="The rule of thumb: RFI when you do not know what to ask for, RFP when "
             "you know the problem but not the solution, RFQ/IFB when you know "
             "exactly what you want and only need a number."); n += 1

    X.cards(
        prs, "Why contracts exist, and what they must contain", [
            ("Legalise agreements", "A contract turns a working understanding into "
             "a legally enforceable obligation for both parties."),
            ("Structure relationships", "Defines who does what, by when, to what "
             "standard, and what happens when that fails."),
            ("Description of work", "The deliverables and scope, usually via an "
             "attached procurement statement of work."),
            ("Schedule and delivery", "Delivery dates, milestones, and the "
             "schedule information both parties are bound to."),
            ("Authority and responsibility", "Identification of authority where "
             "appropriate, and the responsibilities of both parties."),
            ("Price and payment terms", "The amount, the milestones that trigger "
             "payment, and the invoicing and approval route."),
            ("Termination and disputes", "Provisions for termination, alternative "
             "dispute resolution and governing jurisdiction."),
            ("Change and management", "How technical and business aspects are "
             "managed, including how contract changes are agreed."),
        ], n, kicker=P5, accent=CYAN, cols=4); n += 1

    X.table(
        prs, "Contract types and who carries the cost risk",
        ["Type", "How it works", "Risk sits with"],
        [["Firm Fixed Price (FFP)", "One price for a well-defined scope, regardless "
          "of the seller's actual cost", "SELLER — the most common and simplest "
          "fixed-price form"],
         ["Fixed Price Incentive Fee (FPIF)", "Fixed price plus an incentive for "
          "meeting agreed cost or performance targets", "Mostly seller, shared "
          "above the target through a share ratio"],
         ["Fixed Price with Economic Price Adjustment (FP-EPA)", "Fixed price with "
          "a defined adjustment for inflation or currency", "Seller, with defined "
          "external exposure shared — for multi-year deals"],
         ["Cost Plus Fixed Fee (CPFF)", "Actual allowable costs reimbursed plus a "
          "fixed fee that does not vary with cost", "BUYER — the seller has no "
          "incentive to control cost"],
         ["Cost Plus Incentive Fee (CPIF)", "Costs reimbursed plus a fee that "
          "varies with performance against targets", "Buyer, partially shared "
          "through the incentive formula"],
         ["Cost Plus Award Fee (CPAF)", "Costs reimbursed plus an award fee at the "
          "buyer's subjective judgement", "Buyer; award is usually not subject to "
          "appeal"],
         ["Time and Materials (T&M)", "Hourly or daily rates plus materials; a "
          "hybrid of fixed unit price and cost reimbursable", "Buyer — cap it "
          "with a not-to-exceed clause"]],
        n, kicker=P5, accent=ROSE, widths=[1.9, 2.5, 2.0]); n += 1

    X.compare(
        prs, "Fixed price versus cost reimbursable — when to choose",
        ("FIXED PRICE",
         "Choose when the scope is well defined",
         ["Requirements are clear, stable and fully specified",
          "The seller carries the cost risk and prices it in",
          "Buyer's cost is predictable from the day of signature",
          "Change is expensive: every variation is a renegotiation",
          "Sellers may cut corners if their margin disappears"]),
        ("COST REIMBURSABLE",
         "Choose when the scope is uncertain",
         ["Requirements are expected to evolve, or the work is R&D",
          "The buyer carries the cost risk and must actively monitor it",
          "Buyer's final cost is unknown until the work is complete",
          "Change is cheap and flexible to accommodate",
          "Requires strong buyer-side cost control and audit rights"]),
        n, kicker=P5, lc=BLUE, rc=AMBER,
        footer_note="Time and materials sits between the two: use it for small "
                    "amounts of work, staff augmentation, or when you need to start "
                    "before the scope can be written — always with a ceiling."); n += 1

    X.cards(
        prs, "Make-or-buy analysis and vendor qualification", [
            ("Make-or-buy analysis", "Compare the total cost, capability, capacity "
             "and risk of doing the work internally versus procuring it."),
            ("Beyond price", "Consider strategic capability retention, "
             "intellectual property and long-term supportability, not just cost."),
            ("Independent estimate", "Produce your own cost estimate before you see "
             "any bid, so you can judge whether a bid is realistic."),
            ("Qualified vendors", "Pre-approved by the organisation, with a history "
             "of work and accounts already set up."),
            ("Preferred vendors", "Often preferred precisely because they are "
             "proven — the procurement cycle is shorter and less risky."),
            ("Source selection criteria", "Published in advance and applied "
             "consistently: capability, capacity, price, references, risk."),
        ], n, kicker=P5, accent=TEAL); n += 1

    X.cards(
        prs, "ECO 2026 emphasis — sustainable procurement", [
            ("Sustainability criteria", "Environmental and social performance sit "
             "in the source selection criteria alongside price and capability."),
            ("Supply chain due diligence", "Assess labour practice, provenance and "
             "modern slavery exposure across the seller's own supply chain."),
            ("Whole-life cost", "Evaluate energy, maintenance and disposal cost "
             "over the asset life, not just the purchase price."),
            ("Contractual commitments", "Write sustainability obligations and "
             "reporting duties into the contract, with measurable targets."),
            ("Local and inclusive sourcing", "Many jurisdictions now weight local "
             "content and supplier diversity in public procurement."),
            ("Reporting obligation", "Sustainability disclosure is increasingly a "
             "regulatory requirement flowing down to project suppliers."),
        ], n, kicker=P5, accent=VIOLET); n += 1

    X.exam(
        prs, "Exam focus — procurement", [
            ("The scope is unclear and likely to change",
             "Choose a cost-reimbursable or T&M contract; a fixed price forces "
             "renegotiation on every variation"),
            ("The buyer wants maximum cost certainty",
             "Firm Fixed Price — the seller carries the cost risk entirely"),
            ("All prospective sellers must receive the same information",
             "Hold a bidder conference; share every question and answer with all "
             "sellers"),
            ("You need to know what solutions exist before specifying",
             "Issue an RFI — an RFP presumes you can already state the problem"),
            ("A T&M contract is running over budget",
             "T&M should carry a not-to-exceed ceiling; the buyer holds the cost "
             "risk and must monitor actively"),
        ], n, accent=ROSE); n += 1

    X.recap(
        prs, "Recap — procurement planning", [
            ("Make or buy first", "Decide internally versus externally on total "
             "cost, capability, capacity and risk — not price alone."),
            ("Strategy then documents", "The procurement strategy sets delivery "
             "method and payment type before bid documents are written."),
            ("Right instrument", "RFI to learn, RFP to solve, RFQ and IFB to "
             "price a known specification."),
            ("Contract type allocates risk", "Fixed price puts cost risk on the "
             "seller; cost reimbursable puts it on the buyer."),
            ("Fair process", "Bidder conferences and published source selection "
             "criteria keep the process defensible."),
            ("Sustainability counts", "ECO 2026 expects environmental and social "
             "criteria in selection and in the contract itself."),
        ], n, accent=CYAN); n += 1
    return n


# =================================================================== close
def _close(prs, n):
    X.statement(
        prs, "Bringing the eight plans back together",
        "The integrated plan is a system, not a folder",
        [("Dependencies", "Assess the consolidated plans for dependencies, gaps "
          "and continued business value before you baseline anything."),
         ("Consistency", "The schedule, budget and resource plan must all "
          "describe the same project or none of them is true."),
         ("Maintenance", "The integrated plan is maintained throughout, not "
          "written once and archived.")],
        n, kicker=P1, accent=BLUE); n += 1

    X.timeline(
        prs, "The planning sequence at a glance", [
            ("Integrate", "Establish the plan, the development approach and the "
             "engagement strategy."),
            ("Scope", "Collect requirements, define scope, build the WBS, "
             "baseline it."),
            ("Schedule", "Define, sequence, estimate, analyse the network, "
             "baseline it."),
            ("Cost", "Estimate costs, aggregate to the budget, set reserves, "
             "baseline it."),
            ("Quality & resources", "Set standards and metrics; plan people and "
             "physical resources."),
            ("Comms, risk, procurement", "Plan communication, risk responses and "
             "what will be bought."),
        ], n, kicker=P1, accent=TEAL,
        note="The order matters because the outputs cascade: you cannot estimate a "
             "duration without a work package, or a budget without a duration and "
             "a resource. Late scope change ripples through all of it."); n += 1


    X.recap(
        prs, "Topic 3 recap — plan the project", [
            ("Integration", "The project management plan reconciles all subsidiary "
             "plans and the three baselines into one coherent system."),
            ("Scope", "Requirements, RTM, scope statement, WBS and WBS dictionary "
             "define and defend what will be delivered."),
            ("Schedule", "Activities, dependencies, durations and network analysis "
             "produce a calculated, defensible date."),
            ("Cost", "Estimating methods and reserve strategy produce a "
             "time-phased cost baseline plus management reserve."),
            ("Quality", "Standards, metrics, cost of quality and improvement "
             "cycles build quality in instead of inspecting it in."),
            ("Resources", "Roles, authority, responsibility, competency, RACI, "
             "levelling and smoothing make the plan executable."),
            ("Communication", "A planned strategy with channels, methods, "
             "cadence and a feedback loop for every stakeholder."),
            ("Risk & procurement", "Ten response strategies, a disciplined "
             "register, and contract types that allocate risk deliberately."),
        ], n, accent=CYAN); n += 1

    X.statement(
        prs, "Where Topic 3 leads next",
        "A plan is only a hypothesis until it meets reality",
        [("Topic 4 — lead", "Take the resource and communication plans into "
          "practice: leadership style, motivation, conflict and coaching."),
         ("Topic 5 — control", "Measure actuals against these baselines with "
          "earned value, quality control and integrated change control."),
         ("Topic 6 — close", "Confirm the acceptance criteria written here were "
          "actually met, and harvest the lessons.")],
        n, kicker=P1, accent=VIOLET); n += 1
    return n


# ================================================================== build
def build(prs, n):
    """Render Topic 3. `n` is the running slide number. Return the next number."""
    X.section(
        prs, 3, "Plan the Project",
        "Building the integrated plan — scope, schedule, cost, quality, "
        "resources, communications, risk and procurement.",
        ["The integrated project management plan",
         "Scope: requirements, WBS and baselines",
         "Schedule: activities, dependencies, critical path",
         "Cost: estimating, budget and reserves",
         "Quality: planning and problem-solving tools",
         "Resources, communications and procurement",
         "Risk: identification, analysis and response"],
        n); n += 1

    n = _plan(prs, n)
    n = _scope(prs, n)
    n = _schedule(prs, n)
    n = _cost(prs, n)
    n = _quality(prs, n)
    n = _resources(prs, n)
    n = _comms(prs, n)
    n = _risk(prs, n)
    n = _procurement(prs, n)
    n = _close(prs, n)
    return n
