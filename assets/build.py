#!/usr/bin/env python3
"""Generates the profile artwork. Run from anywhere: python3 assets/build.py

The drawings follow the portfolio at mouadja02.github.io: an IC datasheet for
part MJ02. Text is set in system fonts (GitHub serves README images without
access to web fonts), so nothing here depends on a font being installed.
"""
import math
from pathlib import Path

OUT = Path(__file__).parent

THEMES = {
    "light": dict(paper="#eef0df", sheet="#e5e9d3", ink="#15201b", muted="#526156", accent="#d93c16", grid="#286e42"),
    "dark": dict(paper="#0d1310", sheet="#131b17", ink="#dee5d5", muted="#8e9d90", accent="#ffb224", grid="#82d2a0"),
}

SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"
HEAVY = "'Arial Black','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

# The 20 pins of the package, in datasheet order (down the left, up the right).
PINS = ["GCP", "AWS", "CFLARE", "SNOW", "SPARK", "PGSQL", "NEO4J", "AIRFLOW", "PY", "RUST",
        "TF", "PINECONE", "CUDA", "DOCKER", "TFORM", "GITHUB", "BASH", "N8N", "CLAUDE", "CURSOR"]


def noise_table(n=256, seed=0x6D6A3032):
    out = []
    for _ in range(n):
        seed = (seed * 1664525 + 1013904223) & 0xFFFFFFFF
        out.append(seed / 0xFFFFFFFF * 2 - 1)
    return out


TABLE = noise_table()


def trace(x0, x1, y, amount, start=0, amp=13.0, period=26, step=3.0):
    """A sine with `amount` (0..1) of noise on it, as an SVG path."""
    pts, i, x = [], start, x0
    while x <= x1 + 0.01:
        v = math.sin(2 * math.pi * i / period) * amp + TABLE[i % 256] * amp * 1.1 * amount
        pts.append(f"{x:.1f} {y - v:.1f}")
        x += step
        i += 1
    return "M" + "L".join(pts), i


def grid(x, y, w, h, t, minor=14):
    lines = []
    k = 0
    gx = x
    while gx <= x + w + 0.01:
        lines.append(f'<path d="M{gx:.0f} {y}V{y + h}" stroke-opacity="{0.2 if k % 5 == 0 else 0.08}"/>')
        gx += minor
        k += 1
    k = 0
    gy = y
    while gy <= y + h + 0.01:
        lines.append(f'<path d="M{x} {gy:.0f}H{x + w}" stroke-opacity="{0.2 if k % 5 == 0 else 0.08}"/>')
        gy += minor
        k += 1
    return f'<g stroke="{t["grid"]}" stroke-width="1">{"".join(lines)}</g>'


def chain(x, y, w, h, t):
    """Figure 1: a noisy input cleaned up by two blocks."""
    mid = y + h / 2
    bw, bh = 86, 46
    gap = (w - 2 * bw - 24) / 3
    xs = [x + 12, x + 12 + gap, x + 12 + gap + bw, x + 12 + 2 * gap + bw, x + 12 + 2 * gap + 2 * bw, x + w - 12]
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{t["sheet"]}"/>', grid(x, y, w, h, t)]
    i = 0
    for (a, b), amount in zip([(xs[0], xs[1]), (xs[2], xs[3]), (xs[4], xs[5])], [1.0, 0.35, 0.0]):
        d, i = trace(a, b, mid, amount, i)
        parts.append(f'<path d="{d}" fill="none" stroke="{t["accent"]}" stroke-width="1.8" stroke-linejoin="round"/>')
    for bx, label in [(xs[1], "PIPELINE"), (xs[3], "MODEL")]:
        parts.append(f'<rect x="{bx:.1f}" y="{mid - bh / 2}" width="{bw}" height="{bh}" fill="{t["paper"]}" stroke="{t["ink"]}" stroke-width="2"/>')
        parts.append(f'<text x="{bx + bw / 2:.1f}" y="{mid + 4.5}" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="13" letter-spacing=".5" fill="{t["ink"]}">{label}</text>')
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{t["ink"]}"/>')
    return "".join(parts)


