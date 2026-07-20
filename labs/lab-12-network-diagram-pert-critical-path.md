# Lab 12 - Network Diagram, PERT and the Critical Path

| Field | Value |
| --- | --- |
| Topic | 3 - Plan the Project |
| ECO 2026 task | Process T8 - Plan and manage schedule |
| Duration | 60 minutes |
| Consumes | Lab 11 WBS and work packages; Lab 03 lessons learned (compliance review must precede UAT) |
| Produces | `artifacts/12-activity-list.md`, `artifacts/12-network-diagram.md`, `artifacts/12-critical-path.md`, `artifacts/12-schedule-baseline.md` |

## Objectives

- Derive an activity list from the WBS work packages, converting deliverables into the activities that produce them.
- Sequence activities using the four dependency types and distinguish mandatory from discretionary logic.
- Compute a forward pass and a backward pass by hand and identify the critical path with total and free float.
- Apply both three-point estimating formulas and compute project-level confidence ranges from variance.
- Compare crashing and fast-tracking, and select the cheapest compression that actually shortens the project.
- Apply the Lab 03 lesson by sequencing compliance review ahead of UAT, and quantify what running them in parallel would cost.

## The definitions the exam builds every schedule question on

```text
CRITICAL PATH
  The LONGEST path through the network. It has ZERO total float. It
  determines the SHORTEST POSSIBLE project duration.
  All four statements describe the same thing, and the exam will phrase the
  question using any one of them.

  Longest path = shortest possible duration is not a contradiction. The
  project cannot finish before its longest chain of dependent work
  finishes; every other path has slack to spare.

  A network may have MORE THAN ONE critical path. More critical paths means
  more risk, because more activities have zero tolerance for delay.

FLOAT (SLACK)
  TOTAL FLOAT   How long an activity can be delayed without delaying the
                PROJECT FINISH.        TF = LS - ES  =  LF - EF
  FREE FLOAT    How long an activity can be delayed without delaying the
                EARLY START of any SUCCESSOR.
                FF = (earliest ES of successors) - EF
  Free float is always less than or equal to total float. An activity can
  have total float but zero free float - delaying it eats someone else's
  slack, not the project's.

  NEGATIVE FLOAT means the schedule is already infeasible against an
  imposed date. It is not a scheduling curiosity; it is a signal that the
  constraint and the plan disagree.

NEAR-CRITICAL PATHS
  Paths with small float. A path with 2 days of float is not safe - a
  three-day slip makes it critical and the critical path moves. Monitor
  near-critical paths; the critical path is dynamic, not a fixed property
  of the plan.

FORWARD PASS   Left to right. Computes ES and EF. Take the MAXIMUM EF of
               predecessors as the ES of the successor.
               EF = ES + Duration
BACKWARD PASS  Right to left. Computes LS and LF. Take the MINIMUM LS of
               successors as the LF of the predecessor.
               LS = LF - Duration
```

## Steps

### Step 1 - Derive the activity list from the WBS

Lab 11 produced deliverables. A schedule needs activities - the verbs that produce those nouns. This is the conversion the WBS deliberately did not do.

Create `artifacts/12-activity-list.md`. Durations are in working days.

| ID | Activity | WBS source | Duration (d) | Predecessors | Owner |
| --- | --- | --- | --- | --- | --- |
| A | Elicit and baseline requirements | 1.2.1 | 10 | - | BA |
| B | Produce UX design and design system | 1.2.2 | 15 | A | UX designer |
| C | Profile legacy data and define cleansing rules | 1.7.1 | 12 | A | DevOps |
| D | Build responsive registration flow | 1.3.2 | 20 | B | Dev lead |
| E | Build course search and selection | 1.3.1 | 18 | B | Dev lead |
| F | Build migration scripts and mapping | 1.7.2 | 14 | C | DevOps |
| G | Build notification engine and templates | 1.4.1 | 16 | D | Dev lead |
| H | Build accessibility conformance | 1.3.3 | 10 | E | UX + Dev |
| I | Rehearse migration and reconcile | 1.7.3 | 8 | F | DevOps |
| J | Build self-service and payment integration | 1.5.1, 1.6.1 | 12 | G, H | Dev lead |
| K | Build performance and load test assets | 1.9.2 | 9 | I | QA lead |
| L | Build PDPA consent, audit logging and encryption | 1.8.1, 1.8.3 | 15 | J, K | Dev + BA |
| M | Execute automated regression suite | 1.9.1 | 10 | L | QA lead |
| N | Compliance review and penetration test | 1.8.4, 1.8.5 | 12 | M | DPO + vendor |
| O | Execute user acceptance testing | 1.9.3 | 8 | N | BA + admin staff |
| P | Cutover, go-live and hypercare | 1.11.3 | 5 | O | DevOps |

