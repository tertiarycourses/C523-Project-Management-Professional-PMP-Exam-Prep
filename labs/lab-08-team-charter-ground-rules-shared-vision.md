# Lab 08 - Team Charter, Ground Rules and Shared Vision

| Field | Value |
| --- | --- |
| Topic | 2 - Start the Project |
| ECO 2026 task | People T1 - Develop a common vision; People T3 - Lead the project team |
| Duration | 45 minutes |
| Consumes | Lab 06 charter, success criteria and PM authority levels; Lab 07 stakeholder register and engagement matrix |
| Produces | `artifacts/08-team-charter.md`, `artifacts/08-ground-rules.md`, `artifacts/08-vision-statement.md` |

## Objectives

- Write a shared project vision that the team can recall without reading it, and test it against explicit criteria.
- Build a team charter naming all 9 team members, their skills, their capacity and their working agreement.
- Set ground rules across six categories, each with an observable, testable standard.
- Choose the decision-making rule for each class of decision - consent, consensus or command - and state when each applies.
- Define the definition of done that the QA lead and the developers will both accept.
- Design a graduated response to ground-rule violations before the first violation happens.
- Establish how the vision and the charter stay current rather than becoming week-1 wallpaper.

## Vision, charter and ground rules are three different things

```text
VISION
  ONE statement of the future state the team is creating and why it matters.
  Aspirational, memorable, outcome-focused. Answers "why are we here?"
  Owned by the whole team. Rarely changes.

TEAM CHARTER
  The team's operating document. Who we are, what we are each good at, how
  we work together, how we decide, what we owe each other. Answers
  "how do we work?" Created BY the team, not issued to them. Reviewed
  periodically.

GROUND RULES
  The specific, observable behaviours the charter commits to. Answers
  "what exactly does that look like on a Tuesday?" Ground rules must be
  testable - if you cannot tell whether one was broken, it is not a
  ground rule, it is a sentiment.

Exam tell: the PROJECT charter (Lab 06) is issued by the sponsor and
authorises the project. The TEAM charter is produced by the team and governs
how they work. A question about authority to spend points at the project
charter. A question about how the team handles disagreement points at the
team charter.
```

## Steps

### Step 1 - Draft the shared vision statement

Create `artifacts/08-vision-statement.md`. The ECO People T1 enablers are "examine the vision and mission", "establish a shared vision" and "support and maintain the vision". You start with the charter's purpose (Lab 06 Step 2) and the success criteria (Lab 06 Step 3), and compress them into something a developer can repeat in a corridor.

A worked example for Contoso:

```text
DRAFT 1 (too long, and it is a scope statement, not a vision)
  "We will deliver a responsive course registration portal with automated
   learner communications, PDPA-compliant consent capture, regulatory reporting data
   support and payment gateway v2 integration, by 30 June, within SGD 480,000."

DRAFT 2 (better, but no human in it)
  "We will cut registration time from 11 minutes to under 4 and abandonment
   from 34% to under 15%."

DRAFT 3 - ADOPTED
  "In four minutes, on a phone, anyone can book the course that changes
   their year - and nobody at Contoso has to retype it."

  Why this one works
    - It names the user, not the system.
    - The two numbers that matter (4 minutes, mobile) are inside it.
    - The second clause honours S-06, the three admin staff whose 24 hours
      a week of manual work is the other half of this project - so the
      vision includes the group most at risk of being treated as collateral.
    - It is 24 words. A developer can recall it in a design argument, which
      is the only test that matters.
```

Test your own draft against these criteria and record the result:

| Criterion | Test | Contoso draft 3 | Your draft |
| --- | --- | --- | --- |
| Memorable | Can a team member repeat it 3 days later without notes? | Yes, 24 words | |
| Outcome, not output | Does it describe a changed world, not a delivered artifact? | Yes - a booking experience, not a portal | |
| Measurable trace | Can you point from it to at least 2 success criteria? | SC-1 (4 min), SC-4 (mobile), SC-3 (admin hours) | |
| Inclusive | Does every one of the 9 team members see their contribution in it? | Yes - UX, dev, content, QA all serve it | |
| Directional | Does it settle at least one real design argument? | Yes - it kills any "one more field on the form" request | |
| Honest | Would you say it in front of S-06, the admin staff? | Yes - it names their relief explicitly | |

