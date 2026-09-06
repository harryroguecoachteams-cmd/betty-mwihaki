# -*- coding: utf-8 -*-
"""
Generates the six pages of bettymwihaki.com from one shell, so the header,
footer, freebie band and CTA stay identical everywhere.

    python _build/build.py

Copy is taken from the Betty Brand Identity Deck (Rogue Coach Teams) and from
Betty's own Coaching Niche Discovery Form. Nothing about her background or her
client outcomes is invented. House style: US English, no em dashes.

September 2026 humanization pass
--------------------------------
The previous build was correct and consistent, and that was the problem: twelve
sections in a row made from one kit, an eyebrow above every heading, 01/02/03
four separate times, three equal rounded cards whenever there happened to be
three of something. This pass keeps the copy, the palette, the type and the
information architecture, and breaks the template:

  * eyebrows survive in three places on the whole site, where they carry
    information rather than describe what the section is doing;
  * numbering survives only on the five phases, where the sequence is real;
  * card grids are replaced by open editorial layouts wherever the content did
    not genuinely need containment (pricing and products still do);
  * card counts and copy lengths are deliberately uneven;
  * the marquee, the animated clarity field, the drawn SVG arc and the scroll
    rail are gone;
  * one recurring device replaces the generic decorative circles: a clay margin
    note, set in Lora italic with a drawn tick, quoting a line that is already
    in the approved copy. Three of them on the whole site.

Draft notes to Betty used to render on the public pages. They are now in
README.md under "Open items" and DRAFT_NOTES stays False.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..'))

# Internal notes never ship. Flip to True only for a local review build.
DRAFT_NOTES = False

# Both forms post here. Create a form in Betty's Formspree account, paste the
# full endpoint below, rebuild, and the opt-in and the consultation form go live
# everywhere at once.
#
# While this is None the forms are replaced by a mailto button, so a visitor
# still reaches her inbox. That is a downgrade, but the previous build posted to
# `formspree.io/f/REPLACE_ME`, which serves a 404 to a real prospect and loses
# the lead silently. FORBIDDEN blocks that placeholder from ever shipping again.
FORM_ENDPOINT = None          # e.g. 'https://formspree.io/f/xdkogqyz'
EMAIL = 'beatricemwihaki@yahoo.com'

NAV = [
    ('about.html', 'About'),
    ('services.html', 'The Method'),
    ('shop.html', 'Resources'),
    ('blog.html', 'Journal'),
]
BOOK = 'contact.html#book'


# --------------------------------------------------------------- fragments --
def lines(*ls):
    """Authored line breaks in a headline. These are art direction, not a
    motion hook: the mask that used to clip and reveal each line is gone, so a
    line that runs long now simply wraps."""
    return '\n        '.join(
        '<span class="ln"><span>%s</span></span>' % l for l in ls)


def eyebrow(t, extra=''):
    """Three of these exist on the whole site. If you are about to add a
    fourth, the section probably needs a better headline instead."""
    return '<p class="eyebrow%s">%s</p>' % ((' ' + extra) if extra else '', t)


ARROW = ('<svg class="ar" viewBox="0 0 19 9" fill="none" aria-hidden="true">'
         '<path d="M0 4.5h16.5M13 1l3.9 3.5L13 8" stroke="currentColor" '
         'stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# The one recurring device. A drawn tick, then a line in Lora italic, sitting
# in the margin the way a note gets written beside a paragraph.
TICK = ('<svg class="tick" viewBox="0 0 26 38" fill="none" aria-hidden="true">'
        '<path d="M1.6 1.4c-.2 9.6.5 16.5 2.5 21 2.4 5.4 8.2 8.8 19.4 10.3" '
        'stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>'
        '<path d="M19.2 28.4L24 32.3l-4.6 3.3" stroke="currentColor" '
        'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def note(text):
    """A margin note. Only ever quotes a line that is already in the approved
    copy, so it adds art direction and no new claim."""
    return '<p class="note">%s<span>%s</span></p>' % (TICK, text)


def btn(href, label, kind='clay', cls=''):
    return '<a class="btn btn-%s %s" href="%s">%s</a>' % (kind, cls, href, label)


def tlink(href, label):
    return '<a class="tlink" href="%s">%s%s</a>' % (href, label, ARROW)


def img(src, alt, cls='', ar='', pos=''):
    """No clip wipe, no scale settle, no parallax frame. An image is an image."""
    st = (' style="--ar:%s"' % ar) if ar else ''
    ps = (' style="object-position:%s"' % pos) if pos else ''
    return ('<div class="imgwrap %s"%s>'
            '<img src="assets/img/%s" alt="%s" loading="lazy" decoding="async"%s>'
            '</div>') % (cls, st, src, alt, ps)


def hero_img(src, alt, cls='', ar=''):
    """Above the fold: never lazy, and it is the LCP element."""
    st = (' style="--ar:%s"' % ar) if ar else ''
    return ('<div class="imgwrap %s"%s>'
            '<img src="assets/img/%s" alt="%s" fetchpriority="high" decoding="async">'
            '</div>') % (cls, st, src, alt)


def figure(src, alt, caption, cls='', ar='', pos=''):
    """A photograph that says where it was taken. Captions are how a page stops
    looking like it was assembled from a library."""
    return ('<figure class="fig %s">%s<figcaption>%s</figcaption></figure>'
            % (cls, img(src, alt, '', ar, pos), caption))


def todo(html):
    return html if DRAFT_NOTES else ''


def mailto(subject, label, kind='clay'):
    return btn('mailto:%s?subject=%s' % (EMAIL, subject.replace(' ', '%20')),
               label, kind)


# The opt-in, and what stands in for it until FORM_ENDPOINT is set.
if FORM_ENDPOINT:
    OPTIN = u'''<form class="optin" action="%s" method="POST">
          <input type="text" name="name" placeholder="First name" aria-label="First name" required>
          <input type="email" name="email" placeholder="Your email address" aria-label="Email address" required>
          <input type="hidden" name="_subject" value="New download - The label-reading guide for real life">
          <button class="btn btn-clay" type="submit">Send it to me</button>
        </form>
        <p class="form-note">No spam. Unsubscribe any time.</p>''' % FORM_ENDPOINT
else:
    OPTIN = u'''<div class="actions">%s</div>
        <p class="form-note">Email me and I will send it straight back.</p>''' % (
        mailto('The label-reading guide for real life', 'Ask me for the guide'))


# ------------------------------------------------------------------ shell ---
HEAD = u"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1F3D33">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300..700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/favicon.svg">
<script>document.documentElement.classList.add('js');window.addEventListener('error',function(){{document.documentElement.classList.remove('js')}},true);</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="announce">
  <b>Free guide</b> &nbsp;The label-reading guide for real life.
  <a href="index.html#guide">Get your copy</a>
</div>

<header class="site-header">
  <div class="nav-scrim" id="navScrim"></div>
  <div class="header-inner">
    <a class="logo" href="index.html" aria-label="Betty, nutrition education for real life">
      <span class="logo-name">Betty<span class="pt"></span></span>
      <span class="logo-sub">Nutrition education for real life</span>
    </a>
    <button class="nav-toggle" id="navToggle" aria-label="Menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav" aria-label="Main">
      {nav}
      <a class="btn btn-clay btn-sm" href="{book}">Start here</a>
    </nav>
  </div>
</header>

<main id="main">
"""

