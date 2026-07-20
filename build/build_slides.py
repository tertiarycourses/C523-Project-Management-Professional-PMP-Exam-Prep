"""
Assemble the full PMP 35 PDU deck.

    python3 build_slides.py

Front matter (cover + WSQ admin) -> Topic 1..6 -> back matter.
All content comes from course_data.py and the data_topicN.py modules.
"""
import importlib
import os
import sys
from pptx import Presentation
from pptx.util import Inches

import layouts as X
import course_data as cd
from layouts import BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE

OUT = f"../courseware/{cd.SHORT_TITLE}-{cd.VERSION}.pptx"

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)


def _asset(name):
    """Locate a logo: the course's own assets first, then the skill copies."""
    for p in (os.path.join(_REPO, "courseware/assets", name),
              os.path.join(_REPO, ".claude/skills/tertiary-course-slides/assets",
                           name)):
        if os.path.exists(p):
            return p
    return None


# ------------------------------------------------------------ front matter
def front(prs, n):
    X.cover(
        prs,
        cd.COURSE_TITLE,
        f"{cd.DAYS}-Day Instructor-Led Programme  ·  35 Contact Hours",
        [
            f"Version: {cd.VERSION}          Trainer: {cd.TRAINER}",
            f"Course Code: {cd.COURSE_CODE}",
            f"{cd.ORG}   ·   UEN {cd.UEN}",
            "Aligned to the PMI PMP Examination Content Outline — July 2026",
        ],
        logos=[_asset("tertiary-infotech-logo.png"),
               _asset("pmp-course-logo.png")],
    )
    n += 1

    X.cards(prs, "Ground Rules", [
        ("Phones on silent",
         "Take calls outside the room so the session is not disrupted for others."),
        ("Participate actively",
         "This course is built around labs and discussion — the more you contribute, "
         "the more you take away."),
        ("No question is too basic",
         "If something is unclear, ask. Others in the room almost certainly share the "
         "same question."),
        ("Punctuality after breaks",
         "Return on time so we can cover the full ECO syllabus within the four days."),
        ("Respect differing views",
         "Project management is contextual — disagreement is useful when handled with "
         "professional respect."),
        ("Confidentiality",
         "Workplace examples shared in class stay in the class; anonymise sensitive "
         "client or employer detail."),
    ], n, kicker="HOW WE WORK TOGETHER", accent=AMBER)
    n += 1

    # How you'll learn — the non-WSQ pedagogy block, in place of the
    # assessment/funding admin the WSQ counterpart carries here.
    X.process(prs, "How You'll Learn", [
        ("Demonstrate", "Each concept is introduced with a worked example on the "
                        "Contoso case study, not an abstract definition."),
        ("Build", "You produce the real artifact — charter, WBS, network diagram, "
                  "risk register, EVM analysis — by hand."),
        ("Verify", "Every lab states a success test so you can check your own work "
                   "before moving on."),
        ("Discuss", "We compare approaches as a group, because the exam rewards "
                    "contextual judgement over recall."),
        ("Recap", "Each day closes with a drill on the exam formats and formulas "
                  "covered that day."),
    ], n, kicker="THE LEARNING ARC", accent=CYAN,
        note="There is no assessment on this course. The mock practice exam in Lab 24 "
             "is a self-scored diagnostic that tells you where to study next.")
    n += 1

    # Course code + PDU orientation
    X.cards(prs, "About This Course", [
        ("Course Code", f"{cd.COURSE_CODE} — quote this on your PMI application as "
                        f"evidence of formal project management education."),
        ("35 contact hours", "This course satisfies the PMI education prerequisite of "
                             "35 contact hours for the PMP application."),
        ("ECO 2026 aligned", "Built against the PMI Examination Content Outline "
                             "effective July 2026, across all three domains."),
        ("Hybrid by design", "The case study is deliberately hybrid, because roughly "
                             "60% of exam items sit in adaptive or hybrid contexts."),
        ("24 hands-on labs", "One continuous project, worked end to end, producing a "
                             "complete set of artifacts you keep."),
        ("No assessment", "This is a commercial short course — there is no graded "
                          "assessment. Your Lab 24 mock score is your readiness signal."),
    ], n, kicker="ORIENTATION", accent=CYAN)
    n += 1

    # Learning outcomes
    X.cards(prs, "Learning Outcomes",
            [(lo, txt) for lo, txt in cd.LEARNING_OUTCOMES],
            n, kicker="BY THE END OF THIS COURSE YOU WILL BE ABLE TO", accent=TEAL,
            cols=2)
    n += 1

    # ECO 2026 orientation
    X.chart(prs, "The PMP Exam Content Outline — July 2026",
            "pie",
            [f"{d[1]} {d[2]}%" for d in cd.ECO_DOMAINS],
            [("Weighting", [d[2] for d in cd.ECO_DOMAINS])],
            n, kicker="WHAT THE EXAM ACTUALLY TESTS", accent=BLUE,
            insight=[
                "People 33% — leading, aligning and communicating with the team and stakeholders.",
                "Process 41% — planning, delivering, measuring and closing the work.",
                "Business Environment 26% — governance, compliance, risk and change. Up sharply from the old 8%.",
                "Approach mix: ~40% predictive, 60% adaptive/agile and hybrid.",
            ])
    n += 1

    X.cards(prs, "What Changed in the July 2026 Exam Update", [
        ("Business Environment tripled",
         "Weighting rises from 8% to 26% — governance, compliance and external change "
         "are now central, not peripheral."),
        ("People eased slightly",
         "From 42% to 33%, but the tasks are sharper: vision, conflict, expectations "
         "and knowledge transfer."),
        ("Process rebalanced",
         "From 50% to 41%, with new emphasis on value-based delivery and financial "
         "management."),
        ("Sustainability is examinable",
         "Named explicitly in compliance, quality (cost of quality) and risk response "
         "enablers."),
        ("Artificial intelligence enters scope",
         "The JTA validated AI as a trend affecting practice — expect it in estimation, "
         "reporting and governance items."),
        ("Graphic-based questions are new",
         "You will be asked to read charts, control charts and diagrams and answer from "
         "them — practise interpretation."),
    ], n, kicker="EXAM UPDATE", accent=ROSE)
    n += 1

    X.table(prs, "PMP Exam Format at a Glance",
            ["Element", "Detail", "What it means for you"],
            [
                ["Questions", f"{cd.ECO_EXAM['questions']} total "
                              f"({cd.ECO_EXAM['scored']} scored + {cd.ECO_EXAM['pretest']} pretest)",
                 "Unscored pretest items are indistinguishable — answer everything seriously."],
                ["Time", f"{cd.ECO_EXAM['minutes']} minutes (4 hours)",
                 "About 80 seconds per question — pace, do not linger."],
                ["Breaks", "Two 10-minute breaks",
                 "First after the case-study section, second midway through the rest."],
                ["Section lock", "No return after a break",
                 "Review your answers BEFORE you start a break."],
                ["Approach mix", cd.ECO_EXAM["approach_mix"],
                 "You cannot pass on waterfall knowledge alone."],
                ["Delivery", "Test centre or online proctored",
                 "Case study questions are available on all modalities."],
            ], n, kicker="EXAM MECHANICS", accent=VIOLET,
            widths=[2, 3.2, 4.2])
    n += 1

    X.cards(prs, "PMP Exam Question Types",
            [(t, d) for t, d in cd.ECO_EXAM["question_types"]],
            n, kicker="SIX FORMATS YOU WILL MEET", accent=AMBER)
    n += 1

    # Course outline (2 slides)
    X.cards(prs, "Course Outline — Topics 1 to 3",
            [(f"Topic {t[0]}. {t[1]}", t[2],
              " · ".join(t[4][:3])) for t in cd.TOPICS[:3]],
            n, kicker="WHERE WE ARE GOING", accent=BLUE)
    n += 1
    X.cards(prs, "Course Outline — Topics 4 to 6",
            [(f"Topic {t[0]}. {t[1]}", t[2],
              " · ".join(t[4][:3])) for t in cd.TOPICS[3:]],
            n, kicker="WHERE WE ARE GOING", accent=TEAL)
    n += 1

    # Day plan
    X.timeline(prs, "The Four Days",
               [(f"Day {d}", f"{title}\n{labs}") for d, title, _t, labs in cd.DAY_PLAN],
               n, kicker="LESSON PLAN", accent=CYAN,
               note="Each day runs 9:30am–6:30pm with a one-hour lunch break and two tea "
                    "breaks. Roughly half of each day is hands-on lab work.")
    n += 1

    for day, title, topics, labs in cd.DAY_PLAN:
        X.table(prs, f"Lesson Plan — Day {day}: {title}",
                ["Time", "Session", "Activity"],
                _day_rows(day, topics, labs), n,
                kicker=f"DAY {day} SCHEDULE", accent=X.ACCENTS[day % 6],
                widths=[1.5, 3.5, 5])
        n += 1

    X.cards(prs, "How to Get the Most From These Four Days", [
        ("Work the arithmetic by hand",
         "The exam gives you no spreadsheet. Do the PERT, EVM and EMV calculations "
         "manually until they are automatic."),
        ("Identify the approach first",
         "Before answering anything, decide whether the scenario is predictive, "
         "adaptive or hybrid — it changes the correct answer."),
        ("Keep every artifact",
         "Each lab feeds the next. By Lab 24 they assemble into one integrated plan "
         "you can reuse at work."),
        ("Ask about your own projects",
         "The most valuable discussions come from real situations in the room — "
         "bring them."),
        ("Track your weak domains",
         "Note which topics you find hardest; the Lab 24 score analysis will confirm "
         "them and set your study order."),
        ("Book the exam deliberately",
         "Sit it while the material is fresh, but only once your mock scores are "
         "consistently above target."),
    ], n, kicker="STUDY STRATEGY", accent=AMBER)
    n += 1

    return n


