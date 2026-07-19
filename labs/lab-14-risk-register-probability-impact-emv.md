# Lab 14 - Risk Register, RBS, EMV and Decision Tree

| Field | Value |
| --- | --- |
| Topic | 3 - Plan the Project |
| ECO 2026 task | Business Environment T5 - Plan and manage risk; Business Environment T4 - Support organisational change |
| Duration | 45 minutes |
| Consumes | Lab 02 PESTLE/TECOP factors; Lab 06 assumption log A-01 to A-07; Lab 13 contingency reserve; Lab 04 compliance threats |
| Produces | `artifacts/14-risk-register.md`, `artifacts/14-rbs.md`, `artifacts/14-pi-matrix.md`, `artifacts/14-emv-analysis.md` |

## Objectives

- Build a risk breakdown structure and use it to identify risks systematically rather than by brainstorm alone.
- Trace risks from the Lab 02 environment scan and the Lab 06 assumption log, since every assumption is a latent risk.
- Write risk statements in cause-event-effect form so that the cause can be attacked and the effect can be priced.
- Assess risks qualitatively on a probability/impact matrix and quantitatively by expected monetary value.
- Select response strategies from all ten - five for threats, five for opportunities.
- Build and solve a decision tree for a real Contoso decision, and defend the recommendation.
- Distinguish secondary risk, residual risk, triggers, and the point at which a risk becomes an issue.

## The vocabulary the exam requires you to use precisely

```text
RISK   An UNCERTAIN event or condition that, IF it occurs, has a POSITIVE
       or NEGATIVE effect on one or more project objectives.
       Two words carry the definition: UNCERTAIN and EFFECT-ON-OBJECTIVE.
       A certainty is not a risk - it is a constraint or a fact to plan
       around. An uncertainty with no effect on an objective is noise.

  INDIVIDUAL RISK   A single event affecting one or more objectives.
  OVERALL RISK      The effect of uncertainty on the project AS A WHOLE,
                    including the combined effect of individual risks.
                    A project can have every individual risk under control
                    and still carry unacceptable overall risk.

THREAT        A risk with a negative effect.
OPPORTUNITY   A risk with a positive effect. Opportunities are risks, they
              belong in the same register, and omitting them is the single
              most common failing in real risk registers.

ISSUE   A risk that HAS OCCURRED, or a current condition that will affect
        objectives. The distinction is tense: a risk MAY happen, an issue
        HAS happened. Risks go in the risk register and are managed by
        response strategies; issues go in the issue log and are managed by
        resolution and escalation. The moment a risk occurs it stops being
        a risk - close it in the register and open it in the issue log.
        Managing an occurred risk as though it were still a risk is how
        issues go unresolved.

RISK APPETITE     The degree of uncertainty an organisation is WILLING to
                  ACCEPT in anticipation of a reward. High-level, strategic.
                  "Contoso is risk-averse on compliance and moderately
                   risk-tolerant on feature scope."
RISK TOLERANCE    The measurable degree of acceptable variation around an
                  objective.
                  "Cost tolerance is zero above SGD 480,000."
RISK THRESHOLD    The specific level at which action is required - the
                  trigger point on the tolerance.
                  "Any risk scoring 20 or above escalates to the sponsor."
  Appetite is the philosophy, tolerance is the range, threshold is the
  line. Exam questions frequently offer all three as options.

SECONDARY RISK    A NEW risk created BY implementing a risk response.
                  Real, common, and routinely forgotten.
RESIDUAL RISK     The exposure that REMAINS after responses are applied.
                  Residual risk is expected and accepted; it is what the
                  contingency reserve in Lab 13 was sized against.
RISK TRIGGER      An observable warning sign that a risk is about to occur
                  or is occurring. A risk without a trigger cannot be
                  monitored - you will discover it by its consequences.
```

## Steps

### Step 1 - Build the risk breakdown structure

Create `artifacts/14-rbs.md`. The RBS is a hierarchy of risk SOURCES. Its purpose is systematic identification: working through categories catches risks that free brainstorming misses, because brainstorming surfaces what is memorable rather than what is likely.

```text
RISK BREAKDOWN STRUCTURE - Contoso Training Portal Upgrade

0.  PROJECT RISK
    |
    +-- 1.  TECHNICAL
    |       +-- 1.1  Requirements definition and stability
    |       +-- 1.2  Technology and architecture
    |       +-- 1.3  Technical interfaces and integration
    |       +-- 1.4  Performance and capacity
    |       +-- 1.5  Data quality, migration and integrity
    |       +-- 1.6  Security and privacy engineering
    |
    +-- 2.  EXTERNAL
    |       +-- 2.1  Regulatory and legislative change
    |       +-- 2.2  Suppliers and vendors
    |       +-- 2.3  Market and competitor movement
    |       +-- 2.4  Regulatory and data protection policy
    |       +-- 2.5  Infrastructure and hosting providers
    |
    +-- 3.  ORGANISATIONAL
    |       +-- 3.1  Resource availability and competence
    |       +-- 3.2  Funding and financial constraint
    |       +-- 3.3  Competing priorities and portfolio conflict
    |       +-- 3.4  Organisational change and staff impact
    |       +-- 3.5  Governance and decision latency
    |
    +-- 4.  PROJECT MANAGEMENT
            +-- 4.1  Estimating and planning accuracy
            +-- 4.2  Scope control and change management
            +-- 4.3  Communication and stakeholder engagement
            +-- 4.4  Schedule and dependency management
            +-- 4.5  Quality planning and control
```

```text
WHY THE RBS COMES BEFORE IDENTIFICATION, not after

  Used as a CHECKLIST, the RBS forces you to ask "what could go wrong in
  category 2.4?" - a question nobody asks spontaneously, and which at
  Contoso produces R-14, the PDPA data protection specification change.

  Used as an ANALYSIS TOOL after identification, the RBS shows CONCENTRATION.
  Count the Contoso risks by category:
      Technical         6 risks
      External          4 risks
      Organisational    4 risks
      Project Mgmt      4 risks
  Reasonably distributed. A register with 15 technical risks and one
  organisational risk does not describe a project with no people problems;
  it describes a technical team that identified risks in the domain it
  understands. Concentration in the RBS is usually a fact about the
  identifiers, not about the project.
```

