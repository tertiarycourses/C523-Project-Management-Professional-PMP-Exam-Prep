# Lab 17 - Conflict Resolution: Five Modes, Leas' Levels and Negotiation

| Field | Value |
| --- | --- |
| Topic | 4 - Lead the Project Team |
| ECO 2026 task | People T2 - Manage conflicts |
| Duration | 45 minutes |
| Consumes | Lab 08 ground rules and decision rules; Lab 16 Tuckman diagnosis and motivation profiles; Lab 07 stakeholder attitudes and salience classifications |
| Produces | `artifacts/17-conflict-log.md`, `artifacts/17-roleplay-notes.md`, `artifacts/17-resolution-plan.md` |

## Objectives

- Place each of the five conflict-handling modes on the assertiveness/cooperativeness axes and state the legitimate use of each.
- Explain why collaborate is the usual keyed answer and identify the specific cases where it is the wrong one.
- Diagnose conflict intensity on Leas' five levels from the language people use.
- Recognise the point at which collaboration stops working and external help is required.
- Run four Contoso role-plays in pairs with role cards, an observer checklist and a structured debrief.
- Maintain a conflict log that records level, mode, intervention and outcome.
- Apply BATNA, ZOPA and the positions-versus-interests distinction to a real Contoso negotiation.

## The five modes

```text
THOMAS-KILMANN - two axes, five modes

  ASSERTIVENESS   how hard you push for YOUR concern
  COOPERATIVENESS how hard you work for THEIR concern

     high assert |  FORCE / DIRECT          COLLABORATE / PROBLEM-SOLVE
                 |  (win-lose)              (win-win)
                 |
                 |          COMPROMISE / RECONCILE
                 |          (lose-lose, or partial win-win)
                 |
     low assert  |  WITHDRAW / AVOID        SMOOTH / ACCOMMODATE
                 |  (lose-lose)             (lose-win)
                 +---------------------------------------------------
                    low cooperative              high cooperative

  EVERY MODE HAS A LEGITIMATE USE. This is the single most-tested idea in
  this lab. The exam does not reward "always collaborate"; it rewards
  matching the mode to the situation. A PM who only collaborates cannot
  stop an unsafe act, and a PM who only forces has no team by sprint 6.
```

| Mode | Assertive | Cooperative | Outcome | When it IS appropriate | When it fails | Contoso example |
| --- | --- | --- | --- | --- | --- | --- |
| Withdraw / Avoid | Low | Low | Lose-lose, deferred | Emotions are too high to think; the issue is trivial; you have no chance of winning and no stake; more information is needed; someone else can resolve it better; a cooling-off period will change the quality of the conversation | The issue is important and will grow; it becomes the PM's default; withdrawal is read as agreement | Rajesh and Aisha at 35 minutes and rising in sprint planning. The PM invokes GR-14, calls a 10-minute cool-off, and reconvenes with both options costed. Withdrawing from the moment, not from the issue |
| Smooth / Accommodate | Low | High | Lose-win | The relationship matters more than this particular point; you are wrong; the issue matters far more to them than to you; you are building goodwill you will need later; harmony is needed temporarily to keep something moving | Used on substantive issues, it quietly concedes scope, budget or quality; repeated accommodation teaches the other side that pressure works | The senior trainer S-16 wants the confirmation email to keep its old salutation. It costs nothing, he is a Lab 07 discretionary stakeholder whose consultation is cheap and valuable, and Grace Tay accommodates. Goodwill banked for the harder change later |
| Compromise / Reconcile | Medium | Medium | Partial win-win / lose-lose | Both parties have equally legitimate positions and equal power; a temporary settlement is needed under time pressure; collaboration has been attempted and failed; the stakes do not justify the cost of full collaboration | Used first, it splits the difference before anyone has understood the interests, so both sides get half a solution that satisfies neither; it is the mode most often mistaken for collaboration | The DPO wants 3 weeks of review, the schedule allows 3 weeks but the scope has grown. Settlement: 4 weeks, with the first 2 weeks running against draft artifacts in parallel. Neither party got what they asked for, and the date holds |
| Force / Direct | High | Low | Win-lose | Safety; a legal or regulatory requirement; an emergency needing an immediate decision; when the decision is unambiguously one person's accountability; when a decision must be protected from a group that is deadlocked and out of time; against people who exploit non-competitive behaviour | Used routinely, it destroys psychological safety, ends open disagreement and drives conflict underground - which is the exact Lab 16 sprint 3 state | The DPO rules that unconsented marketing data cannot be migrated. Not a negotiation, not a vote. Regulatory accountability sits with one named officer and the answer is no |
| Collaborate / Problem-Solve | High | High | Win-win | Both sets of concerns are too important to trade away; you need genuine commitment, not compliance; there is time; the relationship is ongoing; you want to learn from another viewpoint; the conflict conceals a structural problem worth finding | It needs time and trust and it needs both parties to want a solution. Above Leas level 3 the parties no longer share a goal, so collaboration is not available - attempting it there wastes time and can be read as manipulation | The definition-of-done dispute between Kenneth and the developers. Neither "test everything" nor "close the story" is the answer. The 45-minute session finds the real problem - the transfer point was never defined - and fixes it for every future story |