FOOT = u"""</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="logo footer-logo">
          <span class="logo-name">Betty<span class="pt"></span></span>
          <span class="logo-sub">Nutrition education for real life</span>
        </div>
        <p style="margin-top:20px;max-width:340px">
          Practical nutrition coaching for women who are done guessing.
          Understand your food, build a routine you can keep, and stop
          starting over.
        </p>
        <div class="socials">
          <a href="https://www.instagram.com/betty_mwihaki/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.05 1.8.25 2.2.42.6.22 1 .48 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c0 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2 0-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c0-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.2A6.6 6.6 0 1 0 18.6 12 6.6 6.6 0 0 0 12 5.4zm0 10.9A4.3 4.3 0 1 1 16.3 12 4.3 4.3 0 0 1 12 16.3zm6.9-11a1.55 1.55 0 1 1-1.55-1.55A1.55 1.55 0 0 1 18.9 5.3z"/></svg></a>
          <a href="https://www.tiktok.com/@betty_fit8" target="_blank" rel="noopener" aria-label="TikTok"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.6 5.8a4.3 4.3 0 0 1-1-2.8h-3v12.2a2.6 2.6 0 1 1-1.8-2.5V9.6a5.6 5.6 0 1 0 4.8 5.6V9.3a7.3 7.3 0 0 0 4.3 1.4V7.7a4.3 4.3 0 0 1-3.3-1.9z"/></svg></a>
          <a href="mailto:beatricemwihaki@yahoo.com" aria-label="Email Betty"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5.5h18c.55 0 1 .45 1 1v11c0 .55-.45 1-1 1H3c-.55 0-1-.45-1-1v-11c0-.55.45-1 1-1zm1.6 2L12 12.6l7.4-5.1H4.6z"/></svg></a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Betty</a></li>
          <li><a href="services.html">The Method</a></li>
          <li><a href="shop.html">Resources</a></li>
        </ul>
      </div>
      <div>
        <h4>Learn</h4>
        <ul>
          <li><a href="blog.html">Journal</a></li>
          <li><a href="index.html#guide">Free guide</a></li>
          <li><a href="services.html#faq">Questions</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Start here</h4>
        <p>Book a free 20-minute conversation and find out whether the 16-week
        method is the right fit for you.</p>
        <a class="btn btn-ghost btn-sm auto" href="{book}">Book a free call</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Beatrice Mwihaki Igeria. All rights reserved.</span>
      <span>Site by <a href="https://roguecoachteams.com" target="_blank" rel="noopener">Rogue Coach Teams</a></span>
    </div>
  </div>
</footer>

<div class="disclaimer">
  <div class="wrap">
    Betty provides nutrition coaching and education for general wellness. It is
    not medical advice, diagnosis or treatment, and it is not a substitute for
    care from your doctor or a registered dietitian. Coaching supports habits,
    understanding and accountability; individual results differ. Please speak to
    your physician before changing how you eat or exercise, especially if you
    are managing a medical condition, are pregnant, or take prescription
    medication.
  </div>
</div>

<script src="assets/site.js" defer></script>
</body>
</html>
"""


def shell(page, title, desc, body):
    nav = '\n      '.join(
        '<a href="%s"%s>%s</a>' % (h, ' class="active"' if h == page else '', l)
        for h, l in NAV)
    return (HEAD.format(title=title, desc=desc, nav=nav, book=BOOK)
            + body + FOOT.format(book=BOOK))


# ------------------------------------------------------- shared components --
# The free guide is the one place an eyebrow earns its keep: "Free guide" is
# information. The visual is the guide's actual content, set as type, instead of
# a stock photograph of somebody else's food diary.
GUIDE = u"""
<section class="s guide" id="guide">
  <div class="wrap">
    <div class="split lean">
      <div class="split-copy">
        {eyebrow}
        <h2>{h}</h2>
        <p class="lede">Serving size, protein, added sugar. Three numbers, in
        that order, and you can judge almost any packet in the aisle. This is the
        short, plain-English guide I wish every woman had before she started
        another diet.</p>
        {optin}
      </div>
      <div class="split-media">
        <div class="three" aria-hidden="true">
          <p>Serving size</p>
          <p>Protein</p>
          <p>Added sugar</p>
        </div>
        {n}
      </div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('Free guide'),
           h=lines('The label-reading', 'guide for real life'),
           optin=OPTIN,
           n=note('Three numbers, in that order.'))


def cta(h_lines, sub, label='Book a free call'):
    return u"""
<section class="cta">
  <div class="wrap">
    <div class="cta-grid">
      <h2>{h}</h2>
      <div>
        <p class="lede">{sub}</p>
        <div class="actions">
          {btn}
          {tl}
        </div>
      </div>
    </div>
  </div>
