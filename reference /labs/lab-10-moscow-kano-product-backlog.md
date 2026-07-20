# Lab 10 - MoSCoW, Kano and the Product Backlog

| Field | Value |
| --- | --- |
| Topic | 3 - Plan the Project |
| ECO 2026 task | Process T3 - Help ensure value-based delivery; Process T2 - Develop and manage project scope |
| WSQ learning outcome | LO1 - Scope medium-scale project requirements to drive timely completions |
| Duration | 90 minutes |
| Consumes | Lab 09 requirements register REQ-001 to REQ-031; Lab 05 benefits map B1-B4; Lab 07 stakeholder expectations and misalignment M-1 |
| Produces | `artifacts/10-moscow.md`, `artifacts/10-kano.md`, `artifacts/10-product-backlog.md`, `artifacts/10-release-plan.md` |

## Objectives

- Apply MoSCoW with the discipline rules that make it a prioritisation tool rather than a labelling exercise.
- Apply the Kano model and understand why customer satisfaction is not linear with functionality.
- Use the productive disagreement between MoSCoW and Kano to find the requirements both would have got wrong alone.
- Write a product backlog of well-formed user stories with relative estimates.
- Compute a release plan against real capacity and prove the Must-haves land before gate G2.
- Make the AI recommender trade-off from Lab 07 misalignment M-1 concrete and numeric.

## Prioritisation: the two models and why you need both

```text
MoSCoW - prioritisation by OBLIGATION. Answers "what must ship?"

  MUST     Launch FAILS without it. The test is brutal and specific:
           is it legally required, contractually required, or is the
           product not viable without it? If the answer to all three is
           no, it is not a Must. "The sponsor wants it" is not a Must.
  SHOULD   Important, painful to omit, but there is a workaround. The
           product is viable, if diminished, without it.
  COULD    Desirable. Included if capacity allows. First to be dropped.
  WON'T    Explicitly excluded from THIS release. Not "no" - "not now".
           Recording Won'ts is what stops them being re-argued weekly.

  THE DISCIPLINE RULE that makes MoSCoW work:
    MUSTS SHOULD BE ROUGHLY 60% OR LESS OF TOTAL EFFORT.
    If Musts are 90% of effort, you have no flex. The first problem that
    arises consumes your entire buffer and you are then choosing between
    missing the date and dropping something you called mandatory. A plan
    with no Coulds is a plan with no shock absorber. When everything is
    a Must, nothing is - and the prioritisation has done no work.

KANO - prioritisation by SATISFACTION. Answers "what will they notice?"

  BASIC / MUST-BE        Expected. Presence produces NO satisfaction;
                         absence produces STRONG dissatisfaction.
                         Asymmetric and unforgiving. Nobody praises a site
                         for loading; everybody condemns one that does not.
  PERFORMANCE /          Satisfaction rises LINEARLY with how much you
  ONE-DIMENSIONAL        deliver. More is better, and customers can
                         articulate wanting it. Speed, price, capacity.
  EXCITEMENT / DELIGHTER Unexpected. Absence produces NO dissatisfaction
                         because it was never anticipated; presence
                         produces disproportionate delight.
  INDIFFERENT            Customers do not care either way. Building these
                         is pure waste and they are easy to miss because
                         someone internally always wants them.
  REVERSE                Presence produces DISSATISFACTION. More is worse.
                         Forced account creation, mandatory newsletters.

  THE TIME DECAY - the part candidates forget and the exam likes:
    Kano categories MIGRATE DOWNWARD over time. Today's delighter becomes
    tomorrow's performance attribute and then next year's basic.
      Mobile responsiveness: DELIGHTER in 2012, PERFORMANCE by 2016,
                             BASIC by 2020 and unarguably BASIC in 2026.
      Free shipping, instant confirmation emails, dark mode - same path.
    Consequence: a Kano classification has an expiry date. Contoso's 41%
    mobile completion is not a missing delighter; it is a missing BASIC,
    which is why it produces dissatisfaction rather than indifference,
    and why it outranked the AI recommender 25 to 16 in the Lab 02 scan.
```

## Steps

### Step 1 - Apply MoSCoW to the Lab 09 requirements

Create `artifacts/10-moscow.md`. Test every candidate Must against the three-part question before accepting it.

