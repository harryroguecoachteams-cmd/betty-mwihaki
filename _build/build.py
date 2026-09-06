# -*- coding: utf-8 -*-
"""
Generates the six pages of bettymwihaki.com from one shell, so the header,
footer, freebie band and CTA stay identical everywhere.

    python _build/build.py

Copy is taken from the Betty Brand Identity Deck (Rogue Coach Teams) and from
Betty's own Coaching Niche Discovery Form. Nothing about her background or her
client outcomes is invented. House style: US English, no em dashes.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..'))

NAV = [
    ('about.html', 'About'),
    ('services.html', 'The Method'),
    ('shop.html', 'Resources'),
    ('blog.html', 'Journal'),
]
BOOK = 'contact.html#book'


# --------------------------------------------------------------- fragments --
def lines(*ls):
    """Editorial headline split into masked lines. Keep each line short: the
    mask clips horizontally as well as vertically."""
    return '\n        '.join(
        '<span class="ln"><i>%s</i></span>' % l for l in ls)


def eyebrow(t, extra=''):
    return '<p class="eyebrow%s">%s</p>' % ((' ' + extra) if extra else '', t)


ARROW = ('<svg class="ar" viewBox="0 0 19 9" fill="none" aria-hidden="true">'
         '<path d="M0 4.5h16.5M13 1l3.9 3.5L13 8" stroke="currentColor" '
         'stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def btn(href, label, kind='clay', cls=''):
    return '<a class="btn btn-%s %s" href="%s">%s</a>' % (kind, cls, href, label)


def tlink(href, label):
    return '<a class="tlink" href="%s">%s%s</a>' % (href, label, ARROW)


def img(src, alt, cls='', ar='', pos='', delay=''):
    style = []
    if ar:
        style.append('--ar:%s' % ar)
    if delay:
        style.append('--d:%s' % delay)
    st = (' style="%s"' % ';'.join(style)) if style else ''
    ps = (' style="--pos:%s"' % pos) if pos else ''
    return ('<div class="imgwrap %s"%s><div class="par">'
            '<img src="assets/img/%s" alt="%s" loading="lazy" decoding="async"%s>'
            '</div></div>') % (cls, st, src, alt, ps)


def hero_img(src, alt, cls='', ar=''):
    """Above the fold: never lazy, and it is the LCP element."""
    style = (' style="--ar:%s"' % ar) if ar else ''
    return ('<div class="imgwrap %s"%s><div class="par">'
            '<img src="assets/img/%s" alt="%s" fetchpriority="high" decoding="async">'
            '</div></div>') % (cls, style, src, alt)


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

<div class="rail" aria-hidden="true"><div class="rail-line"><div class="rail-fill"></div><div class="rail-pt"></div></div></div>

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
GUIDE = u"""
<section class="freebie" id="guide" data-sec="Free guide">
  <div class="wrap">
    <div class="split">
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
        <p class="lede" data-rv style="--d:120ms">Serving size, protein, added sugar. Three numbers, in
        that order, and you can judge almost any packet in the aisle. This is the
        short, plain-English guide I wish every woman had before she started
        another diet.</p>
        <form class="optin" action="https://formspree.io/f/REPLACE_ME" method="POST" data-rv style="--d:200ms">
          <input type="text" name="name" placeholder="First name" aria-label="First name" required>
          <input type="email" name="email" placeholder="Your email address" aria-label="Email address" required>
          <input type="hidden" name="_subject" value="New download - The label-reading guide for real life">
          <button class="btn btn-clay" type="submit">Send it to me</button>
        </form>
        <p class="form-note" data-rv style="--d:260ms">No spam. Unsubscribe any time.</p>
      </div>
      <div class="split-media">{img}</div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true">
    <span class="shape s1 d1"></span><span class="shape s2 d3"></span>
  </div>
</section>
""".format(
    eyebrow=eyebrow('Free guide'),
    h=lines('The label-reading', 'guide for real life'),
    img=img('guide-table.jpg', 'A food diary open on a table beside an apple and a glass of water',
            'wide', '1.2/1'))


def cta(h_lines, sub, label='Book a free call'):
    return u"""
<section class="cta" data-sec="Start here">
  <div class="wrap">
    <div class="cta-grid">
      <div>
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
      </div>
      <div>
        <p class="lede" data-rv style="--d:120ms">{sub}</p>
        <div class="actions" data-rv style="--d:200ms">
          {btn}
          {tl}
        </div>
      </div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true">
    <span class="shape s1 d2"></span><span class="shape s2 d1"></span><span class="shape s3 d3"></span>
  </div>