### Step 2 - Trace risks from Lab 02 factors and Lab 06 assumptions

Risk identification is not invention. Most risks on a well-run project are already sitting in earlier artifacts, unlabelled.

**From the Lab 02 PESTLE/TECOP scan:**

| Lab 02 factor | Factor description | Becomes risk |
| --- | --- | --- |
| L1 Legal | PDPA enforcement activity increased; personal data directly exposed | R-08 penetration test finds a major vulnerability; R-06 DPO review overruns |
| E1 Economic | Client L&D budgets down 8% | R-14 PDPA data protection specification change (regulatory policy pressure) |
| E2 Economic | Fixed board ceiling with reserve inside it | R-12 no management reserve for unforeseen events |
| T1 Technological | Payment gateway v1 being deprecated | R-01 gateway v2 API unstable |
| O1 Organisational (TECOP) | Admin staff capacity already stretched | R-09 admin SMEs unavailable |
| P1 TECOP - People | Key skills concentrated in few individuals | R-03 key developer unavailable |

**From the Lab 06 assumption log - every assumption is a latent risk:**

```text
THE ASSUMPTION-TO-RISK CONVERSION

  An assumption is something taken as TRUE WITHOUT PROOF. The risk is
  simply the assumption being FALSE. This conversion is mechanical, and
  it is the highest-yield risk identification technique available to you
  because the analytical work was already done in Lab 06.

  A-01  "Abandonment will fall to 15% with the new flow"
        -> R-07  Performance and usability targets missed
  A-02  "The full 9-person team is available for six months"
        -> R-03  Key developer unavailable during build
  A-03  "The gateway v2 API is stable and documented"
        -> R-01  Gateway v2 API unstable, integration rework
  A-04  "Legacy learner data is clean enough to migrate"
        -> R-02  Legacy data quality worse than assumed
  A-05  "The DPO can complete the compliance review in 3 weeks"
        -> R-06  DPO review exceeds 3 weeks
  A-06  "PDPA data protection rules will not change before launch"
        -> R-14  PDPA data protection specification changes
  A-07  "The three admin staff will be available as SMEs"
        -> R-09  Admin SMEs unavailable

  WORKED IN FULL - A-05 becoming R-06:

    ASSUMPTION A-05  "The DPO can complete the compliance review in three
                      weeks." Basis: the prior project took three weeks.
                      Weakness in the basis: the prior project's compliance
                      scope was SMALLER, so the analogue is imperfect - and
                      Lab 06 recorded that explicitly.

    RISK R-06        "As a result of the DPO's compliance review scope
                      being larger than the prior project on which the
                      three-week estimate was based, the review may take
                      six weeks rather than three, which would delay UAT
                      and threaten the fixed 30 June launch date."

    Note what the conversion preserves: the CAUSE is the imperfect
    analogue, which is attackable - confirm scope and booking with the DPO
    by week 4. The assumption's validation date becomes the risk's
    mitigation deadline. This is the same situation as the Lab 01
    Scenario 2 exam question, and the whole point is that it is now
    visible in week 1 rather than discovered in week 20.
```

### Step 3 - Write risk statements in cause-event-effect form

```text
THE REQUIRED FORM

  "As a result of <CAUSE>, <EVENT> may occur, which would lead to <EFFECT>."

    CAUSE   A FACT. Something true today. Not uncertain.
    EVENT   The UNCERTAIN occurrence. This is the risk itself.
    EFFECT  The consequence FOR A PROJECT OBJECTIVE - cost, schedule,
            scope or quality. Quantified wherever possible.

  WHY THE FORM MATTERS - it is not bureaucratic pedantry:

    The CAUSE is where MITIGATION acts. You cannot reduce the probability
    of an event directly; you act on its cause. A risk statement without a
    cause gives you nothing to attack, which is why registers full of
    single-line risks generate responses like "monitor closely".

    The EFFECT is where CONTINGENCY and IMPACT are priced. A risk
    statement without a quantified effect cannot be scored, cannot be
    ranked, and cannot contribute to the EMV that sized the Lab 13
    reserve.

  BAD:  "Data migration risk."
        No cause to attack, no event to detect, no effect to price.

  BAD:  "The migration might go wrong."
        An event with no cause and an unpriceable effect.

  GOOD: "As a result of no data profiling having been performed on the
         nine-year-old legacy learner database, the data may contain
         duplicate and malformed records beyond the volume assumed in the
         estimate, which would lead to an additional SGD 18,000 of
         cleansing effort and a 6-day delay to the migration rehearsal."

  Read the good version and notice that the response writes itself:
  profile the data in sprint 2. The cause names the gap.
```

### Step 4 - Build the risk register

Create `artifacts/14-risk-register.md`. Probability is given as a decimal and as a 1-5 score. Impact is scored 1-5, with the cost impact in SGD and the schedule impact in days.

