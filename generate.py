#!/usr/bin/env python3
"""Generate entry.png: a newspaper-style front page summing up the world news
of Wednesday 25 November 2026. Everything is drawn in code with Pillow;
no photos, no downloaded images, no AI-generated art.

Deterministic: fixed layout, fixed text, fixed colours, no timestamps and
no randomness, so repeated runs produce byte-identical PNG output.

Usage:
    python3 generate.py            # writes entry.png next to this file
    python3 generate.py out.png    # writes to the given path
"""

import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36
INK = (18, 18, 18)
PAPER = (250, 247, 238)
RULE = (18, 18, 18)
MUTED = (90, 86, 78)
ACCENT = (158, 32, 24)
BLUE = (24, 64, 110)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)      # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)            # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)        # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)              # noqa: E731


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, spacing=4):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def story_block(draw, x, y, w, kicker, headline, body, head_size=25,
                body_size=15, kicker_color=ACCENT):
    """Draw one story: red kicker, serif headline, sans body. Returns y below."""
    draw.text((x, y), kicker, font=SANS_B(12), fill=kicker_color)
    y += 20
    head_lines = wrap(draw, headline, SERIF_B(head_size), w)
    y = draw_lines(draw, head_lines, x, y, SERIF_B(head_size), INK, spacing=2)
    y += 4
    body_lines = wrap(draw, body, SANS(body_size), w)
    y = draw_lines(draw, body_lines, x, y, SANS(body_size), INK, spacing=3)
    return y


