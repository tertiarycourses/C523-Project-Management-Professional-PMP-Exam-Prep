# Lab 04 - Compliance, Sustainability and AI-Governance Register

| Field | Value |
| --- | --- |
| Topic | 1 - Business Environment |
| ECO 2026 task | Business Env T2 - Plan and manage project compliance; Process T7 - Plan and optimize quality (regulatory compliance, sustainability) |
| WSQ learning outcome | LO4 - Analyze program risks and engage stakeholders through scheduled touchpoints |
| Duration | 75 minutes |
| Consumes | Lab 02 PESTLE factors L1, L2, En1, T1; Lab 03 EEF list and escalation thresholds |
| Produces | `artifacts/04-compliance-register.md`, `artifacts/04-sustainability-plan.md`, `artifacts/04-ai-governance.md` |

## Objectives

- Classify Contoso's compliance requirements into categories and identify the threats to each.
- Quantify the consequences of noncompliance so compliance work can be prioritised against other work.
- Define how compliance will be *measured*, not merely asserted.
- Build a sustainability section covering the group net-zero obligation.
- Build an AI-governance register - new territory the July 2026 ECO now expects you to handle.

## Why the ECO singles compliance out

Business Env T2 has seven enablers, more than most tasks. It expects you to confirm requirements, classify them, find threats to them, support them, analyse the consequences of failure, decide actions, and *measure* the extent of compliance. Notice that last one - the exam frequently offers "we complied" as a distractor against "here is our compliance evidence and its measurement".

## Steps

### Step 1 - Confirm the compliance requirements

Create `artifacts/04-compliance-register.md`. Categorise every requirement. The ECO names four categories explicitly: security, health and safety, sustainability, and regulatory.

| ID | Requirement | Category | Source | Mandatory? | Verification evidence |
| --- | --- | --- | --- | --- | --- |
| C-01 | PDPA consent capture before collecting learner personal data | Regulatory | Personal Data Protection Act 2012 | Yes | Consent audit log; DPO sign-off |
| C-02 | PDPA - purpose limitation; data used only for stated purpose | Regulatory | PDPA | Yes | Data flow map; processing register |
| C-03 | PDPA - learner right to access and correct their data | Regulatory | PDPA | Yes | Working self-service data request feature |
| C-04 | SSG funding claims require NRIC-linked attendance records | Regulatory | SSG funding terms | Yes | Sample claim file passing SSG validation |
| C-05 | 7-year retention of funding-related learner records | Regulatory | SSG funding terms | Yes | Retention policy + automated archival test |
| C-06 | NRIC data masked in all non-production environments | Security | PDPA + internal policy | Yes | Masking script output; pen-test report |
| C-07 | Encryption of personal data at rest and in transit | Security | Internal IT security standard | Yes | TLS config; DB encryption attestation |
| C-08 | Role-based access control on learner records | Security | Internal IT security standard | Yes | Access matrix; quarterly access review |
| C-09 | Payment handling PCI-DSS scope minimised via hosted gateway | Security | PCI-DSS | Yes | Gateway integration design; SAQ-A completion |
| C-10 | WCAG 2.1 AA accessibility on learner-facing pages | Regulatory / social | Group accessibility policy | Yes | Automated axe scan + manual audit |
| C-11 | Hosting carbon profile reported for procurement | Sustainability | Group net-zero-by-2035 | Yes | Vendor carbon disclosure |
| C-12 | Display of subsidy and fee information must be accurate | Regulatory | SSG / consumer protection | Yes | Fee calculation test pack |
| C-13 | Workstation ergonomics for the on-site project team | Health and safety | WSH Act | Yes | Workplace assessment record |

### Step 2 - Identify threats to compliance

For the highest-stakes requirements, name what could actually cause a failure. This is what makes the register useful rather than a checklist.