</section>
""".format(eyebrow=eyebrow('Start here'), h=lines(*h_lines), sub=sub,
           btn=btn(BOOK, label, 'clay'), tl=tlink('services.html', 'See the 16-week method'))


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

ARC_PATH = 'M 92 214 C 300 214 336 92 566 128 C 796 164 838 62 1108 78'


def arc_block(dark=False):
    labels = '|'.join(p[0] for p in PHASES)
    stroke = 'rgba(255,255,255,.22)' if dark else 'var(--sage-line)'
    return u"""
    <div class="arc-wrap" data-phases="{labels}" aria-hidden="true">
      <svg viewBox="0 0 1200 300" fill="none" preserveAspectRatio="xMidYMid meet">
        <path class="track" d="{d}" stroke="{stroke}" stroke-width="1.5"/>
        <path class="draw" d="" stroke="var(--clay)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <div class="arc-nodes"></div>
    </div>
""".format(labels=labels, d=ARC_PATH, stroke=stroke)


def rails_block(full=False, cls='rails-mobile'):
    items = []
    for i, (name, short, long) in enumerate(PHASES):
        body = long if full else short
        items.append(
            '      <div class="phase">\n'
            '        <p class="p">Phase 0%d</p>\n'
            '        <h3>%s</h3>\n'
            '        <p class="d">%s</p>\n'
            '      </div>' % (i + 1, name, body))
    return ('    <div class="rails %s">\n'
            '      <div class="prog"></div>\n%s\n    </div>\n'
            % (cls, '\n'.join(items)))


PRINCIPLES = [
    ('Understand your food', 'Learn the reason, never just the rule.'),
    ('Keep it practical', 'It has to work in an ordinary week.'),
    ('Progress over perfection', 'One meal never becomes a verdict.'),
    ('You do not do it alone', 'Support and accountability stay human.'),
    ('Learn it for life', 'Build capability, not dependency.'),
]

SIGNATURE = [
    'Stop guessing what to eat. Start understanding your food.',
    'You do not need more nutrition noise.',
    'Progress comes from what you repeat.',
    'Build habits you can actually maintain.',
]


def marquee(dark=False):
    its = ''.join('<span class="it">%s</span>' % s for s in SIGNATURE)
    return ('<div class="marq%s" aria-label="Betty in four lines">'
            '<div class="marq-track">%s</div></div>'
            % (' dark' if dark else '', its))


# =============================================================== index.html ==
def build_index():
    b = []

    b.append(u"""
<section class="hero" data-sec="Top">
  <div class="hero-grid">
    <div class="hero-copy">
      {eyebrow}
      <h1 data-rv="lines">{h}</h1>
      <p class="lede" data-rv style="--d:620ms">Practical nutrition coaching for women who are
      ready for sustainable progress they can maintain.</p>
      <div class="actions" data-rv style="--d:740ms">
        {b1}
        {tl}
      </div>
    </div>
    <div class="hero-art">
      {im}
      <div class="badge" data-rv="scale" style="--d:900ms">
        <span class="k"><span data-count="16">16</span> weeks</span>
        <span class="v">Clarity &middot; Action &middot; Accountability</span>
      </div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true">
    <span class="shape s1 d1"></span><span class="shape s2 d2"></span><span class="shape s3 d3"></span>
  </div>
</section>

<section class="hero-strip">
  <div class="wrap wide" data-stagger="110">
    <div class="it"><h3>Food clarity</h3><p>Understand your food</p></div>
    <div class="it"><h3>Simple action</h3><p>Build real-life routines</p></div>
    <div class="it"><h3>Confidence</h3><p>Stop starting over</p></div>
  </div>
</section>
""".format(eyebrow=eyebrow('The Food Clarity Method'),
           h=lines('Stop guessing', 'what to eat.', 'Start understanding',
                   'your food.'),
           b1=btn('services.html', 'Explore the 16-week method', 'clay'),
           tl=tlink('services.html#phases', 'See how it works'),
           im=hero_img('betty-hero.jpg',
                       'Betty smiling on the water in a red jacket', 'tall')))

    # her words
    b.append(u"""
<section class="s statement" data-sec="Her words">
  <div class="wrap">
    <div class="statement-grid">
      <div>
        {eyebrow}
        <p class="q" data-rv="lines">{q}</p>
      </div>
      <div class="after">
        <p class="lede" data-rv style="--d:200ms">If you have said a version of that out loud, you are
        in the right place. No shame and no panic. Just practical education and
        steady support until food makes sense again.</p>
        <div class="actions" data-rv style="--d:280ms">{tl}</div>
      </div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true"><span class="shape s1 d3"></span></div>
</section>
""".format(eyebrow=eyebrow('Her words'),
           q=lines('&ldquo;I am eating', 'healthy, but I am',
                   'still not losing', 'weight. I do not',
                   '<span class="hl">know what to try next.</span>&rdquo;'),
           tl=tlink('about.html', 'Meet Betty')))

    # who this is for
    b.append(u"""
