# Project Management Professional (PMP) Exam Prep (C523)

Courseware for the Tertiary Infotech Academy non-WSQ short course **Project Management Professional (PMP) Exam Prep**.

The course delivers the **35 contact hours of project management education** PMI requires before sitting the PMP examination, and is aligned to the **PMI PMP Examination Content Outline (ECO), July 2026** — People 33%, Process 41%, Business Environment 26%.

| | |
| --- | --- |
| Course code | C523 |
| Duration | 4 days · 32 instructional hours |
| Mode | Instructor-led, hands-on practical labs |
| Version | v1.0 · 20 July 2026 |
| Trainer | Dr. Alfred Ang |

## Contents

| Path | What it is |
| --- | --- |
| [courseware/PMP-Exam-Prep-v1.0.pptx](courseware/PMP-Exam-Prep-v1.0.pptx) | Trainer slide deck (289 slides) + PDF |
| [courseware/LP-PMP-Exam-Prep.docx](courseware/LP-PMP-Exam-Prep.docx) | Lesson Plan + PDF |
| [courseware/LG-PMP-Exam-Prep.docx](courseware/LG-PMP-Exam-Prep.docx) | Learner Guide + PDF |
| [LG-PMP-Exam-Prep.md](LG-PMP-Exam-Prep.md) | Learner Guide, Markdown mirror |
| [labs/](labs/) | 24 hands-on labs + index and tools guide |

## Topics

1. **Business Environment** — foundations, governance, compliance, change, development approaches
2. **Start the Project** — business case, charter, stakeholders, team formation
3. **Plan the Project** — scope, schedule, cost, quality, resources, communications, risk
4. **Lead the Project Team** — leadership, motivation, conflict, coaching, communication
5. **Monitor and Control the Project** — earned value, flow metrics, quality control, change control
6. **Close the Project** — acceptance, transition, benefits realisation, lessons learned, exam strategy

## The labs

24 labs (1,285 minutes of hands-on time) built on one continuous case study — the **Contoso Training Portal Upgrade**, a deliberately hybrid project. Each lab consumes artifacts produced by earlier labs, so by the Lab 24 capstone they assemble into a single integrated project management plan, followed by a full-format mock practice exam with domain score analysis.

See the [lab index](labs/README.md) for the full list.

## Building the courseware

All artifacts are generated from a single source (`course_data.py` + `data_domain1..6.py`) so the deck, Lesson Plan and Learner Guide cannot drift apart.

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

Requires `python-pptx`, `python-docx`, `Pillow` and LibreOffice (`soffice`) for PDF rendering.

---

© 2026 Tertiary Infotech Academy Pte Ltd · UEN 201200696W