The last criterion is the one teams skip. A vision that would embarrass you in front of the people it affects is a slogan.

### Step 2 - Name the team

Create `artifacts/08-team-charter.md`. The Lab 06 constraint CON-4 fixes the team at 9 people with no additional headcount, so this list is complete and permanent. Capacity is stated in story points per 2-week sprint and totals the Lab 06 figure of approximately 34.

| # | Name | Role | Primary skills | Sprint capacity (pts) | Known development need |
| --- | --- | --- | --- | --- | --- |
| T-1 | Rajesh Menon | Development lead | Java, API design, system architecture, mentoring | 6 | Delegating instead of coding the hard part himself |
| T-2 | Wei Ling Chua | Senior developer | Front-end, React, accessibility (WCAG 2.1 AA) | 7 | Payment gateway domain knowledge |
| T-3 | Daniel Ofori | Developer | Back-end, data migration, SQL | 6 | Automated testing practice |
| T-4 | Aisha Rahman | Developer | Integration, payment gateways, security | 6 | First project at this scale; needs pairing early |
| T-5 | Nurul Idris | UX designer | Research, prototyping, usability testing, mobile-first | 4 | Facilitating sessions with hostile stakeholders |
| T-6 | Kenneth Lau | QA lead | Test strategy, automation, regression suites, defect triage | 3 | Being included at design time, not handed builds |
| T-7 | Farah Ismail | Business analyst | Requirements, PDPA and regulatory domain, traceability | 2 | Overloaded - see the Step 7 capacity note |
| T-8 | Vikram Shah | DevOps engineer | CI/CD, environments, release automation, monitoring | Enabling, not story-point bearing | Handover documentation for S-11 IT Ops |
| T-9 | Grace Tay | Content lead | Communications copy, tone, learner comms templates | Enabling, not story-point bearing | PDPA consent-wording constraints |
| | | | **Story-point capacity** | **32 + spike allowance = approx. 34** | |

Record the external roles the team works with daily but who are not team members - this prevents the recurring confusion about who the product owner reports to:

| Person | Relationship to the team | From Lab 07 |
| --- | --- | --- |
| Marcus Tan, Head of L&D Ops | Product owner. Owns backlog priority. Not the team's manager. | S-03 |
| Priya Nathan, COO | Sponsor. Owns the business case and the gates. | S-01 |
| Data Protection Officer | Gate G3 owner. Consulted from sprint 1, not at the end. | S-04 |
| The 3 admin staff | SMEs with capped hours, and the users. | S-06 |
| IT Operations Manager | Receives the system at handover. Reviews at G1 and G2. | S-11 |

### Step 3 - Write the working agreement on time and availability

The team is not co-located: Daniel Ofori works from Accra (GMT), everyone else is in Singapore (GMT+8). That is an 8-hour offset with only a narrow natural overlap, so core hours must be explicit or they will be discovered by accident.

```text
TIME-ZONE ARITHMETIC

  Singapore (SGT, GMT+8)   09:00  10:00  14:00  17:00  18:00
  Accra     (GMT+0)        01:00  02:00  06:00  09:00  10:00

  Daniel's working day 09:00-18:00 GMT  =  17:00-02:00 SGT
  Singapore working day 09:00-18:00 SGT =  01:00-10:00 GMT

  NATURAL OVERLAP  17:00-18:00 SGT / 09:00-10:00 GMT  =  ONE hour.

  AGREED CORE HOURS  16:00-19:00 SGT / 08:00-11:00 GMT  =  THREE hours.
    Singapore team shifts one hour later on Tue/Thu.
    Daniel starts at 08:00 GMT on Tue/Thu.
    Standup is at 16:15 SGT / 08:15 GMT, not 09:15 SGT.

  Consequence recorded honestly: Singapore members lose an hour of evening
  twice a week and Daniel starts early twice a week. The cost is shared, not
  imposed on the person in the minority time zone. That is the point.
```