| Requirement | Legally required? | Contractually required? | Product non-viable without it? | MoSCoW | Reasoning |
| --- | --- | --- | --- | --- | --- |
| REQ-010 Single-form registration | No | No | Yes | **Must** | This is the product. Without it there is no upgrade |
| REQ-018 PDPA consent capture | Yes | No | Yes | **Must** | PDPA obligation, C-01/C-02. Cannot launch without it |
| REQ-019 SSG NRIC attendance | Yes | Yes | Yes | **Must** | Funding claims fail without it; regulator S-15 |
| REQ-020 Gateway v2 payment | No | Yes | Yes | **Must** | v1 is being deprecated; no payment means no registration |
| REQ-022 Page load under 2.0s | No | No | Yes | **Must** | A slow mobile flow reproduces the 34% abandonment; the benefit case fails |
| REQ-025 WCAG 2.1 AA | Yes | No | No | **Must** | Accessibility obligation C-11; also 40,000 to retrofit vs 8,000 built in |
| REQ-027 Data migration | No | No | Yes | **Must** | Learners must retain their bookings at cutover |
| REQ-011 Save and resume | No | No | No | **Should** | Recovers some abandonment; workaround is starting again |
| REQ-006 Admin template editing | No | No | No | **Should** | Developer can edit templates as a workaround; costs the B2 benefit partially |
| REQ-007 IT Ops runbook | No | No | No | **Should** | Handover possible without it but supportability suffers |
| REQ-031 Fewer than 8 escaped defects | No | No | No | **Should** | A quality target, not a shippable feature |
| Saved payment methods | No | No | No | **Could** | Convenience; no benefit line depends on it |
| Waitlist for full courses | No | No | No | **Could** | Desirable; no baseline metric attached |
| AI course recommender | No | No | No | **Won't** | Charter exclusion OUT-1; 55 points; deferred to phase 2 |
| Native mobile apps | No | No | No | **Won't** | Charter exclusion OUT-7; responsive web meets R-6 |

Now do the arithmetic that most teams skip. Using the story points you will assign in Step 3:

```text
MoSCoW EFFORT SPLIT - the discipline check

  Must     202 points
  Should   123 points
  Could     76 points
  TOTAL    401 points

  Must as a share of total effort  =  202 / 401  =  50.4%

  VERDICT: PASSES the 60% rule with room to spare.

  What this actually means operationally: if the project loses 199 points
  of capacity to risk, rework or absence, every Must-have still ships. That
  is the shock absorber. Compare the alternative many teams produce:

  A BADLY PRIORITISED VERSION of the same backlog
    Must     360 points  (89.8%)
    Should    31 points
    Could     10 points
  This plan delivers the same product on a good day and fails completely on
  a normal one. There is nothing to drop. The first serious risk event
  forces a date conversation with the sponsor, and that conversation is
  avoidable - it was created by the prioritisation, not by the risk.

  Note also that the Won't list has a POINT VALUE. AI recommender 55 points.
  Won'ts are not free-floating opinions; they are quantified decisions.
```

### Step 2 - Classify the features on Kano

Create `artifacts/10-kano.md`. Classify by asking the Kano pair of questions for each feature: how would you feel if the feature were present, and how would you feel if it were absent.

| # | Feature | If present | If absent | Kano class | Note |
| --- | --- | --- | --- | --- | --- |
| K-01 | Registration completes successfully | Expected | Angry | **Basic** | Nobody thanks you for this |
| K-02 | Page loads under 2.0s on mobile | Expected | Frustrated | **Basic** | Was a performance attribute in 2015. Time decay has made it basic |
| K-03 | Mobile responsive layout | Expected | Angry | **Basic** | Delighter in 2012, basic in 2026. This is the textbook decay case |
| K-04 | Booking confirmation email arrives | Expected | Anxious, contacts support | **Basic** | Absence generates support tickets, which is B3 |
| K-05 | PDPA consent screen | Neutral | Neutral (learner), Angry (regulator) | **Basic** | Learners are indifferent; the regulator is not. Basic by obligation |
| K-06 | WCAG 2.1 AA accessibility | Neutral for most, essential for some | Excluded entirely for some users | **Basic** | For the affected users this is binary, not incremental |
| K-07 | Registration speed under 4 min | Pleased, and more so the faster | Dissatisfied, increasingly | **Performance** | Linear. 3 minutes beats 4 beats 5 |
| K-08 | Number of clicks to register | Pleased, fewer is better | Dissatisfied | **Performance** | Directly linear; drives the 12-field cap |
| K-09 | Course search filter richness | Pleased, more filters better to a point | Mildly dissatisfied | **Performance** | Diminishing returns beyond about five filters |
| K-10 | Self-service reschedule | Delighted - they expected to phone | No dissatisfaction; they phone as always | **Excitement** | Currently a delighter, and B3 depends on it. Will be basic within three years |
| K-11 | Save and resume a registration | Pleasantly surprised | Not noticed | **Excitement** | Nobody asks for it; those who hit it are grateful |
| K-12 | Download attendance record instantly | Delighted | Not noticed - they email admin | **Excitement** | Also removes admin work, so it pays twice |
| K-13 | Course recommendations by AI | Mildly interested | Not noticed | **Indifferent** | The Lab 02 scan scored it 16. Learners arrive knowing what they want |
| K-14 | Mandatory account creation before browsing | Annoyed, some leave | Relieved | **Reverse** | Adding this REDUCES satisfaction. A live cause of the 34% abandonment |

