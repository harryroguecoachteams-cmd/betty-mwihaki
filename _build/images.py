# -*- coding: utf-8 -*-
"""
Rebuilds assets/img from the originals. Run it only when the source photos
change; the output is committed.

    python _build/images.py

Betty's own photos live in F:\\betty\\betty photos\\ and arrived as 460 to 600px
screenshots, so every placement in the stylesheet is capped to keep the worst
upscale near 1.2x. Stock food and reader photography is pulled from Pexels once
and self-hosted, never hotlinked. EXIF, GPS and IPTC are stripped on the way out.
"""
import os
from PIL import Image, ImageFilter

SRC = r'F:/betty/betty photos'
STOCK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_stock')
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   '..', 'assets', 'img'))

# Pexels ids, downloaded into _stock/ as <name>.jpg before running:
#   https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=1400
STOCK_IN_USE = False

PEXELS = {
    'meals-glass': 4929677, 'meal-prep': 30635717, 'ingredients': 4963581,
    'bowl': 566564, 'guide-table': 12499375,
    'kitchen-woman': 3960597, 'kitchen-scale': 3743169,
    'kitchen-slice': 8552737, 'kitchen-plates': 12673786,
    'plate-balanced': 3814676, 'veg-white': 142520,
}


def cover(im, ratio, focus=0.5, vfocus=0.5):
    """Crop to `ratio` (w/h), keeping the focus point."""
    w, h = im.size
    if w / h > ratio:
        nw, nh = int(round(h * ratio)), h
    else:
        nw, nh = w, int(round(w / ratio))
    x = int(round((w - nw) * focus))
    y = int(round((h - nh) * vfocus))
    return im.crop((x, y, x + nw, y + nh))


def save(im, name, q=86, sharpen=True):
    im = im.convert('RGB')
    if sharpen:                      # helps the small sources survive a 1.2x upscale
        im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=58, threshold=3))
    clean = Image.new('RGB', im.size)
    clean.putdata(list(im.getdata()))            # drops every metadata block
    path = os.path.join(OUT, name)
    clean.save(path, 'JPEG', quality=q, optimize=True, progressive=True, subsampling=1)
    print('%-22s %sx%s %6.1f KB' % (name, im.size[0], im.size[1],
                                    os.path.getsize(path) / 1024.0))


def shot(n):
    return Image.open(os.path.join(SRC, 'Screenshot_%d.png' % n))


def stock(fn, out, ratio, w, focus=0.5, vfocus=0.5, q=82):
    im = cover(Image.open(os.path.join(STOCK, fn + '.jpg')), ratio, focus, vfocus)
    save(im.resize((w, int(round(w / ratio))), Image.LANCZOS), out, q=q, sharpen=False)


# ---------------------------------------------------------------- new photos --
# Five photographs Betty sent on 3 Sep 2026, 945-1200px wide, so for the first
# time these are DOWNSCALES rather than upscales. They exist to make the site
# unmistakably hers: real places, real clothes, ordinary light. No unsharp mask,
# because nothing here is being stretched.
WA = {
    'coast':  '9.13.19 PM',   # running on the sand at Haystack Rock
    'trail':  '9.13.55 PM',   # on a walking trail, hand shading her eyes
    'cabin':  '9.15.03 PM',   # smiling in an aircraft seat
    'red-a':  '9.17.29 PM',   # red dress, sisal baskets on the wall
    'red-b':  '9.17.35 PM',
}


def wa(key):
    return Image.open(os.path.join(
        SRC, 'WhatsApp Image 2026-09-03 at %s.jpeg' % WA[key]))


def new_photos():
    # Wide editorial plate, and the one full-bleed image on the site. The
    # source is 945px, so 1440 is a 1.52x upscale, over the 1.2x ceiling every
    # other placement respects. It is allowed here and only here: the subject is
    # 40px tall in a hazy seascape, where softness reads as distance rather than
    # as a defect, and the page needs one image that runs edge to edge. Resample
    # once at 1440 rather than shipping 1120 and letting the browser stretch it.
    save(cover(wa('coast'), 2.35, vfocus=0.42).resize((1440, 613), Image.LANCZOS),
         'coast-wide.jpg', q=82)
    # Everything below is a downscale, so no sharpening and a higher quality.
    save(cover(wa('trail'), 0.82, focus=0.46, vfocus=0.46)
         .resize((660, 805), Image.LANCZOS), 'betty-trail.jpg', q=86, sharpen=False)
    save(cover(wa('cabin'), 1.00, focus=0.42, vfocus=0.34)
         .resize((520, 520), Image.LANCZOS), 'betty-cabin.jpg', q=86, sharpen=False)
    save(cover(wa('red-b'), 0.70, focus=0.50, vfocus=0.44)
         .resize((580, 829), Image.LANCZOS), 'betty-red.jpg', q=86, sharpen=False)


# --------------------------------------------------------------- social card --
# assets/og.jpg, the 1200x630 image every link preview shows: Slack, WhatsApp,
# Facebook, LinkedIn, X, iMessage. Without one, a shared link renders as a grey
# rectangle with a URL under it, which is the least premium object a premium
# brand can put in somebody's feed.
#
# It is built here rather than screenshotted so it stays on the deck: forest
# ground, the wordmark with its clay point, one signature line set in Lora, and
# her own photograph on the right.
FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_fonts')
FOREST = (0x1F, 0x3D, 0x33)
CLAY = (0xC9, 0x69, 0x4A)
CLAY_HI = (0xE5, 0x94, 0x73)
SAGE = (0x8F, 0xA9, 0x9B)