<section class="s bg-oat" data-sec="Who it is for">
  <div class="wrap">
    <div class="split lean">
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
        <p class="lede" data-rv style="--d:140ms">You have tried diets, supplements and weight-loss
        trends. You are tired of being handed another rule without any real
        understanding of why it is supposed to work.</p>
      </div>
      <div class="split-media">{im}</div>
    </div>
    <div class="cards mt-l" data-stagger="110">
      <div class="card"><span class="num">01</span><h3>Where you are</h3>
        <p>You still struggle with stubborn weight and belly fat, even in the
        weeks when you feel like you are doing everything right.</p></div>
      <div class="card"><span class="num">02</span><h3>What is frustrating</h3>
        <p>You are confused about what actually works, because every source
        tells you something different and all of them sound certain.</p></div>
      <div class="card"><span class="num">03</span><h3>What you need</h3>
        <p>Clear guidance, a structure that survives a real week, and someone
        holding you to it who is not going to judge you.</p></div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('Who this is for'),
           h=lines('You are not new', 'to trying.'),
           im=img('reader-quiet.jpg',
                  'A woman sitting quietly at home, thinking', 'tall', '',
                  '50% 30%')))

    # position
    b.append(u"""
<section class="s" data-sec="The gap">
  <div class="wrap">
    <div class="head">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">She cuts through the conflicting advice first, then
      turns what is left into a routine you can actually keep.</p>
    </div>
    <div class="tript">
      <div class="pan noise"><span class="k">The noise</span><p>Diets, supplements and weight-loss trends.</p></div>
      <div class="conn" style="--d:250ms"></div>
      <div class="pan gap"><span class="k">The gap</span><p>Understanding what, how much and why to eat.</p></div>
      <div class="conn" style="--d:450ms"></div>
      <div class="pan betty"><span class="k">Betty</span><p>The practical coach who makes the next step clear.</p></div>
    </div>
    <p class="serif-quote center mt-l" data-rv>Clarity is the competitive advantage.</p>
  </div>
</section>
""".format(eyebrow=eyebrow('The difference'),
           h=lines('Betty makes nutrition', 'understandable.')))

    # transformation + clarity field
    b.append(u"""
<section class="s bg-oat" data-sec="The change">
  <div class="wrap">
    <div class="split lean">
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
        <p class="lede" data-rv style="--d:140ms">The outcome is not perfect eating. It is knowing what
        to do next, and why.</p>
        <div class="stages mt-l">
          <div class="stage" data-stage><span class="n">01</span><div>
            <h3>Confused</h3><p>Rules, fear and conflicting advice.</p></div></div>
          <div class="stage" data-stage><span class="n">02</span><div>
            <h3>Capable</h3><p>Food choices make sense in real life.</p></div></div>
          <div class="stage" data-stage><span class="n">03</span><div>
            <h3>Confident</h3><p>You can adjust without starting over.</p></div></div>
        </div>
      </div>
      <div>
        <div class="clarity" aria-hidden="true">
          <span class="lbl a">Noise</span>
          <span class="lbl b">Clarity</span>
        </div>
      </div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('The transformation'),
           h=lines('Confusion becomes', 'confidence.')))

    # the method
    b.append(u"""
<section class="s bg-forest method" data-sec="The method">
  <div class="wrap">
    <div class="head center">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">A practical 16-week weight-loss and nutrition coaching
      journey, in five phases.</p>
    </div>
{arc}
{rails}
    <div class="actions center" style="justify-content:center" data-rv>
      {b1}
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('The signature offer', 'center'),
           h=lines('The Food', 'Clarity Method'),
           arc=arc_block(dark=True), rails=rails_block(),
           b1=btn('services.html', 'See the full method', 'ghost', 'auto')))

    # meet betty
    b.append(u"""
<section class="s" data-sec="Betty">
  <div class="wrap">
    <div class="split reverse">
      <div class="split-media">{im}</div>
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
        <p data-rv style="--d:140ms">I began teaching yoga in Kenya at eighteen, guided by
        Mrs Kanja, who was the first person to sit me down and teach me about
        eating well. Preparing for bodybuilding competitions in the States is
        where precision nutrition stopped being a theory for me.</p>
        <p data-rv style="--d:200ms">Then my own body stopped responding the way it used to, and
        I understood the frustration from the inside. There is so much health
        information out there that it has become genuinely impossible for a
        normal person to tell what is real and what is marketing.</p>
        <p data-rv style="--d:260ms">Taking the complicated and making it simple is my natural
        gift. It is also the whole job.</p>
        <div class="actions" data-rv style="--d:320ms">{tl}</div>
      </div>
    </div>
  </div>
</section>

<div class="marq-wrap">{marq}</div>
""".format(eyebrow=eyebrow('Your coach'),
           h=lines('I take the', 'complicated and', 'make it simple.'),
           im=img('betty-portrait.jpg',
                  'Betty smiling in a Strength tee, beside a framed photograph '
                  'of herself competing', 'tall'),
           tl=tlink('about.html', 'Read her story'),
           marq=marquee()))

    # results
    b.append(u"""
<section class="s bg-oat" data-sec="Results">
  <div class="wrap">
    <div class="head">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">Two stories in Betty's own words. Coaching supports
      habits, understanding and accountability. It is not a promise of a
      particular result.</p>
    </div>
    <div class="results">
      <div class="result">
        <span class="stat"><span data-count="30">30</span> lbs</span>
        <p>She had already tried plan after plan when she came to me. We did not
        add a single supplement. We changed how she ate and she learned the
        reason behind every choice. Thirty pounds down, and she can feed herself
        now without me.</p>
        <p class="who">Nutrition coaching client</p>
      </div>
      <div class="result dark">
        <span class="pull">The hardest client I have ever coached.</span>
        <p>My own cousin. She came to me worried about where her health was
        heading and we worked through her nutrition together, month after month.
        Family is the hardest audience there is, and the most worth it. She
        understands her food now, and she is not guessing anymore.</p>
        <p class="who">Nutrition coaching client</p>
      </div>
    </div>
    <div class="todo">
      <strong>Draft note for Betty:</strong> both stories are yours, reworded to
      stay inside the brand deck's claims rules (page 28): no diagnosis, cure or
      reversal language, and outcomes framed around coaching and habits. Before
      launch we need your written confirmation of the wording plus each client's
      permission to publish it.
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('Real outcomes'),
           h=lines('What has happened', 'for the women I coach.')))

    # testimonials
    b.append(u"""
<section class="s" data-sec="In her words">
  <div class="wrap">
    <div class="head center">
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">From women who have finished the sixteen weeks.</p>
    </div>
    <div class="quotes" data-stagger="110">
      <div class="quote placeholder-quote"><span class="mark">&ldquo;</span>
        <p>Client testimonial goes here. Ask for two or three sentences on what
        she had already tried, what changed, and how she feels in her clothes
        now.</p>
        <p class="who">Client name</p><p class="role">Program graduate</p></div>
      <div class="quote placeholder-quote"><span class="mark">&ldquo;</span>
        <p>Client testimonial goes here. The strongest ones name the specific
        fear she had before starting, and what actually happened instead.</p>
        <p class="who">Client name</p><p class="role">Program graduate</p></div>
      <div class="quote placeholder-quote"><span class="mark">&ldquo;</span>
        <p>Client testimonial goes here. A line about learning to read labels or
        judge portions lands especially well with this audience.</p>
        <p class="who">Client name</p><p class="role">Program graduate</p></div>
    </div>
    <div class="todo">
      <strong>Draft note for Betty:</strong> these three cards are placeholders
      on purpose. Send Rogue Coach Teams real testimonials (first name plus one
      or two sentences, photo optional) and they go straight in.
    </div>
  </div>
</section>
""".format(h=lines('In her words.')))

    b.append(GUIDE)

    # video
    b.append(u"""
<section class="s" data-sec="In the gym">
  <div class="wrap">
    <div class="head center">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">Nutrition is the work. Training is where I learned what
      food actually does.</p>
    </div>
    <div class="reels" data-stagger="130">
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
""".format(eyebrow=eyebrow('In the gym', 'center'),
           h=lines('I do not just teach this.', 'I live it.')))

    # principles
    b.append(u"""
<section class="s bg-oat" data-sec="Principles">
  <div class="wrap">
    <div class="head">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
    </div>
    <div class="principles">
{rows}
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('What I believe'),
           h=lines('Five beliefs behind', 'every conversation.'),
           rows='\n'.join(
               '      <div class="principle"><span class="n">0%d</span>'
               '<h3>%s</h3><p>%s</p></div>' % (i + 1, t, d)
               for i, (t, d) in enumerate(PRINCIPLES))))

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
<section class="phero" data-sec="About">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        {eyebrow}
        <h1 data-rv="lines">{h}</h1>
        <p class="lede" data-rv style="--d:560ms">I am Betty. I teach women to understand their food, so
        the next choice is obvious and the progress keeps going after I am out of
        the picture.</p>
        <div class="actions" data-rv style="--d:660ms">{b1}</div>
      </div>
      <div>{im}</div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true"><span class="shape s1 d1"></span><span class="shape s2 d2"></span></div>