def header(theme, mobile=False):
    t = THEMES[theme]
    W, H = (480, 430) if mobile else (900, 300)
    mono = f'font-family="{MONO}" font-size="11" letter-spacing="1.3"'
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">',
         '<title id="t">Mouad Jaouhari, Data &amp; AI Engineer</title>',
         '<desc id="d">Datasheet title block for part MJ02. A noisy signal passes through a pipeline and a model and comes out clean.</desc>',
         f'<rect width="{W}" height="{H}" fill="{t["paper"]}"/>',
         # top strip
         f'<rect x="24" y="14" width="48" height="20" fill="{t["ink"]}"/>',
         f'<text x="48" y="28.5" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="1" fill="{t["paper"]}">MJ02</text>',
         f'<text x="84" y="28" {mono} fill="{t["ink"]}">DATASHEET</text>',
         f'<text x="{W - 24}" y="28" text-anchor="end" {mono} fill="{t["muted"]}">REV. NOV 2026 · PESSAC, FR</text>',
         f'<path d="M0 46H{W}" stroke="{t["ink"]}" stroke-width="1.5"/>']
    name = f'font-family="{HEAVY}" font-weight="900" letter-spacing="-2" fill="{t["ink"]}"'
    if mobile:
        s += [f'<text x="24" y="112" font-size="58" {name}>MOUAD</text>',
              f'<text x="24" y="168" font-size="58" {name}>JAOUHARI</text>',
              f'<path d="M24 188H{W - 24}" stroke="{t["ink"]}" stroke-width="2"/>',
              f'<text x="24" y="216" font-family="{SANS}" font-weight="700" font-size="19" letter-spacing=".5" fill="{t["ink"]}">DATA &amp; AI ENGINEER</text>',
              f'<text x="24" y="236" {mono} fill="{t["muted"]}">SIGNAL-TO-SYSTEM CONVERTER</text>',
              chain(24, 256, W - 48, 120, t),
              f'<text x="24" y="398" font-family="{MONO}" font-size="11" fill="{t["muted"]}">Figure 1. Noise in, decisions out.</text>']
    else:
        s += [f'<text x="28" y="124" font-size="68" {name}>MOUAD</text>',
              f'<text x="28" y="190" font-size="68" {name}>JAOUHARI</text>',
              f'<path d="M28 212H452" stroke="{t["ink"]}" stroke-width="2"/>',
              f'<text x="28" y="242" font-family="{SANS}" font-weight="700" font-size="21" letter-spacing=".5" fill="{t["ink"]}">DATA &amp; AI ENGINEER</text>',
              f'<text x="28" y="264" {mono} fill="{t["muted"]}">SIGNAL-TO-SYSTEM CONVERTER</text>',
              chain(488, 74, 384, 168, t),
              f'<text x="488" y="264" font-family="{MONO}" font-size="11" fill="{t["muted"]}">Figure 1. Noise in, decisions out.</text>']
    s += [f'<path d="M0 {H - 1}H{W}" stroke="{t["ink"]}" stroke-width="2"/>', '</svg>']
    return "\n".join(s) + "\n"


def pinout(theme):
    t = THEMES[theme]
    per, pitch, top = len(PINS) // 2, 34, 52
    bx, by, bw = 250, 24, 140
    bh = (per - 1) * pitch + 56
    W, H = 640, by * 2 + bh
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">',
         '<title id="t">MJ02 pin configuration</title>',
         f'<desc id="d">A {len(PINS)}-pin package. Each pin is a technology: {", ".join(PINS)}.</desc>',
         f'<rect width="{W}" height="{H}" fill="{t["sheet"]}"/>', grid(0, 0, W, H, t, 16),
         f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" fill="none" stroke="{t["ink"]}"/>']
    for n, label in enumerate(PINS, start=1):
        left = n <= per
        row = n - 1 if left else len(PINS) - n
        y = top + row * pitch
        lx, tx, anchor = (bx - 30, bx - 40, "end") if left else (bx + bw, bx + bw + 40, "start")
        nx, nanchor = (bx + 10, "start") if left else (bx + bw - 10, "end")
        s.append(f'<rect x="{lx}" y="{y - 7}" width="30" height="14" fill="{t["paper"]}" stroke="{t["ink"]}" stroke-width="1.5"/>')
        s.append(f'<text x="{tx}" y="{y + 4.5}" text-anchor="{anchor}" font-family="{MONO}" font-size="13" fill="{t["ink"]}">{label}</text>')
        s.append(f'<text x="{nx}" y="{y + 4}" text-anchor="{nanchor}" font-family="{MONO}" font-size="11" fill="{t["paper"]}" fill-opacity=".6" data-n="1">{n}</text>')
    # body goes under the pin numbers, so insert it before them
    body = [f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="{t["ink"]}"/>',
            f'<path d="M{bx + bw / 2 - 14} {by}a14 14 0 0 0 28 0" fill="{t["sheet"]}"/>',
            f'<circle cx="{bx + 15}" cy="{by + 15}" r="3.5" fill="{t["paper"]}" fill-opacity=".7"/>',
            f'<g transform="translate({bx + bw / 2} {by + bh / 2}) rotate(-90)">'
            f'<text text-anchor="middle" y="4" font-family="{HEAVY}" font-weight="900" font-size="40" letter-spacing="-1" fill="{t["paper"]}">MJ02</text>'
            f'<text text-anchor="middle" y="26" font-family="{MONO}" font-size="10" letter-spacing="3" fill="{t["paper"]}" fill-opacity=".6">DATA · AI · 2026</text></g>']
    numbers = [line for line in s if 'data-n="1"' in line]
    rest = [line for line in s if 'data-n="1"' not in line]
    s = rest + body + [line.replace(' data-n="1"', "") for line in numbers]
    s.append("</svg>")
    return "\n".join(s) + "\n"


if __name__ == "__main__":
    files = {
        "header-light.svg": header("light"),
        "header-dark.svg": header("dark"),
        "header-mobile-light.svg": header("light", mobile=True),
        "header-mobile-dark.svg": header("dark", mobile=True),
        "pinout-light.svg": pinout("light"),
        "pinout-dark.svg": pinout("dark"),
    }
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8", newline="\n")
        print(f"{name}: {len(svg)} bytes")