| ID | RBS | Risk statement (cause - event - effect) | P (dec) | P (1-5) | I (1-5) | Cost impact | Sched impact | Score PxI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | 1.3 | As a result of the gateway v2 API being newly released and validated only by vendor announcement, the API may prove unstable or incompletely documented, which would lead to integration rework | 0.35 | 3 | 5 | 42,000 | 12 d | **15** |
| R-02 | 1.5 | As a result of no data profiling having been performed on the legacy database, data quality may be worse than assumed, which would lead to additional cleansing effort | 0.25 | 2 | 4 | 18,000 | 6 d | **8** |
| R-03 | 3.1 | As a result of the team commitment being verbal rather than written, a key developer may be reassigned mid-build, which would lead to lost velocity and knowledge | 0.30 | 3 | 4 | 15,000 | 8 d | **12** |
| R-04 | 1.5 | As a result of the 24-month migration boundary not having been volume-tested, migration volume may exceed the estimate, which would lead to extended migration windows | 0.20 | 2 | 4 | 22,000 | 5 d | **8** |
| R-05 | 4.2 | As a result of the product owner having authority to reorder the backlog each sprint, undeclared scope may enter through story refinement, which would lead to Must-have work being displaced | 0.40 | 4 | 3 | 9,000 | 4 d | **12** |
| R-06 | 3.5 | As a result of the three-week DPO review estimate resting on a smaller prior project, the compliance review may take six weeks, which would lead to UAT delay against a fixed launch date | 0.15 | 2 | 5 | 30,000 | 15 d | **10** |
| R-07 | 1.4 | As a result of the 2.0-second performance budget being unvalidated on the target infrastructure, the target may be missed at load, which would lead to optimisation rework late in the build | 0.25 | 2 | 4 | 12,000 | 7 d | **8** |
| R-08 | 1.6 | As a result of legacy consent and session handling being carried into the new platform, the penetration test may find a major vulnerability, which would lead to remediation before G3 clearance | 0.10 | 1 | 5 | 35,000 | 10 d | **5** |
| R-09 | 3.4 | As a result of the three admin staff having no capped SME allocation and fearing redundancy, they may become unavailable as subject matter experts, which would lead to requirements gaps and weak training | 0.30 | 3 | 3 | 8,000 | 5 d | **9** |
| R-10 | 1.2 | As a result of accessibility conformance being verified only at audit, WCAG failures may be found late, which would lead to rework of completed learner-facing pages | 0.20 | 2 | 4 | 14,000 | 6 d | **8** |
| R-11 | 4.1 | As a result of the 34-point velocity being drawn from two prior projects with different team composition, actual velocity may fall below 34, which would lead to committed scope not fitting the 12 sprints | 0.45 | 4 | 3 | 6,000 | 8 d | **12** |
| R-12 | 3.2 | As a result of the contingency reserve sitting inside a fixed ceiling with no management reserve, an unforeseen event may exhaust available funds, which would lead to forced scope reduction or a ceiling variation request | 0.15 | 2 | 5 | 20,000 | 0 d | **10** |
| R-13 | 4.2 | As a result of stakeholder expectations remaining misaligned on v1 scope (Lab 07 M-1), requirements churn may continue after baseline, which would lead to rework and change control load | 0.25 | 2 | 3 | 7,000 | 4 d | **6** |
| R-14 | 2.4 | As a result of a PDPA data protection advisory expected in Q3, the data protection specification may change before launch, which would lead to rework of attendance and fee handling | 0.10 | 1 | 5 | 26,000 | 8 d | **5** |
| R-15 | 2.5 | As a result of environment provisioning depending on an external hosting vendor with no contractual lead time, environments may be delivered late, which would lead to blocked build and test activity | 0.35 | 3 | 2 | 5,000 | 4 d | **6** |
| R-16 | 3.4 | As a result of the week-8 redeployment communication to admin staff being unconfirmed, one or more admin staff may resign before handover, which would lead to loss of operational knowledge at launch | 0.20 | 2 | 3 | 9,000 | 3 d | **6** |
| O-01 | 1.2 | As a result of a prior Contoso project having built a reusable notification component, that component may be adaptable to this build, which would lead to reduced development effort | 0.30 | 3 | 3 | -12,000 | -5 d | **9** |
| O-02 | 2.2 | As a result of the penetration test vendor having early-window availability, the security test may be brought forward, which would lead to earlier finding resolution and reduced schedule risk | 0.25 | 2 | 3 | -8,000 | -4 d | **6** |

**Responses, owners, triggers and residual exposure:**

