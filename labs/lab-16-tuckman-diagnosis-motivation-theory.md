# Lab 16 - Tuckman Diagnosis, Motivation Theory and Leadership Style

| Field | Value |
| --- | --- |
| Topic | 4 - Lead the Project Team |
| ECO 2026 task | People T3 - Lead the project team; People T1 - Develop a common vision |
| Learning outcome | LO3 - Lead and develop project teams to sustain performance |
| Duration | 75 minutes |
| Consumes | Lab 08 team charter, ground rules, definition of done and skills matrix; Lab 15 RACI |
| Produces | `artifacts/16-tuckman-diagnosis.md`, `artifacts/16-motivation-plan.md`, `artifacts/16-leadership-style-plan.md` |

## Objectives

- Diagnose a team's Tuckman stage from observed behaviour rather than from elapsed time.
- Select the leader action that actually moves a team out of the stage it is in.
- Apply six motivation theories to named individuals and produce a specific action from each.
- Distinguish Herzberg hygiene factors from motivators, and predict what a pay rise will and will not fix.
- Compute a Vroom expectancy score numerically and use it to locate which of three factors is broken.
- Map a situational leadership style to each team member's competence and commitment, and explain why one style for the whole team is a management error.
- Distinguish servant leadership from laissez-faire, which are behaviourally different and outcome-opposite.

## The five stages

```text
TUCKMAN - FORMING, STORMING, NORMING, PERFORMING, ADJOURNING

  Two rules the exam tests

  1. STAGES ARE DIAGNOSED FROM BEHAVIOUR, NOT FROM THE CALENDAR. A team
     six months in can be storming. A team that changes two members can
     go back to forming. Time on the project tells you nothing.

  2. YOU CANNOT SKIP STORMING. A team that appears to go straight from
     forming to norming has usually suppressed the conflict, not resolved
     it. It surfaces later, larger, and at a worse moment. Storming is
     evidence the team is engaging with real work, not evidence of
     failure.

  Regression is normal. New member, new product owner, a re-baseline, a
  redundancy rumour - any of these can push a performing team back to
  storming. The correct response is to lead for the stage the team is
  actually in now, not the stage it reached last month.
```

| Stage | Observable behaviour | What the team needs | Leader action | Leader failure mode |
| --- | --- | --- | --- | --- |
| Forming | Polite, tentative, deferential. Questions go to the PM rather than to each other. Nobody disagrees in public. Roles are unclear | Direction, structure, purpose | Direct. Set the vision, clarify roles, publish the ground rules, make expectations explicit, chair firmly | Assuming the silence is agreement |
| Storming | Open disagreement on approach. Challenges to roles and to the PM's authority. Sub-groups form. Frustration and blame language. Missed commitments | Coaching, facilitation, safe conflict | Coach. Surface the conflict, facilitate rather than decide, enforce ground rules, remove the structural cause of the friction | Suppressing the conflict to keep the peace, or taking sides |
| Norming | Ground rules are used by the team, not enforced by the PM. Members correct each other constructively. Processes stabilise. Commitments start being met | Support, reinforcement, autonomy | Support. Reinforce the norms, hand back decisions, praise the behaviour you want repeated | Withdrawing too early, before the norms are internalised |
| Performing | Self-organising. Solves problems without the PM. High trust. Members cover for each other. Velocity stable and predictable | Delegation, obstacle removal | Delegate. Get out of the way. Remove impediments, protect the team from outside disruption | Continuing to direct a team that no longer needs it |
| Adjourning | Anxiety about what comes next. Disengagement. Nostalgia. Loose ends left undone | Closure, recognition, transition | Recognise contributions, complete lessons learned, help each member to their next assignment | Ending the project with no closure ritual - handled in Lab 23 |

Watching one clear explanation of the model is worthwhile if you have not met it before; Tuckman's 1965 paper *Developmental Sequence in Small Groups* is the primary source and the stage names come directly from it.

## Steps

### Step 1 - Read the sprint 3 evidence

Create `artifacts/16-tuckman-diagnosis.md`. Read the narrative below and record only what you observe. Do not label the stage yet.

