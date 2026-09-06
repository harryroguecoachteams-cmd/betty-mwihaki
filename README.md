# Betty | Nutrition education for real life

Website for **Beatrice "Betty" Mwihaki Igeria**, built by Rogue Coach Teams.

**Live:** https://harryroguecoachteams-cmd.github.io/betty-mwihaki/
**Source of truth:** `_build/build.py`. Run it, do not hand-edit the HTML.

```bash
python _build/build.py     # regenerates all six pages
python _build/images.py    # rebuilds assets/img from the originals
```

**Before launch, set `FORM_ENDPOINT` at the top of `_build/build.py`.** Both
forms are currently showing a mailto button instead of a real form, and the
build prints a warning every time it runs until that is fixed. See open item 2.

---

## What this is

A static six-page site built to the **Betty Brand Identity Deck** (September 2026).
The first draft, from August 2026, followed a Kajabi reference layout in teal and
coral. That is gone. Everything below now comes from the deck.

| Deck | Here |
|---|---|
| Lora headlines + Inter body | same, variable weights from Google Fonts |
| Forest `#1F3D33`, Clay `#C9694A`, Sage `#8FA99B`, Oat `#F4F0E8`, White | full token set in `assets/style.css` |
| 60% forest and white / 25% oat and sage / 15% clay | clay is accent only; section grounds no longer alternate on a fixed formula |
| "Betty" wordmark with one clay point | header, footer, favicon |
| Nav: About, The Method, Coaching, Resources, Start here | About, The Method, Resources, Journal, Start here |
| Hero: "Stop Guessing What to Eat. Start Understanding Your Food." | home `<h1>`, verbatim |
| Hero strip: Food clarity / Simple action / Confidence | one forest line of running type under the hero |
| Her words (p5) | pull quote, home |
| The woman we serve (p4) | "You are not new to trying", as running editorial |
| Position: The noise / The gap / Betty (p6) | a typographic ladder, home |
| Transformation: Confused, Capable, Confident (p3) | a photograph and a plain sequence, home |
| The Food Clarity Method, five phases (p14) | editorial timeline, home and The Method |
| Credibility (p15), Personality (p10) | a definition list and a paragraph of running prose, About |
| Five principles (p9) | home, "Five beliefs behind every conversation" |
| Signature language (p13) | one oversized statement, home |
| Free guide: the label-reading guide (p27) | opt-in band on every page |
| Claims non-negotiables (p28) | see below |

### Page mapping

| File | Nav label |
|---|---|
| `index.html` | Home |
| `about.html` | About |
| `services.html` | The Method |
| `shop.html` | Resources |
| `blog.html` | Journal |
| `contact.html` | Start here |

The deck's nav lists "The Method" and "Coaching" separately. They are one page
here, because there is one offer. Say the word and they split.

---

## The September 2026 humanization pass

The build before this one was correct, consistent and measurably sound, and it
still read as a site a machine had laid out. The tell was not in any single
element. It was the rhythm: twelve sections in a row made from one kit, an
eyebrow above every heading, `01 / 02 / 03` in four unrelated places, and three
equal rounded cards every time the content happened to arrive in threes.

This pass kept the copy, the palette, the type, the information architecture and
the accessibility work, and broke the template.

### What was removed, and why

| Removed | Why |
|---|---|
| 9 of 12 section eyebrows | "The transformation", "The difference", "Real outcomes" describe what a section *is doing*. Nobody says them out loud. Three survive: the hero and the free guide band. |
| `01 / 02 / 03` on Who this is for, Confused / Capable / Confident, Credibility, and the weekly process | Numbers are decoration unless the order is the content. Only the five phases keep them. |
| Every `.card` grid | Three equal rounded boxes is the shape a layout takes when nobody chose it. Pricing tiers, product cards and the contact aside keep their boxes, because that content is genuinely modular. Everything else is type, rules and whitespace. |
| The scrolling marquee | Four brand slogans on an infinite loop, saying nothing the page did not already say better. Replaced by one oversized statement: *Progress comes from what you repeat.* |
| The clarity field | 49 dots scrubbing from seeded chaos into a 7x7 grid. Clever, abstract, and it would have worked just as well for a law firm. Replaced by a photograph of Betty and a plain three-step sequence. |
| The drawn SVG arc | The five phases drew themselves along a curve via `stroke-dashoffset`, nodes placed with `getPointAtLength`. Replaced by a vertical editorial timeline that reads identically and needs no JavaScript. |
| The scroll rail | A fixed desktop progress rail with clickable section ticks. Technically nice, unnecessary. |
| Floating animated circles | Six sections carried two or three drifting flat circles. Generic decorative geometry doing work that photography and typography should do. |
| Image parallax, clip wipes and 1.13 scale settles | Applied to every image on the site. An image is an image. |
| Per-element stagger delays | `data-stagger` gave every child of every grid an increasing delay. That is what makes a page scroll like a product demo. |
| 22px radius everywhere, pill buttons | The component-library look. Now 3px on photography, 8-10px on the few real containers, 6px on buttons. |
| Card hover lifts and drop shadows | `translateY(-5px)` plus a 54px shadow is a SaaS pricing page. Hover now changes a border. |
| "Clarity is the competitive advantage." | A consulting deck sentence sitting on a nutrition coach's home page. |
| Three placeholder testimonial cards | See **Testimonials** below. These were live on the public URL. |
| Five on-page draft notes to Betty | Also live on the public URL. They are now open items, below, and `DRAFT_NOTES` in `build.py` stays `False`. |

