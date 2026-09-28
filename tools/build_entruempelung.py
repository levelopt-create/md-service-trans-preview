# -*- coding: utf-8 -*-
"""
Erzeugt den Bereich /entruempelung/ (Übersicht + 5 Leistungsseiten) im Design von MD Service Trans.

    python tools/build_entruempelung.py

Quellen: tools/entruempelung_content.py (Texte), tools/icons_sprite.html (Icons)
Ausgabe: entruempelung/*.html und sitemap.xml
"""
import datetime
import html
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "entruempelung"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import entruempelung_content as C  # noqa: E402

DOMAIN = C.DOMAIN
PHONE_DISPLAY, PHONE_TEL, WA, EMAIL = "0177 3188914", "+491773188914", "491773188914", "info@mdservicetrans.de"
FORM_URL = "../index.html?leistung=Entruempelung#kontakt"
SHORT = {
    "haushaltsaufloesung": "Haushaltsauflösung",
    "wohnungsaufloesung": "Wohnungsauflösung",
    "keller-dachboden-garage": "Keller & Dachboden",
    "vermuellte-wohnung": "Vermüllte Wohnung",
    "geschaeftsaufloesung": "Büro & Gewerbe",
}
SPRITE = (ROOT / "tools" / "icons_sprite.html").read_text(encoding="utf-8")


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def icon(name):
    return f'<svg class="icon" aria-hidden="true"><use href="#i-{name}"/></svg>'


# ------------------------------------------------------------------ fragments
def render_section(sec):
    k = sec["kind"]
    out = []
    if sec.get("h2"):
        out.append(f"<h2>{inline(sec['h2'])}</h2>")
    if k == "text":
        out += [f"<p>{inline(p)}</p>" for p in sec["paras"]]
    elif k == "bullets":
        out.append('<ul class="bullets">' + "".join(f"<li>{inline(i)}</li>" for i in sec["items"]) + "</ul>")
    elif k == "checklist":
        out.append('<ul class="check-list">' + "".join(f"<li>{icon('check')}<span>{inline(i)}</span></li>" for i in sec["items"]) + "</ul>")
    elif k == "steps":
        out.append('<ol class="timeline">' + "".join(f"<li><strong>{inline(t)}</strong><p>{inline(d)}</p></li>" for t, d in sec["items"]) + "</ol>")
    elif k == "callout":
        out.append('<aside class="callout" role="note">' + f"<h3>{inline(sec['title'])}</h3>" + "".join(f"<p>{inline(p)}</p>" for p in sec["paras"]) + "</aside>")
    elif k == "prices":
        out.append('<ul class="factor-list">' + "".join(f"<li><strong>{inline(a)}</strong><span>{inline(b)}</span></li>" for a, b in sec["items"]) + "</ul>")
        if sec.get("after"):
            out.append(f"<p>{inline(sec['after'])}</p>")
    else:
        raise SystemExit(f"Unbekannter Abschnittstyp: {k}")
    return "\n".join(out)


def faq_html(items):
    return '<div class="faq">' + "".join(f"<details><summary>{esc(q)}</summary><p>{inline(a)}</p></details>" for q, a in items) + "</div>"


def strip_markup(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)


def faq_ld(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_markup(a)}} for q, a in items
        ],
    }


PROVIDER = {
    "@type": "LocalBusiness",
    "name": "MD Service Trans",
    "url": DOMAIN + "/",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "Jenaer Str. 13", "postalCode": "90491", "addressLocality": "Nürnberg", "addressCountry": "DE"},
}


def script_ld(graph):
    return '<script type="application/ld+json">\n' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2) + "\n</script>"


def chips():
    return '<div class="area-list">' + "".join(f'<span class="area-chip">{icon("pin")}{esc(r)}</span>' for r in C.REGIONS) + "</div>"