```text
THE TWO CONCLUSIONS THAT CHANGE THE PLAN

K-14 is a REVERSE feature that ALREADY EXISTS in the legacy portal. The
current system forces account creation before a learner can browse. Kano
says this actively produces dissatisfaction. REMOVING functionality is
therefore a value-adding change - REQ-009 specifies guest browse without
login precisely for this reason. Reverse features are the only Kano class
where the correct backlog item is a deletion, and teams routinely miss them
because a backlog is a list of things to add.

K-13, the AI recommender, is INDIFFERENT. This is the strongest available
answer to the Lab 07 M-1 misalignment. The Head of Sales frames it as a
competitive necessity; Kano evidence from actual learners says its presence
produces mild interest and its absence produces nothing. That is not an
argument about importance - it is data about satisfaction.
```

### Step 3 - Where MoSCoW and Kano disagree, and why that is useful

Running both models produces conflicts. The conflicts are the point; if the two models agreed everywhere, one of them would be redundant.

| Feature | MoSCoW | Kano | Conflict | Resolution |
| --- | --- | --- | --- | --- |
| K-05 PDPA consent screen | **Must** | **Basic** (learners indifferent) | None - they agree, but for different reasons | A Kano BASIC must always be a MoSCoW MUST. Basics are invisible when present and fatal when absent. This is the reliable rule |
| K-03 Mobile responsive | **Must** | **Basic** | Agree | Same rule. Time decay made it basic; obligation to the benefit case makes it Must |
| K-10 Self-service reschedule | **Must** (B3 benefit depends on it) | **Excitement** | Kano says learners would not miss it | Keep as Must. The benefit is internal - 1,100 fewer tickets at SGD 22 - not learner satisfaction. Kano measures customer delight, not business value |
| K-11 Save and resume | **Should** | **Excitement** | A delighter that is only a Should | Correct. Delighters are legitimate Shoulds and Coulds. They deliver disproportionate satisfaction per point but the product is viable without them |
| K-12 Instant record download | **Could** | **Excitement** | A delighter demoted to Could | Correct and deliberate. This is where a Kano delighter SHOULD be a MoSCoW Could - if capacity appears, this is the highest-satisfaction-per-point item to pull in |
| K-13 AI recommender | **Won't** | **Indifferent** | Agree | Two independent models reaching the same conclusion is the evidence to take to the M-1 session |
| K-09 Search filter richness | **Should** | **Performance** | Performance attributes are where competitors compete | Deliver a viable minimum as Must (REQ-009), improvements as Should. Performance attributes are the natural home of incremental delivery |

```text
THE RULES THAT FALL OUT OF THE CONFLICT ANALYSIS

  A Kano BASIC must be a MoSCoW MUST.
      No exceptions. Basics are the entry ticket. Omitting one does not
      reduce satisfaction proportionally - it produces failure.

  A Kano DELIGHTER can safely be a MoSCoW COULD.
      Its absence causes no dissatisfaction, by definition. Delighters are
      the correct thing to have in the flexible part of the plan: high
      upside if capacity appears, no downside if it does not.

  A Kano INDIFFERENT should usually be a MoSCoW WON'T.
      Nobody cares. Building it is waste with a schedule cost.

  A Kano REVERSE should generate a REMOVAL item, not an addition.

  BASICS ARE NOT WHERE YOU COMPETE. Doing basics excellently produces no
  advantage - it only avoids failure. Contoso's competitive gain comes from
  performance attributes (speed, clicks) and delighters (self-service),
  which is why the plan buys basics to the minimum acceptable standard and
  spends its remaining capacity on the other two.
```

### Step 4 - Write the product backlog

Create `artifacts/10-product-backlog.md`. Every story uses the form: **As a `<role>`, I want `<capability>`, so that `<benefit>`.** The "so that" clause is not decoration - a story whose benefit clause cannot be completed is a story with no traceable value, and Lab 09's backward traceability would flag it as gold plating.

