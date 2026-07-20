"""Topic 1 — Business Environment."""
import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

BE = "Business Environment"


def build(prs, n):
    """Render Topic 1. `n` is the running slide number. Return the next number."""

    # ------------------------------------------------------------ 1. divider
    X.section(
        prs, 1, "Business Environment",
        "Where projects come from, why they are funded, and the governance, "
        "compliance and change context every project must survive in. This topic "
        "sets the vocabulary used for the rest of the course.",
        ["What a project is, and what project management actually delivers",
         "The 12 PMI principles and what project success really depends on",
         "Life cycles and development approaches: predictive, agile and hybrid",
         "Organisational culture, EEFs, OPAs and structured change management",
         "Project governance, escalation thresholds and phase gates",
         "Compliance, sustainability and the responsible use of AI in projects"],
        n); n += 1

    # ------------------------------------------------- 2. definition of project
    X.statement(
        prs, "The foundation of everything that follows",
        "A project is a temporary endeavour undertaken to create a unique "
        "product, service or result.",
        [("TEMPORARY", "It has a definite start and a definite end — ending when "
                       "objectives are met, or when it is clear they cannot be."),
         ("UNIQUE", "The output has never been produced in exactly this form before, "
                    "so some degree of uncertainty is always present."),
         ("DELIVERS CHANGE", "A project moves the organisation from a current state "
                             "to a future state that carries business value.")],
        n, kicker="Definition of a project", accent=BLUE); n += 1

    # --------------------------------------------------- 3. project vs operations
    X.compare(
        prs, "Projects versus operations — why the distinction matters",
        ("PROJECT WORK", "Temporary, unique, change-driven",
         ["Has a defined start and end date fixed by the charter",
          "Produces a unique deliverable that did not previously exist",
          "Staffed by a team that is assembled and later released",
          "Success is measured against scope, schedule, cost and benefits",
          "Progressively elaborated as more information becomes known",
          "Funded from a capital or change budget with a business case"]),
        ("OPERATIONAL WORK", "Ongoing, repetitive, efficiency-driven",
         ["Continues indefinitely as long as the business needs the output",
          "Produces the same product or service repeatedly to a standard",
          "Staffed by a permanent functional team reporting to a line manager",
          "Success is measured against throughput, cost per unit and quality",
          "Optimised for stability and predictable repetition, not novelty",
          "Funded from a recurring operating expense budget"]),
        n, kicker=cd.eco(BE, 1), lc=BLUE, rc=TEAL,
        footer_note="Exam cue: if the scenario describes work that never ends or "
                    "simply repeats, it is operations — the correct answer usually "
                    "involves transitioning the deliverable to operations, not "
                    "extending the project."); n += 1

    # ------------------------------------------------------- 4. examples cards
    X.cards(
        prs, "What counts as a project? Recognising project work in the wild",
        [("Developing a software product",
          "Building a new mobile banking app from concept to launch — unique code, a "
          "fixed release date, and a team disbanded after go-live."),
         ("Constructing a new office",
          "Design, permits, build and fit-out of a physical asset, with heavy "
          "regulatory compliance and irreversible, expensive change late on."),
         ("Filming a motion picture",
          "Highly creative, schedule-driven work with named talent constraints and a "
          "single big-bang delivery to distribution."),
         ("An advertising campaign",
          "Short, iterative, market-sensitive delivery where the external environment "
          "can invalidate the concept mid-flight."),
         ("Redesigning a business process",
          "An internal change project whose real deliverable is adoption by people, "
          "not a document — heavy change management content."),
         ("Migrating to a cloud platform",
          "Technical transformation with security, data-residency and compliance "
          "obligations plus a hard decommission deadline.")],
        n, kicker=cd.eco(BE, 8), accent=TEAL); n += 1

    # ---------------------------------------------- 5. what is project management
    X.statement(
        prs, "What is project management?",
        "The application of knowledge, skills, tools and techniques to project "
        "activities to meet the project requirements.",
        [("A DISCIPLINE", "It spans initiating, planning, executing, monitoring and "
                          "controlling, and closing — performed with intent, not by accident."),
         ("A VALUE ENGINE", "Projects are how strategy actually happens; without them an "
                            "organisation's strategic plan stays a slide deck."),
         ("A RISK REDUCER", "Structured management makes uncertainty visible early, when "
                            "responding to it is still cheap.")],
        n, kicker="Project management defined", accent=VIOLET); n += 1

    # ------------------------------------------------------ 6. role of the PM
    X.cards(
        prs, "The role of the project manager — six jobs you are actually paid for",
        [("Integrator",
          "Holds the whole picture together, making sure scope, schedule, cost, quality "
          "and risk decisions are consistent with one another."),
         ("Communicator",
          "Spends roughly 90% of the working day communicating — translating between "
          "technical teams, sponsors and customers."),
         ("Decision maker",
          "Makes calls within delegated authority and escalates cleanly and quickly "
          "when a threshold is breached."),
         ("Servant leader",
          "Removes impediments, protects the team from noise, and creates the "
          "conditions in which skilled people can do good work."),
         ("Risk owner",
          "Continuously scans internally and externally for threats and opportunities, "
          "and drives agreed responses to closure."),
         ("Business steward",
          "Keeps the project honest about business value, stopping or reshaping work "
          "that no longer justifies its investment.")],
        n, kicker=cd.eco(BE, 1), accent=AMBER); n += 1

    # ----------------------------------------------------- 7. triple constraint
    X.statement(
        prs, "The triple constraint — the physics of every project",
        "Scope, time and cost are joined; move one and at least one other must "
        "move, or quality silently absorbs the difference.",
        [("SCOPE", "The work required and the features delivered. Uncontrolled growth "
                   "here is scope creep and is the single most common project failure."),
         ("TIME", "The schedule and its milestones. Compressing time without adding cost "
                  "or cutting scope only borrows quality from the future."),
         ("COST", "The approved budget including reserves. Cutting cost mid-flight "
                  "usually means fewer people, which extends time.")],
        n, kicker="Triple constraint", accent=ROSE); n += 1

    # -------------------------------------------- 8. constraint trade-off matrix
    X.matrix2x2(
        prs, "Which constraint is fixed? Choosing your development approach from it",
        "REQUIREMENTS CERTAINTY  →  high",
        "DELIVERY DATE  →  fixed",
        [("Fixed date, vague scope", "Use agile with a fixed timebox and a variable "
          "backlog. Deliver the highest-value slice by the date.", VIOLET),
         ("Fixed date, clear scope", "Predictive delivery with a firm baseline and "
          "strong change control is the natural fit.", BLUE),
         ("Flexible date, vague scope", "Exploratory or iterative work — prototype, "
          "learn, then commit once the problem is understood.", ROSE),
         ("Flexible date, clear scope", "Incremental delivery lets the customer take "
          "value early while the remaining work continues.", TEAL)],
        n, kicker=cd.eco("Process", 3), accent=CYAN,
        note="In agile the triple constraint inverts: cost and time are fixed by the "
             "sprint, and scope is the variable that flexes."); n += 1

    # ------------------------------------------------------ 9. PM competencies
    X.cards(
        prs, "The PMI Talent Triangle — three competency areas the PMP tests",
        [("Ways of Working",
          "Technical mastery of the many methods available — predictive, agile, hybrid — "
          "and the judgement to tailor the method to the environment."),
         ("Power Skills",
          "Collaborative leadership, effective communication, empathy, conflict "
          "resolution and the influence needed without formal authority."),
         ("Business Acumen",
          "Understanding priority, cost versus benefit, industry context and how to make "
          "decisions that hold up commercially, not just technically.")],
        n, kicker="PMI Talent Triangle", accent=BLUE, cols=3); n += 1

    # ------------------------------------------ 10-11. 12 PMI principles (2 slides)
    X.cards(
        prs, "The 12 PMI project management principles (1 of 2)",
        [("Be a diligent, respectful, caring steward",
          "Act with integrity and in the organisation's and society's interest, "
          "honouring both internal and external obligations."),
         ("Create a collaborative team environment",
          "Teams that share agreements, structures and processes deliver more than "
          "individuals working in parallel silos."),
         ("Effectively engage with stakeholders",
          "Engage proactively and to the degree needed to contribute to project success "
          "and customer satisfaction."),
         ("Focus on value",
          "Continually evaluate and adjust project alignment to business objectives and "
          "the intended benefits and value."),
         ("Recognize and respond to system interactions",
          "See the project as a system of interacting parts; a change in one area has "
          "consequences elsewhere in the organisation."),
         ("Demonstrate leadership behaviours",
          "Leadership is a behaviour anyone on the team can show, not a position on an "
          "organisation chart.")],
        n, kicker="PMI principles", accent=TEAL); n += 1

    X.cards(
        prs, "The 12 PMI project management principles (2 of 2)",
        [("Tailor based on context",
          "Design the delivery approach around the project's context, objectives, "
          "stakeholders, governance and environment."),
         ("Build quality into processes and deliverables",
          "Quality is designed in and inspected continuously, not bolted on by testing "
          "at the end of the schedule."),
         ("Navigate complexity",
          "Continually evaluate and address complexity arising from human behaviour, "
          "system interactions, ambiguity and uncertainty."),
         ("Optimize risk responses",
          "Consistently evaluate exposure to both threats and opportunities, seeking "
          "responses proportional to the impact."),
         ("Embrace adaptability and resilience",
          "Build capacity to absorb impacts and recover quickly, so setbacks do not "
          "become project failures."),
         ("Enable change to achieve the future state",
          "Prepare those affected for adoption; a delivered output that nobody uses has "
          "produced zero value.")],
        n, kicker="PMI principles", accent=VIOLET); n += 1

    # ------------------------------------------------- 12. project success factors
    X.chart(
        prs, "What project success actually depends on",
        "bar",
        ["Understanding of the core problem", "Collaboration & communication",
         "PM effectiveness", "Team member skill levels",
         "Funding & resource availability", "Organisational project maturity"],
        [("Relative influence on outcome", [95, 88, 82, 76, 70, 64])],
        n, kicker=cd.eco(BE, 1), accent=AMBER,
        insight=["Most failures trace back to solving the wrong problem well, "
                 "not to weak execution of the right one.",
                 "Communication quality outranks tooling — no tool rescues a team "
                 "that does not talk to its stakeholders.",
                 "Organisational maturity sets the ceiling; a strong PM in an "
                 "immature organisation still fights the system.",
                 "Funding matters, but adequate funding on the wrong scope simply "
                 "buys a faster failure."]); n += 1

    # --------------------------------------------------- 13. life cycles overview
    X.compare(
        prs, "Two different life cycles — do not confuse them on the exam",
        ("PROJECT LIFE CYCLE", "The phases the project passes through",
         ["The series of phases a project moves through from start to close",
          "Typical phases: feasibility, design, build, test, deploy, close",
          "Phases usually end in a phase gate or stage-gate review",
          "At each gate the sponsor decides go, go-with-change, hold or kill",
          "Defined by the organisation's methodology and governance",
          "Answers the question: where are we in the journey?"]),
        ("DEVELOPMENT LIFE CYCLE", "How the deliverable is actually produced",
         ["The approach used to create the product inside those phases",
          "Options: predictive, iterative, incremental, adaptive/agile, hybrid",
          "Chosen from requirements certainty, risk and delivery cadence",
          "Can differ per deliverable within one and the same project",
          "Defined by the team with the sponsor, and can be tailored",
          "Answers the question: how are we building the thing?"]),
        n, kicker=cd.eco("Process", 3), lc=BLUE, rc=ROSE,
        footer_note="A single project can have a predictive project life cycle for "
                    "governance while using an agile development life cycle inside "
                    "the build phase — that combination is a hybrid."); n += 1

    # ------------------------------------------ 14. generic project life cycle timeline
    X.timeline(
        prs, "The generic project life cycle and its effort profile",
        [("Starting the project", "Charter approved, sponsor named, high-level scope and "
                                  "stakeholders identified. Cost and staffing are low."),
         ("Organising & preparing", "The integrated plan is built. Effort ramps up and "
                                    "the ability to influence outcome is still high."),
         ("Carrying out the work", "The bulk of cost and staffing. Changes here are "
                                   "expensive; risk decreases as work is completed."),
         ("Ending the project", "Acceptance, transition, procurement and financial "
                                "closure, lessons learned, release of the team.")],
        n, kicker=cd.eco(BE, 1), accent=TEAL,
        note="Risk and stakeholder influence are highest at the start; the cost of "
             "change is highest at the end. That single relationship explains most of "
             "PMI's guidance on planning and early engagement."); n += 1

    # ------------------------------------------ 15. cost of change curve chart
    X.chart(
        prs, "Why early decisions dominate: risk, influence and the cost of change",
        "line",
        ["Initiation", "Planning", "Early execution", "Mid execution",
         "Late execution", "Closing"],
        [("Stakeholder influence & risk", [95, 80, 58, 38, 18, 5]),
         ("Cost of making a change", [5, 15, 35, 60, 88, 98])],
        n, kicker=cd.eco("Process", 3), accent=ROSE,
        insight=["The two curves cross early — after that point, changes cost more "
                 "than the influence they buy.",
                 "This is the mathematical argument for investing in requirements "
                 "and stakeholder engagement up front.",
                 "Agile flattens the cost-of-change curve by keeping increments "
                 "small and reversible rather than by planning harder.",
                 "Exam cue: 'the change was requested late in execution' signals a "
                 "formal impact analysis, not immediate action."]); n += 1

    # ------------------------------------- 16. common life cycle definitions table
    X.table(
        prs, "Common life cycle definitions — the vocabulary PMI uses",
        ["Life cycle", "Requirements", "Delivery", "Goal / when to use"],
        [["Predictive", "Fixed and baselined up front",
          "One delivery at the end", "Manage cost — best when the solution is well "
          "understood and change is expensive"],
         ["Iterative", "Dynamic; refined each cycle",
          "One final delivery, repeated refinement", "Correctness of the solution — "
          "prototype until the right thing is understood"],
         ["Incremental", "Dynamic; decomposed into slices",
          "Frequent smaller usable deliveries", "Speed to value — customer gets working "
          "capability before the whole is finished"],
         ["Adaptive / agile", "Dynamic, in a prioritised backlog",
          "Frequent delivery via short timeboxes", "Customer value through fast "
          "feedback — best under high uncertainty"],
         ["Hybrid", "Mixed by component or phase",
          "Mixed cadence across the project", "Fit the approach to each part — the "
          "most common shape in real organisations"]],
        n, kicker=cd.eco("Process", 3), accent=BLUE, widths=[1.1, 1.4, 1.3, 2.4],
        note="Memory hook: iterative improves the same thing repeatedly; incremental "
             "adds new usable pieces. Agile deliberately does both at once."); n += 1

    # ------------------------------------------ 17. development approaches process
    X.process(
        prs, "The development approach continuum, from most to least predictive",
        [("Predictive", "Full scope defined up front, single delivery at the end, "
                        "change controlled formally through a change board."),
         ("Iterative", "Repeated cycles refine one solution until it is right; the "
                       "delivery to the customer still happens once."),
         ("Incremental", "Successive usable slices are handed over, each adding "
                         "functionality to what the customer already has."),
         ("Adaptive / Agile", "Short timeboxes deliver working increments while the "
                              "backlog is continuously reprioritised on feedback."),
         ("Hybrid", "Deliberately combines approaches — for example predictive "
                    "infrastructure alongside an agile application build.")],
        n, kicker=cd.eco("Process", 3), accent=VIOLET,
        note="The approach is a tailoring decision, not an identity. PMI expects you "
             "to justify it from requirements certainty, risk, regulatory constraint "
             "and how quickly value can be delivered."); n += 1

    # --------------------------------------------------------- 18. project cadence
    X.cards(
        prs, "Project cadence — the timing and frequency of delivery",
        [("Single delivery",
          "One handover at the very end of the project. Typical of construction, "
          "regulated pharmaceuticals and large infrastructure."),
         ("Multiple deliveries",
          "Work is separated into parts released as they complete, not necessarily in a "
          "fixed sequence or on a fixed calendar."),
         ("Periodic delivery",
          "Multiple deliveries released on a fixed drumbeat — monthly, bi-monthly or "
          "every sprint — which makes planning predictable."),
         ("Continuous delivery",
          "Every accepted change flows to production as it is ready, supported by "
          "automated testing and deployment pipelines."),
         ("Cadence versus approach",
          "Cadence is about when the customer receives value; the development approach "
          "is about how the work is produced."),
         ("Why it matters",
          "Cadence drives the release plan, the funding profile, and how often the "
          "benefits measurement system must be read.")],
        n, kicker=cd.eco("Process", 3), accent=CYAN); n += 1

    # ------------------------------------------- 19. agile = incremental + iterative
    X.statement(
        prs, "The definition you must be able to state cold",
        "Agile is both incremental — small, regular releases of value — and "
        "iterative — reflecting and improving regularly.",
        [("INCREMENTAL", "Each sprint hands over a potentially releasable increment, so "
                         "the customer accrues real value long before the end."),
         ("ITERATIVE", "Each sprint also revisits and refines what exists, and the "
                       "retrospective refines how the team works."),
         ("THE COMBINATION", "Doing only one of the two is not agile: increments without "
                             "reflection stagnate; reflection without increments stalls.")],
        n, kicker="Agile fundamentals", accent=TEAL); n += 1

    # ------------------------------------------------- 20. waterfall vs agile compare
    X.compare(
        prs, "Predictive (waterfall) versus adaptive (agile) delivery",
        ("PREDICTIVE / WATERFALL", "Plan the work, then work the plan",
         ["Requirements are gathered once, then baselined and frozen",
          "Design, build and test are performed once, in sequence",
          "Success is conformance to the approved scope, schedule and budget",
          "Change is a formal event requiring a change request and CCB approval",
          "Detailed documentation is produced and is itself a deliverable",
          "Customer sees the working product late, usually at UAT"]),
        ("ADAPTIVE / AGILE", "Inspect and adapt, every timebox",
         ["Requirements live in a backlog and are refined continuously",
          "Design, build and test are performed once per increment",
          "Success is working product and realised customer value",
          "Change is expected and absorbed by reprioritising the backlog",
          "Working software is favoured over comprehensive documentation",
          "Customer sees working product at the end of every sprint"]),
        n, kicker=cd.eco("Process", 3), lc=BLUE, rc=ROSE,
        footer_note="Predictive performs the full life cycle once; adaptive performs "
                    "it once per increment. That single sentence answers a surprising "
                    "number of exam questions."); n += 1

    # ----------------------------------------------- 21. complexity / uncertainty
    X.matrix2x2(
        prs, "The Stacey model — matching approach to complexity and uncertainty",
        "TECHNOLOGY / HOW  →  uncertain",
        "REQUIREMENTS / WHAT  →  uncertain",
        [("Complicated", "Requirements are unclear but technology is known. Use "
          "iterative or incremental cycles to converge on the right scope.", AMBER),
         ("Complex", "Both what and how are uncertain. Agile with short feedback "
          "loops and small safe-to-fail experiments is the fit.", ROSE),
         ("Simple", "Both what and how are well understood. Predictive delivery is "
          "efficient and the cheapest option to govern.", BLUE),
         ("Complicated (technical)", "The what is clear but the how is not. Use "
          "spikes, prototypes and iterative technical proving.", VIOLET)],
        n, kicker=cd.eco("Process", 3), accent=ROSE,
        note="Agile is suited to high-uncertainty work. Using agile on genuinely "
             "simple, well-understood work adds ceremony without buying any "
             "information."); n += 1

    # --------------------------------------------------- 22. agile manifesto values
    X.compare(
        prs, "The Agile Manifesto (2001) — four values, stated as preferences",
        ("WE VALUE MORE", "The left-hand side of each pairing",
         ["Individuals and interactions",
          "Working software (working product)",
          "Customer collaboration",
          "Responding to change",
          "Seventeen practitioners agreed these in Snowbird, Utah in 2001",
          "The values sit above the 12 principles and all frameworks"]),
        ("OVER", "The right-hand side still has value",
         ["… over processes and tools",
          "… over comprehensive documentation",
          "… over contract negotiation",
          "… over following a plan",
          "'While there is value in the items on the right, we value the "
          "items on the left more'",
          "Agile never says documentation or plans are worthless"]),
        n, kicker="Agile Manifesto", lc=VIOLET, rc=CYAN,
        footer_note="Exam trap: an option saying agile teams do not plan or do not "
                    "document is always wrong. Agile teams plan more often, in "
                    "smaller pieces, and document what is genuinely useful."); n += 1

    # ---------------------------------------- 23-24. 12 agile principles, two slides
    X.cards(
        prs, "The 12 Agile Principles (1 of 2)",
        [("Satisfy the customer early",
          "Highest priority is satisfying the customer through early and continuous "
          "delivery of valuable software."),
         ("Welcome changing requirements",
          "Even late in development; agile processes harness change for the customer's "
          "competitive advantage."),
         ("Deliver frequently",
          "Deliver working product from a couple of weeks to a couple of months, with a "
          "preference for the shorter timescale."),
         ("Business and developers together",
          "Business people and developers must work together daily throughout the "
          "project, not meet at handover points."),
         ("Build around motivated individuals",
          "Give them the environment and support they need, and trust them to get the "
          "job done."),
         ("Face-to-face conversation",
          "The most efficient and effective method of conveying information within a "
          "development team.")],
        n, kicker="Agile principles", accent=TEAL); n += 1

    X.cards(
        prs, "The 12 Agile Principles (2 of 2)",
        [("Working product is the measure",
          "Working software is the primary measure of progress — not percentage "
          "complete, not documents produced."),
         ("Sustainable pace",
          "Sponsors, developers and users should be able to maintain a constant pace "
          "indefinitely; heroics are a warning sign."),
         ("Technical excellence",
          "Continuous attention to technical excellence and good design enhances "
          "agility and keeps future change cheap."),
         ("Simplicity",
          "The art of maximising the amount of work not done — building only what is "
          "needed is essential."),
         ("Self-organising teams",
          "The best architectures, requirements and designs emerge from self-organising "
          "teams, not from imposed plans."),
         ("Reflect and adjust",
          "At regular intervals the team reflects on how to become more effective, then "
          "tunes and adjusts its behaviour.")],
        n, kicker="Agile principles", accent=AMBER); n += 1

    # -------------------------------------------------------- 25. Scrum overview
    X.cards(
        prs, "Scrum — the most widely used agile framework",
        [("Product Owner",
          "Owns and prioritises the product backlog, represents the business, and is "
          "accountable for maximising the value the team delivers."),
         ("Scrum Master",
          "Facilitates the events, coaches the team on Scrum, removes impediments, and "
          "shields the team from outside interference."),
         ("Development Team",
          "Three to nine cross-functional people who self-organise to turn backlog items "
          "into a done increment each sprint."),
         ("Product Backlog",
          "The single ordered list of everything that might be needed, continuously "
          "refined and re-ordered by the Product Owner."),
         ("Sprint Backlog",
          "The subset the team commits to this sprint, plus the plan for delivering it; "
          "owned entirely by the development team."),
         ("Increment",
          "The sum of all completed backlog items this sprint plus all prior sprints, in "
          "a potentially releasable state.")],
        n, kicker="Scrum roles and artifacts", accent=VIOLET); n += 1

    # ------------------------------------------------ 26. sprint / ceremonies process
    X.process(
        prs, "The sprint — Scrum events in the order they occur",
        [("Sprint Planning", "The team pulls backlog items into the sprint and agrees "
                             "the sprint goal. Timeboxed to 8 hours for a month sprint."),
         ("Daily Scrum", "A 15-minute timeboxed sync where the team inspects progress "
                         "toward the sprint goal and replans the next 24 hours."),
         ("Development Work", "The team builds the increment, refining the backlog for "
                              "future sprints as it goes."),
         ("Sprint Review", "The team demonstrates the increment to stakeholders and the "
                           "backlog is adapted based on their feedback."),
         ("Sprint Retrospective", "The team inspects how it worked and commits to "
                                  "specific improvements for the next sprint.")],
        n, kicker=cd.eco("Process", 3), accent=CYAN,
        note="A sprint is a timebox of one month or less. Its length is fixed, its "
             "scope is not — the sprint end date never moves to accommodate "
             "unfinished work."); n += 1

    # ------------------------------------------------ 27. other agile ceremonies
    X.cards(
        prs, "Agile ceremonies beyond the core Scrum events",
        [("Product strategy meeting",
          "The Product Owner shares the product vision and roadmap so the team "
          "understands why the backlog is ordered the way it is."),
         ("Backlog refinement (grooming)",
          "An ongoing session where items are clarified, split, estimated and "
          "re-ordered so the top of the backlog is always ready."),
         ("Daily standup",
          "Five to fifteen minutes, timeboxed, and not necessarily daily on every team — "
          "the purpose is coordination, not status reporting."),
         ("Release planning",
          "Maps multiple sprints to a release date so stakeholders outside the team can "
          "plan marketing, training and operations."),
         ("Project retrospective",
          "Held at the end of the project to review both the work and the process — the "
          "agile equivalent of lessons learned."),
         ("Demo or showcase",
          "An informal review with wider stakeholders, used to gather feedback before "
          "committing to the next block of work.")],
        n, kicker=cd.eco("Process", 3), accent=BLUE); n += 1

    # ------------------------------------------------------- 28. retrospective process
    X.process(
        prs, "Running a retrospective that actually changes behaviour",
        [("Set the stage", "Establish psychological safety and remind everyone the aim "
                           "is improvement of the system, not blame of individuals."),
         ("Gather data", "Collect facts about the sprint — metrics, events, incidents — "
                         "so opinions can be anchored to evidence."),
         ("Generate insights", "Ask why the data looks as it does; use root cause tools "
                               "such as 5 Whys or a fishbone diagram."),
         ("Decide what to do", "Choose one or two improvements the team can genuinely "
                               "complete in the next sprint."),
         ("Close the retrospective", "Confirm the actions, name owners, and put them "
                                     "into the next sprint backlog so they are real work.")],
        n, kicker=cd.eco(BE, 6), accent=ROSE,
        note="A retrospective with no action items in the next sprint backlog is "
             "theatre. Track improvement actions with the same rigour as feature "
             "work."); n += 1

    # ---------------------------------------------------------- 29. project team
    X.cards(
        prs, "The project team — makeup, sourcing and skills",
        [("Team composition",
          "Refers to the team's makeup and how members are brought together; it varies "
          "with organisational culture, location and project scope."),
         ("Full-time and part-time",
          "Members may be dedicated or shared. Shared members multitask, which reduces "
          "throughput and increases handover risk."),
         ("Generalists and specialists",
          "Specialists bring depth for hard problems; generalists give the team the "
          "flexibility to redistribute work when plans change."),
         ("Avoid single points of failure",
          "If only one person holds a required skill, their absence stops the project — "
          "cross-train deliberately."),
         ("Cross-functional teams",
          "A team that contains every skill needed to take an item from idea to done "
          "removes waiting on external groups."),
         ("T-shaped people",
          "Generalising specialists with one deep specialty plus broad general skills — "
          "the most valuable shape for agile teams.")],
        n, kicker="People and teams", accent=TEAL); n += 1

    # ------------------------------------------------------------ 30. agile teams
    X.cards(
        prs, "Agile team characteristics and the agile team space",
        [("Small",
          "Typically three to twelve members. Communication paths grow quadratically, so "
          "large teams spend their capacity coordinating."),
         ("Co-located or well-connected",
          "Physical or virtual co-location creates an osmotic environment where useful "
          "information is absorbed without a meeting."),
         ("Dedicated",
          "100% allocated to one team to avoid multitasking, which is the single largest "
          "source of hidden delay in knowledge work."),
         ("Information radiators",
          "Burndown charts, Kanban boards and impediment lists on display, so status is "
          "visible at a glance without a report."),
         ("Pairing",
          "Two people work on one item together, checking each other's thinking and "
          "spreading knowledge as a side effect."),
         ("Swarming",
          "Multiple team members converge on one blocked or high-value item to finish it "
          "fast rather than starting new work.")],
        n, kicker="Agile teams", accent=CYAN); n += 1

    # ------------------------------------------------------ 31. agile team roles
    X.table(
        prs, "Agile team roles and their traditional equivalents",
        ["Agile role", "What they do", "Closest predictive equivalent"],
        [["Product Owner", "Represents the customer and business, owns and prioritises "
          "the product backlog, accepts or rejects each increment",
          "Business analyst plus sponsor's delegate"],
         ["Team Facilitator", "Also called Scrum Master, agile lead, team coach or "
          "servant leader; runs ceremonies, removes blockers, grows the team",
          "Project manager (facilitation half of the role)"],
         ["Cross-functional member", "Generalising specialists — T-shaped people who "
          "self-organise to deliver the increment end to end",
          "Team member from a functional department"],
         ["Agile Coach", "Works across several teams on practice maturity and "
          "organisational impediments beyond a single team",
          "PMO methodology lead"],
         ["Stakeholder / customer", "Attends reviews, supplies the feedback that "
          "re-orders the backlog, and confirms value is real",
          "Steering committee member or end user"]],
        n, kicker="Agile roles", accent=VIOLET, widths=[1.1, 2.6, 1.6],
        note="Note what is missing: agile has no role that assigns tasks to "
             "individuals. Work is pulled by the team, not pushed by a manager."); n += 1

    # ---------------------------------------------------------- 32. tailoring
    X.statement(
        prs, "Tailoring — the principle that makes everything else practical",
        "We can, and should, tailor anything on our project so it meets the "
        "outcomes and delivers business value.",
        [("PROCESS", "The development approach, the number of phases, the depth of "
                     "planning and the frequency of governance reviews."),
         ("ARTIFACTS", "Which plans, registers and reports genuinely help — and which "
                       "exist only because a template said so."),
         ("METHODS & TOOLS", "The estimating techniques, meeting formats, tooling and "
                             "metrics that fit this team and this context.")],
        n, kicker=cd.eco(BE, 1), accent=AMBER); n += 1

    # ------------------------------------------------------ 33. tailoring approach
    X.process(
        prs, "The four-step tailoring approach",
        [("Select the initial approach", "Choose predictive, adaptive or hybrid based on "
                                         "requirements certainty, risk and delivery cadence."),
         ("Tailor for the organisation", "Adjust for the organisation's methodology, "
                                         "PMO requirements, governance and regulatory obligations."),
         ("Tailor for the project", "Adjust for product type, culture, team size and "
                                    "criticality — a safety-critical build needs more rigour."),
         ("Implement ongoing improvement", "Inspect the tailored process at retrospectives "
                                           "and adjust it as the project and team mature.")],
        n, kicker=cd.eco(BE, 6), accent=BLUE,
        note="Tailoring is not permission to skip work you find inconvenient. Every "
             "removal should be a reasoned decision you could defend to the sponsor "
             "or an auditor."); n += 1

    # --------------------------------------------------- 34. types of managers
    X.cards(
        prs, "Types of managers — who owns what in the organisation",
        [("Project Manager",
          "Assigned by the performing organisation to lead the team responsible for "
          "achieving the project objectives and delivering business value."),
         ("Functional Manager",
          "Manages a functional or business unit and provides the people, skills and "
          "physical resources the project consumes."),
         ("Operations Manager",
          "Responsible for ensuring ongoing business operations run efficiently, and "
          "receives the project's output at transition."),
         ("Program Manager",
          "Coordinates related projects to obtain benefits not available from managing "
          "them individually, and resolves cross-project conflicts."),
         ("Portfolio Manager",
          "Selects and balances the mix of programs and projects so the investment "
          "aligns with organisational strategy."),
         ("Product Manager",
          "Owns a product across its whole life — well before a project starts and long "
          "after it closes — driving the roadmap and value.")],
        n, kicker=cd.eco(BE, 1), accent=TEAL); n += 1

    # ------------------------------------------------- 35. product management compare
    X.compare(
        prs, "Product management versus project management",
        ("PRODUCT MANAGEMENT", "Continuous, value-and-market driven",
         ["Spans the entire product life cycle, potentially for years",
          "Owns the vision, roadmap and the ordered backlog of value",
          "Measures success by adoption, revenue, retention and outcomes",
          "Funding is often a standing capacity, not a one-off approval",
          "Ends only when the product is retired from the market",
          "Asks: are we building the right thing?"]),
        ("PROJECT MANAGEMENT", "Temporary, delivery-and-constraint driven",
         ["Spans one temporary endeavour with a defined start and end",
          "Owns the plan, the baselines and the delivery of agreed scope",
          "Measures success by scope, schedule, cost, quality and benefits",
          "Funding is approved against a specific business case",
          "Ends at acceptance, transition and administrative closure",
          "Asks: are we building the thing right?"]),
        n, kicker=cd.eco("Process", 3), lc=ROSE, rc=BLUE,
        footer_note="Organisations increasingly fund persistent product teams rather "
                    "than discrete projects — the PMP now expects you to operate "
                    "comfortably in both models."); n += 1

    # ------------------------------------------------- 36. PM influence / structures
    X.table(
        prs, "Organisational structure and project manager authority",
        ["Structure", "PM authority", "PM role", "Resource control"],
        [["Functional", "Little or none", "Part-time coordinator",
          "Functional manager controls the budget and the people"],
         ["Weak matrix", "Low", "Part-time expediter or coordinator",
          "Functional manager still controls the budget"],
         ["Balanced matrix", "Low to moderate", "Full-time project manager",
          "Budget is shared between PM and functional manager"],
         ["Strong matrix", "Moderate to high", "Full-time project manager",
          "Project manager controls the budget"],
         ["Projectised", "High to almost total", "Full-time project manager",
          "Project manager controls budget and staff entirely"],
         ["Hybrid / composite", "Varies by project", "Varies",
          "Mixed — the most common real-world arrangement"]],
        n, kicker=cd.eco(BE, 1), accent=VIOLET, widths=[1.3, 1.2, 1.8, 2.4],
        note="If an exam scenario says the PM has no authority over resources, you "
             "are in a functional or weak matrix — the correct action is almost "
             "always to negotiate with the functional manager."); n += 1

    # -------------------------------------------------------------- 37. PMO types
    X.table(
        prs, "Project Management Office types and their degree of control",
        ["PMO type", "Authority and control", "What it provides"],
        [["Supportive", "Low degree of control — consultative",
          "Serves as a project repository; supplies templates, best practices, "
          "training and information from other projects"],
         ["Controlling", "Moderate degree of control — compliance",
          "Provides support and ensures compliance through adoption of methods, "
          "frameworks, specific templates, forms and tools"],
         ["Directive", "High degree of control — direct management",
          "Takes control by directly managing the projects; project managers are "
          "assigned by and report into the PMO"],
         ["Agile / value delivery office", "Enabling rather than controlling",
          "Coaches teams, removes organisational impediments and reports on flow and "
          "benefits rather than on plan conformance"]],
        n, kicker=cd.eco(BE, 1), accent=AMBER, widths=[1.4, 1.7, 3.2],
        note="Memory hook: Supportive suggests, Controlling checks, Directive "
             "directs. The exam tests which one owns the project manager."); n += 1

    # ------------------------------------------------------ 38. PESTLE / TECOP / VUCA
    X.cards(
        prs, "Reading the external business environment: PESTLE, TECOP and VUCA",
        [("PESTLE",
          "Political, Economic, Socio-cultural, Technological, Legal and Environmental "
          "forces — the standard scan of the macro environment."),
         ("TECOP",
          "Technical, Environmental, Commercial, Operational and Political — a risk-"
          "oriented scan used heavily in engineering and construction."),
         ("VUCA",
          "Volatility, Uncertainty, Complexity and Ambiguity — describes the character "
          "of the environment rather than listing its factors."),
         ("Why the PM does this",
          "External change can invalidate the business case mid-project; scanning turns "
          "an ambush into a managed risk with a response."),
         ("How often",
          "Not once at initiation. ECO T8 requires the PM to continually review the "
          "external environment for impacts to scope and backlog."),
         ("What you do with it",
          "Feed findings into the risk register, reprioritise the backlog, and escalate "
          "anything that threatens the business case.")],
        n, kicker=cd.eco(BE, 8), accent=CYAN); n += 1

    # -------------------------------------- 39. external change response process
    X.process(
        prs, "Responding to a change in the external business environment",
        [("Survey", "Continuously scan regulations, technology, geopolitics, "
                    "competitors and market conditions relevant to the project."),
         ("Assess impact", "Determine what the change does to scope, backlog, business "
                           "case, benefits, risk exposure and compliance obligations."),
         ("Prioritise", "Rank the impact against other demands; not every external "
                        "change deserves a response this quarter."),
         ("Act or escalate", "Reprioritise the backlog within your authority, or raise a "
                             "change request and escalate beyond your threshold."),
         ("Review continually", "Re-check the environment on a defined cadence and "
                                "update the risk register and the plan accordingly.")],
        n, kicker=cd.eco(BE, 8), accent=ROSE,
        note="Classic exam scenario: a new regulation is announced mid-project. The "
             "best first action is to assess the impact on the project — not to stop "
             "work, and not to immediately change scope."); n += 1

    # ------------------------------------------------------------ 40. EEF vs OPA
    X.compare(
        prs, "Enterprise Environmental Factors versus Organizational Process Assets",
        ("EEF — conditions you must live with", "Usually inputs; largely outside your control",
         ["Internal: resource capabilities, organisational culture, IT systems, "
          "distribution of facilities, employee capability",
          "External: marketplace conditions, laws, regulations and standards",
          "External: operating conditions, social and cultural influences",
          "Government or industry standards you cannot negotiate away",
          "Risk tolerances and the organisation's appetite for change",
          "You adapt the project to EEFs; you rarely change them"]),
        ("OPA — knowledge you can reuse", "Inputs and outputs; you can and should update them",
         ["Processes, policies and procedures: organisational charts, procurement "
          "rules, hiring and onboarding procedures",
          "Templates, checklists, standardised WBS structures and forms",
          "Organisational knowledge bases: engineering wikis, libraries, archives",
          "Lessons learned repositories and historical estimating databases",
          "Configuration management and financial control procedures",
          "ECO T6 requires you to update OPAs — they are an output too"]),
        n, kicker=cd.eco(BE, 1), lc=BLUE, rc=TEAL,
        footer_note="Fastest test: can the project change it? If yes it is usually an "
                    "OPA. If the project must simply conform to it, it is an EEF."); n += 1

    # ------------------------------------------------------- 41. EEF/OPA exam drill
    X.exam(
        prs, "Exam drill: classify these as EEF or OPA",
        [("Economic demand for a new shopping area; local neighbourhood demand for a "
          "better town centre",
          "EEF — external marketplace and social conditions the project must respond "
          "to but cannot change."),
         ("Historical society conservation building regulations affecting the site",
          "EEF — a legal and regulatory constraint from outside the organisation; it "
          "becomes a compliance requirement."),
         ("An archive of past large infrastructure projects held by your company",
          "OPA — a knowledge base and historical information repository you can mine "
          "for estimates and lessons."),
         ("The approved vendor and contractor list, and the tenant selection process",
          "OPA — internal processes, policies and procedures the organisation "
          "maintains and the project must apply.")],
        n, kicker="EEF vs OPA", accent=AMBER); n += 1

    # ------------------------------------------------- 42. org culture assessment
    X.cards(
        prs, "Assessing organisational culture — what to actually look at",
        [("Leadership, hierarchy and authority",
          "How decisions get made and how far they must travel. This directly sets your "
          "realistic escalation lead time."),
         ("Shared vision, beliefs and expectations",
          "What people believe the organisation is for. A project that contradicts this "
          "will meet quiet, persistent resistance."),
         ("Diversity, equity and inclusion practices",
          "Whether varied perspectives are genuinely sought; this shapes team formation "
          "and the quality of risk identification."),
         ("Risk tolerance and appetite",
          "How much uncertainty the organisation will accept determines your reserve "
          "levels and your response strategies."),
         ("Regulations, policies and code of conduct",
          "The formal rules of the road, including the ethical standards the team is "
          "expected to uphold without supervision."),
         ("Motivation and reward systems",
          "What behaviour actually gets rewarded. If individuals are rewarded, a team "
          "incentive scheme will not stick.")],
        n, kicker=cd.eco(BE, 7), accent=VIOLET); n += 1

    # ---------------------------------------- 43. change management statement
    X.statement(
        prs, "Why change management belongs to the project manager",
        "Organisational change requires individual change — a delivered output "
        "that nobody adopts has produced exactly zero value.",
        [("YOU ARE A CHANGEMAKER", "Whether or not your organisation has a PMO, the "
                                   "project manager is the person driving change into the business."),
         ("TAILOR THE STRATEGY", "Change approach must fit the circumstances, the people "
                                 "affected and the timing — there is no universal script."),
         ("USE A ROBUST APPROACH", "Structured models such as ADKAR give you a checklist "
                                   "you can measure adoption against, not just good intentions.")],
        n, kicker=cd.eco(BE, 7), accent=ROSE); n += 1

    # ------------------------------------------------------- 44. ADKAR process
    X.process(
        prs, "The ADKAR model — five milestones an individual must reach",
        [("Awareness", "The person understands why the change is needed. Address this "
                       "with communication from a credible, senior sponsor."),
         ("Desire", "The person chooses to support the change. Address this by making "
                    "the personal 'what's in it for me' explicit and honest."),
         ("Knowledge", "The person knows how to change. Address this with training, "
                       "documentation and worked examples."),
         ("Ability", "The person can demonstrate the new skills and behaviours. Address "
                     "this with coaching, practice time and hands-on support."),
         ("Reinforcement", "The change sticks. Address this with recognition, metrics "
                           "and removal of the old way of working.")],
        n, kicker=cd.eco(BE, 7), accent=TEAL,
        note="Diagnostic power: if adoption is failing, find the first milestone the "
             "person has not reached. More training will never fix a Desire problem."); n += 1

    # ------------------------------------------------------- 45. plan for change
    X.cards(
        prs, "Plan for change — the practical activities to build into your plan",
        [("Define readiness activities",
          "Specify the knowledge transfer, training and readiness work required to "
          "implement the change the project brings."),
         ("Run an attitudinal survey",
          "Find out how affected people actually feel before go-live, so resistance is "
          "measured rather than assumed away."),
         ("Create an information campaign",
          "Familiarise people with the coming change over time; a single announcement "
          "email is not a communication plan."),
         ("Be open about effects",
          "Transparent about the potential negative effects too — hidden bad news "
          "destroys the trust the change depends on."),
         ("Create a rollout plan",
          "Sequence adoption by group, region or business unit so support capacity "
          "matches the number of people changing at once."),
         ("Measure adoption",
          "Define adoption metrics up front and track them after go-live; benefits "
          "realisation depends on them, not on delivery.")],
        n, kicker=cd.eco(BE, 7), accent=CYAN); n += 1

    # ------------------------------- 46. internal org change impacts on the project
    X.cards(
        prs, "When the organisation changes around your project",
        [("Reorganisations",
          "A new reporting structure can remove your sponsor or reassign your team "
          "mid-flight; re-confirm authority immediately."),
         ("Strategy or priority shifts",
          "A change in strategic direction can reprioritise value, including removing "
          "deliverables you have already built."),
         ("New deliverables demanded",
          "Internal business changes frequently create a need for deliverables that were "
          "never in the approved baseline."),
         ("Process changes",
          "New internal processes may change how you must procure, hire, report or "
          "release — check them before you are blocked."),
         ("Stay informed",
          "The PM, sponsor or product owner must be familiar with business plans, "
          "reorganisations and other internal activity."),
         ("Recommend options",
          "Assess the impact, then recommend options for changes to the project rather "
          "than presenting a single fait accompli.")],
        n, kicker=cd.eco(BE, 7), accent=AMBER); n += 1

    # -------------------------------------------------------- 47. governance defined
    X.statement(
        prs, "Project governance",
        "The framework of structures, rules, procedures, reporting and ethics "
        "within which project decisions are legitimately made.",
        [("SINGLE ACCOUNTABILITY", "Governance offers one clear point of accountability "
                                   "for the project, so decisions do not orbit unowned."),
         ("SPANS THE LIFE CYCLE", "It encompasses the whole project life cycle, from "
                                  "authorisation through phase gates to closure."),
         ("ALREADY EXISTS", "Governance is typically already in place — established by a "
                            "PMO or aligned to organisational policy; you inherit it.")],
        n, kicker=cd.eco(BE, 1), accent=BLUE); n += 1

    # ---------------------------------------------------- 48. governance board cards
    X.cards(
        prs, "The governance board and what it is responsible for",
        [("Who sits on it",
          "Typically the project sponsor, senior managers from affected business units, "
          "and PMO resources; sometimes customer representatives."),
         ("Provides oversight",
          "Independent oversight of whether the project remains viable, compliant and "
          "aligned to the strategy that funded it."),
         ("Reviews key deliverables",
          "Formally reviews and accepts major deliverables at defined checkpoints rather "
          "than only at the very end."),
         ("Guides project decisions",
          "Provides direction on decisions that exceed the project manager's delegated "
          "authority or cross business unit boundaries."),
         ("Approves changes above threshold",
          "Acts as, or feeds into, the change control board for changes larger than the "
          "PM can approve alone."),
         ("Governance varies",
          "Its type and intensity depend on the project's strategic importance, "
          "constraints and external oversight requirements.")],
        n, kicker=cd.eco(BE, 1), accent=VIOLET); n += 1

    # ---------------------------------------------- 49. escalation process
    X.process(
        prs, "Governance defines escalation — the thresholds decision path",
        [("Detect the deviation", "An issue, risk or change is identified that may push "
                                  "the project outside its agreed tolerance."),
         ("Test against threshold", "Compare the impact to the documented tolerance for "
                                    "cost, schedule, scope, quality and risk."),
         ("Within threshold", "Work with the team to find a resolution and record the "
                              "decision; do not consume sponsor attention unnecessarily."),
         ("Outside threshold", "Escalate to the stakeholder who is authorised to act, "
                               "with options and a recommendation, not just a problem."),
         ("Record and communicate", "Log the decision, update the plan and registers, "
                                    "and inform everyone affected by the outcome.")],
        n, kicker=cd.eco(BE, 1), accent=ROSE,
        note="Escalating everything makes you look incapable; escalating nothing makes "
             "you look reckless. The written threshold is what makes the difference "
             "defensible."); n += 1

    # ------------------------------------------------------- 50. success metrics
    X.formula(
        prs, "Defining project success metrics that governance can act on",
        [("Schedule performance", "SPI = EV ÷ PV",
          "Below 1.00 means the project is earning value more slowly than planned; a "
          "common governance threshold is SPI below 0.90."),
         ("Cost performance", "CPI = EV ÷ AC",
          "Below 1.00 means each dollar spent is buying less value than planned; often "
          "escalated when CPI falls below 0.90."),
         ("Benefit realisation", "BRR = Actual ÷ Planned benefit",
          "Measured after transition to operations; it is the metric that proves the "
          "business case was real, not merely persuasive."),
         ("Return on investment", "ROI = (Benefit − Cost) ÷ Cost",
          "The financial justification governance used to fund the project; re-check it "
          "whenever scope or cost changes materially."),
         ("Compliance level", "% requirements evidenced",
          "The share of identified compliance requirements with current, auditable "
          "evidence — the measure ECO T2 asks for.")],
        n, kicker=cd.eco(BE, 1), accent=AMBER,
        note="ECO Business Environment T1 explicitly requires you to define success "
             "metrics and escalation thresholds. Vague metrics make governance "
             "ceremonial."); n += 1

    # ------------------------------------------------------- 51. phase gates timeline
    X.timeline(
        prs, "Governance checkpoints: phase gates in a predictive project",
        [("Concept gate", "Is the idea worth investigating? The business case is "
                          "outline only and the estimate is order-of-magnitude."),
         ("Planning gate", "Is the plan credible and funded? Baselines are approved and "
                           "the estimate tightens to a definitive range."),
         ("Build gate", "Is the solution being produced to spec? Design is frozen and "
                        "major deliverables are formally reviewed."),
         ("Readiness gate", "Is the organisation ready to receive it? Testing, training "
                            "and compliance evidence are confirmed."),
         ("Closure gate", "Have benefits started and is everything transitioned? "
                          "Contracts, finances and lessons learned are closed out.")],
        n, kicker=cd.eco(BE, 1), accent=TEAL,
        note="At every gate the decision is one of four: continue, continue with "
             "modification, hold and re-plan, or terminate. 'Continue because we have "
             "already spent the money' is the sunk cost fallacy."); n += 1

    # ------------------------------------------- 52. phase relationships compare
    X.compare(
        prs, "Project phase relationships — sequential versus overlapping",
        ("SEQUENTIAL PHASES", "One phase completes before the next begins",
         ["Each phase ends at a gate that must be passed to continue",
          "Lowest risk of rework because each stage is confirmed before build",
          "Longest overall duration — no phase runs in parallel",
          "Preferred where safety, regulation or irreversibility dominates",
          "Clearest governance because decisions are discrete events",
          "Change late in the sequence is the most expensive kind"]),
        ("OVERLAPPING PHASES", "The next phase starts before the prior one ends",
         ["Known as fast tracking; used to compress the total schedule",
          "Increases risk of rework because assumptions may prove wrong",
          "Requires far more communication between the overlapping teams",
          "Governance gates become partial or conditional approvals",
          "Common in construction and product development under time pressure",
          "The PM must explicitly accept and reserve for the rework risk"]),
        n, kicker=cd.eco("Process", 3), lc=BLUE, rc=AMBER,
        footer_note="In adaptive delivery, the equivalent checkpoint is the sprint "
                    "review — governance moves from a rare heavyweight gate to a "
                    "frequent lightweight inspection of a working increment."); n += 1

    # ---------------------------------------------- 53. governance predictive vs agile
    X.compare(
        prs, "Applying governance in predictive versus adaptive projects",
        ("PREDICTIVE GOVERNANCE", "Few, heavy, document-based checkpoints",
         ["Phase gate reviews at defined milestones in the schedule",
          "Evidence is documentation: plans, designs, test reports, sign-offs",
          "Change control board approves deviations from the baseline",
          "Status reported against percentage complete and earned value",
          "Escalation follows a documented threshold and hierarchy",
          "Benefits are typically confirmed after the whole project closes"]),
        ("ADAPTIVE GOVERNANCE", "Many, light, product-based checkpoints",
         ["Sprint review at the end of every timebox, with stakeholders present",
          "Evidence is a working increment that can be inspected directly",
          "The Product Owner reprioritises the backlog instead of raising CRs",
          "Status reported through burndown, velocity and cumulative flow",
          "Impediments escalated immediately by the team facilitator",
          "Benefits can be measured from the first released increment"]),
        n, kicker=cd.eco(BE, 1), lc=BLUE, rc=VIOLET,
        footer_note="The governance obligation is identical in both; only the "
                    "frequency, the artefacts and the evidence change. Regulated "
                    "industries still require agile teams to produce audit trails."); n += 1

    # -------------------------------------------------------- 54. value-based delivery
    X.statement(
        prs, "Value-based delivery — the reason the project exists",
        "Value is the worth, importance or usefulness of the output to the "
        "organisation and its stakeholders — not the volume of work completed.",
        [("IDENTIFY VALUE", "Agree the value components with key stakeholders early, in "
                            "measurable terms, so 'success' is not decided retrospectively."),
         ("PRIORITISE BY VALUE", "Order the work by value and stakeholder feedback so "
                                 "the most valuable capability is delivered first."),
         ("VERIFY MEASUREMENT", "Confirm a measurement system is in place to track "
                                "benefits — you cannot claim value you never measured.")],
        n, kicker=cd.eco("Process", 3), accent=TEAL); n += 1

    # --------------------------------------------- 55. value delivery process
    X.process(
        prs, "Delivering and evaluating project value",
        [("Identify components", "Work with key stakeholders to name the value "
                                 "components and how each will be recognised."),
         ("Prioritise the work", "Order the backlog or scope by value and stakeholder "
                                 "feedback rather than by ease or by who shouted loudest."),
         ("Deliver incrementally", "Assess every opportunity to release value earlier in "
                                   "smaller pieces rather than banking it all to the end."),
         ("Measure benefits", "Verify the measurement system is live and read it; track "
                              "actual benefit against the business case forecast."),
         ("Re-examine value", "Continually examine whether the business value still "
                              "justifies the remaining investment, and re-plan if not.")],
        n, kicker=cd.eco("Process", 3), accent=CYAN,
        note="A project that is on time and on budget but delivers no measured benefit "
             "has failed. PMI's value-delivery view treats the business case as a live "
             "document, not an entry ticket."); n += 1

    # ------------------------------------------------------------ 56. compliance
    X.cards(
        prs, "Project compliance — who is responsible for what",
        [("External standards",
          "Government regulations, industry standards, privacy law and any licensing the "
          "product or the organisation requires."),
         ("Internal standards",
          "Corporate policies, the quality management system, the code of conduct and "
          "the organisation's own methodology."),
         ("The PMO's role",
          "Monitors compliance at organisational level, maintains the standards and "
          "audits projects against them."),
         ("The project team's role",
          "Responsible for compliance in project activity — quality of processes and "
          "deliverables, and the work done by vendors."),
         ("Procurement compliance",
          "Vendor work must meet the same obligations; contracts must pass the "
          "requirement down and give you audit rights."),
         ("The PM's stewardship",
          "Compliance stewardship is your personal responsibility — it is an ethical "
          "obligation under the PMI Code of Conduct.")],
        n, kicker=cd.eco(BE, 2), accent=ROSE); n += 1

    # -------------------------------------------- 57. compliance categories table
    X.table(
        prs, "Classifying compliance categories",
        ["Category", "Typical requirements", "Consequence of failure"],
        [["Environmental", "Emissions limits, waste handling, environmental impact "
          "assessment, site remediation",
          "Fines, forced remediation, loss of operating licence, reputational damage"],
         ["Workplace health and safety", "Risk assessments, permits to work, protective "
          "equipment, incident reporting",
          "Injury, prosecution of individuals, stop-work orders, insurance loss"],
         ["Ethical and anti-corruption", "Anti-bribery policy, conflict of interest "
          "declarations, gift registers, procurement fairness",
          "Criminal liability, contract voiding, blacklisting from public tenders"],
         ["Data protection and security", "Consent, data residency, encryption, breach "
          "notification, access control",
          "Regulatory fines, breach notification cost, customer attrition"],
         ["Social responsibility", "Labour standards in the supply chain, accessibility, "
          "inclusion, community obligations",
          "Reputational harm, activist and investor pressure, contract loss"],
         ["Quality and process", "Standards conformance, documented process rigour, "
          "traceability of test evidence",
          "Rework, product recall, refused acceptance, warranty exposure"]],
        n, kicker=cd.eco(BE, 2), accent=AMBER, widths=[1.4, 2.4, 2.4],
        note="Categories vary with industry, solution scope and the organisation's "
             "unique legal and regulatory exposure — classify them for your project, "
             "not from a template."); n += 1

    # ---------------------------------------------- 58. compliance requirements cards
    X.cards(
        prs, "Confirming compliance requirements for your project",
        [("Legal and regulatory constraints",
          "Requirements for specific practices, mandatory standards, privacy laws and "
          "rules for handling sensitive information."),
         ("Where compliance is owned",
          "Identify who in the organisation handles compliance — legal, quality, "
          "security, or an external regulator's inspector."),
         ("The quality policy",
          "Understand the organisation's quality policy and how much process rigour and "
          "quality control it demands of this project."),
         ("Tailor the rigour",
          "How much control is genuinely relevant here? A safety-critical system and an "
          "internal reporting tool do not need the same rigour."),
         ("Awareness across the team",
          "Confirm the team and stakeholders actually know the compliance matters that "
          "apply — assumed knowledge is a common failure."),
         ("Evidence, not intention",
          "Every requirement needs a named owner, a control and auditable evidence that "
          "the control is actually operating.")],
        n, kicker=cd.eco(BE, 2), accent=VIOLET); n += 1

    # -------------------------------------------- 59. compliance threats matrix
    X.matrix2x2(
        prs, "Prioritising threats to compliance",
        "LIKELIHOOD OF OCCURRING  →  high",
        "SEVERITY OF CONSEQUENCE  →  high",
        [("Monitor closely", "Severe but unlikely — for example a major data breach. "
          "Maintain preventive controls and a tested response plan.", AMBER),
         ("Act immediately", "Severe and likely — for example missing a known "
          "regulatory deadline. Escalate and fund a response now.", ROSE),
         ("Accept and log", "Minor and unlikely — record in the register, review "
          "periodically, and do not spend scarce control effort here.", TEAL),
         ("Fix the process", "Minor but frequent — for example repeated missing "
          "sign-offs. Correct the underlying process, not each instance.", BLUE)],
        n, kicker=cd.eco(BE, 2), accent=ROSE,
        note="Analyse the consequences of non-compliance before choosing the "
             "response, and measure the extent to which the project is compliant on "
             "a defined cadence."); n += 1

    # ---------------------------------------- 60. supporting compliance process
    X.process(
        prs, "Methods that support compliance through the project",
        [("Documentation", "Maintain a compliance register of requirements, owners, "
                           "controls and evidence, updated as obligations change."),
         ("Risk planning", "Prioritise compliance risks explicitly in the risk register "
                           "with named responses, not as generic assumptions."),
         ("Compliance council", "Convene quality and audit specialists plus relevant "
                                "legal and technical experts to rule on grey areas."),
         ("Compliance audit", "Run a formal audit at defined checkpoints to test that "
                              "controls actually operate as designed."),
         ("Stewardship", "Model and enforce compliance behaviour in the team every day — "
                         "it is ultimately your personal responsibility.")],
        n, kicker=cd.eco(BE, 2), accent=BLUE,
        note="Measure compliance the way you measure schedule: the percentage of "
             "identified requirements with current evidence, trended over time and "
             "reported to governance."); n += 1

    # ------------------------------------------------ 61. sustainability statement
    X.statement(
        prs, "Sustainability is now a compliance and a value dimension",
        "The 2026 ECO makes sustainability an explicit information requirement, "
        "a quality obligation and a category of project risk.",
        [("ENVIRONMENTAL", "Carbon footprint of the solution, energy and water use, "
                           "materials, waste and end-of-life disposal of what you build."),
         ("SOCIAL", "Labour conditions across the supply chain, accessibility of the "
                    "deliverable, and impact on the surrounding community."),
         ("GOVERNANCE", "Transparent reporting of sustainability claims, ethical "
                        "procurement, and avoidance of greenwashing in benefit claims.")],
        n, kicker=cd.eco(BE, 2), accent=TEAL); n += 1

    # ------------------------------------------ 62. sustainability in the ECO table
    X.table(
        prs, "Where sustainability appears in the 2026 ECO",
        ["ECO reference", "What it requires", "What you actually do"],
        [["Process T1 — integrated plan", "Determine critical information requirements, "
          "explicitly including sustainability",
          "Add sustainability criteria to the plan and to the definition of done"],
         ["Process T7 — quality", "Manage cost of quality and sustainability together",
          "Cost sustainable options in the business case rather than as an afterthought"],
         ["Business Env T2 — compliance", "Confirm sustainability among the compliance "
          "requirement categories",
          "Register environmental and social obligations with owners and evidence"],
         ["Business Env T5 — risk", "Execute risk responses for security and "
          "sustainability risks",
          "Log sustainability risks in the register with real, funded responses"],
         ["Business Env T8 — external change", "Survey regulatory change in the external "
          "environment", "Track emerging disclosure and reporting regulation "
          "affecting the deliverable"]],
        n, kicker=cd.eco(BE, 2), accent=CYAN, widths=[1.7, 2.3, 2.3],
        note="Exam framing: sustainability is treated as a legitimate constraint and "
             "benefit, so 'ignore it because it is not in scope' is never the best "
             "answer."); n += 1

    # ------------------------------------------------------- 63. AI in PM cards
    X.cards(
        prs, "AI in project management — where it genuinely helps",
        [("Estimation",
          "Models trained on historical project data produce range estimates and flag "
          "where your estimate diverges from comparable past work."),
         ("Risk detection",
          "Pattern analysis across schedule, issue logs and communications surfaces "
          "emerging risks earlier than a monthly review would."),
         ("Status reporting",
          "Automated generation of status narratives from tool data, freeing PM time "
          "for stakeholder work rather than slide assembly."),
         ("Schedule optimisation",
          "Scenario simulation across thousands of resource and sequence permutations to "
          "test compression options before committing."),
         ("Requirements analysis",
          "Clustering and de-duplicating large volumes of stakeholder input, and "
          "flagging ambiguous or untestable requirements."),
         ("Meeting and knowledge capture",
          "Transcription, action extraction and searchable project memory that makes "
          "lessons learned findable rather than archived.")],
        n, kicker=cd.eco(BE, 8), accent=VIOLET); n += 1

    # -------------------------------------------- 64. AI governance & ethics risks
    X.cards(
        prs, "Governing AI use on your project — the risks you own",
        [("Data confidentiality",
          "Client data, contracts and personal information pasted into external tools may "
          "leave your control and breach your obligations."),
         ("Accuracy and hallucination",
          "Generated estimates, text and analysis can be confidently wrong; a human must "
          "own and verify anything that reaches a stakeholder."),
         ("Bias in the training data",
          "A model trained on past projects reproduces past bias — in vendor selection, "
          "in estimating, and in performance judgement."),
         ("Transparency and disclosure",
          "Stakeholders should know when analysis or reporting they rely on was "
          "machine-generated; concealment is an ethics failure."),
         ("Accountability stays human",
          "Delegating a task to AI never delegates the accountability; the project "
          "manager remains answerable for the decision."),
         ("Regulatory exposure",
          "AI-specific regulation is emerging quickly — treat it as an external "
          "environment change to survey under ECO T8.")],
        n, kicker=cd.eco(BE, 2), accent=ROSE); n += 1

    # ------------------------------------------------- 65. AI adoption process
    X.process(
        prs, "Introducing AI into your project practice responsibly",
        [("Define the use case", "Name the specific decision or task AI will support, "
                                 "and the measurable improvement you expect from it."),
         ("Check policy and law", "Confirm what your organisation's AI policy, contracts "
                                  "and applicable regulation permit before any data moves."),
         ("Classify the data", "Determine what data may be used, where it may be "
                               "processed, and what must never leave your environment."),
         ("Pilot with a human in the loop", "Run the AI output alongside the existing "
                                            "method and compare; never switch over blind."),
         ("Measure and govern", "Track accuracy and benefit, disclose usage to "
                                "stakeholders, and review at the governance checkpoint.")],
        n, kicker=cd.eco(BE, 7), accent=AMBER,
        note="AI adoption is itself an organisational change project. Everything you "
             "learned about ADKAR applies to getting your own team to use it well."); n += 1

    # ------------------------------------------------------- 66. exam traps
    X.exam(
        prs, "Exam focus: Business Environment traps",
        [("A new law is announced that affects your project mid-execution",
          "Assess the impact on the project first, then raise a change request through "
          "the defined governance path."),
         ("An issue arises that exceeds your documented tolerance level",
          "Escalate to the stakeholder authorised to act, presenting options and a "
          "recommendation — do not decide alone."),
         ("A stakeholder asks you to skip a compliance step to hit the date",
          "Refuse and escalate. Compliance stewardship is non-negotiable and is an "
          "ethical obligation under the Code of Conduct."),
         ("The organisation reorganises and your sponsor is replaced",
          "Assess the impact on the project, then re-confirm the charter, authority "
          "and priorities with the new sponsor.")],
        n, kicker="EXAM FOCUS", accent=ROSE); n += 1

    X.exam(
        prs, "Exam focus: approach, governance and value traps",
        [("Requirements are unclear and are expected to keep evolving",
          "Recommend an adaptive or hybrid approach with short feedback loops — not a "
          "longer, more detailed requirements phase."),
         ("The sponsor asks why the project should continue after a market shift",
          "Re-examine the business value against the remaining investment and present "
          "the options, including terminating."),
         ("A team wants to drop retrospectives because they feel unproductive",
          "Fix the retrospective, do not remove it — check whether actions are actually "
          "reaching the next sprint backlog."),
         ("You are told 'we are agile so we do not need documentation'",
          "Wrong. Agile values working product over comprehensive documentation; "
          "regulated projects still require compliance evidence.")],
        n, kicker="EXAM FOCUS", accent=AMBER); n += 1

    # ---------------------------------------------------- 67. domain weighting chart
    X.chart(
        prs, "Where Business Environment sits in the July 2026 exam",
        "pie",
        ["People (33%)", "Process (41%)", "Business Environment (26%)"],
        [("Share of scored questions", [33, 41, 26])],
        n, kicker=cd.eco(BE, 1), accent=BLUE,
        insight=["Business Environment is roughly 44 of the 170 scored questions — "
                 "too many to treat as a side topic.",
                 "Its eight tasks cover governance, compliance, change control, "
                 "impediments, risk, improvement, org change and external change.",
                 "This topic delivers T1, T2, T7 and T8; the remaining tasks appear "
                 "in Topics 5 and 6 of this course.",
                 "About 40% of the exam is predictive and 60% adaptive or hybrid, so "
                 "answer in the context each scenario states."]); n += 1

    # -------------------------------------------------------------- 68. recap
    X.recap(
        prs, "Topic 1 recap — Business Environment",
        [("A project is temporary and unique",
          "It delivers change and business value, and ends when objectives are met or "
          "are shown to be unachievable."),
         ("Triple constraint and tailoring",
          "Scope, time and cost are joined; tailor process, artifacts and methods to the "
          "context rather than applying a template."),
         ("Two life cycles, five approaches",
          "The project life cycle is the phases; the development life cycle is "
          "predictive, iterative, incremental, agile or hybrid."),
         ("Agile is incremental plus iterative",
          "Four Manifesto values and twelve principles; Scrum supplies the roles, "
          "events and artifacts most teams actually use."),
         ("EEFs constrain, OPAs are reusable",
          "You conform to EEFs; you apply and then update OPAs — updating them is an "
          "explicit ECO obligation."),
         ("Change needs individuals to change",
          "ADKAR gives five milestones — awareness, desire, knowledge, ability and "
          "reinforcement — to diagnose adoption failure."),
         ("Governance sets thresholds",
          "Escalate outside tolerance with options; resolve inside tolerance with the "
          "team. Phase gates decide go, change, hold or kill."),
         ("Compliance and sustainability are owned by you",
          "Classify requirements, analyse threats, evidence controls, and treat "
          "sustainability as both constraint and benefit."),
         ("Value, not activity, defines success",
          "Prioritise by value, deliver incrementally, verify a benefits measurement "
          "system exists and read it."),
         ("AI helps but never takes accountability",
          "Use it for estimation, risk detection and reporting under an explicit policy, "
          "with a human verifying every output.")],
        n, kicker="RECAP", accent=CYAN); n += 1

    return n