Note that every activity begins with a verb and every WBS source is a noun. That is the correct relationship between the two artifacts.

### Step 2 - Understand the dependencies you have just declared

```text
DEPENDENCY TYPES - the four relationships

  FS  FINISH-TO-START   Predecessor must FINISH before successor STARTS.
                        By far the most common; every dependency in the
                        Contoso network above is FS.
                        "Regression testing (M) starts after consent build
                         (L) finishes."
  SS  START-TO-START    Predecessor must START before successor STARTS.
                        "Compliance evidence assembly starts 3 days after
                         the compliance review starts" - they run together.
  FF  FINISH-TO-FINISH  Predecessor must FINISH before successor FINISHES.
                        "Migration reconciliation cannot finish before the
                         migration run finishes."
  SF  START-TO-FINISH   Predecessor must START before successor FINISHES.
                        RARE. Almost always a handover or shutdown case:
                        "The legacy portal cannot be shut down until the
                         new portal has started serving traffic."
                        If SF appears as an exam option it is usually the
                        distractor - but know it is real, not a trick.

DEPENDENCY SOURCES - who imposed the logic, which decides whether you can
change it

  MANDATORY (hard logic)     Inherent in the nature of the work or legally
                             required. You cannot choose otherwise.
                             "Consent capture (L) must be built before it
                              can be tested (M)." Physically necessary.
                             "Compliance review (N) before UAT (O)."
                             Contractually and procedurally required.
  DISCRETIONARY (soft logic) Chosen for preference, best practice or risk
                             reduction. CAN be changed - and discretionary
                             dependencies are the FIRST place to look when
                             fast-tracking, because they are the only
                             dependencies you are permitted to break.
                             "E (search) after B (design)" is partly
                             discretionary - search could begin from
                             wireframes before the full design system.
  EXTERNAL                   Outside the project team's control.
                             "Penetration test (N) depends on the external
                              security vendor's availability."
  INTERNAL                   Within the project team's control.

LEADS AND LAGS - both are modifiers on a dependency, and the sign is what
the exam checks

  LEAD  ACCELERATES the successor. Negative time. Overlap.
        "H can start 3 days before E finishes"  =  FS-3d lead.
        Leads create overlap and therefore create RISK - if E's last three
        days change the design, H reworks.
  LAG   DELAYS the successor. Positive time. Waiting.
        "O starts 5 days after N finishes"  =  FS+5d lag, to allow the
        DPO's mandated response window for findings.
        A lag is elapsed time in which NO WORK OCCURS. If work occurs, it
        is an activity and should be modelled as one - hiding work inside
        a lag is a common and damaging modelling error.

  WORKED EXAMPLES ON THE CONTOSO NETWORK
    N -> O with FS+5d lag:  N finishes day 110. With a 5-day lag for the
      DPO findings response window, O starts day 115 rather than day 110,
      and the project finishes 5 days later at day 128. The base network
      below assumes no lag; add it in Step 8 and observe the effect.
    E -> H with FS-3d lead:  H starts 3 days before E completes.
      H's ES moves from 43 to 40. Because H already has 8 days of float,
      this lead buys nothing at all - it shortens a non-critical path.
      This is the single most common compression error: applying leads and
      crashing to activities that are not on the critical path.
```

### Step 3 - Draw the network diagram

Create `artifacts/12-network-diagram.md`. This is an activity-on-node diagram: activities are boxes, arrows are dependencies.