</section>
""".format(h=lines(*h_lines), sub=sub, btn=btn(BOOK, label, 'clay'),
           tl=tlink('services.html', 'See the 16-week method'))


PHASES = [
    ('Clarify', 'See the current patterns, confusion and real starting point.',
     'We start with the week you actually have, not an ideal one. What you have '
     'already tried, what happened each time, and where the confusion is coming '
     'from. Nothing here is a test and there is no wrong answer.'),
    ('Understand', 'Learn food, portions and the reason behind each choice.',
     'Labels, portions, protein, carbohydrates. You learn what each one does and '
     'roughly how much you personally need, so every food on your plate is there '
     'for a reason you can say out loud.'),
    ('Apply', 'Put the knowledge to work in everyday meals and routines.',
     'We build the structure around your kitchen, your budget and your schedule. '
     'Not a printed plan you abandon on the first difficult day, but a way of '
     'deciding that still works in a restaurant or at a family table.'),
    ('Stay consistent', 'Use support and accountability to keep moving.',
     'Weekly check-ins, honest feedback and adjustments as your body responds. '
     'One imperfect meal is still just one meal. This is the phase where most '
     'women stop starting over.'),
    ('Own it', 'Trust the skills and maintain progress beyond the program.',
     'By the end you should not need me. That is the design. You can read a '
     'label, judge a portion and adjust when life changes, without waiting for '
     'anyone to give you permission.'),
]


def phase_list(full=False):
    """The five phases, as a plain editorial timeline. This is the only place on
    the site that still numbers anything, because here the order is the point."""
    items = []
    for i, (name, short, long) in enumerate(PHASES):
        items.append(
            '      <li class="phase">\n'
            '        <p class="p">Phase 0%d</p>\n'
            '        <h3>%s</h3>\n'
            '        <p class="d">%s</p>\n'
            '      </li>' % (i + 1, name, long if full else short))
    return '    <ol class="phases">\n%s\n    </ol>\n' % '\n'.join(items)


PRINCIPLES = [
    ('Understand your food',
     'Learn the reason, never just the rule. If you cannot say out loud why a '
     'food is on your plate, the plan is doing the thinking for you, and it will '
     'stop working the first week life gets complicated.'),
    ('Keep it practical', 'It has to work in an ordinary week.'),
    ('Progress over perfection',
     'One meal never becomes a verdict. You are allowed a bad Tuesday.'),
    ('You do not do it alone', 'Support and accountability stay human.'),
    ('Learn it for life',
     'Build capability, not dependency. The whole design is that you leave.'),
]


# =============================================================== index.html ==
def build_index():
    b = []

    # ------------------------------------------------------------------ hero
    # The floating circles are gone. The 16-week badge is now a caption bolted
    # to the bottom of the photograph rather than a white card hovering over it.
    b.append(u"""
<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      {eyebrow}
      <h1 data-rv="lines">{h}</h1>
      <p class="lede">Practical nutrition coaching for women who are
      ready for sustainable progress they can maintain.</p>
      <div class="actions">
        {b1}
        {tl}
      </div>
    </div>
    <figure class="hero-art">
      {im}
      <figcaption>
        <b>Sixteen weeks</b>
        <span>Clarity, action, accountability</span>
      </figcaption>
    </figure>
  </div>
</section>

<div class="strip">
  <div class="wrap">
    <p>Food clarity<i></i>Simple action<i></i>Confidence</p>
  </div>
</div>
""".format(eyebrow=eyebrow('The Food Clarity Method'),
           h=lines('Stop guessing', 'what to eat.', 'Start understanding',
                   'your food.'),
           b1=btn('services.html', 'Explore the 16-week method', 'clay'),
           tl=tlink('services.html#phases', 'See how it works'),
           im=hero_img('betty-hero.jpg',
                       'Betty smiling on the water in a red jacket', 'tall')))

    # -------------------------------------------------------------- her words
    b.append(u"""
<section class="s tight statement">
  <div class="wrap">
    <div class="statement-grid">
      <p class="q" data-rv>{q}</p>
      <div class="after">
        <p class="lede">If you have said a version of that out loud, you are
        in the right place. No shame and no panic. Just practical education and
        steady support until food makes sense again.</p>
        <div class="actions">{tl}</div>
      </div>
    </div>
  </div>
</section>
""".format(q=lines('&ldquo;I am eating', 'healthy, but I am',
                   'still not losing', 'weight. I do not',
                   '<em>know what to try next.</em>&rdquo;'),
           tl=tlink('about.html', 'Meet Betty')))

    # ------------------------------------------------------- who this is for
    # Was three equal rounded cards numbered 01/02/03. Now one column of running
    # editorial with hanging subheads and deliberately uneven paragraphs.
    b.append(u"""
<section class="s">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
      </div>
      <div class="ed-body" data-rv>
        <p class="lede">You have tried diets, supplements and weight-loss
        trends. You are tired of being handed another rule without any real
        understanding of why it is supposed to work.</p>
        <div class="ed-row">
          <h3>Where you are</h3>
          <p>You still struggle with stubborn weight and belly fat, even in the
          weeks when you feel like you are doing everything right. You have read
          the articles and followed the accounts. You have probably been stricter
          with yourself than anyone reading this would guess, and the mirror has
          not agreed with the effort.</p>
        </div>
        <div class="ed-row">
          <h3>What keeps frustrating you</h3>
          <p>Every source tells you something different, and all of them sound
          certain.</p>
        </div>
        <div class="ed-row">
          <h3>What you actually need</h3>
          <p>Clear guidance, a structure that survives a real week, and someone
          holding you to it who is not going to judge you.</p>
        </div>
      </div>
    </div>
  </div>
</section>
""".format(h=lines('You are not new', 'to trying.')))

    # ----------------------------------------------- the difference + a plate
    # Was three connected rounded panels with animated connector lines, then a
    # line reading "Clarity is the competitive advantage", which is a consulting
    # deck sentence and not something Betty would say. Both are gone.
    b.append(u"""
<section class="s bg-oat">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
        <p class="lede">She cuts through the conflicting advice first, then
        turns what is left into a routine you can actually keep.</p>
      </div>
      <div class="ed-body">
        <div class="ladder" data-rv>
          <div class="rung">
            <p class="k">The noise</p>
            <p class="t">Diets, supplements and weight-loss trends.</p>
          </div>
          <div class="rung">
            <p class="k">What is missing</p>
            <p class="t">Understanding what, how much and why to eat.</p>
          </div>
          <div class="rung her">
            <p class="k">Betty</p>
            <p class="t">The practical coach who makes the next step clear.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="plate">
    {fig}
  </div>
</section>
""".format(h=lines('Betty makes nutrition', 'understandable.'),
           fig=figure('coast-wide.jpg',
                      'Running barefoot on wet sand at Haystack Rock on the '
                      'Oregon coast',
                      'Cannon Beach, Oregon. Not a training session. Just a '
                      'good day.',
                      'plate-img', '2.35/1')))

    # ------------------------------------------------------ confusion to confidence
    # Was a scroll-scrubbed field of 49 dots resolving from chaos into a grid,
    # labelled Noise and Clarity. Clever, abstract, and it could have belonged to
    # any consultancy. Replaced with a photograph of Betty and a plain sequence.
    b.append(u"""
<section class="s">
  <div class="wrap">
    <div class="split reverse lean">
      <div class="split-media">{fig}</div>
      <div class="split-copy">
        <h2 data-rv>{h}</h2>
        <p class="lede">The outcome is not perfect eating. It is knowing what
        to do next, and why.</p>
        <div class="seq" data-rv>
          <div class="st">
            <h3>Confused</h3>
            <p>Rules, fear and conflicting advice.</p>
          </div>
          <div class="st">
            <h3>Capable</h3>
            <p>Food choices make sense in real life.</p>
          </div>
          <div class="st on">
            <h3>Confident</h3>
            <p>You can adjust without starting over.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