| Agreement | Standard |
| --- | --- |
| Core hours | 16:00-19:00 SGT / 08:00-11:00 GMT, Monday to Friday |
| Standup | 16:15 SGT / 08:15 GMT, 15 minutes, timeboxed, camera on |
| Meeting-free block | 09:00-12:00 SGT for the Singapore members; 13:00-16:00 GMT for Daniel |
| Outside core hours | Asynchronous only. No expectation of a reply |
| Annual leave | Declared in the shared calendar before sprint planning; capacity reduced accordingly in that sprint's commitment |
| On-call | None until launch week; launch-week rota agreed at sprint 11 |

### Step 4 - Set ground rules across six categories

Create `artifacts/08-ground-rules.md`. Every rule must be observable. "Be respectful" is not a ground rule; "no interrupting - use the raise-hand" is.

| # | Category | Ground rule | How you can tell it was broken |
| --- | --- | --- | --- |
| GR-1 | Meetings | Standup is 15 minutes and timeboxed. Anything needing discussion is parked and taken after | The standup ran to 25 minutes |
| GR-2 | Meetings | Every meeting has a stated purpose and a named decision or output before the invite goes out | An invite with no agenda |
| GR-3 | Meetings | Camera on for standup, sprint review and retrospective. Off is fine for working sessions | A black square at retro |
| GR-4 | Decisions | Decisions are recorded in the decision log within 24 hours with the rationale, not just the outcome | A decision nobody can find or explain a month later |
| GR-5 | Decisions | Anyone may ask "is this a consent, consensus or command decision?" at any point and get an answer | The question is deflected |
| GR-6 | Communication | Channel messages during core hours: reply within 4 working hours. Outside core hours: next working day | A 3-day-old unanswered question |
| GR-7 | Communication | Blockers are raised the moment they are known, not at the next standup | A blocker surfaced at standup that was known yesterday |
| GR-8 | Communication | No decision that affects another person's work is taken in a private direct message. Move it to the team channel | A change nobody else saw coming |
| GR-9 | Code quality | No merge to main without one reviewer approval and a green CI run | A red build on main |
| GR-10 | Code quality | The definition of done in Step 5 applies to every story with no exceptions and no "we will test it later" | A story marked done with no test |
| GR-11 | Code quality | Automated regression suite must stay green. A red suite is the team's top priority until it is green | A suite red for more than one day |
| GR-12 | Conflict | Disagreement goes to the person first, the team second, the PM third. Never to the sponsor first | The PM hears about it from Priya Nathan |
| GR-13 | Conflict | Attack the design, never the designer. Say "this approach has a problem", not "you have a problem" | Personal language in a review comment |
| GR-14 | Conflict | Anyone may call a 10-minute cool-off in a heated discussion and it is granted without argument | The call is overridden |
| GR-15 | Work hours | No expectation of work outside core and declared hours. Nobody is judged on message timestamps | A late-night reply praised in front of the team |
| GR-16 | Work hours | Overtime is a schedule signal, not a solution. Two consecutive weeks of overtime triggers a re-plan | Sustained overtime with no re-plan |

The team must write GR-16's number themselves. A ground rule the team was handed is a policy; a ground rule the team wrote is a commitment.

### Step 5 - Agree the definition of done

The Lab 16 storming narrative is caused by a definition of done that was never agreed. Agree it now, with the QA lead (T-6 Kenneth Lau) in the room, not after the fact.