# ------------------------------------------------------------------ page shell
def header(current):
    def cur(name):
        return ' aria-current="page"' if current == name else ""

    sub = [("./", "Übersicht", "hub")] + [(s["slug"] + ".html", SHORT[s["slug"]], s["slug"]) for s in C.SERVICES]
    subnav = "".join(f'<a href="{href}"{cur(key)}>{label}</a>' for href, label, key in sub)
    return f"""{SPRITE}
<a class="skip-link" href="#main">Zum Inhalt springen</a>
<header class="site-header">
  <div class="container header-inner">
    <a href="../index.html" class="brand" aria-label="MD Service Trans — Startseite">
      <img src="../assets/brand/logo.png" alt="MD Service Trans Logo">
    </a>
    <nav class="main-nav" id="main-nav" aria-label="Hauptnavigation">
      <a href="../index.html#leistungen">Leistungen</a>
      <a href="./" class="nav-current">Entrümpelung</a>
      <a href="../index.html#warum-wir">Warum wir</a>
      <a href="../index.html#ablauf">Ablauf</a>
      <a href="../index.html#einsatzgebiet">Einsatzgebiet</a>
      <a href="../index.html#kontakt">Kontakt</a>
    </nav>
    <div class="header-cta">
      <a class="phone-link" href="tel:{PHONE_TEL}" aria-label="Anrufen: {PHONE_DISPLAY}">{icon('phone')}<span>{PHONE_DISPLAY}</span></a>
      <a class="btn btn-primary" href="{FORM_URL}">Kostenlose Anfrage</a>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Menü öffnen">{icon('menu')}</button>
    </div>
  </div>
</header>
<nav class="subnav" aria-label="Entrümpelung: Leistungen"><div class="container subnav-inner">{subnav}</div></nav>"""


def footer():
    links = "".join(f'<a href="{s["slug"]}.html">{esc(s["name"])}</a>' for s in C.SERVICES)
    return f"""<a class="whatsapp-fab" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Per WhatsApp kontaktieren">{icon('chat')}</a>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="../assets/brand/logo.png" alt="MD Service Trans Logo">
        <p>Umzüge, Möbeltransporte, Montage/Demontage und Entrümpelung in Nürnberg &amp; Franken. Inhaber: Maksym Davydiuk.</p>
      </div>
      <div class="footer-col">
        <h4>Entrümpelung</h4>
        {links}
      </div>
      <div class="footer-col">
        <h4>Unternehmen</h4>
        <a href="../index.html#leistungen">Alle Leistungen</a>
        <a href="../impressum.html">Impressum</a>
        <a href="../datenschutz.html">Datenschutz</a>
        <a href="../agb.html">AGB</a>
        <a href="../widerruf.html">Widerrufsbelehrung</a>
        <a href="#" data-cookie-settings>Cookie-Einstellungen</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 MD Service Trans — Maksym Davydiuk, Nürnberg</span>
      <span><a href="tel:{PHONE_TEL}">+49 177 3188914</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    </div>
  </div>
</footer>
<script src="entruempelung.js" defer></script>
<script src="../cookie-consent.js" defer></script>"""


def cta_band():
    return f"""<section class="section">
  <div class="container">
    <div class="cta-band">
      <div>
        <h2>Räumung geplant? Wir machen Ihnen ein klares Angebot.</h2>
        <p>Schildern Sie uns kurz Ihre Situation — am schnellsten per WhatsApp mit ein paar Fotos.</p>
      </div>
      <div class="cta-band-actions">
        <a class="btn btn-primary" href="{FORM_URL}">Angebot anfragen {icon('arrow')}</a>
        <a class="btn btn-secondary" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('chat')} WhatsApp</a>
      </div>
    </div>
  </div>
</section>"""


def page(filename, title, description, current, main, graph):
    canonical = DOMAIN + "/entruempelung/" + ("" if filename == "index.html" else filename)
    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{attr(title)}</title>
<meta name="description" content="{attr(description)}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0B3559">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="MD Service Trans">
<meta property="og:title" content="{attr(title)}">
<meta property="og:description" content="{attr(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/brand/favicon-512.png">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary">

<link rel="icon" type="image/png" sizes="32x32" href="../assets/brand/favicon-32.png">
<link rel="apple-touch-icon" href="../assets/brand/favicon-180.png">

<link rel="stylesheet" href="../assets/fonts/fonts.css">
<link rel="stylesheet" href="../styles.css">
<link rel="stylesheet" href="entruempelung.css">
{script_ld(graph)}
</head>
<body class="theme-green">
{header(current)}

<main id="main">
{main}
</main>

