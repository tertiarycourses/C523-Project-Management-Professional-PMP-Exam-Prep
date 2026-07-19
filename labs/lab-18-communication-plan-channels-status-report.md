# Lab 18 - Communication Plan, Channels and Status Reporting

| Field | Value |
| --- | --- |
| Topic | 4 - Lead the Project Team |
| ECO 2026 task | People T8 - Plan and manage communication; People T4 - Engage stakeholders |
| Duration | 45 minutes |
| Consumes | Lab 07 stakeholder register, engagement matrix and engagement cadence table; Lab 03 governance model and escalation thresholds |
| Produces | `artifacts/18-communication-plan.md`, `artifacts/18-status-reports.md` |

## Objectives

- Compute communication channels with N(N-1)/2 and derive the management implication of superlinear growth.
- Choose push, pull or interactive communication for each stakeholder and justify the choice.
- Place Contoso communications correctly in the formal/informal by written/verbal grid.
- Build a communication plan in which every row has a named feedback loop, not just a broadcast.
- Trace a message through the sender-receiver model and name the real noise sources on this project.
- Write the same week-14 project status three ways for three audiences from one set of underlying numbers.
- Notice, unprompted, that CPI 0.919 breaches the Lab 03 cost variance threshold and triggers a mandatory escalation.

## Steps

### Step 1 - Compute the communication channels

```text
NUMBER OF COMMUNICATION CHANNELS  =  N(N - 1) / 2

  where N is the number of PEOPLE who need to communicate with each other.

  The formula counts the unique PAIRS in a group. Each pair is one
  potential two-way channel that has to be established and maintained.
```

Work the Contoso cases:

```text
CASE 1 - THE DELIVERY TEAM ALONE
  The Lab 08 team charter names 9 members.

    N = 9
    9 x (9 - 1) / 2  =  9 x 8 / 2  =  72 / 2  =  36 channels

CASE 2 - ADD THE PM
  The PM is a tenth person in the room, not an observer of the nine.

    N = 10
    10 x 9 / 2  =  90 / 2  =  45 channels

  Adding ONE person added NINE channels, not one. The new person forms a
  pair with every existing member.

CASE 3 - THE PROJECT WORKING GROUP
  The 9 team members, the PM, Marcus Tan the product owner (S-03), and
  the PM's manager who chairs the delivery forum.

    N = 12
    12 x 11 / 2  =  132 / 2  =  66 channels

CASE 4 - THE GROWTH SCENARIO THE EXAM ASKS ABOUT
  Suppose the constraint CON-4 were lifted and the team grew from 9 to 13.

    N = 9   ->  9 x 8 / 2   =  36 channels
    N = 13  ->  13 x 12 / 2 =  78 channels

    People    +4 on 9    =  +44%
    Channels  +42 on 36  =  +117%

  A 44% increase in headcount produced a 117% increase in the coordination
  surface. Channels grow with the SQUARE of N while capacity grows
  linearly with N. Coordination cost is superlinear; output is not.
```

