# Lab 07 - Stakeholder Register, Power/Interest Grid and Salience Model

| Field | Value |
| --- | --- |
| Topic | 2 - Start the Project |
| ECO 2026 task | People T4 - Engage stakeholders; People T5 - Align stakeholder expectations; People T6 - Manage stakeholder expectations |
| Duration | 50 minutes |
| Consumes | Lab 03 governance bodies; Lab 04 compliance owners; Lab 06 charter, success criteria and exclusions |
| Produces | `artifacts/07-stakeholder-register.md`, `artifacts/07-power-interest-grid.md`, `artifacts/07-salience-model.md`, `artifacts/07-engagement-matrix.md` |

## Objectives

- Identify the full stakeholder set, including the ones projects habitually forget.
- Analyse each stakeholder on power, interest, attitude and impact.
- Plot the power/interest grid and derive the engagement strategy each quadrant demands.
- Apply the salience model to resolve the cases the grid cannot handle.
- Build the current-versus-desired engagement matrix that drives the Lab 18 communication plan.
- Surface and plan to resolve the misaligned expectations already visible in the case.

## Steps

### Step 1 - Identify stakeholders

Identification is not a five-minute brainstorm. Work through categories systematically so you catch the ones that get missed.

| Category | Prompt | Contoso stakeholders found |
| --- | --- | --- |
| Decision makers | Who authorises, funds, or can stop this? | COO (sponsor), Project Board, Group Finance |
| Users | Who uses the product? | Learners, administration staff, trainers |
| Beneficiaries | Who gets the benefit? | Learners, Ops team, Finance, corporate clients |
| Delivery | Who builds it? | The 9-person project team |
| Governance | Who reviews or approves? | DPO, CCB, Head of L&D Ops as product owner |
| Suppliers | Who do we depend on? | Payment gateway vendor, hosting vendor, PDPA assessor |
| Regulators | Who can sanction us? | PDPC, the national training regulator |
| Affected but not consulted | Whose work changes? | The 3 admin staff, support desk, trainers |
| Opponents | Who might resist? | Head of Sales, trainers wary of the change |
| Influencers | Who shapes opinion without formal power? | Senior trainer with 12 years' tenure, IT operations manager |

The row that matters most is "affected but not consulted". The three admin staff whose 24 hours a week of manual work is being automated are the group most affected by this project and the group with the least formal power. Lab 04's sustainability plan already flagged this. If they are not in the register, the register is wrong.

### Step 2 - Build the stakeholder register

Create `artifacts/07-stakeholder-register.md`. Score power and interest 1-5. Attitude uses: Champion, Supporter, Neutral, Resistant, Blocker.

| ID | Stakeholder | Role | Power | Interest | Attitude | Main expectation | Main concern |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | Priya Nathan | COO, sponsor | 5 | 5 | Champion | Launch 30 June within SGD 480,000; abandonment under 15% | Date slipping; board exposure |
| S-02 | Group Finance Director | Board member | 5 | 3 | Neutral | No ceiling breach; benefits actually realised | Cost overrun; unverified benefits |
| S-03 | Marcus Tan | Head of L&D Ops, product owner | 4 | 5 | Champion | Registration speed; manual work eliminated | Team pulled away mid-project |
| S-04 | Data Protection Officer | Compliance gate owner | 5 | 4 | Neutral | Zero major findings; evidence pack complete | Compliance squeezed by schedule pressure |
| S-05 | Head of Sales | Commercial | 3 | 4 | Resistant | Wants the AI recommender in v1 | Competitors ahead on features |
| S-06 | Admin staff (3) | Users, SMEs | 1 | 5 | Neutral, anxious | Job security; a system that works | Redundancy; not being consulted |
| S-07 | Learners (14,000) | End users | 2 | 4 | Neutral | Fast, mobile, self-service registration | Disruption; losing booking history |
| S-08 | Trainers (23) | Affected users | 2 | 3 | Resistant | No change to their scheduling | Extra admin burden landing on them |
| S-09 | Support desk lead | Affected, beneficiary | 2 | 4 | Supporter | Fewer tickets; good handover | Launch-week ticket spike |
| S-10 | Project team (9) | Delivery | 2 | 5 | Supporter | Clear priorities; protected focus | Scope thrash; unrealistic date |
| S-11 | IT Operations Manager | Infrastructure, influencer | 4 | 3 | Neutral | Stable, supportable platform | Being handed unsupportable software |
| S-12 | Payment gateway vendor | Supplier | 3 | 2 | Neutral | Clean v2 migration | Low - we are a small account |
| S-13 | Hosting vendor | Supplier | 2 | 2 | Neutral | Contract renewal | Low |
| S-14 | PDPC | Regulator | 5 | 1 | Neutral | Lawful data handling | None unless we breach |
| S-15 | National training regulator | Regulator, funder | 5 | 2 | Neutral | Valid funding claim data | None unless claims fail |
| S-16 | Senior trainer (12 yrs) | Influencer | 2 | 3 | Resistant | To be consulted, not informed | Loss of informal influence |
| S-17 | Corporate clients (top 8) | Customers | 3 | 3 | Neutral | No disruption to bulk bookings | Service interruption at launch |