```text
CONTOSO TRAINING PORTAL UPGRADE - SPRINT 3 OBSERVATION LOG
Week 8 of 28. Sprint 3 of 12. Gate G1 (design baseline) passed in week 6.

MONDAY, SPRINT PLANNING
  Rajesh Menon (dev lead) proposes a service-layer abstraction over the
  payment gateway so the v2 integration can be swapped later. Aisha Rahman,
  who owns the gateway work, says the abstraction is speculative and will add
  a sprint to the integration. The exchange runs 35 minutes. Neither moves.
  Rajesh ends it with "we will do it my way, I am the dev lead". Aisha does
  not reply. Wei Ling Chua and Daniel Ofori say nothing throughout.
  The team commits to 34 points, its stated capacity.

WEDNESDAY, STANDUP (16:15 SGT / 08:15 GMT)
  Kenneth Lau (QA lead) says two stories were passed to him marked done with
  no unit tests and no staging deployment. He says, in the standup, "either
  the definition of done means something or we should stop pretending we have
  one". Standup runs 26 minutes. Ground rule GR-1 is not called by anyone.

THURSDAY
  Farah Ismail (BA) misses the PDPA data-inventory deadline for the second
  sprint running. She is the only person rated 5 on PDPA/accreditation-compliance domain in the
  Lab 08 skills matrix, holds 2 story points of capacity, and is currently
  covering requirements elicitation, the compliance evidence pack, and the
  admin-staff SME sessions. She has not raised a blocker. When asked at
  standup she says "it is fine, I will catch up".

FRIDAY
  Two separate direct-message conversations are running: Rajesh with Wei Ling
  about "how we get the architecture right without a fight", and Aisha with
  Kenneth about "whether the definition of done is even being applied". Ground
  rule GR-8 forbids exactly this. Neither conversation is in the team channel.

  Nurul Idris (UX) tells the PM privately that she no longer raises design
  concerns at planning "because it just turns into an argument".

END OF SPRINT
  Committed 34 points. Delivered 21. Velocity in sprint 1 was 26, sprint 2
  was 29. Two stories carried over. The retrospective produced three actions,
  all of which were process tweaks; nobody named the architecture
  disagreement or the definition-of-done dispute.
```

Record the evidence in a table before you diagnose. Diagnosing first and then finding evidence is how PMs confirm the stage they expected.

| # | Observed behaviour | Which Tuckman indicator it matches |
| --- | --- | --- |
| E-1 | Open, unresolved disagreement on technical approach at planning | Storming - disagreement on approach |
| E-2 | Authority asserted to end a debate ("I am the dev lead") | Storming - challenge to and assertion of role authority |
| E-3 | Two team members silent throughout a 35-minute dispute | Storming - members withdrawing rather than engaging |
| E-4 | Public frustration about the definition of done | Storming - process and standards contested |
| E-5 | Ground rule GR-1 broken with nobody calling it | Not yet norming - the team does not own its own rules |
| E-6 | Sub-groups forming in direct messages, breaking GR-8 | Storming - coalition formation, conflict moving underground |
| E-7 | A member no longer raising concerns in the open | Storming - reduced psychological safety |
| E-8 | Velocity dropped 29 -> 21 against a stable commitment | Storming - performance dips in this stage |
| E-9 | Retrospective avoided the two real conflicts | Storming, and being suppressed |
| E-10 | An overloaded member concealing a blocker | Structural cause, predicted by the Lab 08 skills matrix |

### Step 2 - Diagnose the stage and name the structural causes

```text
DIAGNOSIS: STORMING, with the conflict going underground.

  The tell is not the disagreement - disagreement at planning is healthy and
  is what norming teams do routinely. The tells are:

    -  the disagreement was ENDED by authority rather than resolved (E-2)
    -  it then MOVED to private channels (E-6)
    -  a member has stopped contributing in the open (E-7)
    -  the retrospective, the team's own designated repair mechanism,
       did not touch either real issue (E-9)

  A team that argues in the open and resolves it is norming. A team that
  argues in the open, is overruled, and then argues in direct messages is
  storming and heading for the Lab 17 conflict escalation.

  Velocity 26 -> 29 -> 21 is a symptom, not the problem. Chasing the velocity
  number is the error; the 8 lost points are the cost of the conflict.

STRUCTURAL CAUSES - these are the PM's to fix, not the team's

  C-1  The definition of done exists (Lab 08 Step 5) but is not enforced at
       the point of transfer, so QA discovers the breach after the fact.
       This is a process defect that presents as an interpersonal conflict.

  C-2  Architecture decisions have a rule in the Lab 08 decision table -
       consensus, then command by Rajesh if deadlocked after ONE timeboxed
       session. Rajesh went to command inside the same session, skipping the
       consensus attempt. The rule was right; it was not followed.

  C-3  Farah is a single point of failure on PDPA/accreditation compliance at 2 points of capacity
       across three workstreams. The Lab 08 matrix predicted this in week 1
       and the mitigating action (Grace Tay shadowing) was scheduled but not
       started. Her missed deadline is a capacity fact, not a performance one.

  C-4  Nobody is enforcing GR-1 or GR-8. Ground rules the team does not
       enforce for itself are the PM's ground rules, which means the team
       is not yet norming.
```