| Group | N | N(N-1)/2 | Channels | Channels added by the last person |
| --- | --- | --- | --- | --- |
| Two developers pairing | 2 | 2x1/2 | 1 | 1 |
| Core design trio: dev lead, UX, BA | 3 | 3x2/2 | 3 | 2 |
| Sprint planning: 4 devs + QA lead | 5 | 5x4/2 | 10 | 4 |
| Team without the PM | 9 | 9x8/2 | 36 | 8 |
| Team plus PM | 10 | 10x9/2 | 45 | 9 |
| Team, PM, product owner | 11 | 11x10/2 | 55 | 10 |
| Working group (adds PM's manager) | 12 | 12x11/2 | 66 | 11 |
| Grown team scenario | 13 | 13x12/2 | 78 | 12 |
| Project board (6 members) | 6 | 6x5/2 | 15 | 5 |
| All 17 Lab 07 stakeholder entries plus PM | 18 | 18x17/2 | 153 | 17 |

The last row is the number that should change your behaviour. There are 153 potential channels across the stakeholder set. Nobody can service 153 channels. A communication plan is not administrative tidiness; it is the decision about which of the 153 you will actually maintain and at what frequency.

Write the management implications into `artifacts/18-communication-plan.md`:

```text
WHAT THE NUMBERS OBLIGE YOU TO DO

  1. SUBDIVIDE. Two sub-teams of 5 and 5 have 10 + 10 = 20 internal
     channels plus a defined interface, against 45 for one group of 10.
     This is why feature teams, sub-teams and squads exist. It is not a
     fashion; it is arithmetic.

  2. ADDING PEOPLE COSTS MORE THAN IT PAYS, AT FIRST. Brooks' law - adding
     people to a late project makes it later - has this formula underneath
     it. The 10th person contributes one person's capacity and 9 new
     channels, plus the onboarding time of the people who must staff them.
     This is the arithmetic behind rejecting "add two developers" in the
     Lab 01 Scenario 2 answer key.

  3. STRUCTURED FORUMS BEAT AD-HOC CONTACT. One standup of 10 people
     replaces up to 45 pairwise updates. The ceremony is a channel
     compression device.

  4. PLAN, DO NOT BROADCAST. With 153 possible stakeholder channels, the
     alternative to a plan is not "informal communication" - it is
     copying everyone into everything, which produces the appearance of
     communication and the reality of none.

  5. EVERY NEW STAKEHOLDER HAS A COST. Before adding someone to a
     distribution list, note that at N=18 the next person adds 18
     channels. "Just cc them" is never free.
```

### Step 2 - Choose push, pull or interactive for each stakeholder

```text
THE THREE COMMUNICATION METHODS

  PUSH          Sent to specific recipients. Delivery is assured;
                UNDERSTANDING IS NOT. Email, reports, memos, voicemail.
                Use for: records, formal notification, routine status to
                many people, anything needing an audit trail.
                Failure mode: you sent it, therefore you believe they know.

  PULL          Recipients access it when they choose. Suits large volumes
                and large audiences. Dashboards, wikis, shared drives,
                knowledge repositories, the Kanban board.
                Use for: reference material, detail, self-service, large
                or dispersed audiences.
                Failure mode: nobody pulls, and critical news sits unread.
                NEVER use pull for anything urgent or unwelcome.

  INTERACTIVE   Multi-directional and real time. Meetings, calls, standups,
                video, corridor conversations, workshops.
                Most effective for complex, sensitive, ambiguous or
                contentious content, and the only method that confirms
                understanding as it goes.
                Use for: decisions, conflict, bad news, negotiation,
                anything requiring commitment rather than compliance.
                Cost: the most expensive per person-minute. Do not use it
                for routine status.

  THE RULE THE EXAM TESTS
    The harder, more sensitive or more contentious the message, the more
    interactive the method must be. Bad news delivered by email is the
    single most common wrong answer in this area.
```

| Stakeholder | Method | Why this method |
| --- | --- | --- |
| S-01 Priya Nathan, COO (sponsor) | Interactive primary, push secondary | Decisions are needed from her weekly; a written one-pager follows the conversation as the record, not instead of it |
| S-02 Group Finance Director | Push | High power, low interest. Wants the numbers monthly, correct and brief. Interactive would over-consume him |
| S-03 Marcus Tan, product owner | Interactive, daily | Continuous prioritisation, acceptance decisions and ambiguity resolution. Nothing else works |
| S-04 Data Protection Officer | Interactive for the review, pull for evidence | The evidence pack is large and detailed - pull. The findings conversation is consequential - interactive |
| S-05 Head of Sales | Interactive | Lab 07 classifies him dangerous, Lab 17 logs CF-03 at L3. Contentious content must never go by email |
| S-06 Admin staff (3) | Interactive, always | Lab 17 CF-04. This group's issue is safety and trust. A redundancy communication by email would escalate it to L4 |
| S-07 Learners (14,000) | Push for transactional, pull for reference | Booking confirmations are push. Help content, FAQs and the migration explainer are pull |
| S-08 Trainers (23) | Push monthly, interactive at the briefing | Volume is manageable, content is routine, but the change affects them, so at least one interactive touchpoint |
| S-09 Support desk lead | Interactive at handover, pull for runbooks | Handover is complex and consequential; runbooks are reference |
| S-10 Project team (9) | Interactive daily, pull for artifacts | Standup, review, retro; backlog and board are pull |
| S-11 IT Operations Manager | Interactive at gates, pull for architecture docs | Reviews at G1, G2 and handover per Lab 07 |
| S-16 Senior trainer (12 yrs) | Interactive | Lab 07 marks him discretionary and resistant. His stated need is "to be consulted, not informed" - which is a request for interactive, and cheap to honour |
| S-17 Corporate clients (top 8) | Push, via account managers | Reassurance at scale; the account manager provides the interactive layer |

```text
CHECK YOUR TABLE FOR THIS ERROR
  If every resistant or anxious stakeholder in your plan receives push
  communication, your plan will fail on exactly the stakeholders it most
  needed to work on. S-05, S-06, S-08 and S-16 are the four Lab 07
  entries with a Resistant or anxious attitude. Every one of them needs
  an interactive element.
```

### Step 3 - Place communications in the formal/informal by written/verbal grid

| | Written | Verbal |
| --- | --- | --- |
| **Formal** | Project charter (Lab 06); the monthly project board report; the change request and CCB decision record; the compliance evidence pack for the DPO; the contract with the gateway vendor; the gate G1/G2/G3 sign-off records; the redeployment statement of intent to S-06 | Sprint review demo to the sponsor and product owner; the gate review meetings; the CCB meeting; the formal escalation briefing to the project board; the vendor negotiation session (Lab 17 Step 7) |
| **Informal** | Team channel messages; comments on a story card; a note on the Kanban board; a quick email confirming a corridor agreement; the retrospective wall | Daily standup; corridor conversations; the private word with Farah about capacity; the Lab 08 level-2 ground-rule conversation; the 1:1 with Nurul to bring her back into planning |

Three observations to record:

```text
1. The redeployment statement to the admin staff is FORMAL WRITTEN and it
   is delivered IN PERSON. The Lab 17 CF-04 resolution requires both: the
   written form gives them the certainty they asked for, and the in-person
   delivery is what stops it reading as a dismissal notice. Formality and
   method are separate choices.

2. Most of the highest-value communication on this project is INFORMAL
   VERBAL - the private word, the 1:1, the corridor. None of it appears
   in a communication plan and all of it is where the Lab 16 and Lab 17
   interventions actually happen. The plan governs the formal traffic; it
   does not replace the informal.

3. Anything that will be audited must exist in the FORMAL WRITTEN cell.
   The DPO's evidence pack, the CCB decisions and the gate sign-offs
   cannot rest on a verbal agreement, no matter how clear it was.
```

### Step 4 - Build the communication plan with feedback loops

The ECO People T8 enabler is "establish a feedback loop". A row with no feedback mechanism is a broadcast, and a broadcast tells you nothing about whether the message arrived. Complete every column.

| # | Stakeholder | Information need | Format | Method | Frequency | Sender | Feedback loop |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-01 | S-01 COO | Progress, risks, decisions required | One-page brief plus 30-min meeting | Interactive + push | Weekly | PM | She states the decision back in her own words at the end of the meeting; PM emails the decision record within 24 hrs and asks her to confirm |
| C-02 | S-02 Finance Director | Cost position, CPI/SPI, forecast at completion | One-page financial summary | Push | Monthly | PM | Standing 10-minute slot at the monthly board for questions; if no questions two months running, PM calls to check the report is still being read |
| C-03 | Project Board | Full status: EVM, gates, escalations against thresholds | 4-page board report | Push then interactive | Monthly | PM | Board minutes record decisions and actions with owners; PM confirms actions at the next board's opening item |
| C-04 | S-03 Marcus Tan (PO) | Backlog state, acceptance, priority calls | Working session and board | Interactive | Daily plus ceremonies | PM | Acceptance recorded on the story card in staging; disagreement surfaces immediately at the daily |
| C-05 | S-04 DPO | Compliance coverage: 5 of 8 requirements evidenced | Coverage table plus evidence pack | Pull for evidence, interactive for review | Fortnightly plus gates | Farah Ismail (BA) | DPO signs each requirement line as accepted or returns it with a named gap; unsigned lines are visible in the coverage fraction |
| C-06 | S-05 Head of Sales | Roadmap position, phase-2 status | Meeting with a one-page roadmap | Interactive | Monthly | PM | He restates the phase-2 decision date; PM confirms in writing after each meeting - this is the Lab 17 CF-03 escalation control |
| C-07 | S-06 Admin staff (3) | Progress, training dates, redeployment status | Group session, 30 min | Interactive | Weekly | Ops Manager | Open question round every session with the PM present; anonymous concern route through the PM as advocate per Lab 07 |
| C-08 | S-07 Learners | Transactional confirmations; change and migration notices | Email and portal notice | Push, plus pull for FAQ | Per transaction; launch comms at weeks 22, 24, 26 | Grace Tay (content lead) | Open and click rates measured; support-desk ticket themes reviewed weekly; usability sessions in sprints 3, 5, 7 |
| C-09 | S-08 + S-16 Trainers | What changes for them specifically | Briefing note plus monthly briefing | Push plus interactive | Monthly | Farah Ismail | Q&A at the briefing; senior trainer S-16 consulted directly on comms wording before each release |
| C-10 | S-09 Support desk lead | Release content, known issues, runbooks | Release note plus runbook wiki | Push plus pull | Per release, plus handover session | Vikram Shah (DevOps) | Support lead confirms readiness in writing before each release; launch-week ticket volume reviewed daily |
| C-11 | S-10 Project team | Everything: goal, blockers, WIP, decisions | Standup, sprint review, retro, decision log | Interactive plus pull | Daily and fortnightly | PM | Blockers raised same day per GR-7; retro actions carry an owner and a date and are reviewed at the next retro |
| C-12 | S-11 IT Ops Manager | Architecture, supportability, handover readiness | Review meeting plus architecture docs | Interactive at gates, pull otherwise | G1, G2, handover | Rajesh Menon (dev lead) | Written supportability conditions accepted into the backlog as stories, so acceptance is visible in the board |
| C-13 | S-17 Corporate clients | Continuity assurance across the launch | Account manager briefing | Push via account managers | Pre-launch and launch week | Head of Sales | Account managers report client concerns back to the PM within 48 hours |
| C-14 | Vendors (S-12, S-13) | Integration schedule, SLA performance | Email plus review call | Push plus interactive | Fortnightly during integration | Aisha Rahman | SLA response times logged and reviewed against the contracted 4 hours |

```text
TEST EVERY ROW WITH THIS QUESTION
  "How would I know if this message did not land?"

  If the answer is "I would not", the row has no feedback loop and it is
  a broadcast. Rewrite it. Note the shape of the good answers above -
  a restatement, a signature, a measured rate, a ticket theme, a story
  accepted into a backlog. Each is an OBSERVABLE consequence of the
  message having been received and understood.
```

### Step 5 - Trace the communication model and name the noise

```text
THE SENDER-RECEIVER MODEL

  SENDER -> ENCODE -> TRANSMIT -> DECODE -> RECEIVER
                        (medium)
     ^                                          |
     |------------------ FEEDBACK <-------------|

                    NOISE affects every stage

  ENCODE     turning meaning into words, numbers, a chart
  TRANSMIT   the medium carrying it
  DECODE     the receiver reconstructing meaning from the signal
  FEEDBACK   the receiver confirming what they understood - the ONLY
             stage that tells the sender anything

  The sender is accountable for the message being UNDERSTOOD, not for it
  having been sent. Encoding is the sender's job and so is checking the
  decode.
```

| Stage | Contoso noise source | Consequence | Control |
| --- | --- | --- | --- |
| Encode | The PM writes "CPI 0.919" to the COO, who does not use earned value | She reads a decimal and takes no action; a threshold breach passes unnoticed | Encode for the audience: "we are spending SGD 1.09 for every dollar of work delivered" |
| Encode | "Done" means ten things to Kenneth and "functionally complete" to Rajesh | The Lab 17 CF-02 conflict | A written definition of done, agreed by consensus (Lab 08 Step 5) |
| Transmit | Daniel Ofori is 8 hours behind the rest of the team | Decisions taken while he is asleep; he is a silent party to them | Core hours 16:00-19:00 SGT / 08:00-11:00 GMT (Lab 08 Step 3); decisions logged in writing |
| Transmit | English is a second language for several team members; heavy technical jargon in reviews | Nodding without comprehension | Ask for a restatement, never "does everyone understand?" - which reliably returns yes |
| Transmit | Team channel volume; 40 messages an hour during integration | Important messages buried | Blockers to a dedicated channel per GR-7; decisions to the decision log |
| Decode | Eight weeks of silence from the Ops Manager to the admin staff | Silence decoded as bad news, because their prior experience says so. Two are job hunting | Say the true thing early, in person. Silence always carries a message; you do not control which one |
| Decode | Head of Sales hears "deferred to phase 2" as "refused" | Escalation to the sponsor, Lab 17 CF-03 | A dated phase-2 decision point makes deferral verifiable rather than a euphemism |
| Feedback | Status reports distributed with no acknowledgement mechanism | The PM believes the board is informed; the board has not read page 3 | The C-03 feedback loop: minuted decisions and actions confirmed at the following board |
| Feedback | "Any questions?" at the end of a briefing | Silence read as understanding | Ask a specific person to state the next action in their own words |

### Step 6 - The week-14 status data

Create `artifacts/18-status-reports.md`. One set of facts follows. All three reports in Step 7 must be traceable to it. Tailoring means changing the encoding for the audience; it does not mean changing the numbers.

```text
CONTOSO TRAINING PORTAL UPGRADE - STATUS AS AT END OF WEEK 14
Sprint 7 of 12. Gate G1 passed week 6. Gate G2 due week 18.

EARNED VALUE - the figures are given here; Lab 20 computes them from the
raw cost and progress data, and this lab uses them as inputs.

  BAC   Budget at completion         SGD 480,000
  PV    Planned value to date        SGD 268,000
  EV    Earned value to date         SGD 249,000
  AC    Actual cost to date          SGD 271,000

  CV    = EV - AC   = 249,000 - 271,000  = -22,000
  SV    = EV - PV   = 249,000 - 268,000  = -19,000
  CPI   = EV / AC   = 249,000 / 271,000  = 0.919
  SPI   = EV / PV   = 249,000 / 268,000  = 0.929
  EAC   = BAC / CPI = 480,000 / 0.919    = 522,306
  VAC   = BAC - EAC = 480,000 - 522,306  = -42,306

  Percent of budget spent    271,000 / 480,000 = 56.5%
  Percent of work earned     249,000 / 480,000 = 51.9%

DELIVERY
  Sprint 7 of 12 in progress. Velocity: sprint 5 = 31, sprint 6 = 33,
  sprint 7 forecast 33 against a capacity of 34.
  Must-have stories: 71 of 104 complete.

COMPLIANCE
  5 of 8 remaining compliance requirements evidenced and accepted by the
  DPO. 3 outstanding: consent withdrawal flow, PDPA data retention
  schedule, and the data processor agreement with the hosting vendor.

RISK
  Two risks at a score of 20 or above on the Lab 14 register:
    R-03  Payment gateway v2 API instability (probability 4 x impact 5 = 20)
    R-07  Loss of admin SME availability - two of three job hunting
          (probability 4 x impact 5 = 20)

BUDGET LINES
  Contingency reserve released to date: SGD 9,000 of SGD 26,000.

GOVERNANCE - from the Lab 03 escalation thresholds
  Cost variance beyond -5% against plan       -> escalate to Project Board
                                                 within 5 working days
  Schedule variance threatening a gate date   -> escalate to Project Board
  Any risk scoring 20 or above                -> reported at the next board
  Change over SGD 10,000 or critical path     -> CCB
```

Before writing anything, test the numbers against the thresholds and write down what you find:

```text
THRESHOLD TEST - do this yourself before reading on

  Cost variance as a percentage:
      CV% = CV / EV = -22,000 / 249,000 = -8.8%

  The Lab 03 threshold is -5%. Actual is -8.8%.

  -> THE THRESHOLD IS BREACHED. Escalation to the Project Board is
     MANDATORY within 5 working days. It is not a judgement call, it is
     not something to raise at the next scheduled monthly board if that
     is more than 5 days away, and it does not become optional because
     the team believes it is recoverable.

  Schedule variance as a percentage:
      SV% = SV / PV = -19,000 / 268,000 = -7.1%
      SPI 0.929 - behind plan, but no gate date is yet threatened.
      Report, do not escalate.

  Risk: two risks at 20. Both are reportable at the next board.

  The single most common failure with a status report is producing an
  accurate one that does not act on its own contents. A report that
  states CPI 0.919 and then requests no decision has told the board the
  facts and left them with the impression that nothing is required.
```

### Step 7 - Write the same status three ways

Same data, three audiences, three encodings. Write all three into `artifacts/18-status-reports.md`.

**(a) Sponsor one-pager - Priya Nathan, COO. Outcome, risk, decision needed. No jargon, no acronyms, one page.**

```text
CONTOSO TRAINING PORTAL UPGRADE
Sponsor brief - week 14 of 28
For: Priya Nathan, COO      From: [PM]      Date: [date]

WHERE WE ARE
  Just over half the work is done and we are just past half the calendar.
  The registration flow works end to end and was demonstrated to real
  learners in sprint 5. Two-thirds of the must-have features are complete.

THE ONE THING YOU NEED TO KNOW
  We are spending about SGD 1.09 for every dollar of work we are
  completing. If that rate continues to the end, the project finishes at
  approximately SGD 522,000 against the approved SGD 480,000 - an
  overrun of about SGD 42,000, which is 9%.

  This crosses the board's 5% cost threshold, so I am escalating it to
  the Project Board this week as the governance model requires. I am
  bringing you this first.

WHY
  Two causes, both identified and both being worked:
    -  The payment gateway integration has taken longer than planned
       because the vendor's new interface was less stable than they
       stated. That work is now two-thirds complete.
    -  Compliance evidence has needed more analyst time than allowed for.

WHAT I NEED FROM YOU
  A decision at the Project Board on ONE of three options:
    1  Absorb the overrun by removing the two lowest-value must-have
       features. Saves an estimated SGD 38,000. Does not affect the
       registration time or mobile targets. My recommendation.
    2  Approve an increase to the ceiling of SGD 45,000. Requires Group
       Finance and a board ceiling variation.
    3  Move the launch date. NOT recommended - it misses the July intake
       and forfeits the benefit this year.

  I need this decision by week 16. After that, option 1 stops being
  available because the work will have started.

WHAT IS NOT AT RISK
  The 30 June launch date. The registration-time and mobile targets.
  All eight compliance requirements will be met before go-live.

THE OTHER THING WORTH YOUR ATTENTION
  Two of the three administration staff are job hunting because the
  redeployment commitment made in week 8 was never issued. If we lose
  them we lose both our subject-matter experts and our launch-week
  support. This needs the Ops Manager to issue the written statement
  this week. I have asked; your weight would help.
```

**(b) Project Board monthly report - EVM figures, gates, escalations against thresholds.**

```text
CONTOSO TRAINING PORTAL UPGRADE (CTP-2026-01)
Project Board report - period ending week 14
Prepared by: [PM]      Status: AMBER

1  PERFORMANCE AGAINST BASELINE

   BAC   480,000     PV  268,000     EV  249,000     AC  271,000
   CV    -22,000     CV%  -8.8%      CPI  0.919
   SV    -19,000     SV%  -7.1%      SPI  0.929
   EAC    522,306    VAC  -42,306    TCPI (to BAC)  1.10

   Budget spent 56.5%. Work earned 51.9%.
   Contingency reserve released: 9,000 of 26,000.

2  ESCALATION AGAINST THRESHOLDS - BOARD DECISION REQUIRED

   Threshold: cost variance beyond -5%, escalate within 5 working days.
   Actual: -8.8%. BREACHED. This report constitutes that escalation,
   raised on day 2 of the 5.

   Forecast overrun at completion: SGD 42,306 (8.8% of BAC).
   TCPI to complete within BAC is 1.10, against a delivered CPI of 0.919.
   Recovering to budget requires a 20% improvement in cost efficiency
   over the remaining work. The board should treat that as unlikely.

   Options tabled:
     Option 1  Descope 2 must-have items, saving an estimated 38,000.
               No impact on SC-1 to SC-4 targets. Requires CCB approval
               as a scope baseline change. RECOMMENDED.
     Option 2  Ceiling variation of 45,000. Group Finance approval
               required per the governance model.
     Option 3  Schedule extension. Rejected - CON-1, the July intake.

   Decision required by week 16.

   Threshold: schedule variance threatening a gate date.
   Actual: SPI 0.929, no gate date currently threatened. Gate G2 remains
   week 18 on the current velocity of 33 against a capacity of 34.
   REPORTED, NOT ESCALATED.

3  GATES

   G1  Design baseline           Week 6   PASSED
   G2  Build complete            Week 18  On track, 71 of 104 must-haves
   G3  Pre-launch, DPO-owned     Week 24  At risk - see section 4

4  COMPLIANCE

   5 of 8 requirements evidenced and accepted by the DPO.
   Outstanding: consent withdrawal flow; PDPA data retention schedule;
   data processor agreement with the hosting vendor.
   All three are scheduled for sprints 8 and 9. G3 cannot pass with any
   of them open. No board action required at this point.

5  RISK - items scoring 20 or above

   R-03  Payment gateway v2 API instability            P4 x I5 = 20
         Response: vendor support package agreed at SGD 19,500 (CCB
         approved); spike completed; integration two-thirds done.
         Trend: reducing.
   R-07  Loss of admin SME availability                P4 x I5 = 20
         Two of three staff job hunting. Root cause: the week-8
         redeployment communication was not issued.
         Response: Ops Manager to issue a written statement within 5
         working days. BOARD IS ASKED TO NOTE that this risk is
         entirely within Contoso's control and is currently unmitigated.
         Trend: increasing.

6  DELIVERY

   Sprint 7 of 12. Velocity 31, 33, 33 forecast against capacity 34.
   Must-have stories 71 of 104 complete (68%).

7  DECISIONS REQUESTED OF THE BOARD

   D-1  Select option 1, 2 or 3 on the cost overrun.        By week 16.
   D-2  Note R-07 and direct that the redeployment statement is issued.
```

**(c) Team standup and sprint report - backlog, blockers, WIP.**

```text
SPRINT 7 - DAY 4 STANDUP BOARD
Sprint goal: consent withdrawal flow demonstrable in staging.

  COMMITTED 33 pts   |  DONE 14  |  IN PROGRESS 12  |  NOT STARTED 7
  WIP LIMIT: 4 stories in progress. Currently 5. OVER LIMIT.

  IN PROGRESS
    CTP-241  Consent withdrawal UI              Wei Ling    5 pts
    CTP-244  Withdrawal audit trail             Daniel      3 pts
    CTP-238  Gateway refund path                Aisha       5 pts   BLOCKED
    CTP-250  PDPA retention schedule config     Farah       2 pts
    CTP-247  Withdrawal email template          Grace       2 pts

  BLOCKERS
    CTP-238  Vendor sandbox refund endpoint returning 500 since Tuesday.
             Raised with the vendor under the 4-hour SLA on Tuesday
             10:15. No response in 26 hours - the SLA is breached.
             ACTION: PM escalates to the vendor account manager today.
             This is an impediment for the PM to remove, not for Aisha
             to chase.

  WIP OVER LIMIT
    5 in progress against a limit of 4. Nothing new starts until
    CTP-247 or CTP-250 finishes. Pull, do not push.

  DEFINITION OF DONE - TRANSFER GATE
    Two stories are sitting at the QA column boundary. Items 1-7 of the
    definition of done must be demonstrably true before transfer. Kenneth
    has the authority to move them back; that is the process working,
    not an escalation.

  CARRY-OVER RISK
    7 points not started on day 4 of 10. On sprints 5 and 6 velocity we
    finish 33. If CTP-238 is blocked past tomorrow, expect 5 points to
    carry.

  FOR THE TEAM TO KNOW
    Costs are running about 9% above plan across the project. I am taking
    that to the Project Board this week with three options; the one I am
    recommending removes two low-value must-have stories rather than
    asking anyone to work faster. This is a PM problem, not a velocity
    problem. Nobody should read this as pressure to cut corners on the
    definition of done.
```

Now record what changed and what did not:

| Element | Sponsor one-pager | Project Board | Team standup |
| --- | --- | --- | --- |
| CPI 0.919 | "SGD 1.09 spent for every dollar of work" | "CPI 0.919, CV% -8.8%, TCPI 1.10" | "about 9% above plan" |
| EAC 522,306 | "finishes at about SGD 522,000, an overrun of SGD 42,000" | "EAC 522,306, VAC -42,306" | Not reported - not actionable by the team |
| Threshold breach | "crosses the board's 5% threshold, I am escalating this week" | "BREACHED, this report constitutes that escalation, day 2 of 5" | "I am taking that to the Project Board this week" |
| R-07 admin SMEs | Named, with a request for her weight behind it | Logged with score, response, trend and a board direction requested | Not reported - it is not the team's to act on |
| Blocker CTP-238 | Not reported - one blocked story is not sponsor-level | Visible only as the R-03 trend | Full detail, with the PM owning the escalation |
| Underlying data | Identical | Identical | Identical |

```text
THE PRINCIPLE
  Every number in all three reports comes from the same four figures:
  BAC 480,000, PV 268,000, EV 249,000, AC 271,000. Nothing was softened,
  omitted to flatter, or rounded in a favourable direction.

  What changed is ENCODING (jargon out for the sponsor), ALTITUDE
  (blockers out for the sponsor, EAC out for the team) and CALL TO
  ACTION (a decision for the sponsor and board, a reassurance and an
  impediment for the team).

  What did NOT change is the facts. If your sponsor version and your
  board version would lead a reader to different conclusions about
  whether the project is in trouble, you have not tailored - you have
  produced two accounts, and when they meet, your credibility is the
  thing that is lost.
```

### Step 8 - Compare a bad status report with a good one

```text
BAD - week 14 status, the version that gets written under pressure

  "Good progress this period. The team continues to work hard and
   velocity remains strong. Sprint 7 is underway and going well. We are
   tracking against the plan with some minor variances which we are
   managing closely. The payment gateway integration has presented some
   challenges but the team is on top of it. Compliance work continues.
   A couple of risks are being monitored. We remain confident of hitting
   the 30 June date. No issues to raise at this stage."
```

| Defect | Where | Why it matters |
| --- | --- | --- |
| No numbers at all | Throughout | "Some minor variances" describes a -8.8% cost variance identically to a -0.3% one |
| Governance breach concealed | "minor variances which we are managing closely" | A mandatory escalation has been dressed as routine management. This is the serious one |
| Effort reported instead of outcome | "the team continues to work hard" | Effort is not progress. It also implies that if things go wrong the team was not working hard enough |
| Vague risk statement | "a couple of risks are being monitored" | Two risks at score 20, one of them entirely within Contoso's control and currently unmitigated |
| No decision requested | "no issues to raise" | The board leaves believing nothing is needed. A decision that must be taken by week 16 has been silently deferred |
| Optimism as evidence | "we remain confident" | Confidence is not a forecast. EAC 522,306 is |
| Compliance unquantified | "compliance work continues" | 5 of 8 done and 3 outstanding against a gate that cannot pass with any open |
| Bad news buried in soft language | "presented some challenges" | The reader cannot tell whether this is on track or off it, so they will assume on track |

```text
GOOD - the same period, same facts

  "AMBER. Cost variance is -8.8% against a -5% escalation threshold, so
   this report is a formal escalation to the Board under the governance
   model, raised on day 2 of the permitted 5.

   CPI 0.919. EAC 522,306 against a BAC of 480,000: a forecast overrun of
   SGD 42,306. TCPI to recover within budget is 1.10 against a delivered
   0.919, so recovery by efficiency alone should not be assumed.

   Cause: gateway v2 integration effort above plan (vendor interface less
   stable than stated, now two-thirds complete) and analyst effort on
   compliance evidence above plan.

   Schedule: SPI 0.929, behind plan, no gate date currently threatened.
   G2 remains week 18 on current velocity. Reported, not escalated.

   Compliance: 5 of 8 requirements accepted by the DPO; 3 outstanding,
   scheduled for sprints 8 and 9. G3 cannot pass with any open.

   Risks at 20+: R-03 gateway instability, trend reducing. R-07 loss of
   admin SMEs, trend increasing and currently unmitigated - the cause is
   an internal communication that was committed to in week 8 and never
   issued.

   DECISION REQUIRED BY WEEK 16: descope two must-have items saving an
   estimated 38,000 (recommended); or a ceiling variation of 45,000; or a
   schedule extension (not recommended, CON-1). After week 16 the first
   option is no longer available."
```

The difference between the two is not length; the good version is shorter. It is that every sentence carries a number, a threshold, a cause, a trend or a decision. Read your own draft sentence by sentence and delete anything that carries none of the five.

### Step 9 - Answer the exam-style scenarios

```text
SCENARIO 1
A project team of 8 people plus the project manager is expanded by adding 4
more developers to recover a slipping schedule. What happens to the number of
communication channels, and what should the project manager conclude?

  A. Channels increase from 36 to 78, a 117% increase for a 44% increase in
     people; coordination cost grows superlinearly, so the added capacity may
     not produce proportionate output.
  B. Channels increase from 8 to 12, in proportion to the team size.
  C. Channels increase from 36 to 78, which is offset by the additional
     capacity, so throughput will rise by 44%.
  D. The channel count is unchanged because the communication plan already
     defines the channels.

SCENARIO 2
At week 14 the project reports CPI 0.919 and a cost variance of -8.8%. The
governance model requires escalation to the Project Board within 5 working days
for any cost variance beyond -5%. The team believes the variance is recoverable
in the next two sprints and asks you to wait until it is resolved before
reporting it. What should the project manager do?

  A. Wait two sprints. Reporting a variance you expect to recover creates
     unnecessary alarm at board level.
  B. Escalate to the Project Board within 5 working days as the governance
     model requires, presenting the variance, the cause, the forecast and
     options including the team's recovery view.
  C. Report it at the next scheduled monthly board meeting.
  D. Release contingency reserve to cover the variance so the reported figure
     falls back inside the threshold.

SCENARIO 3
You must tell three administration staff that their roles will change
significantly when the new system launches. They have been anxious about
redundancy for eight weeks. What is the BEST communication approach?

  A. A carefully worded email to all three simultaneously so that everyone
     receives identical information at the same moment.
  B. Post the redeployment plan on the company intranet and notify them of
     the link.
  C. An in-person session delivering the written statement, with time for
     questions and a named follow-up date.
  D. Ask their line manager to tell them informally.
```

Answer key:

```text
SCENARIO 1 -> A.  N(N-1)/2. Before: 8 team plus the PM is N=9, giving
            9x8/2 = 36. After: 12 plus the PM is N=13, giving 13x12/2 = 78.
            People rose 44%, channels rose 117%. B applies a linear
            relationship, which is exactly the intuition the formula exists
            to correct. C gets the arithmetic right and the conclusion wrong -
            it assumes coordination is free, when the new members also consume
            existing members' time to onboard, which is Brooks' law and the
            reason "add developers to a late project" is a wrong answer in
            almost every PMP scenario. D confuses planning the channels with
            eliminating them; the plan decides which channels you service, it
            does not change how many exist.

SCENARIO 2 -> B.  The threshold is a governance rule agreed in advance
            precisely so that this judgement is not made under pressure in the
            moment. -8.8% is beyond -5%, so escalation is mandatory and the
            clock is 5 working days. Note that B does not ignore the team - the
            recovery view goes INTO the escalation as one of the options, which
            is the correct place for it. A substitutes the PM's optimism for
            the board's decision right and, if the recovery fails, the board
            learns both that the project is over budget and that it was not
            told; the second is worse. C misses the 5-day clock whenever the
            board is more than a week away, and treats a triggered escalation
            as routine reporting. D is the worst answer: contingency reserve is
            for identified risks in the register, not for making a variance
            disappear from a report, and using it this way is concealment
            dressed as financial management.

SCENARIO 3 -> C.  The content is sensitive, personally consequential, and
            lands on people who have spent eight weeks decoding silence as bad
            news. That combination demands the most interactive method
            available, and the written statement travels with it because what
            they asked for is certainty in writing. A is push for a message
            that will generate immediate questions the sender will not be
            present to answer - identical wording is not the same as identical
            understanding. B is pull for urgent, unwelcome, personal news,
            which is the worst possible pairing of method and content. D
            delegates the delivery to someone who is not accountable for the
            decision and makes it informal, when what this group needs is
            formal certainty. The rule: the harder the message, the more
            interactive the method.
```

## Deliverable

Submit to `artifacts/`:

- `18-communication-plan.md` - the channels table with at least eight computed cases including the 9-to-13 growth comparison showing +44% people against +117% channels; the five written management implications; the push/pull/interactive assignment for at least twelve stakeholders with a justification each; the completed formal/informal by written/verbal grid with at least two Contoso examples per cell; the full communication plan table with all seven columns populated for at least fourteen rows, every one with a named feedback loop; the communication model with at least eight Contoso noise sources, each with a stage, a consequence and a control.
- `18-status-reports.md` - the week-14 underlying data; your own threshold test showing CV% = -8.8% against the -5% threshold and stating that escalation is mandatory within 5 working days; the three tailored status reports; the comparison table showing what changed and what did not; the bad-versus-good report comparison with at least six named defects.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your channel figures are 36 for N=9 and 78 for N=13, and you stated the +44% versus +117% comparison explicitly.
- You derived a management implication from the formula rather than just computing it. If your notes end at "78 channels", you have done the arithmetic and missed the point.
- Every row of your communication plan has a feedback loop that would let you detect a message failing to land. Rows saying "email sent" have no feedback loop.
- Every Resistant or anxious stakeholder in your plan (S-05, S-06, S-08, S-16) receives an interactive element.
- You computed CV% = -22,000 / 249,000 = -8.8% and identified the Lab 03 threshold breach yourself, and your board report states that escalation is mandatory within 5 working days rather than treating it as a judgement call.
- Your three status reports are all traceable to the same four figures - BAC 480,000, PV 268,000, EV 249,000, AC 271,000 - and none of them softens, omits or rounds favourably.
- Your sponsor one-pager contains no acronyms, translates CPI into money, and asks for a specific decision by a specific date.
- Your team report contains blockers and WIP and does not contain EAC. Reporting a forecast at completion to a standup is altitude failure in the other direction.
- Your bad-report critique names the concealed governance breach, not only the missing numbers.
- You noted that Lab 20 derives these EVM figures from raw cost and progress data, and that this lab consumes them rather than computing them.
