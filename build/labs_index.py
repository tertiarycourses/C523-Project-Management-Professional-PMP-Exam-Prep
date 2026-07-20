"""
Canonical lab index — the alignment backbone.

The PPT activity slides, the Lesson Plan schedule, the Learner Guide lab
chapters and the labs/README all read THIS list, so a lab cannot appear in
one artifact with a different number, title, topic, ECO task or duration
than it has in another.

Fields
  no       lab number (1-24)
  slug     the labs/lab-NN-<slug>.md filename stem
  title    human title, used verbatim everywhere
  topic    course topic 1-6
  day      training day 1-4
  eco      ECO 2026 task reference(s) exercised
  lo       course learning outcome
  minutes  FULL duration of the lab including its extension steps
  in_class minutes actually timetabled in the Lesson Plan; the balance
           (minutes - in_class) is self-study the learner completes after
           the session. in_class MUST total LAB_MINUTES_PER_DAY[day] — 180 on
           days 1-3 and 280 on day 4, whose afternoon is the capstone lab
           and the self-scored mock practice exam (no assessment).
  tools    keys into course_data.TOOLS (live browser tools), may be empty
  outputs  artifacts produced, consumed by later labs
"""

LABS = [
    # ---------------------------------------------- Topic 1 · Day 1
    dict(no=1, slug="pmp-exam-orientation-35-pdu-study-plan",
         title="PMP Exam Orientation and 35-PDU Study Plan",
         topic=1, day=1, eco="All domains", lo="LO1", minutes=45, in_class=20,
         tools=[], outputs=["Personal study plan", "Domain self-assessment"]),
    dict(no=2, slug="pestle-tecop-external-environment-scan",
         title="PESTLE and TECOP External Environment Scan",
         topic=1, day=1, eco="BE T8", lo="LO1", minutes=45, in_class=20,
         tools=["mindmap"], outputs=["PESTLE scan", "TECOP risk themes"]),
    dict(no=3, slug="eef-opa-inventory-governance-escalation",
         title="EEF/OPA Inventory with Governance and Escalation Thresholds",
         topic=1, day=1, eco="BE T1", lo="LO1", minutes=45, in_class=20,
         tools=[], outputs=["EEF/OPA inventory", "Escalation threshold table"]),
    dict(no=4, slug="compliance-sustainability-ai-governance-register",
         title="Compliance, Sustainability and AI Governance Register",
         topic=1, day=1, eco="BE T2", lo="LO4", minutes=45, in_class=20,
         tools=[], outputs=["Compliance register", "AI governance controls"]),

    # ---------------------------------------------- Topic 2 · Day 1
    dict(no=5, slug="business-case-cost-benefit-analysis",
         title="Business Case and Cost-Benefit Analysis",
         topic=2, day=1, eco="Process T3", lo="LO1", minutes=50, in_class=25,
         tools=["stats"], outputs=["Business case", "NPV/ROI/payback model"]),
    dict(no=6, slug="project-charter",
         title="Project Charter",
         topic=2, day=1, eco="Process T1", lo="LO1", minutes=45, in_class=20,
         tools=[], outputs=["Approved project charter"]),
    dict(no=7, slug="stakeholder-register-power-interest-salience",
         title="Stakeholder Register, Power/Interest Grid and Salience Model",
         topic=2, day=1, eco="People T4, T5", lo="LO4", minutes=50, in_class=25,
         tools=[], outputs=["Stakeholder register", "Power/interest grid",
                            "Salience classification"]),
    dict(no=8, slug="team-charter-ground-rules-shared-vision",
         title="Team Charter, Ground Rules and Shared Vision",
         topic=2, day=1, eco="People T1, T2", lo="LO3", minutes=45, in_class=30,
         tools=[], outputs=["Team charter", "Ground rules", "Vision statement"]),

    # ---------------------------------------------- Topic 3 · Day 2
    dict(no=9, slug="requirements-elicitation-mind-mapping-rtm",
         title="Requirements Elicitation and Traceability Matrix",
         topic=3, day=2, eco="Process T2", lo="LO1", minutes=50, in_class=30,
         tools=["mindmap"], outputs=["Requirements list", "RTM"]),
    dict(no=10, slug="moscow-kano-product-backlog",
         title="MoSCoW and Kano Prioritisation with Product Backlog",
         topic=3, day=2, eco="Process T3", lo="LO1", minutes=50, in_class=30,
         tools=["scrum"], outputs=["Prioritised backlog", "Story point estimates"]),
    dict(no=11, slug="wbs-wbs-dictionary",
         title="Work Breakdown Structure and WBS Dictionary",
         topic=3, day=2, eco="Process T2", lo="LO1", minutes=50, in_class=30,
         tools=[], outputs=["WBS", "WBS dictionary", "Scope baseline"]),
    dict(no=12, slug="network-diagram-pert-critical-path",
         title="Network Diagram, PERT Estimating and Critical Path",
         topic=3, day=2, eco="Process T8", lo="LO2", minutes=60, in_class=35,
         tools=[], outputs=["Network diagram", "Critical path", "Float table"]),
    dict(no=13, slug="cost-estimating-budget-reserves",
         title="Cost Estimating, Budget and Reserve Analysis",
         topic=3, day=2, eco="Process T6", lo="LO2", minutes=50, in_class=25,
         tools=["stats"], outputs=["Cost estimates", "Cost baseline",
                                   "Reserve plan"]),
    dict(no=14, slug="risk-register-probability-impact-emv",
         title="Risk Register, Probability/Impact Matrix and EMV Decision Tree",
         topic=3, day=2, eco="BE T5", lo="LO4", minutes=60, in_class=30,
         tools=["systemloop"], outputs=["Risk register", "P/I matrix",
                                        "EMV decision tree"]),

    # ---------------------------------------------- Topic 4 · Day 3
    dict(no=15, slug="raci-responsibility-assignment-matrix",
         title="RACI Responsibility Assignment Matrix",
         topic=4, day=3, eco="People T3, Process T4", lo="LO2", minutes=45, in_class=20,
         tools=["raci"], outputs=["RACI matrix", "Resource plan"]),
    dict(no=16, slug="tuckman-diagnosis-motivation-theory",
         title="Tuckman Diagnosis and Motivation Theory Application",
         topic=4, day=3, eco="People T3", lo="LO3", minutes=45, in_class=20,
         tools=[], outputs=["Team stage diagnosis", "Motivation action plan"]),
    dict(no=17, slug="conflict-resolution-role-play-leas-levels",
         title="Conflict Resolution Role-Play across the Five Modes",
         topic=4, day=3, eco="People T2", lo="LO3", minutes=50, in_class=20,
         tools=[], outputs=["Conflict analysis", "Resolution strategy"]),
    dict(no=18, slug="communication-plan-channels-status-report",
         title="Communication Plan, Channels Formula and Status Report",
         topic=4, day=3, eco="People T8", lo="LO4", minutes=50, in_class=20,
         tools=[], outputs=["Communications management plan", "Status report"]),

    # ---------------------------------------------- Topic 5 · Day 3
    dict(no=19, slug="kanban-board-wip-lead-cycle-time",
         title="Kanban Board with WIP Limits and Lead/Cycle Time",
         topic=5, day=3, eco="Process T9", lo="LO5", minutes=45, in_class=20,
         tools=["kanban"], outputs=["Kanban board", "Cycle time measurements"]),
    dict(no=20, slug="earned-value-management-analysis",
         title="Earned Value Management and Schedule Compression",
         topic=5, day=3, eco="Process T9", lo="LO5", minutes=60, in_class=25,
         tools=["stats"], outputs=["EVM calculation sheet", "Forecast (EAC/ETC)",
                                   "Compression decision"]),
    dict(no=21, slug="root-cause-analysis-5whys-fishbone-pareto",
         title="Root Cause Analysis with 5 Whys, Fishbone and Pareto",
         topic=5, day=3, eco="BE T4", lo="LO3", minutes=60, in_class=25,
         tools=["5whys", "fishbone", "pareto"],
         outputs=["5 Whys chain", "Fishbone diagram", "Pareto chart"]),
    dict(no=22, slug="spc-control-chart-statistical-analysis",
         title="SPC Control Chart and Statistical Process Analysis",
         topic=5, day=3, eco="Process T7", lo="LO5", minutes=60, in_class=30,
         tools=["spc", "stats"], outputs=["Control chart", "Stability verdict",
                                          "Capability summary"]),

    # ---------------------------------------------- Topic 6 · Day 4
    dict(no=23, slug="project-closure-benefits-lessons-learned",
         title="Project Closure, Benefits Realisation and Lessons Learned",
         topic=6, day=4, eco="Process T10, BE T6", lo="LO5", minutes=105, in_class=105,
         tools=[], outputs=["Closure checklist", "Final report",
                            "Lessons learned register"]),
    dict(no=24, slug="capstone-project-plan-mock-exam",
         title="Capstone: Consolidated Project Plan and Mock Exam",
         topic=6, day=4, eco="All domains", lo="LO1-LO5", minutes=175, in_class=175,
         tools=[], outputs=["Consolidated project management plan",
                            "Mock exam score analysis by domain"]),
]

