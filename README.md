# Project Management Professional (PMP) Exam Prep (C523)

Courseware for the Tertiary Infotech Academy non-WSQ short course **Project Management Professional (PMP) Exam Prep**.

The course delivers the **35 contact hours of project management education** PMI requires before sitting the PMP examination, and is aligned to the **PMI PMP Examination Content Outline (ECO), July 2026** — People 33%, Process 41%, Business Environment 26%.

**📅 [Register for this course →](https://www.tertiarycourses.com.sg/project-management-professional-pmp-exam-prep.html)**

| | |
| --- | --- |
| Course code | C523 |
| Register | [tertiarycourses.com.sg](https://www.tertiarycourses.com.sg/project-management-professional-pmp-exam-prep.html) |
| Duration | 4 days · 32 instructional hours |
| Mode | Instructor-led, hands-on practical labs |
| Version | v2.0 · 20 July 2026 |
| Trainer | Dr. Alfred Ang |

## Contents

| Path | What it is |
| --- | --- |
| [courseware/PMP-Exam-Prep-v2.0.pptx](courseware/PMP-Exam-Prep-v2.0.pptx) | Trainer slide deck (536 slides) + PDF |
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

24 labs (1,385 minutes of hands-on time) built on one continuous case study — the **Contoso Training Portal Upgrade**, a deliberately hybrid project. Each lab consumes artifacts produced by earlier labs, so by the Lab 24 capstone they assemble into a single integrated project management plan, followed by a full-format mock practice exam with domain score analysis.

See the [lab index](labs/README.md) for the full list.

## Building the courseware

All artifacts are generated from a single source (`build/course_data.py`, `build/labs_index.py` and the six `build/data_topicN.py` modules) so the deck, Lesson Plan, Learner Guide and labs cannot drift apart.

```bash
cd build
python3 build_slides.py        # -> courseware/PMP-Exam-Prep-v2.0.pptx
python3 build_lesson_plan.py   # -> courseware/LP-PMP-Exam-Prep.docx
python3 build_learner_guide.py # -> courseware/LG-PMP-Exam-Prep.docx + LG-*.md
```

Requires `python-pptx`, `python-docx`, `Pillow` and LibreOffice (`soffice`) for PDF rendering.

---

© 2026 Tertiary Infotech Academy Pte Ltd · UEN 201200696W