""".format(h=lines('Confusion becomes', 'confidence.'),
           fig=figure('betty-trail.jpg',
                      'On a walking trail on a bright morning, hand raised '
                      'against the sun',
                      'An ordinary morning, on an ordinary trail.',
                      'tall-fig', '0.82/1')))

    # ------------------------------------------------------------- the method
    b.append(u"""
<section class="s bg-forest">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
        <p class="lede">A practical 16-week weight-loss and nutrition coaching
        journey, in five phases. Each one does a single job, and nothing moves
        until the one before it is holding.</p>
        <div class="actions">{b1}</div>
      </div>
      <div class="ed-body" data-rv>
{phases}
      </div>
    </div>
  </div>
</section>
""".format(h=lines('The Food', 'Clarity Method'),
           phases=phase_list(),
           b1=btn('services.html', 'See the full method', 'ghost', 'auto')))

    # ---------------------------------------------------------- meet betty
    # Two photographs at two different sizes, one of them overlapping, plus a
    # caption. Asymmetric on purpose.
    b.append(u"""
<section class="s airy">
  <div class="wrap">
    <div class="split reverse">
      <div class="split-media stack-media">
        {im}
        {fig}
      </div>
      <div class="split-copy">
        <h2 data-rv>{h}</h2>
        <p>I began teaching yoga in Kenya at eighteen, guided by
        Mrs Kanja, who was the first person to sit me down and teach me about
        eating well. Preparing for bodybuilding competitions in the States is
        where precision nutrition stopped being a theory for me.</p>
        <p>Then my own body stopped responding the way it used to, and
        I understood the frustration from the inside. There is so much health
        information out there that it has become genuinely impossible for a
        normal person to tell what is real and what is marketing.</p>
        <p>Taking the complicated and making it simple is my natural
        gift. It is also the whole job.</p>
        <div class="actions">{tl}</div>
      </div>
    </div>
  </div>
</section>
""".format(h=lines('I take the', 'complicated and', 'make it simple.'),
           im=img('betty-portrait.jpg',
                  'Betty smiling in a Strength tee, beside a framed photograph '
                  'of herself competing', 'tall'),
           fig=figure('betty-cabin.jpg', 'Smiling in an aircraft seat',
                      'Somewhere over the Atlantic.', 'inset-fig', '1/1'),
           tl=tlink('about.html', 'Read her story')))

    # ------------------------------------------------------------- statement
    # This replaces the infinite scrolling marquee of four brand lines.
    b.append(u"""
<section class="s tight bg-oat">
  <div class="wrap">
    <p class="big" data-rv>Progress comes from<br>what you <em>repeat</em>.</p>
  </div>
</section>
""")

    # --------------------------------------------------------------- results
    # Two stories, two different shapes. The three placeholder testimonial cards
    # that used to follow are gone: they were dashed boxes reading "Client
    # testimonial goes here" on a live public page.
    b.append(u"""
<section class="s">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
        <p class="lede">Two stories in Betty's own words. Coaching supports
        habits, understanding and accountability. It is not a promise of a
        particular result.</p>
      </div>
      <div class="ed-body">
        <div class="figure-row" data-rv>
          <p class="stat"><b>30</b><span>pounds</span></p>
          <div>
            <p>She had already tried plan after plan when she came to me. We did
            not add a single supplement. We changed how she ate and she learned
            the reason behind every choice. Thirty pounds down, and she can feed
            herself now without me.</p>
            <p class="who">Nutrition coaching client</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <blockquote class="band" data-rv>
    <div class="wrap">
      <p class="pull">The hardest client I have ever coached.</p>
      <p>My own cousin. She came to me worried about where her health was
      heading and we worked through her nutrition together, month after month.
      Family is the hardest audience there is, and the most worth it. She
      understands her food now, and she is not guessing anymore.</p>
      <footer>Nutrition coaching client</footer>
    </div>
  </blockquote>
</section>
""".format(h=lines('What has happened', 'for the women I coach.')))

    b.append(GUIDE)

    # ------------------------------------------------------------ principles
    b.append(u"""
<section class="s">
  <div class="wrap narrow">
    <h2 class="mb-l" data-rv>{h}</h2>
    <div class="beliefs">
{rows}
    </div>
  </div>
</section>
""".format(h=lines('Five beliefs behind', 'every conversation.'),
           rows='\n'.join(
               '      <div class="belief"><h3>%s</h3><p>%s</p></div>' % (t, d)
               for t, d in PRINCIPLES)))

    b.append(cta(['Stop guessing', 'what to eat.'],
                 'Book a free 20-minute conversation. We will talk through what '
                 'you have already tried, what is actually getting in the way, '
                 'and whether the 16-week method is right for you.'))

    return shell(
        'index.html',
        'Betty | Nutrition Education for Real Life',
        'Practical nutrition coaching for women who are ready for sustainable '
        'progress they can maintain. Stop guessing what to eat and start '
        'understanding your food.',
        ''.join(b))


# =============================================================== about.html ==
def build_about():
    b = []
    b.append(u"""
<section class="phero">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        <h1 data-rv="lines">{h}</h1>
        <p class="lede">I am Betty. I teach women to understand their food, so
        the next choice is obvious and the progress keeps going after I am out of
        the picture.</p>
        <div class="actions">{b1}</div>
      </div>
      <div>{im}</div>
    </div>
  </div>
</section>
""".format(h=lines('Expert enough', 'to trust. Human', 'enough to tell', 'the truth.'),
           b1=btn(BOOK, 'Book a free call', 'clay'),
           im=hero_img('betty-portrait.jpg',
                       'Betty smiling in a Strength tee, beside a framed '
                       'photograph of herself competing', 'tall dn', '4/4.5')))

    # Her story. The red dress photograph bleeds off the left edge, cropped
    # closer than a grid would allow, because the sisal baskets on that wall are
    # the single most Betty thing in the whole photo library.
    b.append(u"""
<section class="s">
  <div class="wrap">
    <div class="split">
      <div class="split-copy">
        <h2 data-rv>{h}</h2>
        <p>I found health and fitness young. After finishing high school
        in Kenya I began teaching yoga classes under the mentorship of Mrs Kanja,
        who was the first person to sit me down and teach me about eating well.</p>
        <p>After I moved to the States I trained under several coaches
        as I prepared for bodybuilding competitions. That is where precision
        nutrition stopped being a theory for me. I learned what food actually
        does: how varieties and amounts can be adjusted to reach a specific goal
        in a specific body.</p>
        <p>I competed. I once placed first. What stayed with me was not
        the trophy. It was realizing how much of what I had been taught about
        food before that point was noise.</p>
        {n}
      </div>
      <div class="split-media">{im}</div>
    </div>
  </div>