| ID | Story | Points | MoSCoW | Kano | Acceptance criteria (abbreviated) | Traces to |
| --- | --- | --- | --- | --- | --- | --- |
| US-01 | As a prospective learner, I want to search and filter courses without logging in, so that I can evaluate options before committing | 8 | Must | Basic | Guest reaches a target course in 3 interactions; filters on title, category, date, location | REQ-009 |
| US-02 | As a learner, I want to register for a course on a single form, so that I can finish quickly on my phone | 13 | Must | Basic | Maximum 12 fields; completes in under 4 min in usability test | REQ-010 |
| US-03 | As a learner, I want pages to load quickly on mobile data, so that I do not give up mid-registration | 21 | Must | Basic | 95th percentile under 2.0s on 4G; holds at 400 concurrent | REQ-022, REQ-023 |
| US-04 | As a learner using a screen reader, I want all pages to meet WCAG 2.1 AA, so that I can register independently | 13 | Must | Basic | Zero level A or AA failures on scan and manual audit | REQ-025 |
| US-05 | As a learner, I want to resume an interrupted registration, so that I do not lose my progress | 8 | Should | Excitement | Resumable from the same step within 7 days | REQ-011 |
| US-06 | As a learner, I want an immediate booking confirmation, so that I know my place is secured | 21 | Must | Basic | 95th percentile delivery under 60 seconds over 100 test bookings | REQ-012 |
| US-07 | As a learner, I want a reminder 48 hours before my course, so that I do not miss it | 13 | Must | Basic | Dispatched between 47 and 49 hours before start | REQ-013 |
| US-08 | As a learner, I want automatic notice when I reschedule or cancel, so that I have a record of the change | 8 | Must | Basic | Notice within 60 seconds of either event | REQ-014 |
| US-09 | As a learner, I want to reschedule my booking myself, so that I do not have to phone during office hours | 13 | Must | Excitement | Unaided reschedule completed in usability test | REQ-016 |
| US-10 | As a learner, I want to cancel my booking myself and get my refund, so that I am not dependent on support | 21 | Must | Excitement | Cancellation and refund initiated within policy window | REQ-017 |
| US-11 | As a learner, I want to pay by card or PayNow, so that I can use my preferred method | 8 | Must | Basic | Both methods succeed end to end against v2 sandbox and production | REQ-020 |
| US-12 | As a learner, I want to see all my bookings on one page, so that I can manage my schedule | 13 | Must | Performance | All past and upcoming bookings with correct status | REQ-015 |
| US-13 | As the DPO, I want explicit consent captured with the purpose stated, so that data collection has a lawful basis | 21 | Must | Basic | Consent record with timestamp, version and purpose; DPO accepts | REQ-018, C-01, C-02 |
| US-14 | As a funding administrator, I want NRIC-linked attendance in the SSG claim format, so that claims process without rework | 13 | Must | Basic | Generated claim file validates against SSG spec with no manual edit | REQ-019, C-06 |
| US-15 | As the DPO, I want every access to personal data logged, so that we can demonstrate accountability | 8 | Must | Basic | Audit entry for 100% of access events in scripted test | REQ-021, C-09 |
| US-16 | As the DPO, I want learner data encrypted at rest and in transit, so that a breach does not expose personal data | 21 | Must | Basic | Pen test confirms TLS 1.2+ and encryption at rest | REQ-026, C-04 |
| US-17 | As an administrator, I want to create and edit communication templates myself, so that I am not waiting on developers | 13 | Should | Performance | Admin creates, previews and publishes a template unaided | REQ-006 |
| US-18 | As a learner, I want richer course search filters, so that I can narrow a long list quickly | 34 | Should | Performance | Filters on price, level, format, trainer added to the base four | REQ-009 extension |
| US-19 | As a learner, I want my existing bookings to still be there after the upgrade, so that I lose nothing in the move | 21 | Must | Basic | Reconciliation report shows zero variance; exceptions explained | REQ-027, REQ-008 |
| US-20 | As an IT operations engineer, I want runbooks, monitoring and alerting, so that I can support the service after handover | 13 | Should | Indifferent (to learners) | IT Ops signs the supportability checklist at G3 | REQ-007 |
| US-21 | As the QA lead, I want an automated regression suite in CI, so that we catch breakage before learners do | 21 | Should | Basic (indirectly) | Suite runs on every build; covers US-01 to US-12 paths | REQ-030 |
| US-22 | As an administrator, I want the three staff trained and a rehearsed rollback, so that cutover is survivable | 34 | Should | Indifferent | All three pass competency check; rollback rehearsed within window | REQ-028, REQ-029 |
| US-23 | As a learner, I want to download my attendance record instantly, so that I can claim my own funding without emailing admin | 21 | Could | Excitement | Record downloads as PDF within 5 seconds | REQ-019 extension |
| US-24 | As a learner, I want to save my payment method, so that repeat registration is faster | 21 | Could | Excitement | Tokenised method stored per PDPA consent; reusable at checkout | New |

