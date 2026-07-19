"""
Domain 1 - Business Environment. Hands-on activities for labs 01-04.

Each dict is one lab. `num` is the global contiguous lab number across all
domains; `topic` is the domain number (matches course_data TOPICS num). The
build engine renders one PPT activity + step slides, one Learner-Guide section
and one Lesson-Plan schedule entry per activity.
"""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="PMP Exam Orientation and 35 PDU Study Plan",
        objective="Business Env T1 - Define and establish project governance (success metrics)",
        desc=(
            "Reconstruct the ECO (July 2026) blueprint from its totals - 180 questions, 170 scored, 240 "
            "minutes - deriving the per-domain scored counts and the 80-second pacing rule by hand. "
            "Catalogue all six question types including graphic-based items, record the 35 contact-hour "
            "evidence, and build a six-week study plan weighted to the domain percentages. Test "
            "answer-selection heuristics on three Contoso case scenarios."
        ),
        build=(
            "An exam blueprint with derived question counts and pacing figure "
            "(artifacts/01-exam-blueprint.md), a 35 contact-hour record (artifacts/01-pdu-log.md), a "
            "six-week weighted study plan (artifacts/01-study-plan.md), answer-selection heuristics and a "
            "baseline score."
        ),
        services="Spreadsheet, Markdown editor",
        steps=[
            ("Build the exam blueprint from the ECO 2026 numbers and derive the per-domain scored-question counts", ""),
            ("Log the six question types and write an approach for each under time pressure", ""),
            ("Record your 35 contact-hour evidence against the PMP eligibility rule", ""),
            ("Build a six-week study plan weighted to the blueprint domain percentages", ""),
            ("Write your answer-selection heuristics: what to eliminate and what to prefer", ""),
            ("Apply the heuristics to three scenarios, naming the heuristic that decided each", ""),
            ("Set your baseline score over 20 timed practice questions", ""),
        ],
        test=(
            "The per-domain counts read 56 / 70 / 44 and sum to exactly 170; the pacing figure is "
            "80 seconds per question derived from 240 / 180; the study plan gives Process the largest "
            "single hour allocation and contains two full-length timed mocks in the final week; and each "
            "scenario answer names a heuristic rather than only a letter."
        ),
    ),
    dict(
        num=2,
        topic=1,
        title="PESTLE and TECOP External Environment Scan",
        objective=(
            "Business Env T8 - Evaluate external business environment changes; "
            "Business Env T7 - Support organizational change"
        ),
        desc=(
            "From the Contoso briefing pack, run a PESTLE scan across all six categories, scoring every "
            "factor for impact and likelihood. Run a TECOP scan over the five risk dimensions to surface "
            "the operational and political exposure PESTLE misses. Combine and rank both tables, take the "
            "vital few scoring 16 or above, and translate each into a scope, backlog or cost consequence "
            "with a named destination artifact."
        ),
        build=(
            "A scored six-category PESTLE scan (artifacts/02-pestle-scan.md), a scored five-dimension TECOP "
            "scan (artifacts/02-tecop-scan.md), a combined ranked factor table, and a backlog-impact table "
            "mapping each top factor to its destination artifact (artifacts/02-backlog-impacts.md)."
        ),
        services="PESTLE, TECOP, Mind Mapping",
        steps=[
            ("Read the Contoso operating-environment briefing pack", ""),
            ("Build and score the PESTLE table, adding at least two factors of your own", ""),
            ("Run the TECOP scan across the technical, environmental, commercial, operational and political dimensions", ""),
            ("Rank the combined factors and take the vital few scoring 16 or above", ""),
            ("Translate each ranked factor into a scope and backlog consequence with a destination artifact", ""),
            ("Set the review cadence, owner and out-of-cycle triggers", ""),
            ("Answer the exam-style scenarios on responding to external change", ""),
        ],
        test=(
            "Every PESTLE letter carries at least one factor, every score is the product of a stated impact "
            "and likelihood, the TECOP table surfaced at least one factor absent from the PESTLE table, and "
            "every factor scoring 16 or above has a named destination artifact in a later lab rather than a "
            "vague instruction to monitor."
        ),
    ),
    dict(
        num=3,
        topic=1,
        title="EEF/OPA Inventory, Governance and Escalation Thresholds",
        objective=(
            "Business Env T1 - Define and establish project governance; "
            "Business Env T4 - Remove impediments and manage issues"
        ),
        desc=(
            "Separate Enterprise Environmental Factors - conditions the project must live with - from "
            "Organizational Process Assets, the templates and standards it reuses. Design the Contoso "
            "governance model: which body decides what, at which cadence, with what rights. Set numeric "
            "escalation thresholds for cost, schedule, risk and issue severity, and separate the change "
            "control path from the issue resolution path."
        ),
        build=(
            "A classified EEF/OPA inventory (artifacts/03-eef-opa-inventory.md), a governance model naming "
            "decision bodies, rights, cadence and success metrics (artifacts/03-governance-model.md), and a "
            "numeric escalation threshold table separating change and issue paths "
            "(artifacts/03-escalation-thresholds.md)."
        ),
        services="Spreadsheet, Markdown editor",
        steps=[
            ("Inventory the Contoso Enterprise Environmental Factors", ""),
            ("Inventory the Contoso Organizational Process Assets", ""),
            ("Design the governance model: bodies, decision rights and cadence", ""),
            ("Define the project success metrics and their measurement baselines", ""),
            ("Set numeric escalation thresholds for cost, schedule, risk and issues", ""),
            ("Separate the change control path from the issue resolution path", ""),
            ("Answer the exam-style scenarios on governance and escalation", ""),
        ],
        test=(
            "Every item in the inventory is classified as an EEF or an OPA and the learner can justify each "
            "classification; each governance body has a named decision right and cadence; every escalation "
            "threshold carries a number rather than a word such as significant; and the change path and the "
            "issue path are visibly different routes with different owners."
        ),
    ),
    dict(
        num=4,
        topic=1,
        title="Compliance, Sustainability and AI-Governance Register",
        objective=(
            "Business Env T2 - Plan and manage project compliance; "
            "Process T7 - Plan and optimize quality (regulatory compliance, sustainability)"
        ),
        desc=(
            "Classify Contoso's compliance requirements - PDPA personal-data protection, the statutory "
            "seven-year attendance retention obligation and the pre-go-live review - then identify the "
            "threats to each and quantify the consequences of noncompliance. Decide the actions and how "
            "compliance is measured. Add the two areas the July 2026 ECO expects: net-zero hosting, and "
            "AI governance for the deferred AI recommender."
        ),
        build=(
            "A compliance register with threats, consequences, actions and measures "
            "(artifacts/04-compliance-register.md), a sustainability plan covering the net-zero hosting "
            "obligation (artifacts/04-sustainability-plan.md), and an AI-governance register "
            "(artifacts/04-ai-governance.md)."
        ),
        services="Spreadsheet, Markdown editor",
        steps=[
            ("Confirm the compliance requirements and classify them by category", ""),
            ("Identify the threats to each compliance requirement", ""),
            ("Analyse and quantify the consequences of noncompliance", ""),
            ("Decide the approach and the specific actions for each requirement", ""),
            ("Define how compliance is measured, with evidence and a measurement owner", ""),
            ("Build the sustainability section against the group net-zero obligation", ""),
            ("Build the AI-governance register for the deferred AI recommender", ""),
            ("Answer the exam-style scenarios on compliance decisions", ""),
        ],
        test=(
            "Every compliance requirement has a named threat, a quantified consequence, an action and a "
            "measurement method with an owner; the sustainability section ties to a reportable hosting "
            "carbon figure; and the AI-governance register records data use, human oversight and an "
            "accountable owner rather than a general statement of intent."
        ),
    ),
]
