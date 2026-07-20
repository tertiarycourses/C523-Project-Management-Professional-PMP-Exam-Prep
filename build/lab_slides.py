"""
Lab activity slides — the bridge between the deck and the labs/ folder.

Each lab in labs_index.py gets one information-dense activity slide rendered
at the end of its topic, so the deck, the Lesson Plan, the Learner Guide and
the labs all reference the same lab number, title, ECO task, LO and duration.
"""
import layouts as X
import course_data as cd
from labs_index import BY_TOPIC
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

ACCENTS = [TEAL, BLUE, VIOLET, AMBER, CYAN, ROSE]

# Concrete, information-dense steps per lab. Each step is a real instruction,
# never a one-liner placeholder.
STEPS = {
1: ["Record your PMP eligibility route: degree plus 36 months leading projects, "
    "or diploma plus 60 months, and confirm the 35 contact hours this course supplies.",
    "Score yourself 1-5 on each of the three ECO domains — People, Process and "
    "Business Environment — to expose where your knowledge is thinnest.",
    "Weight your available study hours by the exam percentages: Process 41%, "
    "People 33%, Business Environment 26%.",
    "Block an eight-week study calendar with named topics per week, not vague "
    "'revision' entries.",
    "Schedule three full 180-question mock exams into that calendar, spaced at "
    "weeks 4, 6 and 8.",
    "Write down your target exam date and work backwards to confirm the plan is "
    "actually achievable."],
2: ["List the Contoso project's external drivers under each PESTLE heading: "
    "political, economic, socio-cultural, technological, legal, environmental.",
    "Open the Mind Mapping tool and branch each PESTLE factor into the specific "
    "effect it has on the training portal project.",
    "Repeat the scan using TECOP — technical, environmental, commercial, "
    "operational, political — and note which factors only TECOP surfaced.",
    "Rate every factor for likelihood and impact on a 1-5 scale, then rank them.",
    "Identify the three factors most likely to force a scope or schedule change.",
    "Write a one-paragraph environmental summary suitable for the project "
    "charter's assumptions and constraints section."],
3: ["Inventory the enterprise environmental factors constraining Contoso: "
    "existing systems, culture, staff capability, market and regulation.",
    "Inventory the organisational process assets available to reuse: templates, "
    "historical data, procurement rules, lessons learned.",
    "Classify each item explicitly as EEF or OPA and justify the classification "
    "in one line — this is a heavily examined distinction.",
    "Define the governance structure: who sponsors, who sits on the steering "
    "committee, and what the project manager may decide alone.",
    "Set numeric escalation thresholds for cost variance, schedule slip and risk "
    "severity, stating what triggers escalation to whom.",
    "Define the phase gates and the go / no-go criteria applied at each."],
4: ["Identify every compliance requirement touching the portal: data protection, "
    "accessibility, financial audit, and workplace health and safety.",
    "Classify each requirement into a compliance category and name its owner "
    "inside the organisation.",
    "Assess the consequence of non-compliance for each — financial penalty, "
    "reputational damage, or inability to launch.",
    "Add sustainability requirements: energy use of the hosting platform, "
    "e-waste from decommissioned hardware, and supplier sustainability criteria.",
    "Register the AI governance controls: where AI is used in the project, what "
    "data it consumes, and how its output is reviewed before acting on it.",
    "Define how compliance will be MEASURED, not merely asserted — the 2026 "
    "outline expects a metric."],
5: ["State the business problem in one sentence and the opportunity in one more.",
    "List three options including 'do nothing', with the cost and benefit of each.",
    "Build the cash-flow table: initial investment, annual benefit, and running "
    "net position across five years.",
    "Calculate payback period, NPV at a 6% discount rate, ROI and the "
    "benefit-cost ratio using the Statistics tool.",
    "Identify the non-financial benefits and state how each will be measured.",
    "Write the recommendation, naming the benefits owner accountable after the "
    "project closes."],
6: ["Draft the charter's purpose statement and its measurable success criteria "
    "— numbers, not adjectives.",
    "Record high-level requirements and explicitly list what is OUT of scope.",
    "Name the sponsor, project manager and key stakeholders, and state the "
    "authority delegated to the project manager.",
    "Add the summary milestone schedule and the high-level budget with its "
    "confidence range.",
    "Record assumptions, constraints and the top five high-level risks.",
    "Define the approval criteria and who signs the charter into effect."],
7: ["List every stakeholder affected by the portal upgrade, including those who "
    "merely believe they are affected.",
    "For each, record interest, influence, expectations and their current "
    "attitude toward the project.",
    "Plot all stakeholders on a power/interest grid and assign the four "
    "strategies: manage closely, keep satisfied, keep informed, monitor.",
    "Re-classify the top eight using the salience model — power, legitimacy and "
    "urgency — and note where it disagrees with the grid.",
    "Complete a SEAM recording Current (C) and Desired (D) engagement for each "
    "key stakeholder.",
    "Write the engagement action that moves each stakeholder from C to D, with "
    "an owner and a date."],
8: ["Draft the team's shared vision in a single sentence every member can repeat "
    "without reading it.",
    "Define roles and responsibilities so no member is unclear what they own.",
    "Agree working hours, core overlap for the distributed members, and expected "
    "response times.",
    "Set the ground rules: meeting norms, decision rules, and how disagreement "
    "is raised and settled.",
    "Define the Definition of Ready and Definition of Done the team will hold "
    "each other to.",
    "Agree the conflict protocol and the escalation path before any conflict "
    "actually occurs."],
9: ["Run a requirements elicitation session using the Mind Mapping tool, "
    "branching from the portal's core capabilities.",
    "Convert each branch into a numbered requirement written as a testable "
    "statement, not a wish.",
    "Classify each requirement as functional, non-functional, business, "
    "stakeholder, transition or quality.",
    "Build the Requirements Traceability Matrix linking requirement to business "
    "need, deliverable, test and acceptance criterion.",
    "Identify gaps: requirements with no test, and deliverables with no "
    "originating requirement.",
    "Have a nominated 'business owner' review and sign off the matrix."],
10: ["Take the requirements from Lab 09 and apply MoSCoW: Must, Should, Could, "
     "Won't have this release.",
     "Challenge the Musts — if more than 60% of effort is Must, the "
     "prioritisation has failed and must be redone.",
     "Apply Kano classification: basic, performance and delight features, and "
     "note which Musts are merely basic expectations.",
     "Write the top fifteen items as user stories in the standard 'As a… I "
     "want… so that…' form with acceptance criteria.",
     "Estimate each story in story points using relative sizing against a chosen "
     "reference story.",
     "Order the backlog by value per point and confirm the first sprint's "
     "capacity is realistic."],
11: ["Decompose the portal scope into major deliverables — not activities — at "
     "WBS level 2.",
     "Break each deliverable down until every work package is estimable and "
     "assignable, typically 8-80 hours.",
     "Apply the 100% rule: verify the children of every parent sum to exactly "
     "the parent's scope, no more and no less.",
     "Assign a unique WBS code identifier to every element.",
     "Write the WBS dictionary entry for five work packages: description, "
     "resources, cost, quality requirements and acceptance criteria.",
     "Assemble the scope baseline — scope statement plus WBS plus dictionary — "
     "and record who approves it."],
12: ["List the activities derived from the Lab 11 work packages with their "
     "durations.",
     "Determine each dependency and classify it as mandatory, discretionary, "
     "external or internal.",
     "Draw the precedence network using finish-to-start relationships, adding "
     "leads and lags where genuinely required.",
     "Apply three-point PERT estimating to the five most uncertain activities: "
     "(O + 4M + P) / 6, with sigma = (P − O) / 6.",
     "Run the forward and backward pass to compute early and late start and "
     "finish for every activity.",
     "Identify the critical path, state the project duration, and list the total "
     "and free float for every non-critical activity."],
13: ["Estimate each work package by the most defensible method — analogous, "
     "parametric or bottom-up — and record which you used and why.",
     "Apply three-point estimating to the packages with the widest uncertainty.",
     "Roll the estimates up through the WBS to a total direct cost.",
     "Calculate contingency reserve from the Lab 14 risk EMVs and add it to form "
     "the cost baseline.",
     "Add management reserve above the baseline and state who must approve its "
     "release.",
     "Plot the cumulative spend as an S-curve and identify the periods of "
     "highest cash demand."],
14: ["Build a risk breakdown structure grouping risks into technical, external, "
     "organisational and project-management categories.",
     "Identify at least fifteen risks, writing each in cause-event-effect form "
     "so the response is targetable.",
     "Score probability and impact on 1-5 scales and plot every risk on the "
     "probability/impact matrix.",
     "Use the System Thinking tool to map the reinforcing loops behind your top "
     "three risks — most schedule risk is systemic, not incidental.",
     "Build an EMV decision tree for the highest-value decision and calculate "
     "the expected monetary value of each branch.",
     "Assign a response strategy and a named owner to every red and amber risk, "
     "then note the secondary risks your responses create."],
15: ["List the Lab 11 work packages down the rows and the project roles across "
     "the columns.",
     "Open the RACI tool and assign Responsible, Accountable, Consulted and "
     "Informed for every work package.",
     "Verify exactly ONE Accountable per row — two accountable parties means "
     "nobody is accountable.",
     "Scan the columns for overload: a role Responsible for most rows is a "
     "single point of failure.",
     "Reduce excessive Consulted entries — over-consultation is the most common "
     "cause of decision latency.",
     "Review the matrix with the team and have each member confirm their "
     "assignments aloud."],
16: ["Assess which Tuckman stage the Contoso team is in, citing the observable "
     "behaviours that justify your diagnosis.",
     "State the leadership action appropriate to that stage rather than the one "
     "you personally prefer.",
     "Map each team member's dominant motivator using McClelland: achievement, "
     "affiliation or power.",
     "Apply Herzberg to separate hygiene complaints from genuine motivator gaps "
     "— they need different remedies.",
     "Design one specific intervention per team member, with a date and an "
     "observable success indicator.",
     "Define how you will detect regression to an earlier stage after the next "
     "team change."],
17: ["Read the conflict scenario and identify the true source: resources, "
     "priorities, technical opinion, or interpersonal style.",
     "Assess the conflict's position on Leas' five levels — the level dictates "
     "whether the team can still resolve it themselves.",
     "Role-play the conflict using each of the five modes in turn: collaborate, "
     "compromise, accommodate, force, avoid.",
     "Record what each mode produced and the relationship cost it incurred.",
     "Select the appropriate mode for this situation and justify it against the "
     "urgency and the relationship's importance.",
     "Write the agreed resolution, the ground rule that prevents recurrence, and "
     "how adherence will be monitored."],
18: ["List every stakeholder group from Lab 07 with the information each "
     "actually needs — not everything you have.",
     "Calculate the communication channels using N(N−1)/2 and state what the "
     "result implies for meeting design.",
     "Specify format, frequency, method and owner for each communication.",
     "Classify each as push, pull or interactive, and confirm anything requiring "
     "confirmed understanding is interactive.",
     "Draft a one-page status report tailored to the steering committee: "
     "exceptions and decisions needed, not raw activity.",
     "Draft the same status for the delivery team and note how radically the "
     "content differs for the same underlying facts."],
19: ["Open the Kanban tool and create columns matching Contoso's real workflow, "
     "including any waiting states.",
     "Populate the board with the current sprint's stories from Lab 10.",
     "Set explicit WIP limits per column based on team size, then observe what "
     "the limits block.",
     "Record the start and finish date of each item to measure lead time and "
     "cycle time.",
     "Identify the bottleneck column — where work queues rather than flows — and "
     "propose a specific intervention.",
     "Apply Little's Law to forecast delivery from your measured throughput "
     "rather than from optimism."],
20: ["Record the given Contoso data: BAC, and the PV, EV and AC at the reporting "
     "period.",
     "Calculate the variances: CV = EV − AC and SV = EV − PV, stating whether "
     "each is favourable.",
     "Calculate the indices: CPI = EV / AC and SPI = EV / PV, and interpret each "
     "against 1.0.",
     "Forecast the outcome: EAC = BAC / CPI, then ETC = EAC − AC and "
     "VAC = BAC − EAC.",
     "Calculate TCPI = (BAC − EV) / (BAC − AC) and state whether the required "
     "efficiency is realistically achievable.",
     "Decide between crashing and fast tracking to recover, quantifying the "
     "added cost or the added risk of your choice."],
21: ["Review the Contoso defect data and write the problem statement as a "
     "measurable gap, not an opinion.",
     "Open the 5 Whys tool and drill from the presenting symptom to a root cause "
     "you can actually act on.",
     "Open the Fishbone tool and group candidate causes under people, process, "
     "technology, environment, materials and measurement.",
     "Open the Pareto tool, enter the defect counts by category and identify the "
     "vital few driving roughly 80% of the defects.",
     "Compare what each tool surfaced — the three disagree, and the disagreement "
     "is the most useful output.",
     "Propose a countermeasure for the top two root causes, each with an owner, "
     "a date and a verification measure."],
22: ["Enter the twenty process measurements into the SPC tool and plot them in "
     "time order.",
     "Calculate the process mean and the upper and lower control limits.",
     "Identify any point falling outside the control limits and investigate it "
     "as an assignable cause.",
     "Apply the rule of seven: seven consecutive points on one side of the mean "
     "signals a non-random shift even inside the limits.",
     "Use the Statistics tool to compute mean, standard deviation and the "
     "distribution shape.",
     "State whether the process is in control, and separately whether it is "
     "acceptable — the two are different questions."],
23: ["Verify every deliverable against the acceptance criteria agreed in the "
     "charter and scope statement.",
     "Obtain and record formal stakeholder sign-off — informal agreement is not "
     "closure.",
     "Confirm transition readiness: documentation, training and support "
     "arrangements for the receiving team.",
     "Close all procurements, settle final payments and archive the contracts "
     "and financial records.",
     "Run the retrospective and write the lessons learned into the "
     "organisational repository, not just the project folder.",
     "Confirm the benefits measurement system is live and the benefits owner "
     "accepts accountability past project end."],
24: ["Consolidate every artifact from Labs 01-23 into one integrated project "
     "management plan with a contents page.",
     "Verify internal consistency: the WBS, schedule, budget, RACI and risk "
     "register must all describe the same project.",
     "Present the plan to the class as though to a steering committee, in ten "
     "minutes, defending your key trade-offs.",
     "Sit the full 180-question mock exam under timed conditions — 240 minutes, "
     "closed book, two breaks.",
     "Score the mock by ECO domain and compare against the 33/41/26 weighting to "
     "expose your weakest area.",
     "Rewrite your Lab 01 study plan using the mock results, naming the specific "
     "topics to revisit before booking the exam."],
}