```text
THE EXAM RULE, STATED PRECISELY

  Collaborate / problem-solve is the PMP-preferred mode and is the keyed
  answer more often than all the others combined - because it is the only
  mode that resolves the conflict rather than managing it, and because it
  is the mode PMs most often skip.

  BUT IT IS NOT ALWAYS RIGHT. Choose otherwise when:

    FORCE      safety, a legal or regulatory requirement, a genuine
               emergency, or a decision that is one named person's
               accountability. "Let us find a win-win on whether to
               breach PDPA" is not a defensible answer.
    WITHDRAW   emotions are too high for anyone to think; the issue is
               trivial; you need information you do not yet have.
    ACCOMMODATE the point is small, they care far more, and the
               relationship is worth more than the point.
    COMPROMISE equal power, equal legitimacy, no time, or collaboration
               already tried and failed.

  Watch the question stem. "What should you do FIRST" after a heated
  exchange is often withdraw-then-collaborate: cool off, gather facts,
  then problem-solve. "What is the BEST resolution" is usually
  collaborate. A safety or compliance stem is force.
```

## Leas' five levels of conflict

```text
SPEED LEAS - CONFLICT INTENSITY

  L1  PROBLEM TO SOLVE     Focus is the ISSUE. People share a goal and
                           disagree about how to reach it. Language is
                           factual and future-oriented.
  L2  DISAGREEMENT         Focus shifts to SELF-PROTECTION. People start
                           holding back, generalising, and managing how
                           they look. Facts get shaded.
  L3  CONTEST              Focus is WINNING. Positions harden, sides form,
                           people keep score, language distorts and
                           exaggerates. Personal attacks begin.
  L4  FIGHT / FLIGHT       Focus is the OTHER PARTY. The goal is no longer
                           to win the point but to remove, defeat or escape
                           the other person. Factions are formal. Language
                           is ideological.
  L5  INTRACTABLE          Focus is DESTRUCTION. The relationship itself is
                           the target. No settlement is acceptable to the
                           parties; only separation ends it.

  THE THRESHOLD THAT MATTERS

  Up to L3 the parties still share a goal, so COLLABORATION IS AVAILABLE.
  At L4 and above they do not, and collaboration is not available: you
  cannot problem-solve with someone whose objective is your removal.
  At L4+ the PM's realistic options are separation of the parties,
  formal decision by an authority, and EXTERNAL HELP - HR, a professional
  mediator, senior management. A PM attempting to mediate an L5 conflict
  between their own team members is out of their depth and usually
  becomes a party to it.

  CONFLICT ONLY ESCALATES ONE LEVEL AT A TIME, and it escalates when it
  is left alone. Every level is cheaper to resolve than the next one.
```

| Level | Language cues you can actually hear | What the PM does |
| --- | --- | --- |
| L1 Problem to solve | "How do we...", "What if we...", "I think the issue is...". Specific, factual, future-focused. Names the problem, not the person | Facilitate normally. Collaborate. Often the team resolves it without you. Do not over-intervene - L1 conflict is productive |
| L2 Disagreement | "Some people think...", "I would rather not say who...", "That is not entirely accurate". Vagueness, hedging, humour used to deflect, facts withheld to avoid exposure | Get it back to specifics and to the open. Restore safety so people stop self-protecting. Collaborate, but you must facilitate actively now |
| L3 Contest | "You always...", "They never...", "Us and them", "This is the third time". Absolutes, score-keeping, distortion, coalitions, win-lose framing, first personal attacks | Actively mediate. Separate people from the problem. Set ground rules for the conversation itself. Collaboration is still possible but no longer spontaneous. This is the last level at which the PM can usually resolve it alone |
| L4 Fight / flight | "I cannot work with him", "One of us has to go", "That whole team is the problem". Requests for transfer or resignation. Talk about people rather than issues. Formal factions | Do NOT attempt to mediate to a win-win. Separate the parties structurally, make an authority decision, and bring in HR or a professional mediator. Protect the rest of the team from the fallout |
| L5 Intractable | "He should not be employed here", "I will make sure this fails". The objective is harm. Attempts at outside damage, formal complaints as weapons | Beyond PM resolution. Escalate to HR and senior management. Expect separation. The PM's job becomes protecting the project and the uninvolved team members |

## Steps

### Step 1 - Build the conflict log

Create `artifacts/17-conflict-log.md`. Log conflict as you log risk: recording it is what stops it escalating unnoticed from L2 to L3.