</section>

<section class="s bg-oat airy">
  <div class="wrap narrow">
    <h2 data-rv>{h2}</h2>
    <p>As I got older I started noticing it. I could work hard, eat what I
    thought was healthy, and still struggle with stubborn belly fat and clothes
    that did not fit the way I wanted them to. It was frustrating, because I felt
    like I was doing everything right.</p>
    <p>The biggest problem was not a lack of effort. It was confusion.</p>
    <p>Should I avoid carbs? Should I fast? Should I eat more protein? How
    much is too much? Is something labeled &ldquo;healthy&rdquo; actually helping me reach
    my goal?</p>
    <p>So I went back to the fundamentals: nutrition, portions, consistency,
    and genuinely understanding what I was putting into my body. That changed
    everything for me, and it made one thing very clear. I did not want women to
    believe their only remaining option was another extreme diet or hours they do
    not have in a gym.</p>
    <p class="big-p"><strong>That is why I coach.</strong></p>
  </div>
</section>
""".format(h=lines('It started with yoga', 'in Kenya, at eighteen.'),
           im=figure('betty-red.jpg',
                     'Standing against a pale wall hung with woven sisal '
                     'baskets, in a red dress',
                     'The baskets came from home. So did most of the rest of it.',
                     'drop', '0.70/1'),
           n=note('What stayed with me was not the trophy.'),
           h2=lines('My body stopped', 'responding the way', 'it used to.')))

    # the promise
    b.append(u"""
<section class="s">
  <div class="wrap">
    <div class="split reverse">
      <div class="split-media">{im}</div>
      <div class="split-copy">
        <h2 data-rv>{h}</h2>
        <p>Most of this market says <em>follow the plan</em>. I would rather
        you <em>understand the choice</em>. A printed plan works right up until the
        day you eat something that is not on it.</p>
        <p>So I teach women to understand food portions. To read a label.
        To know what a serving actually looks like on their own plate, instead of
        jumping from one trend to the next and hoping.</p>
        <p>The goal is to leave you more capable than when you arrived.
        Not more dependent on me.</p>
        <div class="actions">{tl}</div>
      </div>
    </div>
  </div>
</section>
""".format(h=lines('Clarity that leads', 'to progress you keep.'),
           im=img('betty-kettlebell.jpg',
                  'Betty holding a kettlebell in a training studio', 'tall'),
           tl=tlink('services.html', 'See the 16-week method')))

    # Credibility was four numbered cards; personality was four more. Both are
    # now plain two-column text, which is what they always were underneath.
    b.append(u"""
<section class="s tight bg-oat">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
        <p class="lede">Where the knowledge came from, and what it lets me
        shortcut for you.</p>
      </div>
      <div class="ed-body">
        <dl class="deflist" data-rv>
          <dt>Foundation</dt>
          <dd>She began teaching yoga in Kenya at eighteen, guided by Mrs Kanja.</dd>
          <dt>Discipline</dt>
          <dd>Bodybuilding preparation sharpened her nutrition precision to the
          point where every gram was accounted for.</dd>
          <dt>Lived empathy</dt>
          <dd>She understands stubborn belly fat and a body that changes.</dd>
          <dt>Responsible proof</dt>
          <dd>Client stories shared accurately, and only with permission.</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="s tight">
  <div class="wrap narrow">
    <h2 class="mb-l" data-rv>{h2}</h2>
    <p class="run" data-rv><b>Warm.</b> She understands the mirror, the
    frustration and the fear. <b>Plain-spoken.</b> Science becomes language you
    can repeat to someone else. <b>Unshockable.</b> No judgment about failed
    diets, setbacks or starting over. <b>Steady.</b> Calm confidence, with no
    hype and no urgency theater.</p>
    <p class="run-after">Expert enough to be trusted. Human enough to be told
    the truth.</p>
  </div>
</section>
""".format(h=lines('Knowledge made', 'practical.'),
           h2=lines('The knowledgeable', 'friend.')))

    # The competition photographs. Three real credentials at three different
    # widths and three different vertical offsets, because three equal squares
    # in a row is the shape a layout takes when nobody chose it. The crops stay
    # square: these source frames are composites of two poses, and cropping them
    # to a portrait or landscape ratio cuts one of the figures in half.
    b.append(u"""
<section class="s bg-oat">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
        <p class="lede">I competed in bodybuilding and I once placed first. Not
        because the trophy matters to you, but because that is where I learned
        exactly what food does to a body, and how precisely it can be adjusted.</p>
      </div>
    </div>
    <div class="uneven">
      {i1}{i2}{i3}
    </div>
    <div class="pair">
      {i4}
      <p class="narrow-p">You will never be asked to train like this. That is not
      the point and it is not the program. The point is that I learned nutrition
      at the level where every gram counted, so I can tell you which parts
      genuinely matter in a normal week and which parts you can stop worrying
      about.</p>
    </div>
  </div>
</section>

<section class="s tight">
  <div class="wrap">
    <h2 class="mb-l" data-rv>{h2}</h2>
    <div class="reels">
      <figure class="reel"><video controls preload="none" playsinline poster="assets/img/betty-carbs-poster.jpg">
        <source src="assets/video/betty-carbs.mp4" type="video/mp4"></video>
        <figcaption>Making off-season carbs work</figcaption></figure>
      <figure class="reel"><video controls preload="none" playsinline poster="assets/img/betty-hiit-poster.jpg">
        <source src="assets/video/betty-hiit.mp4" type="video/mp4"></video>
        <figcaption>A legs and glutes finisher</figcaption></figure>
      <figure class="reel"><video controls preload="none" playsinline poster="assets/img/betty-triceps-poster.jpg">
        <source src="assets/video/betty-triceps.mp4" type="video/mp4"></video>
        <figcaption>Why arm size is not just biceps</figcaption></figure>
    </div>
  </div>
</section>

<section class="s bg-forest tight">
  <div class="wrap narrow">
    <p class="big light" data-rv>
      I work with women who have tried diets, supplements and weight-loss trends
      but still struggle with stubborn weight and belly fat. Over 16 weeks, I
      help them lose weight sustainably, fit into their clothes again, and feel
      confident in their bodies.
    </p>
    <p class="sig">Beatrice &ldquo;Betty&rdquo; Mwihaki Igeria</p>
  </div>
