#!/usr/bin/env python3
"""
Generate the WSQ Learner Guide as BOTH:
  * a Word document (.docx) in house format, and
  * an aligned Markdown mirror (LEARNER-GUIDE.md)

from one source, so the two can never diverge.

Content is derived from course_data.py (topics + ECO map), labs_index.py
(the 24 labs) and the slide content modules, so the Learner Guide stays
aligned with the deck, the Lesson Plan and the labs.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SKILL = os.path.join(REPO, ".claude/skills/tertiary-lesson-plan")
sys.path.insert(0, HERE)
sys.path.insert(0, SKILL)

import prodoc  # noqa: E402
import course_data as cd  # noqa: E402
from labs_index import LABS, BY_TOPIC, filename  # noqa: E402

from docx import Document  # noqa: E402
from docx.shared import Pt, RGBColor  # noqa: E402
from docx.enum.text import WD_BREAK  # noqa: E402
from docx.enum.table import WD_TABLE_ALIGNMENT  # noqa: E402

BRAND = RGBColor(0x1F, 0x6F, 0xEB)
DARK = RGBColor(0x16, 0x1B, 0x26)
GREY = RGBColor(0x5B, 0x63, 0x72)
HEADER_FILL = "1F6FEB"
TOPIC_FILL = "E8F0FE"
LAB_FILL = "E8F8F1"

# Read from the single source so the record can never drift from the cover.
VERSIONS = [(v, d, summary, author) for v, d, summary, author in cd.VERSION_HISTORY]

md = []          # markdown mirror accumulator


def _logo(name):
    for p in (os.path.join(REPO, "courseware/assets", name),
              os.path.join(SKILL, "assets", name),
              os.path.join(REPO, ".claude/skills/tertiary-course-slides/assets", name)):
        if os.path.exists(p):
            return p
    return None


def _shade(cell, hexc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hexc)
    cell._tc.get_or_add_tcPr().append(el)


def _cell(cell, text, size=9.5, bold=False, color=DARK, fill=None):
    cell.text = ""
    r = cell.paragraphs[0].add_run(str(text))
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.name = "Arial"
    r.font.color.rgb = color
    if fill:
        _shade(cell, fill)


def h1(doc, text, mdlevel="#"):
    doc.add_heading(text, level=1)
    md.append(f"\n{mdlevel} {text}\n")


def h2(doc, text):
    doc.add_heading(text, level=2)
    md.append(f"\n## {text}\n")


def h3(doc, text):
    doc.add_heading(text, level=3)
    md.append(f"\n### {text}\n")


def para(doc, text, size=11, bold=False, color=DARK, after=6, md_out=True):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.name = "Arial"
    r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(after)
    if md_out:
        md.append(f"**{text}**\n" if bold else f"{text}\n")
    return p


def bullet(doc, text, size=11, md_out=True):
    p = doc.add_paragraph(style="List Bullet")
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.name = "Arial"
    if md_out:
        md.append(f"- {text}")
    return p


def numbered(doc, text, size=11):
    p = doc.add_paragraph(style="List Number")
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.name = "Arial"
    return p


def table(doc, headers, rows, widths=None, md_out=True):
    t = doc.add_table(rows=0, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.add_row().cells
    for i, htxt in enumerate(headers):
        _cell(hdr[i], htxt, 9.5, bold=True,
              color=RGBColor(0xFF, 0xFF, 0xFF), fill=HEADER_FILL)
    for row in rows:
        c = t.add_row().cells
        for i, v in enumerate(row):
            _cell(c[i], v, 9, bold=(i == 0),
                  color=DARK if i == 0 else GREY,
                  fill=TOPIC_FILL if i == 0 else None)
    if md_out:
        md.append("")
        md.append("| " + " | ".join(headers) + " |")
        md.append("| " + " | ".join("---" for _ in headers) + " |")
        for row in rows:
            md.append("| " + " | ".join(str(v).replace("\n", " ")
                                        for v in row) + " |")
        md.append("")
    return t


# ------------------------------------------------------------ topic bodies
# Detailed teaching notes per topic. These expand the slide content into
# prose the learner can study from after the class.
TOPIC_NOTES = {
1: [
 ("What a project is, and why that definition matters",
  "A project is a temporary endeavour undertaken to create a unique product, "
  "service or result. Two words carry the weight. *Temporary* means it has a "
  "definite beginning and end — it is not the ongoing operation that follows. "
  "*Unique* means the deliverable differs in some material way from what came "
  "before; if you are producing the same thing repeatedly, that is operations, "
  "not a project. The exam tests this boundary constantly: maintaining a "
  "running payroll system is operations, replacing it is a project.",
  ["Temporary — a defined start and finish, not perpetual",
   "Unique — the output differs materially from previous outputs",
   "Progressive elaboration — detail increases as the project advances",
   "Delivers business value, which is the reason it was funded at all"]),
 ("The triple constraint and why quality sits in the middle",
  "Scope, time and cost form the classic triangle, with quality dependent on "
  "all three. Change any one and at least one other must move, or quality "
  "absorbs the damage. In practice this is the single most useful conversation "
  "tool a project manager has: when a stakeholder asks for more scope at a "
  "fixed date and budget, the triangle is what you draw. Modern practice "
  "extends this to six constraints — scope, schedule, cost, quality, resources "
  "and risk.",
  ["Increase scope with fixed time and cost, and quality falls",
   "Compress schedule, and cost rises (crashing) or risk rises (fast tracking)",
   "Cut budget, and either scope or quality must give",
   "Never silently absorb a change — make the trade-off explicit and documented"]),
 ("Development approaches across the value delivery spectrum",
  "Predictive (waterfall) approaches plan scope thoroughly up front and control "
  "change formally; they suit stable requirements and high-compliance "
  "environments. Adaptive (agile) approaches accept that requirements will "
  "emerge, and deliver in short increments so feedback arrives early. Hybrid "
  "blends them — for example, a fixed regulatory scope delivered predictively "
  "alongside a user-facing component delivered in sprints. The July 2026 exam "
  "splits roughly 40% predictive, 60% adaptive and hybrid, so you cannot pass "
  "on waterfall knowledge alone.",
  ["Predictive — scope fixed early, change via formal change control",
   "Iterative — repeated cycles refine the same deliverable",
   "Incremental — successive slices each add usable functionality",
   "Agile — both iterative and incremental, with continuous feedback",
   "Hybrid — deliberately combines approaches per component"]),
 ("Enterprise environmental factors and organisational process assets",
  "EEFs are conditions you do not control but must work within: market "
  "conditions, regulation, organisational culture, the infrastructure you are "
  "handed. OPAs are the assets your organisation gives you to reuse: templates, "
  "historical data, lessons learned, procurement rules, defined processes. The "
  "exam distinction is simple but heavily tested — EEFs constrain you, OPAs "
  "help you.",
  ["EEF internal — culture, structure, existing systems, staff capability",
   "EEF external — regulation, market conditions, standards, geopolitics",
   "OPA processes — policies, procedures, templates, defined workflows",
   "OPA knowledge — historical data, lessons learned, estimating databases"]),
 ("Governance, escalation and phase gates",
  "Governance is the framework of authority: who decides what, within which "
  "thresholds, and what happens when a threshold is breached. A governance "
  "board or steering committee provides oversight; the project manager operates "
  "within delegated tolerances. When a problem exceeds your tolerance — a cost "
  "overrun beyond the agreed percentage, a risk above the agreed severity — you "
  "escalate. Phase gates are the scheduled decision points where the project is "
  "formally reviewed and authorised to continue, be redirected, or be stopped.",
  ["Define escalation thresholds BEFORE you need them",
   "Escalating within an agreed threshold is competence, not failure",
   "Phase gates permit a go / no-go decision, including cancellation",
   "Governance defines success metrics, not just spending limits"]),
 ("Compliance, sustainability and AI — the 2026 additions",
  "The July 2026 outline raised Business Environment from 8% to 26% of the "
  "exam and named sustainability explicitly across compliance, cost of quality "
  "and risk response. Compliance is no longer only legal and regulatory: "
  "environmental impact, workplace health and safety, ethical practice and "
  "data security all sit inside the compliance envelope. Artificial "
  "intelligence enters as both a tool (estimation, risk detection, reporting) "
  "and a governance concern (bias, explainability, data protection).",
  ["Classify compliance categories, then assess threats to each",
   "Analyse the consequences of non-compliance, not just the requirement",
   "Measure the extent of compliance — it is a metric, not a binary",
   "AI used on a project needs its own governance and audit trail"]),
],
2: [
 ("The business case and why projects get funded",
  "Projects exist to deliver benefit. The business case is the documented "
  "economic feasibility study that justifies the investment: the problem or "
  "opportunity, the options considered, the recommended option, and the "
  "financial and non-financial returns. It is prepared before the charter and "
  "is the reference point you return to whenever someone proposes a change "
  "that erodes the value the project was funded to deliver.",
  ["Cost-benefit analysis compares the cost of the work to the benefit gained",
   "Payback period — how long until the investment is recovered; shorter is better",
   "Net present value (NPV) — future cash flows discounted to today; positive is good",
   "Internal rate of return (IRR) and benefit-cost ratio (BCR) — higher is better",
   "Opportunity cost — the value of the option you did NOT choose"]),
 ("The project charter",
  "The charter authorises the project and, critically, authorises the project "
  "manager to apply organisational resources to it. It is issued by a sponsor "
  "external to the project with the authority to fund it. Without a charter you "
  "have no mandate. It stays deliberately high level — names, objectives, "
  "high-level requirements, summary milestones and budget, key risks, and the "
  "approval criteria.",
  ["Authorises the project's existence and the PM's authority",
   "Signed by the sponsor, not written by the sponsor alone",
   "Contains measurable objectives and success criteria",
   "Records assumptions, constraints and high-level risk",
   "Is not re-baselined — it is the founding document"]),
 ("Identifying and analysing stakeholders",
  "A stakeholder is anyone who affects, is affected by, or believes they are "
  "affected by the project. That last clause matters: perceived impact "
  "generates real behaviour. Identification is continuous, not a one-off task "
  "at initiation. The stakeholder register records who they are, their "
  "interest, influence, expectations and your engagement strategy.",
  ["Power/interest grid — the most commonly examined classification",
   "Salience model — power, legitimacy and urgency combined",
   "Directions of influence — upward, downward, sideward, outward",
   "Engagement levels — unaware, resistant, neutral, supportive, leading",
   "The SEAM records Current (C) versus Desired (D) engagement per stakeholder"]),
 ("Aligning and managing expectations",
  "The 2026 outline separates engaging stakeholders (People T4) from aligning "
  "their expectations (T5) and managing those expectations over time (T6). "
  "Alignment is the facilitation work of getting parties with different "
  "definitions of success to agree one definition. Management is the ongoing "
  "monitoring of satisfaction and responding when it drifts.",
  ["Identify expectations explicitly — unstated expectations become disputes",
   "Facilitate discussion where expectations conflict; do not arbitrate silently",
   "Monitor internal and external customer satisfaction continuously",
   "Build trust deliberately; influence follows trust, not authority"]),
],
3: [
 ("The integrated project management plan",
  "The project management plan is not one document but the integration of all "
  "subsidiary plans — scope, schedule, cost, quality, resource, communications, "
  "risk, procurement and stakeholder engagement — plus the three baselines "
  "(scope, schedule, cost). Integration is the point: the plans must be "
  "internally consistent, and a change to one usually forces a change to "
  "others.",
  ["Subsidiary management plans define HOW each knowledge area will be run",
   "Baselines are the approved versions against which performance is measured",
   "Changes to a baseline require an approved change request — always",
   "Rolling wave planning elaborates near-term work in detail, later work coarsely"]),
 ("Scope: from requirements to work packages",
  "Scope work moves from elicitation (what do stakeholders need?) through "
  "definition (what will we deliver?) to decomposition (what work produces it?). "
  "The Requirements Traceability Matrix links each requirement forward to the "
  "deliverable, test and acceptance that satisfies it. The WBS decomposes the "
  "deliverables — not the activities — down to work packages, and obeys the "
  "100% rule: the WBS contains all the work and only the work.",
  ["Scope creep — uncontrolled additions without change control",
   "Gold plating — the team adding unrequested extras; never acceptable",
   "The WBS decomposes DELIVERABLES; the activity list decomposes the work",
   "The WBS dictionary carries the detail for each work package",
   "Scope baseline = scope statement + WBS + WBS dictionary"]),
 ("Schedule: dependencies, estimating and the critical path",
  "Activities are sequenced by dependency type (mandatory, discretionary, "
  "external, internal) and relationship (finish-to-start being the most common). "
  "Durations are estimated by analogous, parametric, three-point or bottom-up "
  "methods. The critical path is the longest path through the network and "
  "therefore the shortest possible duration; activities on it have zero float. "
  "Compressing it means crashing (adding cost) or fast tracking (adding risk).",
  ["Three-point (PERT): (O + 4M + P) / 6, with σ = (P − O) / 6",
   "Total float — delay available before the project end date slips",
   "Free float — delay available before the NEXT activity is affected",
   "Critical path activities have zero total float by definition",
   "Crashing adds cost; fast tracking adds risk and potential rework"]),
 ("Cost: estimating, budgeting and reserves",
  "Cost estimates roll up from work packages into the cost baseline, to which "
  "contingency reserve is added for identified risks. Management reserve sits "
  "above the cost baseline for unknown-unknowns and requires management "
  "approval to access. The distinction is examined frequently: contingency is "
  "inside the baseline and under your control, management reserve is outside "
  "it and is not.",
  ["Cost baseline = work package estimates + contingency reserve",
   "Budget at completion (BAC) = cost baseline + management reserve",
   "Contingency reserve — for identified (known) risks; PM controls it",
   "Management reserve — for unidentified risks; management controls it"]),
 ("Quality: planning it in, not inspecting it in",
  "Quality is conformance to requirements and fitness for use. It is cheaper to "
  "prevent than to inspect, and far cheaper to fix early than late — the cost "
  "of change curve rises steeply as the project progresses. The cost of quality "
  "splits into conformance costs (prevention, appraisal) and non-conformance "
  "costs (internal failure, external failure). External failure — the customer "
  "finds the defect — is the most expensive outcome of all.",
  ["Prevention — training, process design, prototyping; the cheapest lever",
   "Appraisal — inspection, testing, audits; finds defects before the customer",
   "Internal failure — rework caught in-house",
   "External failure — the customer finds it; cost includes reputation",
   "Root cause tools: 5 Whys, fishbone, Pareto, control charts"]),
 ("Risk: identification through response",
  "Risk is an uncertain event that, if it occurs, has a positive or negative "
  "effect on objectives. Risks are future and uncertain; issues are present and "
  "certain. Qualitative analysis prioritises risks by probability and impact; "
  "quantitative analysis models their aggregate effect in money or time. "
  "Response strategies mirror each other for threats and opportunities.",
  ["Threats: escalate, avoid, transfer, mitigate, accept",
   "Opportunities: escalate, exploit, share, enhance, accept",
   "EMV = probability × impact, summed across outcomes",
   "Secondary risk arises FROM your response; residual risk remains after it",
   "A risk that has occurred is no longer a risk — it is an issue"]),
 ("Procurement and contract types",
  "Contract type determines who carries cost risk. Fixed-price contracts place "
  "risk on the seller and suit well-defined scope. Cost-reimbursable contracts "
  "place risk on the buyer and suit uncertain scope. Time and materials sits "
  "between the two and suits small or urgent engagements where scope is not yet "
  "clear.",
  ["Firm fixed price (FFP) — seller carries the cost risk entirely",
   "Fixed price incentive fee (FPIF) — shared risk with a performance incentive",
   "Cost plus fixed fee (CPFF) — buyer carries cost risk; fee is fixed",
   "Cost plus incentive/award fee (CPIF/CPAF) — buyer risk with incentives",
   "Time and materials (T&M) — hybrid; cap it or it becomes open-ended"]),
],
4: [
 ("Leadership style and the servant leader",
  "There is no single correct leadership style; the ECO asks you to *determine "
  "an appropriate* style for the situation, team maturity and organisational "
  "context. Servant leadership — the dominant model in adaptive environments — "
  "inverts the usual hierarchy: the leader's job is to remove impediments, "
  "grow people and make it safe to raise problems, so the team can do the work.",
  ["Servant leadership — serve the team so the team can deliver",
   "Transformational — inspire through vision and individual attention",
   "Transactional — exchange reward for defined performance",
   "Laissez-faire — hands off; only works with a mature, self-organising team",
   "Situational — deliberately vary the style by person and circumstance"]),
 ("Team development and motivation",
  "Tuckman's model — forming, storming, norming, performing, adjourning — "
  "describes how teams mature, and each stage calls for different leadership. "
  "Storming is normal and necessary, not a failure. Motivation theory tells you "
  "what to reach for: Herzberg separates hygiene factors (whose absence "
  "demotivates) from motivators (whose presence motivates), which is why a pay "
  "rise fixes dissatisfaction but does not create engagement.",
  ["Forming — provide direction and clarify purpose",
   "Storming — facilitate conflict; do not suppress it",
   "Norming — reinforce the working agreements the team has built",
   "Performing — delegate and remove blockers; stay out of the way",
   "Adjourning — recognise contribution and capture lessons learned"]),
 ("Conflict management — the most examined People topic",
  "Conflict is inevitable and, handled well, productive. The five modes trade "
  "off assertiveness against cooperativeness. Collaborating (problem solving) "
  "produces a genuine win-win and is the preferred answer in most exam "
  "situations, because it addresses the underlying need rather than splitting "
  "the difference. Forcing and avoiding are appropriate only in narrow "
  "circumstances — emergencies, or trivia not worth the cost of resolution.",
  ["Collaborate / problem solve — win-win; the usual best answer",
   "Compromise / reconcile — lose-lose; both give something up",
   "Smooth / accommodate — lose-win; preserves the relationship",
   "Force / direct — win-lose; fast, but damages trust",
   "Withdraw / avoid — defers; appropriate only for trivia or cooling off"]),
 ("Communication",
  "Communication consumes most of a project manager's time. The channels "
  "formula, N(N−1)/2, shows why: adding people to a team increases the "
  "communication burden quadratically. A communications management plan defines "
  "who needs what information, in what format, how often, and through which "
  "method — push, pull or interactive.",
  ["Channels = N(N − 1) / 2 — ten people means forty-five channels",
   "Push — sent to recipients (email, reports); no confirmation of understanding",
   "Pull — recipients retrieve it (portals, dashboards); suits large audiences",
   "Interactive — real-time exchange; the only mode that confirms understanding",
   "Tailor the message to the stakeholder — this is an explicit ECO enabler"]),
],
5: [
 ("Earned value management",
  "EVM integrates scope, schedule and cost into a single set of measures, and "
  "it is the most calculation-heavy topic on the exam. Three inputs drive "
  "everything: planned value (what you said you would have done by now), earned "
  "value (what you have actually completed, valued at budget) and actual cost "
  "(what you spent doing it). Everything else derives from those three.",
  ["CV = EV − AC   ·   SV = EV − PV   (positive is good in both cases)",
   "CPI = EV / AC   ·   SPI = EV / PV   (above 1.0 is good in both cases)",
   "EAC = BAC / CPI when current variances are expected to continue",
   "ETC = EAC − AC   ·   VAC = BAC − EAC",
   "TCPI = (BAC − EV) / (BAC − AC) — the performance needed to finish on budget"]),
 ("Integrated change control",
  "Every change request follows the same path regardless of who raised it: "
  "record it, assess its impact across scope, schedule, cost, quality and risk, "
  "take it to the change control board for a decision, then either implement "
  "and update the baselines and documents, or record the rejection. The exam's "
  "most common trap is the option that implements a change without assessing "
  "impact or obtaining approval — it is always wrong.",
  ["Never implement an unapproved change, however senior the requester",
   "Assess impact across ALL constraints before recommending a decision",
   "Corrective action realigns performance with the plan",
   "Preventive action reduces the probability of future variance",
   "Update the baselines and affected documents after approval"]),
 ("Controlling quality with statistical tools",
  "Control charts distinguish variation that is inherent in the process "
  "(common cause) from variation that signals something has changed "
  "(assignable cause). A point outside the control limits is out of control. "
  "So is the rule of seven: seven consecutive points on one side of the mean "
  "indicates a non-random pattern even when every point sits inside the limits.",
  ["Control limits (UCL/LCL) are calculated from the process, usually ±3σ",
   "Specification limits come from the customer and are a different thing",
   "Rule of seven — seven consecutive points on one side signals assignable cause",
   "Pareto — the 80/20 rule; fix the vital few categories first",
   "In control does not mean acceptable; it means predictable"]),
 ("Issues, impediments and risk that has arrived",
  "The 2026 outline gives impediment removal its own task. The distinction "
  "matters: a risk is uncertain and future; when it occurs it becomes an issue "
  "and moves from the risk register to the issue log. Impediments and blockers "
  "are anything stopping the team from progressing, and clearing them is "
  "explicitly the project manager's job.",
  ["Recognise the moment a risk becomes an issue and re-classify it",
   "Evaluate impact, then prioritise — not every impediment is urgent",
   "Apply an intervention strategy, then reassess that it actually worked",
   "Escalate beyond your threshold rather than absorbing the impact silently"]),
],
6: [
 ("Closing the project or phase",
  "Closure is a formal process, not simply stopping work. Deliverables are "
  "accepted against the acceptance criteria agreed at the start; the product is "
  "transitioned to the receiving organisation with the knowledge needed to run "
  "it; procurements are closed and contracts archived; resources are released; "
  "and lessons learned are transferred into the organisational repository so "
  "the next project inherits them. Projects terminated early are closed through "
  "exactly the same process.",
  ["Obtain formal stakeholder approval of completion — not informal agreement",
   "Validate readiness for transition before handing over",
   "Archive contracts, financial records and project documentation",
   "Release resources deliberately, with recognition",
   "Update OPAs so the organisation learns; this is the durable output"]),
 ("Benefits realisation",
  "The project ends before the benefits arrive. The benefits management plan "
  "names the benefits owner, the metrics and the measurement timeframe, so that "
  "value is confirmed after handover rather than assumed at closure. The 2026 "
  "outline's emphasis on value-based delivery makes this explicit: verify a "
  "measurement system is in place to track benefits.",
  ["Benefits are usually realised after the project closes",
   "A named benefits owner carries accountability past project end",
   "Metrics and baselines must exist before you can claim value",
   "Examine business value throughout — not only at the gate reviews"]),
 ("Preparing for the examination",
  "The exam is 180 questions in 240 minutes: about eighty seconds each. Ten "
  "questions are unscored pretest items, indistinguishable from the rest. Two "
  "ten-minute breaks are offered, the first after the case-study section — and "
  "once you start a break you cannot return to the previous section, so review "
  "before you break, not after.",
  ["180 questions (170 scored, 10 pretest) in 240 minutes",
   "People 33% · Process 41% · Business Environment 26%",
   "About 40% predictive, 60% adaptive and hybrid",
   "Six question types, including the new graphic-based items",
   "Read for what the question ASKS — 'first', 'best', 'next' change the answer"]),
],
}


def main():
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)
    prodoc.style_headings(doc)

    prodoc.add_cover_page(
        doc, "Learner Guide", cd.COURSE_TITLE, cd.VERSION,
        org_logo=_logo("tertiary-infotech-logo.png"),
        course_logo=_logo("pmp-course-logo.png"),
        course_code=cd.COURSE_CODE)
    prodoc.add_version_control(doc, VERSIONS)
    prodoc.add_toc(doc)

    md.append(f"# {cd.COURSE_TITLE} — Learner Guide\n")
    md.append(f"**Version {cd.VERSION}** · Course Code {cd.COURSE_CODE} · "
              f"Trainer {cd.TRAINER} · {cd.ORG} (UEN {cd.UEN})\n")
    md.append("> Aligned to the PMI PMP Examination Content Outline — July 2026.\n")

    # -------------------------------------------------------- introduction
    h1(doc, "How to Use This Guide")
    para(doc, f"This Learner Guide accompanies the {cd.DAYS}-day "
              f"{cd.COURSE_TITLE} (course code {cd.COURSE_CODE}), delivered by "
              f"{cd.TRAINER}. It follows the same six topics as the slide "
              f"deck and the Lesson Plan, and the {len(LABS)} hands-on labs "
              f"referenced here are the same labs you complete in class.")
    para(doc, "Each topic chapter contains the teaching notes for that topic, "
              "the Examination Content Outline tasks it delivers, the labs that "
              "practise it, and a set of review questions. Work through the "
              "chapter after the session, then attempt the review questions "
              "without referring back.")
    para(doc, "The course is aligned to the PMI Examination Content Outline "
              "published for the July 2026 exam update. Where this guide differs "
              "from older PMP material, the 2026 outline governs.", after=10)

    h2(doc, "Learning Outcomes")
    table(doc, ["Ref", "Learning Outcome"],
          [[lo, txt] for lo, txt in cd.LEARNING_OUTCOMES])

    h2(doc, "Examination Content Outline — July 2026")
    table(doc, ["Domain", "Weighting", "What it covers"],
          [[f"Domain {r}. {name}", f"{pct}%", blurb]
           for r, name, pct, blurb in cd.ECO_DOMAINS])
    para(doc, f"Exam format: {cd.ECO_EXAM['questions']} questions "
              f"({cd.ECO_EXAM['scored']} scored, {cd.ECO_EXAM['pretest']} "
              f"unscored pretest) in {cd.ECO_EXAM['minutes']} minutes. "
              f"{cd.ECO_EXAM['breaks']} {cd.ECO_EXAM['approach_mix']}")

    h2(doc, "The Running Case Study")
    para(doc, "Every lab builds on the Contoso Training Portal Upgrade — a "
              "hybrid project to modernise a training provider's course "
              "registration and learner communications. It has a fixed launch "
              "date, a limited budget, a mandatory compliance review, and "
              "product increments delivered in sprints. Artifacts you produce "
              "in early labs become inputs to later ones, so by the capstone "
              "you hold a complete project management plan.")

    # ------------------------------------------------------ topic chapters
    for no, name, blurb, ecos, subtopics in cd.TOPICS:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        h1(doc, f"Topic {no}. {name}")
        para(doc, blurb)

        h2(doc, "Examination Content Outline Coverage")
        rows = []
        for dom, tn in ecos:
            stmt = next(s for n2, s, _ in cd.ECO_TASKS[dom] if n2 == tn)
            enablers = next(e for n2, _, e in cd.ECO_TASKS[dom] if n2 == tn)
            rows.append([f"{dom} T{tn}", stmt, "; ".join(enablers)])
        table(doc, ["Task", "Task statement", "Enablers"], rows)

        h2(doc, "What This Topic Covers")
        for st in subtopics:
            bullet(doc, st)

        # detailed teaching notes
        for heading, body, points in TOPIC_NOTES.get(no, []):
            h2(doc, heading)
            para(doc, body)
            for p in points:
                bullet(doc, p)

        # labs for this topic
        labs = BY_TOPIC.get(no, [])
        if labs:
            h2(doc, "Hands-on Labs for This Topic")
            table(doc, ["Lab", "Title", "ECO", "LO", "In class", "Self-study",
                        "Produces"],
                  [[f"{l['no']:02d}", l["title"], l["eco"], l["lo"],
                    f"{l['in_class']} min",
                    f"{l['minutes'] - l['in_class']} min",
                    ", ".join(l["outputs"])]
                   for l in labs])
            para(doc, "Full step-by-step instructions for each lab are in the "
                      "labs/ folder of your course materials. You complete the "
                      "core steps in class; the extension steps are self-study "
                      "that finishes the artifact.",
                 size=10, color=GREY)

        h2(doc, "Review Questions")
        for q in REVIEW_QUESTIONS.get(no, []):
            numbered(doc, q)
            md.append(f"1. {q}")

    # --------------------------------------------------------- lab summary
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Complete Lab Index")
    ic = sum(l["in_class"] for l in LABS)
    tot = sum(l["minutes"] for l in LABS)
    para(doc, f"{len(LABS)} labs totalling {tot} minutes "
              f"({tot/60:.1f} hours) of hands-on practice: {ic} minutes "
              f"timetabled in class across the four days, and {tot - ic} "
              f"minutes of extension work you complete as self-study.")
    table(doc, ["Lab", "Title", "Day", "Topic", "ECO Task", "LO",
                "In class", "Self-study"],
          [[f"{l['no']:02d}", l["title"], f"Day {l['day']}", f"T{l['topic']}",
            l["eco"], l["lo"], str(l["in_class"]),
            str(l["minutes"] - l["in_class"])] for l in LABS])

    h2(doc, "Tools Used in the Labs")
    table(doc, ["Tool", "Purpose", "URL"],
          [[n, p, u] for _k, (n, u, p) in cd.TOOLS.items()])

    # -------------------------------------------------------- exam section
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h1(doc, "Preparing for the PMP Examination")

    h2(doc, "Exam Structure")
    table(doc, ["Element", "Detail"],
          [["Questions", f"{cd.ECO_EXAM['questions']} "
                         f"({cd.ECO_EXAM['scored']} scored + "
                         f"{cd.ECO_EXAM['pretest']} pretest)"],
           ["Duration", f"{cd.ECO_EXAM['minutes']} minutes"],
           ["Breaks", cd.ECO_EXAM["breaks"]],
           ["Approach mix", cd.ECO_EXAM["approach_mix"]],
           ["Domains", "People 33% · Process 41% · Business Environment 26%"]])

    h2(doc, "Question Types")
    table(doc, ["Type", "What it asks of you"],
          [[t, d] for t, d in cd.ECO_EXAM["question_types"]])

    h2(doc, "Formula Reference")
    table(doc, ["Formula", "Expression", "Reading"],
          [["Cost variance", "CV = EV − AC", "Positive is under budget"],
           ["Schedule variance", "SV = EV − PV", "Positive is ahead of schedule"],
           ["Cost performance index", "CPI = EV / AC", "Above 1.0 is under budget"],
           ["Schedule performance index", "SPI = EV / PV", "Above 1.0 is ahead"],
           ["Estimate at completion", "EAC = BAC / CPI",
            "When current variance is expected to continue"],
           ["Estimate to complete", "ETC = EAC − AC", "Remaining expected cost"],
           ["Variance at completion", "VAC = BAC − EAC", "Forecast budget variance"],
           ["To-complete performance index", "TCPI = (BAC − EV) / (BAC − AC)",
            "Efficiency needed to finish on budget"],
           ["Three-point (PERT)", "(O + 4M + P) / 6", "Weighted average estimate"],
           ["PERT standard deviation", "(P − O) / 6", "Estimate uncertainty"],
           ["Expected monetary value", "EMV = probability × impact",
            "Summed across outcomes"],
           ["Communication channels", "N(N − 1) / 2", "Grows quadratically"]])

    h2(doc, "Study Plan After the Course")
    for step in [
        "Week 1-2: Re-read this guide topic by topic and redo the labs on a "
        "project of your own.",
        "Week 3-4: Drill practice questions by domain, weighting your time "
        "Process 41%, People 33%, Business Environment 26%.",
        "Week 5-6: Practise the graphic-based and case-study question types "
        "specifically — they behave differently from plain multiple choice.",
        "Week 7-8: Sit at least three full 180-question mock exams under timed "
        "conditions, reviewing every wrong answer to its underlying concept.",
        "Submit your PMI application using this course for the 35 contact hours.",
    ]:
        numbered(doc, step)

    prodoc.add_page_numbers(doc, left_text="www.tertiarycourses.com.sg")
    prodoc.enable_update_fields(doc)

    out_docx = os.path.join(REPO, "courseware", f"LG-{cd.SHORT_TITLE}.docx")
    doc.save(out_docx)

    out_md = os.path.join(REPO, f"LG-{cd.SHORT_TITLE}.md")
    with open(out_md, "w") as f:
        f.write("\n".join(md).replace("\n\n\n", "\n\n") + "\n")

    print(f"saved -> {out_docx}")
    print(f"saved -> {out_md}")


REVIEW_QUESTIONS = {
1: ["Distinguish a project from operations, and give an example of each from "
    "your own workplace.",
    "Your sponsor asks for additional scope while holding the date and budget "
    "fixed. Explain the trade-off using the triple constraint.",
    "Classify each of the following as an EEF or an OPA: a lessons-learned "
    "database, a new data-protection regulation, the organisation's "
    "procurement policy, the existing IT infrastructure.",
    "What is the difference between a governance escalation threshold and a "
    "phase gate?",
    "Name three compliance categories beyond legal and regulatory that the "
    "2026 outline expects you to consider.",
    "How does the July 2026 exam update change the weighting of Business "
    "Environment, and why does that matter for your study plan?"],
2: ["What does the project charter authorise that no other document does?",
    "A project has an initial investment of $200,000 and returns $60,000 per "
    "year. Calculate the payback period and state one limitation of using it "
    "alone.",
    "Compare the power/interest grid with the salience model. When would you "
    "prefer each?",
    "A stakeholder is currently resistant but needs to be supportive. How "
    "would you record and act on that in a SEAM?",
    "Explain the difference between engaging stakeholders and aligning their "
    "expectations, per ECO People T4 and T5.",
    "Why is 'anyone who believes they are affected' included in the definition "
    "of a stakeholder?"],
3: ["State the 100% rule and explain what it prohibits.",
    "Given O=4, M=6, P=14 days, calculate the PERT estimate and the standard "
    "deviation.",
    "Distinguish total float from free float, and state the float of an "
    "activity on the critical path.",
    "A risk has a 30% probability and a $80,000 impact. Calculate the EMV and "
    "explain how you would use it.",
    "Contrast contingency reserve with management reserve, including who "
    "controls each.",
    "Which contract type would you choose for a well-defined deliverable with "
    "a fixed specification, and who carries the cost risk?",
    "Distinguish scope creep from gold plating, and state why gold plating is "
    "never acceptable.",
    "List the five threat response strategies and their opportunity mirrors."],
4: ["Describe the leadership action appropriate at each stage of Tuckman's "
    "model.",
    "Explain why a pay rise may remove dissatisfaction without creating "
    "motivation, using Herzberg's theory.",
    "A designer and a developer disagree on a screen layout. Which conflict "
    "mode would you use first, and why?",
    "Calculate the number of communication channels for a team of 12, and "
    "state what the result implies for your communications plan.",
    "Distinguish push, pull and interactive communication, and state which "
    "confirms understanding.",
    "What does 'represent the voice of the team' require of a project manager "
    "in practice?"],
5: ["A project has BAC $500,000. At week 10: PV $200,000, EV $180,000, AC "
    "$210,000. Calculate CV, SV, CPI, SPI and EAC, and state the project's "
    "health in one sentence.",
    "A senior stakeholder instructs you to implement a change immediately. "
    "State your correct sequence of actions.",
    "Distinguish common cause from assignable cause variation, and explain the "
    "rule of seven.",
    "When does a risk become an issue, and what changes in your documentation "
    "at that moment?",
    "Compare crashing with fast tracking, including the cost and risk "
    "consequences of each.",
    "Explain how a Pareto chart directs your quality improvement effort."],
6: ["List the activities required to formally close a project or phase.",
    "Why are benefits usually realised after the project has closed, and who "
    "is accountable for them?",
    "What is the difference between the lessons learned register and the "
    "lessons learned repository?",
    "A project is terminated early. Which closure activities still apply?",
    "State the exam's question count, scored count, duration and break "
    "structure.",
    "Explain the significance of the words 'first', 'best' and 'next' in a "
    "situational exam question."],
}


if __name__ == "__main__":
    main()
