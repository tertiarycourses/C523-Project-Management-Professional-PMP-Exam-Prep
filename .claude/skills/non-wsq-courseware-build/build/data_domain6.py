"""
Domain 6 - Close the Project.

Per-domain hands-on activities (single source of the labs). Each dict maps to
one labs/lab-NN-*.md file. `num` is the GLOBAL contiguous lab number; `topic`
is the domain number (6).
"""

DOMAIN6 = [
    dict(
        num=23,
        topic=6,
        title="Project Closure, Benefits Realisation and Lessons Learned",
        objective=(
            "Process T10 - Manage project closure and transitions; Business Environment T6 - Support organizational "
            "change and continuous improvement; People T7 - Help ensure knowledge transfer."
        ),
        desc=(
            "Close the Contoso project against the four closure enablers. Define closure criteria first, "
            "run Control Quality against specification before seeking acceptance through Validate Scope, "
            "then validate operational readiness. Write the final report against all eight charter success "
            "criteria - including the one missed - and reconcile the final cost. Hand every benefit to a "
            "named owner with a post-closure review date."
        ),
        build=(
            "artifacts/23-closure-checklist.md separating procurement from administrative closure; "
            "artifacts/23-final-report.md with the eight criteria and cost reconciliation; "
            "artifacts/23-lessons-learned.md; artifacts/23-benefits-realisation.md handing B1 to B4 to "
            "named owners; artifacts/23-transition-plan.md."
        ),
        services="Closure checklist, Benefits realisation register, Lessons learned register",
        steps=[
            ("Define the closure criteria before closing anything", ""),
            ("Verify scope with Control Quality before seeking acceptance", ""),
            ("Obtain formal acceptance from the customer through Validate Scope", ""),
            ("Validate readiness for transition to operations", ""),
            ("Write the final report against all eight charter success criteria", ""),
            ("Hand over the benefits to named owners with review dates beyond project end", ""),
            ("Capture lessons learned that each update a named organisational process asset", ""),
            ("Plan the knowledge transfer and release the team", ""),
            ("Answer the exam-style scenarios on closure sequence, acceptance and benefits ownership", ""),
        ],
        test=(
            "Control Quality verifies against specification first, Validate Scope obtains acceptance "
            "second; the checklist separates procurement from administrative closure; SC-2 is reported NOT "
            "MET with its consequence quantified as a SGD 42,529 annual benefit shortfall; the final cost "
            "reconciles to SGD 478,900 with contingency closing at zero exposure; and every benefit B1 to "
            "B4 has a named owner who is not the project manager."
        ),
    ),
    dict(
        num=24,
        topic=6,
        title="Capstone - Integrated Project Management Plan and Mock Exam",
        objective="All domains - People, Process and Business Environment across the full ECO 2026 task list.",
        desc=(
            "Part A assembles twenty-three labs of artifacts into one integrated project management plan: "
            "a component index mapping all 25 components to the lab that produced each, the three "
            "baselines and the PMB accounted separately, and a twenty-assertion consistency audit. Part B "
            "is a 30-question mock practice exam in ECO 2026 format under a 40-minute timer, scored by "
            "domain against the published weights."
        ),
        build=(
            "artifacts/24-project-management-plan.md with the component index and twenty-assertion audit; "
            "artifacts/24-mock-exam-answers.md with all 30 answers recorded before the key was read; "
            "artifacts/24-score-analysis.md; artifacts/24-exam-readiness-plan.md with a dated plan for "
            "every domain below 70%."
        ),
        services="Project management plan index, Consistency audit, Mock practice exam, Score analysis",
        steps=[
            ("Build the plan index mapping all 25 components to the lab and artifact that produced each", ""),
            ("Account for the three baselines and the performance measurement baseline separately", ""),
            ("Run the twenty-assertion consistency audit and record every discrepancy found", ""),
            ("Prepare the five-minute executive presentation outline with timings per slide", ""),
            ("Sit the 30-question mock practice exam in ECO 2026 format under a 40-minute timer", ""),
            ("Score the mock practice exam by domain against the 33/41/26 weights", ""),
            ("Separate confident correct answers from flagged guesses and identify the weakest domain", ""),
            ("Write the remediation plan naming specific labs, ECO tasks, a dated action and a re-test date", ""),
            ("Complete the exam-day readiness checklist covering eligibility, pacing and answer selection", ""),
        ],
        test=(
            "The plan index accounts for the three baselines plus the PMB, and the learner explains why "
            "management reserve requires a baseline change while contingency does not; the audit PV sum "
            "comes to SGD 480,000 with at least one genuine discrepancy recorded; the mock exam was taken "
            "in 40 minutes without looking at the key; and per-domain scores are compared against 33%, "
            "41% and 26%."
        ),
    ),
]