def hline(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def vline(draw, x, y0, y1, width=1, fill=(170, 164, 152)):
    draw.line([(x, y0), (x, y1)], fill=fill, width=width)


def draw_tanker_scene(draw, x, y, w, h):
    """Small code-drawn schematic: two tankers on a strait, one on fire."""
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    # sky and sea
    draw.rectangle([x + 2, y + 2, x + w - 2, y + int(h * 0.55)],
                   fill=(214, 228, 238))
    draw.rectangle([x + 2, y + int(h * 0.55), x + w - 2, y + h - 2],
                   fill=(58, 110, 158))
    # sun
    draw.ellipse([x + w - 62, y + 12, x + w - 22, y + 52], fill=(232, 178, 62))
    # waves
    for i, wy in enumerate((0.62, 0.72, 0.83)):
        yy = y + int(h * wy)
        for xx in range(x + 8, x + w - 30, 46):
            draw.arc([xx, yy, xx + 36, yy + 16], 0, 180,
                     fill=(214, 228, 238), width=2)
    # tanker 1 (left, intact)
    tx, ty = x + 14, y + int(h * 0.52)
    draw.rectangle([tx, ty, tx + 118, ty + 26], fill=(40, 40, 40))
    draw.rectangle([tx + 74, ty - 18, tx + 100, ty], fill=(40, 40, 40))
    draw.rectangle([tx + 82, ty - 30, tx + 94, ty - 18], fill=(40, 40, 40))
    # tanker 2 (right, on fire)
    tx2 = x + w - 132
    draw.rectangle([tx2, ty, tx2 + 118, ty + 26], fill=(40, 40, 40))
    draw.rectangle([tx2 + 18, ty - 18, tx2 + 44, ty], fill=(40, 40, 40))
    fx, fy = tx2 + 66, ty - 14
    draw.polygon([(fx, fy), (fx - 16, fy + 18), (fx - 4, fy + 18)],
                 fill=(232, 120, 30))
    draw.polygon([(fx + 6, fy - 12), (fx - 8, fy + 18), (fx + 20, fy + 18)],
                 fill=(240, 170, 40))
    draw.polygon([(fx + 2, fy + 2), (fx - 4, fy + 18), (fx + 10, fy + 18)],
                 fill=(158, 32, 24))
    draw.rectangle([x + 2, y + h - 22, x + w - 2, y + h - 2],
                   fill=(18, 48, 84))
    draw.text((x + 10, y + h - 19), "STRAIT OF HORMUZ  -  SCHEMATIC, NOT A PHOTO",
              font=SANS_B(10), fill=(255, 255, 255))


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    x0, x1 = MARGIN, W - MARGIN

    # ---- Masthead -------------------------------------------------------
    d.text((x0, 18), "THE WORLD IN ONE PAGE", font=SERIF_B(58), fill=INK)
    hline(d, x0, x1, 96, width=4)
    d.text((x0, 104), "WEDNESDAY, 25 NOVEMBER 2026",
           font=SANS_B(17), fill=INK)
    d.text((x1, 104), "ONE IMAGE  ·  SEVEN STORIES",
           font=SANS_B(17), fill=ACCENT, anchor="ra")
    hline(d, x0, x1, 134, width=2)

    # ---- Lead story: Strait of Hormuz ----------------------------------
    y = 150
    d.text((x0, y), "LEAD STORY  ·  MIDDLE EAST", font=SANS_B(13),
           fill=ACCENT)
    y += 24
    lead_head = "Two oil tankers hit mines and catch fire in the Strait of Hormuz"
    y = draw_lines(d, wrap(d, lead_head, SERIF_B(40), x1 - x0 - 330),
                   x0, y, SERIF_B(40), INK, spacing=2)
    lead_body = (
        "Iran's Revolutionary Guard said two tankers struck naval mines and "
        "exploded while trying to transit an unauthorised route through the "
        "strait. Washington is reportedly weighing new options in its "
        "confrontation with Iran."
    )
    y = draw_lines(d, wrap(d, lead_body, SANS(16), x1 - x0 - 330),
                   x0, y + 8, SANS(16), INK, spacing=4)
    draw_tanker_scene(d, x1 - 300, 176, 300, 168)
    hline(d, x0, x1, 366, width=2)

    # ---- Row 2: Huawei | Shenzhou-24 ------------------------------------
    col_w = (x1 - x0 - 28) // 2
    lx, rx = x0, x0 + col_w + 28
    y2 = 384
    story_block(
        d, lx, y2, col_w, "TECH  ·  UNITED STATES",
        "Huawei convicted in New York on 10 of 12 counts",
        "A Brooklyn jury found the Chinese telecoms giant guilty of "
        "conspiring to steal trade secrets, bank fraud, wire fraud and "
        "violating US sanctions over its business in Iran. It was acquitted "
        "of the racketeering charge. Sentencing is set for September 2027.",
        head_size=24, body_size=14)
    story_block(
        d, rx, y2, col_w, "SPACE  ·  CHINA",
        "Pakistan's first astronaut reaches Tiangong station",
        "Shenzhou-24 launched from Jiuquan and docked with China's Tiangong "
        "space station about three and a half hours later. Aboard was "
        "Muhammad Zeeshan Ali, the first Pakistani in orbit and the first "
        "foreigner ever to visit Tiangong.",
        head_size=24, body_size=14)
    vline(d, x0 + col_w + 14, 384, 566)
    hline(d, x0, x1, 576, width=1, fill=(170, 164, 152))

    # ---- Row 3: US GDP | Colombia ---------------------------------------
    y3 = 594
    story_block(
        d, lx, y3, col_w, "ECONOMY  ·  UNITED STATES",
        "US growth revised sharply up to 4.3% in third quarter",
        "The Bureau of Economic Analysis said real GDP grew at an annual "
        "rate of 4.3% in July-September, up from its first estimate of 3.4% "
        "and well above forecasts of 3.5%, driven by investment and "
        "consumer spending.",
        head_size=24, body_size=14)
    story_block(
        d, rx, y3, col_w, "LATIN AMERICA  ·  COLOMBIA",
        "All hostages freed as forces storm Cartagena supermarket",
        "Colombian police and troops ended a day-long siege at an Exito "
        "supermarket in Cartagena, freeing every remaining hostage. One "
        "captor was killed and others arrested. The standoff began with a "
        "botched robbery of an armoured cash truck.",
        head_size=24, body_size=14)
    vline(d, x0 + col_w + 14, 594, 776)
    hline(d, x0, x1, 786, width=1, fill=(170, 164, 152))

    # ---- Row 4: COP31 | Houthi attacks ----------------------------------
    y4 = 804
    story_block(
        d, lx, y4, col_w, "CLIMATE  ·  COP31",
        "Climate talks end with no deal to move away from fossil fuels",
        "The UN COP31 climate talks closed without agreement on "
        "transitioning away from fossil fuels. Pope Leo XIV said he was "
        "concerned, warning that extreme weather linked to the climate "
        "crisis is becoming more frequent.",
        head_size=22, body_size=14)
    story_block(
        d, rx, y4, col_w, "MIDDLE EAST  ·  SAUDI ARABIA",
        "Houthis strike Saudi refinery as Riyadh tower attack injures 11",
        "Yemen's Houthis said they attacked Saudi Arabia's Ras Tanura oil "
        "refinery, causing fires. A day earlier, a Houthi strike on a "
        "skyscraper in Riyadh injured 11 people, Saudi civil defence said.",
        head_size=22, body_size=14)
    hline(d, x0, x1, 950, width=2)

    # ---- Also in brief ----------------------------------------------------
    y5 = 962
    brief = ("ALSO IN BRIEF:  Australia and Solomon Islands sign a treaty "
             "barring foreign military bases  ·  Dow closes above 50,000 "
             "for the first time  ·  South Korea's KOSPI plunges 6.2% as "
             "Asian stocks slide")
    y5 = draw_lines(d, wrap(d, brief, SANS_B(13), x1 - x0),
                    x0, y5, SANS_B(13), MUTED, spacing=3)

    # ---- Footer ------------------------------------------------------------
    hline(d, x0, x1, 1004, width=1, fill=(170, 164, 152))
    d.text((x0, 1008),
           "Sources: Just Security · Reuters · U.S. Bureau of Economic Analysis "
           "· Xinhua / China Manned Space Agency · AFP",
           font=SANS(10), fill=MUTED)

    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
