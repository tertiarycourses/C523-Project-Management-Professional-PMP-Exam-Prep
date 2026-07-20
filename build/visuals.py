"""
Visual slide primitives for the PMP 35 PDU deck.

All-white theme, Arial everywhere, 16:9. Every helper here renders a
*visual* layout (cards, process maps, matrices, charts) -- never a plain
bullet wall. See tertiary-ppt-design house standard.
"""
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION

# ---------------------------------------------------------------- palette
BLUE   = RGBColor(0x1F, 0x6F, 0xEB)
TEAL   = RGBColor(0x10, 0xB9, 0x81)
INK    = RGBColor(0x16, 0x1B, 0x26)
GREY   = RGBColor(0x5B, 0x63, 0x72)
VIOLET = RGBColor(0x7C, 0x3A, 0xED)
AMBER  = RGBColor(0xF5, 0x9E, 0x0B)
ROSE   = RGBColor(0xE1, 0x1D, 0x48)
CYAN   = RGBColor(0x06, 0xB6, 0xD4)
LIGHT  = RGBColor(0xF5, 0xF8, 0xFC)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LINE   = RGBColor(0xDD, 0xE3, 0xEC)

# rotating accent palette so consecutive slides differ in colour
ACCENTS = [BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE]

SW, SH = Inches(13.333), Inches(7.5)
FONT = "Arial"

# Read from the single source so the footer can never drift from the cover.
import course_data as _cd
COURSE = _cd.COURSE_TITLE
CODE = _cd.COURSE_CODE
COPYRIGHT = f"© 2026 {_cd.ORG}"


def accent_for(i):
    return ACCENTS[i % len(ACCENTS)]


def tint(c, f=0.90):
    """Lighten a colour toward white by factor f (0=orig, 1=white)."""
    return RGBColor(
        int(c[0] + (255 - c[0]) * f),
        int(c[1] + (255 - c[1]) * f),
        int(c[2] + (255 - c[2]) * f),
    )


# ---------------------------------------------------------------- text util
def _tf(shape, text, size, color=INK, bold=False, align=PP_ALIGN.LEFT,
        anchor=MSO_ANCHOR.TOP, italic=False, space_after=4, line=1.0):
    tf = shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.10)
    tf.margin_top = tf.margin_bottom = Inches(0.05)
    lines = text if isinstance(text, list) else [text]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        p.line_spacing = line
        r = p.add_run()
        r.text = str(ln)
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = FONT
    return tf


# ---------------------------------------------------------- text metrics
# Arial advance width as a fraction of point size, measured empirically for
# mixed-case sentence text. Bold runs slightly wider.
# Measured from rendered output, not guessed: 23 real bold titles sampled from
# the PDF gave a mean advance of 0.488 and a max of 0.506 of the point size.
# Using the measured MAX keeps the estimate on the safe side (a slightly early
# wrap costs a little space; a late one clips text).
_ADV = 0.472          # regular Arial, same sampling method
_ADV_BOLD = 0.506
_ADV_MEAN = 0.455     # measured mean — for call sites where over-reserving
_ADV_BOLD_MEAN = 0.488  # is itself the defect (see `conservative` below)

# _tf() sets margin_left/right to 0.10in, and those insets are inside the
# shape width — text wraps against (width - 2 * inset), not width.
_INSET_EMU = 91440  # 0.10 in