| ID | Strategy | Response detail | Owner | Trigger | Secondary risk | Residual P |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Mitigate | Sprint 1 spike against the v2 sandbox to validate A-03 before committing the integration design; maintain v1 fallback until the spike clears | Dev lead | Spike reports undocumented endpoints or sandbox instability | Spike consumes sprint 1 capacity, reducing early velocity | 0.15 |
| R-02 | Mitigate | Data profiling in sprint 2, ahead of migration script build; cleansing rules agreed before scripting | BA | Profiling finds duplicate rate above 4% | Profiling delays migration script start by up to 3 days | 0.15 |
| R-03 | Mitigate | Written resource commitment from functional managers by week 2; pair programming on the two highest-knowledge areas | PM | Any resource reassignment request received | Pairing reduces raw throughput by roughly 10% | 0.20 |
| R-04 | Mitigate | Volume-test the 24-month boundary during sprint 2 profiling; confirm OUT-6 exclusion is correctly applied | DevOps | Extract row count exceeds estimate by 20% | None material | 0.10 |
| R-05 | Mitigate | Every story maps to a work package per the Lab 11 mapping rule; stories mapping to nothing require a change request | PM | A story appears in refinement with no work package | Additional refinement overhead each sprint | 0.25 |
| R-06 | Mitigate | Confirm review scope and booking with the DPO by week 4; involve the DPO in sprint 2 privacy-by-design rather than presenting at G3 | PM | DPO has not confirmed scope by end of week 4 | Early DPO involvement consumes DPO time the review then needs | 0.10 |
| R-07 | Mitigate | Establish the performance budget in sprint 1 and measure every sprint from sprint 4; load test at 400 concurrent before G2 | Dev lead | Any sprint measurement exceeds 1.6s at the 95th percentile | Continuous measurement adds CI time | 0.15 |
| R-08 | Mitigate | Replace legacy consent and session handling rather than migrating it; security review at design stage | Dev lead | Design review flags a carried-over legacy pattern | Rebuild costs more than migration would have | 0.05 |
| R-09 | Mitigate | Capped SME hours agreed per sprint by week 2; redeployment plan communicated by week 8 per Lab 07 action M-2 | Ops Manager | Any SME session cancelled twice consecutively | Capped hours may under-serve requirements depth | 0.20 |
| R-10 | Mitigate | Accessibility built into the design system (WBS 1.3.3), not audited in at the end; automated scan in CI from sprint 3 | UX designer | Any CI scan returns a level A or AA failure | Design system work delays first build sprint | 0.10 |
| R-11 | Mitigate | Measure velocity from sprint 1; re-forecast at sprint 3 and sprint 6; the 42 points of Coulds are the declared release valve | PM | Two consecutive sprints below 30 points | Dropping Coulds reduces delivered value | 0.25 |
| R-12 | Escalate | Ceiling variation path pre-agreed with Group Finance at baseline, with the trigger defined as a forecast EAC above SGD 470,000 | Sponsor | Forecast EAC exceeds SGD 470,000 | Pre-agreeing a variation path may reduce cost discipline | 0.10 |
| R-13 | Mitigate | Run the Lab 07 M-1 expectation alignment session in week 3 with the trade-off arithmetic from Lab 10 | PM | Any v1 scope request raised outside change control | Session may harden positions rather than resolve them | 0.15 |
| R-14 | Accept (active) | Monitor PDPC announcements per the Lab 02 cadence; hold SGD 1,300 of contingency against it; fee display isolated in the architecture to limit rework | BA | The PDPC issues a consultation or advisory | None | 0.05 |
| R-15 | Transfer | Contractual lead time and delivery date with the hosting vendor, with service credits for late provisioning | DevOps | Vendor misses the environment confirmation date | Contract negotiation consumes DevOps time in week 1 | 0.20 |
| R-16 | Mitigate | Redeployment plan written and communicated by week 8; admin staff involved as SMEs so their expertise is visibly valued | Ops Manager | Any admin staff resignation or leave request | None | 0.15 |
| O-01 | Enhance | Allocate 2 days in sprint 1 to assess and adapt the reusable component; raise the probability of realising it | Dev lead | Component assessment confirms fit | Adapting inherited code may carry unknown defects | 0.40 |
| O-02 | Exploit | Book the pen test vendor's early window now rather than waiting for the planned schedule slot | PM | Vendor confirms the early window | Testing an incomplete build produces findings needing re-test | 0.35 |

### Step 5 - Plot the probability/impact matrix

Create `artifacts/14-pi-matrix.md`. Score = probability score x impact score, both on 1-5.

```text
PROBABILITY / IMPACT MATRIX - threats

              IMPACT ->
          1        2        3        4        5
       +--------+--------+--------+--------+--------+
   5   |   5    |  10    |  15    |  20    |  25    |
       |        |        |        |        |        |
       +--------+--------+--------+--------+--------+
   4   |   4    |   8    |  12    |  16    |  20    |
   P   |        |        | R-05   |        |        |
   R   |        |        | R-11   |        |        |
   O   +--------+--------+--------+--------+--------+
   B   |   3    |   6    |   9    |  12    |  15    |
   A   |        | R-15   | R-09   | R-03   | R-01   |
   B   |        |        |        |        |        |
   I   +--------+--------+--------+--------+--------+
   L   |   2    |   4    |   6    |   8    |  10    |
   I   |        |        | R-13   | R-02   | R-06   |
   T   |        |        | R-16   | R-04   | R-12   |
   Y   |        |        |        | R-07   |        |
       |        |        |        | R-10   |        |
       +--------+--------+--------+--------+--------+
   1   |   1    |   2    |   3    |   4    |   5    |
       |        |        |        |        | R-08   |
       |        |        |        |        | R-14   |
       +--------+--------+--------+--------+--------+

ZONE DEFINITIONS

   RED    (score 20-25)  Unacceptable. Escalate to the sponsor. Response
                         required before baseline. Cannot be accepted.
   AMBER  (score 10-16)  Significant. Active response with a named owner
                         and a defined trigger. Reviewed fortnightly.
   GREEN  (score 1-9)    Monitor. Response may be acceptance. Reviewed at
                         each gate.

CURRENT DISTRIBUTION

   RED    none
   AMBER  R-01 (15), R-03 (12), R-05 (12), R-11 (12), R-06 (10), R-12 (10)
   GREEN  R-02 (8), R-04 (8), R-07 (8), R-09 (9), R-08 (5), R-10 (8),
          R-13 (6), R-14 (5), R-15 (6), R-16 (6)

TIE TO THE LAB 03 ESCALATION THRESHOLD

  Lab 03 set the escalation threshold at a risk score of 20 or above -
  the red zone. No Contoso risk currently reaches 20, which means no risk
  requires sponsor escalation at baseline. That is a finding worth stating
  explicitly to the sponsor, because "nothing to escalate" carries weight
  only when the threshold was defined in advance and the assessment was
  actually performed.

  R-01 at 15 is the closest to the threshold and the one to watch. If the
  sprint 1 spike reports instability, its probability moves from 3 to 4
  and the score becomes 20 - crossing into red and triggering escalation
  automatically. That is exactly how a threshold is supposed to work: the
  escalation decision is made now, in advance, and the trigger fires it.

A NOTE ON MATRIX LIMITATIONS
  The matrix is QUALITATIVE. It ranks; it does not price. R-06 and R-12
  both score 10, but R-06 carries a 15-day schedule impact against an
  immovable launch date while R-12 carries none. Equal scores are not
  equal risks. The matrix prioritises attention; EMV in Step 7 prices
  exposure; and neither replaces reading the risk statement.
```

### Step 6 - Apply all ten response strategies