| ID | Date | Parties | Issue | Leas level | Source of conflict | Mode used | Intervention | Outcome | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CF-01 | Wk 8, sprint 3 | Rajesh Menon / Aisha Rahman | Service-layer abstraction over the payment gateway; cost of one sprint | L2, rising to L3 after the authority ruling | Technical opinion + role authority | Force (by Rajesh), then Withdraw (PM cool-off), then Collaborate | Decision re-run per the Lab 08 rule: one timeboxed 60-min session, both options costed in points, whole team present, Rajesh decides on the record if deadlocked | Abstraction adopted in a reduced form; 3 points, not a sprint. Both signed the decision log | Closed |
| CF-02 | Wk 8, sprint 3 | Kenneth Lau / development team | Two stories transferred marked done with no unit tests and no staging deploy | L3 - public challenge, "stop pretending we have one" | Process ambiguity presenting as a personal standard | Collaborate | 45-min session, definition of done walked line by line, transfer point defined, Kenneth given authority to refuse a breaching transfer | Definition of done unchanged; the transfer gate added. Zero breaching transfers in sprint 4 | Closed |
| CF-03 | Wk 3, ongoing | S-05 Head of Sales / S-03 Marcus Tan (PO) | AI recommender in v1, excluded as OUT-1 | L3 - coalitions, score-keeping, went around the PM to the sponsor | Scope and priority; a Lab 07 "dangerous" stakeholder | Collaborate on process, Force on substance | Facilitated session per Lab 07 M-1: trade-off made concrete at 55 points / 1.6 sprints; sponsor decides; phase-2 slot with a dated review | Deferred to phase 2 with a written decision date. Attitude Resistant -> Neutral | Monitoring |
| CF-04 | Wk 8, escalating | S-06 admin staff (3) / IT-side Ops Manager | Redundancy fear; the week-8 redeployment communication in Lab 07 M-2 was never issued | L3 heading to L4 - two are job hunting, trust in management collapsing | Unmet safety need (Lab 16 Maslow) plus an unkept commitment | Collaborate, with escalation | Escalate that the week-8 action was missed; written redeployment plan issued and briefed in person within 5 working days; SME hours capped and paid | Open - see the resolution plan in Step 6 | **Open, high priority** |
| CF-05 | Wk 9 | Farah Ismail / PM | Missed PDPA inventory deadline twice; blocker concealed | L1 - a problem to solve, not a dispute | Capacity, not performance | Collaborate | Grace Tay shadowing started; compliance evidence pack reassigned; SME sessions capped | Deadline met in sprint 4 | Closed |
| CF-06 | Wk 10 | Vendor account manager / PM | Payment gateway v2 support and integration pricing | L1 | Contractual terms | Collaborate, then Compromise | Interest-based negotiation - see Step 7 | See Step 7 worked example | Open |

The pattern worth naming in your artifact: CF-01, CF-02 and CF-05 all look like interpersonal conflicts and are all caused by process or capacity defects that the PM owns. That is true of most team conflict. Treating them as personality problems produces a personality fight.

### Step 2 - Role-play 1: two developers on architecture (L1/L2)

Create `artifacts/17-roleplay-notes.md`. Work in pairs. Read only your own role card. Ten minutes of role-play, five minutes of debrief.

```text
SITUATION - both parties see this
  Sprint 3 planning. The payment gateway v2 integration is the biggest
  single item in the backlog. Team capacity is 34 points per sprint.
  The Lab 08 decision rule for architecture is: consensus attempt in ONE
  timeboxed session, then Rajesh decides on the record if deadlocked.
```

```text
ROLE CARD A - RAJESH MENON, DEVELOPMENT LEAD
  You want a service-layer abstraction between the application and the
  payment gateway. Your reason: the vendor forced a v1-to-v2 migration on
  us with 9 months' notice and you expect them to do it again. You have
  been burned by direct vendor coupling on two previous projects and had
  to rewrite it both times.
  You have not said any of that out loud. You have only argued that the
  abstraction is "better design".
  You are aware you are the dev lead and that you can simply decide.
  You would prefer not to have to.
  What you actually need: protection against a future forced migration.
```

```text
ROLE CARD B - AISHA RAHMAN, DEVELOPER, OWNS THE GATEWAY WORK
  You estimate the abstraction adds a full sprint to an integration that
  is already the riskiest item in the backlog. Assumption A-03 (the v2 API
  is stable and documented) is still unvalidated. You believe adding a
  speculative layer on top of an unvalidated API doubles the unknowns.
  This is your first project at this scale and you are already unsure you
  can deliver it (Lab 16 rates your expectancy at 0.4). You have not said
  that either.
  You are not against abstraction in principle. You are against building
  it before anyone knows what the API actually does.
  What you actually need: to reduce unknowns, not add them, and to be
  believed about the estimate.
```

```text
OBSERVER CHECKLIST - tick what you actually see
  [ ] Did either party state a REASON, or only a POSITION?
  [ ] Did anyone ask the other "why does that matter to you?"
  [ ] At what Leas level did the exchange run? Note the exact words that
      told you.
  [ ] Which of the five modes did each party use? Did either switch?
  [ ] Was the disagreement about the ISSUE (L1) or did it become about
      each other (L3)?
  [ ] Was authority invoked? At what point, and what happened next?
  [ ] Did any option emerge that neither party arrived with?
  [ ] Was the Lab 08 decision rule referred to by anyone?

DEBRIEF QUESTIONS
  1. Both hidden interests were compatible - Rajesh wants migration
     protection, Aisha wants fewer unknowns. Name the option that serves
     both. Did it emerge in the role-play?
  2. What single question, asked in the first two minutes, would have
     surfaced both interests?
  3. This is L1 or L2 while it is about the design. What specific event
     pushes it to L3?
  4. If the timebox expires with no agreement, what is the correct action
     and who takes it?
```