### What was added

- **Four photographs of Betty**, from the set she sent on 3 September 2026. They
  are 945 to 1200px, so for the first time these are downscales rather than
  upscales: the Oregon coast plate, a walking trail, an aircraft seat, and the
  red dress against a wall of woven sisal baskets. Two of them carry captions
  that say where they were taken, which is the cheapest way there is to stop a
  page looking like it was assembled from a library.
- **One recurring device**, replacing the decorative circles: a clay margin note
  in Lora italic with a drawn tick, as if Betty had annotated the page. It only
  ever quotes a line that is already in the approved copy, so it adds art
  direction and no new claim. Three on the whole site.
- **Deliberate irregularity.** Section paddings come in three sizes applied by
  hand, not one. Grounds no longer alternate predictably; the home page runs two
  white sections back to back and two oat ones. Item counts per section now go
  1, 3, 3, 1, 3, 5, 2, 1, 2, 1, 5, 1. Copy under the three subheads of "Who this
  is for" runs 51 words, 12 words and 24 words.
- **Uneven photography.** The three competition frames on About sit at three
  different widths and three different vertical offsets. Their crops stay square,
  because those source frames are composites of two poses and the first attempt
  at three different aspect ratios cut a figure in half. The coast plate runs
  edge to edge up to 1440px and becomes a centred plate above that. The candid on
  the home page overlaps its neighbour.
- **A wide lead article** on the Journal index, with the other five running small
  beneath it.

### What deliberately did not change

The palette. The critique suggested pulling a second accent from her photography,
and the red jacket in the hero and the red dress on About both sample to roughly
`#F2021B`, a saturated primary red. Dropped into this system it clashes with clay
and fails as a UI colour at small sizes. The deck's clay `#C9694A` already *is*
the warm red of this brand. So the reason for the colour comes from putting the
red photographs on the page next to it, not from inventing a token that breaks
the deck.

Also unchanged: Lora + Inter, the hero messaging, Betty's voice, the navigation,
her story, the Food Clarity Method content, the gym videos, and every
accessibility and responsive fix listed below.

---

## Second pass, 7 September 2026: the photography and the last two grids

The first pass fixed the structure and made the remaining **stock photography**
the loudest thing left. It was: three food shots on Resources, a portioned
meal-prep hero on The Method, and six thumbnails of other women on the Journal
index. Alongside Betty running at Cannon Beach and standing in front of her own
sisal baskets, those read as a template again.

**There is now no stock photography on this site.** Every image is hers. Eleven
licensed files were deleted and `STOCK_IN_USE` in `images.py` is `False`; the
Pexels ids stay in that file as the record if any of it is ever wanted back.
`build.py` refuses to write a page that references one of them by name.

Doing that honestly meant three structural changes rather than three swaps,
because **her photo library has no food and no kitchen photography at all**. It
is 21 frames of gym, competition, running, travel and home. "Show Betty
preparing food, grocery shopping, or reading a label" cannot be done today. See
open item 6.

- **Resources is a library, not a product grid.** One resource exists, it is
  free, and the other two are being written; three equal cards with three
  buttons said the opposite. The guide now runs as the feature with **its own
  cover**, set in Lora on forest with a clay spine rather than photographed,
  because the guide is not written yet and a stock food diary beside an apple is
  the exact image this pass exists to remove. The other two run as entries
  marked "Being written". The shared opt-in band is dropped from this page: the
  guide is already the whole page.
- **The Journal is a contents page.** One lead story at full weight, then five
  entries as category, headline and standfirst. Losing the thumbnails lost
  nothing, because they were pictures of strangers.
- **The Method opens on type.** Its stock meal-prep hero is gone and nothing in
  her library belongs in a nutrition page's hero, so the offer page opens on its
  own words, in two columns.
