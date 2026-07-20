"""Topic 4 — Lead the Project Team."""
import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

P1 = cd.eco("People", 1)
P2 = cd.eco("People", 2)
P3 = cd.eco("People", 3)
P7 = cd.eco("People", 7)
P8 = cd.eco("People", 8)
PR1 = cd.eco("Process", 1)


def build(prs, n):
    """Render Topic 4. `n` is the running slide number. Return the next number."""

    # ---------------------------------------------------------- 1. opening
    X.section(prs, 4, "Lead the Project Team",
              "The People domain in practice. Execution is where the plan meets "
              "human beings — this topic covers how you direct the work, grow the "
              "team, resolve conflict and communicate so the plan actually lands.",
              ["Direct and manage project work, artifacts and knowledge",
               "Develop the team: Tuckman, motivation and team-building",
               "Craft your leadership style and emotional intelligence",
               "Train, coach and mentor to close capability gaps",
               "Manage conflict, decisions and negotiation",
               "Plan and manage communication across a distributed team"],
              n); n += 1

    X.statement(prs, "Why this topic carries the most exam weight",
                "Plans do not deliver projects. People do.",
                [("33% of the exam", "The People domain is the single largest "
                  "cluster of ECO tasks and is tested across every question type."),
                 ("Situational questions", "Most People items are scenario-based: "
                  "you pick the PM's next action, not a definition."),
                 ("Servant-leader default", "PMI expects you to facilitate, coach "
                  "and empower before you ever direct or escalate.")],
                n, kicker=P3, accent=VIOLET); n += 1

    X.cards(prs, "What 'leading the project team' actually means",
            [("Set expectations", "Agree what good looks like at team level — "
              "quality bars, response times, definition of done, escalation rules."),
             ("Empower decisions", "Push authority to the level closest to the work "
              "so the team decides without waiting on the project manager."),
             ("Solve problems", "Break impediments down to root cause, then remove "
              "them or escalate with a recommended option, never just a complaint."),
             ("Represent the voice of the team", "Carry the team's constraints, "
              "capacity and concerns upward to sponsors honestly and without filter."),
             ("Support varied experience", "Deliberately use the differing skills, "
              "cultures and perspectives on the team as a design advantage."),
             ("Clarify roles", "Every work package has one accountable owner; "
              "ambiguity about ownership is the number-one source of team conflict.")],
            n, kicker=P3, accent=TEAL); n += 1

    # ------------------------------------------------ 2. direct & manage work
    X.itto(prs, "Direct and Manage Project Work",
           ["Project management plan (all components)",
            "Project documents: change log, lessons learned register, "
            "milestone list, project communications",
            "Approved change requests",
            "Enterprise environmental factors",
            "Organizational process assets"],
           ["Expert judgment",
            "Project management information system (PMIS)",
            "Meetings: kick-off, stand-up, status review",
            "Interpersonal and team skills",
            "Data and decision-making techniques"],
           ["Deliverables",
            "Work performance data",
            "Issue log",
            "Change requests",
            "Project management plan updates",
            "Project document updates and OPA updates"],
           n, kicker=PR1,
           purpose="Executing process: lead and perform the work defined in the "
                   "plan and implement approved changes to achieve the objectives."); n += 1

    X.process(prs, "Data becomes information becomes reports",
              [("Work performance data", "Raw observations from the work: actual "
                "cost, defect counts, hours logged, change requests raised."),
               ("Work performance information", "Data compared against baselines or "
                "each other — schedule variance, CPI, % of packages complete."),
               ("Work performance reports", "Physical or electronic packaging of "
                "that information — dashboards, status reports, briefings."),
               ("Decisions and action", "Reports raise awareness, generate "
                "decisions and trigger change requests or corrective action.")],
              n, kicker=PR1, accent=BLUE,
              note="Exam cue: data is produced by Direct and Manage Project Work; "
                   "information by the Control processes; reports by Monitor and "
                   "Control Project Work. The verb in the stem tells you which."); n += 1

    X.exam(prs, "Data, information or report?",
           [("'The team logs 14 defects this sprint' — what is this?",
             "Work performance data. Raw, unprocessed measurement straight from "
             "the work itself."),
            ("'Defect rate is 40% above the baseline' — what is this?",
             "Work performance information. Data has been compared to a baseline "
             "and now carries meaning."),
            ("'The sponsor asks for the monthly status pack' — what is this?",
             "A work performance report — the communication artifact built from "
             "work performance information."),
            ("Question asks where deliverables are produced",
             "Direct and Manage Project Work. Deliverables are its primary output; "
             "verified deliverables come later from Control Quality.")],
           n, accent=ROSE); n += 1

    X.cards(prs, "Standardise your project artifacts",
            [("Simple production route", "One agreed way to create a document so "
              "the team spends effort on content rather than on formatting."),
             ("Templates and formats", "Standard formats for status reports, change "
              "requests and minutes make information comparable across periods."),
             ("Review and approval", "A defined path for who drafts, who reviews and "
              "who signs off before an artifact becomes authoritative."),
             ("Version control", "Every artifact carries a version number so people "
              "can tell instantly whether they hold the current truth."),
             ("Security and access", "Classify artifacts and restrict who can edit "
              "versus who can only read, especially for contracts and HR data."),
             ("Timely distribution", "An artifact that arrives after the decision "
              "has been taken has zero value regardless of its quality.")],
            n, kicker=cd.eco("Process", 9), accent=AMBER); n += 1

    X.compare(prs, "Configuration management plan vs configuration management system",
              ("Configuration management plan",
               "A component of the project management plan",
               ["States which items are placed under configuration control",
                "Defines how project and product information is recorded",
                "Says who may request, review and approve a configuration change",
                "Facilitates consistency of the product, service or result",
                "Written during planning; maintained across the whole life cycle"]),
              ("Configuration management system",
               "The tooling and procedures that enforce the plan",
               ["How the PM tracks project artifacts day to day",
                "Monitors and controls changes to baselined items",
                "Holds the audit trail of what changed, when and by whom",
                "Usually a subsystem of the wider PMIS",
                "Includes document control and version control mechanisms"]),
              n, kicker=cd.eco("Business Environment", 3), lc=VIOLET, rc=TEAL,
              footer_note="Configuration management controls the PRODUCT; change "
                          "control controls the PLAN. Exam items often test that "
                          "distinction directly."); n += 1

    X.cards(prs, "Version control and document control in practice",
            [("A subset of configuration management", "Document control is the part "
              "of configuration management dealing with documents and digital records."),
             ("New version number", "Increment on every substantive change so two "
              "people can confirm they are debating the same content."),
             ("Date and time stamp", "Establishes sequence when several edits land "
              "on the same working day from different contributors."),
             ("Author of the change", "Names the person accountable, which makes it "
              "possible to go back and ask why a change was made."),
             ("Change summary line", "One sentence describing what moved lets a "
              "reader decide whether they need to re-read the whole document."),
             ("Single source of truth", "Only one location is authoritative; all "
              "other copies are explicitly labelled as reference copies.")],
            n, kicker=cd.eco("Process", 9), accent=CYAN); n += 1

    X.compare(prs, "Work information management systems",
              ("Project Management Information System (PMIS)",
               "Gathers, integrates and shares project data",
               ["Automated collection of schedule, cost and resource data",
                "Ensures consistency in how data is collected and reported",
                "Feeds dashboards, earned value and status reporting",
                "Includes scheduling tools, work authorisation and configuration systems",
                "An input to almost every executing and controlling process"]),
              ("Artifact management systems",
               "Store and maintain the project's documents",
               ["Repository for plans, registers, logs and specifications",
                "Enforces access rights, retention and version history",
                "Makes artifacts findable — accessibility is an ECO enabler",
                "Supports handover of records at project or phase closure",
                "Continually assessed for effectiveness, per ECO Process T9"]),
              n, kicker=cd.eco("Process", 9), lc=BLUE, rc=AMBER,
              footer_note="ECO Process T9 asks you to 'continually assess the "
                          "effectiveness of artifact management' — a new emphasis "
                          "in the 2026 outline."); n += 1

    # ---------------------------------------------------- 3. manage knowledge
    X.itto(prs, "Manage Project Knowledge",
           ["Project management plan (all components)",
            "Project documents: lessons learned register, project team "
            "assignments, resource breakdown structure, stakeholder register",
            "Deliverables",
            "Enterprise environmental factors",
            "Organizational process assets"],
           ["Expert judgment",
            "Knowledge management (networking, communities of practice, "
            "work shadowing, seminars, storytelling)",
            "Information management (lessons learned register, library "
            "services, information gathering)",
            "Interpersonal and team skills: active listening, "
            "facilitation, leadership, networking, political awareness"],
           ["Lessons learned register",
            "Project management plan updates",
            "Organizational process assets updates"],
           n, kicker=P7,
           purpose="Use existing knowledge and create new knowledge to achieve "
                   "the project's objectives and contribute to organisational learning."); n += 1

    X.compare(prs, "Explicit vs tacit knowledge",
              ("Explicit knowledge",
               "Codified — it can be written down and sent",
               ["Facts, numbers, procedures, diagrams, templates",
                "Easily stored in a repository and searched later",
                "Transferred by documents, training material and databases",
                "Risk: people assume that documenting equals transferring",
                "Managed mainly through information management techniques"]),
              ("Tacit knowledge",
               "Personal — beliefs, insight, experience, know-how",
               ["Judgement, context, 'why we did it that way', relationships",
                "Hard to articulate; often the person does not know they hold it",
                "Transferred by conversation, shadowing, pairing and storytelling",
                "Lost permanently when a key person leaves without handover",
                "Managed mainly through knowledge management techniques"]),
              n, kicker=P7, lc=TEAL, rc=VIOLET,
              footer_note="The hardest part of knowledge management is creating an "
                          "atmosphere of trust so people are willing to share the "
                          "tacit knowledge that makes them individually valuable."); n += 1

    X.cards(prs, "Information radiators",
            [("Big visible charts", "Large, low-tech displays placed where the team "
              "works so status is absorbed passively rather than requested."),
             ("Task or Kanban board", "Shows every work item and its state; makes "
              "work-in-progress and bottlenecks obvious without a status meeting."),
             ("Burndown / burnup chart", "Plots remaining or completed work against "
              "time so the team sees its own trend against the commitment."),
             ("Impediment board", "Lists blockers, owner and age — an ageing blocker "
              "on a public wall creates the pressure to resolve it."),
             ("Team calendar and capacity", "Absences, holidays and shared "
              "commitments visible so the team plans realistically together."),
             ("Radiate, don't report", "Radiators push information out continuously; "
              "reports pull it out periodically and are always slightly stale.")],
            n, kicker=P8, accent=CYAN); n += 1

    X.cards(prs, "The lessons learned register",
            [("Created early, not at the end", "Opened during Manage Project "
              "Knowledge in the first phase and updated throughout execution."),
             ("What it records", "The situation, what was done, the impact, and the "
              "recommendation for anyone facing that situation again."),
             ("Categories", "Lessons on requirements, estimating, risk, "
              "procurement, communication, quality and team dynamics."),
             ("Feeds later phases", "A live register lets the current project fix "
              "itself, not just help the next project."),
             ("Becomes the repository", "At closure the register is folded into the "
              "organisational lessons learned repository, an OPA."),
             ("Retrospectives supply it", "In adaptive work every iteration "
              "retrospective is a scheduled input to the register.")],
            n, kicker=P7, accent=AMBER); n += 1

    X.cards(prs, "Foster a knowledge-sharing culture",
            [("Everyone teaches and learns", "Knowledge transfer is not a one-way "
              "flow from senior to junior; every role holds transferable know-how."),
             ("Include stakeholders and customers", "Suppliers, users and operations "
              "staff hold context the delivery team cannot generate on its own."),
             ("Dedicated sharing roles", "Agile coaches and Scrum Masters exist "
              "partly to make knowledge move across team boundaries."),
             ("Essential at transition", "Product handover to operations fails when "
              "only explicit knowledge crosses and tacit knowledge does not."),
             ("Communities of practice", "Cross-project guilds keep specialists "
              "connected so a solution found once is not re-invented."),
             ("Psychological safety first", "People share what went wrong only when "
              "they are confident the disclosure will not be used against them.")],
            n, kicker=P7, accent=TEAL); n += 1

    # ------------------------------------------- 4. execution of other domains
    X.itto(prs, "Manage Stakeholder Engagement",
           ["Project management plan: communications, stakeholder "
            "engagement, risk and change management plans",
            "Project documents: change log, issue log, lessons learned "
            "register, stakeholder register",
            "Enterprise environmental factors",
            "Organizational process assets"],
           ["Expert judgment",
            "Communication skills: feedback",
            "Interpersonal and team skills: conflict management, cultural "
            "awareness, negotiation, observation/conversation, political awareness",
            "Ground rules",
            "Meetings"],
           ["Change requests",
            "Project management plan updates",
            "Project document updates: change log, issue log, lessons "
            "learned register, stakeholder register"],
           n, kicker=cd.eco("People", 4),
           purpose="Communicate and work with stakeholders to meet their needs, "
                   "address issues and foster appropriate engagement."); n += 1

    X.itto(prs, "Manage Quality",
           ["Project management plan: quality management plan",
            "Project documents: lessons learned register, quality control "
            "measurements, quality metrics, risk report",
            "Organizational process assets"],
           ["Data gathering: checklists",
            "Data analysis: alternatives analysis, document analysis, "
            "process analysis, root cause analysis",
            "Decision making: multicriteria decision analysis",
            "Data representation: affinity diagrams, cause-and-effect "
            "diagrams, flowcharts, histograms, matrix diagrams, scatter diagrams",
            "Audits, design for X, problem solving, quality improvement methods"],
           ["Quality reports",
            "Test and evaluation documents",
            "Change requests",
            "Project management plan updates",
            "Project document updates"],
           n, kicker=cd.eco("Process", 7),
           purpose="Translate the quality management plan into executable quality "
                   "activities — this is quality ASSURANCE, about the process."); n += 1

    X.compare(prs, "Manage Quality vs Control Quality",
              ("Manage Quality (Executing)",
               "Are we using the right process?",
               ["Quality assurance — audits the process, not the product",
                "Outputs quality reports and test/evaluation documents",
                "Uses process analysis and root cause analysis",
                "Drives continuous improvement of how work is done",
                "Owned by the PM, quality department and often the whole team"]),
              ("Control Quality (Monitoring & Controlling)",
               "Did we build the right thing correctly?",
               ["Inspects deliverables against acceptance criteria",
                "Outputs quality control measurements and verified deliverables",
                "Uses inspection, testing, control charts and checksheets",
                "Determines correctness of the output, one deliverable at a time",
                "Feeds verified deliverables into Validate Scope for acceptance"]),
              n, kicker=cd.eco("Process", 7), lc=VIOLET, rc=BLUE,
              footer_note="Mnemonic: Manage Quality is about the PROCESS and "
                          "prevention; Control Quality is about the PRODUCT and "
                          "inspection."); n += 1

    X.itto(prs, "Acquire Resources",
           ["Project management plan: resource management plan, "
            "procurement management plan, cost baseline",
            "Project documents: project schedule, resource calendars, "
            "resource requirements, stakeholder register",
            "Enterprise environmental factors",
            "Organizational process assets"],
           ["Decision making: multicriteria decision analysis",
            "Interpersonal and team skills: negotiation",
            "Pre-assignment",
            "Virtual teams"],
           ["Physical resource assignments",
            "Project team assignments",
            "Resource calendars",
            "Change requests",
            "Project management plan updates",
            "Project document updates and EEF/OPA updates"],
           n, kicker=cd.eco("Process", 4),
           purpose="Obtain team members, facilities, equipment, materials and "
                   "supplies necessary to complete the project work."); n += 1

    X.table(prs, "Four ways you obtain project resources",
            ["Route", "How it works", "When to use it", "Watch out for"],
            [["Pre-assignment",
              "People are named in the charter or promised in the proposal",
              "Competitive bids won on named experts; unique specialists",
              "The named person may no longer be available when you start"],
             ["Negotiation",
              "You bargain with functional managers, other PMs or the PMO",
              "Matrix organisations where resources are shared",
              "You win only what your influence and the project's priority allow"],
             ["Acquisition",
              "Hire externally or contract in the skill from a supplier",
              "The skill genuinely does not exist inside the organisation",
              "Cost, lead time, onboarding and knowledge leaving at contract end"],
             ["Virtual teams",
              "People contribute from different locations or time zones",
              "Scarce skills, remote workers, cost or mobility constraints",
              "Isolation, communication lag, weaker informal knowledge flow"]],
            n, kicker=cd.eco("Process", 4), accent=TEAL,
            widths=[1.1, 1.6, 1.6, 1.7],
            note="If the question describes a resource you cannot get, negotiate "
                 "first, then escalate to the sponsor — do not simply re-plan the "
                 "schedule around the gap."); n += 1

    X.itto(prs, "Develop Team",
           ["Project management plan: resource management plan",
            "Project documents: lessons learned register, project schedule, "
            "project team assignments, resource calendars, team charter",
            "Enterprise environmental factors",
            "Organizational process assets"],
           ["Colocation",
            "Virtual teams and communication technology",
            "Interpersonal and team skills: conflict management, "
            "influencing, motivation, negotiation, team building",
            "Recognition and rewards",
            "Training, individual and team assessments, meetings"],
           ["Team performance assessments",
            "Change requests",
            "Project management plan updates",
            "Project document updates",
            "Enterprise environmental factors updates",
            "Organizational process assets updates"],
           n, kicker=P3,
           purpose="Improve competencies, team member interaction and the overall "
                   "team environment to enhance project performance."); n += 1

    X.statement(prs, "Develop Team in one line",
                "An effective team is the deliverable behind every deliverable.",
                [("Cohesion", "Solidarity and mutual reliance measurably raise "
                  "throughput and lower defect rates."),
                 ("Bonding needs leadership", "Teams do not gel by accident; the "
                  "leader engineers the conditions that let it happen."),
                 ("Team over individual", "Team-building shifts identity from "
                  "'my task is done' to 'our increment is done'.")],
                n, kicker=P3, accent=AMBER); n += 1

    X.cards(prs, "Team-building activities",
            [("Formal", "Facilitated offsites, chartering workshops and structured "
              "team assessments with a defined agenda and outcome."),
             ("Informal", "Five minutes at stand-up, shared meals, coffee "
              "walks — low-cost, high-frequency contact that builds trust."),
             ("Brief", "A short check-in ritual or icebreaker at the start of every "
              "meeting keeps connection alive between bigger events."),
             ("Extended", "Multi-day workshops used at project start or after a "
              "major team change to reset norms and relationships."),
             ("Self-facilitated", "The PM runs it — cheap and fast, but the PM "
              "cannot both facilitate and participate honestly."),
             ("Professionally facilitated", "Neutral facilitator needed when the "
              "PM is part of the problem or the conflict level is high.")],
            n, kicker=P3, accent=VIOLET); n += 1

    # ------------------------------------------------------ 5. Tuckman
    X.timeline(prs, "Tuckman's ladder of team development",
               [("Forming", "Members meet, are polite and still behave as "
                 "individuals; they look to the leader for direction."),
                ("Storming", "Personalities, working styles and role expectations "
                 "collide; productivity dips and conflict surfaces."),
                ("Norming", "The team agrees norms, learns each other's roles and "
                 "settles into a working rhythm."),
                ("Performing", "High trust and interdependence; the team "
                 "self-organises and solves problems without the PM."),
                ("Adjourning", "Work completes, resources release; the team needs "
                 "closure, recognition and knowledge handover.")],
               n, kicker=P3, accent=BLUE,
               note="Teams can regress: a new member, a change of scope or a "
                    "change of PM can drop a performing team back into storming."); n += 1

    X.table(prs, "What the project manager does at each Tuckman stage",
            ["Stage", "What the team looks like", "Your leadership move"],
            [["Forming", "Polite, cautious, dependent, unclear on roles",
              "Be DIRECTIVE — set purpose, roles, ground rules and the team charter"],
             ["Storming", "Disagreement on approach, resistance, low morale",
              "COACH — surface conflict, facilitate, do not suppress the debate"],
             ["Norming", "Norms accepted, trust building, rhythm forming",
              "SUPPORT — let them own decisions, reinforce the norms they set"],
             ["Performing", "Interdependent, self-correcting, high output",
              "DELEGATE — remove impediments, protect the team, stay out of the way"],
             ["Adjourning", "Anxiety about what is next, energy drops",
              "CLOSE — recognise contribution, capture lessons, plan the transition"]],
            n, kicker=P3, accent=TEAL, widths=[0.9, 1.7, 2.2],
            note="Exam pattern: 'the team is arguing about approach' = storming, and "
                 "the best answer is almost always to facilitate the discussion, not "
                 "to decide for them or to reassign someone."); n += 1

    X.chart(prs, "The performance dip you must expect at storming",
            "line",
            ["Forming", "Storming", "Norming", "Performing", "Adjourning"],
            [("Team productivity index", [40, 25, 62, 92, 55]),
             ("Trust / psychological safety", [30, 34, 70, 95, 88])],
            n, kicker=P3, accent=VIOLET,
            insight=["Productivity falls at storming — this is normal, not a sign "
                     "your team is failing.",
                     "Trust keeps rising through storming if conflict is handled "
                     "openly; suppressing it flattens the whole curve.",
                     "Teams left in storming never reach the performing payoff, "
                     "which is where most of the value is created.",
                     "At adjourning output falls but trust stays high — that is "
                     "exactly when knowledge transfer is easiest."],
            ymax=100); n += 1

    X.exam(prs, "Tuckman traps on the exam",
           [("A new member joins a high-performing team",
             "The team regresses toward forming/storming; re-establish roles and "
             "ground rules rather than assuming performance continues."),
            ("Team members openly disagree about the technical approach",
             "This is storming. Facilitate a structured discussion — conflict here "
             "is productive and expected."),
            ("The team resolves issues without involving you",
             "Performing. Your job is removing impediments and shielding the team, "
             "not reasserting control."),
            ("Project ends and the team seems demotivated",
             "Adjourning. Recognise contributions, complete lessons learned and "
             "manage the release/transition of each member.")],
           n, accent=ROSE); n += 1

    # ------------------------------------------------- 6. motivation theories
    X.table(prs, "The motivational theories PMI expects you to know",
            ["Theory", "Core idea", "What it tells a project manager"],
            [["Maslow's hierarchy of needs",
              "Physiological, safety, belonging, esteem, self-actualisation",
              "You cannot motivate with growth opportunities if job security is "
              "in doubt — lower needs dominate first"],
             ["Herzberg's motivation-hygiene",
              "Hygiene factors prevent dissatisfaction; motivators create satisfaction",
              "Fixing salary or the office removes complaints but never creates "
              "engagement — that needs achievement and recognition"],
             ["McGregor's Theory X / Theory Y",
              "X assumes people avoid work; Y assumes people seek responsibility",
              "Your assumption becomes self-fulfilling; Theory Y underpins agile "
              "and servant leadership"],
             ["McClelland's achievement motivation",
              "Achievement, affiliation or power becomes dominant per person",
              "Match the assignment and the reward to the individual's dominant "
              "need, not to your own"],
             ["Vroom's expectancy theory",
              "Motivation = expectancy x instrumentality x valence",
              "If any of the three is zero, motivation is zero — the reward must "
              "be attainable, linked and actually wanted"]],
            n, kicker=P3, accent=AMBER, widths=[1.2, 1.7, 2.1]); n += 1

    X.process(prs, "Maslow's hierarchy of needs",
              [("Physiological", "Pay, rest, food, tolerable working conditions — "
                "nothing else motivates while these are unmet."),
               ("Safety", "Job security, physical and psychological safety, "
                "predictable process and fair treatment."),
               ("Belonging", "Team membership, inclusion, friendship — this is "
                "where team-building does its work."),
               ("Esteem", "Recognition, respect, status, being trusted with "
                "meaningful and visible responsibility."),
               ("Self-actualisation", "Mastery, growth, doing work the person "
                "finds intrinsically worth doing.")],
              n, kicker=P3, accent=BLUE,
              note="Practical read: announcing a restructure destroys the safety "
                   "level, and every motivational lever above it stops working "
                   "until safety is restored."); n += 1

    X.compare(prs, "Herzberg: hygiene factors vs motivators",
              ("Hygiene factors",
               "Their absence causes dissatisfaction; their presence does not motivate",
               ["Salary, benefits and job security",
                "Working conditions and equipment",
                "Company policy and administration",
                "Quality of supervision and interpersonal relations",
                "Fix these to get to neutral — never to get to engaged"]),
              ("Motivators",
               "Their presence creates genuine satisfaction and effort",
               ["Achievement — visibly completing something difficult",
                "Recognition for the work done",
                "The work itself being interesting and meaningful",
                "Responsibility and autonomy over how the work is done",
                "Advancement and personal growth"]),
              n, kicker=P3, lc=ROSE, rc=TEAL,
              footer_note="Exam cue: 'the team got a bonus but morale is still "
                          "low' — you addressed a hygiene factor. Look for a "
                          "motivator such as recognition, autonomy or growth."); n += 1

    X.matrix2x2(prs, "McGregor's Theory X and Theory Y in practice",
                "Assumption about the team",
                "Resulting management style",
                [("Theory X · directive", "Assumes people dislike work and avoid "
                  "responsibility, so supervise closely and control tightly.", ROSE),
                 ("Theory Y · participative", "Assumes people seek responsibility "
                  "and self-direct, so delegate, involve and trust.", TEAL),
                 ("Theory X risk", "Close supervision suppresses initiative and "
                  "confirms the manager's low expectations — a self-fulfilling loop.",
                  AMBER),
                 ("Theory Y risk", "Autonomy without clear expectations becomes "
                  "drift; empowerment still needs boundaries and a definition of done.",
                  VIOLET)],
                n, kicker=P3, accent=VIOLET,
                note="PMI's default posture is Theory Y. Agile, servant leadership "
                     "and self-organising teams all assume Theory Y people."); n += 1

    X.cards(prs, "McClelland's achievement motivation theory",
            [("Need for achievement (nAch)", "Driven by challenging but attainable "
              "goals and concrete feedback; dislikes vague or trivial work."),
             ("Need for affiliation (nAff)", "Driven by belonging and harmony; give "
              "collaborative work and avoid isolating or adversarial roles."),
             ("Need for power (nPow)", "Driven by influence and impact; give "
              "coordination, negotiation and representation responsibilities."),
             ("Shaped by life experience", "One of the three becomes dominant based "
              "on a person's history, not on their job title."),
             ("Use it to design roles", "Craft assignments and rewards around each "
              "member's dominant need rather than a single team-wide incentive."),
             ("Build T-shaped people", "Balance the needs across the team so it can "
              "self-organise instead of depending on one dominant personality.")],
            n, kicker=P3, accent=CYAN); n += 1

    X.formula(prs, "Vroom's expectancy theory",
              [("Motivational force", "M = E x I x V",
                "Motivation is the product of three beliefs — if any one is zero, "
                "the whole motivation is zero."),
               ("Expectancy (E)", "Effort → Performance",
                "'If I work hard, can I actually succeed?' Undermined by unrealistic "
                "targets, missing skills or missing tools."),
               ("Instrumentality (I)", "Performance → Outcome",
                "'If I succeed, will the promised reward really arrive?' Destroyed "
                "by one broken promise."),
               ("Valence (V)", "Value of the outcome",
                "'Do I actually want that reward?' A team dinner has zero valence "
                "for someone who wants a promotion.")],
              n, kicker=P3, accent=AMBER,
              note="Diagnostic use: when motivation is low, test all three terms "
                   "before assuming the problem is the size of the reward."); n += 1

    X.compare(prs, "Two behaviours that quietly destroy your schedule",
              ("Parkinson's Law",
               "Work expands to fill the time allotted to it",
               ["A five-day task given ten days will take ten days",
                "Generous estimates get consumed, never returned as savings",
                "Counter with short timeboxes and fixed iteration lengths",
                "Counter by making remaining work visible on a burndown",
                "Explains why padding every estimate does not create real buffer"]),
              ("Student syndrome",
               "People start only at the last possible moment",
               ["Safety in the estimate is spent at the end, not at the start",
                "Any early problem then hits the deadline with no buffer left",
                "Counter with early checkpoints and definition-of-done gates",
                "Counter by decomposing into small items that finish continuously",
                "Together with Parkinson's Law, the core argument for timeboxing"]),
              n, kicker=cd.eco("Process", 8), lc=AMBER, rc=ROSE,
              footer_note="Critical chain scheduling responds to both by stripping "
                          "individual task padding and pooling it into a shared "
                          "project buffer the PM controls."); n += 1

    # ------------------------------------------------------- 7. leadership
    X.cards(prs, "Servant leadership behaviours",
            [("Listening", "Understand the problem as the team experiences it "
              "before offering your own solution or judgement."),
             ("Helping people grow", "Treat capability building as a deliverable; "
              "grow the team's role capability, not just this project's output."),
             ("Safe to fail", "Make it safe to make mistakes and raise concerns "
              "early, when they are still cheap to fix."),
             ("Coaching, not controlling", "Ask questions that let the team find "
              "the answer instead of issuing the answer yourself."),
             ("Remove impediments", "Your primary daily job: clear the blockers "
              "the team cannot clear from inside the team."),
             ("Pave the way for others", "Promote the energy and intelligence of "
              "others; take the credit last and the blame first.")],
            n, kicker=P3, accent=TEAL); n += 1

    X.table(prs, "Leadership styles you must recognise",
            ["Style", "Behaviour", "Best fit"],
            [["Servant",
              "Focuses on others' growth, learning, autonomy and well-being",
              "Agile and knowledge work; PMI's default posture"],
             ["Laissez-faire",
              "Hands-off; the team makes its own decisions with little input",
              "Highly mature, expert, self-organising teams"],
             ["Transactional",
              "Rewards for meeting goals; manages by exception when things go wrong",
              "Routine, repeatable work with clear measurable targets"],
             ["Transformational",
              "Inspirational motivation, intellectual stimulation, individual attention",
              "Change programmes needing energy and a compelling vision"],
             ["Charismatic",
              "High energy, self-confident, strong convictions, persuasive presence",
              "Rallying stakeholders; risky if it substitutes for substance"],
             ["Interactional",
              "Blend of transactional, transformational and charismatic",
              "Most real projects — deliberately mixed as the situation shifts"],
             ["Directive",
              "Tells people what to do and how; low participation",
              "Crisis, safety incidents, and brand-new teams at forming"]],
            n, kicker=P3, accent=VIOLET, widths=[1.0, 2.2, 1.6]); n += 1

    X.matrix2x2(prs, "Situational leadership: match style to readiness",
                "Task competence of the individual →",
                "Commitment / confidence ↑",
                [("Low competence, high commitment", "DIRECT. New and enthusiastic. "
                  "Give clear instruction, standards and close checkpoints.", BLUE),
                 ("High competence, high commitment", "DELEGATE. Hand over the "
                  "outcome and the decision rights; stay available, stay out.", TEAL),
                 ("Low competence, low commitment", "COACH. Explain the why, build "
                  "skill deliberately and rebuild confidence with early wins.", ROSE),
                 ("High competence, low commitment", "SUPPORT. The skill is there; "
                  "the motivation is not. Listen, remove friction, restore purpose.",
                  AMBER)],
                n, kicker=P3, accent=BLUE,
                note="There is no single correct leadership style. The ECO enabler "
                     "is literally 'determine an appropriate leadership style' — "
                     "appropriate to this person, this task, this moment."); n += 1

    X.compare(prs, "Leading vs managing",
              ("Leading",
               "Direction, alignment, commitment — about people",
               ["Sets and communicates the vision and the why",
                "Aligns people around a shared goal",
                "Inspires, motivates and builds commitment",
                "Develops capability and challenges the status quo",
                "Asks: are we doing the right thing?"]),
              ("Managing",
               "Planning, organising, controlling — about work",
               ["Plans, budgets and schedules the work",
                "Organises structure, roles and staffing",
                "Monitors variance and applies corrective action",
                "Maintains stability, predictability and control",
                "Asks: are we doing the thing right?"]),
              n, kicker=P3, lc=VIOLET, rc=BLUE,
              footer_note="A project manager does both every day. The exam usually "
                          "wants leading behaviour in People-domain scenarios and "
                          "managing behaviour in Process-domain scenarios."); n += 1

    X.cards(prs, "Emotional intelligence — the four domains",
            [("Self-awareness", "Recognising your own emotions in the moment and "
              "understanding how your actions land on other people."),
             ("Self-management", "Thinking before you act; regulating your response "
              "so pressure does not leak into the team as anxiety."),
             ("Social awareness", "Reading the emotional state of the room; empathy "
              "for what others are experiencing but not saying."),
             ("Social skill", "Establishing rapport, managing your own attitude and "
              "steering relationships toward a productive outcome."),
             ("Why it matters here", "EI is the mechanism behind conflict "
              "resolution, influencing, negotiation and stakeholder trust."),
             ("It is trainable", "Unlike personality, EI is a learnable practice — "
              "pause, name the emotion, choose the response.")],
            n, kicker=P3, accent=ROSE); n += 1

    X.activity(prs, "Role play: practising emotional intelligence under pressure",
               "In trios, run a coaching conversation about a stressful workplace "
               "moment. Rotate roles: team leader, team member, observer. The full "
               "script and prompts are in the Learner Guide.",
               ["Team member recalls a recent moment when they reacted emotionally "
                "at work and describes it factually.",
                "Leader coaches self-awareness: 'what were you feeling, and what "
                "did you notice in yourself first?'",
                "Leader models self-management by describing a pause-and-clarify "
                "response instead of an immediate reaction.",
                "Member re-runs the scenario applying the pause, then asks a "
                "clarifying question rather than defending.",
                "Leader coaches empathy: what might the other person have been "
                "experiencing that you did not see?",
                "Observer records which of the four EI domains appeared and where "
                "the conversation slipped into advice-giving."],
               "One observation sheet per trio mapping the conversation to the four "
               "EI domains, plus one improvement each person will apply this week.",
               n, accent=ROSE, duration="25 MIN"); n += 1

    X.cards(prs, "Interpersonal and team skills",
            [("Active listening", "Listen for content, tone and what is being "
              "avoided; confirm understanding before responding."),
             ("Communication styles assessment", "Identify preferred styles so you "
              "can tailor how information is delivered per stakeholder."),
             ("Influencing", "Persuade without authority using evidence, "
              "relationships and alignment to the other party's interests."),
             ("Motivation", "Apply the right theory to the right person to sustain "
              "discretionary effort over a long project."),
             ("Nominal group technique", "Silent idea generation then structured "
              "ranking, so loud voices do not dominate the outcome."),
             ("Political awareness", "Understand where real power and informal "
              "influence sit, and work with the organisation as it actually is.")],
            n, kicker=P3, accent=CYAN); n += 1

    X.compare(prs, "Rewards vs recognition",
              ("Rewards",
               "Tangible, consumable, tied to an outcome",
               ["A bonus, a voucher, a gift, a paid course",
                "Given for a specific achievement or measurable outcome",
                "Used to motivate toward a defined result",
                "Must be attainable, visible and fairly applied",
                "Never give a reward without recognition attached to it"]),
              ("Recognition",
               "Intangible, experiential, tied to behaviour",
               ["Public thanks, a note to a manager, visible credit",
                "Acknowledges the person's behaviour, not just the outcome",
                "Increases the recipient's sense of being valued",
                "Costs nothing and can be given continuously",
                "Can absolutely be given on its own without any reward"]),
              n, kicker=P3, lc=AMBER, rc=TEAL,
              footer_note="Cultural caution: public individual recognition motivates "
                          "in some cultures and embarrasses in others. Ask before "
                          "you design the ritual."); n += 1

    X.cards(prs, "Adopt a growth mindset as a leader",
            [("Experience guides, not dictates", "Let past processes inform your "
              "action without locking you into last project's answer."),
             ("Commit to improving", "Treat your own leadership practice as "
              "something to iterate on, with feedback and deliberate change."),
             ("Discover through discussion", "Find the best approach through debate "
              "and introspection rather than asserting it up front."),
             ("Avoid complacency", "Blind acceptance of 'how we do things' is how "
              "an organisation stops learning."),
             ("Model fallibility", "A leader who says 'I got that wrong' licenses "
              "the whole team to surface their own errors early."),
             ("Inclusive competence", "Lead with empathy, assume motivations vary, "
              "and deliberately include external and part-time resources.")],
            n, kicker=P3, accent=VIOLET); n += 1

    # ------------------------------------- 8. training / coaching / mentoring
    X.process(prs, "Plan training, coaching and mentoring",
              [("Gap analysis", "Compare required knowledge, skills and attributes "
                "against what the team actually holds today."),
               ("Design the mix", "Choose the blend of soft-skill and technical "
                "development, formal and informal, per person."),
               ("Schedule it close to use", "Deliver training near the point of "
                "application so the skill is used before it decays."),
               ("Deliver and practise", "Pair training with coaching so learning "
                "converts into active, on-the-job use."),
               ("Assess the outcome", "Measure improvement, not attendance, and "
                "feed the result back into the next gap analysis.")],
              n, kicker=P3, accent=BLUE,
              note="Training is a cost that belongs in the project budget when the "
                   "gap is project-specific; organisational capability gaps usually "
                   "belong to the functional manager."); n += 1

    X.cards(prs, "Elements of training and delivery models",
            [("Instructor-led classroom", "Highest interaction and fastest "
              "clarification; highest cost in time and travel."),
             ("Virtual classroom", "Live but distributed; needs deliberate "
              "facilitation to keep participation genuine rather than passive."),
             ("Self-paced e-learning", "Cheap and scalable for explicit knowledge; "
              "weak for tacit knowledge and judgement."),
             ("Document reviews", "Structured reading with a comprehension "
              "checkpoint; good for standards, policies and compliance content."),
             ("Interactive simulation", "Safe rehearsal of a high-stakes task; the "
              "only realistic option for rare, dangerous or costly scenarios."),
             ("On-the-job training", "Real work with a safety net; highest transfer "
              "rate but consumes the time of an experienced person.")],
            n, kicker=P3, accent=AMBER); n += 1

    X.table(prs, "Training vs coaching vs mentoring",
            ["Dimension", "Training", "Coaching", "Mentoring"],
            [["Purpose", "Acquire a skill for use now", "Apply or improve an "
              "existing skill", "Long-term personal and professional growth"],
             ["Horizon", "Short — a session or a course", "Medium — weeks around "
              "a performance goal", "Long — months or years"],
             ["Relationship", "Trainer to learners", "Coach to individual or team",
              "Experienced person to a less experienced person"],
             ["Content owner", "The trainer sets the curriculum",
              "The coachee sets the goal; coach asks the questions",
              "The mentee sets the direction; mentor shares experience"],
             ["Also called", "Upskilling", "Performance coaching",
              "Sponsorship, job shadowing, professional guidance"],
             ["Typical output", "Certification, badge, new capability",
              "Changed behaviour on a specific task", "Career progression, "
              "transferred tacit knowledge"]],
            n, kicker=P3, accent=TEAL, widths=[1.0, 1.4, 1.5, 1.6]); n += 1

    X.process(prs, "Steps to coach performance",
              [("Agree the goal", "Establish what good looks like and confirm the "
                "coachee actually owns and wants that goal."),
               ("Explore reality", "Ask questions to surface what is happening now, "
                "with evidence, not opinion or hearsay."),
               ("Give specific feedback", "Describe observed behaviour and its "
                "impact — never label the person's character."),
               ("Demonstrate and practise", "Model the desired behaviour, then let "
                "them rehearse it while you observe."),
               ("Agree actions and follow up", "Commit to a small, dated action and "
                "schedule the check-in that makes it real.")],
              n, kicker=P3, accent=VIOLET,
              note="Coaching is asking, not telling. If you find yourself giving "
                   "the answer in the first two minutes, you have switched from "
                   "coaching to instructing."); n += 1

    X.process(prs, "SBI — a technique for giving feedback",
              [("Situation", "Anchor the feedback in a specific time and place: "
                "'in yesterday's design review…' — never 'you always…'."),
               ("Behaviour", "Describe only what was observable — the words said, "
                "the action taken — with no interpretation of motive."),
               ("Impact", "State the effect on you, the team or the work: "
                "'…the tester left without the information she needed.'"),
               ("Pause and listen", "Stop talking. Let the other person respond; "
                "you may be missing context that changes the picture."),
               ("Agree forward action", "Convert the conversation into one specific "
                "behaviour to repeat or change next time.")],
              n, kicker=P3, accent=ROSE,
              note="SBI works for positive feedback too — and positive SBI is the "
                   "single cheapest way to make corrective feedback land later."); n += 1

    X.cards(prs, "Coach teams and individuals in project management",
            [("Delegate then observe", "Hand over a real task, watch how it is done "
              "and feed back — the most common informal coaching opportunity."),
             ("Encourage others to lead", "Let a team member run the stand-up, the "
              "demo or the risk review while you sit in the room."),
             ("Collaborate on a PM task", "Build the schedule or the risk register "
              "together so the reasoning is transferred, not just the artifact."),
             ("Facilitate sessions", "Formalise it: teach facilitation by "
              "co-facilitating, then handing the session over."),
             ("Pair individuals", "Deliberately pair a strong and a developing "
              "member on the same work item to transfer tacit knowledge."),
             ("Model behaviours", "The team copies what you do under pressure, not "
              "what you wrote in the team charter.")],
            n, kicker=P3, accent=CYAN); n += 1

    X.activity(prs, "Role play: coaching a struggling team member",
               "In pairs, run a one-to-one coaching conversation about a performance "
               "gap (e.g. low customer satisfaction scores). Swap roles after the "
               "first round. Full script in the Learner Guide.",
               ["Leader opens with a genuine strength observed before naming the gap.",
                "Leader uses SBI to describe one specific, observed behaviour and "
                "its impact — no character judgements.",
                "Leader asks open questions to let the coachee diagnose the cause "
                "themselves rather than supplying it.",
                "Leader demonstrates the desired behaviour once, briefly, then hands "
                "the conversation back.",
                "Coachee rehearses the behaviour; leader gives one reinforcing and "
                "one adjusting piece of feedback.",
                "Both agree one dated action and the date of the follow-up check-in."],
               "A completed coaching note per pair: the observed behaviour, the "
               "impact, the agreed action and the follow-up date.",
               n, accent=TEAL, duration="25 MIN"); n += 1

    X.cards(prs, "Measure training and coaching outcomes",
            [("Post-training assessment", "Test whether the skill can be performed, "
              "not merely whether the session was enjoyed."),
             ("Observation on the job", "The real proof: does the behaviour appear "
              "in actual work two weeks after the course?"),
             ("Certification evidence", "Badges or a letter from the awarding body "
              "give externally verifiable proof of a capability."),
             ("Retrospective discussion", "Share what was learned in a team "
              "retrospective so one person's training benefits everyone."),
             ("Augment with coaching", "Training alone decays fast; coaching after "
              "training converts knowledge into active use."),
             ("Knowledge-sharing pairs", "Pair the trained person with a peer so "
              "they must explain it — teaching consolidates learning.")],
            n, kicker=P7, accent=AMBER); n += 1

    X.cards(prs, "Maintain mentorships and job shadowing",
            [("Longer-term partnerships", "Mentoring is a relationship, not an "
              "event; value accrues over months of repeated contact."),
             ("Job shadowing", "Observing an expert at work transfers both explicit "
              "procedure and the tacit judgement behind it."),
             ("Tailor to the context", "Some organisations run formal mentoring "
              "with reporting; others keep it deliberately informal."),
             ("Use during transitions", "Shadowing at handover moves skills from "
              "the project team into the receiving operations team."),
             ("Recruit stakeholders", "Valued stakeholders make excellent mentors "
              "and their involvement deepens their engagement."),
             ("Mentor project managers", "Many organisations grow PMs specifically "
              "through mentorship rather than formal training.")],
            n, kicker=P7, accent=VIOLET); n += 1

    X.cards(prs, "Assess team member performance",
            [("Formal and informal methods", "Combine structured assessments with "
              "continuous observation; neither alone gives a fair picture."),
             ("Baseline on joining", "Assess when a member joins so you can measure "
              "development rather than guess at it later."),
             ("Monitor progress", "Repeat the assessment so the conversation is "
              "about trajectory, not a single snapshot."),
             ("Self-regulating teams", "Psychologically safe agile teams assess and "
              "correct their own performance in retrospectives."),
             ("Focus on the team", "Team performance assessments target the team's "
              "capability; individual appraisal usually sits with line management."),
             ("Feed Develop Team", "Assessment results identify the training, "
              "coaching and team-building the team actually needs next.")],
            n, kicker=P3, accent=BLUE); n += 1

    X.cards(prs, "Self-organising teams collaborate and learn",
            [("Encourage initiative", "Expect team members to pick up work and "
              "raise problems without waiting for an assignment."),
             ("Cross-role coaching", "Coach people on how to contribute to other "
              "project roles so the team is resilient to absence."),
             ("Surface tacit knowledge", "Coach the individual who holds undocumented "
              "know-how into explaining and demonstrating it."),
             ("Use servant leadership", "Support and enable rather than assign and "
              "check; self-organisation dies under close supervision."),
             ("Shadow during transitions", "Use shadowing, coaching and mentoring to "
              "move skills from the project team to the organisation."),
             ("Ground rules still apply", "Self-organising is not unbounded — the "
              "team charter defines the boundary they organise within.")],
            n, kicker=P3, accent=TEAL); n += 1

    # ------------------------------------------------------- 9. conflict
    X.itto(prs, "Manage Team",
           ["Project management plan: resource management plan",
            "Project documents: issue log, lessons learned register, "
            "project team assignments, team charter",
            "Work performance reports",
            "Team performance assessments",
            "Enterprise environmental factors and organizational process assets"],
           ["Interpersonal and team skills: conflict management, "
            "decision making, emotional intelligence, influencing, leadership",
            "Project management information system"],
           ["Change requests",
            "Project management plan updates: resource management plan, "
            "schedule baseline, cost baseline",
            "Project document updates: issue log, lessons learned "
            "register, project team assignments",
            "Enterprise environmental factors updates"],
           n, kicker=P2,
           purpose="Track team performance, provide feedback, resolve issues and "
                   "manage team changes to optimise project performance."); n += 1

    X.statement(prs, "Who owns conflict on a project",
                "Everyone owns it. You influence how it is handled.",
                [("Shared responsibility", "All team members and stakeholders are "
                  "responsible for managing conflict, not just the PM."),
                 ("PM influences direction", "You shape the handling through "
                  "interpersonal skills and servant leadership, not authority."),
                 ("Team resolves it", "The team is empowered to resolve its own "
                  "conflicts; the leader facilitates when they cannot.")],
                n, kicker=P2, accent=ROSE); n += 1

    X.cards(prs, "Sources of conflict on projects",
            [("Competition for resources", "Scarce people, budget and equipment "
              "force zero-sum choices between work streams."),
             ("Differing objectives and values", "Goals that conflict at the "
              "organisational level surface as friction at the team level."),
             ("Role and responsibility disputes", "Ambiguity about who decides and "
              "who delivers is the most common and most fixable source."),
             ("Differing work approaches", "Two competent people with different "
              "methods each believe the other is doing it wrong."),
             ("Communication breakdown", "Missing, late or ambiguous information "
              "gets filled in with assumption, then with blame."),
             ("Novelty of the project", "Projects are unique and members often have "
              "not worked together before — no established norms exist yet.")],
            n, kicker=P2, accent=AMBER); n += 1

    X.compare(prs, "Effective vs ineffective conflict management",
              ("Ineffective conflict management",
               "Conflict suppressed, avoided or escalated badly",
               ["Destructive behaviour and personal attacks",
                "Animosity that outlasts the disagreement itself",
                "Poor performance as energy diverts from the work",
                "Reduced productivity and lost calendar time",
                "Attrition — good people leave dysfunctional teams"]),
              ("Effective conflict management",
               "Conflict surfaced early and worked through openly",
               ["Improved understanding of the other position",
                "Better decisions because assumptions were challenged",
                "Higher performance from genuine, not artificial, agreement",
                "Higher productivity as issues stop recurring",
                "Stronger relationships that survive the next disagreement"]),
              n, kicker=P2, lc=ROSE, rc=TEAL,
              footer_note="Zero conflict is not the target. Zero conflict usually "
                          "means people have stopped saying what they think."); n += 1

    X.cards(prs, "Conflict as part of a psychologically safe culture",
            [("Disruption and innovation connect", "The friction that produces new "
              "ideas is the same friction that feels uncomfortable."),
             ("Encourage disagreement", "Actively invite dissent so risks are named "
              "while there is still time to act on them."),
             ("Separate people from positions", "Attack the problem, not the person "
              "holding the opposing view."),
             ("Prevent escalation", "Address friction at the level of a differing "
              "opinion, before it hardens into a personal contest."),
             ("Ground rules make it safe", "Agreed norms tell people what "
              "disagreement is allowed to look like on this team."),
             ("Leader goes first", "Safety is created when the leader publicly "
              "accepts challenge without punishing the challenger.")],
            n, kicker=P2, accent=CYAN); n += 1

    X.chart(prs, "Leas' five levels of conflict — escalation",
            "column",
            ["L1 Problem to solve", "L2 Disagreement", "L3 Contest",
             "L4 Crusade", "L5 World war"],
            [("Difficulty of resolution", [1, 2, 4, 7, 10]),
             ("Focus on winning vs solving", [1, 3, 6, 9, 10])],
            n, kicker=P2, accent=ROSE,
            insight=["L1: information sharing and collaboration still work; the "
                     "parties want a solution.",
                     "L2: self-protection begins — language becomes guarded and "
                     "positions get defended.",
                     "L3: the goal shifts from solving the problem to winning "
                     "against the other party.",
                     "L4: protecting one's own group becomes the point; the "
                     "original issue is almost irrelevant.",
                     "L5: destroying the other party is the objective — separate "
                     "the parties, escalate, do not mediate."],
            ymax=10); n += 1

    X.table(prs, "Leas' levels of conflict and your intervention",
            ["Level", "What you hear", "What to do"],
            [["1 · Problem to solve",
              "'How should we handle this?' — focus on the issue, open language",
              "Facilitate collaboratively; the team can resolve this themselves"],
             ["2 · Disagreement",
              "Guarded language, self-protection, humour used to deflect",
              "Encourage direct dialogue; make it safe to state the real position"],
             ["3 · Contest",
              "'I' vs 'you', winning matters, positions distorted to score points",
              "Structure the conversation; refocus on shared objectives and data"],
             ["4 · Crusade",
              "'Us' vs 'them', factions form, the issue becomes ideological",
              "Bring in a neutral facilitator; the PM is likely seen as partisan"],
             ["5 · World war",
              "Destroying the other party is the goal; no resolution is acceptable",
              "Separate the parties, escalate to sponsor/HR — mediation will fail"]],
            n, kicker=P2, accent=VIOLET, widths=[1.1, 2.0, 1.9],
            note="Intervention must match the level. Collaboration attempted at "
                 "level 4 or 5 does not just fail — it burns your credibility as "
                 "a neutral party."); n += 1

    X.matrix2x2(prs, "The five conflict-resolution modes",
                "Cooperativeness — concern for the other party →",
                "Assertiveness — concern for own goal ↑",
                [("Force / Direct (win-lose)", "High assertiveness, low "
                  "cooperation. Push your position through, usually with power.",
                  ROSE),
                 ("Collaborate / Problem solve (win-win)", "High on both. Work "
                  "the underlying interests until both parties genuinely gain.",
                  TEAL),
                 ("Withdraw / Avoid (lose-lose)", "Low on both. Retreat from the "
                  "situation or postpone the issue to another time.", AMBER),
                 ("Smooth / Accommodate (lose-win)", "Low assertiveness, high "
                  "cooperation. Concede your position to preserve the relationship.",
                  BLUE)],
                n, kicker=P2, accent=VIOLET,
                note="Compromise / Reconcile sits in the middle of the grid — "
                     "moderate on both axes, and classified lose-lose because "
                     "both parties give something up."); n += 1

    X.table(prs, "The five conflict approaches and when each is appropriate",
            ["Approach", "Outcome", "What it looks like", "When it is right"],
            [["Collaborate / Problem solve", "Win-win",
              "Incorporate multiple viewpoints; open dialogue to real consensus",
              "PMI's default. Time exists, relationship matters, stakes are high"],
             ["Compromise / Reconcile", "Lose-lose",
              "Both parties give something up to reach a workable middle",
              "Equal power, moderate stakes, a temporary fix under time pressure"],
             ["Smooth / Accommodate", "Lose-win",
              "Emphasise areas of agreement; concede to keep harmony",
              "You are wrong, the issue matters far more to them, or goodwill "
              "is the real objective"],
             ["Force / Direct", "Win-lose",
              "Pursue your view at the other party's expense; use position power",
              "Safety, legal or ethical breach; genuine emergency; no time"],
             ["Withdraw / Avoid", "Lose-lose",
              "Retreat from the situation or postpone the issue",
              "Emotions too high to be productive; you need facts; the issue "
              "is trivial or will resolve itself"]],
            n, kicker=P2, accent=TEAL, widths=[1.3, 0.8, 1.9, 2.0]); n += 1

    X.process(prs, "A repeatable conflict-resolution sequence",
              [("Set the scene", "Get the parties together with an agreed purpose; "
                "state the ground rules for the conversation."),
               ("Identify concerns", "Each party states their position uninterrupted "
                "while the other listens without rebutting."),
               ("Clarify the issues", "Summarise both positions back and confirm "
                "with each party that the summary is accurate."),
               ("Problem-solve jointly", "Move from positions to interests and "
                "generate options that could satisfy both."),
               ("Create an action plan", "Convert the agreement into specific, "
                "owned, dated actions — usually clearer roles."),
               ("Close and follow up", "Confirm both parties are satisfied and "
                "schedule the check-in that verifies it held.")],
              n, kicker=P2, accent=BLUE,
              note="The four behaviours that make this work: open communication, "
                   "active listening, joint problem solving, and a clear action "
                   "plan that neither party can quietly ignore."); n += 1

    X.activity(prs, "Role play: a conflict over project responsibilities",
               "In trios, work a real conflict: a senior member feels overloaded and "
               "over-responsible; a newer member feels distrusted and blocked from "
               "contributing. Third person facilitates. Full script in the Learner Guide.",
               ["Facilitator sets the scene, states the purpose and agrees ground "
                "rules for the conversation.",
                "Each party states their concern for two minutes, uninterrupted, "
                "using 'I feel / I observe' language.",
                "Facilitator summarises both concerns and gets explicit agreement "
                "that the summary is accurate.",
                "Both parties generate options together; the facilitator captures "
                "them without evaluating.",
                "Agree a concrete action plan — clear task ownership and a weekly "
                "check-in — and name the owner of each item.",
                "Debrief: which of the five conflict modes was actually used, and "
                "which of Leas' levels did this conflict sit at?"],
               "One completed conflict resolution record per trio: sources, level, "
               "mode used, agreed actions with owners, and the follow-up date.",
               n, accent=VIOLET, duration="30 MIN"); n += 1

    X.cards(prs, "Interpersonal skills that resolve conflict",
            [("Emotional intelligence", "Use empathy to understand what is driving "
              "each party and to defuse the emotional charge first."),
             ("Influencing", "Persuade parties to reconsider their tone, approach "
              "or mindset when direct authority would only harden positions."),
             ("Leadership", "Steer the exchange toward a constructive direction and "
              "hold the group to the agreed ground rules."),
             ("Decision making", "When the parties genuinely deadlock, offer a "
              "decision method or a solution that moves the situation forward."),
             ("Active listening", "Listen for accusing language, caustic tone and "
              "defensive posture — these tell you the escalation level."),
             ("Political awareness", "Understand what each party stands to lose "
              "organisationally, which is often the real driver.")],
            n, kicker=P2, accent=CYAN); n += 1

    X.cards(prs, "Ground rules: establish, adhere, rectify",
            [("Where they live", "Ground rules are documented in the team charter, "
              "created by the team rather than imposed by the PM."),
             ("What they cover", "Meeting conduct, response times, decision rights, "
              "how disagreement is raised, escalation paths."),
             ("Foster adherence", "Reference them regularly in real situations so "
              "they stay a live agreement rather than a forgotten document."),
             ("Detect violations", "Watch for the quiet ones: interruptions, "
              "decisions made outside the agreed forum, missed commitments."),
             ("Rectify violations", "Address privately and early using SBI; the "
              "whole team is watching whether the rule is real."),
             ("Revisit and update", "When a rule stops fitting, the team changes "
              "it deliberately — it does not simply erode.")],
            n, kicker=P2, accent=AMBER); n += 1

    X.exam(prs, "Conflict questions — the traps PMI sets",
           [("Two team members disagree; the PM should…",
             "Let them resolve it first. The team is empowered; you facilitate only "
             "if they cannot reach resolution."),
            ("'What is the BEST conflict resolution technique?'",
             "Collaborate / problem solve. It is the only genuine win-win and is "
             "PMI's default answer absent other constraints."),
            ("A safety or compliance breach is happening now",
             "Force / direct. Emergencies and ethical breaches are the legitimate "
             "case for asserting authority."),
            ("Emotions are running too high to discuss the issue",
             "Withdraw / avoid temporarily — cool down, gather facts, then return "
             "and collaborate.")],
           n, accent=ROSE); n += 1

    X.exam(prs, "More conflict and team traps",
           [("Conflict recurs on the same topic every week",
             "Go to root cause. Recurring conflict usually signals unclear roles or "
             "an unresolved structural constraint, not personalities."),
            ("A team member repeatedly breaks an agreed ground rule",
             "Address it directly and privately with the individual first, "
             "referencing the team charter the team itself created."),
            ("The sponsor asks you to overrule the team's technical decision",
             "Represent the voice of the team: present their reasoning and the "
             "impact, then negotiate rather than simply comply or refuse."),
            ("Conflict is at Leas' level 5 between two departments",
             "Separate the parties and escalate. Collaboration and mediation are "
             "not viable at that level.")],
           n, accent=ROSE); n += 1

    # ---------------------------------------------------- 10. decision making
    X.cards(prs, "How project teams decide",
            [("Team charter sets the rules", "The charter identifies the "
              "decision-making and conflict-resolution criteria in advance."),
             ("Teams define their Way of Working", "Mature teams establish their own "
              "norms for which decisions need which method."),
             ("Consensus is the aim", "Teams try for genuine agreement first; a "
              "vote is what you use when consensus is not reachable."),
             ("Decide who decides", "The most common decision failure is ambiguity "
              "about whether a group is advising or deciding."),
             ("Timebox the decision", "An undecided decision has a cost; set a "
              "deadline and a fallback method before you start."),
             ("Record the rationale", "Capture why, not just what — it prevents "
              "the same debate reopening three months later.")],
            n, kicker=P3, accent=BLUE); n += 1

    X.table(prs, "Decision-making methods",
            ["Method", "How it works", "When to use it"],
            [["Unanimity", "Everyone agrees on a single course of action",
              "High-cohesion teams; irreversible decisions; the Delphi technique "
              "converges toward it"],
             ["Majority", "More than 50% of the group supports the option",
              "Use odd-numbered groups so a tie cannot block the decision"],
             ["Plurality", "The largest single block decides, even without 50%",
              "More than two options on the table and no majority emerges"],
             ["Autocratic", "One individual decides for the whole group",
              "Emergency, or the decision is genuinely one person's accountability"],
             ["Delphi technique", "Anonymous expert rounds with feedback until "
              "convergence", "Expert estimates where seniority or politics would "
              "distort an open discussion"],
             ["Multicriteria decision analysis", "Score options against weighted "
              "criteria in a matrix", "Comparing suppliers, designs or candidates "
              "on several dimensions at once"],
             ["Fist of five", "Each person shows 0-5 fingers to signal support level",
              "Fast consensus check; anything below three triggers a discussion"],
             ["Dot voting", "Each participant places a fixed number of dots on options",
              "Prioritising a long list of ideas quickly and visibly"]],
            n, kicker=P3, accent=TEAL, widths=[1.2, 1.9, 2.0]); n += 1

    X.process(prs, "Diverge then converge",
              [("Frame the question", "Agree exactly what is being decided and what "
                "constraints any option must satisfy."),
               ("Diverge on the problem", "Explore the problem space fully before "
                "anyone proposes a solution."),
               ("Diverge on solutions", "Generate options without evaluation — "
                "brainstorming, nominal group technique, mind mapping."),
               ("Converge with criteria", "Filter using agreed criteria, then score "
                "with multicriteria decision analysis or dot voting."),
               ("Decide and record", "Choose, capture the rationale and dissent, "
                "and confirm who commits to the decision.")],
              n, kicker=P3, accent=CYAN,
              note="The classic failure mode is converging too early — the group "
                   "evaluates the first idea and never generates the second."); n += 1

    X.activity(prs, "Practice: multi-criteria decision analysis",
               "In table groups, choose between three candidate vendors for a "
               "project component using a weighted scoring matrix, then compare how "
               "the group's decision method changed the outcome.",
               ["List the decision criteria that genuinely matter (cost, "
                "capability, risk, delivery time, support).",
                "Weight each criterion by importance and get the group to agree "
                "the weights before seeing the options.",
                "Score all three vendors against each criterion, using evidence "
                "rather than preference.",
                "Compute the weighted totals and identify the top-ranked option.",
                "Re-run the same choice using dot voting alone and note whether "
                "the answer changes.",
                "Debrief which method you would defend to a sponsor and why."],
               "A completed weighted scoring matrix with agreed weights, scores, "
               "the recommended vendor and a one-paragraph rationale.",
               n, tool="Pivot Analysis", url=cd.TOOLS["pivot"][1],
               accent=CYAN, duration="25 MIN"); n += 1

    # --------------------------------------------------- 11. communication
    X.itto(prs, "Manage Communications",
           ["Project management plan: resource management plan, "
            "communications management plan, stakeholder engagement plan",
            "Project documents: change log, issue log, lessons learned "
            "register, quality report, risk report, stakeholder register",
            "Work performance reports",
            "Enterprise environmental factors and organizational process assets"],
           ["Communication technology, methods and skills "
            "(competence, feedback, nonverbal, presentations)",
            "Project management information system",
            "Project reporting",
            "Interpersonal and team skills: active listening, conflict "
            "management, cultural awareness, meeting management, networking",
            "Meetings"],
           ["Project communications",
            "Project management plan updates: communications management "
            "plan, stakeholder engagement plan",
            "Project document updates: issue log, lessons learned "
            "register, project schedule, risk register, stakeholder register",
            "Organizational process assets updates"],
           n, kicker=P8,
           purpose="Ensure timely and appropriate collection, creation, "
                   "distribution, storage, retrieval, management, monitoring and "
                   "disposition of project information."); n += 1

    X.cards(prs, "Barriers to communication",
            [("Language differences", "Misunderstanding from differences in "
              "language, dialect or fluency — including polite over-agreement."),
             ("Cultural differences", "Norms about directness, hierarchy and "
              "disagreement vary; the same words carry different meaning."),
             ("Technical jargon", "Insider vocabulary excludes the very "
              "stakeholders whose decision you need."),
             ("Physical barriers and noise", "Distance, poor connections, "
              "background noise and time-zone lag degrade the signal."),
             ("Psychological barriers", "Stress, fear of blame or fatigue stop "
              "people hearing and stop people speaking."),
             ("Assumptions and perception", "Filling gaps with what you expect to "
              "be true is the fastest route to a costly rework.")],
            n, kicker=P8, accent=AMBER); n += 1

    X.compare(prs, "Assertive vs aggressive communication",
              ("Assertive",
               "Direct, respectful, confident — the target style",
               ["States a position clearly without attacking the other person",
                "Uses 'I' language: 'I need the spec by Friday because…'",
                "Says no to the request without rejecting the person",
                "Invites the other view and genuinely listens to it",
                "Produces clarity and preserves the relationship"]),
              ("Aggressive",
               "Dominating, confrontational, disrespectful",
               ["Wins the exchange at the other person's expense",
                "Uses 'you' accusations: 'you never deliver anything on time'",
                "Interrupts, raises voice, uses status to close down debate",
                "Treats disagreement as disloyalty",
                "Produces short-term compliance and long-term silence"]),
              n, kicker=P8, lc=TEAL, rc=ROSE,
              footer_note="The two failure modes below assertive: PASSIVE (avoids "
                          "confrontation, agrees then does not deliver) and "
                          "PASSIVE-AGGRESSIVE (disguised hostility, indirect "
                          "sabotage, sarcasm)."); n += 1

    X.table(prs, "The communication styles",
            ["Style", "Behaviour", "Effect on the team"],
            [["Assertive", "Direct, respectful, confident; states needs clearly",
              "Issues get raised early and resolved; the target style"],
             ["Aggressive", "Dominating, confrontational, disrespectful",
              "Compliance in the room, silence afterwards; risks go unreported"],
             ["Passive", "Submissive, avoids confrontation, indirect",
              "Agreement that is not real; commitments quietly missed"],
             ["Passive-aggressive", "Indirect, disguised hostility, sarcasm",
              "Corrosive; the conflict continues underground and cannot be resolved"],
             ["Manipulative", "Controlling and deceitful; uses influence covertly",
              "Destroys trust permanently once detected; an ethics issue"]],
            n, kicker=P8, accent=VIOLET, widths=[1.1, 2.0, 2.0],
            note="Communication styles assessment is an explicit interpersonal and "
                 "team skill in Plan Communications Management — use it to tailor "
                 "your approach per stakeholder."); n += 1

    X.activity(prs, "Role play: overcoming a communication barrier",
               "In pairs, run a conversation in which one party uses heavy technical "
               "jargon and unstated assumptions with a non-technical counterpart. "
               "Full script in the Learner Guide.",
               ["Speaker deliberately explains a solution using acronyms and "
                "internal jargon for ninety seconds.",
                "Listener notes every point at which they lost the thread, without "
                "interrupting.",
                "Speaker restarts, replacing every technical term with a plain "
                "outcome the listener cares about.",
                "Listener asks clarifying questions; speaker answers without "
                "reintroducing jargon.",
                "Both identify the assumptions the speaker made about the "
                "listener's prior knowledge.",
                "Swap roles and repeat with a different topic."],
               "A short 'plain-language rewrite': the original jargon-heavy "
               "explanation beside the version a sponsor could act on.",
               n, accent=AMBER, duration="20 MIN"); n += 1

    X.cards(prs, "Where and how the team works",
            [("Colocation is best where possible", "A shared physical space "
              "maximises informal communication and tacit knowledge transfer."),
             ("Tight matrix / war room", "Deliberately putting the team in one room "
              "for a critical phase measurably raises throughput."),
             ("Environment affects performance", "Noise, lighting, screens and "
              "meeting-room access are real performance variables, not comforts."),
             ("Foster meaningful interaction", "Design contact points that support "
              "autonomy rather than surveillance."),
             ("Respect agreed working hours", "Ground rules about core hours and "
              "response times protect focus and prevent burnout."),
             ("Hybrid is the normal case", "Most teams are now partly distributed; "
              "plan for it rather than treating it as an exception.")],
            n, kicker=P3, accent=BLUE); n += 1

    X.cards(prs, "Managing virtual team members",
            [("Watch team dynamics", "Distance hides friction; you must actively "
              "look for it rather than waiting for it to be reported."),
             ("Enforce transparency", "Make work and status visible with "
              "Kanban-style boards so nobody has to ask what is happening."),
             ("Hold accountability", "Clear ownership matters more remotely, where "
              "informal reminders do not happen naturally."),
             ("Use video deliberately", "Cameras on for discussion so you can read "
              "body language, tone and hesitation."),
             ("Check active participation", "Silence on a call is ambiguous — "
              "invite each person by name rather than asking 'any questions?'."),
             ("Overlap working hours", "Protect a common window across time zones "
              "for the interaction that genuinely needs to be synchronous.")],
            n, kicker=P8, accent=TEAL); n += 1

    X.cards(prs, "Virtual team best practices",
            [("Manage the isolation risk", "Remote members drift out of the "
              "informal loop; build in deliberate social contact."),
             ("Shared goals over individual output", "Focus on team commitments so "
              "distributed members feel part of one outcome."),
             ("Instil shared commitment", "A visible, common definition of done "
              "does more for cohesion than any social event."),
             ("Standardise the tooling", "One agreed channel per purpose prevents "
              "information fragmenting across five tools."),
             ("Write more, assume less", "Distributed teams need decisions recorded "
              "in writing because corridor clarification is unavailable."),
             ("Rotate meeting inconvenience", "Do not always make the same time "
              "zone take the 11pm call.")],
            n, kicker=P8, accent=CYAN); n += 1

    X.cards(prs, "Negotiate and run effective meetings",
            [("Negotiation is a conversation", "Treat it as a conversation with "
              "internal or external parties aimed at reaching agreement."),
             ("Aim for consensus", "Use effective communication so collaboration, "
              "not victory, is the objective of the exchange."),
             ("Stay positive", "Keeping the tone constructive materially increases "
              "the likelihood of a durable agreement."),
             ("Meetings: publish an agenda", "State the purpose and the desired "
              "outcome; if you cannot, cancel the meeting."),
             ("Timebox discussion", "Everyone's time is a project cost; protect it "
              "with explicit time limits per item."),
             ("Close with actions", "End every meeting with decisions, owners and "
              "dates — otherwise it produced nothing.")],
            n, kicker=P8, accent=VIOLET); n += 1

    # ------------------------------- 12. vision, AI, risk/procurement, recap
    X.process(prs, "Root-cause analysis of a misunderstanding of the vision",
              [("Detect the symptom", "Work is being delivered that is technically "
                "correct but does not serve the intended outcome."),
               ("Break down the situation", "Separate what was communicated, what "
                "was heard, and what was actually built."),
               ("Ask why five times", "Drive past 'they misunderstood' to the "
                "mechanism — missing context, competing message, no feedback loop."),
               ("Identify the true root", "Usually a vision never made concrete, or "
                "a middle layer translating it differently to each group."),
               ("Correct and re-promote", "Restate the vision with concrete "
                "examples and verify understanding by asking them to restate it.")],
              n, kicker=P1, accent=BLUE,
              note="ECO People T1 explicitly requires you to 'break down situations "
                   "to identify the root cause of a misunderstanding of the vision' "
                   "— a new 2026 enabler."); n += 1

    X.cards(prs, "Keep the common vision alive",
            [("Co-create it", "A vision the key stakeholders helped write is "
              "defended; one they were shown is merely tolerated."),
             ("Promote it continuously", "Repeat it at kick-off, at every review "
              "and in every decision rationale until it is boring to you."),
             ("Make it decidable", "A useful vision resolves trade-offs — if it "
              "cannot settle an argument it is a slogan, not a vision."),
             ("Keep it current", "Business environments move; a vision not revisited "
              "quietly becomes false and the team notices before you do."),
             ("Test understanding", "Ask team members to state the vision in their "
              "own words; divergence is your early warning."),
             ("Connect daily work to it", "Show each person how their work package "
              "moves the outcome — this is the strongest motivator you have.")],
            n, kicker=P1, accent=TEAL); n += 1

    X.cards(prs, "AI's effect on team roles and upskilling",
            [("Roles shift, not vanish", "Routine drafting, summarising and "
              "reporting move to AI; judgement, context and accountability stay human."),
             ("New capability gaps", "Prompting, output verification and data "
              "handling become skills your gap analysis must now include."),
             ("Verification is a task", "AI output must be reviewed by a competent "
              "human; build that review step explicitly into the workflow."),
             ("Upskill, do not displace", "Plan training so existing members move "
              "up the value chain rather than being replaced by tooling."),
             ("Address the anxiety", "Fear of replacement is a safety-level need in "
              "Maslow's terms and will block every other motivator."),
             ("Govern the use", "Agree ground rules on confidentiality, "
              "attribution and permitted uses before shadow adoption sets them.")],
            n, kicker=P3, accent=ROSE); n += 1

    X.itto(prs, "Implement Risk Responses",
           ["Project management plan: risk management plan",
            "Project documents: lessons learned register, risk register, "
            "risk report",
            "Organizational process assets"],
           ["Expert judgment",
            "Interpersonal and team skills: influencing",
            "Project management information system"],
           ["Change requests",
            "Project document updates: issue log, lessons learned "
            "register, project team assignments, risk register, risk report"],
           n, kicker=cd.eco("Business Environment", 5),
           purpose="Execute agreed-upon risk response plans. Planning responses "
                   "without implementing them is a classic exam trap."); n += 1

    X.itto(prs, "Conduct Procurements",
           ["Project management plan: scope, requirements, communications, "
            "risk, procurement management plans; configuration management plan; "
            "cost baseline",
            "Project documents: lessons learned register, project schedule, "
            "requirements documentation, risk register, stakeholder register",
            "Procurement documentation, seller proposals",
            "Enterprise environmental factors and organizational process assets"],
           ["Expert judgment",
            "Advertising",
            "Bidder conferences",
            "Data analysis: proposal evaluation",
            "Interpersonal and team skills: negotiation"],
           ["Selected sellers",
            "Agreements",
            "Change requests",
            "Project management plan updates",
            "Project document updates: lessons learned register, "
            "requirements documentation, resource calendars, risk register, "
            "stakeholder register"],
           n, kicker=cd.eco("Process", 5),
           purpose="Obtain seller responses, select a seller and award a contract "
                   "— the executing half of procurement management."); n += 1

    X.statement(prs, "The habit that carries you through the People domain",
                "Facilitate first. Direct only when you must.",
                [("Empower before deciding", "Ask whether the team can resolve it "
                  "before you resolve it for them."),
                 ("Understand before acting", "Gather facts and hear the parties "
                  "before choosing an intervention or escalating."),
                 ("Escalate with a recommendation", "When you must go up, bring the "
                  "impact, the options and your recommended action.")],
                n, kicker=P3, accent=TEAL); n += 1

    X.recap(prs, "Topic 4 recap — Lead the Project Team",
            [("Execution processes", "Direct and Manage Project Work produces "
              "deliverables, work performance data, issues and change requests."),
             ("Data → information → reports", "Raw measurement becomes meaningful by "
              "comparison, then becomes a communication artifact."),
             ("Artifacts under control", "Configuration management governs the "
              "product; version and document control keep the record honest."),
             ("Knowledge", "Explicit knowledge is codified and shared; tacit "
              "knowledge needs trust, conversation and shadowing to move."),
             ("Team development", "Tuckman: forming, storming, norming, performing, "
              "adjourning — direct, coach, support, delegate, close."),
             ("Motivation", "Maslow, Herzberg, McGregor, McClelland and Vroom each "
              "answer a different question about why effort appears."),
             ("Leadership style", "Servant leadership is the default; the right "
              "style is situational and deliberately chosen."),
             ("Emotional intelligence", "Self-awareness, self-management, social "
              "awareness and social skill underpin every People-domain task."),
             ("Conflict", "Collaborate is the best mode; Leas' levels tell you when "
              "collaboration is no longer viable and escalation is required."),
             ("Communication", "Tailor to the stakeholder, remove barriers, be "
              "assertive, and make virtual work visible and written down.")],
            n, accent=CYAN); n += 1

    return n