```text
FACILITATOR NOTE - the option that serves both interests
  Run the spike first and defer the abstraction decision. Sprint 4 spends
  3 points validating the v2 API against real transactions, which closes
  assumption A-03. If the API proves stable and well documented, the
  migration risk Rajesh fears is lower than he assumed and a thin
  adapter (3 points) suffices. If it proves unstable, Aisha's unknowns
  are now known and the abstraction is justified on evidence.

  Neither party arrived with this. It costs 3 points against the 13 they
  were arguing over. It is available only if both state WHY, which is the
  entire lesson: positions were incompatible, interests were not.
```

### Step 3 - Role-play 2: Head of Sales versus product owner on scope (L3)

```text
SITUATION - both parties see this
  Week 9. The AI course recommender was assessed in Lab 02 (scored 16
  against 25 for mobile), excluded in the Lab 06 charter as OUT-1 with a
  documented rationale, and estimated at approximately 55 story points -
  1.6 sprints of the team's 34-point capacity. The Head of Sales emailed
  the COO last week saying the project team is "refusing to consider the
  market reality". This meeting is the PM-facilitated follow-up.
```

```text
ROLE CARD A - HEAD OF SALES (S-05)
  A competitor launched a recommender feature six weeks ago. You lost two
  corporate accounts last quarter and you believe this is why. You have a
  revenue number to hit and you are being asked about it monthly.
  You went to the COO because you did not believe the project team would
  listen. You are aware that looked like going around the PM. You are not
  going to apologise for it.
  Your language is absolute: "always", "never", "the team has decided
  without the business". You keep score of past decisions that went
  against you.
  What you actually need: evidence to your board that the competitive gap
  is being addressed on a timetable, and to not be the person who has to
  say "we are not doing it".
```

```text
ROLE CARD B - MARCUS TAN, HEAD OF L&D OPS, PRODUCT OWNER (S-03)
  You own backlog priority. Registration abandonment is 34% and every
  point of it is money leaving. A recommender that suggests courses on a
  form nobody completes is worthless.
  You believe the AI request is a feature-envy reaction to a competitor
  press release and you have said so, which is why relations are cold.
  You are also aware that if the recommender goes in, mobile
  responsiveness comes out - and mobile is 62% of traffic.
  What you actually need: the scope baseline defended without becoming
  the department that blocks the commercial side permanently.
```

```text
OBSERVER CHECKLIST
  [ ] Count absolutes ("always", "never", "the team has decided") and
      score-keeping references. These are the L3 markers.
  [ ] Did either party talk about the OTHER PARTY rather than the issue?
      That would be the L4 boundary.
  [ ] Which mode did the PM use? Did the PM collaborate on PROCESS while
      holding firm on SUBSTANCE?
  [ ] Was the trade-off made CONCRETE with a number, or did it stay a
      debate about importance?
  [ ] Was the going-around-the-PM behaviour addressed, avoided, or used
      as ammunition?
  [ ] Did the session produce a DATED decision point, or a vague
      "we will look at it later"?

DEBRIEF QUESTIONS
  1. Lab 07 classified S-05 as a DANGEROUS stakeholder - power and urgency
     without legitimacy on this specific claim. What does that
     classification tell you to do differently?
  2. Why does "is AI important?" have no answerable form, and what
     question replaces it?
  3. The PM cannot concede the scope and cannot afford to lose the
     relationship. Which mode handles substance and which handles the
     relationship? Can you use two modes at once?
  4. What legitimate route exists for the Head of Sales, and whose job is
     it to make that route look worth using?
```

```text
FACILITATOR NOTE
  The move is to collaborate on process and hold firm on substance, and
  to convert the argument into a choice between two concrete things.

  "The recommender is about 55 points, which is 1.6 sprints. Delivering
  it in v1 means either mobile responsiveness comes out - and mobile is
  62% of learner traffic and 41% completion today - or the 30 June date
  moves, and the date is tied to the July intake. Which of those two would
  you like to put to Priya?"

  "Is AI important?" is unanswerable because everyone says yes. "Which of
  these two do we give up?" is answerable, and it moves the decision to
  where the accountability actually sits - the sponsor.

  On the going-around: name it once, briefly, without heat, and move on.
  "Going to Priya directly meant she got the request without the numbers.
  I would rather she got both, so let us send this together." Making it
  the subject of the meeting escalates to L4 and loses the substance.
```

### Step 4 - Role-play 3: QA lead versus dev lead on the definition of done (L2/L3)

```text
SITUATION - both parties see this
  Sprint 3. Two stories were transferred to QA marked done with no unit
  tests and no staging deployment. One of them shipped to staging and a
  defect in it was found by the product owner during the sprint review
  demo, in front of the sponsor. The definition of done was agreed by the
  whole team in Lab 08, by consensus, with the QA lead present.
```

```text
ROLE CARD A - KENNETH LAU, QA LEAD
  You said in a standup, in front of everyone, "either the definition of
  done means something or we should stop pretending we have one". You
  meant it and you are not withdrawing it.
  The defect found in the review was in an untested story. You feel that
  proved your point and you also feel you were the one who looked bad,
  because "QA missed it" is what people say.
  You are not asking for perfection. You are asking for the ten items
  everyone signed up to.
  You were also not in the room when the architecture was decided, and
  quality is being treated as a stage at the end rather than a design
  input. That is the deeper grievance.
  What you actually need: authority over the transfer gate, and to be in
  the room at design time.
```