| Requirement | Threat to compliance | Likelihood | Detection method |
| --- | --- | --- | --- |
| C-01 consent capture | Developers reuse the legacy consent screen, which pre-ticks the opt-in box | High | Code review + DPO screen walkthrough |
| C-04 NRIC-linked attendance | Attendance API returns learner ID, not NRIC; mapping lost at integration | Medium | Sample SSG claim file test at G2 |
| C-05 7-year retention | Cloud storage lifecycle rule defaults to 90-day deletion | Medium | Automated archival test with a dated record |
| C-06 masking | Production data copied to the test environment for realistic UAT | High | Environment scan before each UAT cycle |
| C-10 accessibility | Accessibility treated as a Should and de-scoped under schedule pressure | High | Accessibility scan gated in the definition of done |
| C-12 fee accuracy | SSG subsidy tier changes after launch (Lab 02 factor P1) | Medium | Fee calculation regression pack; monitored |

The C-06 threat deserves attention: "copy production data to test so UAT is realistic" is a genuinely tempting shortcut that breaches PDPA. Write the control now, before someone proposes it under deadline pressure.

### Step 3 - Analyse the consequences of noncompliance

The ECO enabler is "Analyze the consequences of noncompliance". Quantify where you can, because this is how compliance work wins prioritisation arguments against feature work.

| Requirement | Consequence of failure | Financial exposure | Other consequence |
| --- | --- | --- | --- |
| C-01 to C-03 PDPA | PDPC financial penalty; breach notification obligation | Up to SGD 1,000,000 or 10% of annual turnover for larger organisations | Mandatory notification; reputational damage; learner trust |
| C-04, C-05 SSG | Funding claims rejected or clawed back | Contoso claims approx. SGD 1.2m per year - full year at risk | Loss of approved-provider status |
| C-06 to C-09 security | Data breach; regulatory investigation | Penalty plus incident response cost (prior industry cases: SGD 150k-400k) | Loss of corporate clients |
| C-10 accessibility | Complaint; exclusion of learners with disabilities | Remediation cost approx. SGD 40,000 post-launch vs approx. SGD 8,000 if built in | Group policy breach |
| C-12 fee accuracy | Incorrect charging; refunds and corrections | Refund exposure plus admin cost | Consumer complaint; regulator interest |

Put the headline comparison in one line, because it is the argument you will actually make:

```text
Total project budget                        SGD   480,000
Annual SSG funding at risk from C-04/C-05   SGD 1,200,000
Maximum PDPA penalty exposure               SGD 1,000,000

The compliance workstream protects more value than the entire project costs.
This is why it gates go-live rather than running alongside it.
```

### Step 4 - Decide the approach and actions

For each requirement, state the method that supports compliance - the ECO enabler "Use methods to support compliance".

| ID | Method | When | Owner |
| --- | --- | --- | --- |
| C-01 | Privacy-by-design workshop before consent screens are built; DPO reviews the design | Sprint 1 | BA + DPO |
| C-04, C-05 | Build a sample SSG claim file in sprint 4 and validate it against SSG's own checker before more work depends on it | Sprint 4 | BA + Dev |
| C-06 | Environment policy: production data never leaves production; synthetic data generator built as a deliverable | Sprint 2 | DevOps |
| C-07 to C-09 | Security review checkpoint in the definition of done; external pen test at G2 | Ongoing + G2 | DevOps + QA |
| C-10 | Automated axe-core scan in the CI pipeline, failing the build on AA violations; manual audit at G2 | Every build | QA Lead |
| C-11 | Request carbon disclosure in the hosting vendor evaluation | Procurement | PM |
| C-12 | Fee calculation regression test pack, run every release | Every release | QA Lead |
| All | Formal compliance gate G3 - go-live blocked until DPO clears | Week 24 | DPO |

Note that C-04 is deliberately pulled forward to sprint 4. Discovering the NRIC mapping problem in week 22 would be unrecoverable against a fixed launch date. This is the Lab 03 lessons-learned entry being applied.

### Step 5 - Define how compliance is measured

The final ECO enabler: "Measure the extent to which the project is in compliance". Define a compliance index you can actually report.

