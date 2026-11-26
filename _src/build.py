import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from partials import *
OUT = os.path.join(os.path.dirname(__file__), '..')

SERVICES = [
 ('consult','Consultation','Conseils et accompagnement pour définir votre projet, vos besoins et les solutions adaptées.'),
 ('plans','Conception des plans','Conception et préparation des plans pour vous aider à visualiser et organiser votre projet.'),
 ('btp','Travaux BTP','Réalisation de travaux de construction et d’ouvrages dans le bâtiment et les travaux publics.'),
 ('plumb','Plomberie & installation sanitaire','Installation et travaux de plomberie, équipements sanitaires et réseaux d’eau.'),
 ('elec','Électricité bâtiment & transport électrique','Installations électriques pour bâtiments et solutions liées au transport électrique.'),
 ('cctv','Caméras de surveillance','Installation de systèmes de vidéosurveillance pour renforcer la sécurité de vos espaces.'),
]
TRUST = [('clip','Étude & conseil','Un projet bien défini dès le départ'),('layers','Travaux multi-services','Gros œuvre, réseaux, sécurité'),
         ('route','Suivi du projet','Des fondations aux finitions'),('puzzle','Solutions adaptées','Selon votre besoin et votre budget')]
STEPS = [('p15','01','Fondations','Implantation, fouilles et semelles en béton armé : la base durable de l’ouvrage.'),
         ('p22','02','Élévation des murs','Poteaux, chaînages et maçonnerie en parpaings, à l’aplomb et au niveau.'),
         ('p11','03','Dalle & plancher','Coffrage, poutrelles et hourdis pour des planchers solides.'),
         ('p19','04','Charpente & toiture','Charpente bois et couverture posées par nos équipes.'),
         ('p26','05','Finitions','Carrelage, enduits, peinture et installations techniques.')]
GALLERY = [('p07','feat','livre','Maison à étage — R+1','Gros œuvre achevé'),
           ('p10','','livre','Villa de plain-pied','Toiture posée'),
           ('p12','tall','livre','Villa à arcades','Réalisation'),
           ('p05','','charpente','Charpente sur grande villa','Charpente & toiture'),
           ('p11','wide','gros','Plancher poutrelles-hourdis','Gros œuvre'),
           ('p16','','finitions','Finitions intérieures','Finitions'),
           ('p03','','livre','Villa à colonnes','Réalisation'),
           ('p26','','finitions','Pose de carrelage','Finitions')]

def services_html():
    cards = ''.join(f'''
      <article class="card" data-reveal>
        <span class="num">0{i+1}</span>
        <div class="ic">{icon(ic)}</div>
        <h3>{t}</h3><p>{d}</p>
        <a class="link-arrow" href="contact.html">Demander un devis {icon('arrow')}</a>
      </article>''' for i,(ic,t,d) in enumerate(SERVICES))
    return f'''
<section class="section services" id="services">
  <div class="container">
    <div class="sec-head">
      <div><span class="eyebrow" data-reveal>Nos services</span>
      <h2 class="h2" data-reveal style="--delay:80ms">Six métiers, un seul interlocuteur pour votre projet.</h2></div>
      <p class="lead" data-reveal style="--delay:160ms">Du premier conseil à la mise en service, nous coordonnons les études, le gros œuvre et les installations techniques.</p>
    </div>
    <div class="grid-3" data-stagger="90">{cards}</div>
  </div>
</section>'''

def gallery_html(limit=None, filters=True):
    items = GALLERY if limit is None else GALLERY[:limit]
    tiles = ''.join(f'''
      <figure class="tile {cls}" data-cat="{cat}" data-reveal tabindex="0">
        <img src="assets/img/{p}.jpg" alt="{t} — chantier ETS Les Jeunes Bâtisseurs" loading="lazy">
        <figcaption class="cap"><small>{tag}</small><b>{t}</b></figcaption>
        <span class="zoom">{icon('zoom')}</span>
      </figure>''' for p,cls,cat,t,tag in items)
    chips = '''<div class="filters" role="tablist" data-reveal>
        <button class="chip active" data-filter="all">Tous</button><button class="chip" data-filter="livre">Réalisations</button>
        <button class="chip" data-filter="gros">Gros œuvre</button><button class="chip" data-filter="charpente">Charpente</button>
        <button class="chip" data-filter="finitions">Finitions</button></div>''' if filters else ''
    return f'<div class="gallery" data-stagger="70">{tiles}</div>', chips

