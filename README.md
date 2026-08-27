# Betty Mwihaki, Weight-Loss & Nutrition Coach

Draft website for **Beatrice "Betty" Mwihaki Igeria**, built by Rogue Coach Teams
from her RCT Web Tech Intake and her completed Coaching Niche Discovery Form.

**Live draft:** https://harryroguecoachteams-cmd.github.io/betty-mwihaki/

---

## What this is

A static, six-page site modeled on the **"Website 2"** layout Betty picked in the
intake form. The reference Harsh pointed at was
`https://thetravelcoachnetwork.mykajabi.com/`. Structure, section rhythm and type
system follow that reference:

| Reference | Here |
|---|---|
| Fjalla One display + Montserrat body | same |
| Deep teal `#1A5F79` + coral accent | same |
| Crimson announcement bar | free-ebook bar |
| Full-bleed hero + overlay | "Understand your food. Change your body." |
| 3-up photo strip | meal prep / outdoors / balanced bowls |
| 3-up icon cards | Coaching / Learn Your Food / You Are Not Alone |
| Dark statement band | "Finally, a way of eating you can actually keep doing." |
| Image/text splits | pain point + what Betty does |
| Founder story | Betty's story |
| Freebie opt-in band | The Simple Nutrition Starter Guide |
| Testimonial wall | placeholder cards (see below) |
| "I believe that..." list | from her five pillars |

## Pages

- `index.html` = Home
- `about.html` = About Betty
- `services.html` = Coaching, process, FAQ
- `shop.html` = Guides & resources
- `blog.html` = Blog index (six SEO-seeded titles, no articles yet)
- `contact.html` = Contact + booking request form

All six pages Betty selected in the intake are present. No build step. Plain HTML,
one stylesheet, one small JS file for the mobile menu. Edit the files directly.

> The pages were generated once from `build_betty.py` (kept in the session
> scratchpad) purely to keep the header and footer identical across all six. The
> committed HTML is the source of truth from here on. Hand-edit it.

## Copy source

Every claim on this site is Betty's own, taken from her niche discovery form:
her story (yoga in Kenya at 18, bodybuilding in the US), her USP, her five pillars,
her niche statement, and her two real client results. Nothing about her background
or results was invented.

## Before this goes live: open items

1. **Booking link.** Every CTA points at `contact.html#book`. Betty listed
   "consultation booking calls" as the goal but gave no URL. Paste the real
   Calendly/TidyCal link, then find/replace
   `contact.html#book`.
2. **Form endpoint.** Both the opt-in and the contact form post to
   `https://formspree.io/f/REPLACE_ME`. Swap in a real endpoint (or a Calendly
   embed) or the forms silently do nothing.
3. **Testimonials.** The three cards on the Home page are clearly-marked
   placeholders. Betty gave two real client outcomes (the 30 lb / pre-diabetic
   client, and her cousin) and those sit on the page as *results*, in her own
   words, unnamed. Named testimonials still need collecting.
4. **Photos of Betty.** Every image is licensed stock from Pexels, hotlinked. The
   "About" portrait is a placeholder. Get real photos: one from a competition,
   one relaxed in a kitchen. Consider self-hosting the stock images in
   `assets/img/` before launch rather than hotlinking.
5. **Pricing.** Left as "Investment shared on your call" everywhere. Her form says
   the audience can pay $1,000+; she has not confirmed a number.
6. **Facebook URL.** Intake gave the display name "Beatrice M" only, no link. The
   footer icon points at `#`.
7. **Ebook file.** She has written one. It is not in the repo and there is nothing
   to deliver on signup yet.
8. **Blog articles.** Six titles written from her own keywords; no article pages
   exist. Cards say "Coming soon".
9. **Domain.** Currently on `github.io`. Point a real domain when she has one.
10. **Third success story** on the niche form is blank, as is the Section 2
    observations field.

## Health-claims note

This is a weight-loss site, so the copy deliberately avoids medical claims and a
disclaimer sits in the footer of every page. Her cousin's pre-diabetes outcome is
presented as a client result in her own words, not as a treatment claim. Keep it
that way, and have Betty confirm she is comfortable with how both results are
worded before launch.

## Deploy

Pushing to `main` republishes automatically via GitHub Pages.

```bash
git add -A && git commit -m "update" && git push
```