```text
ACTIVITY-ON-NODE NETWORK - Contoso Training Portal Upgrade

                            +--------+        +--------+
                       +--->|   D    |------->|   G    |----+
                       |    | 20 d   |        | 16 d   |    |
                       |    +--------+        +--------+    |
                       |                                    v
          +--------+   |                              +----------+
     +--->|   B    |---+                              |    J     |
     |    | 15 d   |   |    +--------+   +--------+   |  12 d    |
     |    +--------+   +--->|   E    |-->|   H    |-->|          |
     |                      | 18 d   |   | 10 d   |   +----------+
+--------+                  +--------+   +--------+         |
|   A    |                                                  v
| 10 d   |                                            +----------+
+--------+                  +--------+   +--------+   |    L     |
     |                      |   F    |   |   I    |   |  15 d    |
     |    +--------+        | 14 d   |   |  8 d   |   +----------+
     +--->|   C    |------->|        |-->|        |         |
          | 12 d   |        +--------+   +--------+         |
          +--------+                          |             |
                                              v             |
                                        +----------+        |
                                        |    K     |--------+
                                        |   9 d    |
                                        +----------+
                                                            |
                                                            v
     +--------+     +--------+     +--------+     +--------+
     |   M    |---->|   N    |---->|   O    |---->|   P    |
     | 10 d   |     | 12 d   |     |  8 d   |     |  5 d   |
     +--------+     +--------+     +--------+     +--------+
     regression     compliance       UAT          cutover
       suite        + pen test                    + go-live

     L feeds M.  The tail M -> N -> O -> P is a single mandatory chain.

THE THREE PATHS THROUGH THE NETWORK

  Path 1:  A-B-D-G-J-L-M-N-O-P
           10+15+20+16+12+15+10+12+8+5   =  123 days
  Path 2:  A-B-E-H-J-L-M-N-O-P
           10+15+18+10+12+15+10+12+8+5   =  115 days
  Path 3:  A-C-F-I-K-L-M-N-O-P
           10+12+14+8+9+15+10+12+8+5     =  103 days

  LONGEST PATH = Path 1 at 123 days = THE CRITICAL PATH.
  Path 2 float = 123 - 115 =  8 days.
  Path 3 float = 123 - 103 = 20 days.
```

### Step 4 - Compute the forward and backward pass

Do this by hand before reading the table. The method:

```text
FORWARD PASS  (compute ES and EF, left to right)
  ES of an activity with no predecessor = 0.
  ES = MAXIMUM of the EF values of all its predecessors.
  EF = ES + Duration.

  Worked, for the first few:
    A:  ES = 0,                     EF = 0 + 10  = 10
    B:  ES = EF(A) = 10,            EF = 10 + 15 = 25
    C:  ES = EF(A) = 10,            EF = 10 + 12 = 22
    D:  ES = EF(B) = 25,            EF = 25 + 20 = 45
    E:  ES = EF(B) = 25,            EF = 25 + 18 = 43
    G:  ES = EF(D) = 45,            EF = 45 + 16 = 61
    H:  ES = EF(E) = 43,            EF = 43 + 10 = 53
    J:  ES = MAX(EF(G)=61, EF(H)=53) = 61,  EF = 61 + 12 = 73
        ^^ this is the step candidates get wrong. MAXIMUM, not the most
           recent, not the average.
    L:  ES = MAX(EF(J)=73, EF(K)=53) = 73,  EF = 73 + 15 = 88

  PROJECT DURATION = maximum EF across all activities = EF(P) = 123 days.

BACKWARD PASS (compute LF and LS, right to left)
  LF of an activity with no successor = project duration = 123.
  LF = MINIMUM of the LS values of all its successors.
  LS = LF - Duration.

  Worked, for the last few and one branch point:
    P:  LF = 123,                   LS = 123 - 5  = 118
    O:  LF = LS(P) = 118,           LS = 118 - 8  = 110
    N:  LF = LS(O) = 110,           LS = 110 - 12 =  98
    M:  LF = LS(N) =  98,           LS =  98 - 10 =  88
    L:  LF = LS(M) =  88,           LS =  88 - 15 =  73
    J:  LF = LS(L) =  73,           LS =  73 - 12 =  61
    K:  LF = LS(L) =  73,           LS =  73 -  9 =  64
    B:  LF = MIN(LS(D)=25, LS(E)=33) = 25,  LS = 25 - 15 = 10
        ^^ MINIMUM here, mirroring the maximum on the forward pass.
```

Full computed schedule. Verify every row against your own working.

