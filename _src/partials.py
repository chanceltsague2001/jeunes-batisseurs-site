ICONS = {
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'arrow-up': '<path d="M12 19V5M6 11l6-6 6 6"/>',
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 'wa': '<path d="M3 21l1.6-4.6A8.5 8.5 0 1 1 7.7 19.6z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1.2-1.2-1.8-.9-.8.8a4 4 0 0 1-2.3-2.3l.8-.8-.9-1.8L9.5 9"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 'pin': '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'check-c': '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
 'zoom': '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>',
 'close': '<path d="M6 6l12 12M18 6 6 18"/>',
 'chev-l': '<path d="m15 18-6-6 6-6"/>', 'chev-r': '<path d="m9 18 6-6-6-6"/>',
 'consult': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/><path d="M9 11h6M9 14h4"/>',
 'plans': '<path d="M3 21V5a2 2 0 0 1 2-2h10l6 6v12z"/><path d="M15 3v6h6M7 13h10M7 17h6M11 13v8"/>',
 'plumb': '<path d="M12 2.7S6 9.3 6 14a6 6 0 0 0 12 0c0-4.7-6-11.3-6-11.3z"/><path d="M9.5 15a2.5 2.5 0 0 0 2.5 2.5"/>',
 'btp': '<path d="M2 20h20M4 20V10l6-4v14M10 20V4l10 4v12"/><path d="M14 10h2M14 13h2M14 16h2"/>',
 'elec': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 'cctv': '<path d="M3 7.5 16 3l2.5 7.5L5.5 15z"/><path d="m12 13 1.5 4.5H19M19 15v5M7.3 14.4 6 18H3"/>',
 'clip': '<rect x="5" y="4" width="14" height="18" rx="2"/><path d="M9 2h6v4H9zM9 13l2 2 4-4"/>',
 'layers': '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
 'route': '<circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H15a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h6.5"/>',
 'puzzle': '<path d="M4 7h4a2 2 0 1 1 4 0h4v4a2 2 0 1 1 0 4v4h-4a2 2 0 1 0-4 0H4v-4a2 2 0 1 0 0-4z"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}
def icon(name, cls=''):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

PHONE1, PHONE2 = '659 256 672', '697 899 793'
TEL1, WA = 'tel:+237659256672', 'https://wa.me/237659256672'

def header(active='', solid=False):
    links = [('index.html','Accueil'),('index.html#services','Services'),('realisations.html','Réalisations'),('index.html#apropos','À propos'),('contact.html','Contact')]
    nav = ''.join(f'<a href="{h}" class="{"active" if t==active else ""}">{t}</a>' for h,t in links)
    mob = ''.join(f'<a class="m-link" href="{h}">{t}<span>0{i+1}</span></a>' for i,(h,t) in enumerate(links))
    return f'''
<a class="sr-only" href="#main">Aller au contenu</a>
<header class="header{' is-solid' if solid else ''}" {'data-solid="true"' if solid else ''}>
  <div class="container">
    <a class="brand" href="index.html" aria-label="ETS Les Jeunes Bâtisseurs — accueil">
      <img src="assets/img/mark-white.png" alt="" width="58" height="44">
      <span class="txt"><b>LES JEUNES<br>BÂTISSEURS</b><small>CONCEPTIONS &amp; RÉALISATIONS</small></span>
    </a>
    <nav class="nav" aria-label="Navigation principale">{nav}</nav>
    <div style="display:flex;gap:12px;align-items:center">
      <a class="btn desk" href="contact.html">Demander un devis {icon('arrow','arrow')}</a>
      <button class="burger" aria-label="Ouvrir le menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" role="dialog" aria-label="Menu">
  {mob}
  <div class="m-foot">
    <a class="btn" href="contact.html">Demander un devis {icon('arrow','arrow')}</a>
    <a class="btn btn--wa" href="{WA}">{icon('wa','arrow')} WhatsApp</a>
  </div>
</div>'''

def footer():
    return f'''
<footer class="footer">
  <div class="container">
    <div class="cols">
      <div>
        <a class="brand" href="index.html"><img src="assets/img/logo-white.png" alt="ETS Les Jeunes Bâtisseurs — Conceptions &amp; Réalisations" style="height:96px"></a>
        <p class="desc">Conception, construction et installations techniques : un seul interlocuteur pour accompagner votre projet, de l’étude à la réalisation.</p>
      </div>
      <div><h4>Services</h4><ul>
        <li><a href="index.html#services">Consultation</a></li><li><a href="index.html#services">Conception des plans</a></li>
        <li><a href="index.html#services">Travaux BTP</a></li><li><a href="index.html#services">Plomberie &amp; sanitaire</a></li>
        <li><a href="index.html#services">Électricité</a></li><li><a href="index.html#services">Vidéosurveillance</a></li></ul></div>
      <div><h4>Entreprise</h4><ul>
        <li><a href="index.html#apropos">À propos</a></li><li><a href="realisations.html">Réalisations</a></li>
        <li><a href="index.html#methode">Notre méthode</a></li><li><a href="contact.html">Demander un devis</a></li></ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="{TEL1}">{PHONE1}</a></li><li><a href="tel:+237697899793">{PHONE2}</a></li>
        <li><a href="{WA}">WhatsApp</a></li><li>Yaoundé, Cameroun</li></ul></div>
    </div>
    <div class="bottom">
      <span>© 2026 ETS Les Jeunes Bâtisseurs. Tous droits réservés.</span>
      <a class="to-top" href="#top" aria-label="Retour en haut">{icon('arrow-up')}</a>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" aria-label="Nous écrire sur WhatsApp">{icon('wa')} WhatsApp</a>
<div class="page-fade" aria-hidden="true"></div>'''

def page(title, desc, body, active='', solid=False):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#101923">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/p10.jpg">
<link rel="icon" href="assets/img/mark-color.png">
<link rel="preload" href="assets/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
</head>
<body id="top">
{header(active, solid)}
<main id="main">
{body}
</main>
{footer()}
<script src="js/main.js" defer></script>
</body>
</html>'''