- **One photograph came back into use.** `Screenshot_1`, a trail race with bib
  259 and other ordinary runners on the path behind her, is the least
  physique-posed frame in the library and the only one showing her among other
  people. It sits on About directly beside the line *"You will never be asked to
  train like this."* The photograph and its own disclaimer, in one breath.

Three page heroes now carry a photograph, one carries the guide cover, and two
carry type. That variation is the point.

`build.py` now also asserts that no page contains `REPLACE_ME`, that no page
names a retired stock file, and that no page carries more than two margin notes.

---

## Motion

`assets/site.js`, now 190 lines instead of 490. The whole scroll pipeline is
gone with the things it drove. What is left is behaviour rather than decoration:

- **One reveal.** A 0.7s fade and 18px rise, on block-level containers that opted
  in with `data-rv`. Roughly a third of the sections use it; the rest simply
  appear, which is the point.
- **One masked reveal**, on the `<h1>` of each page, once, with a hand-set
  70ms per-line stagger. Off below 640px, where a fixed line break cannot be
  guaranteed to fit inside the mask.
- The mobile nav, the FAQ accordion, a header that condenses and hides on scroll
  down, and a 280ms page fade.

### Rules the motion still follows

1. **Every hidden state is scoped to `html.js`.** The class is added by an inline
   head script and stripped again by `window.onerror`. No JS means no hiding.
2. **Reveals use position triggers, never ratio thresholds.** `threshold: 0` with
   a negative bottom `rootMargin`. A ratio silently becomes impossible once an
   element grows taller than `viewport / threshold`.
3. **A failsafe reveals everything** 2.2 seconds after `load`, in case an
   observer never fires.
4. `prefers-reduced-motion: reduce` lands every element in its finished state.

---

## Responsive

Measured, not eyeballed. All six pages are probed in an offscreen iframe at
**320, 375, 390, 430, 600, 768, 834, 1024, 1180, 1280, 1440 and 1920 px**, 72
combinations, for horizontal overflow, clipped headline masks, tap targets under
24px and body text under 12.1px. Latest run: **zero** overflow, **zero** clipped
headlines, **zero** undersized targets. The one thing still under 12px is the
logo descriptor, which is logotype rather than copy, and the deck sanctions the
wordmark-only lockup where space is tight.

A separate pass checks contrast on every text node across the six pages against
WCAG AA. Latest run: **zero failures**.

Both passes are reproducible. Serve the site, open any page, and in the console:

```js
const src = await (await fetch('_build/audit.js')).text(); (0, eval)(src);
await audit.contrast();     // every text node, WCAG AA
await audit.responsive();   // 72 probes, 6 pages x 12 widths
```

Serve it with a **threaded** server. Python's single-threaded `http.server`
serialises the asset requests and turns a 1.1s probe into an 18s one.

Tiers are 1180 / 1080 / 980 / 860 / 700 / 640 / 480 plus a landscape-phone query,
and the whole media-query stack is the **last thing in the stylesheet** so a
component rule can never beat it.

Four things that bit on the way here, all invisible in the source:

1. Every fluid `clamp(1rem+4vw, ...)` was **invalid CSS**. Math functions need
   whitespace around `+`, so the whole declaration was dropped and the type scale
   silently fell back to UA defaults.
2. The closed mobile nav panel is `position: fixed` and translated off the right
   edge, which `body { overflow-x }` never clipped. `html { overflow-x: clip }`
   is required.
3. `backdrop-filter` on the sticky header made it the **containing block for its
   fixed descendants**, so the open menu was pinned to the 65px header box
   instead of filling the screen. The blur is off below 980px now, and the panel
   is a full-bleed overlay with a scrim, its top padding measured at open time so
   it clears whatever the header actually is.
4. Every micro label is lifted below 960px, because the audience is women 40+
   reading this on a phone.

---

## Claims and copy

Deck page 28 is a hard constraint, and the August draft broke it:

1. Never guarantee weight loss, body change or a specific result.
2. Frame outcomes around coaching support, education and habits.
3. Avoid cure, reverse, diagnose or medical-treatment language.
4. Use client results only with documentation and permission.
5. Confirm and display relevant credentials and professional scope.

**What changed.** The old home page ran a result card headlined "No longer
pre-diabetic" and described a client's "pre-diabetic diagnosis". Both are
diagnosis and reversal language about a real person. They have been rewritten as
coaching outcomes: the 30 lb story keeps its number, and the cousin's story is
now about understanding her food. The "you can lose the weight without a needle"
line is gone. The blog title about GLP-1 injections is now about what the
medications do and do not teach, which is education rather than a promise.

Copy is otherwise 100% hers, from her Coaching Niche Discovery Form and the deck.
Nothing about her background is invented. The humanization pass changed the
*length* of three paragraphs for layout and left their meaning alone.

