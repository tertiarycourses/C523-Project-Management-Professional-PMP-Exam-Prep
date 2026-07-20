# Lab Tools, Templates and Folder Structure

Everything you need for the 24 labs of the Project Management Professional (PMP) 35 PDU Training course.

## Live browser tools

These run in any modern browser with no installation, no login and no data leaving your machine. Each one is used in specific labs; open it when the lab tells you to and use the exact inputs the lab supplies.

| Tool | URL | What it is for | Used in |
| --- | --- | --- | --- |
| Mind Mapping | [alfredang.github.io/mindmapping](https://alfredang.github.io/mindmapping/) | Expand a central idea into branches for requirements discovery | Lab 09 |
| 5 Whys | [alfredang.github.io/5whys](https://alfredang.github.io/5whys/) | Drill from a symptom to its root cause by asking why five times | Lab 21 |
| Fishbone Diagram | [alfredang.github.io/fishbone](https://alfredang.github.io/fishbone/) | Group candidate causes into categories around a problem statement | Lab 21 |
| Pareto Chart | [alfredang.github.io/paretochart](https://alfredang.github.io/paretochart/) | Rank defect categories to find the vital few driving most of the pain | Lab 21 |
| SPC / Control Chart | [alfredang.github.io/novaspc](https://alfredang.github.io/novaspc/) | Plot a process over time against control limits to separate signal from noise | Lab 22 |
| Statistics | [alfredang.github.io/novastats](https://alfredang.github.io/novastats/) | Descriptive statistics, distributions and hypothesis testing on project data | Labs 05, 13, 20, 22 |
| RACI Matrix | [alfredang.github.io/raci](https://alfredang.github.io/raci/) | Assign Responsible, Accountable, Consulted and Informed per work package | Lab 15 |
| Kanban Board | [alfredang.github.io/kanban](https://alfredang.github.io/kanban/) | Visualise work in progress, limit WIP and expose bottlenecks | Lab 19 |
| Scrum Simulator | [alfredang.github.io/scrum](https://alfredang.github.io/scrum/) | Run sprint planning, review and retrospective mechanics | Lab 10 |
| System Thinking | [alfredang.github.io/systemloop](https://alfredang.github.io/systemloop/) | Map reinforcing and balancing loops behind a recurring problem | Lab 14 |
| Design Thinking | [alfredang.github.io/designthinking](https://alfredang.github.io/designthinking/) | Empathise, define, ideate, prototype and test a solution | Optional, Lab 09 |
| Pivot Analysis | [alfredang.github.io/novapivot](https://alfredang.github.io/novapivot/) | Slice project data by dimension to expose trends and outliers | Optional, Lab 20 |

### Tools by lab

| Lab | Tools |
| --- | --- |
| 02 | Mind Mapping (optional, for the PESTLE expansion) |
| 05 | Statistics |
| 09 | Mind Mapping |
| 10 | Scrum Simulator |
| 13 | Statistics |
| 14 | System Thinking |
| 15 | RACI Matrix |
| 19 | Kanban Board |
| 20 | Statistics |
| 21 | 5 Whys, Fishbone, Pareto Chart |
| 22 | SPC / Control Chart, Statistics |

All other labs are worked on paper or in a spreadsheet.

## Other software you need

- A spreadsheet application for cost baselines, EVM tables and defect logs.
- A markdown editor or word processor for the written artifacts.
- A diagramming tool such as diagrams.net for the WBS, network diagram and org charts.
- A timer for the Lab 24 mock exam. The pacing discipline only works if it is timed.

## Learner folder structure

Create this before Lab 01 and keep every artifact in it. Labs consume each other's outputs, so a missing artifact from Lab 06 will block you in Lab 11.

```text
pmp-35-pdu-labs/
|-- artifacts/          every numbered deliverable, one file per lab
|-- diagrams/           WBS, network diagram, fishbone, control chart exports
|-- worksheets/         working calculations
|-- mock-exam/          Lab 24 answers and score analysis
`-- notes/              your own exam notes and heuristics
```

Name artifacts with the lab number that produced them, for example `artifacts/06-project-charter.md`. Every lab's metadata block lists exactly what it produces.

## The artifact chain

The 24 labs form one continuous project. This is what feeds what.

```text
01 exam blueprint, study plan
02 PESTLE/TECOP scan ------------> 03, 04, 05, 06, 14
03 EEF/OPA, governance, thresholds -> 04, 05, 06, 12, 20
04 compliance, sustainability, AI --> 06, 09, 11, 14
05 business case, NPV, benefits map -> 06, 13, 23
06 charter, approach, assumptions --> 07, 09, 11, 12, 13, 14, 21, 23
07 stakeholder register, salience --> 08, 15, 18
08 team charter, ground rules ------> 15, 16, 17, 19
09 requirements register, RTM ------> 10, 11, 23
10 backlog, MoSCoW, Kano -----------> 11, 19, 20
11 WBS, WBS dictionary -------------> 12, 13, 15
12 network diagram, critical path --> 13, 20
13 cost baseline, reserves ---------> 14, 20
14 risk register, EMV --------------> 20, 23
15 RACI, resource plan -------------> 16, 18
16 Tuckman, motivation -------------> 17
17 conflict resolution
18 communication plan, status ------> 20, 23
19 Kanban, flow metrics ------------> 21
20 EVM, compression decision -------> 21, 22, 23
21 Pareto, fishbone, 5 Whys --------> 22, 23
22 control chart, capability -------> 23
23 closure, benefits, lessons ------> 24
24 capstone: consolidated plan + mock exam
```

## Starter templates

Use these column structures for the worksheets. Each lab specifies its own required fields, which may extend these.

### Stakeholder register

| ID | Stakeholder | Role | Power | Interest | Attitude | Expectation | Concern |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Risk register

| ID | RBS category | Risk (cause / event / effect) | Probability | Impact SGD | Impact days | Score | Response | Owner | Trigger |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Issue log

| ID | Issue | Raised | Impact | Owner | Due | Status | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Product backlog

| ID | User story | Points | MoSCoW | Kano | Acceptance criteria | Sprint |
| --- | --- | --- | --- | --- | --- | --- |

### Requirements traceability matrix

| REQ ID | Requirement | Source | Charter ref | WBS element | Story | Test case | Compliance ref | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Change request

| ID | Change | Reason | Cost impact | Schedule impact | Risk impact | Decision body | Decision | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### EVM calculation sheet

| Period | Cum PV | Cum EV | Cum AC | CV | SV | CPI | SPI | EAC | VAC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Lessons learned register

| ID | What happened | Impact | Root cause | Recommendation | OPA updated |
| --- | --- | --- | --- | --- | --- |

## The case study

Every lab uses one continuous project.

```text
CONTOSO TRAINING PORTAL UPGRADE

Contoso Learning Pte Ltd is a training provider with 14,000 active learners.
Its course registration portal is 9 years old. Registration takes a median of
11 minutes and 34% of attempts are abandoned. Learner communications consume
24 staff-hours per week across 3 administrators. 62% of traffic is mobile,
against a portal that is not responsive. Legacy consent screens do not meet
current PDPA requirements.

  Sponsor            Priya Nathan, Chief Operating Officer
  Product Owner      Marcus Tan, Head of L&D Operations
  Project Manager    You
  Budget             SGD 480,000 board-approved ceiling, with the
                     SGD 26,000 contingency reserve held inside it
  Launch date        FIXED, 30 June, tied to the July intake window
  Approach           HYBRID - predictive governance with three stage gates,
                     product increments delivered in 2-week sprints
  Compliance         PDPA and SSG funding data review must pass before
                     go-live; the DPO owns gate G3
  Team               9 people: 4 developers, 1 UX designer, 1 QA lead,
                     1 business analyst, 1 DevOps engineer, 1 content lead
  Capacity           approximately 34 story points per sprint, 12 sprints

  Gates              G1 design baseline, week 6
                     G2 build complete, week 18
                     G3 pre-launch, week 24
                     Go live week 26, closure week 28
```

Use this case unless your trainer assigns a real project of your own. If you do substitute a real project, keep the same artifact sequence - the labs depend on each other regardless of which project fills them.
