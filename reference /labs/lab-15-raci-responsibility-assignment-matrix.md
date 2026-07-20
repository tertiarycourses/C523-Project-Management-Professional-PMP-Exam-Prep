# Lab 15 - RACI Responsibility Assignment Matrix and Resource Plan

| Field | Value |
| --- | --- |
| Topic | 4 - Lead the Project Team |
| ECO 2026 task | People T3 - Lead the project team ("Establish clear roles and responsibilities within the team"); Process T4 - Plan and manage resources |
| WSQ learning outcome | LO2 - Organise project resources and assign clear roles and responsibilities to deliver work packages |
| Duration | 45 minutes |
| Consumes | Lab 11 WBS work packages and WBS dictionary; Lab 08 team charter and named team members; Lab 07 stakeholder register |
| Produces | `artifacts/15-raci-matrix.md`, `artifacts/15-resource-plan.md`, `artifacts/15-raci-issues.md` |
| Live tool | [RACI Matrix](https://alfredang.github.io/raci/) |

## Objectives

- Assign R, A, C and I precisely, and defend every assignment against the one-accountable rule.
- Build a real responsibility assignment matrix from the Lab 11 WBS, using the live RACI tool.
- Audit a matrix for the five structural defects that make a RACI useless, and fix them.
- Distinguish resource levelling from resource smoothing, and state which one can move the critical path.
- Resolve a genuine over-allocation on the Contoso business analyst using both techniques.

## What R, A, C and I actually mean

Most RACI matrices fail not because people cannot spell the letters but because they treat R and A as synonyms and hand out C like confetti.

```text
R  RESPONSIBLE   Does the work. The hands on the keyboard.
                 A row may have SEVERAL Rs - work can be shared.

A  ACCOUNTABLE   Owns the outcome. Approves the work as complete.
                 Answers for it when it goes wrong. Has the authority
                 to say "this is done" or "this is not done".
                 EXACTLY ONE per row. Always. No exceptions.

C  CONSULTED     Two-way dialogue BEFORE and DURING the work. Their input
                 changes what gets built. If you would not change the work
                 because of what they say, they are not a C.

I  INFORMED      One-way notification AFTER the fact. No dialogue expected,
                 no input sought. If they push back you have mislabelled them.

THE FIVE RULES - the first is the most heavily tested item in this lab
  1. EXACTLY ONE A per row. Accountability cannot be shared. Two As means
     nobody is accountable, because each can point at the other. If you
     genuinely cannot choose, the task is really two tasks - SPLIT IT.
  2. AT LEAST ONE R per row. A row with an A and no R is a task nobody
     is doing. It will silently not happen.
  3. A and R MAY be the same person. Writing "A/R" is correct and common
     for small tasks. It is not a defect.
  4. C is expensive. Every C is a conversation that must happen before
     the work can finish. Too many Cs is the commonest cause of a slow
     decision process. Challenge every C: "would their input change it?"
  5. I is cheap but not free. Every I is a communication requirement
     that Lab 18 must schedule and someone must produce.

EXAM TRAPS
  - "Two managers are both accountable for the deliverable." That is not a
    valid RACI. The correct answer is always to establish a single
    accountable owner, not to negotiate a shared one.
  - A RACI shows WHO, not WHEN. It is not a schedule. Duration and
    sequence live in Lab 12.
  - RACI is a form of RAM (Responsibility Assignment Matrix). RAM is the
    category; RACI is the popular instance. A RAM can also be drawn at
    the summary level as a resource breakdown structure crossed with the WBS.
  - The RACI does NOT replace the WBS dictionary. The dictionary says what
    the work IS; the RACI says who does it.
```

Know the variants, and know that each one buys clarity at the price of overhead:

| Variant | Extra letters | What it adds | Worth the overhead when |
| --- | --- | --- | --- |
| RACI | - | The baseline | Default. Use this unless you have a specific reason not to |
| RASCI | S = Support | Distinguishes people who actively help the R from people merely consulted | A shared-services team (e.g. DevOps) assists many work packages without owning any |
| RACI-VS | V = Verify, S = Sign-off | Separates "checked it meets spec" from "formally accepted it" | Regulated or gated work - exactly the Contoso compliance pack, where QA verifies and the DPO signs |
| DACI | Driver, Approver, Contributor, Informed | Reframes for a DECISION rather than a task | One-off decisions such as the Lab 20 crash-versus-descope choice |
| CARS / RAPID | Various | Vendor-specific decision frameworks | Rarely worth it inside a single project |

```text
The honest guidance: a RACI that people actually read beats a RACI-VS that
sits unread in a folder. Add letters only where a real dispute exists about
who verifies versus who accepts. On Contoso there is exactly one such place -
the compliance evidence pack - and Step 4 resolves it by splitting the task
rather than by adding a column of letters everywhere else.
```

## Steps

### Step 1 - Assemble the inputs

A RACI is derived, not invented. Confirm you have each input before you draw a single letter.

| Input | Source | What it supplies |
| --- | --- | --- |
| Work packages | Lab 11 WBS, levels 2 and 3 | The ROWS. Never invent tasks here |
| Acceptance criteria per package | Lab 11 WBS dictionary | Tells you who can credibly be the A |
| Named team members and their roles | Lab 08 team charter | The COLUMNS for the delivery side |
| Decision rights and thresholds | Lab 03 governance model | Whether the A sits inside the team or above it |
| Stakeholder power and interest | Lab 07 register | Who has a legitimate claim to be C rather than I |
| Compliance ownership | Lab 04 register, 13 requirements | Why the DPO cannot be a mere C on branch 1.8 |

The twelve role columns for Contoso, drawn from the Lab 08 team charter and the Lab 07 register:

| Column | Role | Person | Source |
| --- | --- | --- | --- |
| PM | Project Manager | The learner | Lab 06 charter |
| SPON | Sponsor, COO | Priya Nathan (S-01) | Lab 07 |
| PO | Product Owner, Head of L&D Ops | Marcus Tan (S-03) | Lab 07 |
| BA | Business Analyst | 1 of the 9 | Lab 08 |
| UX | UX Designer | 1 of the 9 | Lab 08 |
| DEVL | Dev Lead | Senior of the 4 developers | Lab 08 |
| DEV | Developers (3) | The remaining developers | Lab 08 |
| QA | QA Lead | 1 of the 9 | Lab 08 |
| OPS | DevOps Engineer | 1 of the 9 | Lab 08 |
| CONT | Content Lead | 1 of the 9 | Lab 08 |
| DPO | Data Protection Officer | S-04 | Lab 07, Lab 04 |
| ITOM | IT Operations Manager | S-11 | Lab 07 |

```text
Note that the Dev Lead is counted WITHIN the four developers, not in addition
to them. The team is nine people and the RACI must not quietly create a tenth.
Check your column list against the Lab 08 headcount before proceeding - a RACI
that staffs more people than you have is the commonest way an over-allocation
gets hidden in plain sight.
```

### Step 2 - Draft the matrix (this draft contains deliberate defects)

Below is the first-draft RACI as a real project team would produce it in a 40-minute workshop. It covers 20 rows drawn from the Lab 11 WBS plus four cross-cutting process rows. **It contains five structural defects.** Do not fix them yet - Step 3 is the audit.

| # | Task (WBS ref) | PM | SPON | PO | BA | UX | DEVL | DEV | QA | OPS | CONT | DPO | ITOM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.1.1 Project management plan | A/R | C | C | C | I | C | I | I | I | I | C | I |
| 2 | 1.1.4 Gate review G1 design | R | A | C | C | C | C | I | I | I | I | C | C |
| 3 | 1.2.1 Requirements baseline and RTM | C | I | A | R | C | C | I | C | I | I | C | I |
| 4 | 1.2.2 UX research and wireframes | C | I | A | R | R | C | I | I | I | C | I | I |
| 5 | 1.2.3 Solution architecture and data model | C | I | I | R | I | A/R | C | C | C | I | C | C |
| 6 | 1.3.1 Course search and selection | I | I | A | R | C | R | R | C | I | I | I | I |
| 7 | 1.3.2 Responsive registration flow build | I | I | A | R | C | R | R | C | I | I | I | I |
| 8 | 1.3.3 Accessibility WCAG 2.1 AA conformance | I | I | A | R | R | C | R | C | I | I | I | I |
| 9 | 1.4.1 Communications engine build | I | I | A | R | I | R | R | C | C | C | I | I |
| 10 | 1.4.3 Communication content set | I | I | A | R | C | I | I | I | I | R | C | I |
| 11 | 1.6.1 Payments v2 gateway integration | I | I | C | R | I | A/R | R | C | C | I | I | C |
| 12 | 1.7.2 Data migration scripts and mapping | I | I | C | R | I | A/R | R | C | R | I | C | C |
| 13 | 1.8.4 Compliance evidence pack | A | I | C | R | I | C | I | C | I | I | A | C |
| 14 | 1.8.5 Penetration test and remediation | C | I | I | I | I | A | R | C | R | I | C | C |
| 15 | 1.9.1 Automated regression suite | I | I | I | C | I | C | R | A/R | C | I | I | I |
| 16 | 1.9.3 UAT execution | C | I | A | R | I | C | I | R | I | I | C | I |
| 17 | 1.10.1 Administrator training delivery | C | I | A | C | I | I | I | I | I | C | I | I |
| 18 | 1.11.1 Environment build and release pipeline | I | I | I | I | I | C | I | C | A/R | I | I | C |
| 19 | 1.11.3 Go-live execution and hypercare | A | C | C | I | I | R | R | R | R | I | C | R |
| 20 | Change request approval (under SGD 10,000) | A/R | I | C | C | I | C | I | C | I | I | C | I |
| 21 | Risk response implementation | A | I | C | R | I | C | I | C | C | I | C | C |
| 22 | Sprint acceptance / increment sign-off | C | I | A/R | C | C | C | I | C | I | I | I | I |
| 23 | Compliance requirement verification (13 reqs) | C | I | I | R | I | C | I | R | I | I | A | I |
| 24 | Benefits measurement post-launch (B1-B4) | R | A | R | C | I | I | I | I | I | I | I | I |

### Step 3 - Enter it in the live RACI tool

Open [RACI Matrix](https://alfredang.github.io/raci/) and build the matrix so the tool can run the structural checks for you.

```text
STEP 3A - CREATE THE ROLE COLUMNS
Enter these twelve role names, in this order, exactly:

  PM
  Sponsor (COO)
  Product Owner (Marcus Tan)
  Business Analyst
  UX Designer
  Dev Lead
  Developers
  QA Lead
  DevOps
  Content Lead
  DPO
  IT Ops Manager

STEP 3B - CREATE THE TASK ROWS
Enter these 24 task names, in this order, exactly:

  1.1.1 Project management plan
  1.1.4 Gate review G1 design
  1.2.1 Requirements baseline and RTM
  1.2.2 UX research and wireframes
  1.2.3 Solution architecture and data model
  1.3.1 Course search and selection
  1.3.2 Responsive registration flow build
  1.3.3 Accessibility WCAG 2.1 AA conformance
  1.4.1 Communications engine build
  1.4.3 Communication content set
  1.6.1 Payments v2 gateway integration
  1.7.2 Data migration scripts and mapping
  1.8.4 Compliance evidence pack
  1.8.5 Penetration test and remediation
  1.9.1 Automated regression suite
  1.9.3 UAT execution
  1.10.1 Administrator training delivery
  1.11.1 Environment build and release pipeline
  1.11.3 Go-live execution and hypercare
  Change request approval under SGD 10,000
  Risk response implementation
  Sprint acceptance and increment sign-off
  Compliance requirement verification
  Benefits measurement post-launch

STEP 3C - POPULATE THE CELLS
Set each cell from the Step 2 table. Where the draft shows "A/R", enter
A in the tool and record the R in your own notes - most RACI tools allow
one letter per cell, and A implies the authority, so A is the letter to
keep. Note in artifacts/15-raci-matrix.md every cell where you did this.

STEP 3D - RUN THE CHECKS
Ask the tool (or count by hand) for:
  - Count of A per row      -> must be exactly 1 everywhere
  - Count of R per row      -> must be at least 1 everywhere
  - Count of R per column   -> the bottleneck check
  - Count of C per row      -> the decision-speed check
  - Any column that is entirely I

Export or screenshot the result into artifacts/15-raci-matrix.md.
```

### Step 4 - Audit the matrix and find the five defects

This is the real learning in this lab. A RACI is only worth building if you then interrogate it. Run the five checks in order.

**Check 1 - rows with more than one A.**

```text
Row 13, "1.8.4 Compliance evidence pack": PM has A and DPO has A.
DEFECT 1 - TWO ACCOUNTABLE PARTIES.

Why it happened: it is a genuinely ambiguous task. The PM is accountable for
the pack existing on time for gate G3; the DPO is accountable for it being
adequate. Both claims are legitimate, which is exactly why the workshop
fudged it.

Why "we will share it" is the wrong answer: at G3, if the pack is late AND
thin, the PM says the DPO set the standard too late and the DPO says the PM
never delivered the inputs. Shared accountability produces exactly this.

THE FIX - SPLIT THE TASK. Two tasks, one A each:

  13a  1.8.4a Assemble and submit the compliance evidence pack
         A = PM      (owns delivery, completeness against the 13 Lab 04
                      requirements, and the G3 submission date)
         R = BA      (does the assembly)
         C = DPO, QA, Dev Lead
  13b  1.8.4b Assess the evidence pack and issue the G3 compliance opinion
         A = DPO     (owns the adequacy judgement and the finding)
         R = DPO     (A/R - the DPO does the assessment personally)
         C = PM, BA
         I = Sponsor, IT Ops Manager

Splitting is ALWAYS the correct resolution for a two-A row. Never resolve it
by demoting one party to C - that removes an accountability that genuinely
exists. Note that this split is the RACI-VS distinction (Verify versus
Sign-off) achieved without adding two columns to all 24 rows.
```

**Check 2 - rows with no R.**

```text
Row 17, "1.10.1 Administrator training delivery":
  PM = C, PO = A, Content Lead = C, everyone else I or blank.
DEFECT 2 - NO ONE IS RESPONSIBLE. Nobody is doing this work.

This is the most dangerous defect in the matrix because it is invisible.
There is an A, so the row looks governed. There is a C list, so it looks
consulted. But no letter R appears anywhere on the row, which means no hours
are allocated, no one's sprint contains it, and it will not happen until
somebody notices in week 25 that the three admin staff have not been trained.

Recall who these three people are: S-06, the DEPENDENT stakeholders from Lab
07, the group with a legitimate urgent claim and no power to press it. The
row with no R belongs to the stakeholders least able to complain about it.
That is not a coincidence - it is the structural reason dependent
stakeholders get under-served.

THE FIX:
  17  1.10.1 Administrator training delivery
        A = PO (Marcus Tan owns operational readiness of his own staff)
        R = Content Lead (builds and delivers the materials)
        R = BA (supplies the process content)
        C = PM, UX, Support desk lead
        I = Sponsor, IT Ops Manager
```

**Check 3 - columns overloaded with R (the resource bottleneck).**

Count the R assignments down each column of the Step 2 draft:

| Role | Rows carrying R | Count |
| --- | --- | --- |
| PM | 1, 20, 24 | 3 |
| Sponsor | - | 0 |
| Product Owner | 22, 24 | 2 |
| **BA** | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 21, 23 | **14** |
| UX | 4, 8 | 2 |
| Dev Lead | 5, 6, 7, 9, 11, 12, 19 | 7 |
| Developers | 6, 7, 8, 9, 11, 12, 14, 15, 19 | 9 |
| QA Lead | 15, 16, 19, 23 | 4 |
| DevOps | 12, 14, 18, 19 | 4 |
| Content Lead | 10 | 1 |
| DPO | - | 0 |
| IT Ops Manager | 19 | 1 |

```text
DEFECT 3 - THE BA IS RESPONSIBLE ON 14 OF 24 ROWS (58%).

Note that "Developers" is a column of THREE people, so its 9 Rs are 3 each.
The BA column is ONE person carrying 14. Adjusted per head:

  BA          14 R per person
  Dev Lead     7 R per person
  Developers   3 R per person (9 shared across 3)
  QA Lead      4 R per person

The BA carries twice the load of the next busiest individual and nearly five
times the load of an individual developer. This is a resource bottleneck: the
BA becomes the critical resource on which most work packages wait, and the
schedule in Lab 12 assumed no such queueing.

This is the same person who in Lab 16 is diagnosed as the source of the
team's storming-phase friction. The team read it as attitude. The RACI shows
it is structural: you cannot be a bottleneck on 58% of the work and remain
responsive to everyone. Fixing behaviour would have failed; fixing the load
is the intervention that works.

THE FIX - reassign five R assignments off the BA:
  Row 6  1.3.1 Course search       BA: R -> C   (Dev Lead and Devs keep R)
  Row 7  1.3.2 Registration flow   BA: R -> C   (Dev Lead and Devs keep R)
  Row 8  1.3.3 Accessibility       BA: R -> I   (UX and Devs keep R; the BA
                                                 adds nothing here)
  Row 12 1.7.2 Migration scripts   BA: R -> C   (DevOps and Devs keep R;
                                                 BA remains C for the mapping
                                                 rules, which is real input)
  Row 21 Risk response             BA: R -> C   (PM takes A/R; risk response
                                                 implementation is PM work)

  Result: BA drops from 14 R to 9 R, concentrated where BA skill is genuinely
  required - requirements, RTM, UX research support, content, payments rules,
  compliance verification, UAT and the evidence pack.

  Cross-check that no receiving column becomes the new bottleneck:
    Dev Lead stays at 7, Developers stay at 9 shared across 3 (3 each),
    PM rises from 3 to 4. No new bottleneck created. FIX ACCEPTED.
```

**Check 4 - columns that are entirely I.**

```text
Scan for any role whose column contains only I. In the corrected matrix:

  Sponsor      has A on rows 2 and 24, C on several. NOT all-I. Correct -
               the sponsor holds gate G1 accountability and owns benefits.
  IT Ops Mgr   in the DRAFT holds C on 5 rows, R on row 19, I elsewhere.
               Borderline but defensible.
  DPO          holds A on 13b and 23, C elsewhere. Correct.

DEFECT 4 - the near-miss worth stating. In the draft, the Content Lead holds
exactly ONE R (row 10) and I on almost everything else. A column that is
nearly all I asks a hard question: why is this person on the project?

The answer here is that the draft UNDER-USES the Content Lead, not that the
role is unnecessary. Rows 10, 17 and the learner launch messaging (1.10.2 -
absent from the draft entirely) are all content work. The fix in Check 2
already gives the Content Lead an R on row 17. Add 1.10.2 as row 25:

  25  1.10.2 Learner communications and launch messaging
        A = PO,  R = Content Lead,  C = PM, UX, BA, DPO,  I = Sponsor, Support

  Content Lead now holds 3 R. The role is justified.

THE RULE: a column that is entirely I means either (a) the person is a
stakeholder, not a team member, and belongs in the Lab 18 communication plan
rather than the RACI, or (b) you have failed to identify the work they are
actually doing. Decide which, in writing. Do not leave the column there
unexamined.
```

**Check 5 - too many Cs.**

Count C per row in the draft, and flag anything above four:

| Row | Task | C count | Verdict |
| --- | --- | --- | --- |
| 1 | Project management plan | 6 | Too many |
| 2 | Gate review G1 | 7 | Too many |
| 5 | Solution architecture | 5 | Acceptable - genuinely cross-cutting |
| 19 | Go-live and hypercare | 3 | Fine |
| 20 | Change request approval | 5 | Too many |

```text
DEFECT 5 - ROW 2, GATE REVIEW G1, HAS SEVEN CONSULTED PARTIES.

Apply the test: would their input change the decision? Walk the seven.

  PO         Yes - owns the product being gated.           KEEP as C.
  BA         Yes - owns the requirements baseline at G1.   KEEP as C.
  UX         Yes - the design baseline IS the G1 artifact. KEEP as C.
  Dev Lead   Yes - feasibility of the architecture.        KEEP as C.
  DPO        Yes - privacy-by-design input at G1 is the
             Lab 07 M-3 action and the Lab 03 lesson.      KEEP as C.
  IT Ops Mgr Yes - supportability review at G1 is the
             Lab 07 engagement action for S-11.            KEEP as C.
  QA Lead    Not at G1 - QA's gate is G2 build complete.   DEMOTE to I.

  Result: 6 Cs. Still high, but every one survives the test, and G1 is a
  formal gate where broad consultation is the point. Compare row 20:

ROW 20, CHANGE REQUEST APPROVAL UNDER SGD 10,000, HAS FIVE Cs.
  This is the row where too many Cs does real damage. Under the Lab 06
  charter the PM may approve these unilaterally. Five mandatory consultations
  on a sub-SGD-10,000 change converts a delegated authority into a committee,
  and the delegation exists precisely to avoid that.

  FIX: reduce to PO (C - product impact) and Dev Lead (C - technical
  impact). QA, DPO and IT Ops become I, escalating to C only when the change
  touches test scope, personal data, or production infrastructure
  respectively. Record that conditional rule in the matrix notes.

THE PRINCIPLE: consultation is not free and it is not politeness. Each C is
a scheduled conversation on the critical path of a decision. A RACI with many
Cs describes an organisation that cannot decide anything quickly, and the
RACI is where you can see that before it costs you a schedule.
```

Record all five defects in `artifacts/15-raci-issues.md` using this format:

| # | Defect | Row/Column | Why it matters | Fix applied | Downstream lab affected |
| --- | --- | --- | --- | --- | --- |
| D-1 | Two As | Row 13, compliance evidence pack | Neither party answerable at G3 | Split into 13a (A=PM) and 13b (A=DPO) | Lab 04 compliance register, Lab 23 acceptance |
| D-2 | No R | Row 17, admin training | Work silently unstaffed; hits dependent stakeholders S-06 | R = Content Lead + BA | Lab 23 transition readiness |
| D-3 | R bottleneck | BA column, 14 of 24 rows | Queueing not modelled in the Lab 12 schedule | 5 Rs reassigned; BA to 9 | Lab 12 schedule, Lab 16 storming |
| D-4 | Near all-I column | Content Lead | Role unjustified or work unidentified | Added row 25; Content Lead to 3 R | Lab 18 comms plan |
| D-5 | Too many Cs | Row 20, change approval | Delegated authority turned into a committee | Reduced 5 C to 2 C plus conditional rules | Lab 03 thresholds |

### Step 5 - Before and after, in numbers

The audit must produce a measurable change, or it was a discussion rather than an audit.

| Metric | Before | After | Target |
| --- | --- | --- | --- |
| Rows with exactly one A | 23 of 24 | 25 of 25 | All rows |
| Rows with at least one R | 23 of 24 | 25 of 25 | All rows |
| Highest individual R load | BA, 14 | BA, 9 | No individual above 10 |
| BA share of all R rows | 58% | 36% | Under 40% |
| Columns that are all I | 0 (Content Lead at 1 R, near-miss) | 0 | None |
| Rows with more than 4 C | 3 (rows 1, 2, 20) | 1 (row 2, justified) | Justified only |
| Total task rows | 24 | 25 | Traces to WBS |

```text
THE BA WORKED EXAMPLE - before and after in one line each

  BEFORE  BA is R on 1.2.1, 1.2.2, 1.2.3, 1.3.1, 1.3.2, 1.3.3, 1.4.1,
          1.4.3, 1.6.1, 1.7.2, 1.8.4, 1.9.3, risk response, compliance
          verification.  = 14 R.
          Every one of those work packages waits on one person.

  AFTER   BA is R on 1.2.1, 1.2.2, 1.2.3, 1.4.1, 1.4.3, 1.6.1, 1.8.4a,
          1.9.3, compliance verification.  = 9 R.
          BA is now C on 1.3.1, 1.3.2, 1.7.2 and risk response, and I on
          1.3.3 - still involved, no longer blocking.

  The five rows moved are precisely the ones where the BA was adding
  coordination rather than analysis. That distinction - is this person doing
  the work, or attending it - is what the R-versus-C test is for.
```

### Step 6 - Build the resource plan and histogram

Create `artifacts/15-resource-plan.md`. The RACI says who; the resource plan says how much and when.

```text
RESOURCE HISTOGRAM
  A bar chart of demand for ONE resource across TIME. Weeks along the
  bottom, hours or FTE up the side, with a horizontal line at that
  resource's AVAILABLE capacity.

  Any bar above the line is an OVER-ALLOCATION. It is not a warning; it is
  an arithmetic impossibility. The plan is asking for hours that do not
  exist, and the schedule built on it is already wrong.

  Build one histogram per scarce resource, not one for the team as a whole.
  A team-level histogram averages the bottleneck away - the BA at 140% and
  the Content Lead at 40% average to a comfortable 90% and you see nothing.
```

The Contoso BA demand profile, derived from the corrected RACI and the Lab 12 activity durations. Capacity is 40 hours per week, less 10% for standing ceremonies and administration, giving 36 usable hours.

| Week | 1.2.1 RTM | 1.2.2 UX research | 1.2.3 Architecture | 1.6.1 Payments rules | 1.8.4a Evidence | Total hrs | Capacity | Utilisation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 20 | 6 | 4 | 0 | 0 | 30 | 36 | 83% |
| 4 | 22 | 8 | 4 | 0 | 0 | 34 | 36 | 94% |
| **5** | 24 | 14 | 12 | 0 | 0 | **50** | 36 | **139%** |
| **6** | 20 | 16 | 14 | 0 | 0 | **50** | 36 | **139%** |
| **7** | 12 | 12 | 10 | 16 | 0 | **50** | 36 | **139%** |
| **8** | 8 | 10 | 8 | 22 | 2 | **50** | 36 | **139%** |
| 9 | 4 | 4 | 2 | 18 | 4 | 32 | 36 | 89% |
| 10 | 2 | 2 | 0 | 14 | 6 | 24 | 36 | 67% |

```text
BA HISTOGRAM - weeks 3 to 10, capacity line at 36 hrs

  50 |         ####  ####  ####  ####
  45 |         ####  ####  ####  ####
  40 |         ####  ####  ####  ####
  36 |--####---####--####--####--####--------------  CAPACITY 36
  30 |  ####   ####  ####  ####  ####  ####
  24 |  ####   ####  ####  ####  ####  ####  ####
  18 |  ####   ####  ####  ####  ####  ####  ####
  12 |  ####   ####  ####  ####  ####  ####  ####
   6 |  ####   ####  ####  ####  ####  ####  ####
     +--------------------------------------------
   wk   3   4    5     6     7     8    9    10
        83% 94% 139%  139%  139%  139%  89%  67%

  THE OVER-ALLOCATION
    Weeks 5-8, four consecutive weeks at 139%.
    Excess = (50 - 36) x 4 weeks = 14 x 4 = 56 hours of work with
    nowhere to go.

  THE ARITHMETIC THAT MATTERS
    Total BA demand weeks 3-10 = 30+34+50+50+50+50+32+24 = 320 hours.
    Total BA capacity weeks 3-10 = 36 x 8 = 288 hours.
    The plan needs 320 hours from a person who has 288. It is short by 32
    hours REGARDLESS of how the work is rearranged.

    This is the distinction that decides the remedy. Of the 56 excess hours
    in weeks 5-8, only 24 can be absorbed by the slack in weeks 9-10
    (4 + 12 = 16 hours) plus weeks 3-4 (6 + 2 = 8 hours). The remaining
    32 hours are a genuine capacity shortfall, not a sequencing problem.
```

### Step 7 - Level or smooth: the distinction the exam tests

```text
RESOURCE LEVELLING
  Adjust the schedule so that resource demand never exceeds available
  supply. Constraint = the RESOURCE.
  Delays activities as far as necessary, INCLUDING beyond their float.
  CAN AND OFTEN DOES change the critical path.
  CAN AND OFTEN DOES extend the project end date.
  Use when the resource limit is absolute - one BA, no budget for another.

RESOURCE SMOOTHING
  Adjust activities only WITHIN their available free and total float, to
  even out the peaks. Constraint = the SCHEDULE.
  DOES NOT delay any activity beyond its float.
  DOES NOT change the critical path.
  DOES NOT change the project end date.
  MAY FAIL to fully remove the over-allocation - and that is the trade.
  Use when the date is fixed, as it is on Contoso.

THE ONE-LINE EXAM ANSWER
  Levelling protects the RESOURCE and may cost you the DATE.
  Smoothing protects the DATE and may fail to fix the RESOURCE.

  If the question says the end date cannot move -> smoothing.
  If the question says the resource limit is hard -> levelling.
  If the question says the critical path changed after resource
  optimisation -> it was levelling. Smoothing cannot do that.
```

Now work both remedies against the real BA over-allocation.

```text
REMEDY A - RESOURCE LEVELLING

  Delay 1.2.3 solution architecture support by 2 weeks so the BA's
  architecture hours (12, 14, 10, 8 in weeks 5-8) move to weeks 7-10.

  Resulting BA profile:
    wk 5  50 - 12 = 38    (106%)  still over
    wk 6  50 - 14 = 36    (100%)  at capacity
    wk 7  50 - 10 + 12 = 52  (144%)  WORSE
    wk 8  50 -  8 + 14 = 56  (156%)  WORSE

  Levelling by a 2-week delay alone is insufficient - it moves the peak
  rather than removing it, because the underlying demand exceeds supply.
  A sufficient delay is 4 weeks, pushing architecture support to weeks 9-12.

  Resulting profile weeks 5-12 with a 4-week delay:
    wk 5  38 (106%)   wk 9  32 + 12 = 44  (122%)
    wk 6  36 (100%)   wk 10 24 + 14 = 38  (106%)
    wk 7  40 (111%)   wk 11  8 + 10 = 18  ( 50%)
    wk 8  42 (117%)   wk 12  4 +  8 = 12  ( 33%)

  Still not clean, because 320 hours will not fit in 288. To fully level,
  the BA's involvement in 1.2.3 must extend to week 13.

  THE CONSEQUENCE - and this is the point:
    1.2.3 solution architecture and data model is an INPUT to gate G1
    (design baseline, week 6). Delaying BA support on it to week 13 pushes
    the G1 design baseline package past its gate date.
    G1 slipping delays the start of 1.3.2 registration flow build, which
    Lab 12 identified as being ON THE CRITICAL PATH.
    LEVELLING HAS MOVED THE CRITICAL PATH AND THREATENS THE 30 JUNE DATE,
    which charter constraint CON-1 declares immovable.
    Levelling is therefore REJECTED on Contoso.

REMEDY B - RESOURCE SMOOTHING

  Move only within float. From Lab 12, 1.2.2 UX research support carries
  9 days of total float; 1.6.1 payments rules work carries 6 days.

  Shift 1.2.2 BA hours later within float:
    Move 6 hrs from wk 5, 8 hrs from wk 6 to weeks 9 and 10.
  Shift 1.6.1 BA hours later within float:
    Move 6 hrs from wk 7, 10 hrs from wk 8 to weeks 9 and 10.

  Resulting profile:
    wk 3  30 (83%)
    wk 4  34 (94%)
    wk 5  50 - 6  = 44   (122%)  still over
    wk 6  50 - 8  = 42   (117%)  still over
    wk 7  50 - 6  = 44   (122%)  still over
    wk 8  50 - 10 = 40   (111%)  still over
    wk 9  32 + 14 = 46   (128%)  now over
    wk 10 24 + 16 = 40   (111%)  now over

  Check the total: 30+34+44+42+44+40+46+40 = 320. Unchanged, as it must be.
  Smoothing MOVES work; it does not REDUCE it. The peak fell from 139% to
  128% and no activity exceeded its float, so the critical path and the
  30 June date are intact - but the BA is still over-allocated every week
  from 5 to 10.

  SMOOTHING DID NOT SOLVE IT, and honestly reporting that is the correct
  outcome. Smoothing is allowed to fail.

THE DECISION FOR CONTOSO
  Neither technique alone works, because the problem is a 32-hour capacity
  shortfall, not a sequencing problem. Schedule optimisation cannot create
  hours. The remedy is a combination:

    1. SMOOTH first, using the float - it is free and risks nothing.
       Peak 139% -> 128%.
    2. Then REDUCE DEMAND, using the Step 4 RACI fix - moving five R
       assignments off the BA removes approximately 40 hours of BA work
       from weeks 5-10 (1.3.1, 1.3.2, 1.3.3 and 1.7.2 support).
       320 - 40 = 280 hours against 288 capacity. It now fits.
    3. Re-run the histogram to confirm no week exceeds 36 hours.
    4. Only if steps 1-3 fail, escalate for a part-time second analyst,
       which is a cost change requiring the Lab 03 threshold route.

  Note what just happened: the RACI audit in Step 4 was not a paperwork
  exercise. Fixing the R distribution was the intervention that actually
  resolved the over-allocation, after two scheduling techniques could not.
  A resource problem is often a responsibility problem wearing a schedule
  costume.
```

### Step 8 - Connect the RACI to the communication plan

Every C and every I in the matrix is a promise to communicate. Lab 18 has to schedule and staff those promises, so count them now.

| Letter | Count in corrected matrix | What Lab 18 must provide |
| --- | --- | --- |
| C | 94 | A two-way forum: workshop, review, or working session. Each has a duration and a diary slot |
| I | 121 | A one-way artifact: status report, dashboard, release note, or distribution list entry |

```text
THE SIZING CHECK

  94 consultations across 25 tasks and a 26-week project is roughly 3.6
  consultation events per task. If each is a 45-minute session, that is
  about 70 hours of consultation time across the project - real cost that
  appears nowhere in the Lab 13 estimate unless you put it there.

  121 notifications cannot each be a bespoke email. Group them:
    - Sponsor and Finance -> the Lab 18 monthly one-pager
    - Team-wide I -> the sprint review and the fortnightly status report
    - DPO and IT Ops I -> the gate review packs at G1, G2, G3
    - Support desk and admin staff I -> the weekly session from Lab 07

  If you cannot name the channel that delivers a given I, that I is a
  fiction. Delete it or fund it. An unfunded I is how stakeholders end up
  saying "nobody told me" while your RACI claims they were informed.
```

### Step 9 - Answer the exam-style scenarios

```text
SCENARIO 1
On reviewing the RACI for the compliance evidence pack, both the project
manager and the Data Protection Officer insist they are accountable for it -
the PM for its delivery, the DPO for its adequacy. Both positions are
reasonable. What should the project manager do?

  A. Record both as Accountable and note the shared accountability in the
     matrix, since both claims are legitimate.
  B. Record the DPO as Accountable and the PM as Responsible, since the DPO
     has the regulatory authority.
  C. Split the work package into two tasks - assembly and submission, and
     assessment and opinion - each with a single accountable owner.
  D. Escalate to the sponsor to decide which of the two is accountable.

SCENARIO 2
A project manager reviews a responsibility assignment matrix and finds the
business analyst is marked Responsible on 14 of 24 work packages, while the
schedule shows no queueing delay for that resource. Which statement is the
BEST description of the problem?

  A. The business analyst is a highly capable resource and this reflects
     appropriate use of their skills.
  B. The matrix reveals a resource bottleneck that the schedule has not
     modelled, so the schedule's durations are optimistic.
  C. The matrix is fine; RACI shows responsibility, not workload, so no
     conclusion about the schedule can be drawn.
  D. The business analyst should be marked Accountable rather than
     Responsible on most of those rows.

SCENARIO 3
A project has a contractually fixed delivery date. Resource analysis shows
the lead engineer is allocated at 130% for six weeks. The project manager
rearranges activities within their available float, which lowers the peak to
118% but does not eliminate the over-allocation, and confirms the critical
path is unchanged. What has the project manager done, and what should they
do next?

  A. Resource levelling; next, accept the new end date.
  B. Resource smoothing; next, report that the over-allocation persists and
     seek a demand reduction or additional capacity.
  C. Resource levelling; next, crash the critical path.
  D. Resource smoothing; next, level the resources instead, since smoothing
     failed.
```

Answer key:

```text
SCENARIO 1 -> C.  Accountability cannot be shared, and the correct resolution
            for a genuine dual claim is always to split the task so each
            party is accountable for the part they can actually answer for.
            A is the defect itself, merely documented - two As means neither
            party is answerable, because each can point at the other when it
            fails at G3.
            B destroys a real accountability. The PM is genuinely answerable
            for the pack being delivered on time and complete against the 13
            Lab 04 requirements; demoting the PM to Responsible pretends
            otherwise, and the DPO cannot be accountable for a submission
            date they do not control.
            D escalates a decision the PM is competent to make, and the
            sponsor's answer would in any case be C.

SCENARIO 2 -> B.  A responsibility assignment matrix is one of the few
            artifacts that exposes concentration of work, and 14 of 24 rows
            on a single individual is a bottleneck. If the schedule shows no
            queueing for that resource, the schedule assumed the BA could do
            all of it in parallel, which is arithmetically false - so the
            durations are optimistic and the plan is already wrong.
            A confuses capability with capacity. A capable person still has
            36 usable hours a week.
            C states a half-truth to reach a wrong conclusion. RACI does not
            show hours, but 58% of all Responsible assignments on one head is
            evidence enough to require a resource histogram - which on
            Contoso showed 139% utilisation for four consecutive weeks.
            D would make it worse: it removes the doing from the person who
            is doing it, and creates 14 rows with an A and no R - the Check 2
            defect.

SCENARIO 3 -> B.  Working within float, with the critical path unchanged, is
            the definition of resource SMOOTHING. The two identifying
            features are both stated in the question.
            Smoothing is permitted to fail, and it did. The correct next step
            is honest reporting plus an attack on the demand side - reduce
            scope of that engineer's assignments, reassign work, or add
            capacity - not further schedule manipulation, which cannot create
            hours.
            A and C misname the technique: levelling would have moved
            activities beyond their float and could have changed the critical
            path, which the question explicitly rules out.
            D is the trap. Levelling would indeed remove the over-allocation,
            but it does so by delaying activities beyond their float, which
            on a contractually fixed date is not available. Choosing
            levelling here trades a contract breach for a resource
            spreadsheet that balances.
```

## Deliverable

Submit to `artifacts/`:

- `15-raci-matrix.md` - the corrected 25-row by 12-column matrix, with every row tracing to a Lab 11 WBS code or a named cross-cutting process, plus your export or screenshot from the [RACI Matrix](https://alfredang.github.io/raci/) tool.
- The row-level counts of A, R and C, and the column-level counts of R, proving each rule is satisfied.
- `15-raci-issues.md` - the five defects in the defect table format, each with the row or column, why it matters, the fix applied, and the downstream lab affected.
- The before-and-after metric table showing the BA falling from 14 R to 9 R and every row holding exactly one A.
- `15-resource-plan.md` - the BA resource histogram for weeks 3 to 10 with the 36-hour capacity line, the utilisation percentages, and the total-demand-versus-total-capacity arithmetic.
- Both remedies worked: the levelling option with its critical-path consequence and the reason it is rejected, and the smoothing option with its residual over-allocation honestly stated.
- The combined recommendation and the demonstration that the RACI fix, not the scheduling technique, is what closes the gap.
- The C and I counts, with the Lab 18 channel named for each grouping.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Every one of your 25 rows has exactly one A and at least one R. Count them; do not assume.
- You resolved the two-A defect on the compliance evidence pack by SPLITTING the task, not by demoting the DPO or the PM to C.
- You found the row with no R, and you can say why that row belonged to the dependent stakeholders from Lab 07 rather than to anyone powerful.
- Your R-per-column count identified the BA at 14 of 24 rows, and you connected that to the Lab 16 storming diagnosis as a structural cause rather than a behavioural one.
- You challenged every C with the question "would their input change the work?" and you demoted at least one C to I with a stated reason.
- Your resource histogram has an explicit capacity line and you stated the total demand (320 hours) against total capacity (288 hours) before choosing a remedy.
- You can state, without looking it up, that levelling can change the critical path and extend the end date while smoothing works within float and cannot.
- You rejected levelling for Contoso on the specific ground that it pushes the G1 design baseline and therefore the critical path past the immovable 30 June date in constraint CON-1.
- You reported that smoothing reduced the peak from 139% to 128% but did NOT eliminate the over-allocation, rather than presenting smoothing as a solution.
- You recognised that a 320-hour demand against 288 hours of capacity cannot be solved by rearranging the schedule, and that the demand reduction came from the RACI audit.
- Every C and I in your matrix has a named Lab 18 channel. If you cannot name the channel, you have deleted the letter rather than left it as a fiction.