| Activity | Dur | Preds | ES | EF | LS | LF | Total float | Free float | Critical? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 10 | - | 0 | 10 | 0 | 10 | 0 | 0 | **Yes** |
| B | 15 | A | 10 | 25 | 10 | 25 | 0 | 0 | **Yes** |
| C | 12 | A | 10 | 22 | 30 | 42 | 20 | 0 | No |
| D | 20 | B | 25 | 45 | 25 | 45 | 0 | 0 | **Yes** |
| E | 18 | B | 25 | 43 | 33 | 51 | 8 | 0 | No |
| F | 14 | C | 22 | 36 | 42 | 56 | 20 | 0 | No |
| G | 16 | D | 45 | 61 | 45 | 61 | 0 | 0 | **Yes** |
| H | 10 | E | 43 | 53 | 51 | 61 | 8 | 8 | No |
| I | 8 | F | 36 | 44 | 56 | 64 | 20 | 0 | No |
| J | 12 | G, H | 61 | 73 | 61 | 73 | 0 | 0 | **Yes** |
| K | 9 | I | 44 | 53 | 64 | 73 | 20 | 20 | No |
| L | 15 | J, K | 73 | 88 | 73 | 88 | 0 | 0 | **Yes** |
| M | 10 | L | 88 | 98 | 88 | 98 | 0 | 0 | **Yes** |
| N | 12 | M | 98 | 110 | 98 | 110 | 0 | 0 | **Yes** |
| O | 8 | N | 110 | 118 | 110 | 118 | 0 | 0 | **Yes** |
| P | 5 | O | 118 | 123 | 118 | 123 | 0 | 0 | **Yes** |

```text
RESULT

  CRITICAL PATH   A - B - D - G - J - L - M - N - O - P
  DURATION        123 working days
  Every activity on it has total float = 0.

  NEAR-CRITICAL   Path 2 (A-B-E-H-J-...) has only 8 days of float. An
                  8-day slip on E or H makes a SECOND critical path. This
                  path must be monitored, not ignored - E is an 18-day
                  build activity and 8 days is less than half its duration.

  COMFORTABLE     Path 3 (A-C-F-I-K-...) has 20 days of float.

TOTAL FLOAT vs FREE FLOAT - read the difference off the table

  C, F and I each have 20 days of TOTAL float but ZERO FREE float.
  Meaning: C can slip 20 days without delaying the project, but it cannot
  slip even one day without pushing F's early start. The 20 days of slack
  belongs to the PATH, not to C individually. Consume it at C and F, I and
  K have none left.

  K has 20 days of total float AND 20 days of free float, because its only
  successor L has an ES of 73 driven by J, not by K. K can slip 20 days
  and affect nobody.

  H has 8 days of both. Its successor J starts at 61 driven by G.

  This distinction is directly tested. Total float is about the project;
  free float is about your immediate successor.
```

### Step 5 - Apply three-point estimating and compute confidence ranges

Single-point estimates hide uncertainty. Three-point estimating exposes it.

```text
THE TWO FORMULAS - know both, and know which is which

  TRIANGULAR (simple average)      tE = (O + M + P) / 3
      Weights all three equally. Use when you have little confidence in
      the most likely estimate, or when historical data is thin.

  BETA / PERT (weighted average)   tE = (O + 4M + P) / 6
      Weights the most likely estimate four times. Use when the most
      likely value is genuinely the best information you have. This is
      the one the exam means by "PERT" unless it says otherwise.

  STANDARD DEVIATION               SD = (P - O) / 6
  VARIANCE                         V  = ((P - O) / 6)^2  =  SD^2

  Why /6: the beta distribution assumption places O and P roughly three
  standard deviations either side of the mean, giving a range of 6 SD.

  CRITICAL RULE FOR PROJECT-LEVEL UNCERTAINTY:
    You may NOT add standard deviations. You add VARIANCES, then take the
    square root of the total.
      Project SD = SQRT( sum of variances of activities ON THE CRITICAL PATH )
    Adding SDs directly overstates uncertainty substantially, and it is a
    deliberate exam distractor.
```