```text
BACKLOG TOTALS - verify these yourself

  Must    US-01,02,03,04,06,07,08,09,10,11,12,13,14,15,16,19
          8+13+21+13+21+13+8+13+21+8+13+21+13+8+21+21   =  202 points
  Should  US-05,17,18,20,21,22
          8+13+34+13+21+34                              =  123 points
  Could   US-23,24
          21+21                                          =   42 points
  Won't   AI recommender (55), native apps, CMS replacement, bulk-booking
          portal, trainer scheduling  - NOT counted in the backlog total

  BACKLOG TOTAL                                          =  367 points

  Add the two remaining Coulds carried from the Lab 09 register that have
  not yet been written as stories - waitlist for full courses (13) and
  saved search alerts (21):                              =  401 points

  Must share = 202 / 401 = 50.4%   PASSES the 60% discipline rule.
```

### Step 5 - Estimate with story points, not hours

```text
RELATIVE SIZING vs ABSOLUTE TIME - why points and not days

  A story point expresses SIZE relative to other stories, combining
  complexity, effort and uncertainty into one number. It is deliberately
  not a time unit.

  Why relative beats absolute:
    - People are demonstrably bad at absolute estimation and reliably
      good at comparison. "Is this bigger than that?" is a question
      humans answer well.
    - Points are person-independent. A senior and a junior developer
      disagree about how many DAYS a story takes; they agree it is
      twice the size of the reference story.
    - Points do not decay. A day estimate assumes a specific person at a
      specific time. A size estimate survives reassignment.
    - Velocity converts points to time empirically, from observed data,
      rather than from optimism.

  MODIFIED FIBONACCI  1, 2, 3, 5, 8, 13, 21, 34
    The gaps widen deliberately. Precision is impossible at scale, and the
    scale refuses to let you pretend otherwise. You cannot estimate 17,
    because you cannot tell 17 from 18. Anything estimated 34 or above is
    an EPIC and must be split before it enters a sprint.

  PLANNING POKER
    1. Product owner reads the story and answers questions.
    2. Every estimator privately selects a card.
    3. All reveal SIMULTANEOUSLY - this is the whole mechanism. It
       prevents anchoring on the first or the loudest number.
    4. Highest and lowest estimators explain their reasoning. The value is
       in this discussion, not in the number - divergence almost always
       means the story is understood differently by different people.
    5. Re-estimate. Repeat until convergence. Two rounds usually suffice.

  REFERENCE STORY ANCHORING
    Choose one small, well-understood, already-completed story and fix it
    as the anchor. Everything is estimated against it.
```

```text
CONTOSO REFERENCE STORY - fix this before estimating anything else

  US-11  "Pay by card or PayNow"  =  8 POINTS

  Why this one is the anchor:
    - The team has built payment integrations before, so it is understood.
    - It has real complexity (two methods, external API, error paths) but
      no research uncertainty.
    - It is mid-scale, so stories can be compared upward and downward.

  Calibration from the anchor:
    US-15 audit logging      = 8   "about the same size as payment"
    US-02 registration form  = 13  "clearly bigger, not twice as big"
    US-03 performance work   = 21  "much bigger - performance work is
                                    open-ended until measured"
    US-01 guest search       = 8   "same as the anchor"
    US-18 richer filters     = 34  "an epic - must be split before sprint"

  Note US-18 and US-22 both sit at 34. Both are flagged for splitting at
  the sprint planning where they are pulled in. A 34 is not an estimate;
  it is a statement that the story is not yet ready.
```

**INVEST criteria** - the test of a well-formed story:

| Letter | Criterion | What it prevents | Contoso check |
| --- | --- | --- | --- |
| **I** | Independent | Stories that cannot be reordered or dropped | US-23 can ship without US-24. US-13 must precede US-14 - a known and accepted dependency |
| **N** | Negotiable | A story written as a specification, killing collaboration | US-09 states the need, not the screen layout |
| **V** | Valuable | Technical tasks masquerading as stories | Every story has a "so that" clause naming a benefit |
| **E** | Estimable | Stories the team cannot size because they are not understood | US-03 needed a spike before it could be sized at 21 |
| **S** | Small | Stories that cannot finish inside a sprint | US-18 and US-22 at 34 points must be split |
| **T** | Testable | Stories with no acceptance criteria | Every story above carries acceptance criteria from the Lab 09 register |