</section>
""".format(eyebrow=eyebrow('About Betty'),
           h=lines('Expert enough', 'to trust. Human', 'enough to tell', 'the truth.'),
           b1=btn(BOOK, 'Book a free call', 'clay'),
           im=hero_img('betty-portrait.jpg',
                       'Betty smiling in a Strength tee, beside a framed '
                       'photograph of herself competing', 'tall dn', '4/4.5')))

    b.append(u"""
<section class="s" data-sec="Her story">
  <div class="wrap">
    <div class="split">
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
        <p data-rv style="--d:140ms">I found health and fitness young. After finishing high school
        in Kenya I began teaching yoga classes under the mentorship of Mrs Kanja,
        who was the first person to sit me down and teach me about eating well.</p>
        <p data-rv style="--d:200ms">After I moved to the States I trained under several coaches
        as I prepared for bodybuilding competitions. That is where precision
        nutrition stopped being a theory for me. I learned what food actually
        does: how varieties and amounts can be adjusted to reach a specific goal
        in a specific body.</p>
        <p data-rv style="--d:260ms">I competed. I once placed first. What stayed with me was not
        the trophy. It was realizing how much of what I had been taught about
        food before that point was noise.</p>
      </div>
      <div class="split-media">{im}</div>
    </div>
  </div>