LIGHTBOX = f'''<div class="lightbox" role="dialog" aria-label="Visionneuse"><div><img src="" alt=""><p class="lb-cap"></p></div>
<button class="lb-close" aria-label="Fermer">{icon('close')}</button><button class="lb-prev" aria-label="Précédent">{icon('chev-l')}</button><button class="lb-next" aria-label="Suivant">{icon('chev-r')}</button></div>'''

def cta_html():
    return f'''
<section class="section cta" id="contact">
  <div class="cta__bg"><img src="assets/img/p20.jpg" alt="" data-parallax="30"></div>
  <div class="container">
    <div>
      <span class="eyebrow" data-reveal>Contact</span>
      <h2 data-reveal style="--delay:80ms">Un projet en tête ?<br><em>Parlons-en.</em></h2>
      <p class="lead" data-reveal style="--delay:160ms">Décrivez-nous votre besoin : nous vous rappelons pour en discuter et préparer un devis adapté.</p>
      <div class="hero__ctas" data-reveal style="--delay:240ms"><a class="btn" style="opacity:1;animation:none" href="contact.html">Demander un devis {icon('arrow','arrow')}</a></div>
    </div>
    <div class="contact-box" data-reveal="fade" style="--delay:200ms">
      <div class="row"><span class="ic">{icon('phone')}</span><div><small>Téléphone</small><b>{PHONE1}</b></div></div>
      <div class="row"><span class="ic">{icon('phone')}</span><div><small>Téléphone</small><b>{PHONE2}</b></div></div>
      <div class="btns"><a class="btn btn--ghost-light" href="{TEL1}">{icon('phone','arrow')} Appeler</a><a class="btn btn--wa" href="{WA}">{icon('wa','arrow')} WhatsApp</a></div>
    </div>
  </div>
</section>'''

home = f'''
<section class="hero">
  <div class="hero__media"><img src="assets/img/p10.jpg" alt="Villa réalisée par ETS Les Jeunes Bâtisseurs" fetchpriority="high"></div>
  <div class="container hero__content">
    <span class="eyebrow">Conceptions &amp; Réalisations</span>
    <h1><span class="line"><span>Nous concevons.</span></span><span class="line"><span>Nous bâtissons.</span></span><span class="line"><span><em>Durablement.</em></span></span></h1>
    <p class="lead">Études, plans, travaux BTP, plomberie, électricité et vidéosurveillance : votre projet suivi de la première idée jusqu’aux finitions.</p>
    <div class="hero__ctas">
      <a class="btn" href="#services">Découvrir nos services {icon('arrow','arrow')}</a>
      <a class="btn btn--ghost-light" href="contact.html">Nous contacter</a>
    </div>
  </div>
  <div class="hero__meta"><b>Yaoundé · Cameroun</b><span>Construction &amp; services techniques</span></div>
  <a class="scroll-cue" href="#services" aria-label="Défiler vers la suite"><i></i>Défiler</a>
</section>

<section class="trust" aria-label="Nos engagements"><div class="container"><ul data-stagger="80">
{''.join(f'<li data-reveal><span class="ic">{icon(i)}</span><span><b>{t}</b><small>{s}</small></span></li>' for i,t,s in TRUST)}
</ul></div></section>

{services_html()}

<section class="section about" id="apropos">
  <div class="container split">
    <div>
      <span class="eyebrow" data-reveal>À propos</span>
      <h2 class="h2" data-reveal style="--delay:80ms">Une équipe de jeunes bâtisseurs, sur le terrain.</h2>
      <p data-reveal style="--delay:140ms">ETS Les Jeunes Bâtisseurs accompagne particuliers et entreprises dans la conception et la réalisation de leurs projets de construction et d’installations techniques.</p>
      <p class="mission" data-reveal style="--delay:200ms">« Construire des ouvrages solides et des installations fiables, avec rigueur, écoute et transparence. »</p>
      <ul class="checks" data-stagger="70">
        {''.join(f'<li data-reveal>{icon("check-c")} {x}</li>' for x in ['Équipe présente sur chaque chantier','Conseil avant les travaux','Suivi de l’étude aux finitions','Tenue de sécurité sur site'])}
      </ul>
      <a class="btn btn--ghost-dark" href="#methode" data-reveal>Découvrir notre méthode {icon('arrow','arrow')}</a>
    </div>
    <div class="media-stack" data-reveal="fade">
      <div class="main" data-reveal="mask"><img src="assets/img/p32.jpg" alt="L’équipe ETS Les Jeunes Bâtisseurs sur un chantier" data-parallax="24"></div>
      <div class="inset"><img src="assets/img/p29.jpg" alt="Membres de l’équipe en tenue de chantier"></div>
      <div class="tag"><b>Sur le terrain</b>Nos équipes en tenue<br>de sécurité</div>
    </div>
  </div>
</section>

<section class="process" id="methode">
  <div class="process__pin">
    <div class="container process__head">
      <div><span class="eyebrow">Notre méthode</span><h2 class="h2" style="margin-top:18px">De la fondation à la finition.</h2></div>
      <p class="lead">Chaque chantier suit des étapes claires, documentées en photos et partagées avec vous.</p>
    </div>
    <div class="process__track">
      {''.join(f'<article class="step"><figure><img src="assets/img/{p}.jpg" alt="{t}" loading="lazy"><figcaption>ÉTAPE {n}</figcaption></figure><h3>{t}</h3><p>{d}</p></article>' for p,n,t,d in STEPS)}
    </div>
    <div class="container"><div class="process__bar"><i></i></div></div>
  </div>
</section>

<section class="section projects" id="realisations">
  <div class="container">
    <div class="sec-head">
      <div><span class="eyebrow" data-reveal>Réalisations</span><h2 class="h2" data-reveal style="--delay:80ms">Nos chantiers, en vraies images.</h2></div>
      <div style="display:flex;flex-direction:column;gap:20px;align-items:flex-start">{gallery_html()[1]}</div>
    </div>
    {gallery_html(7)[0]}
    <div style="margin-top:48px;text-align:center" data-reveal><a class="btn btn--ghost-dark" href="realisations.html">Voir toutes les réalisations {icon('arrow','arrow')}</a></div>
  </div>
</section>
{cta_html()}
{LIGHTBOX}'''