**Definition of Ready** - a story may not enter a sprint until all of these are true:

```text
DEFINITION OF READY

  [ ] Written in the As a / I want / So that form with a real benefit
  [ ] Acceptance criteria written and agreed with the product owner
  [ ] Estimated by the team at 21 points or fewer
  [ ] Dependencies identified and either resolved or scheduled earlier
  [ ] UX design available where the story is learner-facing
  [ ] Compliance implications assessed with the DPO where personal
      data is touched - this row exists because of Lab 03's lesson that
      compliance discovered late is compliance discovered expensively
  [ ] Test approach agreed with the QA lead
  [ ] No blocking open question remains

  A story failing any line stays in the backlog. Pulling unready stories
  into a sprint is the most common cause of sprints that finish with
  everything "nearly done" - which, in points delivered, is zero.
```

### Step 6 - Build the release plan against real capacity

```text
CAPACITY ARITHMETIC

  Team capacity per sprint         34 story points  (Lab 06 CON-4)
  Sprint length                     2 weeks
  Number of sprints                12
  TOTAL CAPACITY        34 x 12  = 408 story points

  BACKLOG TOTAL                   = 401 story points

  SLACK                408 - 401 =   7 story points  =  1.7% of capacity

  This is genuinely tight and you should say so out loud. Seven points of
  slack across six months is not a buffer; it is a rounding error. The plan
  works only because 42 points sit in Coulds that can be dropped without
  breaking the product. The real buffer is not the 7 points - it is the
  Could column. That is precisely what the MoSCoW discipline rule was
  protecting, and it is why a 90%-Must backlog would have been undeliverable
  at exactly the same total size.
```

Create `artifacts/10-release-plan.md`. Sequence by dependency and by gate obligation, not by preference.

| Sprint | Weeks | Stories | Points | Cumulative | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | 1-2 | US-01 (8), US-11 (8), spike on gateway v2 and performance (16) | 32 | 32 | Spikes de-risk A-03 and size US-03. Gate G1 design work runs alongside |
| 2 | 3-4 | US-02 (13), US-13 (21) | 34 | 66 | Consent built WITH the registration form, not after it. Privacy by design, per the Lab 07 DPO action |
| 3 | 5-6 | US-06 (21), US-15 (8) | 29 | 95 | **G1 design gate, week 6.** First usability test with real learners (A-01) |
| 4 | 7-8 | US-03 (21), US-08 (8) | 29 | 124 | Performance work early, because it is open-ended and the 21 could grow |
| 5 | 9-10 | US-07 (13), US-12 (13), US-05 (8) | 34 | 158 | First Should (US-05) enters once Musts are tracking ahead |
| 6 | 11-12 | US-09 (13), US-04 (13), US-14 (13) | 39 | 197 | Over nominal capacity - see the note below |
| 7 | 13-14 | US-10 (21), US-16 (21) | 42 | 239 | Over nominal capacity - see the note below |
| 8 | 15-16 | US-19 (21), US-17 (13) | 34 | 273 | Migration built early enough to rehearse, per REQ-029 |
| 9 | 17-18 | US-21 (21), US-20 (13) | 34 | 307 | **G2 build complete, week 18.** All Musts must be done by here |
| 10 | 19-20 | US-22 (34) split into two | 34 | 341 | Training and rollback rehearsal. Compliance review begins |
| 11 | 21-22 | US-18 (34) split into two | 34 | 375 | Compliance review completes week 22 (M6). UAT follows, never in parallel |
| 12 | 23-24 | US-23 (21), waitlist (13) | 34 | 409 | **G3 pre-launch, week 24.** US-24 and saved search alerts drop to phase 2 |

