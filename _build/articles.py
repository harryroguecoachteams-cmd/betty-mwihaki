# -*- coding: utf-8 -*-
"""
The Journal's actual content.

The Journal used to be six headlines with "Coming soon" under every one of
them, which reads to a stranger as a business that built the shelves before it
had anything to put on them. These three are the first three real ones. They
are the three topics Betty already teaches inside the sixteen weeks: why the
scale will not move, how to read a label, and what a portion looks like.

House rules that apply to every article added here:

  * First person. Betty is speaking, not an agency describing her.
  * Second person for the reader, short sentences, no jargon without a
    translation in the same sentence. That is the deck's tone of voice slide.
  * No diagnosis, cure or reversal language, and no guaranteed outcome. Deck
    page 28. Anything that edges toward a medical question ends by sending the
    reader to their doctor, not to a coaching call.
  * No em dashes and no en dashes. build.py asserts on both.
  * No number about Betty (years coaching, clients coached) that she has not
    given us in writing.

Every article needs a client-facing read: they are written in her voice and she
has to be able to say all of it out loud. That is an open item in the README.
"""

# slug, category, title, dek, date (ISO), read time, body html
ARTICLES = [

    dict(
        slug='eating-healthy-not-losing-weight',
        cat='Food clarity',
        title='Why you are eating healthy and still not losing weight',
        dek='The four reasons I see most often, and not one of them is that '
            'you are not trying hard enough.',
        date='2026-09-07',
        mins=5,
        desc='You changed how you eat and the scale has not moved. Here are '
             'the four most common reasons, from a nutrition coach: portion '
             'size, the whole week, protein, and the restart cycle.',
        body=u"""
<p>You are doing the things. There are vegetables in the fridge. There is less
takeout than there used to be. You swapped the soda, you walk more than you did
a year ago, and you have not had a proper dessert in weeks.</p>

<p>The scale has not noticed.</p>

<p>Let me say the thing that usually gets said far too late: this is almost
never a discipline problem. In the women I coach, effort is rarely what is
missing. Effort is usually the thing there is too much of, pointed in four
directions at once.</p>

<p>Here are the four reasons I run into most.</p>

<h2>1. Healthy and how much are two different questions</h2>

<p>Olive oil. Granola. Nuts. Nut butter. Avocado. Protein bars. Smoothies.</p>

<p>Every one of those is real food and I am not asking you to give any of them
up. They are also some of the most energy dense things in your kitchen, which
means a small change in the amount is a large change in the total.</p>

<p class="pull">Healthy tells you about the quality of a food. It tells you
nothing about how much of it you ate.</p>

<p>Two level tablespoons of peanut butter and a generous scoop straight from
the jar are the same food and roughly twice the energy. A handful of almonds
eaten standing at the counter is very easy to eat twice. A smoothie can quietly
carry a whole meal of fruit, oats, yogurt and honey and still leave you hungry
an hour later, because you drank it in ninety seconds and your body barely
registered it as eating.</p>

<p>None of that is a moral failure. It is arithmetic, and arithmetic is
fixable.</p>

<h2>2. Your week is not four days long</h2>

<p>Monday to Thursday you are precise. Then Friday evening arrives. There is a
birthday, a restaurant, a Sunday lunch at somebody's mother's house, and by
Monday you are precise again.</p>

<p>If you only look at the four disciplined days, the numbers make no sense. If
you look at all seven, they usually make perfect sense.</p>

<p>I am not telling you to eat plain chicken on a Saturday night. I want you to
eat at the restaurant. But you cannot count Monday and ignore Saturday and then
be surprised, because your body counts the whole week whether you do or
not.</p>

<p>Try this before you try another diet. For one week, write down what you eat
on the three days you would normally not write anything down. Do not change
them. Just look at them.</p>

<h2>3. Protein is doing less work for you than it could</h2>

<p>Protein does two jobs that matter a great deal to a woman who wants to lose
weight and still like what she sees.</p>

<p>It keeps you full for longer than the same amount of energy from anything
else, which makes the evening easier with no willpower involved at all.</p>

<p>And when you are eating less overall, protein is what helps you hold on to
the muscle you already have. Losing weight is not really the goal on its own.
Losing weight while keeping your strength and your shape is the goal, and
protein is a large part of the difference between those two outcomes.</p>

<p>Most women I meet are not eating too much. They are eating a breakfast with
almost no protein in it, a lunch built around bread, and then a good dinner. By
four in the afternoon they are ravenous, and the four o'clock version of a
person makes very different decisions than the ten o'clock version.</p>

<p>You do not need a spreadsheet for this. Start by putting a real protein in
every meal including the first one, roughly a palm sized portion. How much you
personally need depends on your body, your goal and how you train, and working
that out is one of the first things we do together. But almost nobody gets
worse by anchoring breakfast.</p>

<h2>4. You keep restarting instead of continuing</h2>

<p>This one costs more than the other three put together.</p>

<p>The cycle goes like this. Strict from Monday. Something goes wrong on
Wednesday. Wednesday becomes a write off, and so does the rest of the week,
because the plan is already broken. Start again Monday.</p>

<p>Six weeks of that is six good days. Not six weeks.</p>

<p>One imperfect meal is still just one meal. The next meal is a completely
separate decision and it is available to you in a few hours. There is nothing
to restart, because nothing actually ended.</p>

<p>Progress comes from what you repeat. Unglamorous, and true.</p>

<h2>What I would do this week</h2>

<ol>
  <li>Pick the meal you eat most often and look honestly at the portion. Not to
  punish it. Just so you know what it is.</li>
  <li>Put a protein in breakfast. That single change does more than most whole
  diets.</li>
  <li>Count the week, not the day.</li>
  <li>Change one thing, not seven. Seven changes at once is how a week becomes
  a write off.</li>
</ol>

<h2>One more thing, and I mean it</h2>

<p>If your weight has changed quickly and you cannot explain it, if you are
managing a medical condition, or if you take prescription medication, talk to
your doctor. Nutrition coaching sits alongside medical care. It does not
replace it, and I would rather you had both.</p>
""",
    ),

    dict(
        slug='read-a-nutrition-label',
        cat='Label literacy',
        title='How to read a nutrition label in thirty seconds',
        dek='Serving size, protein, added sugar. Three numbers, in that order, '
            'and you can judge almost any packet in the aisle.',
        date='2026-09-07',
        mins=4,
        desc='A plain English method for reading a nutrition label fast: '
             'serving size first, then protein, then added sugars, then the '
             'first three ingredients.',
        body=u"""
<p>Most people read a nutrition panel the way you read a contract you have
already signed. Eyes go down the numbers, nothing goes in, and you buy it
anyway because the front of the box said high protein.</p>

<p>You do not need to read the whole panel. You need three numbers, in one
order, and then you can judge almost anything in the aisle in about half a
minute.</p>

<p>Serving size. Protein. Added sugar.</p>

<h2>First: the serving size, and how many are in the pack</h2>

<p>This is the number every other number depends on, and it is the one the
front of the pack is quietly relying on you to skip.</p>

<p>Look at the top of the panel. It gives you the serving size, and directly
underneath it, the number of servings in the container. Everything below that
line describes one serving. Not the packet. One serving.</p>

<p>Two servings in a bottle of juice. Two and a half in a bag of chips that no
human being has ever eaten across two and a half sittings. Four in a tub of ice
cream.</p>

<p class="pull">Every number on the panel describes one serving. The bag has no
idea what you plan to do with it.</p>

<p>So the first question is never how many calories. It is: how much of this am
I actually going to eat? If the answer is the whole bag and the bag holds two
servings, double every number on the panel before you judge it. That one habit
changes more shopping decisions than anything else I teach.</p>

<h2>Second: protein</h2>

<p>Now find protein, in grams, per serving.</p>

<p>I want you to look at this before calories, because it tells you what the
food is going to do for you rather than only what it costs you. Protein is the
number that decides whether this holds you until your next meal or puts you
back in the cupboard in an hour.</p>

<p>A rough test for anything sold as a snack or a meal replacement: if there is
very little protein in it, it is a carbohydrate wearing a health label. That is
not a reason never to eat it. It is a reason to stop expecting it to carry you
to dinner.</p>

<p>Compare like with like. Two yogurts, same shelf, same size, similar price.
One has four grams of protein and the other has fifteen. Those are genuinely
different foods, and the front of the pot will not always tell you which one is
in your hand.</p>

<h2>Third: added sugar</h2>

<p>On a United States label there are two sugar lines, and the difference
between them matters.</p>

<p><strong>Total sugars</strong> includes what was already in the food. The
sugar in plain milk. The sugar in fruit. Nobody needs to worry about the sugar
in an apple.</p>

<p><strong>Added sugars</strong> is the line somebody chose to put there. That
is the one to read.</p>

<p>A plain yogurt can show a fair number under total sugars and zero under
added. The flavored version, same brand and same size, can carry two or three
teaspoons that were a decision. Four grams is about a teaspoon, which is a
useful thing to carry around in your head.</p>

<p>You are not banning sugar. You are deciding where you spend it. I would
rather you spent it on something you sit down and enjoy than on a sauce you did
not know was sweet.</p>

<h2>Two more things, once the three numbers are quick</h2>

<h3>The first three ingredients</h3>

<p>Ingredients are listed by weight, heaviest first. You do not need to read all
thirty of them. Read the first three. That is most of what you are holding.</p>

<p>If sugar, or one of the many words that mean sugar, is in the first three
ingredients of something being sold to you as a health food, you now know more
than the front of the box was telling you.</p>

<h3>The front of the pack is advertising</h3>

<p>High protein. Low fat. All natural. Made with real fruit. Those are
marketing claims. Most of them are perfectly legal and none of them are the
panel.</p>

<p>Low fat very often means sugar went in to make it taste like food again.
Made with real fruit can mean a splash. Natural means close to nothing.</p>

<p>The front is written to sell it. The back is there because the law says so.
Read the back.</p>

<h2>The thirty second routine</h2>

<ol>
  <li>Serving size, and how many servings are in the pack. Multiply if you are
  eating the whole thing.</li>
  <li>Protein per serving. Is this going to hold you or not?</li>
  <li>Added sugars, not total sugars. Four grams is roughly a teaspoon.</li>
  <li>The first three ingredients.</li>
</ol>

<p>Do that four or five times in a real aisle and it stops being a task. It
becomes something you notice without deciding to.</p>
""",
    ),

    dict(
        slug='what-a-portion-looks-like',
        cat='Portions',
        title='What a portion really looks like on your plate',
        dek='You do not need a food scale on the counter for the rest of your '
            'life. You need a reliable way to judge it by eye.',
        date='2026-09-07',
        mins=4,
        desc='How to judge a portion without weighing every meal, using your '
             'own hands and your own plates, plus the three places portions '
             'usually go wrong.',
        body=u"""
<p>There is a version of nutrition where you weigh everything, log everything
and know your numbers to the gram. I have lived in that version. I prepared for
bodybuilding competitions, and for months at a time every gram was accounted
for.</p>

<p>It works. It is also not a life, and it is not what I am going to ask of
you.</p>

<p>What you need is not a scale on the counter forever. You need a reliable way
to judge a portion by eye, so you can make the call at a friend's house, in a
restaurant, and at seven on a Wednesday evening when you are tired.</p>

<h2>Your hand is the measuring cup you never leave at home</h2>

<p>Your hand is roughly proportional to you. A tall woman has a bigger hand and
needs more food than a smaller woman does. That is exactly the property you want
in a measuring tool.</p>

<ul>
  <li><strong>Protein: a palm.</strong> Thickness as well as width. Chicken,
  fish, beef, eggs, cottage cheese, Greek yogurt, beans.</li>
  <li><strong>Vegetables: a fist</strong>, and more than one is fine. This is
  the one thing almost nobody is overeating.</li>
  <li><strong>Starchy carbohydrates: a cupped hand.</strong> Rice, pasta,
  potato, bread, oats.</li>
  <li><strong>Fats: a thumb.</strong> Oil, butter, nut butter, cheese,
  nuts.</li>
</ul>

<p>That is one meal. For most women, most of the time, one palm, one or two
fists, one cupped hand and a thumb is a plate that works.</p>

<p>Notice what is not in that list. No food is banned. Nothing has to be
weighed. And it travels with you, which a kitchen scale does not.</p>

<h2>The plate version, if you would rather look than count</h2>

<p>Same idea, done by area. Half the plate vegetables. A quarter protein. A
quarter starchy carbohydrate. A thumb of fat somewhere, usually in the
cooking.</p>

<p>If you eat out of a bowl the same proportions still apply, they are just
harder to see, which is why I ask a lot of women to use a plate for the first
few weeks. Not forever. Only long enough for your eye to learn it.</p>

<h2>Where portions actually go wrong</h2>

<h3>The food you never put on a plate</h3>

<p>Nothing eaten standing at the counter feels like a portion. The piece of
cheese while you cook. The last of the children's dinner. The handful from the
bag on the way past.</p>

<p>Individually trivial, and together very often the whole difference. I am not
asking you to stop. I am asking you to notice, for one week.</p>

<h3>Restaurants</h3>

<p>A restaurant portion is frequently two of yours, and it is built that way on
purpose. That is not a trap, it is the business.</p>

<p>Two things that work. Decide before the food arrives that half of it is
going home. Or order a protein and a vegetable side instead of a dish where the
carbohydrate is the entire plate. Neither one requires you to explain yourself
to anybody at the table.</p>

<h3>Anything you drink</h3>

<p>A latte, a juice, a glass of wine and a smoothie all pass through without
registering as a portion. They still count. This is the single most common
thing I find when a woman tells me she is eating almost nothing and nothing is
changing.</p>

<h2>Do you ever need a scale?</h2>

<p>Sometimes. Briefly. As a teaching tool.</p>

<p>If you genuinely cannot picture what a hundred grams of cooked rice looks
like, weigh it once. Look at it, on your own plate, in your own kitchen. Then
put the scale away. You are calibrating your eye, not signing up to weigh your
food for the rest of your life.</p>

<p class="pull">A plan tells you the number. An education means you can still
make the call when the number is not there.</p>

<h2>What to do this week</h2>

<ol>
  <li>Use a plate for your main meal every day and set it out to the hand sizes
  above.</li>
  <li>Put the vegetables on first, before you decide anything else.</li>
  <li>Notice the food you eat without plating it. Only notice it.</li>
  <li>Weigh exactly one thing you eat often, once, and then stop.</li>
</ol>

<p>Give that a week and you will start seeing portions instead of guessing at
them. That is a skill, and once you have it nobody can take it back off
you.</p>
""",
    ),
]

# Written, waiting their turn. These are the topics that used to sit on the
# Journal index reading "Coming soon", which is why they now live here instead
# of on a public page.
BACKLOG = [
    ('Food clarity', 'What weight-loss medications do, and what they do not '
                     'teach you'),
    ('Over 40', 'Stubborn belly fat after 40: what actually changed'),
    ('Simple action', 'Confused about what to eat? Start with these four '
                      'questions'),
]