# ---------- Réalisations
ALL = [('p07','feat','livre','Maison à étage — R+1','Gros œuvre achevé'),('p10','','livre','Villa de plain-pied','Toiture posée'),
       ('p12','tall','livre','Villa à arcades','Réalisation'),('p03','','livre','Villa à colonnes','Réalisation'),
       ('p09','wide','charpente','Charpente — vue d’ensemble','Charpente & toiture'),('p05','','charpente','Fermes de charpente','Charpente & toiture'),
       ('p18','','charpente','Couverture en tôle','Charpente & toiture'),('p23','wide','charpente','Charpente en cours','Charpente & toiture'),
       ('p11','wide','gros','Plancher poutrelles-hourdis','Gros œuvre'),('p17','','gros','Hourdis en place','Gros œuvre'),
       ('p02','tall','gros','Coffrage de dalle','Gros œuvre'),('p01','','gros','Élévation et coffrages','Gros œuvre'),
       ('p06','wide','gros','Chantier R+1','Gros œuvre'),('p15','','gros','Semelles de fondation','Fondations'),('p13','','gros','Terrassement en pente','Fondations'),
       ('p21','wide','gros','Poteaux en béton armé','Gros œuvre'),('p04','','gros','Ferraillage en hauteur','Gros œuvre'),('p24','','gros','Poteaux et chaînages','Gros œuvre'),
       ('p27','','gros','Arcades en construction','Gros œuvre'),('p22','','gros','Élévation des poteaux','Gros œuvre'),
       ('p16','','finitions','Finitions intérieures','Finitions'),('p26','','finitions','Pose de carrelage','Finitions'),
       ('p08','','finitions','Carrelage marbré','Finitions'),('p25','','finitions','Plan de travail maçonné','Finitions')]
tiles = ''.join(f'''<figure class="tile {cls}" data-cat="{cat}" data-reveal tabindex="0"><img src="assets/img/{p}.jpg" alt="{t}" loading="lazy">
  <figcaption class="cap"><small>{tag}</small><b>{t}</b></figcaption><span class="zoom">{icon('zoom')}</span></figure>''' for p,cls,cat,t,tag in ALL)
real = f'''
<section class="page-hero"><div class="bg"><img src="assets/img/p31.jpg" alt=""></div><div class="container">
  <p class="crumbs"><a href="index.html">Accueil</a> / Réalisations</p>
  <h1>Nos réalisations</h1><p class="lead">Une sélection de chantiers en cours et d’ouvrages réalisés par nos équipes.</p></div></section>
<section class="section projects"><div class="container">
  <div style="margin-bottom:40px">{gallery_html()[1]}</div>
  <div class="gallery" data-stagger="60">{tiles}</div></div></section>
{cta_html()}{LIGHTBOX}'''

