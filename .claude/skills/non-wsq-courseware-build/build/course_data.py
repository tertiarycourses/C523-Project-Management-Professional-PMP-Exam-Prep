"""
SINGLE SOURCE OF TRUTH — Project Management Professional (PMP) Exam Prep (C523).

Every artifact (PPT, Lesson Plan, Learner Guide, LG.md) is generated from this
module plus data_domain1.py … data_domain6.py, so they cannot drift apart.

Content mirrors the PMI PMP Examination Content Outline (ECO), July 2026:
People 33% / Process 41% / Business Environment 26%.

NON-WSQ COURSE — there is no assessment, no funding, no SSG/SkillsFuture
content, no TRAQOM, no digital attendance, and no TGS- reference anywhere.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Project Management Professional (PMP) Exam Prep"
SHORT_TITLE  = "PMP-Exam-Prep"
COURSE_CODE  = "C523"
VERSION      = "v1.0"
VERSION_DATE = "20 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 4
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Scope project requirements and build a business case, charter and "
    "traceable scope baseline that authorise delivery.",
    "LO2: Develop an integrated project plan with realistic schedule, cost and "
    "resource baselines using PERT, critical path and reserve analysis.",
    "LO3: Lead a project team through its development stages, applying "
    "leadership style, motivation theory and structured conflict resolution.",
    "LO4: Analyse project risk quantitatively and engage stakeholders through a "
    "planned communication and escalation cadence.",
    "LO5: Control delivery against baselines with earned value, flow metrics "
    "and statistical process control, then close the project and realise benefits.",
    "LO6: Apply the PMI PMP Examination Content Outline (ECO 2026) across all "
    "three domains and sit a full-format mock exam with domain score analysis.",
]

LO_TITLES = [
    "Scope & Authorise",
    "Plan & Baseline",
    "Lead the Team",
    "Risk & Stakeholders",
    "Control & Close",
    "Exam Readiness",
]

# ------------------------------------------------------- ECO 2026 reference
ECO_DOMAINS = [
    ("I", "People", 33, "How you lead, align and communicate with the humans on "
                        "and around the project."),
    ("II", "Process", 41, "How you plan, deliver, measure and close the work itself."),
    ("III", "Business Environment", 26, "How the project connects to governance, "
                                        "compliance, risk and organisational change."),
]

ECO_EXAM = {
    "questions": 180,
    "scored": 170,
    "pretest": 10,
    "minutes": 240,
    "breaks": "Two 10-minute breaks — the first after the case-study section, the "
              "second midway through the independent questions.",
    "approach_mix": "About 40% predictive; the remaining 60% split between "
                    "adaptive/agile and hybrid.",
    "question_types": [
        ("Multiple choice", "One best answer from four options — the bulk of the exam."),
        ("Multiple response", "More than one correct answer; the item tells you how many."),
        ("Matching", "Drag items from one column to match a second column."),
        ("Enhanced matching", "Matching that includes an image or diagram for context."),
        ("Graphic-based (NEW)", "Read a chart, graph, diagram or image, then answer from it."),
        ("Case study", "A scenario with supporting visuals, then a series of linked questions."),
    ],
}

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Business Environment",
         subtitle="Foundations · governance · compliance · change · development approaches",
         concepts=[
            "A project is a temporary endeavour creating a unique product, service "
            "or result — it is bounded in time and delivers change, unlike operations.",
            "The 12 PMI principles and the triple constraint frame every tailoring "
            "decision you make on the exam and on the job.",
            "Two life cycles, five approaches: the project life cycle is the phases; "
            "the development life cycle is predictive, iterative, incremental, agile or hybrid.",
            "EEFs constrain you and OPAs are reusable assets — you conform to EEFs, "
            "you apply and then update OPAs.",
            "Governance sets escalation thresholds: escalate outside tolerance with "
            "options, resolve inside tolerance with the team; phase gates decide go, change, hold or kill.",
            "Compliance, sustainability and the responsible use of AI are the project "
            "manager's own obligations, not someone else's department.",
         ]),

    dict(num=2, code="02",
         title="Start the Project",
         subtitle="Business case · charter · stakeholders · team formation",
         concepts=[
            "The business case justifies the project; the charter authorises it. The "
            "business case can exist without a project — the charter cannot.",
            "Cost-benefit analysis with NPV, payback and BCR turns a proposal into a "
            "defensible investment decision.",
            "The charter is issued by the sponsor, names the project manager and "
            "states their authority level — it is high level and rarely changed.",
            "Stakeholder identification, power/interest analysis and the salience "
            "model determine who gets what engagement and how often.",
            "The team charter establishes ground rules and a shared vision before the "
            "first conflict, not after it.",
            "The development approach is a documented tailoring decision justified by "
            "project context — never a personal preference.",
         ]),

    dict(num=3, code="03",
         title="Plan the Project",
         subtitle="Scope · schedule · cost · quality · resources · communications · risk",
         concepts=[
            "The integrated project management plan is the sum of subsidiary plans "
            "plus the scope, schedule and cost baselines.",
            "Requirements elicitation feeds a requirements traceability matrix so "
            "every deliverable traces back to a business need.",
            "MoSCoW and Kano prioritise the backlog by value; the WBS decomposes "
            "scope to work packages with a WBS dictionary.",
            "PERT three-point estimating and critical path analysis expose which "
            "activities actually drive the finish date and where float exists.",
            "Cost estimating produces a budget with contingency reserve for known "
            "unknowns and management reserve for unknown unknowns.",
            "Risk identification, qualitative and quantitative analysis with EMV and "
            "decision trees produce a risk register with owned responses.",
         ]),

    dict(num=4, code="04",
         title="Lead the Project Team",
         subtitle="Leadership · motivation · conflict · coaching · communication",
         concepts=[
            "Tuckman's forming, storming, norming, performing and adjourning gives "
            "you a diagnosis, and each stage calls for a different leadership response.",
            "Situational leadership, servant leadership and motivation theory "
            "(Maslow, Herzberg, McClelland, Theory X/Y) drive team performance.",
            "RACI removes ambiguity: exactly one Accountable per work package, "
            "Responsible parties who do the work.",
            "The five conflict modes — collaborate, compromise, smooth, force, "
            "withdraw — are chosen by context; collaborate/problem-solve is preferred.",
            "The channels formula n(n-1)/2 shows why communication complexity grows "
            "faster than team size.",
            "A communication plan defines who needs what information, in what format, "
            "how often, and through which channel.",
         ]),

    dict(num=5, code="05",
         title="Monitor and Control the Project",
         subtitle="Earned value · flow metrics · quality control · change control · issues",
         concepts=[
            "Earned value management combines scope, schedule and cost into CPI, SPI, "
            "EAC and VAC — it tells you THAT something is wrong, not why.",
            "Schedule compression is a choice between crashing (adds cost) and "
            "fast-tracking (adds risk); both must be justified against the baseline.",
            "Kanban flow metrics — WIP limits, lead time and cycle time — expose "
            "bottlenecks that a Gantt chart hides.",
            "Root cause analysis with 5 Whys, fishbone and Pareto finds the vital few "
            "causes behind most of the pain.",
            "Statistical process control separates assignable causes from common-cause "
            "noise, and a stable process can still fail its specification.",
            "Integrated change control evaluates every change against all baselines "
            "before approval — the change control board decides, the PM does not.",
         ]),

    dict(num=6, code="06",
         title="Close the Project",
         subtitle="Acceptance · transition · benefits realisation · lessons learned · exam strategy",
         concepts=[
            "Closure requires formal stakeholder acceptance against documented "
            "criteria, not merely the end of the work.",
            "Transition readiness moves the deliverable to operations with the "
            "support, documentation and training that make it sustainable.",
            "Benefits realisation is measured after go-live against the business "
            "case — the project ends, the benefits do not.",
            "Lessons learned only count when they update an organisational process "
            "asset that the next project inherits.",
            "Knowledge transfer protects the organisation from the loss of the team "
            "that built the thing.",
            "Exam strategy: read the last sentence first, identify the development "
            "approach in play, and eliminate answers that bypass the process.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Business Environment & Starting the Project",
    2: "Planning the Project",
    3: "Leading the Team & Controlling Delivery",
    4: "Closing, Exam Strategy & Practice",
}


# ------------------------------------------------------------------ schedule
# Each day totals exactly 480 training minutes (lunch excluded).
# The WSQ assessment block is removed; that time is reallocated into hands-on
# lab time and a longer end-of-day recap.
def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:30", "9:50", 20, "admin", "Welcome, course introduction, exam overview and ground rules"),
            ("9:50", "10:50", 60, "topic", "Topic 1 — Business Environment: projects, principles, life cycles and development approaches"),
            ("10:50", "11:05", 15, "break", "Tea break"),
            ("11:05", "11:35", 30, "topic", "Topic 1 — EEFs, OPAs, governance, escalation, compliance and sustainability"),
            ("11:35", "13:00", 85, "lab", "Hands-on: " + lab_titles([1, 2])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:30", 90, "lab", "Hands-on: " + lab_titles([3, 4])),
            ("15:30", "15:45", 15, "break", "Tea break"),
            ("15:45", "16:30", 45, "topic", "Topic 2 — Start the Project: business case, charter, stakeholders and team"),
            ("16:30", "18:00", 90, "lab", "Hands-on: " + lab_titles([5, 6])),
            ("18:00", "18:30", 30, "recap", "Day 1 recap, exam-style question drill and Q&A"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:30", "9:45", 15, "recap", "Day 1 review and exam-style warm-up questions"),
            ("9:45", "11:00", 75, "lab", "Hands-on: " + lab_titles([7, 8])),
            ("11:00", "11:15", 15, "break", "Tea break"),
            ("11:15", "12:00", 45, "topic", "Topic 3 — Plan the Project: the integrated plan, scope and requirements"),
            ("12:00", "13:00", 60, "lab", "Hands-on: " + lab_titles([9])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:30", 90, "lab", "Hands-on: " + lab_titles([10, 11])),
            ("15:30", "15:45", 15, "break", "Tea break"),
            ("15:45", "16:15", 30, "topic", "Topic 3 — Schedule, cost and reserve analysis"),
            ("16:15", "18:00", 105, "lab", "Hands-on: " + lab_titles([12, 13])),
            ("18:00", "18:30", 30, "recap", "Day 2 recap, formula drill and Q&A"),
        ]),
        3: (DAY_THEMES[3], [
            ("9:30", "9:45", 15, "recap", "Day 2 review and formula warm-up"),
            ("9:45", "10:30", 45, "lab", "Hands-on: " + lab_titles([14])),
            ("10:30", "11:15", 45, "topic", "Topic 4 — Lead the Project Team: leadership, motivation and conflict"),
            ("11:15", "11:30", 15, "break", "Tea break"),
            ("11:30", "13:00", 90, "lab", "Hands-on: " + lab_titles([15, 16])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:30", 90, "lab", "Hands-on: " + lab_titles([17, 18])),
            ("15:30", "15:45", 15, "break", "Tea break"),
            ("15:45", "16:15", 30, "topic", "Topic 5 — Monitor and Control: earned value, quality and change control"),
            ("16:15", "18:00", 105, "lab", "Hands-on: " + lab_titles([19, 20])),
            ("18:00", "18:30", 30, "recap", "Day 3 recap, EVM drill and Q&A"),
        ]),
        4: (DAY_THEMES[4], [
            ("9:30", "9:45", 15, "recap", "Day 3 review and EVM warm-up"),
            ("9:45", "11:15", 90, "lab", "Hands-on: " + lab_titles([21])),
            ("11:15", "11:30", 15, "break", "Tea break"),
            ("11:30", "13:00", 90, "lab", "Hands-on: " + lab_titles([22])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "14:45", 45, "topic", "Topic 6 — Close the Project: acceptance, transition, benefits and lessons learned"),
            ("14:45", "15:45", 60, "lab", "Hands-on: " + lab_titles([23])),
            ("15:45", "16:00", 15, "break", "Tea break"),
            ("16:00", "18:00", 120, "lab", "Hands-on: " + lab_titles([24])),
            ("18:00", "18:30", 30, "recap", "Mock exam debrief, domain score analysis, study plan and course close"),
        ]),
    }


# ------------------------------------------------------------------ deck overview
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="The PMP Exam at a Glance",
    concepts=[
        ("180 questions, 230 minutes",
         "170 scored plus 10 unscored pretest items, with two 10-minute breaks."),
        ("Three domains",
         "People 33%, Process 41%, Business Environment 26% — weighted by the ECO 2026."),
        ("Predictive, agile and hybrid",
         "About 40% predictive; the other 60% splits between adaptive/agile and hybrid."),
        ("Six question formats",
         "Multiple choice and response, matching, enhanced matching, graphic-based and case study."),
        ("Scenario-driven, not recall",
         "Almost every item is a situation asking what you do next, not a definition."),
        ("35 contact hours",
         "This course delivers the 35 hours of project management education PMI requires."),
    ],
    framework_title="The ECO 2026 Domains",
    framework=[
        ("People — 33%", "Lead, align and communicate with the humans on and around the project."),
        ("Process — 41%", "Plan, deliver, measure and close the work itself."),
        ("Business Environment — 26%", "Connect the project to governance, compliance, risk and change."),
    ],
    statement=dict(
        headline="The exam does not ask what you know. It asks what you would do.",
        body="Every lab in this course puts you in a scenario, makes you choose, and "
             "then shows you why the exam would score that choice the way it does.",
        kicker="HOW THIS COURSE WORKS",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("An authorised project", ["Environment scan and governance model",
                                   "Compliance register", "Business case with NPV and BCR",
                                   "Project charter and stakeholder analysis"]),
        ("An integrated plan", ["Requirements traceability matrix", "Prioritised backlog and WBS",
                                "Critical path with PERT estimates",
                                "Cost baseline with reserves and a risk register"]),
        ("A controlled delivery", ["RACI and communication plan", "Kanban flow metrics",
                                   "Earned value analysis and forecasts",
                                   "Root cause analysis and control charts"]),
        ("Exam readiness", ["Closure and benefits realisation", "Consolidated project plan",
                            "Full-format mock exam", "Domain-by-domain score analysis"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Read the scenario and identify which development approach is in play.",
        "Work the technique by hand — the exam gives you no spreadsheet.",
        "Produce the artifact the next lab will consume.",
        "Verify your result against the stated success test.",
        "Connect it to the exam: what would the item stem look like, and what is the tell?",
    ],
)

LAB_SHOTS = {}

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Project Management Professional (PMP) "
    "Exam Prep course. It delivers the 35 contact hours of formal project "
    "management education that PMI requires before you may sit the PMP "
    "examination, and it is aligned to the PMI PMP Examination Content Outline "
    "(ECO) effective July 2026 — People 33%, Process 41%, Business Environment 26%."
)

LG_INTRO2 = (
    "The course is built on a single continuous case study, the Contoso Training "
    "Portal Upgrade. All 24 hands-on labs work that one project from environment "
    "scan through authorisation, planning, delivery, control and closure. Each lab "
    "consumes artifacts produced by earlier labs, so by the capstone you hold a "
    "complete integrated project management plan you built yourself. The project "
    "is deliberately hybrid, because the exam is: roughly 40% of items sit in a "
    "predictive context and the rest split between adaptive/agile and hybrid."
)

LG_SETUP = dict(
    needs=[
        "A laptop with a modern browser (Chrome, Edge, Firefox or Safari).",
        "A spreadsheet application for the estimating, cost and earned value labs.",
        "A folder for your lab artifacts — see the structure in labs/tools.md.",
        "A printed or on-screen copy of the PMI ECO 2026 for reference.",
        "A pen and paper: the exam gives you no spreadsheet, so practise by hand.",
    ],
    verify_text="Confirm your setup before Lab 01: create the artifacts folder and "
                "open one of the live browser tools to check it loads.",
    verify_code="mkdir -p pmp-labs/artifacts && cd pmp-labs",
    conventions=[
        "Placeholders such as <YOUR NAME> are replaced with your own values.",
        "Artifacts are written to artifacts/NN-name.md, numbered by the lab that produced them.",
        "Every lab states what it Consumes and what it Produces — check both before starting.",
        "The live browser tools need no installation, no login, and send no data anywhere.",
        "'Exam tell' boxes flag the cue the PMP examination uses for that concept.",
    ],
)

LAB_NOTE = (
    "The Contoso Training Portal Upgrade is a fictional case study created for "
    "this course. Use only accounts and data you are authorised to use."
)

LG_WRAPUP = dict(
    title="Wrap-Up and Exam Readiness",
    intro="You have worked one project end to end and produced every artifact the "
          "ECO expects a project manager to own. What remains is converting that "
          "into a passing exam performance.",
    sections=[
        dict(title="What you built", bullets=[
            "An environment scan, governance model and compliance register.",
            "A business case, project charter, stakeholder analysis and team charter.",
            "A requirements traceability matrix, prioritised backlog, WBS, critical "
            "path schedule, cost baseline with reserves, and a quantified risk register.",
            "A RACI, communication plan, Kanban flow metrics and an earned value analysis.",
            "A root cause analysis, control chart, closure pack and benefits realisation review.",
        ]),
        dict(title="Applying for the exam", bullets=[
            "This course provides the 35 contact hours of project management education PMI requires.",
            "Confirm you also meet PMI's experience requirement for your education level.",
            "Submit your application at pmi.org; applications are subject to audit, so keep evidence.",
            "Book your exam only once your practice scores are consistently above target.",
        ]),
        dict(title="Study plan after the course", bullets=[
            "Review your Lab 24 domain score analysis and rank your three weakest ECO tasks.",
            "Work full 180-question timed mocks — stamina is a real exam variable.",
            "Re-derive the EVM formulas by hand until they need no lookup.",
            "For every wrong answer, write why the correct answer is correct; that is the learning.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Complete your PMI membership and PMP application with your 35 contact hours.",
    "Schedule a full timed mock exam within two weeks while the material is fresh.",
    "Re-run Labs 12, 13 and 20 without the guide to confirm the calculations are automatic.",
    "Join a study group or PMI chapter to keep exposure to scenario discussion.",
    "Plan your PDU strategy early — the PMP requires 60 PDUs every three years to maintain.",
]

LG_GLOSSARY = [
    ("Adaptive approach", "A development approach delivering in short iterations with "
                          "evolving requirements; agile is an adaptive approach."),
    ("Assumption log", "The record of what is believed true without proof, with an owner "
                       "and a validation date; unvalidated assumptions become risks."),
    ("BAC — Budget at Completion", "The total authorised cost baseline for the project work."),
    ("Benefits realisation", "The measurement, after delivery, of whether the business "
                             "case benefits actually materialised."),
    ("Contingency reserve", "Budget held for identified risks (known unknowns); inside "
                            "the cost baseline and controlled by the project manager."),
    ("CPI — Cost Performance Index", "EV divided by AC. Below 1.0 means the work cost more than planned."),
    ("Critical path", "The longest sequence of dependent activities, determining the "
                      "shortest possible project duration; activities on it have zero float."),
    ("EAC — Estimate at Completion", "The forecast total cost of the project given performance to date."),
    ("EEF — Enterprise Environmental Factor", "A condition outside the team's control "
                                              "that constrains the project; you conform to EEFs."),
    ("EMV — Expected Monetary Value", "Probability multiplied by impact, used to compare "
                                      "risk responses and decision-tree branches."),
    ("EV — Earned Value", "The budgeted value of the work actually completed."),
    ("Float (slack)", "The time an activity can slip without delaying the project finish."),
    ("Hybrid approach", "A deliberate combination of predictive governance with adaptive delivery."),
    ("Kano model", "A prioritisation model classifying features as basic, performance or delighter."),
    ("Lead time / cycle time", "Lead time is request to delivery; cycle time is work start "
                               "to delivery — flow metrics that expose bottlenecks."),
    ("Management reserve", "Budget held for unknown unknowns; outside the cost baseline "
                           "and released only by management."),
    ("MoSCoW", "Prioritisation into Must have, Should have, Could have and Won't have."),
    ("OPA — Organisational Process Asset", "A reusable plan, process, template or lesson "
                                           "from prior work; you apply OPAs and then update them."),
    ("PERT", "Three-point estimating: (Optimistic + 4 × Most Likely + Pessimistic) ÷ 6."),
    ("Predictive approach", "A development approach where scope, schedule and cost are "
                            "defined early and changed through formal change control."),
    ("Project charter", "The document issued by the sponsor that authorises the project "
                        "and names the project manager's authority."),
    ("RACI", "A responsibility assignment matrix: Responsible, Accountable, Consulted, "
             "Informed — exactly one Accountable per work package."),
    ("Risk register", "The record of identified risks with probability, impact, owned "
                      "responses and residual risk."),
    ("RTM — Requirements Traceability Matrix", "The linkage from business need through "
                                               "requirement to deliverable and test."),
    ("Salience model", "Stakeholder classification by power, urgency and legitimacy."),
    ("SPC — Statistical Process Control", "Control charts separating assignable causes "
                                          "from common-cause variation."),
    ("SPI — Schedule Performance Index", "EV divided by PV. Below 1.0 means work is behind schedule."),
    ("Tuckman model", "Team development stages: forming, storming, norming, performing, adjourning."),
    ("WBS — Work Breakdown Structure", "The hierarchical decomposition of total scope "
                                       "into deliverables and work packages."),
    ("WIP limit", "A cap on work in progress that forces finishing over starting."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE,
     "Initial release of the PMP Exam Prep courseware: six topics aligned to the "
     "PMI ECO 2026, 24 hands-on labs on a single continuous case study, and a "
     "four-day schedule of 32 instructional hours with a full-format mock exam.",
     TRAINER),
]