### Step 3 - Choose the leader actions for storming

The stage determines the action. A directing response to a storming team escalates it; a delegating response abandons it.

| Structural cause | Leader action (coaching, not deciding) | Owner | By |
| --- | --- | --- | --- |
| C-1 definition of done | Facilitate a 45-minute session with Kenneth and all four developers to walk the definition of done line by line and agree the transfer point. Do not adjudicate the two disputed stories yourself | PM | This week |
| C-2 architecture | Re-run the decision properly: one timeboxed 60-minute session, both options costed in story points, whole team present. If still deadlocked at the end, Rajesh decides on the record with the rationale logged - which is the agreed rule | PM facilitates, Rajesh decides | Sprint 4 planning |
| C-3 Farah overload | Start the Grace Tay shadowing now; agree capped SME hours with S-06 admin staff per Lab 06 assumption A-07; move the compliance evidence pack ownership to a second person | PM | Week 9 |
| C-4 ground rules | At the next retrospective, ask the team to re-own GR-1 and GR-8 explicitly, including who calls a violation. Level 1 of the Lab 08 graduated response is "any team member names it" - the team has to accept that authority | PM facilitates | Sprint 4 retro |
| E-7 Nurul withdrawn | Private conversation first, then a facilitated re-entry: invite her design concern first at the next planning, before anyone else speaks | PM | Sprint 4 planning |
| E-9 retro avoiding the real issues | Change the retro format for one sprint - use a timeline retro on sprint 3 so the two conflicts appear as events on a wall and are hard to walk past | PM | Sprint 4 retro |

```text
WHAT THE PM MUST NOT DO HERE

  -  Decide the architecture question personally. That removes Rajesh's
     accountability and teaches the team that escalation to the PM wins.
  -  Overrule the definition of done in either direction. The team agreed it
     by consensus in Lab 08; only the team changes it.
  -  Tell Farah to manage her time better. Her problem is capacity and
     single-point-of-failure exposure, both of which are PM-owned.
  -  Wait for the team to sort it out. Storming does not resolve itself;
     it either gets facilitated or it goes underground, which it already has.
  -  Add people to recover the 8 lost points. Brooks' law, and the Lab 06
     constraint CON-4 forbids it anyway.
```

### Step 4 - Apply the six motivation theories

Create `artifacts/16-motivation-plan.md`.

```text
MASLOW - HIERARCHY OF NEEDS
  Physiological -> Safety -> Belonging -> Esteem -> Self-actualisation
  Lower needs dominate until they are met. You cannot motivate someone with
  a stretch assignment while they think they are losing their job.

HERZBERG - TWO-FACTOR THEORY
  HYGIENE FACTORS   salary, job security, working conditions, company policy,
                    supervision quality, status, interpersonal relations
                    Absence causes DISSATISFACTION. Presence causes NEUTRALITY.
                    Hygiene factors cannot motivate. They can only stop
                    demotivating.
  MOTIVATORS        achievement, recognition, the work itself, responsibility,
                    advancement, growth
                    Presence causes SATISFACTION and effort. Absence causes
                    neutrality, not dissatisfaction.
  The two are SEPARATE SCALES, not two ends of one scale.

McGREGOR - THEORY X AND THEORY Y
  Theory X   people dislike work, avoid responsibility, need control and
             coercion. Produces monitoring, approval gates, micro-management.
  Theory Y   people find work natural, seek responsibility, self-direct
             towards goals they accept. Produces delegation and autonomy.
  It is a belief the MANAGER holds, and it is self-fulfilling in both
  directions. Agile and servant leadership assume Theory Y.

McCLELLAND - ACQUIRED NEEDS
  nAch  achievement  wants challenging but achievable goals, personal
                     responsibility, concrete feedback on results
  nAff  affiliation  wants harmony, belonging, good relationships; avoids
                     conflict; dislikes being singled out
  nPow  power        wants influence and impact. Personal power (self-serving)
                     vs institutional power (organisation-serving)
  Everyone has all three; one usually dominates.

PINK - DRIVE
  AUTONOMY   control over task, time, technique and team
  MASTERY    getting demonstrably better at something that matters
  PURPOSE    contributing to something beyond yourself
  Applies to complex, cognitive work - which is all of this project.
  Pink's own finding: for cognitive work, contingent financial rewards can
  REDUCE performance.

VROOM - EXPECTANCY THEORY
  MOTIVATION = EXPECTANCY x INSTRUMENTALITY x VALENCE

  Expectancy      "if I try, can I actually do it?"        (effort -> performance)
  Instrumentality "if I do it, will the reward follow?"    (performance -> reward)
  Valence         "do I want that reward?"                 (value of reward)

  It is MULTIPLICATIVE. Any one factor near zero makes motivation near zero,
  no matter how high the others are. This is the diagnostic value: it tells
  you WHICH of three different problems you have.
```

