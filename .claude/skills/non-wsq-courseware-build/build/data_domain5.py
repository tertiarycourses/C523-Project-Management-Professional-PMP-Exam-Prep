"""
Domain 5 - Monitor and Control the Project.

Per-domain hands-on activities (single source of the labs). Each dict maps to
one labs/lab-NN-*.md file. `num` is the GLOBAL contiguous lab number; `topic`
is the domain number (5).
"""

DOMAIN5 = [
    dict(
        num=19,
        topic=5,
        title="Kanban Board with WIP Limits and Lead/Cycle Time",
        objective="Process T9 - Evaluate project status; Business Environment T4 - Remove impediments and manage issues.",
        desc=(
            "Build a nine-column Kanban board mirroring Contoso's workflow, separating active from queue "
            "columns so waiting time becomes visible. Set a justified WIP limit per column, load 18 story "
            "cards with backlog-entry, work-start and acceptance dates, and compute lead time, cycle time, "
            "throughput and flow efficiency. Apply Little's Law, then find the bottleneck and apply the "
            "five Theory of Constraints steps."
        ),
        build=(
            "artifacts/19-kanban-board.md with the nine-column workflow and WIP limits; "
            "artifacts/19-flow-metrics.md with lead and cycle time, throughput, flow efficiency and the "
            "Little's Law verification; artifacts/19-bottleneck-analysis.md with the utilisation table and "
            "Theory of Constraints response."
        ),
        services="Kanban Board",
        steps=[
            ("Design the workflow columns, separating active stages from queue stages", ""),
            ("Set and justify a WIP limit for every column against the team composition", ""),
            ("Load the 18 real cards with backlog-entry, work-start and acceptance dates", ""),
            ("Compute the flow metrics - lead time, cycle time, throughput and flow efficiency", ""),
            ("Apply Little's Law to verify stability and forecast the remaining release", ""),
            ("Find the bottleneck from column utilisation and apply the Theory of Constraints steps", ""),
            ("Read the cumulative flow diagram and interpret band width, slope and convergence", ""),
            ("Answer the exam-style scenarios on Little's Law, WIP limits and lead versus cycle time", ""),
        ],
        test=(
            "Mean lead time comes to 13.11 days against a mean cycle time of 6.94 days, a flow efficiency "
            "of 52.9%; Little's Law implies a WIP of about 6.25 against an observed 6 on day 12; Test is "
            "the bottleneck on its 100% utilisation, the 97% queue in front of it and the collapse to 33% "
            "downstream; and the learner rejects raising the In Test WIP limit, explaining why it would "
            "lengthen cycle time."
        ),
    ),
    dict(
        num=20,
        topic=5,
        title="Earned Value Management and Schedule Compression",
        objective="Process T9 - Evaluate project status; Process T6 - Plan and manage budget and resources.",
        desc=(
            "From the SGD 480,000 Contoso cost baseline, validate that cumulative planned value at the "
            "final period equals BAC, then compute CV, SV, CPI and SPI at the week-14 status date. "
            "Calculate all three EAC variants, choose the defensible one on evidence, and derive ETC, VAC "
            "and both TCPI figures. Analyse the seven-period CPI/SPI trend and choose between crashing and "
            "fast-tracking from the crash-cost table."
        ),
        build=(
            "artifacts/20-evm-calculations.md with CV, SV, CPI and SPI plus the seven-period trend table; "
            "artifacts/20-forecast.md with all three EAC variants, ETC, VAC and both TCPI figures; "
            "artifacts/20-compression-decision.md with the five-day crash recovery, its cost and the "
            "rejection of fast-tracking."
        ),
        services="Statistics",
        steps=[
            ("Take the cost baseline and actuals, and validate that cumulative PV equals BAC", ""),
            ("Compute the variances and indices at week 14 - CV, SV, CPI and SPI", ""),
            ("Forecast the outcome with all three EAC variants, plus ETC, VAC and TCPI", ""),
            ("Analyse the seven-period CPI/SPI trend rather than the single snapshot", ""),
            ("Check the result against the escalation thresholds and decide whether to escalate", ""),
            ("Decide between crashing and fast-tracking using the crash-cost table", ""),
            ("Write the variance report in sponsor format with three costed options and a recommendation", ""),
            ("Answer the exam-style scenarios on EAC selection, EVM reading and trend interpretation", ""),
        ],
        test=(
            "Cumulative PV at period 12 equals SGD 480,000; CV = -22,000 and SV = -19,000 are in dollars "
            "not days; CPI = 0.919 and SPI = 0.929, CPI carried to four decimals into EAC = SGD 522,420 "
            "and VAC = -SGD 42,420; the TCPI of 1.105 against CPI 0.919 makes recovery not credible; the "
            "crash selects J and O for SGD 15,500, rejecting non-critical F; and escalation is raised on "
            "the forecast, not the actual variance."
        ),
    ),
    dict(
        num=21,
        topic=5,
        title="Root Cause Analysis with 5 Whys, Fishbone and Pareto",
        objective=(
            "Business Environment T4 - Remove impediments and manage issues; Process T7 - Plan and manage quality "
            "of products and deliverables; Business Environment T6 - Support continuous improvement."
        ),
        desc=(
            "Take the defect log for sprints 1 to 7 - the period over which CPI declined monotonically - "
            "and run the three root cause tools in sequence. Pareto on defect frequency isolates the vital "
            "few inside the 80% cut; a second Pareto by rework hours reveals where frequency and cost "
            "disagree. A fishbone generates causes across the six categories, and 5 Whys drives from "
            "symptom to root cause, verified with the removal test."
        ),
        build=(
            "artifacts/21-pareto-analysis.md with the frequency and cost rankings and cumulative "
            "percentages; artifacts/21-fishbone.md with two causes per category; artifacts/21-5whys.md "
            "with the causal chain; artifacts/21-corrective-actions.md separating corrective from "
            "preventive action."
        ),
        services="Pareto Chart, Fishbone Diagram, 5 Whys",
        steps=[
            ("Take the defect data covering sprints 1 to 7 with counts, rework hours and cost", ""),
            ("Build the Pareto chart on defect frequency and locate the 80% cut", ""),
            ("Re-run Pareto by rework cost and notice where the two rankings disagree", ""),
            ("Fishbone the top category across all six cause categories", ""),
            ("Drive from symptom to root cause with 5 Whys", ""),
            ("Verify the root cause with the therefore test and the removal test before acting", ""),
            ("Design corrective, preventive and defect-repair actions and assign owners", ""),
            ("Answer the exam-style scenarios on root cause versus symptom and action type", ""),
        ],
        test=(
            "Cumulative percentages reach 100% with the 80% cut at rank 5 on 81.55%; both Pareto runs rank "
            "acceptance criteria and browser compatibility first and second; every fishbone category "
            "carries two causes; the root cause is a system or process failure rather than an individual's "
            "shortcoming and passes the removal test; and the causal chain connects it back to the CPI "
            "decline found by earned value analysis."
        ),
    ),
    dict(
        num=22,
        topic=5,
        title="SPC Control Chart and Statistical Process Analysis",
        objective="Process T7 - Plan and manage quality of products and deliverables; Process T9 - Evaluate project status.",
        desc=(
            "Plot 20 daily measurements of median registration completion time and compute the centre line "
            "and control limits from the data itself, using the moving-range method rather than the sample "
            "standard deviation. Apply the out-of-control rules including the rule of seven and identify "
            "where the process shifts. Separate common from assignable cause, then assess capability - the "
            "process is in control yet fails specification."
        ),
        build=(
            "artifacts/22-control-chart.md with the individuals chart, centre line and control limits; "
            "artifacts/22-stability-verdict.md with the rule-by-rule out-of-control analysis and the named "
            "assignable cause; artifacts/22-capability-summary.md with the capability indices against the "
            "charter target."
        ),
        services="SPC / Control Chart, Statistics",
        steps=[
            ("Take the 20 daily measurements of median registration completion time", ""),
            ("Compute the centre line and control limits from the moving ranges", ""),
            ("Plot the individuals chart against the computed limits", ""),
            ("Apply the out-of-control rules, including the rule of seven, run by run", ""),
            ("Separate common cause from assignable cause and decide the response to each", ""),
            ("Assess capability against the charter success criterion and distinguish control from specification limits", ""),
            ("Write the quality verdict and the corrective actions", ""),
            ("Answer the exam-style scenarios on tampering, signals and capability", ""),
        ],
        test=(
            "The centre line comes to 4.053 with MR-bar 0.3286, sigma 0.2913 and limits of 3.179 and "
            "4.927, computed from the stable period not all 20 points; sigma is MR-bar divided by 1.128; "
            "the rule of seven is checked on days 1 to 15, longest run 2; days 16 to 20 are assignable "
            "cause with a dated explanation matching the shift; and the negative Cpk leads to re-centring "
            "rather than tightening."
        ),
    ),
]