| Activity | O | M | P | Triangular (O+M+P)/3 | Beta/PERT (O+4M+P)/6 | SD (P-O)/6 | Variance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 6 | 10 | 14 | 10.00 | 10.00 | 1.333 | 1.778 |
| B | 11 | 15 | 19 | 15.00 | 15.00 | 1.333 | 1.778 |
| C | 8 | 12 | 16 | 12.00 | 12.00 | 1.333 | 1.778 |
| D | 14 | 20 | 26 | 20.00 | 20.00 | 2.000 | 4.000 |
| E | 12 | 18 | 24 | 18.00 | 18.00 | 2.000 | 4.000 |
| G | 10 | 16 | 22 | 16.00 | 16.00 | 2.000 | 4.000 |
| L | 9 | 15 | 21 | 15.00 | 15.00 | 2.000 | 4.000 |
| N | 8 | 12 | 16 | 12.00 | 12.00 | 1.333 | 1.778 |

```text
NOTE ON THIS TABLE: every estimate here is SYMMETRIC (P - M = M - O), which
is why triangular and beta/PERT give identical answers. That is convenient
for checking your arithmetic but it is NOT typical. Real estimates skew
right - the worst case is further from the most likely than the best case
is, because there are more ways for work to go wrong than to go right.

  Test yourself on a SKEWED example, activity D revised:
    O = 14, M = 20, P = 38
    Triangular  = (14 + 20 + 38) / 3   = 72 / 3   = 24.00 days
    Beta/PERT   = (14 + 80 + 38) / 6   = 132 / 6  = 22.00 days
    SD          = (38 - 14) / 6        = 4.00 days
  The triangular estimate is 2 days HIGHER because it gives the pessimistic
  tail equal weight. When estimates are skewed, the two formulas diverge,
  and knowing which was used matters.
```

Now compute project-level confidence. Use the critical path activities only.

```text
CRITICAL PATH VARIANCE - A, B, D, G, J, L, M, N, O, P

  Activity   O    M    P    tE      Variance ((P-O)/6)^2
     A       6   10   14   10.00      1.778
     B      11   15   19   15.00      1.778
     D      14   20   26   20.00      4.000
     G      10   16   22   16.00      4.000
     J       8   12   16   12.00      1.778
     L       9   15   21   15.00      4.000
     M       6   10   14   10.00      1.778
     N       8   12   16   12.00      1.778
     O       5    8   11    8.00      1.000
     P       3    5    7    5.00      0.444
                        --------    --------
   EXPECTED DURATION     123.00 d    22.334  total variance

  PROJECT STANDARD DEVIATION = SQRT(22.334) = 4.726 days

  Sanity check: the PERT expected duration of 123.00 days matches the CPM
  duration of 123 days computed in Step 4. It should, because every
  activity's beta estimate equals the duration used in the network.

  CONFIDENCE RANGES - memorise these three percentages

    1 sigma = 68.27%   123 +/- 4.73    =  118.3  to  127.7 days
    2 sigma = 95.45%   123 +/- 9.45    =  113.5  to  132.5 days
    3 sigma = 99.73%   123 +/- 14.18   =  108.8  to  137.2 days

  STATED AS THE EXAM STATES IT:
    "There is a 95.45% probability that the project will complete between
     113.5 and 132.5 working days."

    And the one-sided version, which is what sponsors actually ask:
    "There is a 50% probability of finishing at or before 123 days, and
     approximately an 84% probability of finishing at or before 127.7 days
     (the mean plus one sigma - half of the 31.73% that falls outside one
     sigma lies above it, so 68.27% + 15.87% = 84.14%)."

  WHY THE SPONSOR NEEDS THIS. A single-point answer of "123 days" implies
  a certainty that does not exist. The honest statement is that 123 days
  is a coin flip, and committing to a date needs the plus-one-sigma figure
  of about 128 days, or explicit compression. The Lab 06 charter fixed
  30 June, so the gap between 123 and the available working days is the
  real schedule reserve - and it is smaller than it looks.

  COMMON ERROR: computing variance for ALL activities rather than only
  those on the critical path. Including E, H, C, F, I and K would inflate
  the total variance to about 37 and the SD to 6.1 days, overstating
  uncertainty by roughly 30%. Non-critical activities have float; their
  variability is absorbed before it reaches the project finish.
```

### Step 6 - Compress the schedule