def _font(name, size, weight=None):
    from PIL import ImageFont
    path = os.path.join(FONTS, name)
    if not os.path.exists(path):                       # Georgia is the site's
        path = r'C:/Windows/Fonts/georgia.ttf'         # own declared fallback
    f = ImageFont.truetype(path, size)
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def _tracked(d, xy, text, font, fill, track=0):
    """PIL has no letter-spacing, and the brand's small caps are all tracked."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + track
    return x


def og_card():
    from PIL import ImageDraw
    W, H = 1200, 630
    card = Image.new('RGB', (W, H), FOREST)
    d = ImageDraw.Draw(card)

    # her photograph, right-hand third
    pw = 470
    photo = Image.open(os.path.join(OUT, 'betty-hero.jpg'))
    photo = cover(photo, pw / float(H), focus=0.55).resize((pw, H), Image.LANCZOS)
    card.paste(photo, (W - pw, 0))
    d.rectangle([W - pw - 3, 0, W - pw - 1, H], fill=CLAY)

    x0, right = 78, W - pw - 3 - 78

    # wordmark
    lora_b = _font('Lora.ttf', 66, 600)
    end = d.text((x0, 62), 'Betty', font=lora_b, fill=(255, 255, 255))
    wm = d.textlength('Betty', font=lora_b)
    d.ellipse([x0 + wm + 8, 62 + 48, x0 + wm + 8 + 11, 62 + 59], fill=CLAY)
    _tracked(d, (x0 + 3, 146), 'NUTRITION EDUCATION FOR REAL LIFE',
             _font('Inter.ttf', 15, 600), SAGE, track=2.6)

    # the one line to remember, deck page 30
    lora = _font('Lora.ttf', 52, 500)
    lines = ['Stop guessing', 'what to eat.', 'Start understanding',
             'your food.']
    y = 236
    for i, ln in enumerate(lines):
        d.text((x0, y), ln, font=lora,
               fill=(255, 255, 255) if i < 2 else (0xE8, 0xEF, 0xEA))
        y += 62
    assert max(d.textlength(l, font=lora) for l in lines) < right - x0

    d.rectangle([x0, 520, x0 + 58, 523], fill=CLAY)
    _tracked(d, (x0, 546), 'A PRACTICAL 16-WEEK NUTRITION COACHING METHOD',
             _font('Inter.ttf', 14, 600), CLAY_HI, track=1.9)

    path = os.path.join(os.path.dirname(OUT), 'og.jpg')
    card.save(path, 'JPEG', quality=88, optimize=True, progressive=True)
    print('%-22s %sx%s %6.1f KB'
          % ('og.jpg', W, H, os.path.getsize(path) / 1024.0))


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)

    new_photos()
    og_card()

    # ---- Betty's own photography ------------------------------------------
    # Screenshot_4 is the frame the brand deck picked for the homepage: warm,
    # face forward, personality first. Crop off the carousel dots at the bottom.
    save(cover(shot(4).crop((0, 0, 549, 558)), 0.80, focus=0.58), 'betty-hero.jpg', q=88)
    save(cover(shot(16), 0.80, focus=0.48), 'betty-portrait.jpg', q=88)
    # currently unplaced: the coast plate from the 3 Sep batch is the same
    # scene at four times the resolution. Kept because it is her photograph.
    save(cover(shot(14), 1.34, vfocus=0.42), 'betty-beach.jpg')
    save(cover(shot(10), 1.00, vfocus=0.45), 'betty-street.jpg')
    save(cover(shot(21), 0.80), 'betty-kettlebell.jpg')
    save(cover(shot(18), 0.80), 'betty-cable.jpg')
    # competition frames: About only, framed as credentials
    save(cover(shot(13), 1.00), 'betty-stage.jpg')
    save(cover(shot(7), 1.00), 'betty-backstage.jpg')
    save(cover(shot(11), 1.00), 'betty-track.jpg')
    # Screenshot_1: a trail race, bib 259, other ordinary runners in frame. The
    # least physique-posed image in the whole library and the only one that
    # shows her among other people, so it carries the About page's line about
    # never being asked to train like this.
    save(cover(shot(1), 1.30, vfocus=0.46), 'betty-race.jpg', q=88)

    # As of 7 Sep 2026 no page places a stock photograph. Every image on the
    # site is Betty's own. This half only runs if _stock is present AND
    # STOCK_IN_USE is flipped back on; the ids above are kept as the record.
    if not STOCK_IN_USE or not os.path.isdir(STOCK):
        print('licensed stock is unused by the site, skipping')
        return

    # ---- food, teaching and reader photography ----------------------------
    stock('meals-glass', 'food-portions.jpg', 1.20, 1000)
    stock('meal-prep', 'food-prep.jpg', 1.00, 760)
    stock('ingredients', 'food-whole.jpg', 1.00, 760)
    stock('bowl', 'food-bowl.jpg', 1.20, 900)
    stock('guide-table', 'guide-table.jpg', 1.20, 900)

    # Journal thumbnails. Deck image rule: would the woman in this photo feel
    # understood, or evaluated? No before-and-afters, no body scrutiny, no
    # donut-versus-apple, and nothing that makes the brand look fitness-only.
    for src, out, fy in [('kitchen-woman', 'journal-01', 0.45),
                         ('plate-balanced', 'journal-02', 0.50),
                         ('kitchen-scale', 'journal-03', 0.50),
                         ('kitchen-slice', 'journal-04', 0.42),
                         ('veg-white', 'journal-05', 0.50),
                         ('kitchen-plates', 'journal-06', 0.48)]:
        stock(src, out + '.jpg', 1.42, 760, vfocus=fy)


if __name__ == '__main__':
    import sys
    if 'og' in sys.argv[1:]:
        og_card()
    else:
        main()
