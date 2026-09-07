# Betty | Nutrition education for real life

Website for **Beatrice "Betty" Mwihaki Igeria**, built by Rogue Coach Teams.

**Live:** https://harryroguecoachteams-cmd.github.io/betty-mwihaki/
**Source of truth:** `_build/build.py`. Run it, do not hand-edit the HTML.

**Two constants at the top of `_build/build.py` are still unset, and the build
warns about both every time it runs.** `FORM_ENDPOINT` leaves the opt-in and the
consultation form as a mailto button. `CALENDAR_URL` leaves the site unable to
book the consultation call that Betty's own intake names as its primary goal.
Neither can be set without her accounts. See open items 1 and 3.

```bash
python _build/build.py     # nine pages, plus sitemap.xml and robots.txt
python _build/images.py    # rebuilds assets/img from the originals
python _build/images.py og # rebuilds assets/og.jpg only
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
| `shop.html` | Free guide |
| `blog.html` | Journal |
| `contact.html` | Start here |
| `eating-healthy-not-losing-weight.html` | journal article |
| `read-a-nutrition-label.html` | journal article |
| `what-a-portion-looks-like.html` | journal article |

The deck's nav lists "The Method" and "Coaching" separately. They are one page
here, because there is one offer. Say the word and they split.

`shop.html` is labelled **Free guide** rather than Resources: there is one
resource, it is free, and naming it is both more honest and more clickable than
naming the shelf it sits on. The filename stays so no link anywhere breaks.

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

## The commercial pass, 7 September 2026

The two September passes fixed how the site *looks*. An outside review then
pointed at the right remaining problem, which is a different one:

> The design says premium expert. The evidence on the page still says new
> coaching business.

Nothing visual changed in this pass. No section was redesigned, no component was
added, the palette and the type are untouched. What changed is what the page
claims, how specific it is, and whether a stranger can act on it.

### 1. The hero says who it is for

Was, verbatim from deck page 29:

> Practical nutrition coaching for women who are ready for sustainable progress
> they can maintain.

That sentence fits a diabetes clinic, a sports team, a menopause coach and a
wellness blog equally well. It is now Betty's own positioning statement from
deck page 7, which is far more specific and still entirely hers:

> A practical 16-week nutrition coaching program for women who have tried the
> diets, the supplements and the weight-loss trends and still struggle with
> stubborn weight and belly fat.

The headline above it is unchanged and stays unchanged. It is the one line the
deck says to remember.

### 2. The Nutrition Reset is gone

The pricing section carried three tiers: the free call, the Food Clarity Method,
and a four-week "Nutrition Reset". **That third offer appears in no approved
document.** It is not in the brand deck, not in the Coaching Niche Discovery
Form and not in the web intake. It was invented to fill a third column, and a
cheaper short-format program sitting beside the flagship competes with it for
the same buyer while the brand is still new.

Two tiers now: one conversation, one program. `build.py` refuses to write a page
containing the string "Nutrition Reset" again. If Betty genuinely wants a short
format, it needs a price, a defined four weeks and a reason to choose it over
the sixteen, and then it goes back.

### 3. The client stories say only what Betty said

Her form gives one sentence for the first client: *"I once guided a client who
was suffering from stubborn belly fat and she was pre diabetic. She lost 30 lbs
through nutrition and she learnt how to eat healthy."*

The page had grown past that, into "we did not add a single supplement" and "she
can feed herself now without me". Plausible, probably true, and not something
she told us. On a health page about a real person that is the wrong direction to
drift in, so both stories are back inside her own sentence, minus the medical
wording deck page 28 rules out. The cousin story lost the line "the hardest
client I have ever coached" for the same reason.

### 4. The Journal is real

Three articles are written and live, on the three topics Betty already teaches
inside the sixteen weeks:

| | |
|---|---|
| `eating-healthy-not-losing-weight.html` | Why you are eating healthy and still not losing weight |
| `read-a-nutrition-label.html` | How to read a nutrition label in thirty seconds |
| `what-a-portion-looks-like.html` | What a portion really looks like on your plate |

Before this, every one of the six journal headlines said **Coming soon**, which
tells a stranger the shelves went up before there was anything to put on them.
The three that are not written are in `BACKLOG` in `_build/articles.py`, off the
public site until they exist. `build.py` now refuses to write "Coming soon" onto
any page.

They are drafted in her voice and inside deck page 28: no diagnosis, no cure, no
guaranteed outcome, and anything that edges toward a medical question ends by
sending the reader to their doctor rather than to a coaching call. **Betty has
to read all three and be able to say every sentence out loud.** See open item 5.

Article copy lives in `_build/articles.py`, not in `build.py`. Adding a fourth
means adding one dict.

### 5. First person

She is speaking on her own website. "Betty makes nutrition understandable"
became "I make nutrition understandable", the credibility list on About moved
from *she began teaching yoga* to *I began teaching yoga*, and the position
ladder's last rung is now "I make the next step clear". Deck page 11 asks for
second person and a knowledgeable friend; third person reads as an agency
describing a client.

### 6. The About headline

**Expert enough to trust. Human enough to tell the truth.** is real brand
personality from deck page 10, and it was the wrong h1. The moment a page calls
itself expert, the reader asks what qualification makes it one, and the site
cannot answer that yet. The line stays where the deck put it, in small type at
the end of the personality section. The h1 is now her own history instead of a
self-assessment:

> I know what precision looks like. Real life is not a bodybuilding stage.

### 7. What you actually get

The Method page explained the five phases in full and then explained the weekly
process again. It never listed the deliverables. The second section is now
**What you get for sixteen weeks**: private one-to-one coaching, a nutrition
structure, portion training, label reading, weekly check-ins, real-life problem
solving, and skills you keep. A short version of the same list sits under the
five phases on the home page, so nobody has to reach the pricing page to find
out what is included.

Also softened: *"nothing moves until the one before it is holding"* was a good
sentence and not a true description of coaching a person through sixteen weeks.

### 8. Search and sharing

The site had a title, a description and two Open Graph tags. It now has:

- a canonical URL on every page, from one `SITE_URL` constant
- `og:image`, `og:url`, `og:site_name`, `og:locale`, and a Twitter/X large card
- **`assets/og.jpg`**, a 1200x630 social card built by `images.py` in the deck's
  own type and colors. Without one, every link Betty shares in a WhatsApp group
  or a Facebook post renders as a grey rectangle
- JSON-LD on all nine pages: one `Person` graph referenced by id everywhere,
  plus `Service` for the Food Clarity Method, `FAQPage` on The Method, `Blog`
  and `BlogPosting` on the journal. No rating, no review count, no price and no
  credential, because the site does not have them
- `sitemap.xml` and `robots.txt`, generated by the build
- titles and descriptions rewritten for what she sells rather than for the brand
  line. Home was "Betty | Nutrition Education for Real Life" and is now "Weight
  Loss and Nutrition Coaching for Women | Betty Mwihaki"

`robots.txt` will only be read once the site is on its own domain. GitHub Pages
serves a project site from a subpath, and crawlers read robots.txt from the
domain root.

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

**This is now the biggest single gap on the site, and it is the one nobody at
this end can close.** The design reads as an established practice. The evidence
is one anonymous client and Betty's cousin. Every competitor in this niche runs
four to eight named outcomes. See open item 4 for exactly what to collect.

---

## Open items before launch

Ordered by what it costs to leave undone, not by how hard it is to do. The first
five are the whole distance between a site that looks like an established
practice and a business that reads like one.

### Cannot launch without these

**1. Form endpoint.** Set `FORM_ENDPOINT` at the top of `_build/build.py` to a
Formspree endpoint from Betty's account and rebuild. Until then the opt-in and
the consultation form are both a mailto button: it works, and it converts worse
than a form. The build before this one posted to `formspree.io/f/REPLACE_ME`,
which serves a 404 to a real prospect and loses the lead in silence, so the
mailto is the lesser of two bad options. `build.py` refuses to ship the
placeholder again.

**2. The free guide does not exist.** "The label-reading guide for real life" is
named in the announcement bar, on five pages and in the page titles, and the
button currently opens an email asking Betty to send it. Somebody has to be able
to send a PDF back the same day, or the site's main lead magnet is a promise
with nothing behind it.

There are two ways to close this and we need Betty to pick one:

- Her web intake says **"I have written an EBOOK"** and names a free ebook as the
  freebie. If that ebook fits this niche, we use it, and the section takes its
  real title and cover.
- If it does not fit, the guide gets written. The three headings the site already
  promises are serving size, protein and added sugar, which is exactly the
  content of the new journal article on labels, so most of it is already drafted.

**3. Booking the call.** Betty's own intake names **"CONSULTATION BOOKING
CALLS"** as the primary conversion goal of this website. The website cannot
currently book one. It takes a request and she answers by hand, which asks a
warm prospect to submit, wait, read a reply, agree a time, and come back. Some
of them do not.

Paste a Calendly, TidyCal or Google Appointments link into `CALENDAR_URL` at the
top of `_build/build.py` and rebuild: the Start here page then books the call on
the page, and the questions we ask now move inside the booking flow. Every build
prints a warning until it is set.

### The evidence gap. Nothing here can be done from our end

**4. Four to six more client results.** This is the single biggest commercial
weakness on the site and it is not a design problem. Right now the page carries
one anonymous client and Betty's cousin. A stranger discounts *my cousin got
results* very heavily, and the competitors in this niche all run four to eight
named outcomes.

What to send, per client, in her own words if possible:

- what she had already tried before, and how long she had been trying
- what actually changed, specifically. Pounds, inches, clothes that fit, energy,
  bloodwork she chose to mention, or simply "I stopped restarting every Monday"
- one thing she can now do without Betty. Reading a label, judging a portion,
  eating on holiday, ordering in a restaurant
- first name, and whether we may use it
- optional: a photograph, or a twenty to forty second phone video

No before-and-after body shots. Deck page 26 rules them out and they are not this
brand.

**5. Betty has to sign off on words that are already live.**

- Both client result stories, and **written permission from both clients.** The
  wording is inside what she told us and inside deck page 28, but it is her
  business and her clients.
- **The three journal articles.** They are new writing in her voice on
  `eating-healthy-not-losing-weight.html`, `read-a-nutrition-label.html` and
  `what-a-portion-looks-like.html`. She needs to read all three and be able to
  say every sentence out loud. Anything she would not say, we change.
- The five photographs added on 6 and 7 September: the coast, the trail, the
  aircraft seat, the red dress and the trail race. Please confirm each is her,
  that she is happy to publish it, and that the coast and trail captions are
  accurate.

**6. Credentials, and the professional scope.** Deck non-negotiable 5 asks for
relevant credentials to be confirmed and displayed, and the site currently
displays none, because nobody has told us what she holds. Send anything real:
a nutrition or coaching certification, the yoga qualification, the competition
placing and year, how long she has been coaching, how many women she has worked
with.

If there is no formal nutrition credential, that is genuinely fine and we do not
invent one. Her authority in this brand is meant to be earned, specific and
human, and the About page is built that way. But we should know before launch,
because the answer changes how confidently the page can speak.

### Everything else

**7. Domain and email.** Both are one constant each at the top of `build.py`:
`SITE_URL` and `EMAIL`. Everything follows them, including every canonical tag,
the sitemap, the social card URL and the structured data. `github.io` and a
Yahoo address are the two details on the site that most contradict the rest of
it. A `hello@` on her own domain is a small change with an outsized effect.

**8. Pricing.** Both tiers still read "Investment shared on your call". That is
a defensible choice and it is also the one thing on the page a buyer can wonder
about, so it is worth testing "Investment from $X" or "most clients invest $X to
$Y" once there is a number. **Send the figure and we will make the call on how
to show it.** No price is invented here.

**9. Food and kitchen photography still does not exist.** Her 21 frames are gym,
competition, running, travel and home. Nothing of food, cooking, a grocery aisle,
a label or a plate. That is why The Method opens on type, the Journal has no
images and the guide's cover is set rather than photographed. Even phone
photographs would change those pages: her own kitchen, a plate she actually ate,
a label she was reading, her hands. **This remains the highest-value thing she
could send.**

**10. Social profiles.** The site says *Betty. Nutrition education for real
life.* TikTok says `@betty_fit8`. Nothing is wrong with the handle, but if the
account reads as gym content, a visitor who clicks through gets a different
business than the one she just read about, and deck page 26 specifically warns
against looking fitness-only. Before launch: matching profile photo, the B.
monogram or wordmark where it fits, bios that name the Food Clarity Method, and
a pinned post that introduces the niche.

**11. Facebook URL.** The intake gave the display name "Beatrice M" only, so the
footer links to email rather than a dead Facebook icon.

**12. Photo credit.** The studio, cable and competition frames look
professionally shot. Confirm she can publish them and whether the photographer
is credited.

**13. Photo resolution.** The older frames arrived as 460 to 600px screenshots
and every placement is capped so the worst upscale is about 1.2x. The four newer
photographs are downscales and could carry much larger placements. The one
exception is the coast plate, generated at 1440px from a 945px original, a 1.52x
upscale, because it is the site's only full-bleed image.

**14. The rest of the Journal.** Three more titles are drafted as headlines only
and sit in `BACKLOG` in `_build/articles.py`: weight-loss medications, stubborn
belly fat after 40, and four questions to start with. They are off the site
until they are written. Betty can record them as voice notes and we will
transcribe.

**15. The other two resources.** "The portion handbook" and "Four weeks of real
meals" were on the Resources page marked as being written. They are off it now,
because one real product beside two that do not exist reads as an empty shelf.
Tell us what to actually build and whether either is paid.

---

## Assets

`assets/img/` is fully self-hosted, no hotlinks, all EXIF stripped.
`_build/images.py` rebuilds it.

**`assets/og.jpg`** is the 1200x630 social card, drawn by `images.py` rather
than screenshotted so it stays on the deck: forest ground, the wordmark with its
clay point, the one line to remember set in Lora, and her own photograph on the
right. Rebuild it alone with `python _build/images.py og`. It needs Lora and
Inter in `_build/_fonts/`, which are gitignored and downloaded from
`github.com/google/fonts`; without them the script falls back to Georgia, which
is this site's own declared serif fallback. The card is committed, so this only
matters if you are changing it. Betty's own photographs come from
`F:\betty\betty photos\`; the food and reader photography is licensed stock,
downloaded once into `_build/_stock/` (not committed) and processed locally. If
`_stock` is absent the script rebuilds only Betty's photographs and says so.

## Deploy

Pushing to `main` republishes via GitHub Pages.

```bash
python _build/build.py                       # nine pages, sitemap, robots
git add -A && git commit -m "..." && git push
```

`sitemap.xml` and `robots.txt` are generated by the build, so never hand-edit
them. Both read `SITE_URL` from the top of `build.py`, along with every canonical
tag, every Open Graph URL and the whole JSON-LD graph. **Changing the domain is
one line and a rebuild.**