def build_topic_labs(prs, topic_no, n):
    """Render the activity slides for one topic. Returns the next number."""
    labs = BY_TOPIC.get(topic_no, [])
    if not labs:
        return n

    # topic lab overview
    lab_cards = [(f"Lab {l['no']:02d}. {l['title']}",
                  f"{l['eco']} · {l['lo']} · {l['in_class']} min in class"
                  + (f" + {l['minutes'] - l['in_class']} min self-study"
                     if l["minutes"] > l["in_class"] else ""),
                  "Produces: " + ", ".join(l["outputs"])) for l in labs]
    # A topic with only two labs left half the canvas empty against its
    # sibling slides; pad the row with what those labs feed into.
    if len(labs) == 2:
        consumed = sorted({o for l in labs for o in l["outputs"]})
        lab_cards.append(
            ("Everything you have built",
             "These final labs consolidate the artifacts from Labs 01-22 into "
             "one integrated plan and an exam-readiness score.",
             "Consolidates: " + ", ".join(consumed[:4])))
    X.cards(prs, f"Hands-on Labs — Topic {topic_no}", lab_cards,
            n, kicker="WHAT YOU WILL BUILD", accent=TEAL,
            cols=3 if len(lab_cards) == 3 else (2 if len(labs) <= 4 else 3))
    n += 1

    for i, l in enumerate(labs):
        tool_name = url = None
        if l["tools"]:
            k = l["tools"][0]
            tool_name = cd.TOOLS[k][0]
            url = cd.TOOLS[k][1].replace("https://", "")
            if len(l["tools"]) > 1:
                tool_name = " + ".join(cd.TOOLS[t][0] for t in l["tools"][:2])
        brief = (f"Case study: Contoso Training Portal Upgrade. "
                 f"{l['eco']} · {l['lo']}. "
                 f"Produces {', '.join(l['outputs'])}.")
        X.activity(prs, f"Lab {l['no']:02d}. {l['title']}",
                   brief, STEPS.get(l["no"], []),
                   ", ".join(l["outputs"]), n,
                   tool=tool_name, url=url,
                   accent=ACCENTS[i % len(ACCENTS)],
                   duration=f"{l['in_class']} min in class")
        n += 1
    return n
