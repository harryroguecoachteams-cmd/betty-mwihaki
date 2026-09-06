# Betty | Nutrition education for real life

Website for **Beatrice "Betty" Mwihaki Igeria**, built by Rogue Coach Teams.

**Live:** https://harryroguecoachteams-cmd.github.io/betty-mwihaki/
**Source of truth:** `_build/build.py`. Run it, do not hand-edit the HTML.

```bash
python _build/build.py     # regenerates all six pages
```

---

## What this is

A static six-page site built to the **Betty Brand Identity Deck** (September 2026).
The first draft, from August 2026, followed a Kajabi reference layout in teal and
coral. That is gone. Everything below now comes from the deck.

| Deck | Here |
|---|---|
| Lora headlines + Inter body | same, variable weights from Google Fonts |
| Forest `#1F3D33`, Clay `#C9694A`, Sage `#8FA99B`, Oat `#F4F0E8`, White | full token set in `assets/style.css` |
| 60% forest and white / 25% oat and sage / 15% clay | section rhythm alternates white, oat, forest; clay is accent only |
| "Betty" wordmark with one clay point | header, footer, favicon |
| Nav: About, The Method, Coaching, Resources, Start here | About, The Method, Resources, Journal, Start here |
| Hero: "Stop Guessing What to Eat. Start Understanding Your Food." | home `<h1>`, verbatim |
| Hero strip: Food clarity / Simple action / Confidence | forest band under the hero |
| Her words (p5) | full-width pull quote, home |
| The woman we serve (p4) | "You are not new to trying" + three cards |
| Position: The noise / The gap / Betty (p6) | animated triptych with drawn connectors |
| Transformation: Confused, Capable, Confident (p3) | scroll-scrubbed clarity field |
| The Food Clarity Method, five phases (p14) | drawn arc on home, full timeline on The Method |
| Credibility (p15), Personality (p10) | About |
| Five principles (p9) | home, replacing the old "I believe that" list |
| Signature language (p13) | slow marquee |
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

## Motion

`assets/site.js`. One `requestAnimationFrame` scroll loop drives every scrubbed
element; nothing polls and nothing uses a second library. The brand personality
is "steady, no hype and no urgency theater", so everything is slow, eased on a
single curve (`cubic-bezier(.16,1,.3,1)`) and used once per idea.

- **The confidence point.** The clay dot in the wordmark settles on load, marks
  every section eyebrow, and travels down the right-hand rail as a scroll
  wayfinder with clickable section ticks.
- **Masked line reveals.** Editorial headlines rise line by line out of an
  overflow mask. Off below 640px, where a fixed line break cannot be guaranteed
  to fit.
- **Image reveals.** A clip wipe plus a settle from 1.13, with a slow rAF
  parallax on the inner frame.
- **The clarity field** (home, "Confusion becomes confidence"). 49 dots scrubbed
  from a seeded chaos to a settled 7x7 grid as you scroll, with the clay point
  arriving last. The three stage labels light in step.
- **The drawn arc** (home and The Method). The five-phase path draws itself via
  `stroke-dashoffset`, and the nodes are positioned with `getPointAtLength` so
  they sit exactly on the curve. Below 861px it becomes a vertical timeline with
  the same scrub.
- Signature-language marquee, count-ups, the wiping button fill, nav underlines
  that wipe out the way they wiped in, a header that condenses and hides on
  scroll down, and a 290ms page fade between pages.

### Rules the motion follows

1. **Every hidden state is scoped to `html.js`.** The class is added by an inline
   head script and stripped again by `window.onerror`. No JS means no hiding.
2. **Reveals use position triggers, never ratio thresholds.** `threshold: 0` with
   a negative bottom `rootMargin`. A ratio silently becomes impossible once an
   element grows taller than `viewport / threshold`.
3. **Nothing expensive is animated by the compositor.** The ambient circles are
   flat opaque divs with no blur, blend or mask, and their resting state is the
   visible one, so a stalled animation is invisible rather than fatal.
4. **A failsafe reveals everything** 2.2 seconds after `load`, in case an
   observer never fires.
5. `prefers-reduced-motion: reduce` lands every element in its finished state and
   turns off the marquee, the parallax, the scrubs and the page fade.

---

## Responsive

Measured, not eyeballed. All six pages were probed in an offscreen iframe at
**320, 375, 390, 430, 600, 768, 834, 1024, 1180, 1280, 1440 and 1920 px**, 72
combinations, for horizontal overflow, clipped headline masks, tap targets under
24px and body text under 12.1px. Final run: **zero** overflow, **zero** clipped
headlines, **zero** undersized targets. The one thing still under 12px is the
logo descriptor, which is logotype rather than copy, and the deck sanctions the
wordmark-only lockup where space is tight.

A separate pass checked contrast on all 657 text nodes across the six pages
against WCAG AA. It found eight sage-on-light failures at 2.1 to 2.5:1 and, worse,
forest-on-forest text in the CTA band at 1:1, because `.cta` was a forest section
that never carried the `.bg-forest` class. Both are fixed; sage now has a text
weight (`--sage-ink`) and the plain `--sage` is reserved for shapes, rules and
text on forest. Final run: **zero failures**.

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

Four things that bit, all invisible in the source:

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

Betty still needs to confirm the new wording and get each client's permission
before launch. Copy is otherwise 100% hers, from her Coaching Niche Discovery
Form and the deck. Nothing about her background is invented, and the testimonial
cards are deliberately visible placeholders.

House style: US English, no em dashes. `build.py` asserts on both.

---

## Open items before launch

1. **Booking link.** Every CTA points at `contact.html#book`. Paste the real
   Calendly or TidyCal URL and find/replace `contact.html#book` in `build.py`.
2. **Form endpoint.** The opt-in and contact forms post to
   `https://formspree.io/f/REPLACE_ME`. They do nothing until that is swapped.
3. **Client permission** for both result stories, in writing, plus Betty's
   sign-off on the reworded versions.
4. **Testimonials.** Three placeholder cards on the home page, clearly marked.
5. **Credentials.** Deck non-negotiable 5 asks for professional scope to be
   displayed. Send the certifications and they go on the About page.
6. **Photo resolution.** Betty's photos arrived as 460 to 600px screenshots.
   Every placement is capped so the worst upscale is about 1.2x, which holds,
   but originals would let the heroes get bigger. The red-jacket frame the deck
   chose is now the home hero.
7. **Photo credit.** The studio, cable and pull-up frames look professionally
   shot. Confirm she can publish them and whether the photographer is credited.
8. **Pricing.** Still "Investment shared on your call" everywhere.
9. **Facebook URL.** Intake gave the display name "Beatrice M" only. The footer
   now links to email instead of a dead Facebook icon.
10. **The guide itself.** "The label-reading guide for real life" is the named
    lead magnet everywhere. The PDF does not exist yet.
11. **Journal articles.** Six titles from her own keywords, no article pages.
12. **Domain.** Currently on `github.io`.

---

## Assets

`assets/img/` is now fully self-hosted, no Pexels hotlinks. Betty's own photos
are processed from `F:\betty\betty photos\` by `_build/build.py`'s companion
image step (see the session notes); stock food and reader photography is from
Pexels and stored locally. All EXIF is stripped.

## Deploy

Pushing to `main` republishes via GitHub Pages.

```bash
python _build/build.py
git add -A && git commit -m "..." && git push
```