```text
TWO THINGS TO FIX IN THE PLAN ABOVE - and this is the exercise

  Sprints 6 and 7 are loaded at 39 and 42 points against a 34-point
  capacity. That is not a plan, it is a wish. Real capacity does not
  increase because the schedule needs it to. Rebalance:

    Move US-14 (13) from sprint 6 to sprint 8.
      Sprint 6 becomes 26 points.  Sprint 8 becomes 47 - still wrong.
    Better: move US-14 (13) to sprint 5's place by moving US-05 (8, a
      Should) out of sprint 5 and into sprint 12.
      Sprint 5 = 13+13+13 = 39. Still wrong.

  Work it properly and you will find the only solution that holds every
  sprint at or under 34 requires dropping a COULD. That is the correct
  outcome and it is the point of the exercise: the plan is capacity-bound,
  the arithmetic proves it, and the Could column is where the adjustment
  comes from. Produce a rebalanced 12-sprint table in which NO sprint
  exceeds 34 points, and name which Coulds you dropped.

PROVING THE MUSTS FIT BEFORE G2

  Gate G2 (build complete) is week 18 = end of sprint 9.
  Capacity available to end of sprint 9  =  34 x 9  =  306 points
  Total Must-have effort                              =  202 points

  Headroom  =  306 - 202  =  104 points

  All 16 Must-have stories fit inside the first nine sprints with 104
  points to spare - which is where the Shoulds are drawn from. This is the
  single most important number in the release plan and it is the one the
  sponsor should be shown: the mandatory scope is not merely planned, it is
  proven to fit, with 34% headroom against the gate.
```

### Step 7 - Make the AI recommender trade-off numeric

Lab 07 identified misalignment M-1 and committed you to converting an argument about importance into a concrete trade-off. Here is the arithmetic that session needs.

```text
THE AI RECOMMENDER TRADE-OFF - the numbers for the M-1 session

  AI recommender estimated effort                     55 story points
  Team capacity per sprint                            34 story points
  Sprints required             55 / 34  =            1.62 sprints
                                                   = 3.2 weeks of the
                                                     entire team's output

  Total capacity                                     408 points
  Committed backlog                                  401 points
  Available slack                                      7 points

  To deliver 55 points, 48 points must come from somewhere. There are
  exactly three sources, and no fourth:

  OPTION 1 - DROP COULDS
    All Coulds                                        42 points
    Still short by                                     6 points
    VERDICT: dropping every Could in the plan does NOT free enough
    capacity. This alone answers the question.

  OPTION 2 - DROP SHOULDS
    Drop US-18 richer filters (34) + US-17 templates (13) = 47 points
    Plus all Coulds (42) = 89 points freed, 55 used.
    CONSEQUENCE: administrators keep waiting on developers for template
    changes, so benefit B2 (SGD 25,536/yr of released admin time) is
    partially forfeited to gain an INDIFFERENT feature (Kano K-13).
    VERDICT: trades a quantified benefit for an unquantified one.

  OPTION 3 - DROP A MUST
    Not available. Every Must is legally required, contractually required,
    or the product is not viable without it. Dropping US-04 (WCAG) breaches
    C-11. Dropping US-13 (consent) breaches PDPA. There is no Must whose
    removal is lawful and viable.

  OPTION 4 - MOVE THE DATE
    CON-1: launch 30 June is immovable, tied to the July intake.
    1.62 sprints = 3.2 weeks past the fixed date.

  THE QUESTION FOR THE M-1 SESSION, stated as Lab 07 required:
    "Delivering the AI recommender means giving up either the administrator
     template editing and the enriched search - forfeiting part of the
     SGD 25,536 annual admin saving - or moving the launch 3.2 weeks past
     the July intake. Which of those two does the group prefer?"

  Supporting evidence to bring:
    Lab 02 scored scan       AI 16  vs  mobile 25
    Lab 10 Kano evidence     AI recommender classifies as INDIFFERENT
    Charter exclusion        OUT-1 with documented rationale
    This arithmetic          55 points, 1.62 sprints, 7 points of slack

  Note the shape of the argument. Nobody is asked whether AI is important.
  They are asked to choose between two named, priced losses. That is a
  question a COO can answer in a meeting; "is AI important" is not.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
At the prioritisation workshop, the stakeholder group classifies 88% of the
backlog effort as Must-have. The sponsor supports this, saying "we need all
of it". What should the project manager do?

  A. Accept the prioritisation; the stakeholders own the priorities.
  B. Explain that a backlog at 88% Must has no flexibility, and re-run the
     Must test on each item - legally required, contractually required, or
     product not viable - so that the label reflects obligation rather than
     desire, and show the sponsor what the plan looks like with no buffer.
  C. Reduce the Musts arbitrarily to 60% to satisfy the rule.
  D. Extend the schedule so 88% Musts become deliverable.

SCENARIO 2
A feature is classified as an Excitement attribute on Kano and a Could on
MoSCoW. A team member argues the classification is inconsistent and one of
them must be wrong. How do you respond?

  A. Agree; reclassify it as a Should to resolve the inconsistency.
  B. There is no inconsistency. Kano measures customer satisfaction, MoSCoW
     measures delivery obligation. A delighter's absence causes no
     dissatisfaction by definition, which makes Could the correct and
     deliberate priority - and makes it the best candidate to pull in if
     capacity appears.
  C. Kano takes precedence; promote it to Must.
  D. MoSCoW takes precedence; remove the Kano classification.

SCENARIO 3
Halfway through the project, velocity has averaged 29 points per sprint
rather than the planned 34. Six sprints remain. What does this mean for the
release, and what is the correct response?

  A. Ask the team to work overtime to recover the shortfall.
  B. Add two developers to raise capacity.
  C. Compute the revised forecast, confirm whether the Must-haves still fit,
     and if they do, drop Coulds and then Shoulds to bring the committed
     scope inside the revised capacity - reporting the reduced scope to the
     sponsor rather than the reduced date.
  D. Report that the launch date is at risk and request an extension.
```

