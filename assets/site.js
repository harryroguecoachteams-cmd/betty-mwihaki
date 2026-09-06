/* =============================================================================
   Betty | motion + interface
   One rAF scroll loop drives everything. Every hidden state lives behind
   html.js, which is added by the inline head script and stripped again if
   anything in here throws, so the page always reads.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ----------------------------------------------------------- tiny helpers */
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function clamp(v, a, b) { return v < a ? a : v > b ? b : v; }
  function smooth(v) { return v * v * (3 - 2 * v); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function seeded(s) {                                   // mulberry32
    return function () {
      s |= 0; s = s + 0x6D2B79F5 | 0;
      var t = Math.imul(s ^ s >>> 15, 1 | s);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  /* --------------------------------------------- the single scroll pipeline */
  var tasks = [];        // fn(y, vh)
  var measures = [];     // fn() -> refresh cached geometry
  var queued = false;

  function tick() {
    queued = false;
    var y = window.pageYOffset || root.scrollTop || 0;
    var vh = window.innerHeight || root.clientHeight;
    for (var i = 0; i < tasks.length; i++) { tasks[i](y, vh); }
  }
  function schedule() { if (!queued) { queued = true; requestAnimationFrame(tick); } }
  function remeasure() { for (var i = 0; i < measures.length; i++) { measures[i](); } schedule(); }

  function docRect(el) {
    var r = el.getBoundingClientRect();
    var y = window.pageYOffset || root.scrollTop || 0;
    return { top: r.top + y, height: r.height, left: r.left, width: r.width };
  }

  /* progress of an element through the viewport, 0 before, 1 after.
     `a` is where counting starts (fraction of viewport height from the top),
     `b` is where it finishes. */
  function through(rect, y, vh, a, b) {
    var start = rect.top - vh * a;
    var end = rect.top + rect.height - vh * b;
    if (end <= start) { return y >= start ? 1 : 0; }
    return clamp((y - start) / (end - start), 0, 1);
  }

  /* progress for a compact graphic: 0 when it is still below the fold,
     1 when it sits centered in the viewport. Keeps a scrubbed piece from
     finishing its animation after the reader has scrolled past it. */
  function toCenter(rect, y, vh) {
    var start = rect.top - vh;
    var end = rect.top + rect.height / 2 - vh / 2;
    if (end <= start) { return y >= start ? 1 : 0; }
    return clamp((y - start) / (end - start), 0, 1);
  }

  /* =========================================================== 1. reveals  */
  /* Position triggers, never ratio thresholds: a ratio silently becomes
     impossible once an element grows taller than viewport / threshold. */
  var REVEALERS = '[data-rv],.imgwrap,.eyebrow,.rule,.step,.principle,.tript,' +
                  '.hero-strip .it,.card,.tier,.quote,.result,.post,.product,.persona .p';

  function revealAll() {
    $$(REVEALERS).forEach(function (el) { el.classList.add('is-in'); });
  }

  function setupReveals() {
    // staggered groups: children of [data-stagger] get an increasing delay
    $$('[data-stagger]').forEach(function (g) {
      var step = parseInt(g.getAttribute('data-stagger'), 10) || 90;
      var kids = $$(':scope > *', g);
      kids.forEach(function (k, i) {
        if (!k.style.getPropertyValue('--d')) { k.style.setProperty('--d', (i * step) + 'ms'); }
      });
    });

    var targets = $$(REVEALERS);
    if (REDUCED || !('IntersectionObserver' in window)) { revealAll(); return; }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -11% 0px' });

    targets.forEach(function (el) {
      // anything already on screen at first paint just lands, staggered by CSS
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.9 && r.bottom > 0) { el.classList.add('is-in'); }
      else { io.observe(el); }
    });
  }

  /* ========================================================== 2. parallax  */
  function setupParallax() {
    if (REDUCED) { return; }
    var items = $$('.imgwrap .par').map(function (el) {
      return { el: el, wrap: el.parentNode, rect: null, amt: 30 };
    });
    if (!items.length) { return; }

    function measure() { items.forEach(function (it) { it.rect = docRect(it.wrap); }); }
    measure();
    measures.push(measure);

    tasks.push(function (y, vh) {
      for (var i = 0; i < items.length; i++) {
        var it = items[i], r = it.rect;
        if (!r) { continue; }
        var bottom = r.top + r.height;
        if (bottom < y - 200 || r.top > y + vh + 200) { continue; }
        var center = (r.top + r.height / 2) - y;          // px from viewport top
        var t = clamp(center / vh, -0.4, 1.4);
        it.el.style.transform = 'translate3d(0,' + ((0.5 - t) * it.amt).toFixed(2) + 'px,0)';
      }
    });
  }

  /* ======================================================= 3. scroll rail  */
  /* The confidence point, doubling as a wayfinder. */
  function setupRail() {
    var rail = $('.rail');
    if (!rail) { return; }
    var line = $('.rail-line', rail);
    var fill = $('.rail-fill', rail);
    var pt = $('.rail-pt', rail);
    var secs = $$('[data-sec]');
    if (!secs.length) { rail.style.display = 'none'; return; }

    var ticks = secs.map(function (s) {
      var b = document.createElement('button');
      b.className = 'rail-tick';
      b.type = 'button';
      b.tabIndex = -1;
      b.setAttribute('data-label', s.getAttribute('data-sec'));
      b.setAttribute('aria-label', 'Jump to ' + s.getAttribute('data-sec'));
      b.addEventListener('click', function () {
        s.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth', block: 'start' });
      });
      line.appendChild(b);
      return { el: b, sec: s, top: 0 };
    });

    var docH = 1;
    function measure() {
      docH = Math.max(1, document.body.scrollHeight - window.innerHeight);
      ticks.forEach(function (t) {
        t.top = docRect(t.sec).top;
        t.el.style.top = clamp(t.top / docH, 0, 1) * 100 + '%';
      });
    }
    measure();
    measures.push(measure);

    tasks.push(function (y, vh) {
      rail.classList.toggle('show', y > vh * 0.7);
      var p = clamp(y / docH, 0, 1);
      var pct = (p * 100).toFixed(2) + '%';
      fill.style.height = pct;
      pt.style.top = pct;
      for (var i = 0; i < ticks.length; i++) {
        var next = ticks[i + 1];
        var on = y >= ticks[i].top - 120 && (!next || y < next.top - 120);
        ticks[i].el.classList.toggle('on', on);
      }
    });
  }

  /* ============================================ 4. clarity field (scrubbed) */
  /* 49 dots. Chaos on the way in, a settled grid on the way out, and the
     clay point arrives last. Transform only, scrubbed to scroll position. */
  function setupClarity() {
    var box = $('.clarity');
    if (!box) { return; }
    var N = 7, total = N * N, mid = Math.floor(total / 2);
    var rnd = seeded(20260906);
    var dots = [];

    for (var i = 0; i < total; i++) {
      var col = i % N, row = (i / N) | 0;
      var d = document.createElement('span');
      d.className = 'dot' + (i === mid ? ' pt' : '');
      box.appendChild(d);
      // ordered target, inset so the grid breathes inside the box
      var ox = 0.13 + (col / (N - 1)) * 0.74;
      var oy = 0.13 + (row / (N - 1)) * 0.74;
      // chaos start, pushed outward so the settle reads as a gathering
      var ang = rnd() * Math.PI * 2;
      var rad = 0.30 + rnd() * 0.42;
      dots.push({
        el: d,
        ox: ox, oy: oy,
        cx: clamp(0.5 + Math.cos(ang) * rad, 0.02, 0.98),
        cy: clamp(0.5 + Math.sin(ang) * rad, 0.02, 0.98),
        lag: i === mid ? 0.34 : rnd() * 0.30
      });
    }

    var la = $('.lbl.a', box), lb = $('.lbl.b', box);
    var stages = $$('[data-stage]');
    var W = 0, H = 0, rect = null;

    function measure() {
      W = box.clientWidth; H = box.clientHeight;
      rect = docRect(box);
    }
    measure();
    measures.push(measure);

    function paint(p) {
      var e = smooth(p);
      for (var i = 0; i < dots.length; i++) {
        var d = dots[i];
        var t = smooth(clamp((e - d.lag) / (1 - d.lag), 0, 1));
        var x = lerp(d.cx, d.ox, t) * W;
        var y = lerp(d.cy, d.oy, t) * H;
        var s = lerp(0.62, 1, t);
        d.el.style.transform = 'translate3d(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px,0) scale(' + s.toFixed(3) + ')';
        d.el.style.opacity = lerp(0.42, 1, t).toFixed(3);
      }
      if (la) { la.style.opacity = (1 - clamp((e - 0.18) / 0.38, 0, 1)).toFixed(3); }
      if (lb) { lb.style.opacity = clamp((e - 0.46) / 0.34, 0, 1).toFixed(3); }
      for (var k = 0; k < stages.length; k++) {
        stages[k].classList.toggle('lit', e >= k * 0.30 + 0.06);
      }
    }

    if (REDUCED) { paint(1); return; }
    tasks.push(function (y, vh) {
      if (!rect) { return; }
      paint(toCenter(rect, y, vh));
    });
  }

  /* ================================================ 5. the method, 5 phases */
  function setupArc() {
    var wrap = $('.arc-wrap');
    if (!wrap) { return; }
    var svg = $('svg', wrap);
    var path = $('.track', svg);
    var draw = $('.draw', svg);
    var holder = $('.arc-nodes', wrap);
    var labels = (wrap.getAttribute('data-phases') || '').split('|');
    var vb = svg.viewBox.baseVal;
    var len = path.getTotalLength();
    var n = labels.length;
    var nodes = [];

    draw.setAttribute('d', path.getAttribute('d'));
    draw.style.strokeDasharray = len;
    draw.style.strokeDashoffset = len;

    for (var i = 0; i < n; i++) {
      var at = path.getPointAtLength((len * i) / (n - 1));
      var dot = document.createElement('span');
      dot.className = 'arc-node';
      dot.style.left = (at.x / vb.width) * 100 + '%';
      dot.style.top = (at.y / vb.height) * 100 + '%';
      holder.appendChild(dot);

      var cap = document.createElement('div');
      cap.className = 'arc-cap';
      cap.style.left = clamp((at.x / vb.width) * 100, 7, 93) + '%';
      cap.style.top = ((at.y + 30) / vb.height) * 100 + '%';
      cap.innerHTML = '<p class="p">Phase 0' + (i + 1) + '</p><p class="t">' + labels[i] + '</p>';
      holder.appendChild(cap);
      nodes.push({ dot: dot, cap: cap, at: i / (n - 1) });
    }

    var rect = null;
    function measure() { rect = docRect(wrap); }
    measure();
    measures.push(measure);

    function paint(p) {
      draw.style.strokeDashoffset = (len * (1 - p)).toFixed(1);
      for (var i = 0; i < nodes.length; i++) {
        var lit = p >= nodes[i].at - 0.015;
        nodes[i].dot.classList.toggle('lit', lit);
        nodes[i].cap.classList.toggle('lit', lit);
      }
    }
    if (REDUCED) { paint(1); return; }
    tasks.push(function (y, vh) { if (rect) { paint(toCenter(rect, y, vh)); } });
  }

  /* ---------------------------------- vertical rails (mobile arc + Method) */
  function setupRails() {
    $$('.rails').forEach(function (wrap) {
      var prog = $('.prog', wrap);
      var phases = $$('.phase', wrap);
      if (!prog || !phases.length) { return; }
      var rect = null;
      function measure() { rect = docRect(wrap); }
      measure();
      measures.push(measure);

      function paint(p) {
        prog.style.setProperty('--p', p.toFixed(4));
        for (var i = 0; i < phases.length; i++) {
          phases[i].classList.toggle('lit', p >= (i / phases.length) + 0.03);
        }
      }
      if (REDUCED) { paint(1); return; }
      tasks.push(function (y, vh) { if (rect) { paint(through(rect, y, vh, 0.8, 0.58)); } });
    });
  }

  /* ========================================================== 6. counters  */
  function setupCounters() {
    var els = $$('[data-count]');
    if (!els.length) { return; }
    els.forEach(function (el) {
      var to = parseFloat(el.getAttribute('data-count')) || 0;
      var suffix = el.getAttribute('data-suffix') || '';
      if (REDUCED || !('IntersectionObserver' in window)) { el.textContent = to + suffix; return; }
      el.textContent = '0' + suffix;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) { return; }
          io.disconnect();
          var t0 = 0;
          (function step(ts) {
            if (!t0) { t0 = ts; }
            var p = clamp((ts - t0) / 1400, 0, 1);
            var eased = 1 - Math.pow(1 - p, 4);
            el.textContent = Math.round(to * eased) + suffix;
            if (p < 1) { requestAnimationFrame(step); }
          })(0);
        });
      }, { threshold: 0, rootMargin: '0px 0px -18% 0px' });
      io.observe(el);
    });
  }

  /* ========================================================== 7. marquee   */
  /* Cloned in JS so the markup stays clean and non-JS gets one static pass. */
  function setupMarquee() {
    $$('.marq-track').forEach(function (t) {
      if (REDUCED) { return; }
      var clone = t.innerHTML;
      t.insertAdjacentHTML('beforeend', clone);
      $$('.it', t).slice($$('.it', t).length / 2).forEach(function (n) {
        n.setAttribute('aria-hidden', 'true');
      });
      t.classList.add('run');
    });
  }

  /* ======================================================= 8. header + nav */
  function setupHeader() {
    var header = $('.site-header');
    var toggle = $('#navToggle');
    var nav = $('#nav');
    var scrim = $('#navScrim');
    if (toggle && nav) {
      if (scrim) { scrim.addEventListener('click', function () { if (nav.classList.contains('open')) { toggle.click(); } }); }
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
        }, 1000);
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
    var last = 0;
    tasks.push(function (y) {
      header.classList.toggle('stuck', y > 24);
      var down = y > last && y > 320;
      if (!document.body.classList.contains('nav-open')) {
        header.classList.toggle('hide', down);
      }
      last = y;
    });
  }

  /* =========================================================== 9. accordion */
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

  /* ================================================= 10. page transitions  */
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
      setTimeout(function () { location.href = a.href; }, 290);
    });
    window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });
  }

  /* ================================================================= boot  */
  function boot() {
    setupHeader();
    setupFaq();
    setupTransitions();
    setupReveals();
    setupParallax();
    setupClarity();
    setupArc();
    setupRails();
    setupCounters();
    setupMarquee();
    setupRail();

    var y = new Date().getFullYear();
    $$('[data-year]').forEach(function (n) { n.textContent = y; });

    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', remeasure, { passive: true });
    window.addEventListener('load', function () {
      remeasure();
      // failsafe: nothing may stay hidden because an observer never fired
      setTimeout(function () { revealAll(); remeasure(); }, 2200);
    });
    schedule();
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