Worked Herzberg example, because it is the most-tested distinction on the exam:

```text
WHY A PAY RISE WILL NOT FIX KENNETH LAU

  The situation
    Kenneth Lau, QA lead, is frustrated. He is handed builds marked done
    that are not done. He was not in the room when the architecture was
    decided. His test strategy is treated as a stage at the end rather than
    a design input. He said in a standup that the definition of done is
    a pretence.

  The tempting intervention
    Kenneth is a strong performer and is at risk of leaving, so Contoso
    offers him a 10% salary increase and a "Senior QA Lead" title.

  What Herzberg predicts
    Salary and status are HYGIENE factors. Raising them removes a
    dissatisfier that was not present - Kenneth never complained about pay.
    The predicted effect on his motivation is approximately ZERO, and the
    effect is short-lived: within weeks the new salary is the new baseline.

  What is actually missing is MOTIVATORS
    -  achievement      his work is undone by others downstream
    -  recognition      his standards are treated as obstruction
    -  responsibility   he holds no authority over the transfer gate
    -  the work itself  he is testing, not designing quality in

  What Herzberg predicts WILL work
    -  Kenneth co-owns the definition of done and has the authority to
       refuse a transfer that breaches it (responsibility + achievement).
    -  Kenneth attends design sessions from sprint 4 as a required
       participant, not an optional one (the work itself).
    -  The Lab 08 skills matrix already has Kenneth at 3 on CI/CD and an
       action to run a release himself in sprint 4 (growth + mastery).
    -  The escaped-defect success criterion SC-8 (under 8, from 19) is
       publicly his metric, and it is reported at the sprint review
       (recognition + concrete feedback, which also serves McClelland nAch).

  THE EXAM POINT
    If a team member's dissatisfaction is about the work, giving them more
    money changes nothing. If it is about pay, working conditions or an
    abusive supervisor, no amount of interesting work fixes it - you must
    fix the hygiene factor first. Diagnose which scale you are on before
    you intervene.
```

Worked Vroom calculation, on the same team:

```text
VROOM DIAGNOSIS - AISHA RAHMAN, PAYMENT GATEWAY INTEGRATION

  Rate each factor 0 to 1.

  CASE A - as things stand in sprint 3

    Expectancy      0.4   She is the only person rated 4 on gateway work
                          (Lab 08 matrix), it is her first project at this
                          scale, the vendor API is unvalidated (assumption
                          A-03), and she now has to build it through an
                          abstraction she argued against. She is genuinely
                          unsure she can deliver it.
    Instrumentality 0.8   If she delivers it, the team will see it. Delivery
                          reliably leads to visible credit here.
    Valence         0.9   She wants this. Payment integration is the
                          specialism she is trying to build.

    Motivation = 0.4 x 0.8 x 0.9 = 0.29

  The score is low, and the DIAGNOSIS is unambiguous: the broken factor is
  EXPECTANCY. She wants the reward and believes it will follow; she does not
  believe she can do it. Praise, recognition and bonuses all act on
  instrumentality and valence, which are already fine. They would do nothing.

  THE INTERVENTION MUST RAISE EXPECTANCY
    -  Pair Wei Ling with her on the gateway spike (already an action in the
       Lab 08 skills matrix, not yet started).
    -  Run the sprint-1 vendor spike properly and close assumption A-03, so
       the unknown stops being an unknown.
    -  Re-run the architecture decision with her option genuinely costed, so
       she is not building through a design she believes will fail.
    -  Break the integration into three demonstrable slices so she gets
       evidence of her own capability early rather than at the end.

  CASE B - after the interventions

    Expectancy      0.8   Paired, spike closed, sliced, design agreed
    Instrumentality 0.8   Unchanged
    Valence         0.9   Unchanged

    Motivation = 0.8 x 0.8 x 0.9 = 0.58

  Motivation doubles from a single factor, because the model is
  multiplicative. Note also what this shows about the wrong intervention:
  raising instrumentality from 0.8 to 1.0 while leaving expectancy at 0.4
  gives 0.4 x 1.0 x 0.9 = 0.36 - barely a change. Fixing the wrong factor
  is close to free of effect.

  CASE C - a different member, same arithmetic, different broken factor

    Grace Tay, content lead. Expectancy 0.9 (she is certain she can write
    the comms), Instrumentality 0.2 (content work is never mentioned at
    sprint review; the demo is always screens), Valence 0.8.

    Motivation = 0.9 x 0.2 x 0.8 = 0.14

    Broken factor: INSTRUMENTALITY. She can do it and wants the recognition,
    but performance does not lead to it. The fix is not training and not a
    bonus - it is that the sprint review demo includes the actual learner
    email a learner will receive, presented by Grace. Cost: zero.
```

### Step 5 - Build per-member motivation profiles

| Member | Observed signals | Dominant theory that explains it | Specific action | Theory being applied |
| --- | --- | --- | --- | --- |
| Rajesh Menon, dev lead | Ends debates with positional authority; codes the hard parts himself rather than delegating (Lab 08 development need) | McClelland - nPow, currently expressed as personal power | Give him institutional power instead: name him the accountable decider for architecture in the RACI (Lab 15) with the requirement that he documents rationale and runs the consensus attempt first. Power channelled, not suppressed | McClelland; McGregor Y |
| Kenneth Lau, QA lead | Frustrated by others' standards, not by pay or conditions; publicly challenged the definition of done | Herzberg - motivator deficit, not hygiene | Co-ownership of the definition of done with authority to refuse a breaching transfer; required attendance at design sessions; SC-8 escaped-defect metric publicly his | Herzberg motivators; McClelland nAch |
| Aisha Rahman, developer | Wants the gateway specialism; doubts her own capacity to deliver it at this scale | Vroom - expectancy at 0.4 | Pair with Wei Ling; close assumption A-03 with a spike; slice the integration into three demonstrable pieces | Vroom; Pink mastery |
| Farah Ismail, BA | Hiding a blocker, saying "it is fine", missing deadlines she has never missed before | Maslow - safety, plus structural overload | Fix the capacity first (Grace shadows, SME hours capped, evidence pack reassigned). Then make it explicitly safe to raise a blocker by having the PM raise one first at standup | Maslow safety; Herzberg hygiene (workload) |
| Nurul Idris, UX designer | Has stopped raising design concerns in the open because "it turns into an argument" | Maslow - belonging and safety; McClelland nAff | Invite her concern first at planning before anyone else speaks; enforce GR-13 (attack the design, never the designer); give her the sprint 3/5/7 usability sessions as her own forum where her evidence, not her opinion, argues for her | Maslow; McClelland nAff |
| Daniel Ofori, developer | Silent in the architecture dispute; 8-hour time-zone offset; strong on data migration, weak on test automation | Pink - autonomy is high, mastery need unmet; also a structural inclusion problem | Give him the data migration workstream end to end with decision rights inside it (autonomy). Fund a test-automation growth goal with Kenneth as mentor (mastery). Rotate one ceremony per sprint to his timezone-favourable slot so silence is not the default | Pink; McGregor Y |
| Wei Ling Chua, senior developer | Runs the accessibility standard nobody asked her to own; mentoring instinct visible in the private message with Rajesh | Pink - purpose; McClelland nAff and nAch | Make her the named accessibility owner for WCAG 2.1 AA (charter IN-9) with the authority that goes with it; pair her with Aisha, which serves her mentoring drive and Aisha's expectancy simultaneously | Pink purpose; McClelland |
| Vikram Shah, DevOps | Sole holder of CI/CD knowledge; low visibility in reviews since his work is invisible when it works | Herzberg - recognition deficit; Vroom instrumentality | Report deployment frequency and lead time at the sprint review as a first-class metric; have Kenneth run a release under his coaching, which converts his knowledge into visible teaching | Herzberg recognition; Pink mastery |
| Grace Tay, content lead | Content never features in the demo; certain of her own competence | Vroom - instrumentality at 0.2 | Sprint review demo includes the real learner email, presented by Grace | Vroom |