```text
DEFINITION OF DONE - Contoso Training Portal Upgrade

  A user story is DONE when ALL of the following are true:

   1  Acceptance criteria on the story card are all demonstrably met.
   2  Code reviewed and approved by at least one developer other than the author.
   3  Unit tests written and passing; coverage on new code not below 70%.
   4  Automated regression suite green after merge.
   5  Accessibility checked to WCAG 2.1 AA on any learner-facing UI (charter IN-9).
   6  Responsive behaviour verified on mobile, tablet and desktop breakpoints.
   7  Any personal-data field mapped in the PDPA data inventory (charter IN-4).
   8  Deployed to the staging environment and demonstrable there.
   9  Product owner (Marcus Tan) has accepted it in staging.
  10  Any operational runbook change written for S-11 IT Ops handover.

  NOT part of done: deployed to production. Release is a separate decision
  taken at gate level, not by the team story by story.

  DEFINITION OF READY - a story may not enter a sprint until:
   -  It has acceptance criteria.
   -  It is estimated by the team, not for the team.
   -  Its dependencies are identified and unblocked or scheduled.
   -  Its PDPA impact is known (yes/no), so item 7 above is not a surprise.
```

The distinction between done and released is the one most often missed. If the team defines done as "in production", they cannot finish anything between gate G2 (week 18) and go-live (30 June), which is 6 weeks of work with nothing marked complete.

### Step 6 - Choose the decision-making rule for each decision class

Three rules, three legitimate uses. The error is using one rule for everything - consensus on everything is paralysis, command on everything destroys ownership.

```text
CONSENSUS   Everyone actively agrees. Slow, highest buy-in.
            Use when: the decision binds everyone's daily behaviour and
            requires willing compliance (ground rules, working agreement).

CONSENT     Nobody has a reasoned, principled objection. Not "everyone
            loves it" - "nobody can name a reason this will harm us".
            Much faster than consensus and usually good enough.
            Use when: the decision is reversible and a good-enough answer
            now beats a perfect answer next week (most technical choices).

COMMAND     One named person decides. Others are consulted, then it is
            decided. Fast, lowest buy-in, sometimes the only correct rule.
            Use when: it is genuinely one person's accountability (safety,
            compliance, legal, budget), when the group is deadlocked, or
            when time has run out.
```

| Decision class | Rule | Decider | Why this rule |
| --- | --- | --- | --- |
| Ground rules and working agreement | Consensus | Whole team | Requires willing daily compliance; imposed rules are not followed |
| Definition of done | Consensus | Whole team incl. QA lead | Both dev and QA must accept it or it becomes the Lab 16 conflict |
| Sprint commitment (how much) | Consent | Development team | Team owns its capacity; PM and PO may not commit for them |
| Backlog priority (what order) | Command | Marcus Tan, product owner | It is the PO's accountability. Team is consulted, PO decides |
| Technical design within a story | Consent | Rajesh Menon as dev lead | Reversible, needs speed, needs no objection rather than enthusiasm |
| Architecture affecting all sprints | Consensus, then command if deadlocked after one timeboxed session | Rajesh Menon | See the Lab 17 role-play - deadlock has a decider named in advance |
| PDPA and compliance interpretation | Command | DPO (S-04) | Regulatory accountability sits with one named officer. Not a vote |
| Release go / no-go | Command | Priya Nathan at gate G3 | Sponsor accountability per the Lab 03 governance model |
| Change requests over SGD 10,000 | Command | Per Lab 03 escalation thresholds | Already set by governance; the team does not re-decide it |
| Who does which task in a sprint | Consent | Team self-organises | ECO People T3 - empower the team; PM assigns only if the team cannot |

Write the rule for each class into the team charter and name the decider. The single highest-value line in a team charter is a named decider for the deadlock case, agreed before the deadlock.

### Step 7 - Build the skills and capacity matrix

Rate 1 (no capability) to 5 (can lead and teach). This exposes single points of failure while there is still time to do something about them.