</section>

<section class="s bg-oat">
  <div class="wrap narrow">
    {eyebrow2}
    <h2 data-rv="lines">{h2}</h2>
    <p data-rv style="--d:140ms">As I got older I started noticing it. I could work hard, eat what I
    thought was healthy, and still struggle with stubborn belly fat and clothes
    that did not fit the way I wanted them to. It was frustrating, because I felt
    like I was doing everything right.</p>
    <p data-rv style="--d:180ms">The biggest problem was not a lack of effort. It was confusion.</p>
    <p data-rv style="--d:220ms">Should I avoid carbs? Should I fast? Should I eat more protein? How
    much is too much? Is something labeled &ldquo;healthy&rdquo; actually helping me reach
    my goal?</p>
    <p data-rv style="--d:260ms">So I went back to the fundamentals: nutrition, portions, consistency,
    and genuinely understanding what I was putting into my body. That changed
    everything for me, and it made one thing very clear. I did not want women to
    believe their only remaining option was another extreme diet or hours they do
    not have in a gym.</p>
    <p data-rv style="--d:300ms"><strong>That is why I coach.</strong></p>
  </div>
</section>
""".format(eyebrow=eyebrow('My story'),
           h=lines('It started with yoga', 'in Kenya, at eighteen.'),
           im=img('betty-beach.jpg', 'Betty walking on a beach', 'wide', '1.34/1'),
           eyebrow2=eyebrow('Then it happened to me'),
           h2=lines('My body stopped', 'responding the way', 'it used to.')))

    # the promise
    b.append(u"""