### Step 3 - Plot the power/interest grid

Create `artifacts/07-power-interest-grid.md`. Power 4-5 is high; interest 4-5 is high.

```text
        HIGH POWER
             |
   KEEP      |  MANAGE CLOSELY
 SATISFIED   |
             |  S-01 COO (5,5)
  S-02 Fin   |  S-03 Head L&D Ops (4,5)
  Dir (5,3)  |  S-04 DPO (5,4)
  S-14 PDPC  |
     (5,1)   |
  S-15 Reg   |
     (5,2)   |
  S-11 IT Ops|
     (4,3)   |
-------------+---------------------------  HIGH INTEREST -->
             |
   MONITOR   |  KEEP INFORMED
             |
  S-13 Host  |  S-05 Head of Sales (3,4)
     (2,2)   |  S-06 Admin staff (1,5)
  S-12 Gwy   |  S-07 Learners (2,4)
     (3,2)   |  S-08 Trainers (2,3)
  S-16 Snr   |  S-09 Support lead (2,4)
   trainer   |  S-10 Project team (2,5)
     (2,3)   |  S-17 Corporate clients (3,3)
             |
        LOW POWER
```

Derive the strategy each quadrant demands:

| Quadrant | Strategy | Contoso application |
| --- | --- | --- |
| High power, high interest - **Manage closely** | Involve in decisions, engage frequently, seek agreement not just approval | COO: weekly 1:1. Head of L&D Ops: daily as product owner. DPO: fortnightly plus gate reviews |
| High power, low interest - **Keep satisfied** | Report at their level, do not overload, escalate only what matters to them | Finance Director: monthly financial summary only. Regulators: contact only via defined compliance evidence. IT Ops: architecture review at G1 and G2 |
| Low power, high interest - **Keep informed** | Frequent, honest communication; they will be your advocates or your critics | Admin staff: weekly session. Learners: launch comms plan. Project team: daily standup |
| Low power, low interest - **Monitor** | Minimal effort, watch for changes in position | Hosting vendor, gateway vendor |

The common error is treating "keep satisfied" as "ignore" and "keep informed" as "send an email occasionally". Both are active strategies.

### Step 4 - Apply the salience model where the grid fails

The power/interest grid has a blind spot: it cannot distinguish a stakeholder with a legitimate claim from one who is merely loud, and it has no concept of urgency. The salience model adds those two dimensions.

```text
SALIENCE MODEL - three attributes

  POWER        Can they impose their will? Do they control resources,
               authority, or the ability to stop the project?
  LEGITIMACY   Is their claim appropriate and proper? Do they have a
               right to be involved?
  URGENCY      Is their claim time-sensitive and important to them now?

  ONE attribute   = LATENT stakeholder
     Power only          -> DORMANT     (power they are not using)
     Legitimacy only     -> DISCRETIONARY (deserve attention, no pressure)
     Urgency only        -> DEMANDING   (noisy, no power, no valid claim)

  TWO attributes  = EXPECTANT stakeholder
     Power + Legitimacy  -> DOMINANT    (the classic important stakeholder)
     Power + Urgency     -> DANGEROUS   (coercive; can act without right)
     Legitimacy + Urgency-> DEPENDENT   (valid, pressing, needs an advocate)

  THREE attributes = DEFINITIVE stakeholder
     Immediate priority. Act now.
```