```text
CRASHING
  Add RESOURCES to shorten duration. Overtime, extra staff, faster
  equipment, paid expediting.
    INCREASES COST. Always.
    Does NOT increase risk of rework in the way fast-tracking does.
    WORKS ONLY ON THE CRITICAL PATH. Crashing a non-critical activity
      spends money and shortens nothing. This is the most tested point.
    CHOOSE THE LOWEST COST-PER-DAY-SAVED FIRST.
    Subject to diminishing returns - Brooks's law means adding people to
      a late software task can make it later.

FAST-TRACKING
  Perform in PARALLEL activities that were planned in sequence, or overlap
  them with leads.
    Usually costs nothing directly.
    INCREASES RISK and the likelihood of REWORK, because a successor
      starts before its predecessor's output is final.
    ONLY works on DISCRETIONARY dependencies. You cannot fast-track a
      mandatory dependency - you cannot test code that does not exist,
      and you cannot run UAT before compliance clearance at Contoso.
    Also only meaningful on the critical path.

  Order of preference: fast-track first if safe discretionary dependencies
  exist, because it is free; crash where they do not, because it is
  certain. Neither is free of consequence, and both need the sponsor
  informed.
```

Crash cost table. All four activities below are on the critical path.

| Activity | Normal dur | Crash dur | Max days saved | Normal cost (SGD) | Crash cost (SGD) | Added cost | Cost per day saved |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D Registration flow | 20 | 17 | 3 | 43,400 | 62,000 | 18,600 | **6,200** |
| G Notification engine | 16 | 14 | 2 | 32,240 | 41,240 | 9,000 | **4,500** |
| L Consent and logging | 15 | 12 | 3 | 23,560 | 46,960 | 23,400 | **7,800** |
| N Compliance and pen test | 12 | 10 | 2 | 28,000 | 35,600 | 7,600 | **3,800** |

```text
EXERCISE: the sponsor needs 3 days. Buy them at minimum cost.

  Rank by cost per day saved, cheapest first:
     N  3,800/day  (up to 2 days available)
     G  4,500/day  (up to 2 days available)
     D  6,200/day  (up to 3 days available)
     L  7,800/day  (up to 3 days available)

  Buy the cheapest days in order:
     N, 2 days  @ 3,800  =   7,600
     G, 1 day   @ 4,500  =   4,500
                           --------
     3 days saved for      SGD 12,100

  New duration: 123 - 3 = 120 days.

  THE WRONG ANSWERS AND WHY

    Crashing L for 3 days costs 23,400 - nearly double, for the same 3
    days. Choosing the activity with the largest available saving rather
    than the cheapest per day is the classic error.

    Crashing E (search build, 18 days) would cost money and save NOTHING,
    because E has 8 days of float and is not on the critical path. It
    would shorten path 2 from 115 days to something shorter, while the
    project still finishes in 123. Crashing off the critical path is pure
    waste, and every exam set contains a version of this distractor.

  THE CHECK AFTER EVERY COMPRESSION - do not skip this:
    Recompute the network. Path 2 had only 8 days of float. We removed 3
    days from the critical path, so path 2's float falls from 8 to 5 days.
    Remove 8 days and path 2 becomes critical too, and further crashing of
    path 1 alone stops shortening the project. THE CRITICAL PATH MOVES
    WHEN YOU COMPRESS IT. Crash three days, recompute, then decide the
    next three.
```

### Step 7 - Apply the Lab 03 lesson: compliance before UAT

The Lab 03 lessons-learned register recorded that on the previous release, compliance review was run concurrently with user acceptance testing to save time, and the findings forced rework of screens that had already been accepted by users. The lesson: **compliance review must complete before UAT begins.**

That lesson is why activity N precedes activity O as a mandatory dependency in this network. Quantify what the alternative looks like.