def _day_rows(day, topics, labs):
    """Day schedule for the deck — read from the SAME source the Lesson Plan
    uses, so the two can never disagree.

    This previously carried its own hardcoded timetable, which drifted: it
    collapsed the 3-hour Day 4 assessment into a single 45-minute row and
    omitted the Briefing entirely, contradicting the Lesson Plan and three
    other slides in this deck.
    """
    import build_lesson_plan as blp
    return [[time, session, activity]
            for time, session, activity, _mins, _kind in blp.day_rows(day)]


# ------------------------------------------------------------- back matter
def back(prs, n):
    X.cards(prs, "Your Next 90 Days", [
        ("Submit the PMI application",
         "Use this course for the 35 contact hours; document your project experience "
         "against the eligibility rules."),
        ("Build a study schedule",
         "Plan 8–10 weeks of study, weighting your time by the domain percentages: "
         "Process 41%, People 33%, Business Environment 26%."),
        ("Practise by question type",
         "Drill the new graphic-based and case-study formats, not just multiple choice."),
        ("Re-run the labs at work",
         "Apply the charter, WBS, EVM and control-chart labs to a live project to "
         "consolidate the learning."),
        ("Take full mock exams",
         "Sit at least three timed 180-question mocks under exam conditions before "
         "booking."),
        ("Maintain your certification",
         "The CCR programme requires 60 PDUs every three years once you are certified."),
    ], n, kicker="AFTER THE COURSE", accent=TEAL)
    n += 1

    X.cards(prs, "Recommended Courses", [
        ("Fundamentals of Microsoft Project",
         "Build and control real schedules, baselines and resource plans in MS Project."),
        ("Effective Project Management for Small Projects",
         "A lighter-weight toolkit for projects that do not warrant full PMP rigour."),
        ("Certified Lean Six Sigma Green Belt",
         "Go deeper on DMAIC, SPC and the statistical quality tools introduced here."),
        ("Agile Project Management with Scrum",
         "Extend the adaptive content into full Scrum practice and certification."),
        ("Business Analysis Fundamentals",
         "Strengthen requirements elicitation, traceability and stakeholder analysis."),
        ("Data Analytics for Managers",
         "Turn project and operational data into the metrics your governance board wants."),
    ], n, kicker="CONTINUE YOUR PATHWAY", accent=VIOLET)
    n += 1

    X.cards(prs, "Support", [
        ("Email", "enquiry@tertiaryinfotech.com — for course and certificate queries."),
        ("Telephone", "6100 0613 — office hours, Monday to Friday."),
        ("Course materials", "Slides, Learner Guide and the full lab set are shared "
                             "with you for continued reference."),
        ("Problem-solving tools", "The live 5 Whys, Fishbone, Pareto, SPC and Statistics "
                                  "tools stay available to you after the course."),
        ("PMI application", "Quote this course for the 35 contact hours of project "
                            "management education PMI requires."),
        ("Keep practising", "Re-run the labs on a live project — applied repetition is "
                            "what converts these techniques into exam speed."),
    ], n, kicker="WE ARE HERE TO HELP", accent=CYAN)
    n += 1

    X.statement(prs, "Thank You", "Now go and pass the exam.",
                [("35 contact hours earned", "You have the project management education "
                                             "PMI requires for the application."),
                 ("24 labs completed", "You leave with a full set of working project "
                                       "artifacts."),
                 ("ECO 2026 covered", "Every domain and task on the July 2026 outline "
                                      "has been taught.")],
                n, kicker="END OF COURSE", accent=BLUE)
    n += 1
    return n


# -------------------------------------------------------------------- main
def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    n = 1
    n = front(prs, n)
    front_end = n - 1

    import lab_slides

    counts = {}
    for t in range(1, 7):
        mod = importlib.import_module(f"data_topic{t}")
        start = n
        n = mod.build(prs, n)
        # the topic's hands-on labs, rendered from the shared labs_index
        n = lab_slides.build_topic_labs(prs, t, n)
        counts[t] = n - start

    topics_end = n - 1
    n = back(prs, n)

    prs.save(OUT)

    total = n - 1
    print(f"front matter : {front_end}")
    for t, c in counts.items():
        print(f"topic {t}      : {c}")
    print(f"back matter  : {total - topics_end}")
    print(f"TOTAL SLIDES : {total}")
    print(f"saved -> {OUT}")
    return total


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