Every action in that table is free or nearly free. That is the point of doing the diagnosis: motivation interventions that cost money are usually aimed at the wrong factor.

Apply Maslow across the whole team once, because one need currently dominates for a whole stakeholder group:

```text
MASLOW - THE S-06 PROBLEM

  The three admin staff serve this project as SMEs (Lab 06 assumption A-07)
  and believe they may be made redundant (Lab 07 misalignment M-2).

  They are operating at the SAFETY level. No amount of "you are shaping the
  tool that will transform your work" - an appeal to esteem and
  self-actualisation - will land while they believe the tool ends their job.
  It will read as insulting.

  The Lab 07 action was a written, communicated redeployment plan by week 8.
  It is week 8. If it has not been issued, every motivational approach to
  this group fails until it is. Maslow's ordering is the whole point:
  you cannot skip a level.
```

### Step 6 - Map situational leadership style to each member

Create `artifacts/16-leadership-style-plan.md`. Style is set by the member's competence AND commitment ON A SPECIFIC TASK - not by their seniority and not by your preference.

```text
HERSEY-BLANCHARD - SITUATIONAL LEADERSHIP

  D1  low competence, high commitment    -> S1 DIRECTING
      the eager beginner. Tell them what, how, when. Close supervision.
  D2  some competence, low commitment    -> S2 COACHING
      the disillusioned learner. High direction AND high support. Explain
      why, invite input, still decide.
  D3  high competence, variable commitment -> S3 SUPPORTING
      the capable but hesitant performer. Low direction, high support.
      Listen, encourage, facilitate. They decide.
  D4  high competence, high commitment   -> S4 DELEGATING
      turn it over. Agree the outcome, get out of the way, stay available.

  The classic error: one style applied to the whole team. Directing a D4
  is micro-management and insults them. Delegating to a D1 is abandonment
  and they will fail. The same person can be D4 on one task and D1 on the
  next - Aisha is D4 on integration coding and D2 on gateway v2.
```

| Member | Task in question | Competence | Commitment | Level | Style | What that looks like this sprint |
| --- | --- | --- | --- | --- | --- | --- |
| Rajesh Menon | Architecture and technical leadership | High | High | D4 | Delegating | Agree the decision rule and the documentation requirement, then let him lead. PM does not enter the design |
| Rajesh Menon | Delegating rather than coding it himself | Low | Medium | D2 | Coaching | Explicit coaching agreement: one hard problem per sprint handed to another developer, reviewed in his 1:1 |
| Wei Ling Chua | Front-end and accessibility | High | High | D4 | Delegating | Named owner of WCAG 2.1 AA. No approval required |
| Aisha Rahman | Payment gateway v2 integration | Low-medium | Medium, falling | D2 | Coaching | Pairing with Wei Ling, sliced deliverables, weekly review of the slice, high support and high direction |
| Aisha Rahman | General integration coding | High | High | D4 | Delegating | No supervision needed |
| Daniel Ofori | Data migration | High | High | D4 | Delegating | Owns the workstream end to end |
| Daniel Ofori | Test automation | Low | Medium | D2 | Coaching | Mentored by Kenneth, one automated test per story in sprint 4-5, reviewed |
| Nurul Idris | UX research and usability testing | High | Medium, dropping | D3 | Supporting | She knows how; what she lost is confidence in the forum. Listen, back her publicly, hand her the sessions |
| Kenneth Lau | Test strategy and quality gate | High | Medium, frustrated | D3 | Supporting | Do not tell him how to test. Give him authority and support, remove the structural obstruction |
| Farah Ismail | Requirements and PDPA domain | High | Low, overloaded | D3 | Supporting | Support and load relief, not direction. She does not need telling how - she needs capacity |
| Vikram Shah | CI/CD and environments | High | High | D4 | Delegating | Agree the outcome, stay out. Add a knowledge-transfer objective |
| Grace Tay | Learner communications content | High | Medium | D3 | Supporting | Visibility and a voice at the review, not instruction |

Two conclusions to write into the artifact:

```text
1. There is no D1 on this team, because the Lab 06 constraint fixed a
   9-person team of experienced practitioners. Directing (S1) is therefore
   almost never the right style here - which makes Rajesh's "we will do it
   my way, I am the dev lead" a style mismatch as well as a rule breach.

2. Aisha appears twice at two different levels. If you assign one style per
   PERSON rather than per TASK, you will either micro-manage her integration
   coding or abandon her on the gateway. Both are avoidable by asking the
   competence-and-commitment question about the specific task.
```

### Step 7 - Servant leadership, and how it differs from laissez-faire

```text
SERVANT LEADERSHIP - what the leader actually does

   1  Removes impediments. The PM chases the vendor API documentation so
      Aisha does not have to.
   2  Provides what the team needs. Environments, access, capacity relief,
      protected focus time.
   3  Shields the team from disruption. The Lab 01 scenario - a stakeholder
      injecting work mid-sprint - is intercepted by the PM, not absorbed
      by the developer.
   4  Coaches and grows people. The Kenneth-runs-a-release action.
   5  Facilitates rather than decides. Re-running the architecture session
      instead of ruling on it.
   6  Holds the team to its own agreed standards. Ground rules are enforced,
      including by the PM.
   7  Is accountable for the outcome. Always.

LAISSEZ-FAIRE - what it looks like from outside, and why it is not the same

   The behaviours that look similar
      -  the leader does not decide the architecture
      -  the leader does not assign tasks
      -  the leader is not in the technical detail

   The behaviours that are absent, which is the whole difference
      -  no impediments are removed, because nobody is looking for them
      -  no standards are held; the definition of done erodes unopposed
      -  no facilitation; conflict is left to resolve itself, so it goes
         underground - exactly the sprint 3 state
      -  no shielding; scope injection reaches the team directly
      -  no accountability; when it fails, the team is blamed for not
         self-organising

   THE TEST
      Servant leadership is a leader doing MORE work, of a different kind.
      Laissez-faire is a leader doing LESS work of any kind. If you cannot
      name what the leader did this week, it was laissez-faire.

   Applied to sprint 3: leaving the Rajesh-Aisha dispute alone because
   "the team should self-organise" is laissez-faire. Re-running the
   decision session, enforcing the agreed rule, fixing Farah's capacity and
   getting Nurul's voice back into planning is servant leadership. The
   difference in the sprint 4 outcome is the entire lab.
```

Complete this for your own artifact:

| Servant leadership behaviour | What the PM will do at Contoso in sprint 4 |
| --- | --- |
| Remove impediments | Close assumption A-03 with the vendor; get the staging environment fixed so definition-of-done item 8 is achievable |
| Provide resources | Start the Grace-shadows-Farah action; agree capped SME hours with the admin staff |
| Shield the team | Take the Head of Sales AI-recommender pressure (S-05) at the PM level; it does not reach the sprint |
| Coach | Kenneth mentors Daniel on test automation; Rajesh delegates one hard problem |
| Facilitate | Re-run the architecture decision; change the retro format to a timeline retro |
| Hold standards | Enforce GR-1 and GR-8; expect the team to take that authority back |
| Be accountable | The 8 lost points are reported by the PM as a PM-owned structural failure, not as a team performance issue |

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
Eight weeks into a six-month project, two developers openly disagree about the
system architecture at sprint planning, sub-groups have formed, the team has
stopped calling out its own ground-rule breaches, and velocity has fallen from
29 to 21 points. What stage is the team in and what should the project manager
do?

  A. Norming - the team is working through its differences. Continue to
     delegate and let it resolve.
  B. Storming - facilitate the conflict, enforce the agreed decision rule, and
     remove the structural causes.
  C. Forming - the team does not yet know each other. Set clearer direction
     and assign work personally.
  D. Performing - the debate shows high engagement. Take no action.

SCENARIO 2
A QA lead is dissatisfied because stories reach him marked done without tests
and he is excluded from design decisions. Management proposes a 10% pay rise
and a new title to retain him. What does motivation theory predict?

  A. The pay rise will restore his motivation because compensation is the
     strongest motivator.
  B. Little or no change in motivation - salary and status are hygiene
     factors, and his dissatisfaction is a motivator deficit around
     achievement, responsibility and the work itself.
  C. Motivation will rise then fall, and the correct fix is a larger rise.
  D. His motivation is a Maslow safety issue that money will resolve.