```text
SCENARIO: run N (compliance, 12 d) and O (UAT, 8 d) IN PARALLEL

  Both would start after M (regression) finishes at day 98.
    N: 98 -> 110
    O: 98 -> 106
    The tail becomes MAX(110, 106) + 5 (cutover P) = 115 days.

  APPARENT SAVING: 123 - 115 = 8 days. This is what gets proposed in the
  meeting, and it is arithmetically correct.

  WHAT THE LESSON SAYS ACTUALLY HAPPENS:
    Compliance findings arrive on day 110, after UAT concluded on day 106.
    On the previous release, findings required changes to consent screens
    and data handling that users had already signed off. The consequences,
    from the Lab 03 record:
      - Rework of the affected screens                     6 days
      - RE-RUN of UAT on the changed screens               8 days
      - Re-review by the DPO of the changed screens        4 days
                                                        --------
      Additional elapsed time on the critical path       18 days

    Realistic outcome: 115 + 18 = 133 days, against 123 days for the
    sequential plan. Fast-tracking this dependency LOSES 10 days.

  WHY THIS IS THE TRAP, stated generally:
    Fast-tracking only works on DISCRETIONARY dependencies. N -> O is
    MANDATORY at Contoso for two independent reasons:
      1. Procedurally: the DPO owns the G3 gate and UAT sign-off is part
         of the evidence pack. Accepting a product that has not cleared
         compliance produces evidence that contradicts itself.
      2. Practically: asking users to accept screens that compliance may
         require you to change wastes their time and destroys the value of
         their sign-off.
    A dependency does not become discretionary because the schedule is
    tight. The pressure to reclassify it is exactly the pressure the
    lessons-learned register exists to resist.

  THE CORRECT RESPONSE if 8 days are genuinely needed: crash, per Step 6.
  N itself is the cheapest activity to crash at 3,800 per day - shortening
  the compliance review by adding a second reviewer is legitimate, whereas
  removing the dependency is not.
```

### Step 8 - Build the schedule baseline

Create `artifacts/12-schedule-baseline.md`.

| Component | Content |
| --- | --- |
| Activity list | The 16 activities with WBS traces, durations and owners |
| Network diagram | Activity-on-node with all three paths identified |
| Forward and backward pass | ES, EF, LS, LF, total float and free float for every activity |
| Critical path | A-B-D-G-J-L-M-N-O-P, 123 working days, zero float |
| Near-critical paths | Path 2 at 8 days float - flagged for monitoring |
| Duration confidence | PERT expected 123 days, SD 4.73 days, 95.45% range 113.5 to 132.5 days |
| Milestones | M1 to M10 from the Lab 06 charter, mapped to activity finishes |
| Assumptions | Working days only; team of 9 available throughout (A-02); external pen test vendor available in the N window |
| Schedule reserve | Held at project level, not distributed into activity durations |

```text
SCHEDULE BASELINE vs SCHEDULE

  The SCHEDULE BASELINE is the approved version of the schedule model. It
  changes only through formal change control.
  The SCHEDULE is the current working plan, updated continuously.
  Variance between them is what Lab 20 measures as SV and SPI.

  Padding individual activity durations to feel safe is the wrong way to
  hold reserve: the padding is invisible, it gets consumed silently by
  Parkinson's law, and it destroys the ability to measure variance.
  Hold reserve visibly at project level where it can be managed and
  reported.

FORWARD REFERENCE TO LAB 20
  In Lab 20 you will have actual earned value data - SPI, CPI, SV, CV -
  and you will decide whether to crash or fast-track using those figures
  rather than a hypothetical. The crash cost table built here is the input
  to that decision. The difference is that in Lab 20 you will know how
  much of the 123 days you have already consumed and how much value you
  have actually earned, which converts the choice from an estimate into a
  measurement.
```

### Step 9 - Answer the exam-style scenarios

```text
SCENARIO 1
Using the Contoso network, activity E (build course search, 18 days) is
running 6 days late. What is the effect on the project finish date, and
what should the project manager do?

  A. The project finishes 6 days late; escalate to the sponsor.
  B. E has 8 days of total float, so 6 days of delay does not move the
     project finish. But float falls from 8 to 2 days, making path 2
     near-critical, so E and H move onto the monitoring list and no
     further slippage is tolerable without action.
  C. Crash E to recover the 6 days.
  D. No action; E is not on the critical path.

SCENARIO 2
The sponsor asks you to shorten the project by 3 days at minimum cost,
using the crash table. Which combination is correct?

  A. Crash L by 3 days for SGD 23,400.
  B. Crash D by 3 days for SGD 18,600.
  C. Crash N by 2 days and G by 1 day for SGD 12,100.
  D. Crash E by 3 days, since it has the most available slack.

SCENARIO 3
A project has an expected duration of 123 days with a standard deviation of
4.73 days on the critical path. The sponsor asks for a date she can commit
to publicly with high confidence. Which statement is correct?

  A. 123 days, because that is the expected duration.
  B. 118 days, because that is one standard deviation below the mean.
  C. Approximately 132.5 days gives about 97.7% confidence of finishing at
     or before that date, being two standard deviations above the mean;
     123 days carries only about 50% confidence.
  D. 137 days, because three sigma covers 99.73% of outcomes.
```