# ---------- Contact / devis
opts = ''.join(f'<option>{s[1]}</option>' for s in SERVICES)
contact = f'''
<section class="page-hero"><div class="bg"><img src="assets/img/p28.jpg" alt=""></div><div class="container">
  <p class="crumbs"><a href="index.html">Accueil</a> / Contact</p>
  <h1>Demander un devis</h1><p class="lead">Quelques informations suffisent : nous vous recontactons rapidement pour échanger sur votre projet.</p></div></section>
<section class="section" style="background:var(--warm)"><div class="container quote">
  <aside class="info-card" data-reveal>
    <span class="eyebrow">Contact direct</span>
    <h2 style="font-size:28px;margin:16px 0 8px">Préférez-vous appeler ?</h2>
    <p style="color:rgba(255,255,255,.7);margin-bottom:16px">Nos équipes répondent par téléphone et sur WhatsApp.</p>
    <div class="row">{icon('phone','')}<div><small style="opacity:.6">Téléphone</small><br><b style="font:700 20px var(--f-head)">{PHONE1}</b></div></div>
    <div class="row">{icon('phone','')}<div><small style="opacity:.6">Téléphone</small><br><b style="font:700 20px var(--f-head)">{PHONE2}</b></div></div>
    <div class="row">{icon('pin','')}<div><small style="opacity:.6">Zone d’intervention</small><br><b style="font:600 16px var(--f-head)">Yaoundé et environs</b></div></div>
    <div style="display:grid;gap:12px;margin-top:20px"><a class="btn btn--wa" href="{WA}" style="justify-content:center">{icon('wa','arrow')} Écrire sur WhatsApp</a></div>
  </aside>
  <form class="form" data-reveal style="--delay:120ms" novalidate>
    <h3>Votre projet</h3><p class="sub">Les champs marqués * sont obligatoires.</p>
    <div class="fgrid">
      <div class="field"><label for="nom">Nom complet *</label><input id="nom" required autocomplete="name" placeholder="Ex. Jean Mbarga"></div>
      <div class="field"><label for="tel">Téléphone *</label><input id="tel" type="tel" required autocomplete="tel" placeholder="6XX XXX XXX"></div>
      <div class="field"><label for="mail">E-mail <i>(facultatif)</i></label><input id="mail" type="email" autocomplete="email" placeholder="vous@exemple.com"></div>
      <div class="field"><label for="srv">Service souhaité *</label><select id="srv" required><option value="">Choisir un service</option>{opts}</select></div>
      <div class="field full"><label for="lieu">Lieu du projet *</label><input id="lieu" required placeholder="Quartier, ville"></div>
      <div class="field full"><label for="desc">Décrivez votre projet *</label><textarea id="desc" required placeholder="Type de travaux, surface, délais souhaités…"></textarea></div>
      <div class="field full"><label>Comment préférez-vous être contacté ?</label>
        <div class="radio-row"><label class="on"><input type="radio" name="pref" checked> Appel</label><label><input type="radio" name="pref"> WhatsApp</label><label><input type="radio" name="pref"> E-mail</label></div></div>
    </div>
    <div class="submit"><small>Vos informations servent uniquement à répondre à votre demande.</small><button class="btn" type="submit">Envoyer ma demande {icon('arrow','arrow')}</button></div>
    <div class="success" hidden><span class="chk">{icon('check')}</span>Merci ! Votre demande a bien été envoyée. Nous vous recontactons très vite.</div>
  </form>
</div></section>'''

pages = {
 'index.html': page('ETS Les Jeunes Bâtisseurs — Conceptions & Réalisations', 'Construction, travaux BTP, plans, plomberie, électricité et vidéosurveillance. Demandez votre devis.', home, 'Accueil'),
 'realisations.html': page('Réalisations — ETS Les Jeunes Bâtisseurs', 'Nos chantiers et ouvrages réalisés en photos.', real, 'Réalisations'),
 'contact.html': page('Demander un devis — ETS Les Jeunes Bâtisseurs', 'Contactez-nous par téléphone, WhatsApp ou formulaire pour votre projet.', contact, 'Contact'),
}
for n, html in pages.items():
    open(os.path.join(OUT, n), 'w').write(html)
print('ok')