```text
ROLE CARD B - RAJESH MENON, DEVELOPMENT LEAD
  Your team committed 34 points and delivered 21. You were under pressure
  to show progress at the review. You made a judgement call that two
  stories were functionally complete and that tests could follow next
  sprint.
  You think the definition of done is right in principle and that a
  10-item checklist applied literally to every trivial story is
  bureaucracy. You have not said which of the ten you would drop.
  You resent "in front of the sponsor" being used against you, because
  you were the one trying to have something to show.
  What you actually need: a way to show progress that does not require
  breaking the standard, and relief from the velocity pressure.
```

```text
OBSERVER CHECKLIST
  [ ] Is either party arguing the PRINCIPLE or the two SPECIFIC stories?
      Which is more productive and why?
  [ ] Note the L3 markers: score-keeping ("in front of the sponsor"),
      reputation defence, "we should stop pretending".
  [ ] Did anyone treat this as a PROCESS defect rather than a person
      defect? At what point?
  [ ] Did the PM adjudicate on the merits, or apply and repair the
      agreement the team already made?
  [ ] Was the deeper grievance - Kenneth's exclusion from design -
      surfaced at all? It is the actual cause.
  [ ] Was the velocity pressure named as a contributing structural cause?

DEBRIEF QUESTIONS
  1. This conflict has a surface issue (two stories) and a structural
     cause (no defined transfer point, and quality treated as an end
     stage). Which one does collaboration have to reach?
  2. The team agreed the definition of done by consensus. What does the
     Lab 08 decision rule say about who may now change it?
  3. Rajesh's velocity pressure is real. Whose problem is it, and what
     does that tell you about a PM who lets a commitment number drive a
     quality standard?
  4. If the PM rules in favour of either party, what has the PM taught the
     team about every future done/not-done argument?
```

```text
FACILITATOR NOTE
  Collaborate, and reach the structural cause. The 45-minute session
  walks the ten items and produces three outputs, none of which is a
  ruling on the two stories:

    1. A defined TRANSFER POINT: a story is not moved to the QA column
       until items 1-7 are demonstrably true. Kenneth has the authority to
       move it back, and that is not an escalation, it is the process.
    2. Kenneth attends design sessions from sprint 4 as a required
       participant. This is the Lab 16 Herzberg motivator intervention -
       responsibility and the work itself - and it removes the grievance
       that is actually driving the heat.
    3. The velocity pressure is named as a PM-owned problem. The PM
       reports 21 against 34 as a structural failure of the PM's own,
       not as a team performance issue, which removes the incentive
       Rajesh was responding to.

  The PM who rules "Kenneth is right, quality first" wins the sprint and
  loses the process: every future dispute now comes to the PM.
```

### Step 5 - Role-play 4: admin staff versus Ops Manager on redundancy (escalating, high emotion)

```text
SITUATION - both parties see this
  Week 8. Lab 07 recorded misalignment M-2: the three admin staff fear
  redundancy; the Ops Manager intends redeployment but has not said so.
  The agreed action was a written, communicated redeployment plan by
  week 8. It is week 8 and nothing has been issued. Two of the three are
  actively job hunting. They are also the project's SMEs (Lab 06
  assumption A-07) and the launch-week support cover.
  Lab 07 classified them as DEPENDENT stakeholders: legitimate and urgent
  claim, no power to press it.
  This is a facilitated meeting the PM has called.
```

```text
ROLE CARD A - SITI, SENIOR ADMINISTRATOR, SPEAKING FOR THE THREE
  You have worked here eleven years. You have spent six hours a week for
  three sprints teaching this project's business analyst how your job
  works, and you now believe you have been training your own replacement.
  Nobody has told you anything. The silence is what you are reading, and
  you are reading it as bad news, because in your experience silence has
  always meant bad news.
  You are angry and you are also frightened, and the anger is the part
  that will come out. You may say something close to "so we build it and
  then you get rid of us".
  You have not been asked what you want. If asked, you would say: the
  learner-support and quality-assurance work you have never had time for,
  because 24 hours a week goes on retyping.
  What you actually need: certainty in writing, and to be asked.
```

```text
ROLE CARD B - OPS MANAGER
  You genuinely intend to redeploy all three. There is real work waiting:
  learner support quality, funding-claim verification, corporate client
  onboarding. You have not written it down because HR has not signed off
  the new role descriptions and you did not want to promise something you
  could not guarantee.
  You now realise your caution has been read as evasion for eight weeks.
  You are defensive about that, because your intent was to protect them.
  You are also aware that if they resign, you lose eleven years of
  institutional knowledge, the project loses its SMEs, and launch week
  loses its support cover.
  What you actually need: to say something true and useful today without
  making a commitment HR has not approved.
```

