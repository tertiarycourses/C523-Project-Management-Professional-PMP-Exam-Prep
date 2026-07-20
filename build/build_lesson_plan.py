#!/usr/bin/env python3
"""
Generate the WSQ Lesson Plan DOCX for the PMP 35 PDU course.

Single source of truth is course_data.py, so the Lesson Plan cannot drift
from the slides, Learner Guide or labs.

Each of the four days totals exactly 480 instructional minutes (8 hours),
excluding the 1-hour lunch break.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SKILL = os.path.join(REPO, ".claude/skills/tertiary-lesson-plan")
sys.path.insert(0, HERE)
sys.path.insert(0, SKILL)

import prodoc  # noqa: E402  (from the tertiary-lesson-plan skill)
import course_data as cd  # noqa: E402
from labs_index import (LABS, total_minutes, in_class_minutes,  # noqa: E402
                        self_study_minutes,
                        LAB_MINUTES_PER_DAY as LAB_MIN_PER_DAY)

from docx import Document  # noqa: E402
from docx.shared import Pt, RGBColor, Inches  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK  # noqa: E402
from docx.enum.table import WD_TABLE_ALIGNMENT  # noqa: E402

BRAND = RGBColor(0x1F, 0x6F, 0xEB)
DARK = RGBColor(0x16, 0x1B, 0x26)
GREY = RGBColor(0x5B, 0x63, 0x72)
HEADER_FILL = "1F6FEB"
TOPIC_FILL = "E8F0FE"
BREAK_FILL = "FFF4E5"
LAB_FILL = "E8F8F1"

# Read from the single source so the record can never drift from the cover.
VERSIONS = [(v, d, summary, author) for v, d, summary, author in cd.VERSION_HISTORY]


def _logo(name):
    for p in (os.path.join(REPO, "courseware/assets", name),
              os.path.join(SKILL, "assets", name),
              os.path.join(REPO, ".claude/skills/tertiary-course-slides/assets", name)):
        if os.path.exists(p):
            return p
    return None


def _shade(cell, hexc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hexc)
    cell._tc.get_or_add_tcPr().append(el)


def _cell(cell, text, size=9.5, bold=False, color=DARK, fill=None):
    cell.text = ""
    r = cell.paragraphs[0].add_run(str(text))
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.name = "Arial"
    r.font.color.rgb = color
    if fill:
        _shade(cell, fill)


def h1(doc, text):
    doc.add_heading(text, level=1)


def h2(doc, text):
    doc.add_heading(text, level=2)


def para(doc, text, size=11, bold=False, color=DARK, after=6):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.name = "Arial"
    r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(after)
    return p


def bullet(doc, text, size=11):
    p = doc.add_paragraph(style="List Bullet")
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.name = "Arial"
    return p


def schedule_table(doc, rows):
    """rows: (time, session, activity, minutes, kind)."""
    t = doc.add_table(rows=0, cols=4)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.add_row().cells
    for i, htxt in enumerate(["Time", "Topic / Session", "Activity", "Duration"]):
        _cell(hdr[i], htxt, 9.5, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    total = 0
    for time, session, activity, mins, kind in rows:
        fill = {"topic": TOPIC_FILL, "break": BREAK_FILL,
                "lab": LAB_FILL}.get(kind)
        c = t.add_row().cells
        _cell(c[0], time, 9, fill=fill)
        _cell(c[1], session, 9, bold=(kind == "topic"), fill=fill)
        _cell(c[2], activity, 9, color=GREY, fill=fill)
        _cell(c[3], f"{mins} min" if mins else "—", 9, fill=fill)
        if kind != "lunch":
            total += mins
    for w, i in ((Inches(1.15), 0), (Inches(2.35), 1),
                 (Inches(2.75), 2), (Inches(0.75), 3)):
        for row in t.rows:
            row.cells[i].width = w
    return total


# ------------------------------------------------------------ day schedules
def day_rows(day):
    """Build the row list for a day. Must total 480 instructional minutes."""
    labs = [l for l in LABS if l["day"] == day]
    topics = [t for d, _, ts, _ in cd.DAY_PLAN if d == day for t in ts]
    tnames = [f"Topic {t}. {cd.TOPICS[t-1][1]}" for t in topics]
    first = tnames[0]
    last = tnames[-1]

    # expand ranges like "LO1-LO5" so the label never reads "LO1-LO5, LO5"
    _los = set()
    for l in labs:
        for part in str(l["lo"]).split(","):
            part = part.strip()
            if "-" in part:
                a, b = part.split("-", 1)
                try:
                    _los.update(f"LO{i}" for i in
                                range(int(a.strip()[2:]), int(b.strip()[2:]) + 1))
                    continue
                except ValueError:
                    pass
            if part:
                _los.add(part)
    lab_lo = ", ".join(sorted(_los)) if _los else "—"
    lab_a = ", ".join(f"Lab {l['no']:02d}" for l in labs[:len(labs)//2]) or "—"
    lab_b = ", ".join(f"Lab {l['no']:02d}" for l in labs[len(labs)//2:]) or "—"

    if day == 1:
        opening = ("Course introduction, trainer and learner introductions, "
                   "ground rules, learning outcomes, ECO 2026 orientation")
    else:
        opening = f"Recap of Day {day-1}, exam-style warm-up questions and Q&A"

    if day == 4:
        # Non-WSQ: there is no assessment. The 3 hours the WSQ counterpart
        # spends on the WA and Case Study are reallocated to the capstone lab,
        # exam strategy and the mock-exam debrief.
        return [
            ("9:30 – 9:45", "Day 4 Opening", opening, 15, "admin"),
            ("9:45 – 11:00", first,
             "Concept delivery: closure, benefits realisation, knowledge transfer",
             75, "topic"),
            ("11:00 – 11:15", "Tea Break", "—", 15, "break"),
            ("11:15 – 13:00", "Hands-on Labs",
             f"{lab_a or 'Lab 23'} ({lab_lo})", 105, "lab"),
            ("13:00 – 14:00", "Lunch Break", "—", 60, "lunch"),
            ("14:00 – 15:45", "Capstone Lab",
             f"{lab_b or 'Lab 24'} Part A — consolidate all 23 labs' artifacts into "
             "one integrated project management plan with a consistency audit",
             105, "lab"),
            ("15:45 – 16:00", "Tea Break", "—", 15, "break"),
            ("16:00 – 17:10", "Mock Practice Exam",
             "Lab 24 Part B — 30-question ECO 2026-format mock exam under timed "
             "conditions (self-scored, not an assessment)", 70, "lab"),
            ("17:10 – 18:00", "Mock Exam Debrief",
             "Score by domain against the 33/41/26 weights, work the rationale for "
             "every wrong answer, and build a dated remediation plan", 50, "topic"),
            ("18:00 – 18:30", "Exam Strategy & Course Close",
             "PMI application steps, study plan, exam-day tactics and Q&A",
             30, "admin"),
        ]

    return [
        ("9:30 – 10:00", "Registration & Course Opening", opening, 30, "admin"),
        ("10:00 – 11:15", first, "Concept delivery, worked examples and discussion", 75, "topic"),
        ("11:15 – 11:30", "Tea Break", "—", 15, "break"),
        ("11:30 – 13:00", last, "Concept delivery, worked examples and discussion", 90, "topic"),
        ("13:00 – 14:00", "Lunch Break", "—", 60, "lunch"),
        ("14:00 – 15:45", "Hands-on Labs", f"{lab_a} ({lab_lo})", 105, "lab"),
        ("15:45 – 16:00", "Tea Break", "—", 15, "break"),
        ("16:00 – 17:30", "Hands-on Labs (continued)", f"{lab_b} — group share-back", 90, "lab"),
        ("17:30 – 18:30", "Consolidation",
         "Exam-style question drill on the day's material, recap and Q&A",
         60, "admin"),
    ]


def main():
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)
    prodoc.style_headings(doc)

    prodoc.add_cover_page(
        doc, "LESSON PLAN", cd.COURSE_TITLE, cd.VERSION,
        org_logo=_logo("tertiary-infotech-logo.png"),
        course_logo=_logo("pmp-course-logo.png"),
        course_code=cd.COURSE_CODE)
    prodoc.add_version_control(doc, VERSIONS)
    prodoc.add_toc(doc)

    # ---------------------------------------------------------- overview
    h1(doc, "Course Overview")
    para(doc, f"{cd.COURSE_TITLE} is a {cd.DAYS}-day, "
              f"{cd.DAYS * cd.HOURS_PER_DAY}-hour instructor-led programme "
              f"delivering the 35 contact hours required for the PMI Project "
              f"Management Professional (PMP)® application.")
    para(doc, "The course is fully aligned to the PMI PMP Examination Content "
              "Outline published for the July 2026 exam update. That update "
              "rebalanced the exam domains and introduced sustainability and "
              "artificial intelligence as examinable considerations:")
    for _, name, pct, blurb in cd.ECO_DOMAINS:
        bullet(doc, f"Domain {name} — {pct}% of exam items. {blurb}")
    para(doc, f"Approach coverage: {cd.ECO_EXAM['approach_mix']}", after=10)

    h2(doc, "Target Audience")
    for a in ["Project managers and project leads responsible for medium-scale projects",
              "Team leads, engineers and analysts moving into project management",
              "PMO staff, business analysts and consultants supporting project delivery",
              "Candidates preparing to sit the PMP certification examination"]:
        bullet(doc, a)

    h2(doc, "Prerequisites")
    for a in ["Working familiarity with a project environment, in any industry",
              "No prior PMP study is assumed; all concepts are taught from first principles",
              "A laptop with a spreadsheet application and a modern web browser"]:
        bullet(doc, a)

    h2(doc, "Course Details")
    t = doc.add_table(rows=0, cols=2)
    t.style = "Table Grid"
    for k, v in [("Course Reference", cd.COURSE_CODE),
                 ("Trainer", cd.TRAINER),
                 ("Training Provider", f"{cd.ORG} (UEN {cd.UEN})"),
                 ("Duration", f"{cd.DAYS} days / {cd.DAYS * cd.HOURS_PER_DAY} hours"),
                 ("PDU Value", "35 PDUs / contact hours")]:
        c = t.add_row().cells
        _cell(c[0], k, 10, bold=True, fill=TOPIC_FILL)
        _cell(c[1], v, 10)

    # --------------------------------------------------- learning outcomes
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Learning Outcomes")
    para(doc, "By the end of this course, learners will be able to:")
    t = doc.add_table(rows=0, cols=3)
    t.style = "Table Grid"
    hdr = t.add_row().cells
    for i, htxt in enumerate(["Ref", "Learning Outcome", "Reinforced by"]):
        _cell(hdr[i], htxt, 9.5, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    # Non-WSQ: there is no assessment. Each outcome is reinforced through the
    # hands-on labs that produce its artifacts, and confirmed by the learner's
    # own Lab 24 mock-exam domain score.
    reinforced = {
        "LO1": "Labs 02–06, 09–11 — environment scan, business case, charter, "
               "requirements traceability and WBS",
        "LO2": "Labs 11–13, 15, 20 — WBS, critical path with PERT, cost baseline "
               "with reserves, resource plan and schedule compression",
        "LO3": "Labs 08, 16, 17, 21 — team charter, Tuckman diagnosis, conflict "
               "role-play and root cause analysis",
        "LO4": "Labs 04, 07, 14, 18 — compliance register, stakeholder analysis, "
               "risk register with EMV and the communication plan",
        "LO5": "Labs 19, 20, 22, 23 — flow metrics, earned value, control charts, "
               "closure and benefits realisation",
    }
    for lo, txt in cd.LEARNING_OUTCOMES:
        c = t.add_row().cells
        _cell(c[0], lo, 9.5, bold=True, fill=TOPIC_FILL)
        _cell(c[1], txt, 9.5)
        _cell(c[2], reinforced.get(lo, "Hands-on labs"), 9, color=GREY)

    # ------------------------------------------------------- ECO coverage
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Examination Content Outline Coverage")
    para(doc, "Every task in the July 2026 Examination Content Outline is "
              "delivered within one of the six course topics. The mapping below "
              "is the coverage evidence for that claim.")
    t = doc.add_table(rows=0, cols=3)
    t.style = "Table Grid"
    hdr = t.add_row().cells
    for i, htxt in enumerate(["Topic", "ECO Domain & Tasks Delivered", "Day"]):
        _cell(hdr[i], htxt, 9.5, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    day_of = {t: d for d, _, ts, _ in cd.DAY_PLAN for t in ts}
    for no, name, _blurb, ecos, _subs in cd.TOPICS:
        tasks = "; ".join(
            f"{dom} T{tn}: " +
            next(s for n2, s, _ in cd.ECO_TASKS[dom] if n2 == tn)
            for dom, tn in ecos)
        c = t.add_row().cells
        _cell(c[0], f"Topic {no}. {name}", 9, bold=True, fill=TOPIC_FILL)
        _cell(c[1], tasks, 8.5, color=GREY)
        _cell(c[2], f"Day {day_of[no]}", 9)

    # ----------------------------------------------------- daily schedules
    for day, title, topics, _labs in cd.DAY_PLAN:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        h1(doc, f"Day {day}: {title}")
        tnames = ", ".join(f"Topic {t}. {cd.TOPICS[t-1][1]}" for t in topics)
        para(doc, f"Topics covered: {tnames}", bold=True)
        daylabs = [l for l in LABS if l["day"] == day]
        if daylabs:
            para(doc, "Hands-on labs: " + ", ".join(
                f"Lab {l['no']:02d} {l['title']}" for l in daylabs),
                size=10, color=GREY)
        rows = day_rows(day)
        total = schedule_table(doc, rows)
        assert total == 480, f"Day {day} totals {total} minutes, expected 480"
        para(doc, f"Total instructional time: {total} minutes "
                  f"({total // 60} hours), excluding the 1-hour lunch break.",
             size=9.5, color=GREY, after=2)

    # -------------------------------------------------------------- labs
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Hands-on Laboratory Schedule")
    para(doc, f"The course includes {len(LABS)} hands-on labs built around a "
              f"single running case study, the Contoso Training Portal Upgrade. "
              f"Each lab consumes artifacts produced by earlier labs, so the set "
              f"forms one continuous project.")
    _per_day = ", ".join(f"Day {d} {m}" for d, m in
                         sorted(LAB_MIN_PER_DAY.items()))
    para(doc, f"Each lab is timetabled for its core steps in class "
              f"({in_class_minutes()} minutes across the four days — "
              f"{_per_day}). The extension steps — a "
              f"further {self_study_minutes()} minutes — are completed as "
              f"self-study after the session, so learners leave with a complete "
              f"set of project artifacts.", size=10, color=GREY)
    t = doc.add_table(rows=0, cols=7)
    t.style = "Table Grid"
    hdr = t.add_row().cells
    for i, htxt in enumerate(["Lab", "Title", "Topic", "ECO Task", "LO",
                              "In class", "Self-study"]):
        _cell(hdr[i], htxt, 9, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    for l in LABS:
        c = t.add_row().cells
        _cell(c[0], f"{l['no']:02d}", 8.5, bold=True, fill=LAB_FILL)
        _cell(c[1], l["title"], 8.5)
        _cell(c[2], f"T{l['topic']}", 8.5, color=GREY)
        _cell(c[3], l["eco"], 8, color=GREY)
        _cell(c[4], l["lo"], 8.5, color=GREY)
        _cell(c[5], f"{l['in_class']} min", 8.5, color=GREY)
        _cell(c[6], f"{l['minutes'] - l['in_class']} min", 8.5, color=GREY)

    # ------------------------------------------------------------- tools
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Tools and Resources")
    para(doc, "Learners use the following browser-based tools during the labs. "
              "No installation is required and all tools remain available after "
              "the course.")
    t = doc.add_table(rows=0, cols=3)
    t.style = "Table Grid"
    hdr = t.add_row().cells
    for i, htxt in enumerate(["Tool", "Used for", "URL"]):
        _cell(hdr[i], htxt, 9.5, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    for key, (name, url, purpose) in cd.TOOLS.items():
        c = t.add_row().cells
        _cell(c[0], name, 9, bold=True, fill=TOPIC_FILL)
        _cell(c[1], purpose, 9, color=GREY)
        _cell(c[2], url, 8, color=GREY)

    # ---------------------------------------------- learning reinforcement
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Learning Reinforcement")
    para(doc, "This is a commercial short course and carries no assessment. "
              "Learning is reinforced continuously through the hands-on labs, "
              "the daily exam-style drills, and a self-scored mock practice "
              "exam on Day 4 that tells each learner where to focus their "
              "remaining study.")
    t = doc.add_table(rows=0, cols=4)
    t.style = "Table Grid"
    hdr = t.add_row().cells
    for i, htxt in enumerate(["Mechanism", "Format", "Covers", "When"]):
        _cell(hdr[i], htxt, 9.5, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    for row in [
        ("Hands-on labs", "24 labs on one continuous case study, each producing "
                          "an artifact the next lab consumes",
         "All six topics and every ECO 2026 domain", "Throughout, ~21 hours"),
        ("Lab verification", "Each lab states a success test the learner checks "
                             "their own work against",
         "The technique taught in that lab", "End of each lab"),
        ("Exam-style drills", "Scenario questions in the ECO 2026 formats, worked "
                              "as a group",
         "The day's material", "End of Days 1–3"),
        ("Mock practice exam", "30 questions in ECO 2026 format under a timed "
                               "condition, self-scored by domain",
         "All three domains against the 33/41/26 weights", "Day 4, Lab 24 Part B"),
        ("Domain score analysis", "Per-domain percentage compared to the published "
                                  "weights, with a dated remediation plan",
         "The learner's weakest domains", "Day 4 debrief"),
    ]:
        c = t.add_row().cells
        for i, v in enumerate(row):
            _cell(c[i], v, 9, bold=(i == 0), fill=TOPIC_FILL if i == 0 else None)

    h2(doc, "Trainer Notes")
    for a in ["Circulate during every lab — the labs are where misconceptions "
              "surface, not during concept delivery.",
              "Insist learners work the arithmetic by hand; the exam provides no "
              "spreadsheet.",
              "Before answering any scenario, have learners state whether the "
              "context is predictive, adaptive or hybrid.",
              "The Day 4 mock is diagnostic, not a test — frame it that way so "
              "learners answer honestly rather than defensively.",
              "Debrief every wrong answer by rationale; that is where the learning "
              "converts.",
              "Remind learners this course supplies the 35 contact hours PMI "
              "requires for the PMP application."]:
        bullet(doc, a)

    prodoc.add_page_numbers(doc, left_text="www.tertiarycourses.com.sg")
    prodoc.enable_update_fields(doc)

    out = os.path.join(REPO, "courseware",
                       f"LP-{cd.SHORT_TITLE}.docx")
    doc.save(out)
    print(f"saved -> {out}")
    return out


if __name__ == "__main__":
    main()
