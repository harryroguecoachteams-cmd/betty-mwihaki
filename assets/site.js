/* =============================================================================
   Betty | interface

   What used to be here: a requestAnimationFrame scroll pipeline driving image
   parallax, a fixed scroll-progress rail with section ticks, a 49 dot field
   scrubbing from chaos into a grid, an SVG arc drawn by stroke-dashoffset with
   nodes placed by getPointAtLength, a scrubbed five phase timeline, count-ups,
   a cloned infinite marquee, and a stagger system that gave every child of
   every grid an increasing transition delay.

   All of it worked. Collectively it made the site read as a demonstration of
   what a page can do rather than as Betty's website, so the September 2026 pass
   removed it. What is left is behaviour, not decoration: the nav, the
   accordion, one reveal, and the page fade.

   Every hidden state still lives behind html.js, which is added by the inline
   head script and stripped again if anything in here throws.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }

  /* ============================================================ 1. reveal  */
  /* One reveal, on block-level containers that opted in with data-rv. Position
     triggers, never ratio thresholds: a ratio silently becomes impossible once
     an element grows taller than viewport / threshold. */
  function revealAll() {
    $$('[data-rv]').forEach(function (el) { el.classList.add('is-in'); });
  }

  function setupReveal() {
    var targets = $$('[data-rv]');
    if (!targets.length) { return; }
    if (REDUCED || !('IntersectionObserver' in window)) { revealAll(); return; }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -11% 0px' });

    targets.forEach(function (el) {
      // anything already on screen at first paint just lands
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.9 && r.bottom > 0) { el.classList.add('is-in'); }
      else { io.observe(el); }
    });
  }

  /* ======================================================= 2. header + nav */
  function setupHeader() {
    var header = $('.site-header');
    var toggle = $('#navToggle');
    var nav = $('#nav');
    var scrim = $('#navScrim');

    if (toggle && nav) {
      if (scrim) {
        scrim.addEventListener('click', function () {
          if (nav.classList.contains('open')) { toggle.click(); }
        });
      }
      toggle.addEventListener('click', function () {
        var open = nav.classList.toggle('open');
        // The panel is viewport-fixed and covers the announce bar, so its top
        // padding has to clear whatever the header actually measures right now.
        if (open && header) {
          nav.style.paddingTop = Math.round(header.getBoundingClientRect().bottom + 26) + 'px';
        }
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        document.body.classList.toggle('nav-open', open);
        if (open && header) { header.classList.remove('hide'); }
        // A transform transition on a layer this size can stay pending on the
        // compositor and never start, which would leave the panel off screen.
        // If it has not moved by the time the transition should be over, drop
        // the transition and land it.
        setTimeout(function () {
          var moved = getComputedStyle(nav).transform;
          var stuck = open && nav.classList.contains('open') &&
                      moved !== 'none' && moved.indexOf('1, 0, 0, 1, 0, 0') === -1;
          if (stuck) {
            nav.style.transition = 'none';
            requestAnimationFrame(function () {
              requestAnimationFrame(function () { nav.style.transition = ''; });
            });
          }
        }, 900);
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && nav.classList.contains('open')) { toggle.click(); toggle.focus(); }
      });
      nav.addEventListener('click', function (e) {
        if (e.target.closest('a') && nav.classList.contains('open')) {
          nav.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
          document.body.classList.remove('nav-open');
        }
      });
    }

    if (!header) { return; }
    var last = 0, queued = false;
    function onScroll() {
      queued = false;
      var y = window.pageYOffset || root.scrollTop || 0;
      header.classList.toggle('stuck', y > 24);
      if (!document.body.classList.contains('nav-open')) {
        header.classList.toggle('hide', y > last && y > 320);
      }
      last = y;
    }
    window.addEventListener('scroll', function () {
      if (!queued) { queued = true; requestAnimationFrame(onScroll); }
    }, { passive: true });
    onScroll();
  }

  /* ========================================================== 3. accordion */
  function setupFaq() {
    $$('.faq .q').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var open = btn.getAttribute('aria-expanded') === 'true';
        var group = btn.closest('.faq');
        if (!open && group) {
          $$('.q[aria-expanded="true"]', group).forEach(function (o) {
            o.setAttribute('aria-expanded', 'false');
          });
        }
        btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      });
    });
  }

  /* ================================================== 4. page transitions  */
  function setupTransitions() {
    if (REDUCED) { return; }
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) { return; }
      var a = e.target.closest && e.target.closest('a');
      if (!a || a.hasAttribute('download')) { return; }
      if (a.target && a.target !== '_self') { return; }
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || /^(mailto:|tel:|javascript:)/i.test(href)) { return; }
      var u;
      try { u = new URL(a.href, location.href); } catch (err) { return; }
      if (u.origin !== location.origin) { return; }
      if (u.pathname === location.pathname && u.hash) { return; }
      e.preventDefault();
      document.body.classList.add('leaving');
      setTimeout(function () { location.href = a.href; }, 280);
    });
    window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });
  }

  /* ================================================================= boot  */
  function boot() {
    setupHeader();
    setupFaq();
    setupTransitions();
    setupReveal();

    var y = new Date().getFullYear();
    $$('[data-year]').forEach(function (n) { n.textContent = y; });

    // failsafe: nothing may stay hidden because an observer never fired
    window.addEventListener('load', function () {
      setTimeout(revealAll, 2200);
    });
  }

  try {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', boot);
    } else { boot(); }
  } catch (err) {
    root.classList.remove('js');
    if (window.console) { console.error(err); }
  }
})();