Answer key:

```text
SCENARIO 1 -> B.  The MoSCoW discipline rule exists because a plan with no
            Coulds has no shock absorber, and the first risk event then
            forces a date conversation. But the fix is not to impose a
            number - it is to re-apply the definition, because 88% Must
            almost always means the group has been labelling importance
            rather than obligation. Re-running the three-part test does the
            work honestly. A abdicates a professional responsibility: the
            stakeholders own priority, the PM owns the integrity of the
            method. C is the trap answer - hitting 60% by arbitrary
            reclassification produces a number that satisfies the rule and
            a plan that still fails, because the labels no longer mean
            anything. D treats a fixed constraint (CON-1) as negotiable.

SCENARIO 2 -> B.  The two models measure different things and are supposed
            to disagree. Kano asks what customers will notice; MoSCoW asks
            what the release cannot ship without. A delighter is precisely
            the right thing to place in the flexible part of the plan: no
            dissatisfaction if dropped, disproportionate satisfaction per
            point if delivered. A, C and D all destroy information by
            forcing one model to override the other, and C specifically
            would promote a non-essential feature into the mandatory
            envelope, which is how Must-have inflation begins.

SCENARIO 3 -> C.  Velocity is empirical data, not a target to be argued
            with. Revised forecast: 29 x 6 = 174 points remaining capacity
            against a plan built on 34 x 6 = 204, a shortfall of 30 points.
            Check the Musts first - if they still fit, the release is safe
            and the adjustment comes from Coulds (42 points available),
            which more than covers the 30-point gap without touching a
            single Should. Scope flexes, the date does not: that is exactly
            what CON-1 and the Lab 06 hybrid decision committed to. A
            attacks the symptom and degrades quality and velocity further.
            B is Brooks's law - adding people to a late project makes it
            later, and Lab 06 CON-4 forbids extra headcount anyway. D
            reports the wrong variable; the date is the fixed constraint
            and scope is the flexible one.
```

## Deliverable

Submit to `artifacts/`:

- `10-moscow.md` - every requirement classified, with the three-part Must test shown for each Must, and the effort split arithmetic proving Musts are at or under 60%.
- `10-kano.md` - at least 14 features classified across all five Kano categories, including at least one Reverse and one Indifferent, with the time-decay reasoning stated for at least one feature.
- The MoSCoW-versus-Kano conflict table with a resolution for each conflict and the four rules that fall out of it.
- `10-product-backlog.md` - at least 24 user stories in As a / I want / So that form, each with points from the modified Fibonacci scale, MoSCoW priority, Kano class, acceptance criteria and a trace to a Lab 09 requirement.
- The reference story identified with its point value and the calibration of at least four other stories against it.
- The INVEST assessment and the Definition of Ready.
- `10-release-plan.md` - a rebalanced 12-sprint plan in which no sprint exceeds 34 points, with the dropped Coulds named, and the proof that all Must-have effort fits before gate G2.
- The AI recommender trade-off arithmetic with all four options costed.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every Must in your backlog passes at least one leg of the three-part test, and you can say which leg. "The sponsor wants it" appears nowhere as a justification.
- Your Must effort share is at or below 60% and you computed it rather than assumed it.
- Your Kano classification includes at least one Reverse feature, and the backlog item arising from it is a removal rather than an addition.
- You identified at least one genuine disagreement between MoSCoW and Kano and explained why it is productive rather than an error.
- Every story has a "so that" clause naming a real benefit. A story whose benefit clause is "so that the system works" has no value statement.
- No story larger than 21 points is scheduled into a sprint without being split first.
- Your rebalanced release plan has no sprint above 34 points. If any sprint exceeds capacity, the plan is arithmetic fiction.
- You proved the Must-haves fit before G2 with a number - capacity to sprint 9 versus Must effort - not with an assurance.
- Your AI recommender analysis shows that dropping every Could is still insufficient, and states the trade-off as a choice between two named losses.
