"""
SINGLE SOURCE OF TRUTH for the PMP Exam Prep (C523) courseware.

Every artifact (PPT, Lesson Plan, Learner Guide, labs) reads
from this module so they cannot drift apart.

Content is aligned to the PMI PMP Examination Content Outline (ECO),
July 2026 update:  People 33% / Process 41% / Business Environment 26%.
"""

# ------------------------------------------------------------------ course
COURSE_TITLE = "Project Management Professional (PMP) Exam Prep"
COURSE_CODE = "C523"
TRAINER = "Dr. Alfred Ang"
VERSION = "v2.0"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "201200696W"
DAYS = 4
HOURS_PER_DAY = 8


LEARNING_OUTCOMES = [
    ("LO1", "Scope medium-scale project requirements to drive timely completions."),
    ("LO2", "Develop project plans based on realistic timelines and resource allocations."),
    ("LO3", "Implement methodologies effectively to address project exigencies and "
            "derive solutions from identified root causes."),
    ("LO4", "Analyze program risks and engage stakeholders through scheduled "
            "touchpoints to discuss potential issues."),
    ("LO5", "Coordinate project deliverables against set objectives, costs, and "
            "timelines, and implement corrective actions."),
]

# ------------------------------------------------------- ECO 2026 reference
ECO_DOMAINS = [
    ("I", "People", 33, "How you lead, align and communicate with the humans on and "
                        "around the project."),
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

# ECO tasks, keyed by domain. (task_no, statement, [enablers])
ECO_TASKS = {
    "People": [
        (1, "Develop a common vision", [
            "Help ensure a shared vision with key stakeholders",
            "Promote the shared vision",
            "Keep the vision current",
            "Break down situations to identify the root cause of a misunderstanding of the vision",
        ]),
        (2, "Manage conflicts", [
            "Identify conflict sources",
            "Analyze the context for the conflict",
            "Implement an agreed-on resolution strategy",
            "Communicate conflict management principles with the team and external stakeholders",
            "Establish an environment that fosters adherence to common ground rules",
            "Manage and rectify ground rule violations",
        ]),
        (3, "Lead the project team", [
            "Establish expectations at the team level",
            "Empower the team",
            "Solve problems",
            "Represent the voice of the team",
            "Support the team's varied experiences, skills, and perspectives",
            "Determine an appropriate leadership style",
            "Establish clear roles and responsibilities within the team",
        ]),
        (4, "Engage stakeholders", [
            "Identify stakeholders",
            "Analyze stakeholders",
            "Analyze and tailor communication to stakeholder needs",
            "Execute the stakeholder engagement plan",
            "Optimize alignment among stakeholder needs, expectations, and project objectives",
            "Build trust and influence stakeholders to accomplish project objectives",
        ]),
        (5, "Align stakeholder expectations", [
            "Categorize stakeholders",
            "Identify stakeholder expectations",
            "Facilitate discussions to align expectations",
            "Organize and act on mentoring opportunities",
        ]),
        (6, "Manage stakeholder expectations", [
            "Identify internal and external customer expectations",
            "Align and maintain outcomes to internal and external customer expectations",
            "Monitor internal and external customer satisfaction/expectations and respond as needed",
        ]),
        (7, "Help ensure knowledge transfer", [
            "Identify knowledge critical to the project",
            "Gather knowledge",
            "Foster an environment for knowledge transfer",
        ]),
        (8, "Plan and manage communication", [
            "Define a communication strategy",
            "Promote transparency and collaboration",
            "Establish a feedback loop",
            "Understand reporting requirements",
            "Create reports aligned with sponsors and stakeholder expectations",
            "Support reporting and governance processes",
        ]),
    ],
    "Process": [
        (1, "Develop an integrated project management plan and plan delivery", [
            "Assess project needs, complexity, and magnitude",
            "Recommend a development approach (predictive, adaptive/agile, or hybrid)",
            "Determine critical information requirements (e.g., sustainability)",
            "Recommend a project execution strategy",
            "Create an integrated project management plan",
            "Estimate work effort and resource requirements",
            "Assess consolidated plans for dependencies, gaps, and continued business value",
            "Maintain the integrated project management plan",
            "Collect and analyze data to make informed project decisions",
        ]),
        (2, "Develop and manage project scope", [
            "Define scope",
            "Obtain stakeholder agreement on project scope",
            "Break down scope",
        ]),
        (3, "Help ensure value-based delivery", [
            "Identify value components with key stakeholders",
            "Prioritize work based on value and stakeholder feedback",
            "Assess opportunities to deliver value incrementally",
            "Examine the business value throughout the project",
            "Verify a measurement system is in place to track benefits",
            "Evaluate delivery options to demonstrate value",
        ]),
        (4, "Plan and manage resources", [
            "Define and plan resources based on requirements",
            "Manage and optimize resource needs and availability",
        ]),
        (5, "Plan and manage procurement", [
            "Plan procurement",
            "Execute a procurement management plan",
            "Select preferred contract types",
            "Evaluate vendor performance",
            "Verify objectives of the procurement agreement are met",
            "Participate in agreement negotiations",
            "Determine a negotiation strategy",
            "Manage suppliers and contracts",
            "Plan and manage the procurement strategy",
            "Develop a delivery solution",
        ]),
        (6, "Plan and manage finance", [
            "Analyze project financial needs",
            "Quantify risk and contingency financial allocations",
            "Plan spend tracking throughout the project life cycle",
            "Plan financial reporting",
            "Anticipate future finance challenges",
            "Monitor financial variations and work with the governance process",
            "Manage financial reserves",
        ]),
        (7, "Plan and optimize quality of products/deliverables", [
            "Gather quality requirements for project deliverables",
            "Plan quality processes and tools",
            "Execute a quality management plan",
            "Help ensure regulatory compliance",
            "Manage cost of quality (CoQ) and sustainability",
            "Conduct ongoing quality reviews",
            "Implement continuous improvement",
        ]),
        (8, "Plan and manage schedule", [
            "Prepare a schedule based on the selected development approach",
            "Coordinate with other projects and operations",
            "Estimate project tasks (milestones, dependencies, story points)",
            "Utilize benchmarks and historical data",
            "Create a project schedule",
            "Baseline a project schedule",
            "Execute a schedule management plan",
            "Analyze schedule variation",
        ]),
        (9, "Evaluate project status", [
            "Develop project metrics, analysis, and reconciliation",
            "Identify and tailor needed artifacts",
            "Help ensure artifacts are created, reviewed, updated, and documented",
            "Help ensure accessibility of artifacts",
            "Assess current progress",
            "Measure, analyze, and update project metrics",
            "Communicate project status",
            "Continually assess the effectiveness of artifact management",
        ]),
        (10, "Manage project closure", [
            "Obtain project stakeholder approval of project completion",
            "Determine criteria to successfully close the project or phase",
            "Validate readiness for transition (e.g., to operations or next phase)",
            "Conclude closure activities (lessons learned, retrospectives, procurement, "
            "financials, resources)",
        ]),
    ],
    "Business Environment": [
        (1, "Define and establish project governance", [
            "Establish structure, rules, procedures, reporting, ethics and policies using OPAs",
            "Define success metrics",
            "Outline governance escalation paths and thresholds",
        ]),
        (2, "Plan and manage project compliance", [
            "Confirm compliance requirements (security, health and safety, sustainability, regulatory)",
            "Classify compliance categories",
            "Determine potential threats to compliance",
            "Use methods to support compliance",
            "Analyze the consequences of noncompliance",
            "Determine the approach and actions to address compliance needs",
            "Measure the extent to which the project is in compliance",
        ]),
        (3, "Manage and control changes", [
            "Execute the change control process",
            "Communicate the status of proposed changes",
            "Implement approved changes to the project",
            "Update project documentation to reflect changes",
        ]),
        (4, "Remove impediments and manage issues", [
            "Evaluate the impact of impediments",
            "Prioritize and highlight impediments",
            "Determine and apply an intervention strategy to remove/minimize impediments",
            "Reassess continually to ensure blockers are being addressed",
            "Recognize when a risk becomes an issue",
            "Collaborate with relevant stakeholders on an approach to resolve issues",
        ]),
        (5, "Plan and manage risk", [
            "Identify risks",
            "Analyze risks",
            "Monitor and control risks",
            "Develop a risk management plan",
            "Maintain a risk register (e.g., poor IT security)",
            "Execute a risk management plan (risk response for security and sustainability risks)",
            "Communicate the status of a risk impact on the project",
        ]),
        (6, "Continuous improvement", [
            "Utilize lessons learned",
            "Help ensure continuous improvement processes are updated",
            "Update organizational process assets (OPAs)",
        ]),
        (7, "Support organizational change", [
            "Assess organizational culture",
            "Evaluate the impact of organizational change on the project and determine actions",
        ]),
        (8, "Evaluate external business environment changes", [
            "Survey changes to the external business environment (regulations, technology, "
            "geopolitical, market)",
            "Assess and prioritize impact on project scope/backlog",
            "Continually review the external business environment for impacts",
        ]),
    ],
}


def eco(domain, task_no):
    """Return a short on-slide ECO tag, e.g. 'ECO People T2 · Manage conflicts'."""
    short = {"People": "People", "Process": "Process",
             "Business Environment": "Business Env"}[domain]
    for no, stmt, _ in ECO_TASKS[domain]:
        if no == task_no:
            return f"ECO {short} T{no} · {stmt}"
    raise KeyError(f"{domain} T{task_no}")


# ------------------------------------------------------- topics -> ECO map
# Each topic declares which ECO tasks it delivers, so coverage is provable.
TOPICS = [
    (1, "Business Environment",
     "Where projects come from, why they are funded, and the governance, "
     "compliance and change context they must survive in.",
     [("Business Environment", 1), ("Business Environment", 2),
      ("Business Environment", 7), ("Business Environment", 8),
      ("Process", 3)],
     ["Foundation and project fundamentals",
      "Strategic alignment and business value",
      "Development approaches: predictive, agile, hybrid",
      "Organisational culture and change management",
      "Project governance and escalation",
      "Compliance, sustainability and AI in projects"]),

    (2, "Start the Project",
     "Turning an idea into an authorised project: the business case, the "
     "charter, the stakeholders and the team.",
     [("People", 1), ("People", 4), ("People", 5), ("People", 6),
      ("Process", 1)],
     ["Project integration and the charter",
      "Business case, cost-benefit and benefits management",
      "Identify, analyse and prioritise stakeholders",
      "Align and manage stakeholder expectations",
      "Form the team and build shared understanding",
      "Determine the project approach"]),

    (3, "Plan the Project",
     "Building the integrated plan — scope, schedule, cost, quality, "
     "resources, communications, risk and procurement.",
     [("Process", 1), ("Process", 2), ("Process", 4), ("Process", 5),
      ("Process", 6), ("Process", 7), ("Process", 8),
      ("Business Environment", 5), ("People", 8)],
     ["The integrated project management plan",
      "Scope: requirements, WBS and baselines",
      "Schedule: activities, dependencies, critical path",
      "Cost: estimating, budget and reserves",
      "Quality: planning and problem-solving tools",
      "Resources, communications and procurement",
      "Risk: identification, analysis and response"]),

    (4, "Lead the Project Team",
     "The People domain in practice — leadership style, motivation, "
     "conflict, coaching and communication.",
     [("People", 1), ("People", 2), ("People", 3), ("People", 7),
      ("People", 8), ("Process", 1)],
     ["Direct and manage project work",
      "Craft your leadership skills",
      "Build a collaborative team environment",
      "Empower the team and support performance",
      "Training, coaching and mentoring",
      "Manage conflict and negotiate"]),

    (5, "Monitor and Control the Project",
     "Measuring truth against plan: earned value, quality control, change "
     "control, issues and impediments.",
     [("Process", 9), ("Business Environment", 3),
      ("Business Environment", 4), ("Business Environment", 5),
      ("Business Environment", 6), ("Process", 7)],
     ["Monitor and control project work",
      "Evaluate project progress and earned value",
      "Control quality with statistical tools",
      "Manage changes and integrated change control",
      "Manage issues, impediments and risk",
      "Implement ongoing improvements"]),

    (6, "Close the Project",
     "Landing the project: acceptance, transition, benefits realisation and "
     "the knowledge that outlives the team.",
     [("Process", 10), ("Business Environment", 6), ("People", 7)],
     ["Project and phase closure",
      "Benefits realisation and value confirmation",
      "Knowledge transfer and lessons learned",
      "PMP exam strategy and readiness"]),
]

# -------------------------------------------------------------- day plan
DAY_PLAN = [
    (1, "Business Environment & Starting the Project", [1, 2], "Labs 01-08"),
    (2, "Planning the Project", [3], "Labs 09-14"),
    (3, "Leading the Team & Controlling Delivery", [4, 5], "Labs 15-22"),
    (4, "Closing, Exam Strategy & Practice", [6], "Labs 23-24 + practice exam"),
]

# --------------------------------------------------- problem-solving tools
# Live browser tools from the AI-LMS-TMS trainer toolset.
TOOLS = {
    "5whys": ("5 Whys", "https://alfredang.github.io/5whys/",
              "Drill from a symptom to its root cause by asking 'why' five times."),
    "fishbone": ("Fishbone Diagram", "https://alfredang.github.io/fishbone/",
                 "Group candidate causes into categories around a problem statement."),
    "pareto": ("Pareto Chart", "https://alfredang.github.io/paretochart/",
               "Rank defect categories to find the vital few driving most of the pain."),
    "systemloop": ("System Thinking", "https://alfredang.github.io/systemloop/",
                   "Map reinforcing and balancing loops behind a recurring problem."),
    "spc": ("SPC / Control Chart", "https://alfredang.github.io/novaspc/",
            "Plot a process over time against control limits to separate signal from noise."),
    "stats": ("Statistics", "https://alfredang.github.io/novastats/",
              "Descriptive statistics, distributions and hypothesis testing on project data."),
    "raci": ("RACI Matrix", "https://alfredang.github.io/raci/",
             "Assign Responsible, Accountable, Consulted and Informed per work package."),
    "kanban": ("Kanban Board", "https://alfredang.github.io/kanban/",
               "Visualise work in progress, limit WIP and expose bottlenecks."),
    "scrum": ("Scrum Simulator", "https://alfredang.github.io/scrum/",
              "Run sprint planning, review and retrospective mechanics."),
    "mindmap": ("Mind Mapping", "https://alfredang.github.io/mindmapping/",
                "Expand a central idea into branches for requirements discovery."),
    "designthinking": ("Design Thinking", "https://alfredang.github.io/designthinking/",
                       "Empathise, define, ideate, prototype and test a solution."),
    "pivot": ("Pivot Analysis", "https://alfredang.github.io/novapivot/",
              "Slice project data by dimension to expose trends and outliers."),
}


# ------------------------------------------------------ non-WSQ additions
SHORT_TITLE  = "PMP-Exam-Prep"
VERSION_DATE = "20 July 2026"
MODE         = "Instructor-led, hands-on practical labs"

VERSION_HISTORY = [
    ("1.0", "20 July 2026",
     "Initial release of the PMP Exam Prep courseware.", TRAINER),
    ("2.0", VERSION_DATE,
     "Full-depth build: the deck now carries the complete ECO 2026 teaching "
     "content across all six topics (536 slides), with per-topic concept, "
     "process, formula, ITTO and exam-focus slides. Day 4 afternoon is given "
     "over to the capstone lab and the self-scored mock practice exam.",
     TRAINER),
]