</section>
""".format(h=lines('I have stood', 'on that stage.'),
           i1=img('betty-stage.jpg', 'Betty competing on stage at a bodybuilding show', 'u1', '1/1'),
           i2=img('betty-backstage.jpg', 'Betty warming up backstage before a competition', 'u2', '1/1'),
           i3=img('betty-track.jpg', 'Betty at the start line of a running track', 'u3', '1/1'),
           i4=figure('betty-race.jpg',
                     'Running a trail race with other runners on the path behind',
                     'A trail race, bib 259.', '', '1.3/1'),
           h2=lines('I do not just teach this. I live it.')))

    b.append(GUIDE)
    b.append(cta(['Let us talk about', 'your week.'],
                 'A free 20-minute conversation. No pressure and no pitch you '
                 'have to sit through.'))

    return shell(
        'about.html',
        'About Betty | Nutrition Education for Real Life',
        'Betty began teaching yoga in Kenya at eighteen and went on to compete '
        'in bodybuilding. Today she coaches women to understand their food.',
        ''.join(b))


# ============================================================ services.html ==
def build_services():
    b = []
    b.append(u"""
<section class="phero type">
  <div class="wrap">
    <div class="type-hero">
      <h1 data-rv="lines">{h}</h1>
      <div>
        <p class="lede">A practical 16-week weight-loss and nutrition coaching
        journey. Five phases, one clear lane, and a set of skills you keep.</p>
        <div class="actions">{b1}{tl}</div>
      </div>
    </div>
  </div>
</section>

<section class="s" id="phases">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h2}</h2>
        <p class="lede">Each phase does one job. Nothing moves until the one
        before it is holding.</p>
        {n}
      </div>
      <div class="ed-body" data-rv>
{phases}
      </div>
    </div>
  </div>
</section>
""".format(h=lines('The Food', 'Clarity Method'),
           b1=btn(BOOK, 'Book a free call', 'clay'),
           tl=tlink('#phases', 'See the five phases'),
           h2=lines('Five phases,', 'sixteen weeks.'),
           n=note('By the end you should not need me. That is the design.'),
           phases=phase_list(full=True)))

    b.append(u"""
<section class="s tight bg-oat">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h}</h2>
      </div>
      <div class="ed-body">
        <dl class="deflist wide-dl" data-rv>
          <dt>We talk first</dt>
          <dd>A free 20-minute call. I want to hear what you have tried, what
          happened, and what you actually want your body to feel like.</dd>
          <dt>We build your structure</dt>
          <dd>Not a printed meal plan. A framework for your kitchen, your budget
          and your week, with the reasoning explained every time.</dd>
          <dt>We check in weekly</dt>
          <dd>Accountability, honest feedback and adjustments as your body
          responds. This is where most women stop guessing.</dd>
          <dt>You take it with you</dt>
          <dd>By week sixteen you should not need me. You can read a label, judge
          a portion and feed yourself for life.</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="s">
  <div class="wrap">
    <div class="ed">
      <div class="ed-head">
        <h2 data-rv>{h2}</h2>
        <p class="lede">Every one of them starts with the same free
        conversation.</p>
      </div>
    </div>
    <div class="tiers">
      <div class="tier">
        <span class="flag">Start here</span>
        <h3>Free consultation</h3>
        <p class="price">Free, 20 minutes</p>
        <ul>
          <li>What you have already tried</li>
          <li>What is actually getting in the way</li>
          <li>An honest answer on whether I can help</li>
          <li>No obligation to continue</li>
        </ul>
        {t1}
      </div>
      <div class="tier featured">
        <span class="flag">Flagship program</span>
        <h3>The Food Clarity Method</h3>
        <p class="price">Investment shared on your call</p>
        <ul>
          <li>One-to-one coaching for sixteen weeks</li>
          <li>A nutrition structure built for your life</li>
          <li>Portion and label training, so you learn the why</li>
          <li>Weekly check-ins and accountability</li>
          <li>Adjustments as your body responds</li>
          <li>Habits designed to outlast the program</li>
        </ul>
        {t2}
      </div>
      <div class="tier">
        <span class="flag">Short format</span>
        <h3>The Nutrition Reset</h3>
        <p class="price">Investment shared on your call</p>
        <ul>
          <li>A focused four-week starting block</li>
          <li>Portions, protein and label basics</li>
          <li>A grocery and plate framework</li>
          <li>Ideal if sixteen weeks feels like a lot right now</li>
        </ul>
        {t3}
      </div>
    </div>
  </div>
</section>

<section class="s bg-oat">
  <div class="wrap">
    <div class="split">
      <div class="split-copy">
        <h2 data-rv>{h3}</h2>
        <ul class="checks">
          <li>You have tried the diets, the teas, the supplements, the waist trainers, and none of it stuck.</li>
          <li>Your clothes stopped fitting the way they used to and you cannot work out what changed.</li>
          <li>You want to understand nutrition, not be handed a plan you cannot maintain.</li>
          <li>You are tired of advice that assumes you have unlimited time and a perfect week.</li>
          <li>You are willing to be consistent for sixteen weeks.</li>
        </ul>
      </div>
      <div class="split-media">{im}</div>
    </div>
  </div>
</section>

<section class="s" id="faq">
  <div class="wrap narrow">
    <h2 class="mb-l" data-rv>{h4}</h2>
    <div class="faq">
{faq}
    </div>
  </div>