<section class="s" data-sec="The promise">
  <div class="wrap">
    <div class="split reverse">
      <div class="split-media">{im}</div>
      <div class="split-copy">
        {eyebrow}
        <h2 data-rv="lines">{h}</h2>
        <p data-rv style="--d:140ms">Most of this market says <em>follow the plan</em>. I would rather
        you <em>understand the choice</em>. A printed plan works right up until the
        day you eat something that is not on it.</p>
        <p data-rv style="--d:200ms">So I teach women to understand food portions. To read a label.
        To know what a serving actually looks like on their own plate, instead of
        jumping from one trend to the next and hoping.</p>
        <p data-rv style="--d:260ms">The goal is to leave you more capable than when you arrived.
        Not more dependent on me.</p>
        <div class="actions" data-rv style="--d:320ms">{tl}</div>
      </div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('My promise'),
           h=lines('Clarity that leads', 'to progress you keep.'),
           im=img('betty-kettlebell.jpg',
                  'Betty holding a kettlebell in a training studio', 'tall'),
           tl=tlink('services.html', 'See the 16-week method')))

    # credibility
    b.append(u"""
<section class="s bg-oat" data-sec="Credibility">
  <div class="wrap">
    <div class="head">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">Where the knowledge came from, and what it lets me
      shortcut for you.</p>
    </div>
    <div class="cards four" data-stagger="100">
      <div class="card"><span class="num">01</span><h3>Foundation</h3>
        <p>She began teaching yoga in Kenya at eighteen, guided by Mrs Kanja.</p></div>
      <div class="card"><span class="num">02</span><h3>Discipline</h3>
        <p>Bodybuilding preparation sharpened her nutrition precision.</p></div>
      <div class="card"><span class="num">03</span><h3>Lived empathy</h3>
        <p>She understands stubborn belly fat and a body that changes.</p></div>
      <div class="card"><span class="num">04</span><h3>Responsible proof</h3>
        <p>Client stories shared accurately, and only with permission.</p></div>
    </div>
  </div>
</section>

<section class="s" data-sec="Personality">
  <div class="wrap">
    <div class="head">
      {eyebrow2}
      <h2 data-rv="lines">{h2}</h2>
      <p class="lede" data-rv style="--d:140ms">Expert enough to be trusted. Human enough to be told
      the truth.</p>
    </div>
    <div class="persona" data-stagger="100">
      <div class="p"><h3>Warm</h3><p>She understands the mirror, the frustration and the fear.</p></div>
      <div class="p"><h3>Plain-spoken</h3><p>Science becomes language you can repeat to someone else.</p></div>
      <div class="p"><h3>Unshockable</h3><p>No judgment about failed diets, setbacks or starting over.</p></div>
      <div class="p"><h3>Steady</h3><p>Calm confidence, with no hype and no urgency theater.</p></div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('Credibility'),
           h=lines('Knowledge made', 'practical.'),
           eyebrow2=eyebrow('Personality'),
           h2=lines('The knowledgeable', 'friend.')))

    # the stage
    b.append(u"""
<section class="s bg-oat" data-sec="The stage">
  <div class="wrap">
    <div class="head center">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
      <p class="lede" data-rv style="--d:140ms">I competed in bodybuilding and I once placed first. Not
      because the trophy matters to you, but because that is where I learned
      exactly what food does to a body, and how precisely it can be adjusted.</p>
    </div>
    <div class="strip3" data-stagger="140">
      {i1}{i2}{i3}
    </div>
    <p class="center mt-l" data-rv style="max-width:760px;margin-left:auto;margin-right:auto">
      You will never be asked to train like this. That is not the point and it is
      not the program. The point is that I learned nutrition at the level where
      every gram counted, so I can tell you which parts genuinely matter in a
      normal week and which parts you can stop worrying about.
    </p>
  </div>
</section>

<section class="s" data-sec="In the gym">
  <div class="wrap">
    <div class="head center">
      {eyebrow2}
      <h2 data-rv="lines">{h2}</h2>
    </div>
    <div class="reels" data-stagger="130">
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

<section class="s bg-forest">
  <div class="wrap narrow center">
    {eyebrow3}
    <p class="serif-quote" data-rv style="color:#fff">
      I work with women who have tried diets, supplements and weight-loss trends
      but still struggle with stubborn weight and belly fat. Over 16 weeks, I
      help them lose weight sustainably, fit into their clothes again, and feel
      confident in their bodies.
    </p>
    <p class="mt-l" data-rv style="--d:160ms;font-size:.76rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--sage)">
      Beatrice &ldquo;Betty&rdquo; Mwihaki Igeria
    </p>
  </div>
</section>
""".format(eyebrow=eyebrow('Where the knowledge came from', 'center'),
           h=lines('I have stood', 'on that stage.'),
           i1=img('betty-stage.jpg', 'Betty competing on stage at a bodybuilding show', 'sq'),
           i2=img('betty-backstage.jpg', 'Betty warming up backstage before a competition', 'sq'),
           i3=img('betty-track.jpg', 'Betty at the start line of a running track', 'sq'),
           eyebrow2=eyebrow('In the gym', 'center'),
           h2=lines('I do not just teach this.', 'I live it.'),
           eyebrow3=eyebrow('Positioning', 'center')))

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
<section class="phero" data-sec="The method">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        {eyebrow}
        <h1 data-rv="lines">{h}</h1>
        <p class="lede" data-rv style="--d:560ms">A practical 16-week weight-loss and nutrition coaching
        journey. Five phases, one clear lane, and a set of skills you keep.</p>
        <div class="actions" data-rv style="--d:660ms">{b1}{tl}</div>
      </div>
      <div>{im}</div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true"><span class="shape s1 d1"></span><span class="shape s2 d2"></span></div>
</section>

<section class="s method" id="phases" data-sec="Five phases">
  <div class="wrap">
    <div class="head">
      {eyebrow2}
      <h2 data-rv="lines">{h2}</h2>
      <p class="lede" data-rv style="--d:140ms">Each phase does one job. Nothing moves until the one
      before it is holding.</p>
    </div>
{arc}
{rails}
  </div>
</section>
""".format(eyebrow=eyebrow('The signature offer'),
           h=lines('The Food', 'Clarity Method'),
           b1=btn(BOOK, 'Book a free call', 'clay'),
           tl=tlink('#phases', 'See the five phases'),
           im=hero_img('food-portions.jpg',
                       'Portioned, home-cooked meals prepared for the week',
                       'wide', '1.2/1'),
           eyebrow2=eyebrow('How it runs'),
           h2=lines('Five phases,', 'sixteen weeks.'),
           arc=arc_block(), rails=rails_block(full=True, cls='rails-full')))

    b.append(u"""
<section class="s bg-oat" data-sec="Week to week">
  <div class="wrap">
    <div class="head center">
      {eyebrow}
      <h2 data-rv="lines">{h}</h2>
    </div>
    <div class="steps" data-stagger="120">
      <div class="step"><span class="n">01</span><h4>We talk first</h4>
        <p>A free 20-minute call. I want to hear what you have tried, what
        happened, and what you actually want your body to feel like.</p></div>
      <div class="step"><span class="n">02</span><h4>We build your structure</h4>
        <p>Not a printed meal plan. A framework for your kitchen, your budget
        and your week, with the reasoning explained every time.</p></div>
      <div class="step"><span class="n">03</span><h4>We check in weekly</h4>
        <p>Accountability, honest feedback and adjustments as your body
        responds. This is where most women stop guessing.</p></div>
      <div class="step"><span class="n">04</span><h4>You take it with you</h4>
        <p>By week sixteen you should not need me. You can read a label, judge
        a portion and feed yourself for life.</p></div>
    </div>
  </div>
</section>

<section class="s" data-sec="Ways to work">
  <div class="wrap">
    <div class="head center">
      {eyebrow2}
      <h2 data-rv="lines">{h2}</h2>
      <p class="lede" data-rv style="--d:140ms">Every one of them starts with the same free
      conversation.</p>
    </div>
    <div class="tiers" data-stagger="110">
      <div class="tier">
        <span class="flag">Start here</span>
        <h3>Free consultation</h3>
        <p class="price">Free &middot; 20 minutes</p>
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
    <div class="todo">
      <strong>Draft note for Betty:</strong> pricing is deliberately left as
      &ldquo;shared on your call&rdquo; until you confirm your numbers. Send the figures
      and we will put them live. The Nutrition Reset is a suggested second offer,
      so tell us to keep, change or remove it.
    </div>
  </div>
</section>

<section class="s bg-oat" data-sec="Is it you">
  <div class="wrap">
    <div class="split">
      <div class="split-copy">
        {eyebrow3}
        <h2 data-rv="lines">{h3}</h2>
        <ul class="checks" data-rv="fade" data-stagger="90">
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

<section class="s" id="faq" data-sec="Questions">
  <div class="wrap narrow">
    <div class="head center">
      {eyebrow4}
      <h2 data-rv="lines">{h4}</h2>
    </div>
    <div class="faq">
{faq}
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('The process', 'center'),
           h=lines('How the sixteen', 'weeks actually run.'),
           eyebrow2=eyebrow('Choose your starting point', 'center'),
           h2=lines('Three ways to', 'work together.'),
           t1=btn(BOOK, 'Book the call', 'ghost'),
           t2=btn(BOOK, 'Apply on a free call', 'clay'),
           t3=btn(BOOK, 'Ask about it', 'ghost'),
           eyebrow3=eyebrow('Who this is for'),
           h3=lines('This is for you if.'),
           im=img('betty-cable.jpg', 'Betty training at a cable machine', 'tall'),
           eyebrow4=eyebrow('Before you book', 'center'),
           h4=lines('Questions I get', 'every week.'),
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
def build_shop():
    b = []
    b.append(u"""
<section class="phero" data-sec="Resources">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        {eyebrow}
        <h1 data-rv="lines">{h}</h1>
        <p class="lede" data-rv style="--d:560ms">Short, plain-English guides you can start using this
        week. One clear teaching idea at a time.</p>
      </div>
      <div>{im}</div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true"><span class="shape s1 d1"></span><span class="shape s2 d2"></span></div>
</section>

<section class="s" data-sec="Guides">
  <div class="wrap">
    <div class="products" data-stagger="120">
      <div class="product">
        {i1}
        <div class="product-body">
          <h3>The label-reading guide for real life</h3>
          <p class="price">Free</p>
          <p>Serving size, protein, added sugar. Three numbers in that order and
          you can judge almost any packet in the aisle, without standing in the
          store doing math.</p>
          {b1}
        </div>
      </div>
      <div class="product">
        {i2}
        <div class="product-body">
          <h3>The portion handbook</h3>
          <p class="price">Coming soon</p>
          <p>How to judge a portion without weighing every meal, using your own
          hands, your own plates and the food you already buy.</p>
          {b2}
        </div>
      </div>
      <div class="product">
        {i3}
        <div class="product-body">
          <h3>Four weeks of real meals</h3>
          <p class="price">Coming soon</p>
          <p>A month of straightforward, affordable meals built on the same
          principles I coach, with the reasoning behind every plate.</p>
          {b3}
        </div>
      </div>
    </div>
    <div class="todo">
      <strong>Draft note for Betty:</strong> only the free guide is confirmed.
      The two &ldquo;coming soon&rdquo; products are placeholders so the page is not
      empty. Tell us what you actually want to sell and at what price and we will
      build a real checkout.
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('Resources'),
           h=lines('Understand your', 'food, one idea', 'at a time.'),
           im=hero_img('guide-table.jpg',
                       'A food diary open on a table beside an apple',
                       'wide', '1.2/1'),
           i1=img('guide-table.jpg', 'A food diary open on a table', '', '1.2/1'),
           i2=img('food-whole.jpg', 'Fresh whole ingredients arranged on a plate', '', '1.2/1'),
           i3=img('food-bowl.jpg', 'A balanced breakfast bowl of yogurt and berries', '', '1.2/1'),
           b1=btn('index.html#guide', 'Download free', 'clay'),
           b2=btn('index.html#guide', 'Tell me when it is ready', 'ghost'),
           b3=btn('index.html#guide', 'Join the waitlist', 'ghost')))

    b.append(GUIDE)
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
     'is that you are not trying hard enough.', 'journal-01.jpg'),
    ('Food clarity', 'What weight-loss medications do, and what they do not teach you',
     'Why so many women are reaching for them, what changes when you stop, and '
     'what the education route genuinely asks of you.', 'journal-02.jpg'),
    ('Label literacy', 'How to read a nutrition label in thirty seconds',
     'Serving size, protein, added sugar. Three numbers, in this order, and you '
     'can judge almost any packet in the aisle.', 'journal-03.jpg'),
    ('Over 40', 'Stubborn belly fat after 40: what actually changed',
     'Your body did not betray you. Here is what shifts as we get older, and '
     'what to do about it that is not another crash diet.', 'journal-04.jpg'),
    ('Portions', 'What a portion really looks like on your plate',
     'You do not need a food scale on the counter for the rest of your life. '
     'You need a reliable way to eyeball it.', 'journal-05.jpg'),
    ('Simple action', 'Confused about what to eat? Start with these four questions',
     'Before you change a single thing about how you eat, answer these. They '
     'will save you months of guessing.', 'journal-06.jpg'),
]