{footer()}
</body>
</html>
"""
    (OUT / filename).write_text(doc, encoding="utf-8")
    return canonical


def hero(crumbs, h1, lead):
    trail = "".join(
        (f'<a href="{href}">{esc(label)}</a><span aria-hidden="true">/</span>' if href else f'<span aria-current="page">{esc(label)}</span>')
        for href, label in crumbs
    )
    return f"""<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Brotkrumen">{trail}</nav>
    <span class="eyebrow">Entrümpelung · Nürnberg &amp; Franken</span>
    <h1>{esc(h1)}</h1>
    <p class="lead">{esc(lead)}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{FORM_URL}">Unverbindliches Angebot anfragen {icon('arrow')}</a>
      <a class="btn btn-secondary" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('chat')} Per WhatsApp anfragen</a>
    </div>
    <ul class="hero-points">
      <li>{icon('check')}Klares Angebot vor dem Start</li>
      <li>{icon('check')}Diskret &amp; respektvoll</li>
      <li>{icon('check')}Fachgerechte Entsorgung</li>
      <li>{icon('check')}Besenreine Übergabe</li>
    </ul>
  </div>
</section>"""


# ------------------------------------------------------------------ hub page
def build_hub():
    cards = "".join(
        f'<a class="ent-card" href="{s["slug"]}.html"><span class="ent-card-icon">{icon(s["icon"])}</span>'
        f'<h3>{esc(s["name"])}</h3><p>{esc(s["card"])}</p><span class="ent-card-more">Mehr erfahren {icon("arrow")}</span></a>'
        for s in C.SERVICES
    )
    diff = "".join(render_section(sec) for sec in C.HUB["sections"])
    steps = "".join(
        f'<li><span class="ent-step-icon">{icon(i)}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>'
        for i, t, d in [
            ("chat", "Anfrage", "Per Telefon, WhatsApp, E-Mail oder Formular — gern mit Fotos."),
            ("eye", "Einschätzung", "Wir sehen uns die Räume an oder schätzen anhand Ihrer Fotos ein."),
            ("file", "Angebot", "Sie erhalten Leistungsumfang und Preis, bevor Kosten entstehen."),
            ("truck", "Räumung", "Wir räumen zum vereinbarten Termin und entsorgen fachgerecht."),
            ("check", "Übergabe", "Besenreine Übergabe der geräumten Räume."),
        ]
    )
    factors = "".join(f"<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>" for a, b in C.PRICE_FACTORS)
    audience = "".join(f"<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>" for a, b in C.HUB["audience"])

    main = f"""{hero([("../index.html", "Start"), (None, "Entrümpelung")], C.HUB["h1"], C.HUB["intro"])}

<section class="section" id="leistungen">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Leistungen</span>
      <h2>Was wir für Sie räumen</h2>
      <p>Vom Kellerabteil bis zur kompletten Haushaltsauflösung — wählen Sie Ihren Fall.</p>
    </div>
    <div class="ent-cards">{cards}</div>
  </div>
</section>

<section class="section section-alt" id="unterschied">
  <div class="container prose prose-center">
    {diff}
  </div>
</section>

<section class="section" id="ablauf">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Ablauf</span>
      <h2>In fünf Schritten zur geräumten Wohnung</h2>
    </div>
    <ol class="ent-steps">{steps}</ol>
  </div>
</section>

<section class="section section-alt" id="preise">
  <div class="container two-col">
    <div class="prose">
      <span class="kicker">Preise</span>
      <h2>Was beeinflusst den Preis einer Entrümpelung?</h2>
      <p>Einen verbindlichen Preis nennen wir Ihnen erst, wenn wir die Räume kennen — bei einer Besichtigung oder anhand Ihrer Fotos. Diese Faktoren spielen die größte Rolle:</p>
      <a class="btn btn-primary" href="{FORM_URL}">Angebot anfragen {icon('arrow')}</a>
    </div>
    <ul class="factor-list">{factors}</ul>
  </div>
</section>

<section class="section" id="fuer-wen">
  <div class="container two-col">
    <div class="prose">
      <span class="kicker">Zielgruppen</span>
      <h2>{esc(C.HUB["audience_h2"])}</h2>
      <p>Ob privat oder gewerblich — wir stimmen uns mit allen Beteiligten ab, die für die Räumung zuständig sind.</p>
    </div>
    <ul class="factor-list">{audience}</ul>
  </div>
</section>

<section class="section section-alt" id="faq">
  <div class="container prose prose-center">
    <div class="section-head">
      <span class="kicker">Häufige Fragen</span>
      <h2>Antworten auf die wichtigsten Fragen</h2>
    </div>
    {faq_html(C.HUB["faq"])}
  </div>
</section>

<section class="section" id="regionen">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Regionen</span>
      <h2>Im Einsatz in Nürnberg &amp; Franken</h2>
      <p>Ihr Ort fehlt? Fragen Sie einfach an.</p>
    </div>
    {chips()}
  </div>