def wrapped_lines(text, width_emu, size_pt, bold=False, conservative=True):
    """Lines the text wraps to.

    `conservative=True` uses the measured MAX advance, erring toward an extra
    line — right when the answer feeds a height reserve, because clipping is
    worse than slack. `conservative=False` uses the measured MEAN, for call
    sites where over-reserving is itself the defect (e.g. the title rule,
    which gets stranded a full line below a title that fits on one).

    Word-wrap breaks at spaces (and after / and dashes), so a pure character
    count under-estimates. This walks the words and is the single place that
    estimate is made — every layout sizes its shapes from THIS.
    """
    if not text:
        return 1
    import re as _re
    # An explicit newline is a HARD break the renderer always honours. Splitting
    # on whitespace loses it, so a "title\nsubtitle" string measured as one run
    # under-counts its height and the block overruns whatever sits beneath it.
    if "\n" in str(text):
        return sum(wrapped_lines(part, width_emu, size_pt, bold, conservative)
                   for part in str(text).split("\n"))
    if bold:
        base = _ADV_BOLD if conservative else _ADV_BOLD_MEAN
    else:
        base = _ADV if conservative else _ADV_MEAN
    adv = base * size_pt                               # points per char
    # PowerPoint applies default textbox insets (0.1in each side) that are NOT
    # part of the shape width. Measuring against the raw width over-estimated
    # the usable space by ~11% on narrow boxes and let titles overrun bodies.
    usable = max(width_emu - 2 * _INSET_EMU, width_emu * 0.5)
    avail = max((usable / 12700.0), 1.0)               # EMU -> points
    # Renderers also break after / - — and en/em dashes, not only at spaces.
    # Treating "Acknowledge/feedback" as one unbreakable token under-counted
    # its height and let the label overrun the body beneath it.
    words = [w for w in _re.split(r"(?<=[/\-–—])|\s+", str(text)) if w]
    lines, cur = 1, 0.0
    for word in words:
        wlen = (len(word) + 1) * adv
        if cur + wlen > avail and cur > 0:
            lines += 1
            cur = wlen
        else:
            cur += wlen
        # a single token wider than the box wraps inside itself
        if wlen > avail:
            lines += int(wlen // avail)
            cur = wlen % avail
    return lines


# A rendered line occupies more than font-size x line-spacing: Arial's
# ascent+descent+leading adds ~35%. Measured from an actual render (40pt at
# line_spacing 1.10 produced a 0.823in pitch => 1.48 x size).
_LINE_BOX = 1.35


def text_height(text, width_emu, size_pt, bold=False, line_spacing=1.15,
                conservative=True):
    """Height the wrapped text actually occupies when rendered, in EMU."""
    n = wrapped_lines(text, width_emu, size_pt, bold, conservative)
    return int(n * size_pt * line_spacing * _LINE_BOX * 12700)


def fit_size(text, width_emu, height_emu, start_pt, min_pt=8.0,
             bold=False, line_spacing=1.15):
    """Largest font size at or below `start_pt` whose wrapped text fits."""
    sz = start_pt
    while sz > min_pt:
        if text_height(text, width_emu, sz, bold, line_spacing) <= height_emu:
            return sz
        sz -= 0.5
    return min_pt


def box(slide, x, y, w, h, fill=None, lineclr=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        adj=0.10, shadow=False, linew=1.0):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            s.adjustments[0] = adj
        except Exception:
            pass
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if lineclr is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = lineclr
        s.line.width = Pt(linew)
    s.shadow.inherit = shadow
    return s


def textbox(slide, x, y, w, h, text, size, **kw):
    tb = slide.shapes.add_textbox(x, y, w, h)
    _tf(tb, text, size, **kw)
    return tb


# ---------------------------------------------------------------- chrome
def add_footer(slide, num):
    textbox(slide, Inches(0.45), Inches(7.02), Inches(5.2), Inches(0.32),
            f"{COURSE}  |  {CODE}", 8.5, color=GREY)
    textbox(slide, Inches(5.0), Inches(7.02), Inches(3.4), Inches(0.32),
            COPYRIGHT, 8.5, color=GREY, align=PP_ALIGN.CENTER)
    textbox(slide, Inches(12.15), Inches(7.02), Inches(0.75), Inches(0.32),
            str(num), 8.5, color=GREY, align=PP_ALIGN.RIGHT)


def title_bar(slide, title, kicker=None, accent=BLUE):
    """Kicker + title + accent rule. Returns y where body may start.

    A title long enough to wrap pushes the accent rule and the returned body
    origin down, so the second line is never struck through by the rule or
    overrun by the content beneath it.
    """
    y = Inches(0.42)
    if kicker:
        textbox(slide, Inches(0.62), y, Inches(11.5), Inches(0.26),
                kicker.upper(), 12, color=accent, bold=True)
        y = Inches(0.72)
    # Derive the band from the MEASURED wrap, not a character threshold: a
    # 2-line reservation on a 1-line title orphaned the accent rule half an
    # inch below the text.
    # Measured: the longest single-line titles in this deck render to 864pt
    # (12.0in). The box is 12.2in and LibreOffice does not apply the inset to
    # it the way it does to narrow boxes, so measure against the near-full
    # width and use the MEAN advance — over-reserving here strands the accent
    # rule a full line below a title that actually fits on one.
    # Use the CONSERVATIVE (max) advance: under-reserving here lets the body
    # content overlap a title that wrapped, which is a real defect, whereas
    # over-reserving only leaves cosmetic slack above the accent rule.
    tw_title = Inches(12.2)
    th = text_height(title, tw_title + Inches(0.20), 27, bold=True,
                     line_spacing=1.04, conservative=True)
    # Top-anchored and grown downward: the box starts at the kicker baseline
    # (so a 2-line title cannot ride up over the kicker) and the rule follows
    # the ESTIMATED height. A one-line over-estimate leaves a little slack
    # above the rule — cosmetic — which is the safe direction to err.
    textbox(slide, Inches(0.58), y, tw_title, th,
            title, 27, color=INK, bold=True, line=1.04)
    rule_y = y + th + Inches(0.06)
    box(slide, Inches(0.62), rule_y, Inches(0.9), Inches(0.055),
        fill=accent, shape=MSO_SHAPE.RECTANGLE)
    return rule_y + Inches(0.26)


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])