`build.py` asserts on the way out. It refuses to write a page containing an em
dash, an en dash, the string "Draft note", a placeholder testimonial, or more
than two eyebrows.

### Testimonials

There are none, and there are none on the page. The previous build shipped three
dashed cards reading "Client testimonial goes here" plus an inline note asking
Betty to send real ones. That was the right instinct in a review build and the
wrong thing to have live on a public URL for a working coach. The section is
removed until real testimonials exist. The two client results that *are* real,
which Betty described herself, stay: they run as unnamed outcomes, in two
different shapes, never as quoted testimonials from named people.

---

## Open items before launch

1. **Booking link.** Every CTA points at `contact.html#book`. Paste the real
   Calendly or TidyCal URL and find/replace `contact.html#book` in `build.py`.
2. **Form endpoint. This is the one thing blocking launch.** Set
   `FORM_ENDPOINT` at the top of `_build/build.py` to a real Formspree endpoint
   from Betty's account and rebuild. Until then both forms are replaced by a
   mailto button, which works but converts worse than a form. The previous build
   posted to `formspree.io/f/REPLACE_ME`, which serves a 404 to a real prospect
   and loses the lead silently, so the mailto is the lesser of the two. A
   Calendly or TidyCal embed on `contact.html` would also do the job.
3. **Client permission** for both result stories, in writing, plus Betty's
   sign-off on the reworded versions. Both stories are hers, reworded to stay
   inside the deck's claims rules on page 28: no diagnosis, cure or reversal
   language, outcomes framed around coaching and habits.
4. **Testimonials.** Send first name plus two or three sentences, photo optional,
   and they go in. The strongest ones name the specific fear she had before
   starting and what actually happened instead, or mention learning to read a
   label. Until then the section stays off the site.
5. **The new photographs need Betty's confirmation.** Five frames are now on
   the site that were not before: the coast, the trail, the aircraft seat and the
   red dress from the 3 September batch, plus the trail race on About. Captions describe the scene rather than asserting who
   is in it. Please confirm (a) that each one is her and she is happy to publish
   it, and (b) that the coast and trail captions are accurate.
6. **Food and kitchen photography does not exist.** Her 21 frames are gym,
   competition, running, travel and home, with nothing of food, cooking, a
   grocery aisle, a label or a plate. That is why The Method opens on type and
   the Journal has no thumbnails. Even phone photographs would change those
   pages: her own kitchen, a plate she actually ate, a label she was reading, her
   hands. This is the single highest-value thing she could send.
7. **Credentials.** Deck non-negotiable 5 asks for professional scope to be
   displayed. Send the certifications and they go on the About page.
8. **Photo credit.** The studio, cable and competition frames look professionally
   shot. Confirm she can publish them and whether the photographer is credited.
9. **Pricing.** Still "Investment shared on your call" everywhere. Send the
   figures and they go live. **The Nutrition Reset** is a suggested second offer,
   so say whether to keep, change or remove it.
10. **Facebook URL.** Intake gave the display name "Beatrice M" only. The footer
   links to email instead of a dead Facebook icon.
11. **The guide itself.** "The label-reading guide for real life" is the named
    lead magnet everywhere. The PDF does not exist yet. The band now shows the
    guide's three headings as type rather than a stock photograph, so a real
    cover or a photo of Betty holding it would slot straight in.
12. **Journal articles.** Six titles from her own keywords, no article pages.
    Write them, or record them and we will transcribe.
13. **Resources page.** Only the free guide is confirmed. **The portion handbook**
    and **Four weeks of real meals** are placeholders marked "Coming soon" so the
    page is not empty. Tell us what to actually sell and at what price.
14. **Photo resolution.** The older frames arrived as 460 to 600px screenshots.
    Every placement is capped so the worst upscale is about 1.2x, which holds.
    The four new photographs are downscales and could carry much larger
    placements if we want them to. The one exception is the coast plate, which
    is generated at 1440px from a 945px original, a 1.52x upscale, because it is
    the site's only full-bleed image.
15. **Domain.** Currently on `github.io`.
16. **Email address.** Everything points at `beatricemwihaki@yahoo.com`. Once
    the real domain exists, a `hello@` address on it reads considerably more
    professional. One constant, `EMAIL`, at the top of `build.py`.

---

## Assets

`assets/img/` is fully self-hosted, no hotlinks, all EXIF stripped.
`_build/images.py` rebuilds it. Betty's own photographs come from
`F:\betty\betty photos\`; the food and reader photography is licensed stock,
downloaded once into `_build/_stock/` (not committed) and processed locally. If
`_stock` is absent the script rebuilds only Betty's photographs and says so.

## Deploy

Pushing to `main` republishes via GitHub Pages.

```bash
python _build/build.py
git add -A && git commit -m "..." && git push
```