Answer key:

```text
SCENARIO 1 -> B.  Float is consumed, not lost. Six days of delay against 8
            days of total float leaves 2 days and does not move the
            project finish - so A is wrong and escalating a date threat
            that does not exist damages your credibility. But D is also
            wrong, and this is the real teaching point: "not on the
            critical path" is not the same as "no action required". A path
            with 2 days of float is near-critical, and the critical path
            moves the moment that float is exhausted. The correct action
            is to monitor, not to escalate and not to ignore. C spends
            money to protect float the project does not need.

SCENARIO 2 -> C.  Rank by cost per day saved and buy the cheapest days
            first: N at 3,800 for 2 days (7,600), then G at 4,500 for 1
            day (4,500), totalling SGD 12,100. A costs 23,400 for the
            same result - it selects the activity with the largest total
            saving available rather than the cheapest rate, which is the
            standard trap. B costs 18,600. D is the more serious error:
            E is not on the critical path, so crashing it shortens the
            project by exactly zero days at full cost. Note also that
            after buying these 3 days you must recompute the network,
            because path 2's float drops from 8 days to 5.

SCENARIO 3 -> C.  The expected duration is the 50th percentile - a coin
            flip - so A commits the sponsor to a date she will miss half
            the time. B is worse: one sigma BELOW the mean is roughly 16%
            confidence. Two sigma above the mean gives about 97.7% on a
            one-sided basis (the 95.45% two-sided range leaves 4.55%
            outside, half of it above, so 95.45% + 2.275% = 97.7%). D is
            not wrong statistically but it is poor practice - a date at
            three sigma is so padded that it will be beaten by two weeks,
            which destroys the credibility of every future estimate you
            produce. The professional answer gives the sponsor the
            confidence level attached to each date and lets her choose the
            level of risk she wishes to publish.
```

## Deliverable

Submit to `artifacts/`:

- `12-activity-list.md` - at least 14 activities with IDs, WBS traces, durations, predecessors and owners, each expressed as a verb phrase.
- `12-network-diagram.md` - the activity-on-node diagram with all paths identified and their lengths computed.
- `12-critical-path.md` - the full forward and backward pass table with ES, EF, LS, LF, total float, free float and the critical flag for every activity; the critical path named with its duration; near-critical paths identified with their float.
- The three-point estimating table with both triangular and beta/PERT computed, standard deviations and variances, and at least one skewed example showing the two formulas diverging.
- The project-level standard deviation computed from critical path variances only, with the 1, 2 and 3 sigma confidence ranges stated in words.
- The crash analysis with cost per day saved for at least four activities and the cheapest three-day compression selected and justified.
- The compliance-before-UAT analysis with the parallel-running duration computed and the realistic rework outcome quantified.
- `12-schedule-baseline.md` - all components listed in Step 8.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your critical path is A-B-D-G-J-L-M-N-O-P at 123 days, and every activity on it has zero total float.
- Your forward pass took the MAXIMUM predecessor EF at activity J and your backward pass took the MINIMUM successor LS at activity B. Getting either backwards produces a plausible-looking but wrong schedule.
- Total float equals LS minus ES and also equals LF minus EF for every activity. If the two differ on any row, that row is wrong.
- You identified that C, F and I have 20 days of total float but zero free float, and can explain why.
- You computed project standard deviation from the critical path variances only, and you added variances rather than standard deviations.
- Your 95.45% range is roughly 113.5 to 132.5 days, and you stated it as a probability sentence rather than a number.
- Your crash selection is N plus G at SGD 12,100, chosen by cost per day saved rather than by total days available.
- You stated that crashing activity E would shorten the project by zero days, and why.
- You can explain why the compliance-to-UAT dependency is mandatory rather than discretionary, and quantify what running them in parallel would actually cost.
- You recomputed the network after compressing it, and noted that path 2's float fell from 8 days to 5.