```text
OBSERVER CHECKLIST
  [ ] What Leas level does this open at? What words told you? Watch for
      L4 markers ("you", "management", "they were always going to").
  [ ] Did the PM let the emotion be expressed before moving to solutions?
      Solving too early is the most common failure here.
  [ ] Did anyone acknowledge the impact before defending the intent?
  [ ] Did the Ops Manager explain WHY nothing was written, and did that
      land as a reason or as an excuse?
  [ ] Was anything committed to with a DATE, or only with an intention?
  [ ] Was Siti asked what she actually wants? At what point?
  [ ] Did the PM advocate for the dependent stakeholders, or chair
      neutrally? Which was correct here?

DEBRIEF QUESTIONS
  1. Lab 16 places this group at Maslow's SAFETY level. What does that
     rule out saying? Try "you are shaping the tool that will transform
     your work" out loud in this room and describe how it lands.
  2. The Ops Manager's caution was well-intentioned and did harm. What
     does that tell you about silence as a communication strategy?
  3. This is a DEPENDENT stakeholder group. Lab 07 said the PM's role is
     advocacy. Is advocacy compatible with facilitating neutrally? What
     do you actually do?
  4. Two of three are job hunting. If one resigns next week, what does
     the project lose, and which Lab 06 assumption fails?
  5. What can be committed to TODAY that is both true and useful, given
     HR has not signed off?
```

```text
FACILITATOR NOTE
  Sequence matters more than content here.

    1. Let it be said. Do not move to solutions in the first five
       minutes. An interrupted grievance escalates.
    2. Acknowledge impact before defending intent. "Eight weeks of
       silence while you taught us your job - I understand exactly how
       that reads." Not "that was never our intention", which is a
       defence and lands as a dismissal.
    3. Explain the reason for the silence honestly, and name it as a
       mistake. The reason is true and it is not an excuse.
    4. Commit to what CAN be committed today, with dates:
         - written statement of intent to redeploy all three, from the
           Ops Manager, within 5 working days
         - HR sign-off on role descriptions with a named date
         - SME hours capped and formally recognised as project work,
           not unpaid extra
         - all three consulted on which of the new roles they want
    5. Ask what they want. Siti's answer - learner support and quality
       work - is better for Contoso than anything the Ops Manager had
       drafted. Nobody had asked in eight weeks.

  MODE: collaborate, with the PM ADVOCATING rather than chairing
  neutrally. Lab 07 said the defining feature of a dependent stakeholder
  is that they cannot press their own claim. Neutral chairing leaves a
  powerless party to negotiate with a powerful one, which is not
  neutrality in effect. The PM's advocacy here is what the Lab 04
  sustainability commitment actually costs.

  This conflict is L3 heading to L4. Left another four weeks it reaches
  L4 - resignations, formal complaints, the project's SMEs gone in the
  sprint before launch - and at L4 no facilitated session fixes it.
  The cost of eight weeks of silence is the whole lesson.
```

### Step 6 - Build the resolution plan

Create `artifacts/17-resolution-plan.md`. Every open conflict in the log gets a level, a target level, a mode, an action, an owner, a date and an escalation trigger.

| Conflict | Current level | Target | Mode chosen | Why that mode | Action | Owner | By | Escalate if |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CF-04 admin staff / Ops Manager | L3 -> L4 | L1 | Collaborate, PM advocating | Dependent stakeholders with a legitimate, urgent claim; the relationship and the substance both matter; there is still just enough time | Facilitated session run per Step 5; written redeployment intent in 5 working days; HR date named; SME hours capped and recognised; all three consulted on role choice | PM + Ops Manager | Week 9 | No written statement within 5 working days, or any resignation - then escalate to the COO as a project resource risk |
| CF-03 Head of Sales / PO | L3 | L2 | Collaborate on process, Force on substance | The exclusion is a sponsor-level decision already taken on evidence; the relationship is ongoing and must survive | Monthly roadmap meeting with a standing phase-2 status item; dated phase-2 decision point in the roadmap; sponsor pre-briefed before any approach | PM | Monthly | A second direct approach to the sponsor bypassing the process - then the sponsor restates the route, not the PM |
| CF-06 gateway vendor | L1 | L1 | Collaborate, then Compromise | Commercial negotiation with an ongoing relationship and equal legitimacy; a settlement is acceptable | Interest-based negotiation per Step 7; BATNA prepared before the meeting | PM | Week 11 | No agreement inside the ZOPA by week 12 - then execute the BATNA |
| CF-01 residual | L1 | L1 | Collaborate | Resolved; monitoring only | Spike result reviewed at sprint 4 planning; decision logged with rationale | Rajesh | Sprint 4 | Any repeat of a decision taken by authority inside the same session |
| CF-02 residual | L1 | L1 | Collaborate | Resolved; the transfer gate now carries it | Kenneth attends design sessions from sprint 4; escaped defects tracked against SC-8 | PM | Sprint 4 | Any breaching transfer - handled by the process, not by the PM |

### Step 7 - Negotiation: positions, interests, BATNA and ZOPA

```text
POSITIONS vs INTERESTS
  A POSITION is what someone says they want.
  An INTEREST is why they want it.
  Positions are usually incompatible. Interests are usually not.
  Every role-play in this lab turns on that sentence. Rajesh's position
  was "build the abstraction"; his interest was "protect me from a forced
  migration". Those are different problems and only one of them has a
  3-point solution.

BATNA - Best Alternative To a Negotiated Agreement
  What you will do if this negotiation fails. Not your walk-away price -
  your actual fallback. Your BATNA is the only real source of negotiating
  power, and a weak BATNA that you have not examined is worse than a weak
  BATNA you have, because you will concede without knowing why.
  Improve your BATNA BEFORE you negotiate, not during.

RESERVATION POINT
  The worst deal you would still accept, derived from your BATNA.

ZOPA - Zone Of Possible Agreement
  The range between your reservation point and theirs. If they do not
  overlap, there is no ZOPA and no deal is possible on those terms -
  which is useful to know before you spend three meetings finding out.
```