SCENARIO 3
A developer strongly wants to build the payment gateway integration and knows
that delivering it would be recognised, but has never worked at this scale, the
vendor API is unvalidated, and she has been overruled on the design. Using
expectancy theory, which factor is low and what is the correct intervention?

  A. Valence is low - offer a bonus tied to delivery.
  B. Instrumentality is low - guarantee public recognition at sprint review.
  C. Expectancy is low - pair her with an experienced developer, close the
     technical unknown with a spike, and slice the work so she gets early
     evidence of her own capability.
  D. All three are low - reassign the work to someone else.
```

Answer key:

```text
SCENARIO 1 -> B.  Diagnose from behaviour, not the calendar. Open disagreement
            on approach, sub-group formation, contested standards and a
            velocity dip are the textbook storming indicators. A is the trap:
            a norming team enforces its OWN ground rules - this one has stopped
            doing so, which is precisely what rules it out of norming. C would
            escalate the conflict by removing autonomy from experienced people
            and is a style mismatch with a team that has no D1 members. D
            mistakes unresolved conflict for healthy debate; the tell is that
            the conflict moved into private channels and the retrospective
            avoided it. Note also that "eight weeks in" is deliberately
            irrelevant - time on the project never determines the stage.

SCENARIO 2 -> B.  Herzberg's two factors are separate scales. Salary, status
            and title are hygiene: their absence causes dissatisfaction, their
            presence causes at most neutrality, and neither can motivate. His
            complaint is entirely about achievement (his work undone
            downstream), responsibility (no authority over the transfer gate)
            and the work itself (testing rather than designing quality in) -
            all motivators. A states the exact misconception the theory exists
            to correct. C repeats the error with a bigger number. D misapplies
            Maslow: nothing in the case suggests his job or income is at risk.

SCENARIO 3 -> C.  Motivation = Expectancy x Instrumentality x Valence. She
            wants it (valence high) and believes delivery would be recognised
            (instrumentality high). What she doubts is whether she can do it -
            first project at this scale, unvalidated API, a design she argued
            against. That is expectancy, and the model being multiplicative
            means fixing the other two changes almost nothing: 0.4 x 1.0 x 0.9
            = 0.36 against 0.4 x 0.8 x 0.9 = 0.29. Raising expectancy to 0.8
            gives 0.58, roughly double. A and B act on the two factors that
            are already fine. D removes the growth opportunity from someone
            who wants it and deepens the single-point-of-failure risk the
            Lab 08 skills matrix already flagged.
```

## Deliverable

Submit to `artifacts/`:

- `16-tuckman-diagnosis.md` - the ten-row evidence table completed before the diagnosis; the stated stage with the specific evidence that rules out the adjacent stages; at least four named structural causes; the leader-action table with an owner and a date per cause; the list of actions the PM must not take.
- `16-motivation-plan.md` - all six theories summarised in your own words; the Herzberg worked example distinguishing hygiene from motivator with a predicted outcome for the pay rise; at least two Vroom calculations showing which factor is broken and the arithmetic before and after the intervention; motivation profiles for at least five named team members, each naming the theory and a specific action; the Maslow analysis of stakeholder group S-06.
- `16-leadership-style-plan.md` - a competence/commitment assessment and style for every team member, with at least one member appearing twice at two different levels for two different tasks; the two written conclusions; the servant-leadership versus laissez-faire distinction with the seven behaviours and the sprint 4 application table.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your Tuckman diagnosis cites specific observed behaviours and never uses elapsed time as evidence.
- You can state why the team is storming rather than norming in one sentence, and it refers to who enforces the ground rules.
- Your structural causes are things the PM owns. If your causes list says "Rajesh is difficult" or "Farah is disorganised", redo it - you have diagnosed people where the evidence points at process and capacity.
- None of your leader actions has the PM deciding the architecture or overruling the definition of done.
- Your Herzberg example predicts that the pay rise produces approximately no change, and names at least three motivators that would.
- Your Vroom calculations are multiplicative, and you have demonstrated numerically that fixing the wrong factor barely moves the score.
- At least one team member appears at two different situational-leadership levels for two different tasks, and you can explain why one style per person is wrong.
- Your servant-leadership section names what the leader DOES. If your description of servant leadership would also describe a leader who did nothing, rewrite it.
- Every motivation action names a theory and a specific person. "Improve team morale" is not an action.