Create `artifacts/07-salience-model.md` and classify the difficult cases:

| Stakeholder | Power | Legitimacy | Urgency | Class | What it changes |
| --- | --- | --- | --- | --- | --- |
| S-01 COO | Yes | Yes | Yes | **Definitive** | Highest priority, always |
| S-04 DPO | Yes | Yes | Yes | **Definitive** | Cannot be deprioritised; holds a gate |
| S-06 Admin staff | No | Yes | Yes | **Dependent** | They have a legitimate, urgent claim and no power to press it. They need YOU as advocate. The grid put them in "keep informed" and would have under-served them |
| S-05 Head of Sales | Yes | No (for v1 AI) | Yes | **Dangerous** | Can act coercively - going around you to the sponsor - on a claim already assessed and excluded. Manage the relationship; do not concede the substance |
| S-14 PDPC | Yes | Yes | No | **Dominant** | Real authority, no current claim. Keep satisfied through compliance evidence |
| S-16 Senior trainer | No | Yes | No | **Discretionary** | Deserves consultation; no pressure. Low-cost, high-return to consult |
| S-07 Learners | No | Yes | No | **Discretionary** | Legitimate but unorganised. The product owner represents them; usability testing gives them voice |
| S-11 IT Ops | Yes | Yes | No | **Dominant** | Will become definitive at handover. Engage early or inherit an objection late |

The two insights the salience model produces that the grid did not:

```text
S-06, the admin staff, are DEPENDENT. Legitimate and urgent claim, zero power.
Dependent stakeholders are the ones organisations damage most often, precisely
because there is no consequence for ignoring them. The PM's job is to be their
advocate. This is where the Lab 04 sustainability commitment becomes real.

S-05, Head of Sales, is DANGEROUS. Not because he is a bad actor, but because
he has power and urgency without legitimacy on this specific claim - the AI
recommender was assessed and excluded with rationale. Dangerous stakeholders
are managed by strengthening the legitimate route (the change request process)
and by keeping the sponsor pre-informed, so a direct approach lands on someone
who already has the facts.
```

### Step 5 - Build the engagement matrix

Create `artifacts/07-engagement-matrix.md`. Levels: Unaware, Resistant, Neutral, Supportive, Leading. Mark C for current and D for desired.

| Stakeholder | Unaware | Resistant | Neutral | Supportive | Leading |
| --- | --- | --- | --- | --- | --- |
| S-01 COO | | | | | C/D |
| S-02 Finance Director | | | C | D | |
| S-03 Head of L&D Ops | | | | | C/D |
| S-04 DPO | | | C | D | |
| S-05 Head of Sales | | C | D | | |
| S-06 Admin staff | | | C | D | |
| S-07 Learners | C | | | D | |
| S-08 Trainers | | C | D | | |
| S-09 Support desk lead | | | | C/D | |
| S-10 Project team | | | | C | D |
| S-11 IT Ops Manager | | | C | D | |
| S-16 Senior trainer | | C | | D | |
| S-17 Corporate clients | C | | D | | |

Every gap between C and D needs an action. Gaps without actions are observations, not plans.

| Stakeholder | Gap | Action to close it | Owner | By when |
| --- | --- | --- | --- | --- |
| S-05 Head of Sales | Resistant -> Neutral | Present the Lab 02 scored scan and the Lab 05 option analysis; offer a phase-2 roadmap slot with a decision date | PM | Week 3 |
| S-06 Admin staff | Neutral -> Supportive | Redeployment plan agreed and communicated by week 8, before the automation is visible; involve them as SMEs with capped hours so they shape the tool | PM + Ops Manager | Week 8 |
| S-08 Trainers | Resistant -> Neutral | Demonstrate that trainer admin does not increase; show the scheduling exclusion OUT-5 | BA | Week 6 |
| S-16 Senior trainer | Resistant -> Supportive | Consult directly on the communications wording; invite to sprint review 3 | PM | Week 7 |
| S-04 DPO | Neutral -> Supportive | Involve in the privacy-by-design workshop in sprint 1 rather than presenting finished screens at G3 | BA | Sprint 1 |
| S-07 Learners | Unaware -> Supportive | Usability testing from sprint 3; launch communications plan; migration reassurance about booking history | UX Lead | Sprint 3 |
| S-11 IT Ops | Neutral -> Supportive | Architecture review at G1; supportability requirements accepted into the backlog | Dev Lead | Week 6 |
| S-02 Finance Director | Neutral -> Supportive | Monthly one-page financial summary with CPI/SPI from Lab 20 | PM | Monthly |