| Capability | Rajesh | Wei Ling | Daniel | Aisha | Nurul | Kenneth | Farah | Vikram | Grace | Team min |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Front-end / React | 3 | 5 | 2 | 3 | 2 | 2 | 1 | 1 | 1 | 2 people at 3+ |
| Back-end / API | 5 | 3 | 4 | 4 | 1 | 2 | 1 | 2 | 1 | Healthy |
| Payment gateway v2 | 2 | 1 | 1 | 4 | 1 | 2 | 1 | 1 | 1 | **RISK - one person** |
| Data migration | 2 | 1 | 4 | 2 | 1 | 2 | 3 | 2 | 1 | Thin |
| Test automation | 3 | 3 | 2 | 3 | 1 | 5 | 1 | 3 | 1 | Healthy |
| Accessibility WCAG 2.1 AA | 2 | 4 | 1 | 2 | 4 | 3 | 1 | 1 | 2 | Adequate |
| PDPA / regulatory domain | 1 | 1 | 1 | 2 | 1 | 2 | 5 | 1 | 3 | **RISK - one person** |
| CI/CD and environments | 2 | 2 | 2 | 2 | 1 | 3 | 1 | 5 | 1 | **RISK - one person** |
| UX research and testing | 1 | 2 | 1 | 1 | 5 | 2 | 3 | 1 | 2 | Thin |

Three single points of failure fall out of this immediately, and each needs a named action now:

| Gap | Consequence if that person is unavailable | Action | Owner | By |
| --- | --- | --- | --- | --- |
| Payment gateway - only Aisha (T-4) at 4 | Integration stops. Charter assumption A-03 is already flagged as unvalidated | Wei Ling pairs with Aisha on the sprint-1 gateway spike; both attend vendor briefing | Rajesh | Sprint 1 |
| PDPA / regulatory - only Farah (T-7) at 5, and she carries only 2 pts because she is spread across 3 workstreams | Compliance requirements stall; gate G3 at risk | Grace Tay shadows Farah on consent wording; capped SME hours from S-06 admin staff agreed per Lab 06 assumption A-07 | PM | Week 2 |
| CI/CD - only Vikram (T-8) at 5 | No deployments, no releases | Kenneth (already 3) documents the pipeline and runs one release himself in sprint 4 | Vikram | Sprint 4 |

Note Farah's row against her capacity of 2 points in Step 2. She is the constraint on the requirements workstream and the compliance workstream at the same time. This is exactly the overload that surfaces as visible strain in the Lab 16 sprint-3 diagnosis - it is predictable from this matrix in week 1.

### Step 8 - Design the graduated response to ground-rule violations

ECO People T2 carries the enabler "manage and rectify ground rule violations". A response designed after the first violation looks like a punishment aimed at a person. A response designed in week 1 looks like a process.

| Level | Trigger | Response | Who acts | Recorded? |
| --- | --- | --- | --- | --- |
| 0 - Prevention | Ground rules agreed and visible | Rules posted in the team channel and read at each sprint planning | Team | No |
| 1 - In the moment | First occurrence, minor, no harm done | Any team member names it neutrally at the time: "that is GR-1, we are over time, let us park it" | Any team member | No |
| 2 - Private word | Repeat of the same rule by the same person | PM or the affected person speaks privately, curious first: what is making this rule hard to keep? | PM or peer | Note to self only |
| 3 - Team retrospective | Pattern affecting the team, or a rule the team keeps breaking collectively | Raised at retrospective as a rule problem, not a person problem. Either the behaviour changes or the rule changes | Team, facilitated by PM | Retro action with owner and date |
| 4 - Formal 1:1 | Level 2 and 3 have not changed the behaviour, and delivery or another person is being harmed | Documented 1:1: specific observed behaviour, specific impact, specific expected change, review date within 2 weeks | PM | Written, shared with the person |
| 5 - Escalation | Behaviour continues after level 4, or is a single serious breach (harassment, safety, a compliance violation) | Escalate to the functional manager and, where relevant, HR. Level 5 skips straight to here - see the note below | PM | Formal |