```text
STRATEGIES FOR THREATS - five

  ESCALATE   The threat is OUTSIDE the project's authority or scope to
             address. Move it to the programme, portfolio or organisation.
             Once escalated, it leaves the project risk register - the PM
             no longer owns it. Escalation is not "telling the sponsor";
             it is transferring ownership.
  AVOID      ELIMINATE the threat entirely, usually by removing the cause
             or changing the plan so the risk cannot occur. Probability
             becomes zero. The strongest response, and often the most
             expensive.
  TRANSFER   Shift the IMPACT and ownership of the response to a THIRD
             PARTY. Insurance, warranties, fixed-price contracts,
             performance bonds. The risk still occurs - someone else bears
             the consequence. Transfer always has a premium.
  MITIGATE   REDUCE the probability, the impact, or both, to an acceptable
             level. The most common response. Does not eliminate.
  ACCEPT     Take no action to change the risk.
               ACTIVE acceptance  - establish a contingency reserve or
                 contingency plan. You accept the risk but you fund it.
               PASSIVE acceptance - do nothing at all beyond documenting
                 and periodically reviewing.
             Acceptance is a legitimate, deliberate choice, not a failure
             to decide. Every risk not otherwise responded to is accepted
             whether you say so or not.

STRATEGIES FOR OPPORTUNITIES - five, and they mirror the threats

  ESCALATE   The opportunity is outside the project's authority to pursue.
  EXPLOIT    ENSURE the opportunity is realised. Probability to 100%.
             The mirror of AVOID.
  SHARE      Allocate ownership to a THIRD PARTY better able to capture it -
             joint ventures, partnerships, risk-sharing agreements.
             The mirror of TRANSFER.
  ENHANCE    INCREASE the probability or the positive impact.
             The mirror of MITIGATE.
  ACCEPT     Take it if it arrives; do nothing to pursue it.

  Note the symmetry: Escalate / Avoid-Exploit / Transfer-Share /
  Mitigate-Enhance / Accept. Learning the pairs makes both lists one list.
```

A real Contoso example of each of the ten:

| Strategy | Type | Contoso example |
| --- | --- | --- |
| **Escalate** | Threat | R-12 - the absence of a management reserve is a funding structure decision above the PM's authority. Ownership moves to the sponsor and Group Finance with a pre-agreed ceiling variation path |
| **Avoid** | Threat | R-08 - rather than migrating legacy consent and session handling and testing whether it is secure, the plan REPLACES it entirely. The vulnerability cannot be inherited if the code is not inherited. Probability of the inherited-vulnerability path becomes zero |
| **Transfer** | Threat | R-15 - a contractual lead time with service credits moves the financial impact of late environment provisioning to the hosting vendor. The environments can still be late; Contoso is compensated |
| **Mitigate** | Threat | R-01 - a sprint 1 spike against the v2 sandbox reduces probability from 0.35 to 0.15 by discovering API problems while a v1 fallback still exists and while there is time to respond |
| **Accept (active)** | Threat | R-14 - Contoso cannot influence data protection policy, so the risk is accepted, but SGD 1,300 of contingency is held against it and the fee display is architecturally isolated to limit rework |
| **Accept (passive)** | Threat | Minor browser-version compatibility variance outside the supported matrix. Documented, reviewed at gates, no action and no reserve |
| **Escalate** | Opportunity | A group-wide licensing agreement with the payment gateway would reduce transaction fees across all Contoso systems. That benefit exceeds this project's scope; it is escalated to the COO for portfolio consideration |
| **Exploit** | Opportunity | O-02 - book the penetration test vendor's early window immediately rather than waiting for the planned slot. This converts the opportunity from possible to certain: probability to 1.0 for the booking itself |
| **Share** | Opportunity | Partner with the payment gateway vendor on a joint case study; the vendor supplies integration engineering support at no cost in exchange for the reference. Both parties capture value neither could alone |
| **Enhance** | Opportunity | O-01 - allocate two days in sprint 1 to assess and adapt the reusable notification component, raising the probability of realising it from 0.30 to 0.40 |

### Step 7 - Compute expected monetary value

```text
EMV  =  PROBABILITY  x  IMPACT

  THREATS are NEGATIVE. OPPORTUNITIES are POSITIVE.
  EMV is used for the contingency reserve calculation and inside decision
  trees. It is a QUANTITATIVE technique - it requires numeric probability
  and numeric impact, which is why it follows qualitative analysis rather
  than replacing it.

  THE CRITICAL LIMITATION, and the exam does test it:
  EMV is an AVERAGE ACROSS MANY REPETITIONS. A risk with a 0.10
  probability and a SGD 35,000 impact has an EMV of SGD 3,500 - but the
  actual outcome is never SGD 3,500. It is either zero or SGD 35,000.
  EMV is the right tool for sizing a reserve across a PORTFOLIO of risks,
  where the averaging is real. It is a poor tool for a single catastrophic
  risk that the organisation cannot survive, because surviving on average
  is not a meaningful concept for a one-off event.
```

Sign convention: threat impacts are shown as positive cost figures and summed as exposure; opportunity impacts are shown as negative because they reduce exposure.

| ID | Probability | Cost impact (SGD) | Gross EMV (SGD) | Post-response P | Residual EMV (SGD) |
| --- | --- | --- | --- | --- | --- |
| R-01 | 0.35 | 42,000 | 14,700 | 0.15 | 6,300 |
| R-02 | 0.25 | 18,000 | 4,500 | 0.15 | 2,700 |
| R-03 | 0.30 | 15,000 | 4,500 | 0.20 | 3,000 |
| R-04 | 0.20 | 22,000 | 4,400 | 0.10 | 2,200 |
| R-05 | 0.40 | 9,000 | 3,600 | 0.25 | 2,250 |
| R-06 | 0.15 | 30,000 | 4,500 | 0.10 | 3,000 |
| R-07 | 0.25 | 12,000 | 3,000 | 0.15 | 1,800 |
| R-08 | 0.10 | 35,000 | 3,500 | 0.05 | 1,750 |
| R-09 | 0.30 | 8,000 | 2,400 | 0.20 | 1,600 |
| R-10 | 0.20 | 14,000 | 2,800 | 0.10 | 1,400 |
| R-11 | 0.45 | 6,000 | 2,700 | 0.25 | 1,500 |
| R-12 | 0.15 | 20,000 | 3,000 | 0.10 | 2,000 |
| R-13 | 0.25 | 7,000 | 1,750 | 0.15 | 1,050 |
| R-14 | 0.10 | 26,000 | 2,600 | 0.05 | 1,300 |
| R-15 | 0.35 | 5,000 | 1,750 | 0.20 | 1,000 |
| R-16 | 0.20 | 9,000 | 1,800 | 0.15 | 1,350 |
| **Threat total** | | | **55,900** | | **34,200** |
| O-01 | 0.30 | -12,000 | -3,600 | 0.40 | -4,800 |
| O-02 | 0.25 | -8,000 | -2,000 | 0.35 | -2,800 |
| **Opportunity total** | | | **-5,600** | | **-7,600** |
| **NET EMV** | | | **50,300** | | **26,600** |

