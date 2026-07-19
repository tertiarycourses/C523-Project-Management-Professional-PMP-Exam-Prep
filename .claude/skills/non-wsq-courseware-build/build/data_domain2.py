"""
Domain 2 - Start the Project. Hands-on activities for labs 05-08.

Each dict is one lab. `num` is the global contiguous lab number across all
domains; `topic` is the domain number (matches course_data TOPICS num). The
build engine renders one PPT activity + step slides, one Learner-Guide section
and one Lesson-Plan schedule entry per activity.
"""

DOMAIN2 = [
    dict(
        num=5,
        topic=2,
        title="Business Case and Cost-Benefit Analysis",
        objective="Process T3 - Help ensure value-based delivery; Process T6 - Plan and manage finance",
        desc=(
            "Turn the Contoso baseline metrics into a quantified benefits model, then build the cost side "
            "against the board-approved SGD 480,000 ceiling. Compute payback, NPV, ROI and benefit-cost "
            "ratio by hand, including the year-zero outflow most commonly dropped from NPV. Stress-test "
            "against the Lab 02 downside of an 8% fall in enrolment, then choose among options including a "
            "costed do-nothing."
        ),
        build=(
            "A quantified cost-benefit model with payback, NPV, ROI and BCR plus a downside sensitivity run "
            "(artifacts/05-cba-model.md), a written business case with a recommendation and its deciding "
            "measure (artifacts/05-business-case.md), and a benefits realisation map "
            "(artifacts/05-benefits-map.md)."
        ),
        services="Statistics, Spreadsheet",
        steps=[
            ("Quantify the benefits from the Lab 03 baseline metrics", ""),
            ("Build the cost side against the board-approved budget ceiling", ""),
            ("Compute payback period, NPV, ROI and benefit-cost ratio by hand", ""),
            ("Stress-test the case against the Lab 02 downside enrolment scenario", ""),
            ("Choose among the project options, including a costed do-nothing option", ""),
            ("Write the business case document with a recommendation", ""),
            ("Build the benefits realisation map for later closure measurement", ""),
            ("Answer the exam-style scenarios on value and sunk cost", ""),
        ],
        test=(
            "Every benefit line traces to a Lab 03 baseline metric; all discount factors fall below 1 and "
            "decrease with time; the NPV subtracts the year-zero investment; the BCR is total benefit over "
            "total cost and exceeds 1; the do-nothing option carries a negative number rather than a blank; "
            "and the recommendation cites NPV as the deciding measure."
        ),
    ),
    dict(
        num=6,
        topic=2,
        title="Project Charter",
        objective=(
            "Process T1 - Develop an integrated project management plan and plan delivery; "
            "Process T2 - Develop and manage project scope"
        ),
        desc=(
            "Assemble the governance model, compliance requirements and business-case financials into a "
            "charter that authorises the project. State success criteria each carrying a numeric baseline "
            "and target, and define scope boundaries including exclusions with traceable rationales. Name "
            "the PM's procurement and change-approval authority in figures matching the Lab 03 thresholds, "
            "and open the assumption log."
        ),
        build=(
            "A project charter with measurable success criteria, scope boundaries, exclusions, milestones, "
            "budget and PM authority (artifacts/06-project-charter.md), a development-approach decision "
            "(artifacts/06-approach-decision.md) and an assumption log with validation dates "
            "(artifacts/06-assumption-log.md)."
        ),
        services="Markdown editor, Spreadsheet",
        steps=[
            ("Assemble the charter inputs from the governance, compliance and business-case artifacts", ""),
            ("Write the charter header and the purpose statement", ""),
            ("State measurable success criteria with numeric baselines and targets", ""),
            ("Define scope boundaries, including exclusions and their rationale", ""),
            ("Record the high-level requirements, milestones and budget", ""),
            ("Name the project manager's authority in specific procurement and change-approval figures", ""),
            ("Document the hybrid development approach as a tailoring decision", ""),
            ("Build the assumption and constraint log with validation dates", ""),
            ("Answer the exam-style scenarios on charter authority and scope", ""),
        ],
        test=(
            "Every success criterion carries a numeric baseline and target; the charter has a sponsor "
            "signature block; every exclusion has a traceable rationale; the milestone list contains "
            "milestones only and no durations; the approach decision names what is predictive, what is "
            "adaptive and the interface between them; and every assumption has a validation date before "
            "being wrong becomes unrecoverable."
        ),
    ),
    dict(
        num=7,
        topic=2,
        title="Stakeholder Register, Power/Interest Grid and Salience Model",
        objective=(
            "People T4 - Engage stakeholders; People T5 - Align stakeholder expectations; "
            "People T6 - Manage stakeholder expectations"
        ),
        desc=(
            "Identify the full Contoso stakeholder set, including forgotten groups such as the three admin "
            "staff who are also subject matter experts. Analyse each on power, interest, attitude and "
            "impact, plot the power/interest grid and derive the strategy per quadrant. Where the grid "
            "fails, apply the salience model of power, legitimacy and urgency. Build the current-versus-"
            "desired engagement matrix and close each gap."
        ),
        build=(
            "A stakeholder register scored on power, interest, attitude and impact "
            "(artifacts/07-stakeholder-register.md), a power/interest grid "
            "(artifacts/07-power-interest-grid.md), a salience analysis (artifacts/07-salience-model.md) "
            "and an engagement matrix (artifacts/07-engagement-matrix.md)."
        ),
        services="Power/Interest Grid, Salience Model, Spreadsheet",
        steps=[
            ("Identify the full stakeholder set, including the groups projects habitually forget", ""),
            ("Build the stakeholder register with power, interest, attitude and impact", ""),
            ("Plot the power/interest grid and derive the strategy each quadrant demands", ""),
            ("Apply the salience model where the grid fails to give a usable answer", ""),
            ("Build the current-versus-desired engagement matrix", ""),
            ("Surface and plan to resolve the misaligned stakeholder expectations", ""),
            ("Set a tailored engagement cadence per stakeholder group", ""),
            ("Answer the exam-style scenarios on stakeholder engagement", ""),
        ],
        test=(
            "The register includes the three admin staff; every stakeholder has numeric power and interest "
            "scores matching their grid position; the salience analysis produced at least one insight the "
            "grid did not; every current-to-desired gap has an action with an owner and date; the "
            "expectation-conflict plan attaches a trade-off number; and the cadence differs by stakeholder "
            "rather than one fortnightly email for everyone."
        ),
    ),
    dict(
        num=8,
        topic=2,
        title="Team Charter, Ground Rules and Shared Vision",
        objective="People T1 - Develop a common vision; People T3 - Lead the project team",
        desc=(
            "Draft a shared vision short enough to recall without reading it, traced to the Lab 06 success "
            "criteria. Build the team charter: name all nine members, write the working agreement on core "
            "hours and time zones, and set ground rules across six categories, each with an observable "
            "violation test. Agree a definition of done separating done from released, and set the "
            "decision rule - consent, consensus or command."
        ),
        build=(
            "A vision statement traced to the charter success criteria "
            "(artifacts/08-vision-statement.md), a team charter with the working agreement, definition of "
            "done, decision-rule table and skills matrix (artifacts/08-team-charter.md), and six "
            "ground-rule categories (artifacts/08-ground-rules.md)."
        ),
        services="Team Charter, Definition of Done, Skills Matrix",
        steps=[
            ("Draft the shared vision statement and test it against the criteria", ""),
            ("Name the team and record each member's role", ""),
            ("Write the working agreement on core hours, time zones and availability", ""),
            ("Set ground rules across the six categories, each with an observable standard", ""),
            ("Agree the definition of done that QA and the developers will both accept", ""),
            ("Choose the decision-making rule for each class of decision and name the decider", ""),
            ("Build the skills and capacity matrix and expose the single points of failure", ""),
            ("Design the graduated response to ground-rule violations", ""),
            ("Forward-reference the responsibility assignment matrix and set the vision review cadence", ""),
            ("Answer the exam-style scenarios on team leadership and ground rules", ""),
        ],
        test=(
            "The vision is under 30 words and traces to at least two numbered charter success criteria; "
            "every ground rule has a violation test; the definition of done separates done from released; "
            "the decision table uses at least two rules and names a decider for every command-rule row; and "
            "the skills matrix identifies at least three single points of failure, each with a named owner "
            "and dated mitigation."
        ),
    ),
]