Note the pattern in the highest-value actions: involve people *before* the decision rather than presenting them with the result. The DPO action moves a compliance review from an adversarial gate to a collaborative design input, which is also the Lab 03 lessons-learned recommendation.

### Step 6 - Surface and resolve misaligned expectations

ECO People T5 requires you to "facilitate discussions to align expectations". You cannot align what you have not written down. Three misalignments are already visible in the case.

| # | Misalignment | Party A believes | Party B believes | Resolution approach |
| --- | --- | --- | --- | --- |
| M-1 | Scope of v1 | Head of Sales: AI recommender is essential to v1 | COO: registration speed is the only priority | Joint session with both, using the Lab 02 scored factors and the Lab 05 NPV comparison. Outcome: written phase-2 commitment with a review date, or a change request. Do not let this stay implicit |
| M-2 | Admin staff future | Admin staff: fear redundancy | Ops Manager: intends redeployment but has not said so | Ops Manager states the redeployment plan in writing by week 8. Silence is being read as bad news |
| M-3 | Compliance timing | PM plan: 3-week review | DPO: has not committed; prior review took 3 weeks but scope was smaller | Confirm scope and booking with the DPO by week 4, per assumption A-05 |

For M-1, plan the facilitated session properly:

```text
EXPECTATION ALIGNMENT SESSION - M-1

  Attendees   COO (decides), Head of Sales, Head of L&D Ops, PM
  Duration    60 minutes
  Inputs      Lab 02 ranked factors (AI 16, mobile 25)
              Lab 05 three-option NPV comparison
              Charter exclusion OUT-1 and its rationale
              Team capacity: 34 story points per sprint (Lab 10)

  Structure
    1. Restate the shared goal - both parties want Contoso competitive.
       Establish common ground before difference.
    2. Present the evidence, not opinions. Scores and NPV.
    3. Make the trade-off explicit and concrete: the AI recommender is
       approximately 55 story points, which is 1.6 sprints. Delivering it
       means dropping mobile responsiveness or moving the launch date.
       Ask which of those two the group prefers.
    4. Offer the third path: a dated phase-2 decision point, so the request
       is deferred rather than refused.
    5. COO decides. Record the decision, the rationale and the review date.
    6. Communicate the decision to both parties in writing within 24 hours.

  Why this works: the argument stops being "is AI important" - to which
  everyone says yes - and becomes "which of these two things do we give up",
  which is a question that can actually be answered.
```

### Step 7 - Set the engagement cadence

| Stakeholder group | Channel | Frequency | Owner | Content |
| --- | --- | --- | --- | --- |
| S-01 COO | 1:1 meeting | Weekly, 30 min | PM | Progress, risks, decisions needed |
| S-02 Finance Director | Written summary | Monthly | PM | Cost, CPI/SPI, forecast |
| S-03 Head of L&D Ops | Working session | Daily + sprint ceremonies | PM | Backlog, priorities, acceptance |
| S-04 DPO | Review meeting | Fortnightly + gates | BA | Compliance coverage fraction |
| S-05 Head of Sales | Meeting | Monthly | PM | Roadmap, phase-2 status |
| S-06 Admin staff | Group session | Weekly, 30 min | Ops Manager | Progress, training, redeployment |
| S-07 Learners | Usability sessions, then launch comms | Sprint 3, 5, 7; launch | UX Lead | Test the product, then announce |
| S-08, S-16 Trainers | Briefing | Monthly | BA | Impact on them specifically |
| S-10 Project team | Standup, review, retro | Daily / fortnightly | PM | Everything |
| S-11 IT Ops | Architecture review | At G1, G2, handover | Dev Lead | Supportability |
| S-17 Corporate clients | Account manager briefing | Pre-launch and launch | Head of Sales | Continuity assurance |