```text
RECONCILIATION TO THE LAB 13 CONTINGENCY RESERVE

  Residual net EMV                      SGD 26,600
  Charter contingency reserve           SGD 26,000
  VARIANCE                              SGD    600   (2.3% short)

  The reserve is SUBSTANTIATED. The charter figure of SGD 26,000 was set
  before the risk register existed; the register now independently derives
  SGD 26,600, which is within 2.3%. Record the SGD 600 variance rather
  than adjusting either number to make them match - manufactured
  agreement between two supposedly independent estimates destroys the
  value of having made them independently.

  WHY RESIDUAL AND NOT GROSS:
    Gross net EMV is SGD 50,300. Reserving that amount would double-count,
    because the project is already SPENDING effort on the responses that
    reduce exposure to SGD 26,600 - the sprint 1 spike, the sprint 2 data
    profiling, the written resource commitments. Those response costs sit
    in the work package estimates in Lab 13. Reserving the gross figure
    funds the same risks twice.

  NOTE THE OPPORTUNITY DIRECTION:
    Opportunity probabilities RISE after response (O-01 from 0.30 to 0.40,
    O-02 from 0.25 to 0.35) because ENHANCE and EXPLOIT make good outcomes
    more likely. Threat probabilities FALL. If your post-response
    opportunity EMV moved toward zero, you applied a threat response to an
    opportunity - a common and revealing error.
```

### Step 8 - Build and solve a decision tree

Create `artifacts/14-emv-analysis.md`. A decision tree evaluates a choice under uncertainty by computing the EMV of each branch and selecting the best.

**The decision:** Contoso must integrate payments. Gateway v1 is being deprecated (Lab 02 factor T1), but v2 is newly released and its stability is unproven (assumption A-03, risk R-01). Should the project build against v2 now, or stay on v1 and migrate in phase 2?

```text
NOTATION
  [ ]  DECISION node  - the project chooses. Cost of the choice shown here.
  ( )  CHANCE node    - uncertainty resolves. Branch probabilities must
                        sum to 1.0 at every chance node.
  EMV of a chance node = sum of (probability x outcome value) over branches
  DECISION RULE: at a decision node, choose the branch with the BEST EMV.
                 Here all values are COSTS, so best means LOWEST.

DECISION TREE - payment gateway integration approach

                                    +-- v2 API stable and documented ------ SGD 0 additional
                                    |   p = 0.65
                                    |
              +-- BUILD AGAINST ----(  )
              |   V2 NOW            |
              |   cost SGD 46,000   +-- v2 API unstable, rework required -- SGD 38,000
              |                         p = 0.35
              |
   [DECISION]-+
              |                     +-- v1 deprecated before launch, ------ SGD 95,000
              |                     |   forced emergency migration
              |                     |   p = 0.30
              +-- STAY ON V1, ------(  )
                  MIGRATE PHASE 2   |
                  cost SGD 22,000   +-- v1 survives to phase 2, ----------- SGD 58,000
                                        planned migration
                                        p = 0.70

COMPUTE THE CHANCE NODES FIRST, then add the decision node cost.

  PATH 1 - BUILD AGAINST V2 NOW
    Chance node EMV  =  (0.65 x 0)  +  (0.35 x 38,000)
                     =  0  +  13,300
                     =  SGD 13,300
    Decision node cost (build the v2 integration)  =  SGD 46,000
    TOTAL EMV OF PATH 1  =  46,000 + 13,300  =  SGD 59,300

  PATH 2 - STAY ON V1, MIGRATE IN PHASE 2
    Chance node EMV  =  (0.30 x 95,000)  +  (0.70 x 58,000)
                     =  28,500  +  40,600
                     =  SGD 69,100
    Decision node cost (build the v1 integration)  =  SGD 22,000
    TOTAL EMV OF PATH 2  =  22,000 + 69,100  =  SGD 91,100

  CHECK THE PROBABILITIES:  0.65 + 0.35 = 1.00 at node 1.
                            0.30 + 0.70 = 1.00 at node 2.  Both valid.

  DECISION
    Path 1  SGD 59,300
    Path 2  SGD 91,100
    DIFFERENCE  SGD 31,800 in favour of building against v2 now.

  RECOMMENDATION: BUILD THE PAYMENT INTEGRATION AGAINST GATEWAY V2 NOW.
```