def build_blog():
    cards = []
    for cat, title, dek, im in POSTS:
        cards.append(u"""      <article class="post">
        {im}
        <p class="cat">{cat}</p>
        <h3>{title}</h3>
        <p>{dek}</p>
        <span class="more">Coming soon</span>
      </article>""".format(im=img(im, '', '', '1.42/1'), cat=cat, title=title, dek=dek))

    b = [u"""
<section class="phero" data-sec="Journal">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        {eyebrow}
        <h1 data-rv="lines">{h}</h1>
        <p class="lede" data-rv style="--d:560ms">Straight answers on food, portions and progress. No
        trends, no hype, and no jargon without a translation.</p>
      </div>
      <div>{im}</div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true"><span class="shape s1 d1"></span><span class="shape s2 d2"></span></div>
</section>

<section class="s" data-sec="Articles">
  <div class="wrap">
    <div class="posts" data-stagger="90">
{cards}
    </div>
    <div class="todo">
      <strong>Draft note for Betty:</strong> these six titles come from the
      keywords in your niche form, so they are the searches your audience is
      actually making. Nothing is published yet. Write them, or record them and
      we will transcribe, and each card becomes a real article page.
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow('The journal'),
           h=lines('No nutrition', 'noise. Just what', 'to do next.'),
           im=hero_img('food-prep.jpg',
                       'Balanced portioned meals prepared for the week', 'sq'),
           cards='\n'.join(cards))]

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
def build_contact():
    b = [u"""
<section class="phero" data-sec="Start here">
  <div class="wrap wide">
    <div class="phero-grid">
      <div>
        {eyebrow}
        <h1 data-rv="lines">{h}</h1>
        <p class="lede" data-rv style="--d:560ms">A free 20-minute conversation. No pressure and no
        pitch you have to sit through, just an honest answer on whether I can
        help.</p>
      </div>
      <div>{im}</div>
    </div>
  </div>
  <div class="shapes" aria-hidden="true"><span class="shape s1 d1"></span><span class="shape s2 d2"></span></div>
</section>

<section class="s" id="book" data-sec="Book a call">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        {eyebrow2}
        <h2 data-rv="lines">{h2}</h2>
        <p data-rv style="--d:140ms">Fill this in and I will come back to you with a time. If you
        would rather just email, that works too.</p>
        <form action="https://formspree.io/f/REPLACE_ME" method="POST" data-rv style="--d:200ms">
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
        </form>
        <div class="todo">
          <strong>Draft note:</strong> this form is not wired up yet. Point it at
          a Formspree endpoint, or drop in a Calendly or TidyCal embed, and it
          goes live.
        </div>
      </div>
      <aside class="info-block" data-rv="right" style="--d:180ms">
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
""".format(eyebrow=eyebrow('Start here'),
           h=lines('Let us talk about', 'your week, not', 'another diet.'),
           im=hero_img('betty-street.jpg',
                       'Betty out walking on a bright street', 'sq'),
           eyebrow2=eyebrow('Book your consultation'),
           h2=lines('Tell me where you', 'are right now.'))]

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

if __name__ == '__main__':
    for name, fn in PAGES.items():
        html = fn()
        for bad in (u'—', u'–'):
            assert bad not in html, 'dash found in ' + name
        with io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        print('%-15s %6d bytes' % (name, len(html.encode('utf-8'))))