BY_NO = {l["no"]: l for l in LABS}
BY_TOPIC = {}
for _l in LABS:
    BY_TOPIC.setdefault(_l["topic"], []).append(_l)


def filename(lab):
    return f"lab-{lab['no']:02d}-{lab['slug']}.md"


# What the Lesson Plan's daily schedule allots to labs. Day 4 is larger
# because its afternoon is the capstone lab plus the self-scored mock
# practice exam — this non-WSQ course has no assessment.
LAB_MINUTES_PER_DAY = {1: 180, 2: 180, 3: 180, 4: 280}


def total_minutes():
    return sum(l["minutes"] for l in LABS)


def in_class_minutes():
    return sum(l["in_class"] for l in LABS)


def self_study_minutes():
    return total_minutes() - in_class_minutes()


def _assert_day_budget():
    """The timetabled lab time must match what the Lesson Plan allots."""
    for day in sorted({l["day"] for l in LABS}):
        got = sum(l["in_class"] for l in LABS if l["day"] == day)
        want = LAB_MINUTES_PER_DAY[day]
        if got != want:
            raise AssertionError(
                f"Day {day} timetables {got} min of labs but the Lesson Plan "
                f"allots {want}. Adjust in_class values.")


_assert_day_budget()


if __name__ == "__main__":
    print(f"{len(LABS)} labs, {total_minutes()} minutes "
          f"({total_minutes()/60:.1f} hours)")
    for t in sorted(BY_TOPIC):
        ls = BY_TOPIC[t]
        print(f"  Topic {t}: {len(ls)} labs, "
              f"{sum(l['minutes'] for l in ls)} min")
