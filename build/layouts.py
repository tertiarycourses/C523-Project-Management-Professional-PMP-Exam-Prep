"""
Slide layout library. Each function renders one information-dense,
visual slide. No layout emits a thin "one-liner" page: every card/step
carries a heading AND a supporting detail line.
"""
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.dml.color import RGBColor

from visuals import (
    BLUE, TEAL, INK, GREY, VIOLET, AMBER, ROSE, CYAN, LIGHT, WHITE, LINE,
    ACCENTS, accent_for, tint, box, textbox, title_bar, add_footer, blank,
    COURSE, CODE, COPYRIGHT, FONT, _tf,
    wrapped_lines, text_height, fit_size,
)

L, R = Inches(0.62), Inches(12.71)   # content margins
CW = R - L                            # content width


# ------------------------------------------------------------------ cover
def cover(prs, title, subtitle, meta_lines, logos=()):
    """logos: iterable of image paths rendered top-right on the cover."""
    s = blank(prs)
    box(s, Inches(0), Inches(0), Inches(13.333), Inches(0.55), fill=BLUE,
        shape=MSO_SHAPE.RECTANGLE)
    box(s, Inches(0), Inches(6.95), Inches(13.333), Inches(0.55), fill=INK,
        shape=MSO_SHAPE.RECTANGLE)
    # colour chips
    for i, c in enumerate([BLUE, TEAL, VIOLET, AMBER, CYAN, ROSE]):
        box(s, Inches(0.62 + i * 0.42), Inches(1.62), Inches(0.30), Inches(0.10),
            fill=c, shape=MSO_SHAPE.RECTANGLE)
    textbox(s, L, Inches(1.98), Inches(11.0), Inches(1.9), title, 42,
            color=INK, bold=True, line=1.06)
    textbox(s, L, Inches(3.62), Inches(11.9), Inches(0.45), subtitle, 19,
            color=BLUE, bold=True)
    box(s, L, Inches(4.22), Inches(3.0), Inches(0.05), fill=TEAL,
        shape=MSO_SHAPE.RECTANGLE)
    textbox(s, L, Inches(4.48), Inches(11.9), Inches(1.9), meta_lines, 13,
            color=GREY, space_after=5)
    textbox(s, Inches(0.62), Inches(7.05), Inches(9.0), Inches(0.36),
            COPYRIGHT, 10, color=WHITE)
    # house rule: the cover carries the organisation and course logos
    # sit them in the clear band beneath the top rule, clear of the title
    import os
    x = Inches(12.62)
    for p in [p for p in logos if p and os.path.exists(p)]:
        size = Inches(0.92)
        x -= size
        s.shapes.add_picture(p, x, Inches(0.80), height=size)
        x -= Inches(0.24)
    return s