| Measure | Definition | Target | Frequency |
| --- | --- | --- | --- |
| Compliance coverage | Requirements with verification evidence attached / total requirements | 100% by G3 | Fortnightly |
| Accessibility violations | AA violations from the automated scan | 0 blocking | Every build |
| Masking conformance | Non-production environments passing the personal-data scan | 100% | Weekly |
| Open compliance findings | Major findings open from DPO review | 0 at G3 | Per review |
| Consent audit pass rate | Sampled registrations with valid consent record | 100% | Monthly post-launch |
| Retention test | Dated test records correctly retained at 7-year rule | Pass | Quarterly |

Report it as a single fraction, e.g. `Compliance coverage: 9/13 requirements evidenced (69%) at sprint 6`. That is a measurement. "Compliance is on track" is not.

### Step 6 - Build the sustainability section

Create `artifacts/04-sustainability-plan.md`. Sustainability appears in both Process T7 ("Manage cost of quality and sustainability") and Business Env T2. Cover all three dimensions, not only carbon.

| Dimension | Consideration for Contoso | Action | Measure |
| --- | --- | --- | --- |
| Environmental | Hosting carbon profile against the group net-zero-by-2035 commitment | Require carbon disclosure in vendor evaluation; prefer a region with published renewable-energy supply | kg CO2e per 1,000 registrations, reported quarterly |
| Environmental | Digital replaces paper - current process prints 14,000 confirmation letters a year | Digital confirmations by default | Sheets of paper avoided per year |
| Social | Accessibility (C-10) so learners with disabilities can self-serve | WCAG 2.1 AA gated in CI | AA violations = 0 |
| Social | The 3 admin staff whose manual work is being automated | Redeployment plan to learner support, agreed before launch, communicated at project start not at go-live | Redeployment plan signed by week 8 |
| Economic | Solution must be maintainable at Contoso's thin margin | Total cost of ownership over 5 years included in the Lab 05 business case, not just build cost | 5-year TCO documented |
| Economic | Avoid rebuild in 3 years | Build against the payment gateway v2 API; automated regression suite | Technical debt items logged and tracked |

The social row about the three admin staff matters. Automating 24 hours a week of manual work has a human consequence. A project that delivers its benefits by surprising three people with redundancy has failed on the social dimension, and the ECO's organisational-change task (Business Env T7) expects you to have planned for it.

### Step 7 - Build the AI-governance register

Contoso will not build the AI recommender in this release (Lab 02 ranked it below the mobile work), but two AI uses are already in play. The July 2026 ECO expects AI use to be governed, not assumed.

Create `artifacts/04-ai-governance.md`:

| ID | AI use | Where | Risk | Control | Human accountability |
| --- | --- | --- | --- | --- | --- |
| AI-01 | AI coding assistant used by the developers | Build | Generated code may embed licensed snippets or insecure patterns; may leak proprietary code to the vendor | No personal or production data in prompts; all generated code passes normal review and security scan; vendor account with training-opt-out | Dev lead accountable for every merged line, regardless of who or what wrote it |
| AI-02 | AI drafting of learner communication templates | Content | Inaccurate fee or subsidy information; tone mismatch; hallucinated policy | All templates reviewed and approved by Head of L&D Ops before use; fee figures never AI-generated, always system-derived | Content lead approves each template |
| AI-03 | Proposed phase-2 AI course recommender | Deferred | Recommendation bias by age, gender or nationality; opaque reasoning; PDPA profiling implications | Not in this release. If approved for phase 2: bias testing across protected attributes, learner opt-out, explainability requirement, DPO review of profiling basis | Product Owner; DPO for PDPA basis |
| AI-04 | AI-assisted test case generation | QA | False confidence - generated tests that assert nothing meaningful | QA lead reviews generated tests; mutation testing to verify tests actually detect defects | QA Lead |

Write the governing principle at the top of the file:

```text
CONTOSO AI USE PRINCIPLES - Training Portal Upgrade

1. No learner personal data is placed into any external AI tool.
2. AI output is a draft, never a decision. A named human approves.
3. Anything that affects a learner's money, eligibility or record is
   system-derived, never AI-generated.
4. Every AI use is registered here before it starts.
5. AI use does not transfer accountability. The human who ships it owns it.
```

### Step 8 - Answer the exam-style scenarios

```text
SCENARIO 1
Two weeks before UAT, the BA proposes copying a production database snapshot
into the test environment so that UAT is realistic. The QA lead supports it,
saying synthetic data has been causing false test failures. What do you do?

  A. Approve it; UAT quality is at risk and the test environment is internal.
  B. Approve it on condition the snapshot is deleted immediately after UAT.
  C. Refuse, invoke control C-06, and have DevOps fix the synthetic data
     generator; escalate the UAT quality issue as an impediment if needed.
  D. Ask the DPO whether it is acceptable and proceed on their answer.

SCENARIO 2
At sprint 6, 9 of your 13 compliance requirements have verification evidence
attached. The sponsor asks in the status meeting whether the project is
compliant. What is the BEST answer?

  A. "Yes, compliance is on track."
  B. "Compliance coverage is 9 of 13 requirements evidenced, 69%. The four
     outstanding are C-05, C-09, C-10 and C-11, all scheduled before G3."
  C. "We won't know until the compliance gate at G3."
  D. "Yes, we have a compliance register and a gate."

SCENARIO 3
A developer mentions she has been pasting snippets of the learner registration
code into a public AI assistant to debug it. Some snippets contained sample
learner records copied from a bug report. What is your FIRST action?

  A. Remove the developer from the project.
  B. Update the AI governance register to prohibit it going forward.
  C. Determine what data was exposed, notify the DPO, and assess whether
     this is a reportable PDPA incident.
  D. Ask the AI vendor to delete the data.
```

Answer key:

```text
SCENARIO 1 -> C.  C-06 exists precisely for this moment. B is still a breach -
            deletion afterwards does not undo the copy. D outsources a decision
            you have already documented; the DPO does not need to re-decide a
            settled control. C also does not ignore the real problem: the
            synthetic data generator is failing, so fix it and escalate if it
            blocks. Note the ECO framing - "determine potential threats to
            compliance" is exactly what Step 2 predicted here.

SCENARIO 2 -> B.  "Measure the extent to which the project is in compliance."
            A and D assert without evidence. C abdicates - you have a
            measurement, so use it. B gives a number, names the gaps, and states
            when they close.

SCENARIO 3 -> C.  Personal data has left the organisation. First establish the
            facts and involve the DPO, because a reportable breach has a legal
            notification clock. A punishes before understanding and loses your
            best source of information about what happened. B is necessary but
            second. D is useful but does not discharge the legal obligation.
```

## Deliverable

Submit to `artifacts/`:

- `04-compliance-register.md` - at least 13 requirements across all four ECO categories (security, health and safety, sustainability, regulatory), each with a source and named verification evidence.
- The threats-to-compliance table with a detection method per row.
- The consequences analysis with quantified financial exposure where available.
- The methods-and-actions table with owners and timing.
- The compliance measurement definitions, expressible as a single reportable fraction.
- `04-sustainability-plan.md` - environmental, social and economic dimensions with measures.
- `04-ai-governance.md` - the AI use register plus the five governing principles.
- Written answers to the three scenarios.

## Checkpoint

You did this right if:

- Your register covers all four ECO compliance categories. If every row says "regulatory", you have not classified anything.
- Every requirement names specific verification evidence - a document, a test, a scan - not "review".
- Your consequences table contains at least one number large enough to justify the compliance workstream's cost. If compliance looks cheaper to skip, your analysis is incomplete.
- Compliance is expressed as a measurable fraction, and you can state today's value.
- Your sustainability plan addresses the three admin staff. A plan covering only carbon has missed the social dimension.
- Every AI use in your register names an accountable human. If any row's accountability is "the tool", redo it.
- At least one compliance activity is deliberately pulled early in the schedule to avoid late discovery, and you can say which and why.