Worked example on the real Contoso negotiation, CF-06:

```text
NEGOTIATION - PAYMENT GATEWAY v2 SUPPORT AND INTEGRATION

  THE SITUATION
    The incumbent vendor is forcing the v1-to-v2 migration. They have
    quoted SGD 34,000 for the v2 integration support package: dedicated
    technical contact, sandbox access, a guaranteed 4-hour response SLA
    during the integration window, and migration assistance.
    We budgeted SGD 18,000 within the Lab 06 infrastructure and migration
    line of SGD 26,000. The PM's procurement authority (Lab 06 Step 6)
    is SGD 15,000 per engagement, so anything above that goes to the CCB.

  POSITIONS
    Vendor:   SGD 34,000, take it or leave it, standard package.
    Contoso:  SGD 18,000, that is what we budgeted.

  INTERESTS - what each side actually needs

    CONTOSO
      -  De-risk the integration. It is the riskiest backlog item and
         assumption A-03 is unvalidated. What we truly need is the
         sandbox and the fast SLA during the 6-week integration window,
         not a 12-month support wrapper.
      -  Hold the SGD 480,000 ceiling. It is board-approved and hard.
      -  Not be exposed to another forced migration - Rajesh's CF-01
         interest, which is a NEGOTIATION issue, not an architecture one.

    VENDOR
      -  Retain the account. We are small revenue but we are a reference
         customer in the Singapore training sector, and their sales cycle
         there is slow.
      -  Hit an annual contract value target, which is why the package is
         bundled into 12 months rather than 6 weeks.
      -  Get customers off v1, which costs them to maintain. Our
         migration is worth something TO THEM.

  BATNA - OURS
    Integrate against public v2 API documentation with no support
    package, and buy 40 hours of an independent integration specialist
    at SGD 180/hr = SGD 7,200.
    Cost: SGD 7,200. Risk: no sandbox, no SLA, Aisha is the only person
    at competence 4 on the gateway and her Lab 16 expectancy is 0.4.
    Assessment: viable but genuinely risky. A real BATNA, not a bluff.

  BATNA - THEIRS
    We stay on v1 past their sunset date, or we move to a competitor
    gateway. Both cost them: v1 maintenance they want to end, or the
    loss of a sector reference account.
    Assessment: their BATNA is weaker than they are behaving as if it is.

  RESERVATION POINTS
    Ours:    SGD 22,000. Above that, the BATNA plus the residual risk is
             the better deal, and we breach the budget line.
    Theirs:  estimated SGD 16,000, being roughly their delivery cost on
             a 6-week engagement.

  ZOPA
    SGD 16,000 --------------------------- SGD 22,000
    A ZOPA of about SGD 6,000 exists. A deal is available. The published
    positions of 18,000 and 34,000 concealed that completely, which is
    the practical value of doing this analysis before the meeting rather
    than after the third one.

  THE INTEREST-BASED SETTLEMENT
    -  6-week integration support window instead of 12 months. Serves
       our actual need (the window) and costs them far less to deliver.
    -  Sandbox access and the 4-hour SLA retained in full. These are
       the items that de-risk the work; we do not trade them.
    -  Contoso agrees to a written reference and a sector case study.
       Costs us nothing and serves their strongest interest.
    -  A 24-month notice clause on any future forced API migration,
       written into the agreement. This is Rajesh's CF-01 interest,
       solved contractually for zero dollars rather than architecturally
       for 13 story points.
    -  Price: SGD 19,500.

  RESULT
    Inside the ZOPA. Inside the SGD 26,000 budget line. Above the PM's
    SGD 15,000 procurement authority, so it goes to the CCB per Lab 06 -
    do not miss that step, it is exactly the kind of detail an exam
    scenario turns on.
    And the migration-protection interest that started the sprint 3
    architecture fight is now handled by a contract clause, which is the
    cheapest place it could possibly have been handled.
```

Prepare the same analysis for one further negotiation of your own choosing from the case - suggested: the DPO's review duration, where the positions are 3 weeks against 6 weeks and the interests are evidence quality against a fixed launch date.

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
During a design review, two developers' disagreement becomes heated. One says
"you always overcomplicate everything" and the other stops responding. Other
team members look uncomfortable. What should the project manager do FIRST?

  A. Ask both to explain their technical positions in turn so the team can
     evaluate the merits.
  B. Call a short break, then reconvene with an agreed structure for the
     discussion focused on the design rather than on each other.
  C. Make the architecture decision yourself to stop the conflict.
  D. Ask the development lead to resolve it after the meeting.

SCENARIO 2
A team member tells you that a supplier's technician is working on live
electrical equipment without isolating it, contrary to the site safety
procedure. The technician says he has done it this way for fifteen years and
the schedule is tight. Which conflict-handling mode should the project manager
use?

  A. Collaborate - work with the technician to find an approach that meets
     both safety and schedule needs.
  B. Compromise - agree a partial isolation that saves some time.
  C. Force - stop the work immediately and require compliance with the
     procedure.
  D. Withdraw - it is the supplier's employee and therefore the supplier's
     responsibility.

