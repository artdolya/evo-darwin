"""Renders docs/assets/sdlc-phases.gif, the animation of the phase diagram in docs/SDLC.md.

The Mermaid diagram in docs/SDLC.md is the source. This script holds its own copy of the
phases, the arrows and the labels: PHASES, FORWARD and RETURNS below. When the diagram
changes, change them here too and render the animation again.

Needs Python 3 and the Pillow package. Uses the Ubuntu font, or DejaVu Sans without it.

    python docs/assets/sdlc-phases.py docs/assets/sdlc-phases.gif
    python docs/assets/sdlc-phases.py frame.png --still 2.5    one frame, at 2.5 seconds
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 2  # supersampling factor
W, H = 1200, 580
FRAME_MS = 50

FONT_DIR = "/usr/share/fonts/truetype"
FONTS = [  # (regular, italic, variable font). The first one that is installed is used.
    (f"{FONT_DIR}/ubuntu/Ubuntu[wdth,wght].ttf", f"{FONT_DIR}/ubuntu/Ubuntu-Italic[wdth,wght].ttf", True),
    (f"{FONT_DIR}/dejavu/DejaVuSans.ttf", f"{FONT_DIR}/dejavu/DejaVuSans-Oblique.ttf", False),
]

BG = "#0b1220"
GRID = "#141d33"
CARD = "#162035"
CARD_BORDER = "#334155"
LINE = "#475569"
RETURN = "#64748b"
TEXT = "#cbd5e1"
MUTED = "#8492a6"
WHITE = "#ffffff"

PHASES = [
    (["Discovery"], "#38bdf8"),
    (["Architecture", "and design"], "#818cf8"),
    (["Planning"], "#a78bfa"),
    (["Implementation"], "#e879f9"),
    (["Verification"], "#fb7185"),
    (["Release"], "#fb923c"),
    (["Operation and", "maintenance"], "#fbbf24"),
]
LAST = len(PHASES) - 1

# ---- layout (1x coordinates) ------------------------------------------------
# Phases 1 to 4 are the top row, left to right. Phases 5 to 7 are the bottom row, right to left.
CW, CH = 200, 92
COLS = [170, 432, 694, 956]
TOP, BOTTOM = 200, 440
XC = [x + CW / 2 for x in COLS]
YT, YB = TOP + CH / 2, BOTTOM + CH / 2
MID = (TOP + CH + BOTTOM) / 2
# phase index -> (left, top)
POS = [(COLS[0], TOP), (COLS[1], TOP), (COLS[2], TOP), (COLS[3], TOP),
       (COLS[3], BOTTOM), (COLS[2], BOTTOM), (COLS[1], BOTTOM)]
IDEA = (36, YT - 22, 124, YT + 22)

FORWARD = [  # the connector that leaves phase i (0-based), for every phase but the last
    [(COLS[0] + CW, YT), (COLS[1], YT)],
    [(COLS[1] + CW, YT), (COLS[2], YT)],
    [(COLS[2] + CW, YT), (COLS[3], YT)],
    [(XC[3] + 34, TOP + CH), (XC[3] + 34, BOTTOM)],
    [(COLS[3], YB), (COLS[2] + CW, YB)],
    [(COLS[2], YB), (COLS[1] + CW, YB)],
]
IDEA_LINE = [(IDEA[2], YT), (COLS[0], YT)]

RETURNS = [  # (source phase, corner points, label, label anchor, label align)
    (1, [(XC[1] - 50, TOP), (XC[1] - 50, TOP - 34), (XC[0] + 50, TOP - 34), (XC[0] + 50, TOP)],
     "gap in the DreamContext", ((XC[0] + XC[1]) / 2, TOP - 50), "mm"),
    (3, [(XC[3] - 50, TOP), (XC[3] - 50, TOP - 34), (XC[1] + 50, TOP - 34), (XC[1] + 50, TOP)],
     "gap in the design", ((XC[1] + XC[3]) / 2, TOP - 50), "mm"),
    (3, [(XC[3] + 50, TOP), (XC[3] + 50, TOP - 78), (XC[0] - 50, TOP - 78), (XC[0] - 50, TOP)],
     "trade-off for the Dreamer", ((XC[0] + XC[3]) / 2, TOP - 94), "mm"),
    (4, [(XC[3] - 34, BOTTOM), (XC[3] - 34, TOP + CH)],
     "defect", (XC[3] - 48, MID), "rm"),
    (5, [(XC[2], BOTTOM), (XC[2], TOP + CH)],
     "next release", (XC[2] + 16, MID), "lm"),
    (6, [(COLS[1], YB), (XC[0], YB), (XC[0], TOP + CH)],
     "feedback, new idea", (XC[0] + 16, MID), "lm"),
]
FEEDBACK = 5  # index in RETURNS of the path the main token takes from the last phase to phase 1

# ---- timeline ---------------------------------------------------------------
DWELL, TRAVEL, TRAVEL_BACK, IDEA_TRAVEL = 0.55, 0.40, 0.85, 0.45
ARRIVE = []
_t = 0.0
for _i in range(len(PHASES)):
    ARRIVE.append(_t)
    _t += DWELL + (TRAVEL if _i < LAST else TRAVEL_BACK)
CYCLE = _t
FRAMES = round(CYCLE * 1000 / FRAME_MS)
CYCLE = FRAMES * FRAME_MS / 1000  # make the loop exact


# ---- helpers ----------------------------------------------------------------
def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, k):
    a, b = (rgb(a) if isinstance(a, str) else a), (rgb(b) if isinstance(b, str) else b)
    k = max(0.0, min(1.0, k))
    return tuple(round(a[i] + (b[i] - a[i]) * k) for i in range(3))


def font(size, weight=400, italic=False):
    for regular, slanted, variable in FONTS:
        if not os.path.exists(regular):
            continue
        path = slanted if italic else regular
        if not variable and weight >= 600 and not italic:
            path = regular.replace(".ttf", "-Bold.ttf")
        if not os.path.exists(path):
            path = regular
        f = ImageFont.truetype(path, round(size * S))
        if variable:
            values = []
            for axis in f.get_variation_axes():
                name = axis["name"]
                name = name.decode() if isinstance(name, bytes) else name
                values.append(weight if "eight" in name else axis["default"])
            f.set_variation_by_axes(values)
        return f
    sys.exit("No font found. Install the Ubuntu font or DejaVu Sans, or add a font to FONTS.")


def smooth(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3 - 2 * u)


class Path:
    """A polyline with rounded corners, sampled by arc length."""

    def __init__(self, pts, radius=14):
        out = [pts[0]]
        for i in range(1, len(pts) - 1):
            p0, p1, p2 = pts[i - 1], pts[i], pts[i + 1]
            a = self._toward(p1, p0, radius)
            b = self._toward(p1, p2, radius)
            out.append(a)
            for k in range(1, 12):
                u = k / 12
                out.append(((1 - u) ** 2 * a[0] + 2 * u * (1 - u) * p1[0] + u * u * b[0],
                            (1 - u) ** 2 * a[1] + 2 * u * (1 - u) * p1[1] + u * u * b[1]))
            out.append(b)
        out.append(pts[-1])
        self.pts = out
        self.cum = [0.0]
        for i in range(1, len(out)):
            self.cum.append(self.cum[-1] + math.dist(out[i - 1], out[i]))
        self.length = self.cum[-1]

    @staticmethod
    def _toward(p, q, r):
        d = math.dist(p, q)
        r = min(r, d / 2)
        return (p[0] + (q[0] - p[0]) * r / d, p[1] + (q[1] - p[1]) * r / d)

    def at(self, s):
        s = max(0.0, min(self.length, s))
        lo, hi = 0, len(self.cum) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.cum[mid] <= s:
                lo = mid
            else:
                hi = mid
        seg = self.cum[hi] - self.cum[lo]
        u = 0 if seg == 0 else (s - self.cum[lo]) / seg
        a, b = self.pts[lo], self.pts[hi]
        return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)

    def piece(self, s0, s1, step=3.0):
        n = max(1, math.ceil((s1 - s0) / step))
        return [self.at(s0 + (s1 - s0) * k / n) for k in range(n + 1)]


def sc(p):
    return (p[0] * S, p[1] * S)


def stroke(d, pts, color, width):
    pts = [sc(p) for p in pts]
    d.line(pts, fill=color, width=round(width * S), joint="curve")
    r = width * S / 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=color)


def arrow_head(d, path, color, size=11):
    tip = path.at(path.length)
    back = path.at(path.length - size)
    dx, dy = tip[0] - back[0], tip[1] - back[1]
    n = math.hypot(dx, dy) or 1
    px, py = -dy / n * size * 0.5, dx / n * size * 0.5
    d.polygon([sc(tip), sc((back[0] + px, back[1] + py)), sc((back[0] - px, back[1] - py))], fill=color)


def glow(img, box, radius, color, alpha, blur):
    """Composites a blurred rounded rectangle (1x box) onto img."""
    pad = blur * 3
    x0, y0, x1, y1 = box
    w, h = round((x1 - x0 + 2 * pad) * S), round((y1 - y0 + 2 * pad) * S)
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(
        (pad * S, pad * S, w - pad * S, h - pad * S), radius=radius * S,
        fill=rgb(color) + (round(255 * max(0, min(1, alpha))),))
    layer = layer.filter(ImageFilter.GaussianBlur(blur * S))
    img.alpha_composite(layer, (round((x0 - pad) * S), round((y0 - pad) * S)))


F_TITLE = font(27, 700)
F_SUB = font(15.5, 400)
F_LEGEND = font(14, 500)
F_NUM = font(17, 700)
F_IDEA = font(18, 700)
F_RET = font(14.5, 500, italic=True)

# One card font size for all cards: the largest that fits the longest line.
_avail = CW - 58 - 14
_size = 19.0
while True:
    F_CARD = font(_size, 600)
    if max(F_CARD.getlength(line) for lines, _ in PHASES for line in lines) / S <= _avail:
        break
    _size -= 0.5

FORWARD_PATHS = [Path(p) for p in FORWARD]
IDEA_PATH = Path(IDEA_LINE)
RETURN_PATHS = [Path(r[1], radius=16) for r in RETURNS]
DASH, GAP = 9.0, 7.0
MARCH = round(26 * CYCLE / (DASH + GAP)) * (DASH + GAP) / CYCLE  # px per second, loops exactly


def static_layer():
    img = Image.new("RGBA", (W * S, H * S), rgb(BG) + (255,))
    d = ImageDraw.Draw(img)
    for gx in range(14, W, 28):
        for gy in range(14, H, 28):
            d.ellipse((gx * S - 2, gy * S - 2, gx * S + 2, gy * S + 2), fill=GRID)
    d.text(sc((36, 44)), "Software development life cycle", font=F_TITLE, fill="#f1f5f9", anchor="lm")
    d.text(sc((37, 77)), "Seven phases, from an idea to running software", font=F_SUB, fill=MUTED, anchor="lm")
    # legend
    lx = 936
    stroke(d, [(lx, 40), (lx + 38, 40)], "#94a3b8", 2.5)
    d.polygon([sc((lx + 46, 40)), sc((lx + 36, 35)), sc((lx + 36, 45))], fill="#94a3b8")
    d.text(sc((lx + 56, 40)), "normal flow", font=F_LEGEND, fill=TEXT, anchor="lm")
    lx = 1082
    for k in range(3):
        stroke(d, [(lx + k * 14, 40), (lx + k * 14 + 8, 40)], "#94a3b8", 2.5)
    d.polygon([sc((lx + 48, 40)), sc((lx + 38, 35)), sc((lx + 38, 45))], fill="#94a3b8")
    d.text(sc((lx + 58, 40)), "return", font=F_LEGEND, fill=TEXT, anchor="lm")
    return img


def activation(i, t):
    dt = (t - ARRIVE[i]) % CYCLE
    if dt < 0.12:
        return dt / 0.12
    if dt < DWELL:
        return 1.0
    return math.exp(-(dt - DWELL) / 0.55)


def token_state(t):
    """Returns (kind, index, progress) for the main token: dwell or travel."""
    t %= CYCLE
    for i in range(len(PHASES)):
        if ARRIVE[i] <= t < ARRIVE[i] + DWELL:
            return "dwell", i, 0.0
        dur = TRAVEL if i < LAST else TRAVEL_BACK
        if ARRIVE[i] + DWELL <= t < ARRIVE[i] + DWELL + dur:
            return "travel", i, (t - ARRIVE[i] - DWELL) / dur
    return "dwell", 0, 0.0


def draw_token(img, d, path, u, color):
    e = smooth(u)
    head = path.at(e * path.length)
    tail = path.at(max(0.0, e * path.length - 26))
    fade = min(1.0, u / 0.15, (1 - u) / 0.15)
    stroke(d, [tail, head], mix(BG, color, 0.85 * fade), 4)
    glow(img, (head[0] - 7, head[1] - 7, head[0] + 7, head[1] + 7), 7, color, 0.9 * fade, 5)
    d = ImageDraw.Draw(img)
    r = 5.2 * S
    d.ellipse((head[0] * S - r, head[1] * S - r, head[0] * S + r, head[1] * S + r), fill=mix(color, WHITE, 0.75 * fade + 0.1))
    return d


def render(t, base):
    img = base.copy()
    d = ImageDraw.Draw(img)
    act = [activation(i, t) for i in range(len(PHASES))]
    kind, idx, prog = token_state(t)
    idea_u = ((t - (CYCLE - IDEA_TRAVEL)) % CYCLE) / IDEA_TRAVEL  # 0..1 while the idea token travels
    idea_on = idea_u <= 1.0
    idea_glow = max(0.0, math.sin(math.pi * idea_u)) if idea_on else 0.0

    # pulse rings: one ring leaves a card when the token arrives, a fainter one follows it
    for i, (x, y) in enumerate(POS):
        for delay, strength in ((0.0, 0.8), (0.2, 0.42)):
            k = ((t - ARRIVE[i] - delay) % CYCLE) / 0.8
            if k < 1.0:
                off = 22 * (1 - (1 - k) ** 3)
                d.rounded_rectangle(((x - off) * S, (y - off) * S, (x + CW + off) * S, (y + CH + off) * S),
                                    radius=(18 + off) * S, width=round(2.2 * S),
                                    outline=mix(BG, PHASES[i][1], strength * (1 - k) ** 1.6))

    # return connectors: marching dashes, brighter while their source phase is active
    for (src, _, label, lpos, anchor), path in zip(RETURNS, RETURN_PATHS):
        a = act[src]
        color = mix(RETURN, PHASES[src][1], a)
        end = path.length - 9
        s = -(DASH + GAP) + (t * MARCH) % (DASH + GAP)
        while s < end:
            s0, s1 = max(0.0, s), min(end, s + DASH)
            if s1 - s0 > 0.5:
                stroke(d, path.piece(s0, s1), color, 2.4)
            s += DASH + GAP
        arrow_head(d, path, color)
        d.text(sc(lpos), label, font=F_RET, fill=mix(MUTED, "#f8fafc", a), anchor=anchor)

    # forward connectors
    lit = idea_glow
    c = mix(LINE, PHASES[0][1], lit)
    stroke(d, IDEA_PATH.piece(0, IDEA_PATH.length - 9), c, 2.6)
    arrow_head(d, IDEA_PATH, c)
    for i, path in enumerate(FORWARD_PATHS):
        lit = max(0.0, math.sin(math.pi * prog)) ** 0.6 if (kind == "travel" and idx == i) else 0.0
        c = mix(LINE, PHASES[i + 1][1], lit)
        stroke(d, path.piece(0, path.length - 9), c, 2.6)
        arrow_head(d, path, c)

    # idea pill
    if idea_glow > 0.02:
        glow(img, IDEA, 22, PHASES[0][1], 0.5 * idea_glow, 4)
        d = ImageDraw.Draw(img)
    d.rounded_rectangle([v * S for v in IDEA], radius=22 * S, fill=mix(CARD, PHASES[0][1], 0.14 * idea_glow),
                        outline=mix("#94a3b8", PHASES[0][1], idea_glow), width=round(2.2 * S))
    d.text(sc(((IDEA[0] + IDEA[2]) / 2, YT)), "Idea", font=F_IDEA, fill="#f1f5f9", anchor="mm")

    # cards
    for i, ((lines, accent), (x, y)) in enumerate(zip(PHASES, POS)):
        a = act[i]
        box = (x, y, x + CW, y + CH)
        if a > 0.03:
            glow(img, (x - 1, y - 1, x + CW + 1, y + CH + 1), 19, accent, 0.5 * a, 4)
            d = ImageDraw.Draw(img)
        d.rounded_rectangle([v * S for v in box], radius=18 * S, fill=mix(CARD, accent, 0.14 * a),
                            outline=mix(CARD_BORDER, accent, a), width=round((2 + 1.2 * a) * S))
        bx, by, br = x + 31, y + CH / 2, 16 + 1.5 * a
        d.ellipse(((bx - br) * S, (by - br) * S, (bx + br) * S, (by + br) * S), fill=mix(accent, WHITE, 0.25 * a))
        d.text(sc((bx, by)), str(i + 1), font=F_NUM, fill=BG, anchor="mm")
        lh = 23
        y0 = by - lh * (len(lines) - 1) / 2
        for k, line in enumerate(lines):
            d.text(sc((x + 58, y0 + k * lh)), line, font=F_CARD, fill=mix(TEXT, WHITE, a), anchor="lm")

    # tokens, on top
    if kind == "travel":
        if idx < LAST:
            d = draw_token(img, d, FORWARD_PATHS[idx], prog, PHASES[idx + 1][1])
        else:
            d = draw_token(img, d, RETURN_PATHS[FEEDBACK], prog, PHASES[0][1])
    if idea_on:
        d = draw_token(img, d, IDEA_PATH, idea_u, PHASES[0][1])

    return img.convert("RGB").resize((W, H), Image.LANCZOS)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    base = static_layer()
    if "--still" in sys.argv:
        render(float(sys.argv[sys.argv.index("--still") + 1]), base).save(out)
        return
    times = [k * FRAME_MS / 1000 for k in range(FRAMES)]
    # One palette for all frames. Most of a frame is flat background, so the palette is built
    # from the parts that carry the gradients: each card while it lights up and fades, and each
    # token on its way. Two whole frames add the static colors.
    tiles = []
    for t in (0.2, CYCLE / 2):
        tiles.append(render(t, base))
    for i, (x, y) in enumerate(POS):
        for dt in (0.05, 0.3, DWELL + 0.12, DWELL + 0.3, DWELL + 0.6, DWELL + 1.0, DWELL + 1.6):
            frame = render((ARRIVE[i] + dt) % CYCLE, base)
            tiles.append(frame.crop((x - 46, y - 46, x + CW + 46, y + CH + 46)))
        for u in (0.25, 0.5, 0.75):
            dur = TRAVEL if i < LAST else TRAVEL_BACK
            path = FORWARD_PATHS[i] if i < LAST else RETURN_PATHS[FEEDBACK]
            hx, hy = path.at(smooth(u) * path.length)
            frame = render((ARRIVE[i] + DWELL + u * dur) % CYCLE, base)
            tiles.append(frame.crop((round(hx) - 40, round(hy) - 40, round(hx) + 40, round(hy) + 40)))
    tiles.append(render(CYCLE - IDEA_TRAVEL / 2, base).crop((0, round(YT) - 60, COLS[0] + 30, round(YT) + 60)))
    tw = max(im.width for im in tiles)
    sheet = Image.new("RGB", (tw, sum(im.height for im in tiles)), rgb(BG))
    ty = 0
    for im in tiles:
        sheet.paste(im, (0, ty))
        ty += im.height
    palette = sheet.quantize(colors=255, method=Image.Quantize.MEDIANCUT, kmeans=3, dither=Image.Dither.NONE)
    frames = [render(t, base).quantize(palette=palette, dither=Image.Dither.NONE) for t in times]
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=FRAME_MS, loop=0, optimize=True)
    print(f"{out}: {FRAMES} frames, {CYCLE:.2f} s loop, card font {_size}")


if __name__ == "__main__":
    main()
