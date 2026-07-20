# Lab 01 - PMP Exam Orientation and 35 PDU Study Plan

| Field | Value |
| --- | --- |
| Topic | 1 - Business Environment |
| ECO 2026 task | Business Env T1 - Define and establish project governance (success metrics) |
| Duration | 45 minutes |
| Consumes | Nothing - this is the entry lab |
| Produces | `artifacts/01-exam-blueprint.md`, `artifacts/01-study-plan.md`, `artifacts/01-pdu-log.md` |

## Objectives

- Reproduce the PMP Examination Content Outline (July 2026) blueprint from memory: question counts, timing and domain weights.
- Convert the domain weights into a realistic question-count target per domain.
- Build a personal 6-week study plan anchored on the 35 contact hours earned in this course.
- Record the 35 PDU / contact-hour evidence needed for the PMP application.
- Establish the answer-selection heuristics used in every later lab's scenario questions.

## The Contoso case study

Every lab in this course uses one continuous project.

```text
CONTOSO TRAINING PORTAL UPGRADE

Contoso Learning Pte Ltd is a training provider with 14,000 active learners.
Its course registration portal is 9 years old. Registration takes 11 minutes
and abandons at 34%. Learner communications are sent manually by 3 admin staff.

The project will modernise course registration and learner communications.

  Sponsor            Priya Nathan, Chief Operating Officer
  Project Manager    You
  Budget             SGD 480,000 (hard ceiling, board-approved)
  Launch date        FIXED - 30 June, tied to the July intake enrolment window
  Approach           HYBRID - predictive governance and stage gates,
                     product increments delivered in 2-week sprints
  Constraint         A regulatory compliance review (PDPA data protection)
                     must pass before go-live
  Team               9 people: 4 developers, 1 UX designer, 1 QA lead,
                     1 business analyst, 1 DevOps engineer, 1 content lead
```

You will build one artifact per lab, and by Lab 24 they assemble into a single project management plan.

## Steps

### Step 1 - Build the exam blueprint from the ECO 2026 numbers

Create `artifacts/01-exam-blueprint.md` and complete this table. The totals are given; derive the per-domain question counts yourself.

```text
GIVEN, from the PMP Examination Content Outline, July 2026:

  Total questions on the exam        180
  Scored questions                   170
  Unscored pretest questions          10
  Total testing time                 240 minutes
  Breaks                             Two 10-minute breaks. The first comes after
                                     the case-study section, the second midway
                                     through the independent questions.
  Approach mix                       ~40% predictive; the remaining ~60% split
                                     between adaptive/agile and hybrid
```

| Domain | Weight | Scored questions (weight x 170) | Approx. minutes to allocate |
| --- | --- | --- | --- |
| I - People | 33% | | |
| II - Process | 41% | | |
| III - Business Environment | 26% | | |
| **Total** | **100%** | **170** | **240** |

Work the arithmetic:

```text
People              0.33 x 170 = 56.1  -> about 56 scored questions
Process             0.41 x 170 = 69.7  -> about 70 scored questions
Business Env        0.26 x 170 = 44.2  -> about 44 scored questions
                                          56 + 70 + 44 = 170  (check)

Pacing              240 minutes / 180 questions = 1.33 minutes per question
                    = 80 seconds per question, before breaks
                    A 15-question case study should take about 20 minutes.
```

Write the pacing number at the top of the file in bold. You will be held to it in the Lab 24 mock exam.

### Step 2 - Log the six question types

The July 2026 ECO added graphic-based items. List all six types and, for each, write one sentence on how you will approach it under time pressure.

| Question type | What it looks like | Your approach |
| --- | --- | --- |
| Multiple choice | One best answer from four options; the bulk of the exam | |
| Multiple response | More than one correct answer; the item states how many | |
| Matching | Drag items from one column to match a second column | |
| Enhanced matching | Matching that includes an image or diagram for context | |
| Graphic-based (NEW) | Read a chart, graph, diagram or image, then answer from it | |
| Case study | A scenario with supporting visuals, then a series of linked questions | |

For the graphic-based row, note the three chart types most likely to appear: an earned value S-curve (Lab 20), a control chart (Lab 22) and a burndown/Kanban board (Lab 19). You will build all three in this course, which is the fastest way to be ready to read them.

### Step 3 - Record your 35 contact-hour evidence

PMI requires 35 contact hours of project management education. This course supplies all 35 in one record. Create `artifacts/01-pdu-log.md`:

| Evidence item | What to record | Your entry |
| --- | --- | --- |
| Course title | Project Management Professional (PMP) Exam Prep | |
| Provider | Tertiary Infotech Academy Pte Ltd (UEN 201200696W) | |
| Course reference | C523 | |
| Contact hours claimed | 35 | |
| Delivery dates | Your four course dates | |
| Certificate reference | Issued on completion; store the PDF path here | |
| Project experience | 36 months leading projects (or 60 months if you hold a secondary diploma rather than a degree) | |
| Education | Four-year degree, or secondary diploma / global equivalent | |
| Audit pack location | Folder path where you keep the above | |

Note the eligibility rule in one line so you do not have to look it up again:

```text
Four-year degree      + 36 months leading projects + 35 contact hours
Secondary diploma     + 60 months leading projects + 35 contact hours
```

### Step 4 - Build a 6-week study plan weighted to the blueprint

Study time should follow exam weight, not personal comfort. Since Process is 41% of the exam, it gets the most hours.

Create `artifacts/01-study-plan.md`:

| Week | Focus | Hours | Practice target | Course labs to revisit |
| --- | --- | --- | --- | --- |
| 1 | Business Environment: governance, compliance, external environment | 6 | 60 questions | 01-04 |
| 2 | Process part 1: charter, scope, WBS, schedule | 8 | 80 questions | 05-12 |
| 3 | Process part 2: cost, quality, risk, procurement | 8 | 80 questions | 13-14, 20-22 |
| 4 | People: team leadership, conflict, communication | 7 | 70 questions | 15-18 |
| 5 | Agile and hybrid: backlog, sprints, Kanban, servant leadership | 6 | 60 questions | 10, 19 |
| 6 | Full timed mocks, weak-area repair, closure and benefits | 8 | 2 x 180-question timed mocks | 23-24 |
| | **Total** | **43** | **350 questions + 2 mocks** | |

Adjust the hours to your own calendar but keep two rules: Process must get the largest single block, and week 6 must contain at least two full-length timed mocks. A mock taken untimed teaches you nothing about pacing.

### Step 5 - Write your answer-selection heuristics

Most PMP questions are situational and several options are defensible. What separates the keyed answer is usually a mindset, not a fact. Write these into your notes and apply them in every scenario question from Lab 02 onward.

```text
BEFORE ANSWERING
  1. Identify the approach in play. Words like "sprint", "backlog", "product
     owner" signal adaptive. "Baseline", "change request", "phase gate" signal
     predictive. Both present means hybrid - answer for the part being asked about.
  2. Identify where you are in the life cycle. A planning question and an
     execution question have different right answers.
  3. Identify what the question actually asks: "do FIRST", "do NEXT", "BEST
     response", "MOST likely cause". These are four different questions.

ELIMINATE OPTIONS THAT
  - Escalate to the sponsor before you have gathered facts.
  - Go around the team, the product owner, or an agreed process.
  - Accept a scope change without impact analysis or change control.
  - Blame, discipline, or remove a team member as a first action.
  - Do nothing, or wait for the next scheduled meeting when action is needed.

PREFER OPTIONS THAT
  - Gather information and analyse impact before deciding.
  - Talk directly to the person or team involved.
  - Follow the process the project already agreed.
  - Keep the team empowered and self-organising.
  - Protect delivered value and the customer relationship.
```

### Step 6 - Apply the heuristics to three scenarios

Answer each in writing. State your choice, then name which heuristic decided it.

```text
SCENARIO 1
A senior Contoso stakeholder approaches a developer during a sprint and asks
her to add a "quick" report to the current sprint. She agrees. You find out at
the daily standup the next morning.

  A. Escalate to the COO that the stakeholder is bypassing governance.
  B. Remove the report from the sprint and tell the developer not to accept
     direct requests.
  C. Meet the stakeholder and the product owner together, explain how work
     enters the backlog, and have the request prioritised there.
  D. Allow it this once since the work has already started, and raise it at the
     retrospective.

SCENARIO 2
The compliance officer tells you the PDPA review will now need six weeks, not
the three you planned. The launch date cannot move.

  A. Compress the compliance review by running it in parallel with UAT.
  B. Analyse the schedule impact, develop options with the team, and take the
     options with their cost and risk to the sponsor.
  C. Inform the sponsor immediately that the launch date will slip.
  D. Add two developers to the team to recover the lost time.

SCENARIO 3
A graphic-based item shows a cost performance index (CPI) trending from 1.02 in
period 1 down to 0.87 in period 6, while the schedule performance index (SPI)
holds steady at 0.99. What does the chart tell you?

  A. The project is behind schedule and over budget.
  B. The project is roughly on schedule but is progressively overspending.
  C. The project is ahead of budget and on schedule.
  D. There is not enough information to judge.
```

Answer key, to check only after you have written your own reasoning:

```text
SCENARIO 1  -> C.  Do not escalate first (heuristic: gather and engage before
                   escalating), do not go around the product owner, and do not
                   accept the change outside the agreed intake path. C fixes the
                   instance and the process at once.

SCENARIO 2  -> B.  "Analyse impact, develop options, then present to the
                   sponsor." C escalates with a problem instead of options.
                   A and D are single solutions chosen before analysis - and D
                   invokes Brooks' law, adding people to a late task.

SCENARIO 3  -> B.  SPI ~ 1.0 means schedule performance is on plan. CPI falling
                   from 1.02 to 0.87 means every dollar is buying progressively
                   less work: a worsening cost overrun. You will compute exactly
                   this pattern on real Contoso numbers in Lab 20.
```

### Step 7 - Set your baseline score

Answer 20 practice questions of any source, timed at 80 seconds each, and record the result:

| Metric | Your baseline |
| --- | --- |
| Questions attempted | 20 |
| Correct | |
| Percentage | |
| Average seconds per question | |
| Domain where you scored lowest | |

Keep this number. In Lab 24 you sit a full ECO-format mock and compare against it. A baseline you never wrote down is a baseline you cannot improve against.

## Deliverable

Submit to `artifacts/`:

- `01-exam-blueprint.md` - the completed domain table with derived question counts and the 80-second pacing rule.
- Six question-type rows, each with your approach.
- `01-pdu-log.md` - the completed 35-contact-hour evidence record.
- `01-study-plan.md` - the 6-week weighted plan.
- Your written answer-selection heuristics.
- Written answers to the three scenarios, each naming the deciding heuristic.
- Your baseline score table.

## Checkpoint

You did this right if:

- Your per-domain question counts are 56 / 70 / 44 and sum to exactly 170.
- Your pacing figure is 80 seconds per question, derived from 240 minutes / 180 questions.
- Your study plan gives Process the largest hour allocation of any single domain.
- Your study plan contains at least two full-length timed mocks in the final week.
- For each scenario you named a heuristic, not just a letter. If you only wrote "C", redo it.
- Your PDU log names the provider, the course reference C523, and 35 contact hours.
- You recorded a numeric baseline score you can compare against in Lab 24.
