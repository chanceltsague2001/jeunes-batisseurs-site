/* ETS Les Jeunes Bâtisseurs — interactions & motion design (sans dépendance) */
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const desktop = window.matchMedia('(min-width: 1200px)');
  const header = document.querySelector('.header');

  /* 1. En-tête : transparent → anthracite après 80 px, se cache en descendant, réapparaît en remontant */
  let lastY = 0;
  const onScrollHeader = () => {
    const y = window.scrollY;
    if (!header) return;
    header.classList.toggle('is-solid', y > 80 || header.dataset.solid === 'true');
    if (!document.body.classList.contains('menu-open')) {
      header.classList.toggle('is-hidden', y > 600 && y > lastY + 4);
      if (y < lastY - 4) header.classList.remove('is-hidden');
    }
    lastY = y;
  };

  /* 2. Menu mobile plein écran */
  const burger = document.querySelector('.burger');
  burger && burger.addEventListener('click', () => {
    const open = document.body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  document.querySelectorAll('.mobile-menu a').forEach(a => a.addEventListener('click', () => {
    document.body.classList.remove('menu-open'); document.body.style.overflow = '';
  }));

  /* 3. Révélation au scroll avec décalage (stagger) automatique pour les groupes */
  document.querySelectorAll('[data-stagger]').forEach(group => {
    const step = parseInt(group.dataset.stagger || '80', 10);
    [...group.querySelectorAll(':scope > [data-reveal]')].forEach((el, i) => el.style.setProperty('--delay', `${i * step}ms`));
  });
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
  document.querySelectorAll('[data-reveal]').forEach(el => reduce ? el.classList.add('is-in') : io.observe(el));

  /* 4. Parallaxe légère (desktop uniquement, max ±28 px) */
  const px = [...document.querySelectorAll('[data-parallax]')];
  const parallax = () => {
    if (reduce || !desktop.matches) { px.forEach(el => el.style.transform = ''); return; }
    const vh = window.innerHeight;
    px.forEach(el => {
      const r = el.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const progress = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2); // -1 … 1
      const max = parseFloat(el.dataset.parallax || '28');
      el.style.transform = `translate3d(0, ${(-progress * max).toFixed(1)}px, 0)`;
    });
  };

  /* 5. Section « Notre méthode » : défilement horizontal piloté par le scroll vertical */
  const proc = document.querySelector('.process');
  const track = proc && proc.querySelector('.process__track');
  const bar = proc && proc.querySelector('.process__bar');
  const sizeProcess = () => {
    if (!proc) return;
    if (!desktop.matches || reduce) { proc.style.height = ''; track.style.transform = ''; return; }
    const dist = track.scrollWidth - window.innerWidth + 64;
    proc.style.height = `${window.innerHeight + Math.max(dist, 0)}px`;
  };
  const processScroll = () => {
    if (!proc || !desktop.matches || reduce) return;
    const r = proc.getBoundingClientRect();
    const total = proc.offsetHeight - window.innerHeight;
    const p = Math.min(Math.max(-r.top / total, 0), 1);
    const dist = track.scrollWidth - window.innerWidth + 64;
    track.style.transform = `translate3d(${(-p * dist).toFixed(1)}px,0,0)`;
    bar && bar.style.setProperty('--p', p.toFixed(3));
  };

  /* Boucle rAF unique pour tous les effets liés au scroll */
  let ticking = false;
  const onScroll = () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => { onScrollHeader(); parallax(); processScroll(); waFloat(); ticking = false; });
  };
  const wa = document.querySelector('.wa-float');
  const waFloat = () => wa && wa.classList.toggle('show', window.scrollY > window.innerHeight * 0.6);
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', () => { sizeProcess(); onScroll(); });
  sizeProcess(); onScroll();

  /* 6. Galerie : filtres + lightbox */
  const chips = document.querySelectorAll('.chip');
  chips.forEach(c => c.addEventListener('click', () => {
    chips.forEach(x => x.classList.remove('active')); c.classList.add('active');
    const f = c.dataset.filter;
    document.querySelectorAll('.tile').forEach(t => {
      const show = f === 'all' || t.dataset.cat === f;
      t.animate([{ opacity: show ? 0 : 1, transform: show ? 'scale(.97)' : 'none' }, { opacity: show ? 1 : 0, transform: show ? 'none' : 'scale(.97)' }],
        { duration: 280, easing: 'cubic-bezier(.22,.61,.36,1)', fill: 'forwards' });
      t.style.pointerEvents = show ? '' : 'none';
    });
  }));
  const lb = document.querySelector('.lightbox');
  if (lb) {
    const tiles = [...document.querySelectorAll('.tile')];
    let idx = 0;
    const img = lb.querySelector('img'), cap = lb.querySelector('.lb-cap');
    const show = i => { idx = (i + tiles.length) % tiles.length; const t = tiles[idx]; img.src = t.querySelector('img').src; img.alt = t.querySelector('img').alt; cap.textContent = t.querySelector('.cap b').textContent; };
    tiles.forEach((t, i) => t.addEventListener('click', () => { show(i); lb.classList.add('open'); lb.querySelector('.lb-close').focus(); }));
    lb.querySelector('.lb-close').addEventListener('click', () => lb.classList.remove('open'));
    lb.querySelector('.lb-prev').addEventListener('click', () => show(idx - 1));
    lb.querySelector('.lb-next').addEventListener('click', () => show(idx + 1));
    document.addEventListener('keydown', e => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') lb.classList.remove('open');
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  /* 7. Transition de page (fondu 180 ms) pour les liens internes */
  const fade = document.querySelector('.page-fade');
  document.querySelectorAll('a[href$=".html"]').forEach(a => a.addEventListener('click', e => {
    if (reduce || e.metaKey || e.ctrlKey) return;
    e.preventDefault(); fade.classList.add('on');
    setTimeout(() => location.href = a.href, 180);
  }));
  window.addEventListener('pageshow', () => fade && fade.classList.remove('on'));

  /* 8. Formulaire de devis : confirmation claire */
  const form = document.querySelector('form.form');
  form && form.addEventListener('submit', e => {
    e.preventDefault();
    form.querySelector('.success').hidden = false;
    form.querySelector('.success').animate([{ opacity: 0, transform: 'translateY(8px)' }, { opacity: 1, transform: 'none' }], { duration: 400, easing: 'cubic-bezier(.16,1,.3,1)' });
  });

  /* Outils de capture (dossier de design) : ?freeze=ms fige l'intro, ?reveal=all affiche tout */
  const q = new URLSearchParams(location.search);
  if (q.has('reveal')) document.documentElement.classList.add('freeze-reveal');
  if (q.has('freeze')) document.getAnimations().forEach(a => { a.pause(); a.currentTime = +q.get('freeze'); });
})();