This table becomes the input to the Lab 18 communication plan, where you will size it against the channels formula.

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
The Head of Sales emails the COO directly saying the project team is "refusing
to consider the market reality" on the AI recommender. The COO forwards it to
you with "thoughts?". What do you do FIRST?

  A. Reply to the COO defending the decision with the scan and NPV data.
  B. Meet the Head of Sales to understand what has changed since the last
     discussion, then respond to the COO with the facts and a recommendation.
  C. Add the AI recommender to the backlog as a low priority.
  D. Ask the COO to instruct the Head of Sales to use the change process.

SCENARIO 2
Three weeks before launch, an administrator tells you privately that the admin
team believes they will be made redundant and two are actively job hunting.
Losing them would cost you your SMEs and your launch support. What is the
BEST action?

  A. Reassure her personally that their jobs are safe.
  B. Report it to the Ops Manager as a resourcing risk.
  C. Escalate to the Ops Manager that the week-8 redeployment communication
     was never made, and get a written, communicated plan this week.
  D. Add a risk to the register and monitor it.

SCENARIO 3
Which classification best fits a stakeholder with a legitimate and urgent claim
but no power to enforce it, and what does the classification demand of the PM?

  A. Dominant - keep satisfied.
  B. Dangerous - manage the relationship carefully.
  C. Dependent - the PM must advocate on their behalf.
  D. Discretionary - consult if convenient.
```

Answer key:

```text
SCENARIO 1 -> B.  Engage the stakeholder before responding about them. Something
            may genuinely have changed - a competitor announcement, a lost deal -
            which would be new information legitimately worth assessing. A
            responds without checking. D asks the sponsor to manage a
            relationship that is yours to manage. C concedes scope quietly,
            which is the worst outcome.

SCENARIO 2 -> C.  This is the M-2 misalignment materialising exactly as
            predicted, because the week-8 action was not done. A makes a promise
            you have no authority to make - and if it turns out false you have
            destroyed your credibility with the group. B and D record the
            problem without fixing it. The fix is the communication that should
            already have happened.

SCENARIO 3 -> C.  Dependent. Legitimacy plus urgency, no power. The defining
            feature is that they cannot press their own claim, so it goes
            unaddressed unless someone with access acts for them. That is the
            PM. This is the admin staff, S-06.
```

## Deliverable

Submit to `artifacts/`:

- `07-stakeholder-register.md` - at least 15 stakeholders with power, interest, attitude, expectation and concern, including at least one regulator, one supplier, one opponent and one affected-but-not-consulted group.
- `07-power-interest-grid.md` - the plotted grid with all stakeholders placed and the four quadrant strategies stated.
- `07-salience-model.md` - the three attributes assessed for at least 8 stakeholders, with classifications, including at least one dependent and one dangerous.
- `07-engagement-matrix.md` - current and desired levels, with a named action, owner and date for every gap.
- The three misalignments with resolution approaches, and a full facilitation plan for M-1.
- The engagement cadence table.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your register includes the three admin staff. A register listing only powerful people is a list of bosses, not a stakeholder register.
- Every stakeholder has a numeric power and interest score, and their grid position matches those scores.
- Your salience analysis produced at least one insight the grid did not - if both tools gave you identical conclusions, you applied the grid twice.
- You identified the admin staff as dependent and stated that the PM's role is advocacy.
- Every C-to-D gap in the engagement matrix has an action with an owner and a date. Gaps with no action are not a plan.
- Your M-1 facilitation plan converts the disagreement into a concrete trade-off with a number attached (55 story points / 1.6 sprints), rather than a debate about importance.
- Your engagement cadence has different frequencies for different stakeholders. If everyone gets a fortnightly email, you have not tailored anything - and People T4 explicitly requires tailored communication.
