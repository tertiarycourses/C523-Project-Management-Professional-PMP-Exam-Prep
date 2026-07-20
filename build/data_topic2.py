"""Topic 2 — Start the Project."""
import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE


def build(prs, n):
    """Render Topic 2. `n` is the running slide number. Return the next number."""

    # ------------------------------------------------------------ 1 divider
    X.section(
        prs, 2, "Start the Project",
        "Turning an idea into an authorised project: the business case that "
        "justifies it, the charter that authorises it, the stakeholders who "
        "judge it, and the team that will build it.",
        ["Project integration and the Develop Project Charter process",
         "Business value, business case, cost-benefit and benefits management",
         "Identify, analyse and prioritise stakeholders",
         "Align and manage stakeholder expectations (ECO 2026 People T5/T6)",
         "Form the team, agree the team charter and kick off",
         "Recommend the development approach for the integrated plan"],
        n); n += 1

    # ------------------------------------------------------------ 2 outcomes
    X.cards(prs, "What You Will Be Able To Do After Topic 2", [
        ("Draft a project charter",
         "Write a charter that names the sponsor and PM, states measurable "
         "objectives, and authorises the PM to apply organisational resources."),
        ("Justify a project financially",
         "Build a cost-benefit analysis and read payback, NPV, IRR, ROI and BCR "
         "well enough to defend the selection decision to a steering committee."),
        ("Identify every stakeholder",
         "Work an organisation breakdown structure and document analysis to find "
         "who is affected, then record them properly in a stakeholder register."),
        ("Analyse and prioritise",
         "Apply power/interest and power/influence grids, the stakeholder cube "
         "and the salience model to decide who gets how much of your attention."),
        ("Align expectations",
         "Facilitate discussions that surface conflicting expectations early and "
         "converge them onto one agreed set of project objectives."),
        ("Start the team well",
         "Co-create a team charter, set ground rules and run a kick-off that "
         "leaves everyone sharing the same vision of success."),
    ], n, kicker="TOPIC 2 LEARNING OUTCOMES", accent=TEAL); n += 1

    # ------------------------------------------------------------ 3 statement
    X.statement(
        prs, "Why initiation deserves this much time",
        "Projects are not lost at the end.\nThey are lost at the start.",
        [("Wrong problem",
          "A project with no validated business case delivers perfectly against "
          "an objective nobody needed."),
         ("Wrong people",
          "A stakeholder discovered in month six brings requirements that should "
          "have shaped month one."),
         ("Wrong authority",
          "Without a signed charter the PM has responsibility without the power "
          "to apply resources.")],
        n, kicker=cd.eco("Process", 1), accent=BLUE); n += 1

    # ------------------------------------------------------------ 4 integration
    X.cards(prs, "Project Integration Management: The Unifying Discipline", [
        ("What integration is",
         "The work of identifying, defining, combining, unifying and coordinating "
         "the other knowledge areas so they behave as one system, not ten silos."),
        ("Why it exists",
         "Scope, schedule, cost, quality, resources, communications, risk and "
         "procurement all trade against each other; someone must own the trade-off."),
        ("Who owns it",
         "Integration is the one area the project manager cannot delegate — it is "
         "the definition of the PM role in the PMBOK Guide."),
        ("The through-line",
         "A researched business case, an approved charter and a well-planned "
         "project management plan tie every decision back to business value."),
        ("The test of integration",
         "Change a date and you can immediately state the cost, scope, quality and "
         "risk consequence — that is an integrated project."),
        ("The failure mode",
         "Silo optimisation: each function hits its own target while the project "
         "as a whole misses the business outcome entirely."),
    ], n, kicker=cd.eco("Process", 1), accent=VIOLET); n += 1

    # ------------------------------------------------------------ 5 benefits
    X.cards(prs, "The Key Benefits of Project Integration", [
        ("Strategic alignment",
         "Every deliverable can be traced upward to an organisational objective, so "
         "the project earns its funding rather than merely consuming it."),
        ("A single decision point",
         "Competing demands from stakeholders arrive at one integrating role that "
         "can weigh them against the whole rather than a part."),
        ("Coherent baselines",
         "Scope, schedule and cost baselines are built to be consistent with each "
         "other, so variance analysis measures reality rather than mismatch."),
        ("Controlled change",
         "Changes are assessed for their ripple effect across all knowledge areas "
         "before approval, not discovered downstream."),
        ("Value assurance",
         "Business value is examined throughout the life cycle, so a project whose "
         "case has evaporated can be stopped honestly."),
        ("Clean handover",
         "Integration carries the project through to transition, so benefits are "
         "actually realised by operations after the team disbands."),
    ], n, kicker=cd.eco("Process", 1), accent=CYAN); n += 1

    # ------------------------------------------------------------ 6 process flow
    X.process(prs, "From Idea to Authorised Project: The Initiation Flow", [
        ("Need or opportunity",
         "A market demand, regulation, technology shift or customer request "
         "creates pressure for change."),
        ("Business case",
         "Economic feasibility is studied; costs, benefits and alternatives are "
         "documented for a decision."),
        ("Selection decision",
         "Governance compares candidates using payback, NPV, IRR, ROI and "
         "strategic fit, then funds one."),
        ("Charter developed",
         "The sponsor issues a charter naming the PM and authorising resources "
         "against stated objectives."),
        ("Stakeholders identified",
         "Everyone affected is found, analysed and recorded before planning "
         "assumptions harden."),
        ("Kick-off",
         "Team and stakeholders align on vision, roles and approach, and "
         "planning begins in earnest."),
    ], n, kicker=cd.eco("Process", 1), accent=BLUE,
        note="Exam cue: the charter is an OUTPUT of initiating, not of planning. "
             "Nothing in the project management plan may be baselined before the "
             "charter authorises the project to exist."); n += 1

    # ------------------------------------------------------------ 7 ITTO charter
    X.itto(prs, "Develop Project Charter — ITTO",
        ["Business documents (business case, benefits management plan)",
         "Agreements (contracts, MOUs, SLAs, letters of intent)",
         "Enterprise environmental factors (market, standards, culture)",
         "Organizational process assets (templates, historical data, policies)"],
        ["Expert judgement (strategy, industry, technical, legal)",
         "Data gathering: brainstorming, focus groups, interviews",
         "Interpersonal and team skills: conflict management, facilitation",
         "Meetings — notably the charter workshop with sponsor and key stakeholders"],
        ["Project charter — the authorising document",
         "Assumption log — assumptions and constraints captured from day one",
         "(The charter feeds every subsequent planning process)"],
        n, kicker=cd.eco("Process", 1),
        purpose="Purpose: to produce a document that formally authorises the "
                "existence of the project and gives the project manager authority "
                "to apply organisational resources to project activities."); n += 1

    # ------------------------------------------------------------ 8 charter does
    X.cards(prs, "What the Project Charter Actually Does", [
        ("Authorises the project",
         "It is the formal statement that this project exists and may consume "
         "organisational resources — issued by a sponsor senior enough to fund it."),
        ("Empowers the project manager",
         "It names the PM and states their authority level, converting a job title "
         "into the right to direct people, spend money and make decisions."),
        ("Defines rationale and need",
         "It records why the organisation is doing this, so the reasoning survives "
         "sponsor turnover and mid-project pressure to change direction."),
        ("Verifies strategic alignment",
         "It links the project explicitly to strategic goals, which is what makes "
         "the funding defensible at portfolio review."),
        ("Sets the shared vision",
         "It gives every stakeholder one short reference for what success looks "
         "like, supporting ECO People T1 — develop a common vision."),
        ("Anchors change control",
         "Later change requests are assessed against charter objectives; a change "
         "that breaks the charter needs sponsor, not PM, approval."),
    ], n, kicker=cd.eco("People", 1), accent=AMBER); n += 1

    # ------------------------------------------------------------ 9 charter contents
    X.table(prs, "What Is Included in the Project Charter",
        ["Charter element", "What goes in it", "Why it matters"],
        [["Names and roles",
          "Project sponsor, project manager, key stakeholders and their authority",
          "Removes ambiguity about who decides and who must be consulted"],
         ["Project description",
          "High-level product description plus preliminary requirements",
          "Bounds the solution space before detailed requirements work"],
         ["Measurable objectives",
          "Objectives with success criteria that can be objectively tested",
          "Makes acceptance at closure a measurement, not an argument"],
         ["Business need",
          "The problem or opportunity, plus financial goals or milestones",
          "Preserves the 'why' when the 'what' comes under pressure"],
         ["Summary schedule",
          "High-level milestones and any externally imposed dates",
          "Signals feasibility and exposes immovable constraints early"],
         ["Assumptions and constraints",
          "Boundaries, overall project risk, approval requirements, approved budget",
          "Seeds the assumption log and the initial risk register"],
         ["Exit criteria",
          "Success criteria and the conditions under which the project is stopped",
          "Makes cancelling a failing project a planned option, not a failure"]],
        n, kicker=cd.eco("Process", 1), accent=VIOLET,
        widths=[2.0, 4.0, 4.0]); n += 1

    # ------------------------------------------------------------ 10 approval flow
    X.process(prs, "How a Charter Gets Approved", [
        ("Draft with the sponsor",
         "The PM facilitates; the sponsor owns the content and the authority "
         "behind it."),
        ("Validate with stakeholders",
         "Key stakeholders confirm objectives and success criteria are the ones "
         "they will be judged on."),
        ("Governance review",
         "Portfolio or steering body confirms strategic fit, funding and "
         "priority against other work."),
        ("Sponsor signs",
         "Signature converts a proposal into an authorisation, releasing budget "
         "and named resources."),
        ("Publish and socialise",
         "The charter is communicated widely so the vision is shared, not filed "
         "in a drawer."),
    ], n, kicker=cd.eco("People", 1), accent=TEAL,
        note="The project manager does not approve their own charter. If an exam "
             "option has the PM signing off the charter, it is wrong — the sponsor "
             "or initiating authority signs."); n += 1

    # ------------------------------------------------------------ 11 business value
    X.cards(prs, "Business Value: The Six Reasons Organisations Fund Projects", [
        ("Financial gain",
         "Direct revenue increase or cost reduction, usually the easiest form of "
         "value to quantify and therefore the easiest to defend."),
        ("New customers",
         "Access to a new segment, geography or channel, where the value is in the "
         "lifetime revenue of the relationship rather than the first sale."),
        ("Social benefit",
         "Community, environmental or sustainability outcomes that build licence to "
         "operate — increasingly explicit in ECO 2026 sustainability language."),
        ("First to market",
         "Speed itself is the value: capturing share, setting the standard or "
         "shaping customer expectations before competitors arrive."),
        ("Improvement",
         "Technological or process uplift that raises capability, reduces cycle "
         "time or removes chronic defects in how work is done."),
        ("Regularization",
         "Alignment or compliance with standards and regulations, where the value "
         "is the avoided penalty, avoided shutdown or preserved certification."),
    ], n, kicker=cd.eco("Process", 1), accent=ROSE); n += 1

    # ------------------------------------------------------------ 12 tangible/intangible
    X.compare(prs, "Tangible vs Intangible Business Value",
        ("TANGIBLE VALUE", "Countable, auditable, defensible in a business case", [
            "Monetary assets and direct revenue from new sales",
            "Stockholder equity and improved market capitalisation",
            "Utility, fixtures, tools and physical assets acquired",
            "Market share expressed as a measurable percentage",
            "Cost avoidance and hard headcount or licence savings",
            "Measured cycle-time or defect-rate improvement"]),
        ("INTANGIBLE VALUE", "Real but harder to measure — still must be tracked", [
            "Goodwill and brand recognition in the market",
            "Public benefit, sustainability and community standing",
            "Trademarks, patents and other intellectual property",
            "Strategic alignment and organisational reputation",
            "Employee capability, morale and retention",
            "Customer satisfaction and loyalty"]),
        n, kicker=cd.eco("Process", 1), lc=TEAL, rc=VIOLET,
        footer_note="Both count. ECO Process T3 asks you to identify value "
                    "components WITH key stakeholders and to verify a measurement "
                    "system exists — including for the intangibles."); n += 1

    # ------------------------------------------------------------ 13 business docs
    X.cards(prs, "The Three Business Documents", [
        ("Business case",
         "The documented economic feasibility study that justifies the investment "
         "and establishes the benefits the project work is expected to deliver."),
        ("Cost-benefit analysis",
         "The quantitative core of the business case: all costs against all "
         "benefits over a defined horizon, used to compare candidate projects."),
        ("Benefits management plan",
         "How benefits will be created, maximised and sustained after delivery, "
         "with owners, metrics and time frames for realisation."),
    ], n, kicker=cd.eco("Process", 1), accent=BLUE, cols=3); n += 1

    # ------------------------------------------------------------ 14 who owns
    X.compare(prs, "Business Documents: Who Owns Them and When",
        ("OWNED BY THE SPONSOR / ORGANISATION",
         "Created before the project — the PM is a consumer, not an author", [
            "The business case is developed by the sponsor or a business analyst",
            "The benefits management plan is owned by a benefits owner",
            "Both predate the charter and are inputs to Develop Project Charter",
            "The PM may recommend updates but does not unilaterally change them",
            "They are maintained beyond project closure into benefits realisation"]),
        ("USED BY THE PROJECT MANAGER",
         "Consumed continuously to keep the project honest about value", [
            "Source the charter's rationale, objectives and success criteria",
            "Test every significant change request against continued value",
            "Feed the value discussion at each phase gate or stage review",
            "Trigger an escalation when the business case no longer holds",
            "Provide the acceptance and exit criteria used at closure"]),
        n, kicker=cd.eco("Process", 1), lc=AMBER, rc=CYAN,
        footer_note="Exam cue: 'the business case no longer supports the project' "
                    "means escalate to the sponsor for a stop/continue decision — "
                    "not quietly re-plan."); n += 1

    # ------------------------------------------------------------ 15 CBA process
    X.process(prs, "How to Run a Cost-Benefit Analysis", [
        ("Define the horizon",
         "Fix the period over which costs and benefits will be counted, typically "
         "three to five years."),
        ("Enumerate all costs",
         "Capital, implementation, licensing, training, change management and "
         "ongoing operating cost."),
        ("Quantify benefits",
         "Revenue uplift, cost avoidance and quantified proxies for intangible "
         "benefits, per period."),
        ("Discount to present value",
         "Apply the organisation's discount rate so future money is compared "
         "fairly with today's spend."),
        ("Compute the metrics",
         "Payback period, NPV, IRR, ROI and benefit-cost ratio for the "
         "selection decision."),
        ("Test sensitivity",
         "Re-run with pessimistic assumptions to see how fragile the conclusion "
         "really is."),
    ], n, kicker=cd.eco("Process", 6), accent=VIOLET,
        note="Sunk costs are irrelevant to a go/no-go decision. Money already "
             "spent cannot be recovered by continuing; only future costs and "
             "future benefits belong in the analysis."); n += 1

    # ------------------------------------------------------------ 16 business case
    X.cards(prs, "The Business Case as an Economic Feasibility Study", [
        ("Documented, not verbal",
         "It is a written study that can be reviewed, challenged and audited — "
         "an enthusiastic sponsor's confidence is not a business case."),
        ("Establishes the benefits",
         "It states specifically what benefits the project work will produce, in "
         "units that can later be measured against reality."),
        ("Basis for authorisation",
         "It provides the justification on which further project activities are "
         "authorised — no case, no charter, no funding."),
        ("Includes alternatives",
         "Do nothing, buy, build and partial-scope options are compared, so the "
         "chosen route is a decision rather than a default."),
        ("States success criteria",
         "Defines what 'it worked' will mean, which flows into charter objectives "
         "and eventually into acceptance at closure."),
        ("Is revisited, not filed",
         "ECO Process T3 requires examining business value throughout the project, "
         "so the case is a live document across the life cycle."),
    ], n, kicker=cd.eco("Process", 3), accent=TEAL); n += 1

    # ------------------------------------------------------------ 17 BMP contents
    X.table(prs, "Benefits Management Plan — Required Contents",
        ["Element", "What it specifies", "Typical example"],
        [["Target benefits",
          "The value expected, expressed in measurable terms",
          "Reduce order-processing cost by 18% per transaction"],
         ["Strategic alignment",
          "Which organisational objective the benefit serves",
          "Supports the 'digital-first operations' strategic pillar"],
         ["Time frame",
          "When short-term and long-term benefits will be realised",
          "40% at go-live, full run-rate 12 months post-transition"],
         ["Benefits owner",
          "The accountable person who monitors and reports realisation",
          "Head of Operations, named by the sponsor"],
         ["Metrics",
          "Direct and indirect measures used to demonstrate realisation",
          "Cost per order, error rate, customer satisfaction score"],
         ["Assumptions",
          "Conditions that must hold for the benefits to appear",
          "Volumes remain within +/-10% of forecast"],
         ["Risks",
          "Threats to benefit realisation, distinct from delivery risks",
          "Operations does not adopt the new process after handover"]],
        n, kicker=cd.eco("Process", 3), accent=AMBER, widths=[2.0, 4.2, 3.8]); n += 1

    # ------------------------------------------------------------ 18 benefits owner
    X.cards(prs, "The Benefits Owner: An Accountability Beyond Delivery", [
        ("Works alongside the PM",
         "Partners with the project manager or team lead during delivery to ensure "
         "planned benefits are actively managed as they are delivered."),
        ("Owns the transition",
         "Assists in transitioning the requested benefits to the receiving "
         "organisation so value is not lost at handover."),
        ("Establishes measurement",
         "Ensures measurement metrics and methods are established, baselined and "
         "monitored — you cannot claim a benefit you never measured."),
        ("Reports realised value",
         "Reports to management on the realised results of delivered benefits, "
         "often long after the project team has been released."),
        ("Who holds the role",
         "Typically a business analyst, the sponsor or an operations manager — a "
         "business-side role, not a project-side one."),
        ("In adaptive contexts",
         "The product owner is responsible for making sure the work reaps benefits "
         "for the organisation, prioritising the backlog by value."),
    ], n, kicker=cd.eco("Process", 3), accent=CYAN); n += 1

    # ------------------------------------------------------------ 19 formula
    X.formula(prs, "Benefit Measurement Formulas You Must Recognise", [
        ("Return on investment",
         "ROI = (Benefit − Cost) / Cost",
         "Expressed as a percentage. Bigger is better. Ignores the timing of "
         "cash flows entirely."),
        ("Benefit-cost ratio",
         "BCR = Benefits / Costs",
         "Greater than 1.0 means benefits exceed costs. Bigger is better; used "
         "to rank competing proposals."),
        ("Net present value",
         "NPV = Σ CFt / (1+r)^t − C0",
         "Today's value of all future cash flows minus the investment. Positive "
         "NPV means proceed; choose the highest."),
        ("Payback period",
         "Payback = Cost / Annual net inflow",
         "How long until you recover the investment. Smaller is better; ignores "
         "everything after payback."),
    ], n, kicker=cd.eco("Process", 6), accent=ROSE,
        note="Rule of thumb for the exam: financial-return measures (NPV, IRR, ROI, "
             "BCR) are 'bigger is better'; time and cost measures (payback period, "
             "opportunity cost) are 'smaller is better'."); n += 1

    # ------------------------------------------------------------ 20 methods table
    X.table(prs, "Benefit Measurement Methods Compared",
        ["Method", "What it answers", "Decision rule", "Main weakness"],
        [["Payback period",
          "How fast do we get our money back?",
          "Choose the shortest duration",
          "Ignores all cash flow after payback and the time value of money"],
         ["Opportunity cost",
          "What is the value of the option we gave up?",
          "Choose the option with the smaller opportunity cost",
          "Depends entirely on which alternative you compare against"],
         ["Net present value",
          "What is this worth in today's dollars?",
          "Choose the highest positive NPV",
          "Highly sensitive to the discount rate chosen"],
         ["Internal rate of return",
          "What effective interest rate does it earn?",
          "Choose the highest IRR above the hurdle rate",
          "Misleads when comparing projects of very different sizes"],
         ["Return on investment",
          "What percentage return on money spent?",
          "Choose the highest ROI",
          "Ignores timing, duration and risk of the cash flows"],
         ["Benefit-cost ratio",
          "How many dollars of benefit per dollar spent?",
          "Choose the highest ratio, must exceed 1.0",
          "Sensitive to whether an item is classed as cost or negative benefit"]],
        n, kicker=cd.eco("Process", 6), accent=BLUE, widths=[1.7, 2.9, 2.4, 3.0]); n += 1

    # ------------------------------------------------------------ 21 chart payback
    X.chart(prs, "Payback Period: Cumulative Cash Flow of a $500k Project",
        "line",
        ["Year 0", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"],
        [("Project A cumulative ($k)", [-500, -320, -140, 60, 260, 460]),
         ("Project B cumulative ($k)", [-500, -430, -300, -110, 180, 620])],
        n, kicker=cd.eco("Process", 6), accent=TEAL,
        insight=["Project A crosses zero during year 3 — payback is roughly 2.8 "
                 "years, the shorter and therefore preferred payback.",
                 "Project B pays back later but ends higher, so a payback-only "
                 "rule would reject the project with more total value.",
                 "This is exactly why payback is never used alone: pair it with "
                 "NPV, which counts everything after the crossover point.",
                 "Shorter payback also means less exposure to forecast error, "
                 "which matters most in volatile business environments."]); n += 1

    # ------------------------------------------------------------ 22 chart NPV
    X.chart(prs, "NPV of Four Competing Project Proposals",
        "column",
        ["Proposal A", "Proposal B", "Proposal C", "Proposal D"],
        [("NPV at 10% discount rate ($k)", [420, 610, -80, 180])],
        n, kicker=cd.eco("Process", 6), accent=VIOLET,
        insight=["Proposal B has the highest NPV and is the correct selection on "
                 "financial grounds alone.",
                 "Proposal C has a negative NPV — it destroys value and should not "
                 "be funded regardless of how attractive it sounds.",
                 "NPV is additive across projects, which is why portfolios are "
                 "built on NPV rather than on IRR or ROI percentages.",
                 "Financial ranking is only one input: strategic fit, risk and "
                 "capacity can still override the highest NPV."]); n += 1

    # ------------------------------------------------------------ 23 exam finance
    X.exam(prs, "Exam Traps: Project Selection and Business Documents", [
        ("Two projects, one has higher NPV and the other has shorter payback",
         "Choose the higher NPV — it accounts for the full value of every cash "
         "flow, not just the recovery point."),
        ("A large sum has already been spent and the project now looks unviable",
         "Ignore the sunk cost. Decide on future costs versus future benefits and "
         "escalate a stop recommendation to the sponsor."),
        ("You are asked who writes the business case",
         "The sponsor or business analyst — it exists before the project, and the "
         "PM is a consumer of it, not its author."),
        ("A stakeholder wants a change that breaks the charter objectives",
         "Escalate to the sponsor. The PM cannot approve a change that invalidates "
         "the authorising document."),
    ], n, kicker="EXAM FOCUS", accent=ROSE); n += 1

    # ------------------------------------------------------------ 24 vision
    X.cards(prs, "The Project Vision Statement", [
        ("Created by the sponsor",
         "Written by the project sponsor or an executive, because vision requires "
         "the authority to commit the organisation to a direction."),
        ("Describes desired objectives",
         "States clearly what the desired end state looks like, in language a "
         "non-specialist stakeholder can repeat accurately."),
        ("Shows strategic alignment",
         "Makes explicit which organisational strategic goal this project advances, "
         "so the vision is anchored rather than aspirational."),
        ("Referred to throughout",
         "Revisited at every major decision point to maintain alignment — a vision "
         "used once at kick-off is decoration."),
        ("Kept current",
         "ECO People T1 requires keeping the vision current: when the business "
         "environment shifts, the vision is updated, not ignored."),
        ("Root-cause the drift",
         "When people act inconsistently with the vision, break the situation down "
         "to find the root cause of the misunderstanding rather than blaming."),
    ], n, kicker=cd.eco("People", 1), accent=AMBER); n += 1

    # ------------------------------------------------------------ 25 statement vision
    X.statement(
        prs, "ECO People Task 1 — Develop a Common Vision",
        "A vision only exists if the team\ncan state it without reading it.",
        [("Help ensure it is shared",
          "Co-create the vision with key stakeholders so they own it rather than "
          "receive it."),
         ("Promote it actively",
          "Repeat the vision at stand-ups, reviews and steering meetings until it "
          "becomes the team's default language."),
         ("Keep it current",
          "Revalidate the vision whenever strategy, market or sponsorship changes; "
          "a stale vision misdirects everyone.")],
        n, kicker=cd.eco("People", 1), accent=TEAL); n += 1

    # ------------------------------------------------------------ 26 agile charter
    X.compare(prs, "Predictive Charter vs Agile Team Charter",
        ("PREDICTIVE PROJECT CHARTER",
         "Authorisation document, issued top-down by the sponsor", [
            "Purpose: authorise the project and empower the PM",
            "Author: sponsor or initiating authority signs it",
            "Contains measurable objectives and approved budget",
            "Contains summary milestones and approval requirements",
            "Changes require formal sponsor approval",
            "Written once, referenced throughout the life cycle"]),
        ("AGILE TEAM CHARTER",
         "Working agreement, created bottom-up by the team itself", [
            "Purpose: define how this team will work together",
            "Author: the whole team, facilitated by the servant leader",
            "Team vision or mission in the team's own words",
            "Team roles, responsibilities and the stakeholders served",
            "Team values and the ceremonies the team commits to",
            "Revisited at retrospectives and amended as the team learns"]),
        n, kicker=cd.eco("People", 3), lc=BLUE, rc=VIOLET,
        footer_note="They are complements, not alternatives. A hybrid project "
                    "commonly has both: a signed project charter for authority and "
                    "a team charter for day-to-day working agreements."); n += 1

    # ------------------------------------------------------------ 27 dev approach
    X.matrix2x2(prs, "Choosing the Development Approach",
        "REQUIREMENTS STABILITY  →  high", "high  ←  TECHNICAL UNCERTAINTY",
        [("Adaptive / Agile",
          "Volatile requirements and unfamiliar technology. Deliver in short "
          "increments, inspect and adapt, expect the plan to change.", ROSE),
         ("Iterative",
          "Technology is unfamiliar but the goal is clear. Prototype and refine "
          "the solution through repeated passes.", AMBER),
         ("Incremental",
          "Technology is well understood but stakeholders need value early. "
          "Ship usable slices in sequence.", TEAL),
         ("Predictive / Waterfall",
          "Stable requirements and proven technology. Plan fully, baseline, and "
          "control change through a formal process.", BLUE)],
        n, kicker=cd.eco("Process", 1), accent=VIOLET,
        note="ECO Process T1 asks you to assess project needs, complexity and "
             "magnitude, then RECOMMEND an approach. The recommendation must be "
             "justified by the project's characteristics, not by fashion."); n += 1

    # ------------------------------------------------------------ 28 stakeholder def
    X.statement(
        prs, "Stakeholder Definition",
        "A stakeholder is anyone affected —\nor who believes they are affected —\nby your project.",
        [("Perception counts",
          "Someone who merely believes they are affected can still block you, so "
          "they are a real stakeholder."),
         ("The outcome we want",
          "Productive relationships in which stakeholders actively support project "
          "objectives rather than merely tolerate them."),
         ("The five-step cycle",
          "Identify, analyse, prioritise and engage stakeholders — then monitor "
          "their engagement continuously.")],
        n, kicker=cd.eco("People", 4), accent=CYAN); n += 1

    # ------------------------------------------------------------ 29 SH cycle
    X.process(prs, "The Stakeholder Engagement Cycle", [
        ("Identify",
         "Find everyone affected using the OBS, document analysis, contracts and "
         "expert judgement."),
        ("Analyse",
         "Assess each stakeholder's power, interest, influence, attitude and "
         "expectations of the project."),
        ("Prioritise",
         "Classify with grids, the cube or the salience model to decide where "
         "engagement effort goes."),
        ("Engage",
         "Execute the stakeholder engagement plan with tailored communication "
         "and relationship building."),
        ("Monitor",
         "Track actual versus desired engagement and adjust strategies as "
         "relationships shift."),
    ], n, kicker=cd.eco("People", 4), accent=BLUE,
        note="This cycle repeats. New stakeholders appear at every phase boundary, "
             "reorganisation and change of sponsor — identification is a continuous "
             "activity, not an initiating-phase task you complete once."); n += 1

    # ------------------------------------------------------------ 30 ITTO identify
    X.itto(prs, "Identify Stakeholders — ITTO",
        ["Project charter (names sponsor and key stakeholders)",
         "Business documents (business case, benefits management plan)",
         "Project management plan (communications and risk management plans)",
         "Project documents (change log, issue log, requirements documentation)",
         "Agreements — contracting parties are always stakeholders",
         "Enterprise environmental factors and organizational process assets"],
        ["Expert judgement on organisational politics and industry context",
         "Data gathering: questionnaires and surveys, brainstorming",
         "Data analysis: stakeholder analysis, document analysis",
         "Data representation: stakeholder mapping and representation",
         "Meetings — profile workshops with the sponsor and team"],
        ["Stakeholder register — the central artefact of this process",
         "Change requests (after the first pass)",
         "Project management plan updates",
         "Project documents updates (assumption log, issue log, risk register)"],
        n, kicker=cd.eco("People", 4),
        purpose="Purpose: to identify project stakeholders and analyse and document "
                "relevant information about their interests, involvement, "
                "interdependencies, influence and potential impact on project success."); n += 1

    # ------------------------------------------------------------ 31 SH identification
    X.cards(prs, "Stakeholder Identification in Practice", [
        ("Start early, repeat often",
         "Identify and analyse engagement early and throughout the project — the "
         "cost of a missed stakeholder rises steeply with every planning decision."),
        ("Use the OBS",
         "Walk the organisational breakdown structure top to bottom to find the "
         "initial population of internal stakeholders systematically."),
        ("Mine the documents",
         "Contracts, regulations, prior lessons learned and the business case each "
         "name parties who have a stake in the outcome."),
        ("Ask the stakeholders you have",
         "Snowball sampling: every stakeholder you interview can name two more you "
         "had not considered, especially external ones."),
        ("Look outward deliberately",
         "Regulators, unions, communities, suppliers and end users rarely appear on "
         "an internal org chart but can stop a project cold."),
        ("Record it, do not remember it",
         "Everything found goes into the stakeholder register so the knowledge "
         "survives handover and team changes."),
    ], n, kicker=cd.eco("People", 4), accent=TEAL); n += 1

    # ------------------------------------------------------------ 32 register fields
    X.table(prs, "The Stakeholder Register — Fields and Purpose",
        ["Field", "What you record", "Why you need it"],
        [["Name and organisation",
          "Identity, department, employer and contact details",
          "Basic addressability — you cannot engage whom you cannot reach"],
         ["Role on the project",
          "Sponsor, customer, end user, regulator, supplier, team member",
          "Sets the default expectations and rights of that party"],
         ["Power",
          "Authority to grant, withhold or reverse decisions and resources",
          "Determines how much of the PM's personal attention is warranted"],
         ["Interest",
          "How much the stakeholder cares about the project outcome",
          "Predicts how actively they will seek involvement"],
         ["Influence",
          "Ability to affect the project through others, formally or informally",
          "Reveals people with little authority but high real effect"],
         ["Expectations and needs",
          "What this stakeholder believes success looks like for them",
          "The raw material for aligning expectations (ECO People T5)"],
         ["Communication requirements",
          "Preferred content, format, channel, frequency and language",
          "Drives the communications management plan"],
         ["Attitude / classification",
          "Unaware, resistant, neutral, supportive or leading",
          "Feeds the stakeholder engagement assessment matrix"]],
        n, kicker=cd.eco("People", 4), accent=VIOLET, widths=[2.0, 4.0, 4.0]); n += 1

    # ------------------------------------------------------------ 33 typical SH
    X.cards(prs, "Typical Project Stakeholders", [
        ("End users",
         "The people who will actually operate the product daily; their adoption "
         "decides whether benefits are realised or the system is worked around."),
        ("Customers",
         "Those who acquire or pay for the product — sometimes but not always the "
         "same people as the end users, a distinction worth making explicit."),
        ("Employees and the team",
         "Those doing the work and those whose jobs change because of it; both "
         "populations need engagement, not just the project team."),
        ("Sponsors and managers",
         "The sponsor funds and champions; functional managers control the "
         "resources you must borrow and can quietly withdraw them."),
        ("Business partners and suppliers",
         "Contractors, vendors and integrators whose commitments become your "
         "constraints and whose performance becomes your risk."),
        ("Government and community",
         "Regulators, standards bodies and affected communities who cannot be "
         "negotiated with but must be satisfied."),
    ], n, kicker=cd.eco("People", 4), accent=AMBER); n += 1

    # ------------------------------------------------------------ 34 OBS
    X.cards(prs, "Organisation Breakdown Structure as an Identification Tool", [
        ("What an OBS is",
         "A hierarchical decomposition of the organisation by department and "
         "reporting line, mirroring how the WBS decomposes the work."),
        ("Why it works",
         "Walking it forces a systematic sweep of every function rather than "
         "listing the stakeholders who happen to be top of mind."),
        ("Map work to units",
         "Cross the OBS against the WBS to see which organisational unit owns each "
         "work package — those owners are stakeholders by definition."),
        ("Find the silent affected",
         "Departments that receive the output but do no project work — finance, "
         "legal, support — surface only through this sweep."),
        ("Its blind spot",
         "An OBS only shows internal parties; regulators, customers and community "
         "groups must be found by other means."),
        ("Keep it alive",
         "Reorganisations change the OBS mid-project, which is a trigger to re-run "
         "stakeholder identification."),
    ], n, kicker=cd.eco("People", 4), accent=CYAN); n += 1

    # ------------------------------------------------------------ 35 artifacts
    X.table(prs, "Stakeholder and Communications Artefacts",
        ["Artefact", "What it holds", "When it is used"],
        [["Stakeholder register",
          "Identity, role, power, interest, influence, expectations, attitude",
          "Created in Identify Stakeholders; updated continuously"],
         ["Stakeholder engagement plan",
          "Strategies and actions to move each stakeholder to the desired level",
          "Part of the project management plan; drives daily engagement"],
         ["Communications management plan",
          "Who receives what information, in what format, how often, by whom",
          "Executed throughout; the operational half of engagement"],
         ["Stakeholder engagement assessment matrix (SEAM)",
          "Current (C) versus desired (D) engagement per stakeholder",
          "Reviewed in Monitor Stakeholder Engagement to target effort"],
         ["Assessment grids and models",
          "Power/interest, power/influence, impact/influence, cube, salience",
          "Used during analysis to prioritise and classify"],
         ["Issue log",
          "Stakeholder-raised issues, owners and resolution status",
          "Continuous — unresolved issues erode engagement fast"]],
        n, kicker=cd.eco("People", 4), accent=BLUE, widths=[2.4, 4.0, 3.6]); n += 1

    # ------------------------------------------------------------ 36 assess data
    X.compare(prs, "Assess Stakeholders: Data Gathering and Data Analysis",
        ("DATA GATHERING", "Collecting raw information about stakeholders", [
            "Questionnaires and surveys reach large, dispersed populations cheaply",
            "Surveys work well for end-user expectations across many sites",
            "Brainstorming with the team surfaces stakeholders nobody listed",
            "Brainwriting lets quieter contributors add names without pressure",
            "Interviews go deep with high-power individuals",
            "Focus groups expose disagreements between stakeholder groups"]),
        ("DATA ANALYSIS", "Turning raw information into engagement decisions", [
            "Stakeholder analysis produces a list of interests and their weight",
            "It classifies each party by power, interest, influence and attitude",
            "Document analysis mines charters, contracts and lessons learned",
            "Root-cause analysis explains WHY a stakeholder is resistant",
            "Assumption and constraint analysis tests what we believe about them",
            "Output feeds directly into the register and the engagement plan"]),
        n, kicker=cd.eco("People", 4), lc=TEAL, rc=VIOLET,
        footer_note="Gathering tells you who they are and what they say they want; "
                    "analysis tells you what to do about it. The exam frequently "
                    "asks you to sort a technique into the correct bucket."); n += 1

    # ------------------------------------------------------------ 37 data rep
    X.cards(prs, "Data Representation: Five Ways to Map Stakeholders", [
        ("2D grid: power/interest",
         "Classifies by authority to act against level of concern — the default "
         "grid, giving manage-closely, keep-satisfied, keep-informed, monitor."),
        ("2D grid: power/influence",
         "Classifies by formal authority against active involvement, useful when "
         "informal networks matter more than the org chart."),
        ("2D grid: impact/influence",
         "Classifies by ability to cause change against active involvement, best "
         "when the risk is disruption rather than opposition."),
        ("3D grid: the stakeholder cube",
         "Combines three dimensions at once so a stakeholder is a point in a "
         "volume, capturing combinations a flat grid flattens away."),
        ("Salience model",
         "Classifies by power, legitimacy and urgency, producing seven classes "
         "and identifying the definitive stakeholder who has all three."),
        ("Directions of influence",
         "Classifies by where the stakeholder sits relative to the PM — upward, "
         "downward, sideward or outward — shaping the engagement style."),
    ], n, kicker=cd.eco("People", 5), accent=ROSE); n += 1

    # ------------------------------------------------------------ 38 power/interest
    X.matrix2x2(prs, "Power / Interest Grid",
        "INTEREST IN THE OUTCOME  →  high", "high  ←  POWER OVER THE PROJECT",
        [("Keep satisfied",
          "High power, low interest. Sponsors' peers and senior executives. Brief "
          "them concisely and do not overload them; sudden interest is dangerous.",
          AMBER),
         ("Manage closely",
          "High power, high interest. The sponsor and key customers. Involve them "
          "in decisions, meet frequently and never surprise them.", ROSE),
         ("Monitor",
          "Low power, low interest. Peripheral departments. Minimal effort, but "
          "re-check periodically since positions change.", CYAN),
         ("Keep informed",
          "Low power, high interest. End users and subject experts. Communicate "
          "regularly; they are your best source of requirement detail.", TEAL)],
        n, kicker=cd.eco("People", 5), accent=BLUE,
        note="Power is the authority to impose your will. Interest is how much you "
             "care about the outcome. A stakeholder's position moves as the project "
             "progresses, so re-plot at every phase gate."); n += 1

    # ------------------------------------------------------------ 39 power/influence
    X.matrix2x2(prs, "Power / Influence Grid",
        "ACTIVE INVOLVEMENT (INFLUENCE)  →  high", "high  ←  FORMAL AUTHORITY (POWER)",
        [("Latent authority",
          "High power, low involvement. Can intervene decisively but currently "
          "does not. Keep the relationship warm before you need it.", AMBER),
         ("Decision makers",
          "High power, high involvement. They both can and do shape the project. "
          "Engage constantly and build genuine trust here.", ROSE),
         ("Bystanders",
          "Low power, low involvement. Monitor for changes in either dimension "
          "rather than investing engagement effort now.", CYAN),
         ("Opinion shapers",
          "Low power, high involvement. No formal authority but they move opinion "
          "through networks. Underestimating them is a classic failure.", VIOLET)],
        n, kicker=cd.eco("People", 5), accent=VIOLET,
        note="Power and influence are not the same thing. A respected long-serving "
             "engineer may have no authority and enormous influence — the "
             "power/influence grid exists precisely to expose that person."); n += 1

    # ------------------------------------------------------------ 40 impact/influence
    X.matrix2x2(prs, "Impact / Influence Grid",
        "INFLUENCE — ACTIVE INVOLVEMENT  →  high", "high  ←  IMPACT — ABILITY TO CAUSE CHANGE",
        [("High impact, low influence",
          "Can force change to the project but is not currently involved — for "
          "example a regulator. Engage proactively before they act.", AMBER),
         ("High impact, high influence",
          "Can both cause change and is actively involved. This is where your "
          "engagement plan must be strongest and most personal.", ROSE),
         ("Low impact, low influence",
          "Little ability to change the project and little involvement. Standard "
          "project communications are sufficient here.", CYAN),
         ("Low impact, high influence",
          "Actively involved but cannot force change. Valuable allies and useful "
          "advocates — recruit them deliberately.", TEAL)],
        n, kicker=cd.eco("People", 5), accent=TEAL,
        note="Impact asks 'can they change the project?' Influence asks 'are they "
             "in the room?' The dangerous quadrant is high impact with low "
             "influence — they act without warning."); n += 1

    # ------------------------------------------------------------ 41 cube
    X.cards(prs, "The Stakeholder Cube — Three Dimensions at Once", [
        ("Why a cube",
         "Two-dimensional grids lose information: two stakeholders can share a "
         "quadrant yet need completely different engagement approaches."),
        ("Dimension one: power",
         "The stakeholder's level of authority to impose decisions on the project "
         "or withhold what the project needs."),
        ("Dimension two: interest",
         "The degree to which the stakeholder cares about and attends to the "
         "project's outcome."),
        ("Dimension three: attitude",
         "Whether the stakeholder is supportive, neutral or resistant — the "
         "dimension flat grids most often omit."),
        ("What it reveals",
         "A high-power, high-interest, resistant stakeholder is a very different "
         "problem from a high-power, high-interest supporter."),
        ("How to use it",
         "Treat each cell as a distinct engagement archetype and write a tailored "
         "strategy per archetype in the engagement plan."),
    ], n, kicker=cd.eco("People", 5), accent=CYAN); n += 1

    # ------------------------------------------------------------ 42 salience
    X.matrix2x2(prs, "Salience Model — Power, Legitimacy, Urgency",
        "LEGITIMACY — IS THE CLAIM APPROPRIATE?  →", "→  POWER TO IMPOSE WILL",
        [("Dominant (power + legitimacy)",
          "Real authority and a proper claim, but no time pressure. Sponsors and "
          "steering members. Engage on a planned cadence.", ROSE),
         ("Definitive (all three)",
          "Power, legitimacy AND urgency together. The highest-salience class — "
          "act on their claims immediately and personally.", VIOLET),
         ("Discretionary (legitimacy only)",
          "A proper claim but no power or urgency, such as a community group. "
          "Engagement here is a choice, often an ethical one.", TEAL),
         ("Dependent (legitimacy + urgency)",
          "A legitimate, pressing claim but no power to enforce it — end users. "
          "They depend on an advocate; often the PM.", AMBER)],
        n, kicker=cd.eco("People", 5), accent=VIOLET,
        note="Seven classes exist in total. The other three are single-attribute: "
             "Dormant (power only), Demanding (urgency only) and Dangerous "
             "(power + urgency but no legitimacy — coercive, watch closely)."); n += 1

    # ------------------------------------------------------------ 43 salience table
    X.table(prs, "The Seven Salience Classes in Full",
        ["Class", "Attributes held", "Typical example", "Engagement response"],
        [["Dormant", "Power only", "A regulator not yet engaged",
          "Monitor; the power can activate at any time"],
         ["Discretionary", "Legitimacy only", "A community or charity group",
          "Engage by choice; usually a reputational decision"],
         ["Demanding", "Urgency only", "A vocal individual user",
          "Acknowledge but do not let noise set priority"],
         ["Dominant", "Power + legitimacy", "Sponsor, steering committee",
          "Formal, planned, regular engagement"],
         ["Dangerous", "Power + urgency", "A coercive group applying pressure",
          "Manage carefully; escalate; involve governance"],
         ["Dependent", "Legitimacy + urgency", "End users needing an advocate",
          "Give them a voice through a powerful sponsor"],
         ["Definitive", "Power + legitimacy + urgency", "Customer at a crisis point",
          "Immediate, personal, highest-priority attention"]],
        n, kicker=cd.eco("People", 5), accent=ROSE, widths=[1.6, 2.4, 3.0, 3.0]); n += 1

    # ------------------------------------------------------------ 44 directions
    X.cards(prs, "Directions of Influence", [
        ("Upward",
         "Senior management, the sponsor and the steering committee. Engage with "
         "concise, decision-ready information and never surprise them in public."),
        ("Downward",
         "The project team and specialists providing knowledge or skills. Engage "
         "by clarifying purpose, removing impediments and empowering decisions."),
        ("Sideward",
         "Peers of the project manager and other middle managers who control the "
         "resources you borrow. Engage through negotiation and reciprocity."),
        ("Outward",
         "Suppliers, users, government departments and the public. Engage through "
         "formal agreements, structured consultation and compliance evidence."),
        ("Why direction matters",
         "The same message needs a different form in each direction; a status "
         "report that satisfies the sponsor will not motivate the team."),
        ("Where PMs under-invest",
         "Sideward influence is the most commonly neglected direction, and it is "
         "where resource conflicts are actually resolved."),
    ], n, kicker=cd.eco("People", 4), accent=AMBER); n += 1

    # ------------------------------------------------------------ 45 mapping process
    X.process(prs, "Stakeholder Mapping, Step by Step", [
        ("List from the register",
         "Take every identified stakeholder as a candidate — do not pre-filter "
         "by who seems important."),
        ("Score each dimension",
         "Rate power, interest, influence and attitude on a consistent scale, "
         "with the team, not alone."),
        ("Plot on the grid",
         "Place each stakeholder on the chosen model so the pattern becomes "
         "visible rather than anecdotal."),
        ("Derive strategies",
         "Write a specific engagement action per quadrant, naming who does what "
         "and how often."),
        ("Re-plot each phase",
         "Positions shift as the project progresses; a stale map produces "
         "misdirected effort."),
    ], n, kicker=cd.eco("People", 5), accent=BLUE,
        note="Keep the completed map confidential. A grid that labels a named "
             "executive as low-power, high-resistance is professionally damaging if "
             "it circulates — this is an ethics point as well as a practical one."); n += 1

    # ------------------------------------------------------------ 46 SEAM
    X.table(prs, "Stakeholder Engagement Assessment Matrix (SEAM)",
        ["Stakeholder", "Unaware", "Resistant", "Neutral", "Supportive", "Leading"],
        [["Operations Director", "", "C", "", "D", ""],
         ["Finance Manager", "", "", "C", "D", ""],
         ["End-user representative", "", "", "", "C / D", ""],
         ["External regulator", "C", "", "D", "", ""],
         ["IT Infrastructure lead", "", "", "C", "", "D"]],
        n, kicker=cd.eco("People", 6), accent=TEAL, widths=[3.0, 1.4, 1.4, 1.4, 1.6, 1.4],
        note="C marks current engagement, D marks desired. Every gap between C and "
             "D is an action item for the stakeholder engagement plan. Where C "
             "equals D, protect the position rather than invest further."); n += 1

    # ------------------------------------------------------------ 47 engagement chart
    X.chart(prs, "Engagement Levels Across the Stakeholder Population",
        "column",
        ["Unaware", "Resistant", "Neutral", "Supportive", "Leading"],
        [("Current engagement (count)", [6, 8, 14, 9, 3]),
         ("Desired engagement (count)", [0, 2, 8, 21, 9])],
        n, kicker=cd.eco("People", 6), accent=CYAN,
        insight=["Six unaware stakeholders is an identification and communication "
                 "failure, not an attitude problem — inform them first.",
                 "Eight resistant stakeholders need root-cause analysis: resistance "
                 "usually signals an unaddressed expectation, not obstinacy.",
                 "The desired profile deliberately keeps two resistant: total "
                 "consensus is unrealistic and often means dissent is hidden.",
                 "Moving fourteen neutrals to supportive is the highest-leverage "
                 "engagement investment available on this project."]); n += 1

    # ------------------------------------------------------------ 48 monitor
    X.cards(prs, "Monitor Stakeholder Engagement", [
        ("What the process does",
         "Monitors project stakeholder relationships and tailors strategies for "
         "engaging stakeholders through modification of plans and approaches."),
        ("Key input: the SEAM",
         "The current-versus-desired matrix is re-scored regularly; movement in "
         "the wrong direction is an early warning signal."),
        ("Watch the issue log",
         "A rising count of unresolved stakeholder issues predicts a drop in "
         "engagement long before anyone says so openly."),
        ("Watch participation",
         "Declining attendance at reviews, slow sign-offs and delegated attendance "
         "are behavioural signals of falling engagement."),
        ("Monitor satisfaction explicitly",
         "ECO People T6 requires monitoring internal and external customer "
         "satisfaction and expectations — and responding as needed."),
        ("Outputs",
         "Work performance information, change requests, and updates to the plan, "
         "the register, the issue log and the risk register."),
    ], n, kicker=cd.eco("People", 6), accent=VIOLET); n += 1

    # ------------------------------------------------------------ 49 statement align
    X.statement(
        prs, "ECO 2026 People Task 5 — Align Stakeholder Expectations",
        "Most project conflict is not\ndisagreement. It is two people\nholding different definitions of done.",
        [("Categorize stakeholders",
          "Group them so expectations can be surfaced and reconciled by group "
          "rather than one conversation at a time."),
         ("Identify expectations",
          "Ask directly what each group believes success looks like — do not infer "
          "it from the requirements document."),
         ("Facilitate alignment",
          "Bring conflicting parties into the same conversation and converge them "
          "on one agreed definition.")],
        n, kicker=cd.eco("People", 5), accent=ROSE); n += 1

    # ------------------------------------------------------------ 50 align process
    X.process(prs, "Facilitating an Expectation-Alignment Session", [
        ("Surface privately first",
         "Interview each group separately so positions are honest before they "
         "become public and defended."),
        ("Categorise the gaps",
         "Group differences by theme — scope, quality, timing, cost — so the "
         "session has structure."),
        ("Convene the parties",
         "Bring conflicting stakeholders together with the sponsor present to "
         "supply decision authority."),
        ("Converge to one definition",
          "Drive to a single written statement of objectives and acceptance "
          "criteria that all parties sign."),
        ("Document and republish",
         "Update the charter, register and requirements so the agreement survives "
         "memory and staff turnover."),
    ], n, kicker=cd.eco("People", 5), accent=TEAL,
        note="ECO People T5 also lists 'organize and act on mentoring "
             "opportunities'. Alignment sessions are where a PM can mentor "
             "stakeholders in how project trade-offs actually work."); n += 1

    # ------------------------------------------------------------ 51 manage exp
    X.cards(prs, "ECO People Task 6 — Manage Stakeholder Expectations", [
        ("Identify customer expectations",
         "Distinguish internal customers (other departments receiving the output) "
         "from external customers (paying clients and end users) explicitly."),
        ("Align outcomes continuously",
         "Maintain the fit between what is being built and what customers expect, "
         "rather than confirming alignment only at acceptance."),
        ("Monitor satisfaction",
         "Use surveys, net promoter scores, review attendance and complaint rates "
         "as running indicators of customer satisfaction."),
        ("Respond as needed",
         "The enabler explicitly requires response, not just measurement — a "
         "satisfaction survey nobody acts on is worse than none."),
        ("Manage expectation drift",
         "Expectations inflate over a long project; periodic re-confirmation "
         "against the charter prevents a scope surprise at acceptance."),
        ("Under-promise deliberately",
         "Committing to what you can reliably deliver protects trust far more than "
         "an optimistic commitment that slips."),
    ], n, kicker=cd.eco("People", 6), accent=AMBER); n += 1

    # ------------------------------------------------------------ 52 trust
    X.cards(prs, "Building Trust and Influence Without Authority", [
        ("Trust is the engagement multiplier",
         "ECO People T4 explicitly requires building trust and influencing "
         "stakeholders to accomplish project objectives — it is an assessed skill."),
        ("Competence",
         "Demonstrate that your estimates, forecasts and status reports have been "
         "accurate before; credibility is built from a track record."),
        ("Consistency",
         "Behave the same way under pressure as you do in calm periods; "
         "inconsistency is what stakeholders read as risk."),
        ("Transparency",
         "Report bad news early and unvarnished. A PM who hides a slip once is "
         "never fully believed again."),
        ("Reciprocity",
         "Help peers with their problems before you need help with yours — this is "
         "the currency of sideward influence."),
        ("Follow-through",
         "Close every commitment visibly. Small kept promises compound into the "
         "influence you need when the stakes are large."),
    ], n, kicker=cd.eco("People", 4), accent=CYAN); n += 1

    # ------------------------------------------------------------ 53 exam stakeholders
    X.exam(prs, "Exam Traps: Stakeholders and Engagement", [
        ("A previously unknown stakeholder appears mid-project with requirements",
         "Add them to the stakeholder register and analyse them first, before "
         "assessing the impact of their requirements."),
        ("A key stakeholder is resistant and you must decide what to do",
         "Meet them to understand the root cause of the resistance. Do not "
         "escalate, exclude, or simply add more reports."),
        ("You are asked which model uses power, legitimacy and urgency",
         "The salience model. Power/interest, power/influence and impact/influence "
         "are all two-dimensional grids."),
        ("Stakeholders disagree about what the project should deliver",
         "Facilitate a discussion to align expectations against the charter — "
         "alignment first, change request only if truly needed."),
    ], n, kicker="EXAM FOCUS", accent=ROSE); n += 1

    # ------------------------------------------------------------ 54 comm channels
    X.formula(prs, "Communication Channels and Why Team Size Matters", [
        ("Communication channels",
         "N × (N − 1) / 2",
         "N is the number of people. Channels grow quadratically, which is why "
         "small teams communicate so much more cheaply."),
        ("Team of 5",
         "5 × 4 / 2 = 10",
         "Ten channels — everyone can plausibly stay in sync through informal "
         "conversation alone."),
        ("Team of 10",
         "10 × 9 / 2 = 45",
         "Forty-five channels. Informal alignment starts failing; explicit "
         "communication planning becomes necessary."),
        ("Adding one person to 10",
         "55 − 45 = 10 new channels",
         "The eleventh person adds ten channels, not one — the arithmetic behind "
         "'adding people to a late project makes it later'."),
    ], n, kicker=cd.eco("People", 8), accent=BLUE,
        note="Exam tip: if a question adds or removes people, compute channels "
             "before and after and report the DIFFERENCE — that is usually what is "
             "being asked, not the absolute number."); n += 1

    # ------------------------------------------------------------ 55 agile consid
    X.cards(prs, "Agile Considerations for Starting Well", [
        ("The whole-team approach",
         "All skills needed to deliver sit inside one team, removing the hand-off "
         "delays and the finger-pointing that cross-functional silos create."),
        ("Small teams",
         "Typically three to nine people, keeping communication channels low "
         "enough that alignment happens naturally rather than by process."),
        ("Co-location",
         "Physical or deliberate virtual co-location maximises the osmotic "
         "communication that makes small teams fast."),
        ("Close customers",
         "A customer representative available continuously replaces long "
         "requirement documents with short conversations and fast feedback."),
        ("Information radiators",
         "Big visible charts — task boards, burndowns, impediment lists — in the "
         "team space so status is pulled, not reported."),
        ("Osmotic communication",
         "Useful information overheard in a shared space; team members absorb "
         "context without anyone scheduling a meeting to transmit it."),
    ], n, kicker=cd.eco("People", 8), accent=TEAL); n += 1

    # ------------------------------------------------------------ 56 self-org
    X.compare(prs, "Traditional Management vs Servant Leadership",
        ("TRADITIONAL COMMAND AND CONTROL",
         "The manager holds the plan and issues the assignments", [
            "The manager assigns tasks to named individuals",
            "Decisions escalate up and instructions come back down",
            "Status is reported to the manager who consolidates it",
            "The manager owns the estimates and commits on the team's behalf",
            "Problems are solved by the manager and communicated as decisions",
            "Performance is managed individually against assigned tasks"]),
        ("SERVANT LEADERSHIP",
         "The leader removes impediments so the team can lead itself", [
            "The team pulls work from a prioritised backlog",
            "Decisions are made at the level with the most information",
            "Status is visible to everyone on a radiator, always current",
            "The team estimates and commits to what it believes it can do",
            "The leader's first question is 'what is blocking you?'",
            "Performance is a team outcome, improved through retrospectives"]),
        n, kicker=cd.eco("People", 3), lc=AMBER, rc=TEAL,
        footer_note="Servant leadership: the practice of leading by understanding "
                    "and addressing the needs and development of team members, in "
                    "order to enable the highest possible team performance."); n += 1

    # ------------------------------------------------------------ 57 self org team
    X.cards(prs, "Self-Organising Teams", [
        ("The definition",
         "A cross-functional team in which people fluidly assume leadership as "
         "needed to achieve the team's objectives, rather than by fixed title."),
        ("Cross-functional by design",
         "The team collectively holds every skill required to take an item from "
         "idea to done, so no external hand-off is needed."),
        ("Leadership is situational",
         "Whoever has the most relevant expertise leads that decision, then hands "
         "leadership on — authority follows knowledge."),
        ("The leader still matters",
         "Self-organising does not mean unled: the servant leader sets boundaries, "
         "protects focus and removes impediments from outside."),
        ("What it requires",
         "Psychological safety, a clear goal, real decision authority and time — "
         "teams do not become self-organising by being told to be."),
        ("Why it is faster",
         "Decisions are made where the information already is, eliminating the "
         "escalate-and-wait cycle that dominates traditional structures."),
    ], n, kicker=cd.eco("People", 3), accent=VIOLET); n += 1

    # ------------------------------------------------------------ 58 roles
    X.table(prs, "Project Team Roles You Must Distinguish",
        ["Role", "Accountable for", "Not accountable for"],
        [["Project manager",
          "Integration, the plan, stakeholder engagement and delivery of objectives",
          "Doing the technical work or approving their own charter"],
         ["Project sponsor",
          "Funding, the business case, charter approval and removing senior blockers",
          "Day-to-day management of the project team"],
         ["Team members",
          "Producing the deliverables and estimating their own work",
          "Setting priority between competing business needs"],
         ["Product owner",
          "Backlog priority, maximising value and representing the customer voice",
          "Telling the team how to build it or managing their performance"],
         ["Scrum master / facilitator",
          "Process health, removing impediments, coaching and shielding the team",
          "Assigning work, estimating for the team or setting priority"],
         ["Functional manager",
          "Supplying skilled resources and developing their people's capability",
          "Directing project scope or accepting project deliverables"]],
        n, kicker=cd.eco("People", 3), accent=BLUE, widths=[2.2, 4.0, 3.8]); n += 1

    # ------------------------------------------------------------ 59 T-shaped
    X.cards(prs, "T-Shaped People and Why Teams Want Them", [
        ("What T-shaped means",
         "Deep expertise in one discipline — the vertical stroke — plus working "
         "competence across several others, the horizontal stroke."),
        ("Individual value and versatility",
         "T-shaped people contribute their specialism at full depth while still "
         "being able to pick up adjacent work when the queue demands it."),
        ("Flexibility for the organisation",
         "Teams can rebalance around a bottleneck without waiting for a new hire "
         "or a formal resource request."),
        ("Avoids work stoppages",
         "Reduces the key-person dependency that halts a whole team when one "
         "specialist takes leave or resigns."),
        ("Built deliberately",
         "Train and coach team members to become T-shaped through pairing, "
         "rotation and shadowing — it does not happen by accident."),
        ("The contrast",
         "I-shaped specialists create hand-off queues; generalists without depth "
         "create quality problems. T-shaped is the balance."),
    ], n, kicker=cd.eco("People", 3), accent=CYAN); n += 1

    # ------------------------------------------------------------ 60 team charter
    X.table(prs, "Team Charter and Ground Rules — What Goes In",
        ["Section", "What the team agrees", "Example agreement"],
        [["Shared values",
          "The principles the team holds itself to",
          "We surface bad news early and without blame"],
         ["Behaviour guidelines",
          "How members treat each other day to day",
          "One conversation at a time; no interrupting"],
         ["Communication and tools",
          "Which channel is used for what and expected response times",
          "Chat for the day, email for decisions, board for status"],
         ["Decision-making",
          "How the team decides and what needs consensus",
          "Fist-of-five; a two-thirds majority carries technical decisions"],
         ["Performance expectations",
          "What good contribution looks like on this team",
          "Definition of done applies to every item, no exceptions"],
         ["Conflict resolution",
          "The agreed path when disagreement escalates",
          "Direct conversation, then the team, then the servant leader"],
         ["Meetings",
          "Time, frequency and channel of each ceremony",
          "Stand-up 09:15 daily, 15 minutes, cameras on"],
         ["Other agreements",
          "Shared core hours, improvement time and team norms",
          "Core hours 10:00-16:00; Friday afternoon for improvement work"]],
        n, kicker=cd.eco("People", 2), accent=AMBER, widths=[2.2, 4.0, 3.8],
        note="Critical point: the team charter is created WITH the team, not "
             "issued to it. A charter written by the PM alone produces compliance, "
             "not commitment — and ground rules nobody helped write get broken."); n += 1

    # ------------------------------------------------------------ 61 ground rules
    X.cards(prs, "Making Ground Rules Actually Work", [
        ("Make it visible",
         "An electronic document or a poster on the team wall — ground rules "
         "filed in a shared drive stop influencing behaviour within a week."),
        ("Co-create it",
         "Rules the team wrote itself are enforced by the team; rules imposed on "
         "the team are enforced only by the manager, and only when watching."),
        ("Keep it short",
         "Six to ten rules the team can recall beats a thirty-item document "
         "nobody has finished reading."),
        ("Address violations early",
         "ECO People T2 requires managing and rectifying ground-rule violations — "
         "an unaddressed breach becomes the new de facto rule."),
        ("Model it from the top",
         "The project manager who breaks a ground rule cancels it for everyone, "
         "regardless of what the poster says."),
        ("Revisit at retrospectives",
         "Rules that no longer serve the team are removed and new ones added as "
         "the team's context changes."),
    ], n, kicker=cd.eco("People", 2), accent=ROSE); n += 1

    # ------------------------------------------------------------ 62 kickoff
    X.compare(prs, "The Kick-Off Meeting: Two Distinct Audiences",
        ("ORGANISATIONAL / PUBLIC KICK-OFF",
         "Announcing the project to the wider organisation", [
            "Formally announce project initiation to the organisation",
            "Share a common understanding of the high-level vision and purpose",
            "State the business value the project will deliver",
            "Identify the sponsor, key stakeholders and the project manager",
            "Present high-level items drawn from the project charter",
            "Signal executive commitment so the project is taken seriously"]),
        ("INTERNAL / TEAM KICK-OFF",
         "Turning a group of assigned people into a project team", [
            "Give an overview of the project charter and its objectives",
            "Clarify each team member's role and responsibilities",
            "Present the results of planning efforts completed so far",
            "Initiate the product backlog or the initial work breakdown",
            "Agree the team charter and ground rules together",
            "Establish the ceremony cadence and communication norms"]),
        n, kicker=cd.eco("People", 1), lc=BLUE, rc=TEAL,
        footer_note="Purpose of any kick-off: establish project context, assist in "
                    "team formation, and align team and stakeholders with the "
                    "project vision."); n += 1

    # ------------------------------------------------------------ 63 kickoff timeline
    X.timeline(prs, "When Kick-Off Happens in Each Approach", [
        ("Predictive",
         "One kick-off after planning is largely complete, because the plan is "
         "what is being communicated."),
        ("Iterative",
         "Kick-off at the start, then a re-alignment at each major iteration "
         "boundary as the solution takes shape."),
        ("Incremental",
         "Kick-off at the start plus a short launch for each increment, focused "
         "on the value being shipped."),
        ("Agile / adaptive",
         "A short project kick-off, then effectively a mini kick-off every sprint "
         "at sprint planning."),
        ("Hybrid",
         "A formal organisational kick-off for governance, plus agile ceremonies "
         "for the delivery team."),
    ], n, kicker=cd.eco("Process", 1), accent=VIOLET,
        note="Exam cue: in predictive projects the kick-off usually occurs at the "
             "END of planning; in adaptive projects it occurs at the start of "
             "execution and repeats each iteration."); n += 1

    # ------------------------------------------------------------ 64 exam start
    X.exam(prs, "Exam Traps: Charter, Team and Kick-Off", [
        ("You are newly assigned as PM and asked what to do first",
         "Read the project charter and the business documents to understand "
         "objectives, then identify stakeholders."),
        ("A team member asks who assigns work on an agile team",
         "Nobody assigns it. The team self-organises and pulls work from the "
         "prioritised backlog."),
        ("The team is repeatedly missing agreed stand-up times",
         "Address the ground-rule violation with the team and revisit the team "
         "charter together — do not escalate first."),
        ("A predictive project asks when the kick-off should be held",
         "At the end of planning, once there is an integrated plan worth "
         "communicating to stakeholders."),
    ], n, kicker="EXAM FOCUS", accent=ROSE); n += 1

    # ------------------------------------------------------------ 65 recap
    X.recap(prs, "Topic 2 Recap — Start the Project", [
        ("Integration is the PM's job",
         "Unifying scope, schedule, cost, quality, risk and stakeholders so they "
         "deliver one coherent business value."),
        ("The charter authorises",
         "Signed by the sponsor, it empowers the PM, states measurable objectives "
         "and anchors all later change control."),
        ("Business documents justify",
         "Business case, cost-benefit analysis and benefits management plan exist "
         "before the project and outlive it."),
        ("Know the six value drivers",
         "Financial gain, new customers, social benefit, first to market, "
         "improvement and regularization."),
        ("Financial metrics rank options",
         "Bigger is better for NPV, IRR, ROI and BCR; smaller is better for "
         "payback period and opportunity cost."),
        ("Identify stakeholders early",
         "Use the OBS, document analysis and brainstorming, and record everything "
         "in the stakeholder register."),
        ("Analyse before you engage",
         "Power/interest, power/influence, impact/influence, the cube and the "
         "salience model each answer a different question."),
        ("Align, then manage expectations",
         "ECO People T5 and T6: surface expectations, converge them, then monitor "
         "customer satisfaction and respond."),
        ("Start the team deliberately",
         "Co-create the team charter and ground rules; build T-shaped, "
         "self-organising capability through servant leadership."),
        ("Kick off with purpose",
         "Establish context, form the team and align everyone with the project "
         "vision before execution begins."),
    ], n, kicker="RECAP", accent=CYAN); n += 1

    return n