```text
WHY THE RECOMMENDATION SURVIVES CHALLENGE - and this is the part that
matters more than the arithmetic

  1. THE CHEAPER IMMEDIATE OPTION IS THE MORE EXPENSIVE DECISION.
     Building against v1 costs SGD 22,000 against SGD 46,000 - less than
     half. A decision made on immediate cost alone chooses v1 and is
     wrong by SGD 31,800. This is the entire reason decision trees exist:
     they force the downstream consequences into the comparison.

  2. THE V1 PATH HAS NO GOOD OUTCOME. Note that BOTH v1 branches cost
     more than the ENTIRE v2 path. Even the favourable v1 outcome -
     v1 survives, planned migration at SGD 58,000 - plus its SGD 22,000
     build gives SGD 80,000, which exceeds the v2 path's full EMV of
     SGD 59,300. The v1 option loses even when it wins, because the
     migration is deferred, never avoided. Gateway v1 is being deprecated;
     that is a fact from the Lab 02 scan, not an uncertainty.

  3. SENSITIVITY - how wrong can the probabilities be?
     Find the probability of v2 instability, x, at which the paths are
     equal:
         46,000 + 38,000x  =  91,100
                  38,000x  =  45,100
                        x  =  1.187
     There is no valid probability at which v1 becomes preferable - the
     break-even exceeds 1.0. Even if v2 instability were CERTAIN
     (x = 1.0), path 1 costs 46,000 + 38,000 = SGD 84,000, still below
     path 2's SGD 91,100. The recommendation is robust across the entire
     probability range, which is a much stronger finding than a favourable
     point estimate.

  4. IT ALIGNS WITH THE RISK RESPONSE ALREADY PLANNED. R-01's mitigation
     is a sprint 1 spike against the v2 sandbox. The spike costs little
     and reduces the 0.35 instability probability to 0.15, which would
     lower path 1's EMV to 46,000 + (0.15 x 38,000) = SGD 51,700 -
     improving an already-winning position by a further SGD 7,600.

  5. WHAT THE TREE DOES NOT CAPTURE, and you must say so. The tree prices
     cost only. It does not price the SCHEDULE impact of a forced
     emergency migration landing near the fixed 30 June launch, which
     would be severe and which the 0.30 branch treats as merely expensive.
     Nor does it price the reputational cost of payment failure during the
     enrolment window. Both considerations point the same way as the
     arithmetic, which is fortunate - when they point in opposite
     directions, the tree informs the decision rather than making it.

COST OF THE DECISION NODE ITSELF
  Note that the decision node costs (SGD 46,000 and SGD 22,000) are
  included in each path total, not netted off or ignored. Omitting the
  cost of the choice is a frequent error: it would have given path 1 an
  EMV of SGD 13,300 against path 2's SGD 69,100, exaggerating the
  advantage from SGD 31,800 to SGD 55,800 and making the analysis
  indefensible under scrutiny.
```

### Step 9 - Qualitative versus quantitative, and when a risk becomes an issue

| | Qualitative risk analysis | Quantitative risk analysis |
| --- | --- | --- |
| Purpose | PRIORITISE risks for further attention | NUMERICALLY analyse the effect on objectives |
| Input | Probability and impact as relative scores | Probability as a decimal, impact in SGD or days |
| Tools | P/I matrix, risk data quality assessment, categorisation, urgency assessment | EMV, decision trees, Monte Carlo simulation, sensitivity analysis (tornado diagram) |
| Output | A prioritised risk list; risks ranked into red/amber/green | Quantified overall project risk exposure; probability of meeting objectives; contingency reserve amount |
| Performed | On EVERY project. Fast, subjective, cheap | Not on every project. Slow, requires reliable numeric data |
| At Contoso | Step 5 P/I matrix, all 18 risks | Step 7 EMV, Step 8 decision tree |

```text
THE SEQUENCE, and the exam checks the order:
  Identify -> Qualitative -> (Quantitative, if warranted) -> Plan responses
Qualitative ALWAYS precedes quantitative. You quantify the risks that
qualitative analysis showed were worth the effort of quantifying.

WHEN A RISK BECOMES AN ISSUE - the transition and what changes

  RISK   Uncertain. MAY occur. Lives in the RISK REGISTER. Managed by a
         RESPONSE STRATEGY and an owner. Has a probability below 1.0.
  ISSUE  Certain. HAS occurred. Lives in the ISSUE LOG. Managed by
         RESOLUTION, an owner and a due date. Probability is no longer a
         meaningful concept.

  THE TRANSITION at Contoso, worked:
    R-02, legacy data quality, is a risk in week 1 - probability 0.25.
    In sprint 2, profiling finds a 7% duplicate rate against the 4%
    trigger threshold. R-02 HAS NOW OCCURRED.

    What the PM does, in order:
      1. CLOSE R-02 in the risk register with the disposition "occurred".
         It is no longer a risk. Leaving it open with a probability
         attached is meaningless and clutters the register.
      2. OPEN an issue in the issue log with an owner, a resolution plan
         and a due date.
      3. RELEASE contingency reserve against it - this is a known,
         registered risk, so contingency is the correct funding route per
         Lab 13 Scenario 1. Report the release at the next board.
      4. ASSESS SECONDARY RISKS created by the resolution. Extended
         cleansing delays the migration script build, which pressures the
         migration rehearsal window.
      5. ESCALATE per the Lab 03 issue path if resolution exceeds the PM's
         authority or threatens the critical path.

    The register does not simply lose an entry. A risk that occurs
    produces an issue, a reserve drawdown, and usually a new risk. Risk
    management does not stop when the risk arrives - that is when it
    starts paying for itself.
```

### Step 10 - Answer the exam-style scenarios