# ------------------------------------------------------------ section divider
def section(prs, num, title, blurb, bullets, n, accent=None):
    s = blank(prs)
    accent = accent or accent_for(num)
    # stop the panel and its rule above the footer band so the accent bar
    # never strikes through the course code
    panel_h = Inches(6.94)
    box(s, Inches(0), Inches(0), Inches(4.55), panel_h, fill=tint(accent, .93),
        shape=MSO_SHAPE.RECTANGLE)
    box(s, Inches(4.55), Inches(0), Inches(0.07), panel_h, fill=accent,
        shape=MSO_SHAPE.RECTANGLE)
    textbox(s, Inches(0.62), Inches(1.55), Inches(3.6), Inches(1.5),
            f"{num:02d}", 96, color=accent, bold=True)
    textbox(s, Inches(0.66), Inches(3.05), Inches(3.5), Inches(0.4),
            "TOPIC", 14, color=accent, bold=True)
    textbox(s, Inches(0.62), Inches(3.42), Inches(3.6), Inches(2.2),
            title, 30, color=INK, bold=True, line=1.08)
    # the blurb pushes the bullet list down when it wraps, instead of the
    # list starting at a fixed y and colliding with it
    bl_lines = max(1, -(-len(str(blurb)) // 60))
    bl_h = Inches(0.29) * bl_lines
    textbox(s, Inches(5.15), Inches(1.62), Inches(7.5), bl_h,
            blurb, 16, color=GREY, line=1.22)
    y = max(Inches(2.92), Inches(1.62) + bl_h + Inches(0.26))
    # keep the whole list on the slide even when it is long
    step_y = min(Inches(0.56),
                 (Inches(6.80) - y) / max(len(bullets), 1))
    for i, b in enumerate(bullets):
        box(s, Inches(5.15), y, Inches(0.30), Inches(0.30), fill=accent,
            shape=MSO_SHAPE.OVAL)
        textbox(s, Inches(5.20), y + Inches(0.03), Inches(0.25), Inches(0.26),
                str(i + 1), 11, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
        textbox(s, Inches(5.60), y - Inches(0.02), Inches(7.1), step_y,
                b, 15, color=INK)
        y += step_y
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ cards
def cards(prs, title, items, n, kicker=None, accent=BLUE, cols=3):
    """items: list of (heading, detail) or (heading, detail, extra)."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    rows = (len(items) + cols - 1) // cols
    gap = Inches(0.26)
    cw = (CW - gap * (cols - 1)) / cols
    avail = Inches(7.02) - top - Inches(0.14)
    # fill the available height: single-row layouts get a taller card rather
    # than leaving the lower half of the slide empty.
    ch = (avail - gap * (rows - 1)) / rows
    # a single row of cards stretched to the full content height leaves a
    # void under the text; size it to the content instead
    y_off = Inches(0)
    if rows > 1:
        # Multi-row bands were stretched to fill the content area regardless
        # of how much text the cards held, leaving dead space at the foot of
        # every card and making long runs of card slides look repetitive.
        # Size from the tallest card's measured content instead.
        hw_m2 = cw - Inches(0.80)
        bw_m2 = cw - Inches(0.44)
        want2 = Inches(0)
        for it in items:
            hh2 = text_height(it[0], hw_m2, 14.5 if cols <= 3 else 13,
                              bold=True, line_spacing=1.05)
            body2 = " ".join(str(p) for p in it[1:] if p)
            bh2 = text_height(body2, bw_m2, 11.5, line_spacing=1.18)
            want2 = max(want2, Inches(0.34) + hh2 + Inches(0.16) + bh2
                        + Inches(0.26))
        if want2 < ch:
            # centre the tightened band in the content area so the reclaimed
            # space is shared above and below rather than all falling to the
            # bottom of the slide
            y_off = (ch - want2) * rows / 2
            ch = want2
    if rows == 1:
        # measure the tallest card's real content instead of guessing from
        # a character count that collapsed to the floor for short text
        hw_m = cw - Inches(0.80)
        bw_m = cw - Inches(0.44)
        want = Inches(0)
        for it in items:
            hh_m = text_height(it[0], hw_m, 14.5 if cols <= 3 else 13,
                               bold=True, line_spacing=1.05)
            body_txt = " ".join(str(p) for p in it[1:] if p)
            bh_m = text_height(body_txt, bw_m, 11.5, line_spacing=1.18)
            want = max(want, Inches(0.34) + hh_m + Inches(0.16) + bh_m
                       + Inches(0.28))
        want = max(want, Inches(2.10))
        if want < ch:
            # centre a single-row band so the reclaimed space is shared above
            # and below rather than stranding it all at the foot of the slide
            y_off = (ch - want) / 2
            ch = want
    for i, it in enumerate(items):
        head, detail = it[0], it[1]
        extra = it[2] if len(it) > 2 else None
        c = accent_for(i)
        r, col = divmod(i, cols)
        x = L + col * (cw + gap)
        y = top + y_off + r * (ch + gap)
        box(s, x, y, cw, ch, fill=LIGHT, lineclr=LINE)
        box(s, x, y, cw, Inches(0.075), fill=c, shape=MSO_SHAPE.RECTANGLE)
        box(s, x + Inches(0.20), y + Inches(0.24), Inches(0.34), Inches(0.34),
            fill=c, shape=MSO_SHAPE.OVAL)
        textbox(s, x + Inches(0.20), y + Inches(0.28), Inches(0.34), Inches(0.30),
                str(i + 1), 12, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
        # Size the heading box from its wrapped height and push the body
        # below it. A 3-line heading used to run straight over the body.
        hw = cw - Inches(0.80)
        head_sz = 14.5 if cols <= 3 else 13
        # Measure the heading the same way the bands above do. The old
        # character-count estimate under-counted a 3-line heading (it wraps at
        # word boundaries, not at a fixed chars-per-line), so the body started
        # too high and crowded the heading.
        head_h = text_height(head, hw, head_sz, bold=True,
                             line_spacing=1.05) + Inches(0.08)
        textbox(s, x + Inches(0.62), y + Inches(0.22), hw,
                head_h, head, head_sz, color=INK, bold=True, line=1.05)
        # follow the actual heading height — a fixed floor stranded a gap
        # under short headings
        body_y = Inches(0.22) + head_h + Inches(0.12)
        body = [detail] + ([extra] if extra else [])
        tb = textbox(s, x + Inches(0.22), y + body_y, cw - Inches(0.44),
                     ch - body_y - Inches(0.14), body, 11.5, color=GREY,
                     line=1.18, space_after=4)
        # Body stays top-anchored under the heading. Centring it in a tall
        # card strands a visible void between heading and body.
    add_footer(s, n)
    return s


# ------------------------------------------------------------- process map
def process(prs, title, steps, n, kicker=None, accent=BLUE, note=None):
    """steps: list of (label, detail). Horizontal chevron process map."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    k = len(steps)
    gap = Inches(0.13)
    w = (CW - gap * (k - 1)) / k
    lab_sz = 13 if k <= 4 else (12 if k == 5 else 11)
    det_sz = 10 if k <= 4 else (9.5 if k == 5 else 9)
    y = top + Inches(0.42)
    room = Inches(6.90) - y - (Inches(1.05) if note else Inches(0))

    # A PENTAGON's arrow point is inset by a fraction of its HEIGHT, so the
    # usable flat width depends on h — a constant pad_r let text run into the
    # point. Solve height and width together, sizing from the shared
    # measurement helpers rather than a private heuristic.
    def _fit(l_sz, d_sz, h_guess):
        inset = min(h_guess * 0.5, w * 0.25)          # pentagon point inset
        tw = w - inset - Inches(0.26)                 # + inner padding
        if tw < Inches(0.60):
            tw = Inches(0.60)
        # Size the label band for the TALLEST label measured at the NARROWEST
        # width any step will use, PLUS one spare line. The wrap estimate is a
        # model: one line generous costs a little space, one line short prints
        # the title over the body.
        lh = max(text_height(a, tw, l_sz, bold=True, line_spacing=1.04)
                 for a, _b in steps) + int(l_sz * 1.04 * 1.35 * 12700)
        dh = max(text_height(b, tw, d_sz, line_spacing=1.14)
                 for _a, b in steps)
        return Inches(0.34) + lh + Inches(0.08) + dh + Inches(0.14), lh, tw

    # iterate: height feeds the inset, which feeds the width, which feeds height
    h = Inches(1.62)
    for _ in range(6):
        need_h, lab_h, tw_c = _fit(lab_sz, det_sz, h)
        new_h = max(Inches(1.62), min(need_h, room))
        if abs(new_h - h) < Inches(0.02):
            h = new_h
            break
        h = new_h
    # narrow chevrons (5-6 steps) wrap more, so let the band use the room a
    # note box would otherwise reserve before resorting to shrinking type
    if k >= 5 and need_h > room:
        room = Inches(6.90) - y - (Inches(0.92) if note else Inches(0))
    # if it still does not fit the room, shrink type instead of clipping
    while need_h > room and det_sz > 8.0:
        det_sz -= 0.5
        if lab_sz > 10.0:
            lab_sz -= 0.5
        need_h, lab_h, tw_c = _fit(lab_sz, det_sz, h)
    h = max(Inches(1.62), min(max(need_h, h), room))
    _n2, lab_h, tw_c = _fit(lab_sz, det_sz, h)
    lab_y = Inches(0.34)
    det_y = lab_y + lab_h + Inches(0.08)
    for i, (lab, det) in enumerate(steps):
        c = accent_for(i)
        shp = MSO_SHAPE.PENTAGON if i < k - 1 else MSO_SHAPE.ROUNDED_RECTANGLE
        x = L + i * (w + gap)
        b = box(s, x, y, w, h, fill=tint(c, .88), lineclr=c, shape=shp)
        # every step uses the SAME (narrowest) text width the band was
        # measured at — giving the last shape extra width would let its title
        # wrap differently than the reserved label band allows
        tw_i = tw_c
        textbox(s, x + Inches(0.14), y + Inches(0.11), tw_i,
                Inches(0.22), f"STEP {i+1}", 9, color=c, bold=True)
        textbox(s, x + Inches(0.14), y + lab_y, tw_i,
                lab_h, lab, lab_sz, color=INK, bold=True, line=1.04)
        textbox(s, x + Inches(0.14), y + det_y, tw_i,
                h - det_y - Inches(0.08), det, det_sz, color=GREY, line=1.14)
    if note:
        ny = min(y + h + Inches(0.24), Inches(6.06))
        box(s, L, ny, CW, Inches(0.82), fill=tint(TEAL, .90), lineclr=TEAL)
        box(s, L, ny, Inches(0.065), Inches(0.86), fill=TEAL,
            shape=MSO_SHAPE.RECTANGLE)
        textbox(s, L + Inches(0.24), ny + Inches(0.10), CW - Inches(0.5),
                Inches(0.68), note, 12.5, color=INK, line=1.2)
    add_footer(s, n)
    return s


# ------------------------------------------------------------ two-column
def compare(prs, title, left, right, n, kicker=None,
            lc=BLUE, rc=VIOLET, footer_note=None):
    """left/right: (heading, subtitle, [rows])."""
    s = blank(prs)
    top = title_bar(s, title, kicker, lc)
    gap = Inches(0.30)
    w = (CW - gap) / 2
    # reserve enough for the 0.72in note band plus its 0.16in offset
    h = Inches(7.02) - top - (Inches(1.10) if footer_note else Inches(0.10))
    for (head, sub, rows), c, x in ((left, lc, L), (right, rc, L + w + gap)):
        box(s, x, top, w, h, fill=WHITE, lineclr=LINE)
        box(s, x, top, w, Inches(0.86), fill=c, shape=MSO_SHAPE.RECTANGLE)
        textbox(s, x + Inches(0.24), top + Inches(0.12), w - Inches(0.48),
                Inches(0.36), head, 16, color=WHITE, bold=True)
        textbox(s, x + Inches(0.24), top + Inches(0.50), w - Inches(0.48),
                Inches(0.30), sub, 10.5, color=WHITE)
        # advance by each bullet's wrapped height so the last row is never
        # sliced by the card edge
        bw = w - Inches(0.78)
        nrows = max(len(rows), 1)
        bsz = 12 if nrows <= 6 else 11
        cpl_b = max(int(bw / Inches(0.084 * bsz / 12)), 10)
        blines = [max(1, -(-len(str(r)) // cpl_b)) for r in rows]
        lh_b = Inches(0.19 * bsz / 12)
        gap_b = Inches(0.16)
        avail_b = h - Inches(1.18)
        need_b = sum(bl * lh_b for bl in blines) + gap_b * nrows
        sq_b = min(1.0, avail_b / need_b) if need_b > 0 else 1.0
        y = top + Inches(1.06)
        for row, bl in zip(rows, blines):
            rh = bl * lh_b * sq_b
            box(s, x + Inches(0.24), y + Inches(0.07), Inches(0.16), Inches(0.16),
                fill=c, shape=MSO_SHAPE.OVAL)
            textbox(s, x + Inches(0.52), y - Inches(0.04), bw,
                    rh + Inches(0.14), row, bsz, color=INK, line=1.14)
            y += rh + gap_b * sq_b
    if footer_note:
        ny = top + h + Inches(0.16)
        box(s, L, ny, CW, Inches(0.72), fill=LIGHT, lineclr=LINE)
        box(s, L, ny, Inches(0.065), Inches(0.72), fill=TEAL,
            shape=MSO_SHAPE.RECTANGLE)
        textbox(s, L + Inches(0.24), ny + Inches(0.08), CW - Inches(0.5),
                Inches(0.56), footer_note, 12, color=INK, line=1.18)
    add_footer(s, n)
    return s


# ---------------------------------------------------------------- matrix 2x2
def matrix2x2(prs, title, xlab, ylab, quads, n, kicker=None, accent=BLUE,
              note=None):
    """quads: 4 x (name, detail, colour) ordered TL, TR, BL, BR."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    size = Inches(4.36)
    ox, oy = Inches(2.55), top + Inches(0.18)
    half = size / 2
    order = [(0, 0), (1, 0), (0, 1), (1, 1)]
    # measure the quadrant titles: a fixed title box let a 3-line name print
    # straight over the detail beneath it
    qw = half - Inches(0.32)
    name_sz = 14
    while name_sz > 10 and max(
            text_height(q[0], qw, name_sz, bold=True, line_spacing=1.05)
            for q in quads) > Inches(0.86):
        name_sz -= 0.5
    nh = max(text_height(q[0], qw, name_sz, bold=True, line_spacing=1.05)
             for q in quads)
    det_top = Inches(0.14) + nh + Inches(0.10)
    det_sz = 11
    while det_sz > 8.5 and max(
            text_height(q[1], qw, det_sz, line_spacing=1.18)
            for q in quads) > half - det_top - Inches(0.14):
        det_sz -= 0.5
    for i, (name, det, c) in enumerate(quads):
        cx, cy = order[i]
        x, y = ox + cx * half, oy + cy * half
        box(s, x, y, half, half, fill=tint(c, .88), lineclr=c)
        textbox(s, x + Inches(0.16), y + Inches(0.14), qw,
                nh, name, name_sz, color=c, bold=True, line=1.05)
        textbox(s, x + Inches(0.16), y + det_top, qw,
                half - det_top - Inches(0.12), det, det_sz, color=INK,
                line=1.18)
    textbox(s, ox, oy + size + Inches(0.10), size, Inches(0.32), xlab, 12,
            color=GREY, bold=True, align=PP_ALIGN.CENTER)
    tb = textbox(s, ox - Inches(2.05), oy + half - Inches(0.20), Inches(1.9),
                 Inches(0.4), ylab, 12, color=GREY, bold=True,
                 align=PP_ALIGN.RIGHT)
    if note:
        box(s, Inches(7.20), oy + Inches(0.10), Inches(5.5), Inches(1.0),
            fill=LIGHT, lineclr=LINE)
        textbox(s, Inches(7.42), oy + Inches(0.22), Inches(5.1), Inches(0.8),
                note, 11.5, color=INK, line=1.2)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------- table
def table(prs, title, headers, rows, n, kicker=None, accent=BLUE,
          widths=None, note=None):
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    nr, nc = len(rows) + 1, len(headers)
    avail = Inches(6.92) - top - (Inches(0.86) if note else Inches(0))
    # grow rows to use the slide rather than stranding whitespace below
    h = min(avail, max(Inches(0.52) * nr, Inches(0.44) * nr + Inches(0.18)))
    gf = s.shapes.add_table(nr, nc, L, top, CW, h)
    t = gf.table
    if widths:
        tot = sum(widths)
        for i, w in enumerate(widths):
            t.columns[i].width = int(CW * w / tot)
    for j, htxt in enumerate(headers):
        c = t.cell(0, j)
        c.text = ""
        c.fill.solid()
        c.fill.fore_color.rgb = accent
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        _tf(c, htxt, 11.5, color=WHITE, bold=True, space_after=0)
    for i, row in enumerate(rows, 1):
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.text = ""
            c.fill.solid()
            c.fill.fore_color.rgb = WHITE if i % 2 else LIGHT
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            _tf(c, str(val), 10.5, color=INK if j == 0 else GREY,
                bold=(j == 0), space_after=0, line=1.10)
    if note:
        ny = top + h + Inches(0.18)
        if ny < Inches(6.60):
            box(s, L, ny, CW, Inches(0.62), fill=tint(accent, .92),
                lineclr=accent)
            textbox(s, L + Inches(0.22), ny + Inches(0.08), CW - Inches(0.44),
                    Inches(0.48), note, 11.5, color=INK, line=1.16)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------- chart
def chart(prs, title, kind, cats, series, n, kicker=None, accent=BLUE,
          insight=None, ymax=None):
    """kind: 'bar' | 'column' | 'line' | 'pie' | 'pareto'."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    cw = Inches(8.05) if insight else CW
    ch = Inches(4.86)
    cd = CategoryChartData()
    cd.categories = cats
    for name, vals in series:
        cd.add_series(name, vals)
    kmap = {
        "bar": XL_CHART_TYPE.BAR_CLUSTERED,
        "column": XL_CHART_TYPE.COLUMN_CLUSTERED,
        "line": XL_CHART_TYPE.LINE_MARKERS,
        "pie": XL_CHART_TYPE.PIE,
        "pareto": XL_CHART_TYPE.COLUMN_CLUSTERED,
        "scatter": XL_CHART_TYPE.XY_SCATTER,
        "area": XL_CHART_TYPE.AREA,
    }
    gf = s.shapes.add_chart(kmap[kind], L, top, cw, ch, cd)
    ch_o = gf.chart
    ch_o.font.size = Pt(11)
    ch_o.font.name = FONT
    ch_o.font.color.rgb = GREY
    if kind == "pie":
        ch_o.has_legend = True
        ch_o.legend.position = XL_LEGEND_POSITION.RIGHT
        ch_o.legend.include_in_layout = False
    else:
        ch_o.has_legend = len(series) > 1
        if ch_o.has_legend:
            ch_o.legend.position = XL_LEGEND_POSITION.BOTTOM
            ch_o.legend.include_in_layout = False
        try:
            va = ch_o.value_axis
            va.has_major_gridlines = True
            va.format.line.color.rgb = LINE
            if ymax:
                va.maximum_scale = ymax
            # all-negative (or all-positive) series render off-plot under the
            # default auto axis — anchor the axis so the bars are visible
            # NOTE: do not pin minimum/maximum_scale here. Setting explicit
            # bounds on a BAR_CLUSTERED value axis makes LibreOffice drop the
            # bars entirely (verified: same data renders with auto bounds).
            # Charts needing a fixed ceiling pass ymax explicitly instead.
            ch_o.category_axis.format.line.color.rgb = LINE
        except Exception:
            pass
    # colour the series
    try:
        for si, plot_ser in enumerate(ch_o.series):
            if kind == "pie":
                for pi, pt in enumerate(plot_ser.points):
                    pt.format.fill.solid()
                    pt.format.fill.fore_color.rgb = accent_for(pi)
            elif kind == "line":
                plot_ser.format.line.color.rgb = accent_for(si)
                plot_ser.format.line.width = Pt(2.5)
            else:
                plot_ser.format.fill.solid()
                plot_ser.format.fill.fore_color.rgb = accent_for(si)
    except Exception:
        pass
    if insight:
        x = L + cw + Inches(0.28)
        w = R - x
        box(s, x, top, w, ch, fill=LIGHT, lineclr=LINE)
        box(s, x, top, w, Inches(0.075), fill=accent, shape=MSO_SHAPE.RECTANGLE)
        textbox(s, x + Inches(0.22), top + Inches(0.28), w - Inches(0.44),
                Inches(0.32), "WHAT IT TELLS YOU", 10.5, color=accent, bold=True)
        # advance by wrapped height so long insights don't stack on each other
        iw = w - Inches(0.74)
        cpl = max(int(iw / Inches(0.095)), 8)
        est = [max(1, -(-len(str(it)) // cpl)) for it in insight]
        lh = Inches(0.205)
        gap_i = Inches(0.20)
        avail_i = ch - Inches(0.82)
        need_i = sum(e * lh for e in est) + gap_i * len(insight)
        sq = min(1.0, avail_i / need_i) if need_i > 0 else 1.0
        isz = 11.5 if sq > 0.92 else (10.5 if sq > 0.80 else 9.5)
        y = top + Inches(0.70)
        for it, e in zip(insight, est):
            ih = e * lh * sq
            box(s, x + Inches(0.24), y + Inches(0.06), Inches(0.14),
                Inches(0.14), fill=accent, shape=MSO_SHAPE.OVAL)
            textbox(s, x + Inches(0.50), y - Inches(0.04), iw,
                    ih + Inches(0.14), it, isz, color=INK, line=1.16)
            y += ih + gap_i * sq
    add_footer(s, n)
    return s


# ------------------------------------------------------------- big statement
def statement(prs, title, big, support, n, kicker=None, accent=BLUE):
    s = blank(prs)
    box(s, Inches(0), Inches(0), Inches(13.333), Inches(0.10), fill=accent,
        shape=MSO_SHAPE.RECTANGLE)
    if kicker:
        textbox(s, L, Inches(1.10), Inches(11.9), Inches(0.32),
                kicker.upper(), 13, color=accent, bold=True)
    textbox(s, L, Inches(1.52), Inches(11.9), Inches(0.52), title, 20,
            color=GREY, bold=True)
    # Measure the headline rather than guessing: the rule must sit UNDER the
    # last line, never through it.
    big_w = Inches(11.9)
    big_top = Inches(1.98)
    rule_max = Inches(4.44)          # the rule must clear the support cards
    # the headline shrinks until it fits ABOVE the rule, so the rule can
    # never be forced through the text by a clamp
    budget = rule_max - big_top - Inches(0.22)
    big_sz = fit_size(big, big_w, budget, 40, min_pt=20, bold=True,
                      line_spacing=1.10)
    big_h = min(text_height(big, big_w, big_sz, bold=True, line_spacing=1.10),
                budget)
    textbox(s, L, big_top, big_w, big_h, big, big_sz,
            color=INK, bold=True, line=1.10)
    box(s, L, big_top + big_h + Inches(0.20), Inches(2.4), Inches(0.055),
        fill=accent, shape=MSO_SHAPE.RECTANGLE)
    gap, cols = Inches(0.26), len(support)
    w = (CW - gap * (cols - 1)) / cols
    for i, (h, d) in enumerate(support):
        x = L + i * (w + gap)
        c = accent_for(i)
        box(s, x, Inches(4.72), w, Inches(1.62), fill=tint(c, .90), lineclr=c)
        textbox(s, x + Inches(0.20), Inches(4.86), w - Inches(0.40),
                Inches(0.40), h, 14, color=c, bold=True, line=1.04)
        textbox(s, x + Inches(0.20), Inches(5.32), w - Inches(0.40),
                Inches(0.92), d, 11.5, color=INK, line=1.18)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ timeline
def timeline(prs, title, phases, n, kicker=None, accent=BLUE, note=None):
    """phases: list of (label, detail). Horizontal milestone track."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    # the rail sits far enough down that a two-line label above it still
    # clears the title rule
    y = top + Inches(1.62)
    box(s, L, y, CW, Inches(0.075), fill=LINE, shape=MSO_SHAPE.RECTANGLE)
    k = len(phases)
    step = CW / k
    for i, (lab, det) in enumerate(phases):
        c = accent_for(i)
        cx = L + step * i + step / 2
        box(s, cx - Inches(0.22), y - Inches(0.17), Inches(0.44), Inches(0.44),
            fill=c, shape=MSO_SHAPE.OVAL)
        textbox(s, cx - Inches(0.22), y - Inches(0.12), Inches(0.44),
                Inches(0.36), str(i + 1), 13, color=WHITE, bold=True,
                align=PP_ALIGN.CENTER)
        # clear the rail and the node circle in both directions, so a
        # two-line entry never renders behind the timeline
        up = i % 2 == 0
        # measure the label so a 2-line phase name cannot print over its
        # detail, and so neither can reach back to the rail
        lw = step - Inches(0.20)
        lh_t = text_height(lab, lw, 13.5, bold=True, line_spacing=1.05)
        dh_t = text_height(det, lw, 10.5, line_spacing=1.16)
        blk = lh_t + Inches(0.08) + dh_t
        # never let an upward block reach back above the title rule
        ty = max(top + Inches(0.16), y - Inches(0.30) - blk) if up \
            else y + Inches(0.46)
        textbox(s, cx - step / 2 + Inches(0.10), ty, lw,
                lh_t, lab, 13.5, color=INK, bold=True,
                align=PP_ALIGN.CENTER, line=1.05)
        textbox(s, cx - step / 2 + Inches(0.10), ty + lh_t + Inches(0.08),
                lw, dh_t, det, 10.5, color=GREY,
                align=PP_ALIGN.CENTER, line=1.16)
    if note:
        ny = Inches(5.55)
        box(s, L, ny, CW, Inches(0.86), fill=tint(accent, .92), lineclr=accent)
        box(s, L, ny, Inches(0.065), Inches(0.86), fill=accent,
            shape=MSO_SHAPE.RECTANGLE)
        textbox(s, L + Inches(0.24), ny + Inches(0.11), CW - Inches(0.5),
                Inches(0.64), note, 12.5, color=INK, line=1.2)
    add_footer(s, n)
    return s


# -------------------------------------------------------------- ITTO slide
def itto(prs, title, inputs, tools, outputs, n, kicker="ITTO", purpose=None):
    """Inputs / Tools & Techniques / Outputs -- the PMP process anatomy."""
    s = blank(prs)
    top = title_bar(s, title, kicker, BLUE)
    if purpose:
        box(s, L, top, CW, Inches(0.62), fill=LIGHT, lineclr=LINE)
        box(s, L, top, Inches(0.065), Inches(0.62), fill=AMBER,
            shape=MSO_SHAPE.RECTANGLE)
        textbox(s, L + Inches(0.24), top + Inches(0.09), CW - Inches(0.5),
                Inches(0.48), purpose, 12, color=INK, line=1.16)
        top += Inches(0.80)
    cols = [("INPUTS", inputs, BLUE), ("TOOLS & TECHNIQUES", tools, VIOLET),
            ("OUTPUTS", outputs, TEAL)]
    gap = Inches(0.52)
    w = (CW - gap * 2) / 3
    h = Inches(6.96) - top
    for i, (head, items, c) in enumerate(cols):
        x = L + i * (w + gap)
        box(s, x, top, w, h, fill=WHITE, lineclr=LINE)
        box(s, x, top, w, Inches(0.62), fill=c, shape=MSO_SHAPE.RECTANGLE)
        textbox(s, x + Inches(0.18), top + Inches(0.15), w - Inches(0.36),
                Inches(0.36), head, 12.5, color=WHITE, bold=True,
                align=PP_ALIGN.CENTER)
        # advance by the wrapped height of each item so long entries never
        # overlap the one below (ITTO inputs/outputs are often 2-3 lines)
        # measured sizing via the shared helper — the private heuristic this
        # replaces let 2-3 line entries touch the bullet below them
        avail_h = h - Inches(0.94)
        tw = w - Inches(0.64)
        base_gap = Inches(0.13)
        sz = 11.0
        while sz > 8.5:
            heights = [text_height(it, tw, sz, line_spacing=1.12)
                       for it in items]
            if sum(heights) + base_gap * len(items) <= avail_h:
                break
            sz -= 0.5
        heights = [text_height(it, tw, sz, line_spacing=1.12) for it in items]
        y = top + Inches(0.80)
        for it, ih in zip(items, heights):
            box(s, x + Inches(0.20), y + Inches(0.06), Inches(0.13),
                Inches(0.13), fill=c, shape=MSO_SHAPE.OVAL)
            textbox(s, x + Inches(0.44), y - Inches(0.04), tw,
                    ih, it, sz, color=INK, line=1.12)
            y += ih + base_gap
        if i < 2:
            ax = x + w + Inches(0.10)
            box(s, ax, top + h / 2 - Inches(0.16), Inches(0.32), Inches(0.32),
                fill=tint(c, .70), shape=MSO_SHAPE.CHEVRON)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ activity
def activity(prs, title, brief, steps, deliver, n, tool=None, url=None,
             accent=TEAL, duration=None):
    """Information-dense activity slide: brief + numbered steps + output."""
    s = blank(prs)
    top = title_bar(s, title, "HANDS-ON ACTIVITY", accent)
    # brief band
    box(s, L, top, CW, Inches(0.78), fill=tint(accent, .90), lineclr=accent)
    box(s, L, top, Inches(0.065), Inches(0.78), fill=accent,
        shape=MSO_SHAPE.RECTANGLE)
    textbox(s, L + Inches(0.24), top + Inches(0.10), Inches(9.1), Inches(0.60),
            brief, 12.5, color=INK, line=1.18)
    if duration:
        box(s, Inches(10.60), top + Inches(0.14), Inches(2.0), Inches(0.50),
            fill=accent)
        textbox(s, Inches(10.60), top + Inches(0.24), Inches(2.0), Inches(0.32),
                duration, 12, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    y = top + Inches(0.98)
    # steps grid 2 cols
    gap = Inches(0.26)
    w = (CW - gap) / 2
    rows = (len(steps) + 1) // 2
    hh = (Inches(5.66) - y) / max(rows, 1) - Inches(0.12)
    # Fit the step text to the tile by SHRINKING TYPE when the tile cannot
    # grow — a height cap alone clipped the last line.
    _sw = w - Inches(0.76)
    st_sz = 11.5
    _lines = 1
    if steps:
        while st_sz > 8.0:
            _cpl = max(int(_sw / Inches(0.084 * st_sz / 11.5)), 8)
            _lines = max(max(1, -(-len(str(st)) // _cpl)) for st in steps) + 1
            if Inches(0.185 * st_sz / 11.5) * _lines <= hh - Inches(0.16):
                break
            st_sz -= 0.5
    for i, st in enumerate(steps):
        r, c = divmod(i, 2)
        x = L + c * (w + gap)
        yy = y + r * (hh + Inches(0.12))
        col = accent_for(i)
        box(s, x, yy, w, hh, fill=LIGHT, lineclr=LINE)
        box(s, x, yy, Inches(0.055), hh, fill=col, shape=MSO_SHAPE.RECTANGLE)
        box(s, x + Inches(0.18), yy + Inches(0.15), Inches(0.30), Inches(0.30),
            fill=col, shape=MSO_SHAPE.OVAL)
        textbox(s, x + Inches(0.18), yy + Inches(0.19), Inches(0.30),
                Inches(0.26), str(i + 1), 11, color=WHITE, bold=True,
                align=PP_ALIGN.CENTER)
        textbox(s, x + Inches(0.58), yy + Inches(0.08), _sw,
                hh - Inches(0.16), st, st_sz, color=INK, line=1.14,
                anchor=MSO_ANCHOR.MIDDLE)
    # deliverable + tool
    dy = Inches(5.80)
    box(s, L, dy, Inches(8.30), Inches(1.02), fill=WHITE, lineclr=TEAL, linew=1.5)
    textbox(s, L + Inches(0.24), dy + Inches(0.10), Inches(7.9), Inches(0.28),
            "DELIVERABLE", 10, color=TEAL, bold=True)
    textbox(s, L + Inches(0.24), dy + Inches(0.38), Inches(7.9), Inches(0.56),
            deliver, 12, color=INK, line=1.16)
    if tool:
        box(s, Inches(9.20), dy, Inches(3.51), Inches(1.02), fill=tint(VIOLET, .90),
            lineclr=VIOLET)
        textbox(s, Inches(9.42), dy + Inches(0.10), Inches(3.1), Inches(0.28),
                "TOOL", 10, color=VIOLET, bold=True)
        textbox(s, Inches(9.42), dy + Inches(0.36), Inches(3.1), Inches(0.28),
                tool, 12, color=INK, bold=True)
        if url:
            textbox(s, Inches(9.42), dy + Inches(0.64), Inches(3.1), Inches(0.28),
                    url, 8.5, color=GREY)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ formula
def formula(prs, title, items, n, kicker="KEY FORMULAS", accent=AMBER,
            note=None):
    """items: (name, formula, reading)."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    # clamp row height so 5+ formulas never run past the footer at 7.02in
    reserve = Inches(0.80) if note else Inches(0)
    nrow = max(len(items), 1)
    gap_r = Inches(0.14) if nrow <= 5 else Inches(0.08)
    h = min(Inches(1.06), (Inches(6.92) - top - reserve) / nrow - gap_r)
    # never let the row shrink below the 2-line height the right-hand gloss
    # needs — at 6 rows the gloss was being clipped on every row
    h = max(h, Inches(0.62))

    # EVERY child derives from the row height. Fixed-size children inside a
    # clamped container is what made the chip overhang the card and the
    # gloss escape it.
    chip_h = min(Inches(0.68), h - Inches(0.16))
    chip_y = (h - chip_h) / 2
    gw = Inches(4.35)
    gloss_sz = 11.5 if nrow <= 5 else 10
    gl_need = max(max(1, -(-len(str(r)) // 46)) for _n2, _f2, r in items)
    while (Inches(0.185 * gloss_sz / 11.5) * gl_need) > (h - Inches(0.16)) \
            and gloss_sz > 8.0:
        gloss_sz -= 0.5
    name_sz = 14 if h >= Inches(0.80) else 12
    f_sz = 15 if chip_h >= Inches(0.60) else 13

    y = top
    for i, (name, f, reading) in enumerate(items):
        c = accent_for(i)
        box(s, L, y, CW, h, fill=WHITE, lineclr=LINE)
        box(s, L, y, Inches(0.065), h, fill=c, shape=MSO_SHAPE.RECTANGLE)
        textbox(s, L + Inches(0.26), y + Inches(0.08), Inches(3.5),
                h - Inches(0.16), name, name_sz, color=INK, bold=True,
                line=1.04, anchor=MSO_ANCHOR.MIDDLE)
        box(s, L + Inches(3.90), y + chip_y, Inches(3.55), chip_h,
            fill=tint(c, .88), lineclr=c)
        tbf = textbox(s, L + Inches(3.98), y + chip_y, Inches(3.4),
                      chip_h, f, f_sz, color=c, bold=True,
                      align=PP_ALIGN.CENTER)
        tbf.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        textbox(s, L + Inches(7.70), y + Inches(0.08), gw,
                h - Inches(0.16), reading, gloss_sz, color=GREY, line=1.12,
                anchor=MSO_ANCHOR.MIDDLE)
        y += h + gap_r
    if note:
        box(s, L, y, CW, Inches(0.66), fill=tint(accent, .90), lineclr=accent)
        textbox(s, L + Inches(0.24), y + Inches(0.10), CW - Inches(0.5),
                Inches(0.50), note, 11.5, color=INK, line=1.16)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ exam tip
def exam(prs, title, traps, n, kicker="EXAM FOCUS", accent=ROSE):
    """traps: (question_cue, what_pmi_wants)."""
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    nt = max(len(traps), 1)
    gap_t = Inches(0.14) if nt <= 4 else Inches(0.09)
    band = Inches(6.94) - top
    h = band / nt - gap_t
    cue_w, ans_w = Inches(5.7), Inches(5.25)
    # size from the MEASURED wrap, then grow the row to the height the text
    # actually needs so a 2-line answer is never cut against the footer
    txt_sz = 11.5
    if traps:
        need = max(
            max(text_height(c, cue_w, txt_sz, line_spacing=1.12)
                for c, _w in traps),
            max(text_height(wv, ans_w, txt_sz, line_spacing=1.12)
                for _c, wv in traps))
        while need + Inches(0.52) > h and txt_sz > 9.0:
            txt_sz -= 0.5
            need = max(
                max(text_height(c, cue_w, txt_sz, line_spacing=1.12)
                    for c, _w in traps),
                max(text_height(wv, ans_w, txt_sz, line_spacing=1.12)
                    for _c, wv in traps))
        h = min(max(h, need + Inches(0.52)), band / nt - Inches(0.06))
        # keep the whole band clear of the footer rule at 7.02in
        total = h * nt + gap_t * (nt - 1)
        if top + total > Inches(6.86):
            h = (Inches(6.86) - top - gap_t * (nt - 1)) / nt
    y = top
    for i, (cue, want) in enumerate(traps):
        c = accent_for(i)
        box(s, L, y, CW, h, fill=WHITE, lineclr=LINE)
        box(s, L, y, Inches(0.065), h, fill=c, shape=MSO_SHAPE.RECTANGLE)
        box(s, L + Inches(0.26), y + Inches(0.16), Inches(5.6), Inches(0.30),
            fill=tint(c, .88), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        textbox(s, L + Inches(0.36), y + Inches(0.18), Inches(5.4),
                Inches(0.28), "IF THE QUESTION SAYS", 9, color=c, bold=True)
        textbox(s, L + Inches(0.30), y + Inches(0.48), Inches(5.7),
                h - Inches(0.54), cue, txt_sz, color=INK, line=1.12)
        box(s, L + Inches(6.30), y + Inches(0.16), Inches(0.30), Inches(0.30),
            fill=c, shape=MSO_SHAPE.CHEVRON)
        textbox(s, L + Inches(6.84), y + Inches(0.18), Inches(5.2),
                Inches(0.28), "THE BEST ANSWER IS", 9, color=TEAL, bold=True)
        textbox(s, L + Inches(6.84), y + Inches(0.48), Inches(5.25),
                h - Inches(0.54), want, txt_sz, color=INK, line=1.12)
        y += h + gap_t
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ recap
def recap(prs, title, points, n, kicker="RECAP", accent=CYAN):
    s = blank(prs)
    top = title_bar(s, title, kicker, accent)
    gap = Inches(0.24)
    cols = 2
    w = (CW - gap) / cols
    rows = (len(points) + 1) // 2
    gap_v = Inches(0.12)
    bw = w - Inches(0.80)
    # size the card from the MEASURED head + body, with a safety line, then
    # cap it to the space available
    need = max(text_height(hd, bw, 13, bold=True, line_spacing=1.04)
               + Inches(0.10)
               + text_height(dt, bw, 11, line_spacing=1.16)
               for hd, dt in points) + Inches(0.30)
    room = (Inches(6.92) - top) / max(rows, 1) - gap_v
    body_sz = 11.0
    while need > room and body_sz > 9.0:
        body_sz -= 0.5
        need = max(text_height(hd, bw, 13, bold=True, line_spacing=1.04)
                   + Inches(0.10)
                   + text_height(dt, bw, body_sz, line_spacing=1.16)
                   for hd, dt in points) + Inches(0.30)
    h = min(max(need, Inches(1.00)), room)
    # a two-digit index needs a wider chip than a one-digit one
    chip_w = Inches(0.32) if len(points) < 10 else Inches(0.42)
    for i, (head, det) in enumerate(points):
        r, c = divmod(i, cols)
        x = L + c * (w + gap)
        y = top + r * (h + gap_v)
        col = accent_for(i)
        box(s, x, y, w, h, fill=LIGHT, lineclr=LINE)
        box(s, x, y, Inches(0.055), h, fill=col, shape=MSO_SHAPE.RECTANGLE)
        box(s, x + Inches(0.18), y + Inches(0.15), chip_w, Inches(0.32),
            fill=col, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.5)
        tbn = textbox(s, x + Inches(0.18), y + Inches(0.15), chip_w,
                      Inches(0.32), str(i + 1), 11, color=WHITE, bold=True,
                      align=PP_ALIGN.CENTER)
        tbn.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        hx = x + Inches(0.24) + chip_w
        hh = text_height(head, bw, 13, bold=True, line_spacing=1.04)
        textbox(s, hx, y + Inches(0.12), w - (hx - x) - Inches(0.18),
                hh, head, 13, color=INK, bold=True, line=1.04)
        textbox(s, hx, y + Inches(0.12) + hh + Inches(0.06),
                w - (hx - x) - Inches(0.18),
                h - Inches(0.30) - hh, det, body_sz, color=GREY, line=1.16)
    add_footer(s, n)
    return s


# ------------------------------------------------------------------ break
def break_slide(prs, label, sub, n, accent=AMBER):
    s = blank(prs)
    box(s, Inches(0), Inches(0), Inches(13.333), Inches(7.5),
        fill=tint(accent, .93), shape=MSO_SHAPE.RECTANGLE)
    box(s, Inches(0), Inches(0), Inches(13.333), Inches(0.14), fill=accent,
        shape=MSO_SHAPE.RECTANGLE)
    textbox(s, Inches(0.62), Inches(2.90), Inches(12.1), Inches(1.0), label,
            50, color=INK, bold=True, align=PP_ALIGN.CENTER)
    textbox(s, Inches(0.62), Inches(4.00), Inches(12.1), Inches(0.5), sub,
            17, color=GREY, align=PP_ALIGN.CENTER)
    add_footer(s, n)
    return s