</section>
""".format(h=lines('How the sixteen', 'weeks actually run.'),
           h2=lines('Three ways to', 'work together.'),
           t1=btn(BOOK, 'Book the call', 'ghost'),
           t2=btn(BOOK, 'Apply on a free call', 'clay'),
           t3=btn(BOOK, 'Ask about it', 'ghost'),
           h3=lines('This is for you if.'),
           im=img('betty-cable.jpg', 'Betty training at a cable machine', 'tall'),
           h4=lines('Questions I get every week.'),
           faq='\n'.join(faq_item(i, q, a) for i, (q, a) in enumerate(FAQ))))

    b.append(GUIDE)
    b.append(cta(['Sixteen weeks from', 'now, you could be', 'done guessing.'],
                 'Book your free consultation and we will find out together '
                 'whether this is the right fit.'))

    return shell(
        'services.html',
        'The Food Clarity Method | 16-Week Nutrition Coaching with Betty',
        'A practical 16-week weight-loss and nutrition coaching journey in five '
        'phases: clarify, understand, apply, stay consistent, own it.',
        ''.join(b))


FAQ = [
    ('Do I have to give up carbs?',
     'No. You will learn what carbohydrates do, roughly how much you personally '
     'need, and how to fit them into your week. Cutting out whole food groups is '
     'exactly the kind of advice that leaves women confused and stuck.'),
    ('Will you put me on a meal plan?',
     'Not in the way you are imagining. A printed plan works until the day you '
     'eat something that is not on it. I teach you the reasoning, which is '
     'portions, protein and labels, so you can make a good decision in a '
     'restaurant, at a family gathering, or on a bad week.'),
    ('What if I am already taking a weight-loss medication?',
     'Bring it to the call. That is a conversation to have with me and with your '
     'doctor. My coaching is education and accountability around food, and I will '
     'always tell you when something belongs with your physician rather than '
     'with me.'),
    ('Do I need a gym?',
     'No. This is nutrition coaching. Movement helps and we will talk about it, '
     'but you will not be asked to spend hours you do not have in a gym.'),
    ('How much does it cost?',
     'I share the investment on the consultation call, once I know which program '
     'actually fits you. The call itself is free and there is no obligation to '
     'continue.'),
    ('What happens after sixteen weeks?',
     'You keep going, on your own. That is the whole design. My goal is never to '
     'make you dependent on me. It is to leave you able to manage your own '
     'nutrition for life.'),
]


def faq_item(i, q, a):
    return (u'      <button class="q" type="button" aria-expanded="{ex}" '
            u'aria-controls="fa{i}" id="fq{i}">{q}<span class="ic" aria-hidden="true"></span></button>\n'
            u'      <div class="a" id="fa{i}" role="region" aria-labelledby="fq{i}"><div><p>{a}</p></div></div>'
            ).format(i=i, q=q, a=a, ex='true' if i == 0 else 'false')


# ================================================================ shop.html ==
# The guide's own cover, set in the brand's type rather than photographed. There
# is no photograph of it because it is not written yet, and a stock food diary
# beside an apple is exactly the kind of image this pass exists to remove. It is
# aria-hidden because every word in it is in the heading beside it.
COVER = u"""<div class="cover" aria-hidden="true">
          <p class="c-k">Free guide</p>
          <p class="c-t">The label-reading guide for real life</p>
          <ul class="c-l"><li>Serving size</li><li>Protein</li><li>Added sugar</li></ul>
          <p class="c-b">Betty<i></i></p>
        </div>"""


def build_shop():
    """A library, not a product grid. One resource exists, it is free, and the
    other two are being written. Three equal cards with three buttons underneath
    said the opposite. The guide runs as the feature, the other two as entries,
    and the shared opt-in band is dropped from this page because the guide is
    already the whole page."""
    b = []
    b.append(u"""
<section class="phero">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        <h1 data-rv="lines">{h}</h1>
        <p class="lede">Short, plain-English guides you can start using this
        week, one clear teaching idea at a time. There is one so far. It is
        free, and the next two are being written.</p>
      </div>
      <div class="cover-slot" data-rv>{cover}</div>
    </div>
  </div>
</section>

<section class="s" id="guide">
  <div class="wrap">
    <div class="split lean">
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv>{h2}</h2>
        <p class="lede">Serving size, protein, added sugar. Three numbers, in
        that order, and you can judge almost any packet in the aisle. This is the
        short, plain-English guide I wish every woman had before she started
        another diet.</p>
        {optin}
      </div>
      <div class="split-media">
        <div class="three" aria-hidden="true">
          <p>Serving size</p>
          <p>Protein</p>
          <p>Added sugar</p>
        </div>
        {n}
      </div>
    </div>
  </div>
</section>

<section class="s tight bg-oat">
  <div class="wrap">
    <p class="k-head">Coming next</p>
    <div class="library">
      <article class="entry">
        <div class="e-k"><span class="more">Being written</span></div>
        <div>
          <h3>The portion handbook</h3>
          <p>How to judge a portion without weighing every meal, using your own
          hands, your own plates and the food you already buy.</p>
        </div>
      </article>
      <article class="entry">
        <div class="e-k"><span class="more">Being written</span></div>
        <div>
          <h3>Four weeks of real meals</h3>
          <p>A month of straightforward, affordable meals built on the same
          principles I coach, with the reasoning behind every plate.</p>
        </div>
      </article>
    </div>
  </div>
</section>
""".format(h=lines('Understand your', 'food, one idea', 'at a time.'),
           cover=COVER,
           eyebrow=eyebrow('Free guide'),
           h2=lines('The label-reading', 'guide for real life'),
           optin=OPTIN,
           n=note('Three numbers, in that order.')))

    b.append(cta(['Not sure where', 'to start?'],
                 'Book a free 20-minute call and I will point you at the right '
                 'thing, even if that turns out not to be me.'))

    return shell(
        'shop.html',
        'Resources | Betty, Nutrition Education for Real Life',
        'Plain-English nutrition guides from Betty: label reading, portions and '
        'real meals you can repeat.',
        ''.join(b))


# ================================================================ blog.html ==
POSTS = [
    ('Food clarity', 'Why you are eating healthy and still not losing weight',
     'The four most common reasons the scale will not move, and not one of them '
     'is that you are not trying hard enough.'),
    ('Food clarity', 'What weight-loss medications do, and what they do not teach you',
     'Why so many women are reaching for them, what changes when you stop, and '
     'what the education route genuinely asks of you.'),
    ('Label literacy', 'How to read a nutrition label in thirty seconds',
     'Serving size, protein, added sugar. Three numbers, in this order, and you '
     'can judge almost any packet in the aisle.'),
    ('Over 40', 'Stubborn belly fat after 40: what actually changed',
     'Your body did not betray you. Here is what shifts as we get older, and '
     'what to do about it that is not another crash diet.'),
    ('Portions', 'What a portion really looks like on your plate',
     'You do not need a food scale on the counter for the rest of your life. '
     'You need a reliable way to eyeball it.'),
    ('Simple action', 'Confused about what to eat? Start with these four questions',
     'Before you change a single thing about how you eat, answer these. They '
     'will save you months of guessing.'),
]


def build_blog():
    """A contents page rather than a grid of post cards. The six thumbnails were
    licensed stock photographs of other women, which on an index of Betty's own
    writing was the loudest tell left on the site, and her library has no food or
    kitchen photography to replace them with. So the journal runs on type: one
    lead story at full weight, then the rest as entries."""
    lead = POSTS[0]
    rest = POSTS[1:]

    entries = []
    for cat, title, dek in rest:
        entries.append(u"""      <article class="entry">
        <div class="e-k">
          <p class="cat">{cat}</p>
          <span class="more">Coming soon</span>
        </div>
        <div>
          <h3>{title}</h3>
          <p>{dek}</p>
        </div>
      </article>""".format(cat=cat, title=title, dek=dek))

    b = [u"""