```text
TWO RULES ABOUT THE LADDER

  1. START AT LEVEL 1. The most common PM failure is jumping to level 4 or 5
     on a first occurrence, or to level 5 without ever having had a level 2
     conversation. On the exam, an option that disciplines, removes or reports
     a team member as the FIRST action is nearly always wrong.

  2. SOME THINGS SKIP THE LADDER ENTIRELY. Harassment, discrimination, a
     safety breach, or a deliberate compliance or legal violation goes to
     level 5 immediately. Graduated response is for norm violations, not for
     conduct that is itself a breach. Knowing which is which is the exam
     discrimination.

  Curiosity before correction: at level 2, the first question is not
  "why did you break the rule" but "what is making this rule hard to keep?"
  Half of the time the rule is wrong, not the person. GR-6's 4-hour reply
  window is unkeepable for Daniel across an 8-hour offset - that is a rule
  defect the ladder should surface, not a discipline case.
```

### Step 9 - Forward-reference the RACI and set the vision review cadence

The team charter says who is on the team and how they work. It does not say who is accountable for each deliverable - that is the RACI, built in Lab 15. Record the placeholder now so the two documents stay linked:

| Deliverable area | Likely accountable (A) - confirmed in Lab 15 | Likely responsible (R) |
| --- | --- | --- |
| Registration flow | Marcus Tan (PO) | Wei Ling, Rajesh |
| Payment integration | Rajesh Menon | Aisha |
| Data migration | Rajesh Menon | Daniel |
| PDPA compliance evidence | DPO (S-04) | Farah |
| Test strategy and regression suite | Kenneth Lau | Kenneth, Daniel |
| Learner communications content | Grace Tay | Grace, Nurul |
| Environments and release | Vikram Shah | Vikram |
| Usability testing | Nurul Idris | Nurul, Farah |

Exactly one A per row. If you find yourself wanting two, that is the ambiguity Lab 15 exists to remove and Lab 17 exists to resolve when it turns into conflict.

Finally, the People T1 enabler "support and maintain the vision" needs a mechanism, not an intention:

| Mechanism | Cadence | Owner | What happens |
| --- | --- | --- | --- |
| Vision read aloud at sprint planning | Every 2 weeks | Rotating team member | 20 seconds. Keeps it in working memory |
| Vision tested against the sprint goal | Every sprint planning | PM | If the sprint goal does not serve the vision, one of the two is wrong |
| Vision checked against real learner behaviour | Sprint 3, 5, 7 usability tests | Nurul Idris | Learners either experience the vision or they do not |
| Vision reviewed for continued truth | At gates G1, G2, G3 | Whole team + sponsor | Amend only with the sponsor present |
| Charter and ground rules reviewed | Every 3rd retrospective (sprints 3, 6, 9, 12) | Team | Rules that no longer fit are changed, not quietly ignored |

A vision that is not reread is a poster. The sprint-planning read-aloud costs 20 seconds every two weeks and is the single cheapest thing in this lab.

### Step 10 - Answer the exam-style scenarios

```text
SCENARIO 1
Two weeks into the project you notice the daily standup routinely runs to 25
minutes because the developers debug problems in it. Ground rule GR-1 says the
standup is 15 minutes and timeboxed. What should you do FIRST?

  A. Raise it in your next 1:1 with the development lead and ask him to
     control his developers.
  B. At the next standup, name it neutrally in the moment - "that is GR-1, let
     us park this and take it after" - and hold the timebox.
  C. Escalate to the functional manager that the team is not following its
     agreed working practices.
  D. Remove the standup from the calendar and replace it with a written update.

SCENARIO 2
The QA lead says a story is not done because it has no automated test. The
developer says the acceptance criteria are met and the story should be closed
so the sprint burndown looks right. Both are looking at you. What is the BEST
response?

  A. Decide in favour of the QA lead because quality comes first.
  B. Decide in favour of the developer because the acceptance criteria are the
     contract for the story.
  C. Point both to the agreed definition of done, which requires unit tests
     passing, and ask them to apply it; if the definition itself is wrong,
     raise it at the retrospective for the whole team to change.
  D. Split the difference - close the story and raise the missing test as a
     new story in the next sprint.

SCENARIO 3
A developer working from a different time zone has repeatedly failed to reply
within the 4-hour window that ground rule GR-6 requires. He is a strong
performer and his work is on time. What should the project manager do?

  A. Document a formal warning under the ground-rule violation process.
  B. Have a private conversation asking what makes the rule hard to keep, and
     be prepared to change the rule if the answer is the time-zone offset.
  C. Raise it publicly at the retrospective so the whole team sees the rule
     matters.
  D. Exempt him from GR-6 quietly so the issue goes away.
```