SCENARIO 3
Two senior team members are in open conflict. Each has told you separately that
they cannot continue working with the other and one has asked to be transferred.
They have formed factions and other team members are being asked to take sides.
Attempts to facilitate a joint problem-solving session have failed twice. What
is the appropriate response?

  A. Continue facilitating collaborative sessions; collaboration is the
     preferred approach and needs persistence.
  B. Recognise this as Leas level 4, separate the parties structurally, make
     an authority decision on the disputed work, and involve HR or a
     professional mediator.
  C. Force a resolution by deciding the technical issue yourself.
  D. Withdraw and allow time to reduce the tension.
```

Answer key:

```text
SCENARIO 1 -> B.  Withdraw briefly, then collaborate. "You always" is an L3
            marker - an absolute, aimed at the person rather than the design -
            and one party has already disengaged. Emotion is now high enough
            that nobody is processing content, which is the textbook legitimate
            use of avoid: a cool-off changes the QUALITY of the conversation,
            not the outcome you are avoiding. Note the mode is a temporary
            withdrawal from the MOMENT, not from the issue - the reconvene is
            in the answer. A continues a debate that has stopped being about
            the design, which will escalate it. C removes the team's ownership
            and teaches them that heat brings a PM ruling. D hands a live
            interpersonal conflict to one of the parties' own line manager and
            leaves the team's discomfort unaddressed. Watch the stem word
            FIRST: over a longer horizon the answer is collaborate, but not
            in the next sixty seconds.

SCENARIO 2 -> C.  Force is correct and it is not a close call. Safety is one of
            the named legitimate uses of the forcing mode: there is no win-win
            available on whether to comply with a safety procedure, and the
            cost of being wrong is irreversible. A sounds like the PMP-preferred
            answer and is the trap - "collaborating on a safe-enough shortcut"
            is negotiating on a non-negotiable. B is worse: a partial isolation
            is a partial safety control, which is no safety control. D confuses
            contractual responsibility with the PM's authority to stop unsafe
            work on the project. The same logic applies to legal and regulatory
            requirements, which is why the Contoso DPO's ruling on unconsented
            data is also a force decision.

SCENARIO 3 -> B.  The markers are unambiguous L4: the focus has moved from the
            issue to the other person ("cannot work with him"), a transfer has
            been requested (flight), formal factions have formed, and the wider
            team is being recruited into them. Above L3 the parties no longer
            share a goal, so collaboration is not available - which is exactly
            why two facilitated sessions have already failed. A is the answer
            that mistakes a general preference for a universal rule and will
            burn another two weeks while the team polarises further. C decides
            a technical question when the conflict is no longer technical. D
            leaves an L4 conflict alone, and conflict left alone escalates -
            L5 is where this goes. The exam point is the threshold: know where
            collaboration stops working and where external help starts.
```

## Deliverable

Submit to `artifacts/`:

- `17-conflict-log.md` - at least six logged conflicts with parties, issue, Leas level, source, mode used, intervention, outcome and status; and a written note identifying which of them are process or capacity defects presenting as interpersonal conflict.
- `17-roleplay-notes.md` - completed observer checklists for all four role-plays; for each, the Leas level you diagnosed with the exact words that told you, the modes each party used, and written answers to every debrief question. For role-play 1 you must name the option that serves both hidden interests and state whether it emerged.
- `17-resolution-plan.md` - every open conflict with a current level, target level, chosen mode with justification, action, owner, date and a named escalation trigger.
- The five-mode table completed in your own words with a Contoso example and a "when it fails" for every mode - including a legitimate use for withdraw, accommodate and force.
- The CF-06 negotiation analysis: positions, interests for both sides, both BATNAs, both reservation points, the ZOPA with its numeric range, and the settlement - plus one further negotiation analysed the same way.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every one of the five modes has a legitimate use written against it. If your notes say force and withdraw are always wrong, you will get the safety question wrong.
- You can name three situations in which collaborate is NOT the right answer, and say why in each case.
- Your Leas diagnoses cite the actual words spoken, not your impression of the tone.
- You can state what changes at level 4 and why collaboration is unavailable above level 3.
- Your CF-04 entry treats the admin staff as dependent stakeholders and has the PM advocating, not chairing neutrally - and you can defend why that is not a loss of impartiality.
- Your role-play 1 debrief names the spike-first option and identifies the single question that surfaces both interests.
- Your role-play 2 notes convert "is AI important" into a concrete either/or with a number attached.
- Your role-play 3 notes reach the structural cause (no transfer point, quality treated as an end stage) and not just the two disputed stories.
- Your role-play 4 notes put acknowledgement before defence and contain at least three commitments with dates.
- Your ZOPA is a numeric range derived from two reservation points, each derived from a BATNA. A ZOPA asserted without both BATNAs is a guess.
- Your negotiation settlement serves at least one interest that neither published position mentioned - and you noticed that SGD 19,500 exceeds the PM's SGD 15,000 procurement authority and requires the CCB.