<section class="phero type">
  <div class="wrap">
    <div class="type-hero">
      <h1 data-rv="lines">{h}</h1>
      <div>
        <p class="lede">Straight answers on food, portions and progress. No
        trends, no hype, and no jargon without a translation.</p>
      </div>
    </div>
  </div>
</section>

<section class="s">
  <div class="wrap">
    <article class="lead-story" data-rv>
      <p class="cat">{lcat}</p>
      <h2>{ltitle}</h2>
      <p class="lede">{ldek}</p>
      <span class="more">Coming soon</span>
    </article>
    <p class="k-head">Also in the journal</p>
    <div class="library">
{entries}
    </div>
  </div>
</section>
""".format(h=lines('No nutrition', 'noise. Just what', 'to do next.'),
           lcat=lead[0], ltitle=lead[1], ldek=lead[2],
           entries='\n'.join(entries))]

    b.append(GUIDE)
    b.append(cta(['Would you rather', 'just talk it through?'],
                 'Book a free 20-minute conversation instead of reading another '
                 'article about it.'))

    return shell(
        'blog.html',
        'Journal | Betty, Nutrition Education for Real Life',
        'Straight answers on food, portions and sustainable progress, written '
        'for women who are done guessing.',
        ''.join(b))



# ============================================================= contact.html ==
CONTACT_FORM = u'''<form action="%s" method="POST">
          <div class="field">
            <label for="c-name">Your name</label>
            <input id="c-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="c-email">Email address</label>
            <input id="c-email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="c-goal">What are you hoping to change?</label>
            <select id="c-goal" name="goal">
              <option>Understand nutrition and portions</option>
              <option>Lose weight and keep it off</option>
              <option>Stop relying on quick fixes and diet products</option>
              <option>Fit back into my clothes</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="field">
            <label for="c-tried">What have you already tried?</label>
            <textarea id="c-tried" name="message" placeholder="Diets, supplements, apps, gyms. Tell me honestly, there is no wrong answer here."></textarea>
          </div>
          <input type="hidden" name="_subject" value="New consultation request - Betty">
          <button class="btn btn-clay" type="submit">Request my free call</button>
        </form>''' % (FORM_ENDPOINT or '')

CONTACT_INTRO = ('Fill this in and I will come back to you with a time. If you '
                 'would rather just email, that works too.')

if not FORM_ENDPOINT:
    CONTACT_FORM = u"""<div class="actions">%s</div>
        <p class="form-note">Tell me what you have already tried and what is
        getting in the way. There is no wrong answer, and no pitch waiting at
        the other end.</p>""" % mailto(
        'A free 20-minute consultation', 'Email me to book a call')
    CONTACT_INTRO = 'Send me a note and I will come back to you with a time.'


def build_contact():
    b = [u"""
<section class="phero">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        <h1 data-rv="lines">{h}</h1>
        <p class="lede">A free 20-minute conversation. No pressure and no
        pitch you have to sit through, just an honest answer on whether I can
        help.</p>
      </div>
      <div>{im}</div>
    </div>
  </div>
</section>

<section class="s" id="book">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <h2 data-rv>{h2}</h2>
        <p>{intro}</p>
        {form}
      </div>
      <aside class="info-block">
        <h3>Reach Betty directly</h3>
        <dl>
          <dt>Email</dt>
          <dd><a href="mailto:beatricemwihaki@yahoo.com">beatricemwihaki@yahoo.com</a></dd>
          <dt>Instagram</dt>
          <dd><a href="https://www.instagram.com/betty_mwihaki/" target="_blank" rel="noopener">@betty_mwihaki</a></dd>
          <dt>TikTok</dt>
          <dd><a href="https://www.tiktok.com/@betty_fit8" target="_blank" rel="noopener">@betty_fit8</a></dd>
          <dt>Facebook</dt>
          <dd>Beatrice M</dd>
          <dt>Response time</dt>
          <dd>Usually within one working day.</dd>
        </dl>
      </aside>
    </div>
  </div>
</section>
""".format(h=lines('Let us talk about', 'your week, not', 'another diet.'),
           im=hero_img('betty-street.jpg',
                       'Betty out walking on a bright street', 'sq'),
           h2=lines('Tell me where you', 'are right now.'),
           intro=CONTACT_INTRO, form=CONTACT_FORM)]

    b.append(GUIDE)

    return shell(
        'contact.html',
        'Start Here | Book a Free Call with Betty',
        'Book a free 20-minute nutrition consultation with Betty. No pressure '
        'and no pitch, just an honest answer on whether coaching can help.',
        ''.join(b))


# ------------------------------------------------------------------- write --
PAGES = {
    'index.html': build_index,
    'about.html': build_about,
    'services.html': build_services,
    'shop.html': build_shop,
    'blog.html': build_blog,
    'contact.html': build_contact,
}

# Things that must never reach a public page again.
FORBIDDEN = [
    (u'—', 'em dash'),
    (u'–', 'en dash'),
    ('Draft note', 'internal draft note'),
    ('placeholder-quote', 'placeholder testimonial'),
    ('testimonial goes here', 'placeholder testimonial'),
    ('REPLACE_ME', 'unconfigured form endpoint'),
    ('journal-0', 'retired stock photograph'),
    ('food-portions', 'retired stock photograph'),
    ('food-prep', 'retired stock photograph'),
    ('food-whole', 'retired stock photograph'),
    ('food-bowl', 'retired stock photograph'),
    ('guide-table', 'retired stock photograph'),
    ('reader-quiet', 'retired stock photograph'),
]

if __name__ == '__main__':
    for name, fn in sorted(PAGES.items()):
        html = fn()
        for bad, why in FORBIDDEN:
            assert bad not in html, '%s found in %s' % (why, name)
        eyebrows = html.count('class="eyebrow')
        assert eyebrows <= 2, '%d eyebrows on %s, budget is 2' % (eyebrows, name)
        notes = html.count('class="note"')
        assert notes <= 2, '%d margin notes on %s, budget is 2' % (notes, name)
        with io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        print('%-15s %6d bytes  %d eyebrow(s)  %d note(s)'
              % (name, len(html.encode('utf-8')), eyebrows, notes))
    if not FORM_ENDPOINT:
        print('')
        print('  ** FORM_ENDPOINT is not set, so both forms are showing a')
        print('     mailto button rather than a real form. Paste the')
        print('     Formspree endpoint at the top of this file and rebuild')
        print('     to put the opt-in and the consultation form back. **')