Answer key:

```text
SCENARIO 1 -> B.  Level 1 of the graduated response: name it in the moment,
            neutrally, at the point of occurrence. It is the lowest-cost
            intervention and it reinforces that the rule belongs to the team,
            not to the PM. A routes a team norm through a manager and makes it
            about a person. C is level 5 for a level 1 event - a classic wrong
            answer shape. D deletes a valuable ceremony to avoid enforcing a
            rule, and loses the team's only synchronous daily contact across
            time zones.

SCENARIO 2 -> C.  The team already decided this in Step 5, with the QA lead in
            the room, by consensus. The PM's job is not to adjudicate on the
            merits - that would make every future done/not-done argument the
            PM's to settle - but to apply the agreement the team made and give
            them the legitimate route to change it. A and B both have the PM
            overruling a team decision. D is the worst: it books the debt into
            a future sprint and quietly redefines done to mean "nearly done",
            which is how the Lab 16 storming conflict begins.

SCENARIO 3 -> B.  Level 2, and with curiosity before correction. A 4-hour reply
            window is unkeepable across an 8-hour offset - the rule is the
            defect, not the developer, and the private conversation is what
            surfaces that. A jumps to level 4 for a rule that may itself be
            wrong. C makes an example of a person in front of the team, which
            damages psychological safety far more than a late reply damages
            delivery. D creates a private exception nobody else knows about,
            so the rule is now unequal and unenforceable - and it hides the
            defect instead of fixing it for everyone.
```

## Deliverable

Submit to `artifacts/`:

- `08-vision-statement.md` - the adopted vision, at least two rejected drafts with the reason each was rejected, and the six-criterion test table completed.
- `08-team-charter.md` - all 9 team members with names, roles, skills, sprint capacity and development needs; the external roles table; the working agreement including core hours with the time-zone arithmetic shown; the decision-rule table with a named decider per decision class; the skills matrix with all three single points of failure identified and a dated action for each; the RACI forward reference with exactly one A per row.
- `08-ground-rules.md` - at least 16 ground rules across the six categories, each with an observable violation test; the definition of done and the definition of ready; the six-level graduated response ladder including the note on which breaches skip it.
- The vision maintenance cadence table.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your vision is under 30 words and you can trace it to at least two Lab 06 success criteria by number.
- You can state the difference between the project charter (Lab 06) and the team charter, including who issues each.
- Every ground rule has a violation test. If you cannot describe what breaking it looks like, rewrite it or delete it.
- Your definition of done separates "done" from "released", and you can explain why merging the two would stall the team between week 18 and 30 June.
- Your decision table uses at least two different rules and names a specific person as decider for every command-rule row.
- Your architecture row names a decider for the deadlock case, decided before any deadlock exists.
- Your skills matrix identifies at least three single points of failure, each with a named owner and a dated mitigating action.
- Your graduated response starts at "name it in the moment" and states which categories of breach bypass the ladder entirely.
- Your core hours agreement distributes the time-zone cost across the team rather than loading it entirely on the member in the minority time zone.
- Your vision has a scheduled review mechanism with an owner. An unreviewed vision is decoration.