```text
SCENARIO 1
A project manager identifies that a supplier may deliver late and takes out
an insurance policy covering the financial loss. Two months later the
supplier delivers late and the insurer disputes the claim, delaying payment
by three months. What are the risk management terms for the insurance
purchase and for the claim dispute?

  A. The insurance is mitigation; the dispute is residual risk.
  B. The insurance is transfer; the dispute is a secondary risk - a new
     risk created BY implementing the risk response.
  C. The insurance is avoidance; the dispute is an issue.
  D. The insurance is acceptance; the dispute is a trigger.

SCENARIO 2
Using the Contoso decision tree, a stakeholder argues that building against
v1 is obviously correct because it costs SGD 22,000 rather than SGD 46,000,
saving SGD 24,000 immediately against a fixed ceiling. What is the correct
response?

  A. Agree; against a hard ceiling with no management reserve, the cheaper
     immediate option is prudent.
  B. The immediate cost is only the decision node. Including the
     downstream chance outcomes, v1 has an EMV of SGD 91,100 against
     v2's SGD 59,300 - v1 is SGD 31,800 MORE expensive. Both v1 branches
     individually exceed the entire v2 path, and the break-even
     probability exceeds 1.0, so the conclusion holds even if v2
     instability were certain.
  C. Agree, but add SGD 31,800 to the contingency reserve.
  D. Escalate the decision to the sponsor without a recommendation.

SCENARIO 3
At the sprint 2 review, data profiling confirms the legacy duplicate rate
is 7% against the 4% trigger threshold defined for R-02. What is the
correct sequence of actions?

  A. Increase R-02's probability score in the risk register and continue
     monitoring.
  B. Close R-02 in the risk register as occurred, open a corresponding
     entry in the issue log with an owner and due date, release contingency
     reserve against it, assess the secondary risks the resolution creates,
     and escalate if resolution exceeds the PM's authority.
  C. Raise a change request to increase the cost baseline by the cleansing
     cost.
  D. Absorb the cleansing effort in the migration work package and report
     it as an overrun at the next gate.
```

Answer key:

```text
SCENARIO 1 -> B.  Insurance is the textbook TRANSFER: the impact and the
            response ownership move to a third party for a premium, while
            the risk event itself is unchanged - the supplier is just as
            likely to be late. The claim dispute is a SECONDARY RISK,
            defined precisely as a new risk created by implementing a risk
            response. It did not exist before the insurance was purchased.
            A misnames transfer as mitigation, and residual risk is what
            REMAINS after the response, not what the response creates -
            the residual risk here would be the uninsured portion of the
            loss. C is wrong twice: avoidance would mean changing the plan
            so the supplier could not make the project late at all. D
            confuses acceptance with transfer, and a trigger is a warning
            sign, not a consequence.

SCENARIO 2 -> B.  The stakeholder is comparing decision node costs and
            ignoring the chance nodes entirely, which is exactly the error
            decision trees exist to prevent. The full comparison is
            SGD 59,300 against SGD 91,100. The decisive supporting points
            are that both v1 branches individually exceed the whole v2
            path - even the favourable v1 outcome totals SGD 80,000 - and
            that the break-even probability of 1.187 lies outside the
            valid range, so no reasonable revision of the estimates
            reverses the conclusion. A is the trap and it is made
            plausible by the genuine ceiling pressure, which is why the
            sensitivity analysis matters: the answer is robust, not
            marginal. C misunderstands contingency, which funds identified
            risks rather than the gap between two options. D abdicates -
            the PM has the analysis and owes the sponsor a recommendation.

SCENARIO 3 -> B.  The trigger has fired and the risk HAS OCCURRED, so it
            is no longer a risk. A is the most common real-world error:
            adjusting a probability score for an event that has already
            happened is meaningless, since its probability is now 1.0, and
            it leaves the issue unmanaged in a register designed for
            uncertainty. C is wrong because releasing contingency does NOT
            change the cost baseline - contingency already sits inside it,
            which is the Lab 13 distinction. D hides a registered risk
            event inside a work package, corrupting that package's earned
            value data in Lab 20 and making the migration team appear to
            have overrun when in fact the risk management process worked
            exactly as designed. The full sequence in B matters: the step
            most often omitted is assessing the SECONDARY risks that the
            resolution itself creates.
```

## Deliverable

Submit to `artifacts/`:

- `14-rbs.md` - the risk breakdown structure to two levels across Technical, External, Organisational and Project Management, with the risk count by category and a comment on concentration.
- The traceability showing which Lab 02 factors and which Lab 06 assumptions generated which risks, with at least one conversion worked in full.
- `14-risk-register.md` - 16 to 18 risks including at least two opportunities, each with a cause-event-effect statement, probability as a decimal and a 1-5 score, impact in SGD and days, PxI score, response strategy, owner, trigger, secondary risk and residual probability.
- `14-pi-matrix.md` - the 5x5 grid with every risk plotted by ID, the red/amber/green zones defined, and the tie to the Lab 03 escalation threshold of 20 stated.
- A real Contoso example of each of the ten response strategies - five threat, five opportunity - including both active and passive acceptance.
- `14-emv-analysis.md` - EMV per risk gross and residual, the totals, and the reconciliation to the SGD 26,000 contingency reserve with the variance stated.
- The fully worked decision tree with branch probabilities summing to 1.0 at each chance node, decision node costs included, both path EMVs computed, the recommendation stated, and a sensitivity analysis.
- The qualitative versus quantitative comparison and the risk-to-issue transition sequence.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every risk statement contains a cause that is a present fact, an uncertain event, and an effect on a named project objective. If any statement is a single noun phrase, it cannot be responded to or priced.
- Your register contains at least two opportunities with positive EMV. A register of threats only is half a risk register.
- Every assumption in the Lab 06 log has a corresponding risk, and you can show the conversion for A-05.
- Every risk has a trigger that someone could actually observe. "Monitor closely" is not a trigger.
- Your P/I scores are consistent with your decimal probabilities - a risk at 0.45 should not score 2 on a 1-5 probability scale.
- Your residual net EMV is approximately SGD 26,600, reconciling to the SGD 26,000 contingency with the SGD 600 variance stated rather than hidden.
- Your opportunity probabilities INCREASED after response while your threat probabilities decreased. If both moved the same way, you applied threat logic to opportunities.
- Your decision tree branch probabilities sum to exactly 1.0 at each chance node, and the decision node costs are included in the path totals.
- Your decision tree recommends building against gateway v2 now, with an EMV of SGD 59,300 against SGD 91,100, and you can defend it with the sensitivity analysis rather than the point estimate alone.
- You can state what changes the moment a risk occurs, and name all five actions that follow.
