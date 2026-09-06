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
PEXELS = {
    'meals-glass': 4929677, 'meal-prep': 30635717, 'ingredients': 4963581,
    'bowl': 566564, 'guide-table': 12499375, 'woman-thinking': 8560799,
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


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)

    # ---- Betty's own photography ------------------------------------------
    # Screenshot_4 is the frame the brand deck picked for the homepage: warm,
    # face forward, personality first. Crop off the carousel dots at the bottom.
    save(cover(shot(4).crop((0, 0, 549, 558)), 0.80, focus=0.58), 'betty-hero.jpg', q=88)
    save(cover(shot(16), 0.80, focus=0.48), 'betty-portrait.jpg', q=88)
    save(cover(shot(14), 1.34, vfocus=0.42), 'betty-beach.jpg')
    save(cover(shot(10), 1.00, vfocus=0.45), 'betty-street.jpg')
    save(cover(shot(21), 0.80), 'betty-kettlebell.jpg')
    save(cover(shot(18), 0.80), 'betty-cable.jpg')
    # competition frames: About only, framed as credentials
    save(cover(shot(13), 1.00), 'betty-stage.jpg')
    save(cover(shot(7), 1.00), 'betty-backstage.jpg')
    save(cover(shot(11), 1.00), 'betty-track.jpg')

    # ---- food, teaching and reader photography ----------------------------
    stock('meals-glass', 'food-portions.jpg', 1.20, 1000)
    stock('meal-prep', 'food-prep.jpg', 1.00, 760)
    stock('ingredients', 'food-whole.jpg', 1.00, 760)
    stock('bowl', 'food-bowl.jpg', 1.20, 900)
    stock('guide-table', 'guide-table.jpg', 1.20, 900)
    stock('woman-thinking', 'reader-quiet.jpg', 0.80, 760, vfocus=0.35)

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
    main()