</section>

{cta_band()}"""

    graph = [
        {**PROVIDER},
        {
            "@type": "Service",
            "name": "Entrümpelung & Haushaltsauflösung",
            "serviceType": "Entrümpelung, Haushaltsauflösung, Wohnungsräumung",
            "provider": {"@type": "LocalBusiness", "name": "MD Service Trans", "url": DOMAIN + "/"},
            "areaServed": C.REGIONS,
            "description": C.HUB["intro"],
            "url": DOMAIN + "/entruempelung/",
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Start", "item": DOMAIN + "/"},
                {"@type": "ListItem", "position": 2, "name": "Entrümpelung", "item": DOMAIN + "/entruempelung/"},
            ],
        },
        faq_ld(C.HUB["faq"]),
    ]
    return page("index.html", C.HUB["title"], C.HUB["description"], "hub", main, graph)


# ------------------------------------------------------------------ service pages
def build_service(s):
    others = "".join(
        f'<li><a href="{o["slug"]}.html">{icon(o["icon"])}{esc(o["name"])}</a></li>' for o in C.SERVICES if o["slug"] != s["slug"]
    )
    includes = "".join(f"<li>{icon('check')}<span>{inline(i)}</span></li>" for i in s["includes"])
    when = "".join(f"<li>{inline(i)}</li>" for i in s["when"])
    extra = "\n".join(render_section(sec) for sec in s.get("sections", []))
    url = DOMAIN + "/entruempelung/" + s["slug"] + ".html"

    main = f"""{hero([("../index.html", "Start"), ("./", "Entrümpelung"), (None, s["name"])], s["h1"], s["intro"])}

<section class="section">
  <div class="container detail-grid">
    <article class="prose">
      <h2>Das übernehmen wir</h2>
      <ul class="check-list">{includes}</ul>

      <h2>Wann diese Leistung sinnvoll ist</h2>
      <ul class="bullets">{when}</ul>

      {extra}

      <h2>Häufige Fragen</h2>
      {faq_html(s["faq"])}

      <h2>Im Einsatz in Nürnberg &amp; ganz Franken</h2>
      <p>Wir räumen in Nürnberg, Fürth, Erlangen, Würzburg, Schweinfurt, Bamberg, Bayreuth, Ansbach und Umgebung. Ihr Ort fehlt? Fragen Sie einfach an.</p>
    </article>

    <aside class="detail-aside" aria-label="Kontakt">
      <div class="aside-card">
        <h2>Angebot anfragen</h2>
        <p>Wir melden uns zeitnah bei Ihnen.</p>
        <a class="btn btn-primary btn-block" href="{FORM_URL}">Zum Anfrageformular {icon('arrow')}</a>
        <a class="btn btn-whatsapp btn-block" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('chat')} WhatsApp</a>
        <a class="btn btn-outline-navy btn-block" href="tel:{PHONE_TEL}">{icon('phone')} {PHONE_DISPLAY}</a>
        <a class="btn btn-outline-navy btn-block" href="mailto:{EMAIL}">{icon('mail')} E-Mail</a>
      </div>
      <div class="aside-card aside-card-soft">
        <h3>Weitere Leistungen</h3>
        <ul class="aside-links">{others}</ul>
      </div>
    </aside>
  </div>
</section>

{cta_band()}"""

    graph = [
        {**PROVIDER},
        {
            "@type": "Service",
            "name": s["h1"],
            "serviceType": s["name"],
            "provider": {"@type": "LocalBusiness", "name": "MD Service Trans", "url": DOMAIN + "/"},
            "areaServed": C.REGIONS,
            "description": s["intro"],
            "url": url,
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Start", "item": DOMAIN + "/"},
                {"@type": "ListItem", "position": 2, "name": "Entrümpelung", "item": DOMAIN + "/entruempelung/"},
                {"@type": "ListItem", "position": 3, "name": s["name"], "item": url},
            ],
        },
        faq_ld(s["faq"]),
    ]
    return page(s["slug"] + ".html", s["title"], s["description"], s["slug"], main, graph)


# ------------------------------------------------------------------ run
OUT.mkdir(exist_ok=True)
urls = [DOMAIN + "/", build_hub()] + [build_service(s) for s in C.SERVICES]

today = datetime.date.today().isoformat()
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n" for u in urls
) + "</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")

print(f"OK: {len(urls) - 1} Seiten in {OUT} und sitemap.xml mit {len(urls)} URLs geschrieben.")
