#!/usr/bin/env python3
"""Statischer Generator für den NNL-Demonstrator (PROGRESSIVE digital)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
STAND = "07.10.2026"

SUCH = [
    {"u": "index.html", "t": "Startseite Willkommen", "k": "aktuelles start heide"},
    {"u": "wildnisgebiet.html", "t": "Wildnisgebiet Königsbrücker Heide", "k": "steckbrief schutzstatus ffh natura iucn geschichte betretungsverbot"},
    {"u": "karte.html", "t": "Besucherpfade und interaktive Karte", "k": "karte pfade biberpfad turmpfad haselberg zochau aussichtsturm gohrischheide"},
    {"u": "veranstaltungen.html", "t": "Veranstaltungen und Führungen", "k": "termine führung wanderung jahresprogramm busführung"},
    {"u": "leichte-sprache.html", "t": "Leichte Sprache", "k": "einfach leicht"},
    {"u": "en/index.html", "t": "English", "k": "english wilderness"},
    {"u": "hinweise.html", "t": "Über diesen Demonstrator", "k": "impressum hinweis schrift bildnachweis lizenz"},
]

ICON_SUCHE = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="10" r="6.5" fill="none" stroke="#003c32" stroke-width="2.5"/><path d="M15 15l6 6" stroke="#003c32" stroke-width="2.5" stroke-linecap="round"/></svg>'
FORST = '<svg viewBox="0 0 22 26" aria-hidden="true"><path d="M2 2h18v12c0 6-5 9-9 11C7 23 2 20 2 14Z" fill="none" stroke="#fff" stroke-width="2"/><path d="M11 6l-4 6h2.5l-3 4.5h9l-3-4.5H15Z" fill="#fff"/><path d="M10 16.5h2V20h-2z" fill="#fff"/></svg>'
# Kreis-Signets in NNL-Systematik (Platzhalter für die Logos Wildnisgebiet/NSG – Originaldateien liefert der AG)
SIGNET_WG = '<svg viewBox="0 0 64 64" role="img" aria-label="Logo-Position Wildnisgebiet Königsbrücker Heide (Platzhalter)"><circle cx="32" cy="32" r="31" fill="#a3c95c"/><circle cx="32" cy="32" r="24" fill="#0098ac"/><circle cx="32" cy="32" r="11" fill="#fcec45"/></svg>'
SIGNET_NSG = '<svg viewBox="0 0 64 64" role="img" aria-label="Logo-Position NSG Gohrischheide und Elbniederterrasse Zeithain (Platzhalter)"><circle cx="32" cy="32" r="31" fill="#fff"/><circle cx="32" cy="32" r="26" fill="#0b5546"/><path d="M14 40c6-8 12-10 18-6s12 2 18-6" stroke="#fcec45" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M26 22l6-8 6 8h-3l4 6H25l4-6Z" fill="#a3c95c"/></svg>'
FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4 1.7-4 4.3V10H7v4h3v8h4v-8h3l1-4h-4V8.6c0-.4.3-.6.6-.6Z"/></svg>'
IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4Zm0 2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2Zm5 3.5a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7Zm0 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM17.2 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"/></svg>'

T = {
 "de": dict(skip="Zum Inhalt springen", demo="Demonstrator", demotext="Gestaltungsmuster von PROGRESSIVE digital für die Vergabe 2026-VG-NG17-0001 – keine offizielle Website der NSG-Verwaltung.",
            mehr="Mehr zum Demonstrator", karte="Karte", aktuelles="Aktuelles", kontakt="Kontakt", suche="Suche", such_ph="Ich suche …",
            schrift_gr="Schrift vergrößern", schrift_kl="Schrift verkleinern", kontrast="Kontrast erhöhen", vorlesen="Seite vorlesen",
            menu="Menü", nav=["Entdecken","Besuchen","Leichte Sprache","Veranstaltungen"],
            warn_t="Waldbrandgefahrenstufe", warn_badge="Musteranzeige", warn="Statisches Warnbanner für Waldbrandstufe und Sperrungen. Hier keine aktuelle Warnung, nur Darstellungsbeispiel.",
            warn_link="Verhalten im Gebiet", name="Wildnisgebiet<br>Königsbrücker Heide<br><span style='font-weight:400'>NSG Gohrischheide</span>"),
 "en": dict(skip="Skip to content", demo="Demonstrator", demotext="Design sample by PROGRESSIVE digital for tender 2026-VG-NG17-0001 – not an official website of the reserve administration.",
            mehr="About this demonstrator", karte="Map", aktuelles="News", kontakt="Contact", suche="Search", such_ph="Search …",
            schrift_gr="Increase text size", schrift_kl="Decrease text size", kontrast="High contrast", vorlesen="Read page aloud",
            menu="Menu", nav=["Discover","Visit","Learn","Events"],
            warn_t="Forest fire danger level", warn_badge="Sample display", warn="Static banner for forest fire level and closures. No current warning – display example only.",
            warn_link="Rules on site", name="Königsbrück Heath<br>Wilderness Area<br><span style='font-weight:400'>Gohrischheide Reserve</span>"),
}

def layout(path, title, body, lang="de", active=None, desc="", extra_head="", extra_js=""):
    depth = path.count("/")
    b = "../" * depth
    t = T[lang]
    navlinks = [("wildnisgebiet.html", t["nav"][0]), ("karte.html", t["nav"][1]), ("leichte-sprache.html", t["nav"][2]), ("veranstaltungen.html", t["nav"][3])]
    if lang == "en":
        navlinks = [("en/index.html#discover", t["nav"][0]), ("en/index.html#visit", t["nav"][1]), ("en/index.html#learn", t["nav"][2]), ("veranstaltungen.html", t["nav"][3])]
    nav = "".join(f'<li><a href="{b}{u}"{" aria-current=\"page\"" if active==u else ""}>{n}</a></li>' for u, n in navlinks)
    de_url = b + ("index.html" if lang == "en" else path)
    en_url = b + "en/index.html"
    ls_url = b + "leichte-sprache.html"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – NNL-Demonstrator</title>
<meta name="description" content="{desc or title}">
<meta name="robots" content="noindex, nofollow">
<meta name="author" content="PROGRESSIVE digital – Kock, Rietz GbR">
<link rel="preload" href="{b}fonts/ahn-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{b}fonts/ahn-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{b}css/nnl.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='31' fill='%23a3c95c'/%3E%3Ccircle cx='32' cy='32' r='24' fill='%230098ac'/%3E%3Ccircle cx='32' cy='32' r='11' fill='%23fcec45'/%3E%3C/svg%3E">
{extra_head}
</head>
<body>
<a class="skip" href="#inhalt">{t['skip']}</a>
<div class="demo-hinweis" role="note"><div class="wrap"><strong>{t['demo']}</strong><span>{t['demotext']}</span><a href="{b}hinweise.html">{t['mehr']}</a></div></div>
<header class="kopf">
  <div class="wrap kopf__oben">
    <a class="forst" href="{b}hinweise.html#logos" aria-label="Logo-Position Staatsbetrieb Sachsenforst (Platzhalter)">{FORST}<span>Sachsenforst</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="hauptnav">{t['menu']} <span aria-hidden="true">☰</span></button>
    <div class="kopf__service">
      <a href="{b}karte.html">{t['karte']}</a>
      <a href="{b}{'en/' if lang=='en' else ''}index.html#aktuelles">{t['aktuelles']}</a>
      <a href="{b}{'en/' if lang=='en' else ''}index.html#kontakt">{t['kontakt']}</a>
      <div><form class="suche" role="search" data-base="{b}"><label class="visually-hidden" for="q-{lang}">{t['suche']}</label><input id="q-{lang}" name="q" type="search" placeholder="{t['such_ph']}"><button type="submit" aria-label="{t['suche']}">{ICON_SUCHE}</button></form><span class="suche-meldung visually-hidden" role="status" aria-live="polite"></span></div>
      <div class="a11y" role="group" aria-label="Barrierefreiheit">
        <button type="button" data-a11y="minus" aria-label="{t['schrift_kl']}" title="{t['schrift_kl']}">A−</button>
        <button type="button" data-a11y="plus" aria-label="{t['schrift_gr']}" title="{t['schrift_gr']}">A+</button>
        <button type="button" data-a11y="kontrast" aria-pressed="false" aria-label="{t['kontrast']}" title="{t['kontrast']}">◐</button>
        <button type="button" data-a11y="vorlesen" aria-pressed="false" aria-label="{t['vorlesen']}" title="{t['vorlesen']}">🔊</button>
      </div>
      <div class="social"><a href="https://www.facebook.com/" aria-label="Facebook (externer Link)">{FB}</a><a href="https://www.instagram.com/" aria-label="Instagram (externer Link)">{IG}</a></div>
      <nav class="sprachen" aria-label="Sprache"><a href="{de_url}" lang="de" {'aria-current="true"' if lang=='de' and active!='leichte-sprache.html' else ''}>DE</a><span aria-hidden="true">•</span><a href="{en_url}" lang="en" {'aria-current="true"' if lang=='en' else ''}>EN</a><span aria-hidden="true">•</span><a href="{ls_url}" {'aria-current="true"' if active=='leichte-sprache.html' else ''} title="Leichte Sprache">LS</a></nav>
    </div>
  </div>
  <div class="wrap kopf__haupt">
    <nav class="nav" id="hauptnav" aria-label="Hauptnavigation"><ul>{nav}</ul></nav>
    <a class="marke" href="{b}{'en/' if lang=='en' else ''}index.html" aria-label="Startseite"><span class="marke__name">{t['name']}</span><span class="marke__logos">{SIGNET_WG}{SIGNET_NSG}</span></a>
  </div>
</header>
<div class="warnung" role="region" aria-label="{t['warn_t']}"><div class="wrap">
  <span class="warnung__stufe"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 1 21h22Z" fill="#003c32"/><path d="M11 9h2v6h-2zm0 8h2v2h-2z" fill="#ffc842"/></svg>{t['warn_t']}: <span class="badge">{t['warn_badge']}</span></span>
  <span class="warnung__text">{t['warn']}</span>
  <a href="{b}wildnisgebiet.html#betretung">{t['warn_link']}</a>
</div></div>
{body}
{footer(b, lang)}
<script>window.NNL_SUCHINDEX={json.dumps(SUCH, ensure_ascii=False)};</script>
<script src="{b}js/nnl.js" defer></script>
{extra_js}
</body>
</html>
"""

def footer(b, lang):
    en = lang == "en"
    return f"""<footer class="fuss" id="kontakt">
  <div class="wrap fuss__grid">
    <div>
      <h2>{'Contact' if en else 'Kontakt'}</h2>
      <p>{'Reserve administration Königsbrücker Heide / Gohrischheide and Elbniederterrasse Zeithain' if en else 'Naturschutzgebietsverwaltung Königsbrücker Heide / Gohrischheide und Elbniederterrasse Zeithain'}<br>
      <span class="platzhalter">{'Address, phone, e-mail: placeholder' if en else 'Anschrift, Telefon, E-Mail: Platzhalter'}</span></p>
      <p>{'Contacts: Mail room · Area development · Operational services · Public relations' if en else 'Ansprechpersonen: Poststelle · Gebietsentwicklung · Betriebliche Dienstleistungen · Öffentlichkeitsarbeit'}</p>
    </div>
    <div>
      <h2>{'Explore' if en else 'Entdecken'}</h2>
      <ul>
        <li><a href="{b}wildnisgebiet.html">Wildnisgebiet Königsbrücker Heide</a></li>
        <li><a href="{b}karte.html">{'Trails &amp; map' if en else 'Besucherpfade &amp; Karte'}</a></li>
        <li><a href="{b}veranstaltungen.html">{'Events' if en else 'Veranstaltungen'}</a></li>
        <li><a href="{b}leichte-sprache.html">Leichte Sprache</a></li>
        <li><a href="{b}en/index.html">English</a></li>
      </ul>
    </div>
    <div>
      <h2>Service</h2>
      <ul>
        <li><a href="{b}hinweise.html">{'About this demonstrator' if en else 'Über diesen Demonstrator'}</a></li>
        <li><a href="{b}hinweise.html#impressum">Impressum</a></li>
        <li><a href="{b}hinweise.html#datenschutz">{'Privacy' if en else 'Datenschutz'}</a></li>
        <li><a href="{b}hinweise.html#barrierefreiheit">{'Accessibility' if en else 'Barrierefreiheit'}</a></li>
      </ul>
    </div>
    <div>
      <h2>{'Part of' if en else 'Teil der'}</h2>
      <a class="nnl-dach" href="https://nationale-naturlandschaften.de/" aria-label="Nationale Naturlandschaften (externer Link)"><img src="{b}img/nnl-dachmarke.svg" alt="Nationale Naturlandschaften" width="220" height="55"></a>
    </div>
  </div>
  <div class="wrap fuss__unten">
    <span>NNL-Demonstrator · PROGRESSIVE digital – Kock, Rietz GbR · {'created for tender' if en else 'erstellt für Vergabe'} 2026-VG-NG17-0001 · {'Status' if en else 'Stand'} {STAND}</span>
    <span>{'Map data' if en else 'Kartendaten'} © OpenStreetMap-Mitwirkende · {'Photos' if en else 'Fotos'}: Wikimedia Commons (CC BY-SA)</span>
  </div>
</footer>"""

def write(path, html):
    p = os.path.join(HERE, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)

# ---------- Startseite ----------
def termin(tag, mon, titel, text, ort, gebiet, base=""):
    return f"""<li class="termin" data-gebiet="{gebiet}"><div class="datum" aria-hidden="true"><b>{tag}</b><span>{mon}</span></div>
<div><h3>{titel}</h3><p>{text}</p><span class="tag">{ort}</span><span class="platzhalter">Beispieltermin</span></div></li>"""

start = f"""
<main id="inhalt">
<section class="hero" aria-label="Titelbild">
  <div class="hero__bild"><img src="img/hero-heide.jpg" srcset="img/hero-heide-800.jpg 800w, img/hero-heide.jpg 1600w" sizes="100vw" alt="Blühende Heide mit jungen Kiefern in der Königsbrücker Heide" width="1600" height="1067" fetchpriority="high"></div>
  <span class="hero__credit">Foto: Sonnentau25, CC BY-SA 4.0</span>
  <div class="blase">
    <h2>Wo Natur wieder Natur sein kann</h2>
    <p>Rund 7.000 Hektar ehemaliger Truppenübungsplatz entwickeln sich ohne menschliche Eingriffe.</p>
    <a class="pfeil" href="wildnisgebiet.html">Das Wildnisgebiet entdecken</a>
  </div>
</section>

<section class="willkommen" aria-labelledby="willkommen-titel">
  <div class="wrap">
    <h1 id="willkommen-titel">Willkommen in der Königsbrücker Heide und der Gohrischheide</h1>
    <div class="willkommen__grid">
      <ul class="pillen" aria-label="Schnelleinstieg">
        <li><a class="pille" href="karte.html">Gebiete auf der Karte ansehen</a></li>
        <li><a class="pille" href="veranstaltungen.html">Führungen &amp; Veranstaltungen</a></li>
        <li><a class="pille" href="wildnisgebiet.html#betretung">Betretungsregeln</a></li>
        <li><a class="pille" href="downloads/muster-faltblatt-biberpfad.pdf">Faltblätter zum Download</a></li>
        <li><a class="pille" href="leichte-sprache.html">Leichte Sprache</a></li>
      </ul>
      <div>
        <p class="lead">Nördlich von Königsbrück liegt eines der größten Naturschutzgebiete Sachsens. Wo fast ein Jahrhundert lang militärisch geübt wurde, darf sich die Landschaft heute frei entwickeln. Offene Heideflächen, lichte Kiefernwälder und Feuchtgebiete bieten Lebensraum für seltene Arten.</p>
        <p>An der Elbe bei Zeithain schützt das Naturschutzgebiet Gohrischheide und Elbniederterrasse Zeithain trockene Heiden und Sandflächen. Die Naturschutzgebietsverwaltung betreut beide Gebiete, legt Besucherpfade an und bietet Führungen, Umweltbildung und Forschung.</p>
        <p>Große Teile der Gebiete dürfen nicht betreten werden. Besucherpfade, Aussichtstürme und geführte Wanderungen ermöglichen dennoch spannende Einblicke in die Wildnis.</p>
        <a class="btn btn--gruen" href="wildnisgebiet.html">Mehr über das Wildnisgebiet</a>
      </div>
    </div>
  </div>
</section>

<section class="teaser" aria-label="Themen">
  <div class="wrap teaser__grid">
    <article class="karte">
      <img src="img/heideweg-800.jpg" alt="Sandweg durch lichten Kiefern- und Birkenwald" width="800" height="533">
      <h3>Entdecken</h3>
      <p>Steckbriefe, Schutzstatus und Geschichte der beiden Schutzgebiete – von Natura 2000 bis zum Prozessschutz.</p>
      <ul class="links"><li><a href="wildnisgebiet.html">Wildnisgebiet Königsbrücker Heide</a></li><li><a href="wildnisgebiet.html#gohrischheide">Gohrischheide &amp; Elbniederterrasse</a></li><li><a href="wildnisgebiet.html#faq">Häufige Fragen</a></li></ul>
      <p class="bildnachweis">Foto: Bybbisch94, CC BY-SA 4.0</p>
    </article>
    <article class="karte">
      <img src="img/turm-800.jpg" alt="Hochsitz am Rand einer Lichtung" width="800" height="450">
      <h3>Besuchen</h3>
      <p>Besucherpfade, Aussichtstürme und Radrundwege – mit interaktiver Karte und Faltblättern zum Mitnehmen.</p>
      <ul class="links"><li><a href="karte.html">Besucherpfade &amp; Karte</a></li><li><a href="karte.html#ausflugsziele">Ausflugsziele</a></li><li><a href="veranstaltungen.html">Veranstaltungen</a></li></ul>
      <p class="bildnachweis">Foto: Dr. Bernd Gross, CC BY-SA 3.0</p>
    </article>
    <article class="karte">
      <img src="img/wiedehopf-800.jpg" alt="Wiedehopf auf einem Ast in der Königsbrücker Heide" width="800" height="533">
      <h3>Verstehen</h3>
      <p>Forschung und Monitoring, Umweltbildung für Kitas und Schulen, Junior Ranger und Angebote für Kinder.</p>
      <ul class="links"><li><a href="wildnisgebiet.html#forschung">Forschung &amp; Monitoring</a></li><li><a href="veranstaltungen.html">Umweltbildung</a></li><li><a href="leichte-sprache.html">Leichte Sprache</a></li></ul>
      <p class="bildnachweis">Foto: Jonaskreische, CC BY-SA 4.0</p>
    </article>
  </div>
</section>

<section class="welle-sand" id="aktuelles" aria-labelledby="termine-titel">
  <div class="wrap">
    <h2 id="termine-titel">Veranstaltungen</h2>
    <p>Geführte Wanderungen, Busführungen und Angebote für Familien. Anmeldung über den Online-Shop.</p>
    <ul class="termine">
      {termin("17","Okt","Herbstwanderung am Biberpfad","Geführte Wanderung mit Naturführerin, ca. 3 Stunden.","Königsbrücker Heide","kh")}
      {termin("24","Okt","Busführung Königsbrücker Heide","Rundfahrt mit Halt an Aussichtspunkten im sonst gesperrten Gelände.","Königsbrücker Heide","kh")}
      {termin("07","Nov","Heidewanderung Gohrischheide","Wanderung zum Aussichtsturm mit Blick über die Heide.","Gohrischheide","gh")}
    </ul>
    <p style="margin-top:1.5rem"><a class="btn btn--gruen" href="veranstaltungen.html">Alle Veranstaltungen</a></p>
  </div>
</section>
</main>"""
write("index.html", layout("index.html", "Startseite", start, active=None, desc="NNL-Demonstrator: Startseite Wildnisgebiet Königsbrücker Heide und NSG Gohrischheide"))

# ---------- Inhaltsseite ----------
inhalt = """
<main id="inhalt">
<div class="seitenkopf"><div class="wrap">
  <nav class="brotkrumen" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li><a href="wildnisgebiet.html">Entdecken &amp; Informieren</a></li><li aria-current="page">Wildnisgebiet Königsbrücker Heide</li></ol></nav>
  <h1>Wildnisgebiet Königsbrücker Heide</h1>
</div></div>
<div class="wrap inhalt">
  <article>
    <p class="lead">Die Königsbrücker Heide liegt in der Westlausitz nördlich von Königsbrück. Mit rund 6.932 Hektar ist sie das größte zusammenhängende Naturschutzgebiet im Freistaat Sachsen.</p>
    <ul class="fakten" aria-label="Kennzahlen">
      <li><b>6.932 ha</b>Fläche des Naturschutzgebiets</li>
      <li><b>seit 1996</b>Naturschutzgebiet</li>
      <li><b>IUCN Ib</b>anerkanntes Wildnisgebiet</li>
    </ul>
    <h2 class="zwischen">Vom Truppenübungsplatz zur Wildnis</h2>
    <p>Ab 1906 entstand hier der Truppenübungsplatz Königsbrück, der bis 1992 bestand und zuletzt von der sowjetischen Armee genutzt wurde. Zehn Ortschaften wurden in dieser Zeit geräumt und abgetragen. Nach dem Abzug der Truppen nutzte der Freistaat Sachsen die Gelegenheit, hier ein Naturschutzgebiet mit einem neuartigen Schutzkonzept einzurichten: Auf dem größten Teil der Fläche läuft die Entwicklung ohne lenkende Eingriffe ab.</p>
    <figure>
      <img src="img/offenland.jpg" srcset="img/offenland-800.jpg 800w, img/offenland.jpg 1600w" sizes="(max-width:900px) 100vw, 800px" alt="Weite Heidelandschaft mit Birken am Horizont" width="1600" height="1067">
      <figcaption>Offenland mit Heide und aufkommenden Birken am Zochauer Heidepfad. Foto: Bybbisch94, CC BY-SA 4.0</figcaption>
    </figure>
    <h2 class="zwischen" id="betretung">Betreten nur auf ausgewiesenen Wegen</h2>
    <p>Wegen der langen militärischen Nutzung können im Boden noch Kampfmittelreste liegen. Große Teile des Gebiets dürfen deshalb nicht betreten werden. Gerade diese Ruhe ermöglicht eine nahezu ungestörte Entwicklung der Natur.</p>
    <div class="infobox infobox--warn" role="note">
      <h3>Wichtig für Ihren Besuch</h3>
      <p>Bleiben Sie auf den gekennzeichneten Besucherpfaden. Das Verlassen der Wege ist verboten und kann lebensgefährlich sein. Bei hoher Waldbrandgefahr können Pfade gesperrt werden; aktuelle Hinweise zeigt das Banner oben auf jeder Seite.</p>
    </div>
    <h2 class="zwischen">Schutzstatus</h2>
    <div class="akkordeon">
      <details open><summary>Naturschutzgebiet und Wildnisgebiet</summary><div class="panel"><p>Das Gebiet ist seit 1996 als Naturschutzgebiet festgesetzt und als Wildnisgebiet nach IUCN-Kategorie Ib anerkannt. In der Kernzone hat Prozessschutz Vorrang, in der Pflegezone werden Offenlandlebensräume gezielt erhalten.</p></div></details>
      <details><summary>FFH-Gebiet und Natura 2000</summary><div class="panel"><p>Die Königsbrücker Heide ist zugleich Fauna-Flora-Habitat-Gebiet (EU-Meldenummer DE4847302) und damit Teil des europäischen Schutzgebietsnetzes Natura 2000.</p></div></details>
      <details><summary>Lebensraumtypen, Fauna und Flora</summary><div class="panel"><p><span class="platzhalter">Redaktioneller Platzhalter</span> Hier beschreibt die NSG-Verwaltung die prägenden Lebensraumtypen sowie charakteristische Tier- und Pflanzenarten, ergänzt um Bilder und Verweise auf das Monitoring.</p></div></details>
    </div>
    <h2 class="zwischen" id="gohrischheide">Gohrischheide und Elbniederterrasse Zeithain</h2>
    <figure>
      <img src="img/gohrisch-3.jpg" srcset="img/gohrisch-3-800.jpg 800w, img/gohrisch-3.jpg 1600w" sizes="(max-width:900px) 100vw, 800px" alt="Heidefläche mit blühenden Pflanzen in der Gohrischheide" width="1600" height="1067">
      <figcaption>Heidefläche in der Gohrischheide. Foto: Staubi59, CC BY-SA 4.0</figcaption>
    </figure>
    <p>Das zweite Schutzgebiet der Verwaltung liegt bei Zeithain an der Elbe. Es ist als FFH- und Vogelschutzgebiet (SPA) Teil von Natura 2000. <span class="platzhalter">Steckbrief folgt aus Redaktion</span></p>
    <h2 class="zwischen" id="faq">Häufige Fragen</h2>
    <div class="akkordeon">
      <details><summary>Darf ich mit dem Fahrrad fahren?</summary><div class="panel"><p>Auf dem Radrundweg Königsbrücker Heide und dem Radrundweg Gohrischheide ja. Auf allen übrigen Pfaden gelten die Regeln der Beschilderung. <span class="platzhalter">Musterantwort</span></p></div></details>
      <details><summary>Sind Hunde erlaubt?</summary><div class="panel"><p><span class="platzhalter">Musterantwort</span> Die verbindliche Regelung ergibt sich aus der Schutzgebietsverordnung und wird hier redaktionell gepflegt.</p></div></details>
    </div>
    <h2 class="zwischen" id="forschung">Downloads</h2>
    <ul class="downloads">
      <li><a class="download" href="downloads/muster-faltblatt-biberpfad.pdf" download><span class="download__icon">PDF</span><span><b>Faltblatt Biberpfad (Muster)</b><small>PDF, 1 Seite</small></span></a></li>
      <li><a class="download" href="downloads/muster-jahresprogramm.pdf" download><span class="download__icon">PDF</span><span><b>Jahresprogramm (Muster)</b><small>PDF, 1 Seite</small></span></a></li>
    </ul>
    <p class="bildnachweis">Fakten: Wikipedia „Königsbrücker Heide“ (abgerufen 07.10.2026) und Sitemap der Vergabeunterlagen. Die Redaktion übernimmt nach Zuschlag die geprüften Inhalte der NSG-Verwaltung.</p>
  </article>
  <aside class="seitenleiste" aria-label="Weiterführend">
    <div class="kasten"><h2>Besuchen &amp; Erleben</h2><ul class="links"><li><a href="karte.html">Besucherpfade &amp; Karte</a></li><li><a href="veranstaltungen.html">Führungen buchen</a></li><li><a href="karte.html#ausflugsziele">Aussichtstürme</a></li></ul></div>
    <div class="kasten kasten--hell"><h2>Auf einen Blick</h2><p><b>Lage:</b> Westlausitz, nördlich von Königsbrück</p><p><b>Höchste Erhebung:</b> Königshöhe, 194,5 m</p><p style="margin:0"><b>Betreuung:</b> Naturschutzgebietsverwaltung im Staatsbetrieb Sachsenforst</p></div>
    <img src="img/kiefernwald-800.jpg" alt="Lichter Kiefernwald mit Hinweisschild" style="border-radius:18px" width="800" height="533">
    <p class="bildnachweis" style="margin-top:-1rem">Foto: Bybbisch94, CC BY-SA 4.0</p>
  </aside>
</div>
</main>"""
write("wildnisgebiet.html", layout("wildnisgebiet.html", "Wildnisgebiet Königsbrücker Heide", inhalt, active="wildnisgebiet.html"))

# ---------- Karte ----------
karte = """
<main id="inhalt">
<div class="seitenkopf"><div class="wrap">
  <nav class="brotkrumen" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li><a href="karte.html">Besuchen &amp; Erleben</a></li><li aria-current="page">Besucherpfade &amp; Karte</li></ol></nav>
  <h1>Besucherpfade und interaktive Karte</h1>
</div></div>
<div class="wrap kartenlayout">
  <div>
    <div id="karte" data-src="data/nsg.geojson" role="region" aria-label="Interaktive Karte der Schutzgebiete mit Besucherpfaden und Aussichtstürmen" tabindex="0"></div>
    <p class="bildnachweis">Kartengrundlage und Gebietsgrenzen: © OpenStreetMap-Mitwirkende (ODbL), Stand der Daten Mai 2026. Für den Echtbetrieb liefert der Auftraggeber die amtlichen Geodaten.</p>
  </div>
  <div>
    <p class="lead" style="font-size:1.15rem">Klicken Sie auf ein Schutzgebiet, um hineinzuzoomen. Besucherpfade und Aussichtstürme zeigen beim Anklicken einen Kurztext mit Link zur Detailseite.</p>
    <h2 style="font-size:1.3rem">Gebiet wählen</h2>
    <div class="gebiete">
      <button class="pille" type="button" data-zoom-gebiet="Wildnisgebiet Königsbrücker Heide">Königsbrücker Heide</button>
      <button class="pille" type="button" data-zoom-gebiet="Gohrischheide und Elbniederterrasse Zeithain">Gohrischheide</button>
      <button class="pille" type="button" data-zoom-gebiet="alle">Beide Gebiete</button>
    </div>
    <h2 style="font-size:1.3rem">Legende</h2>
    <ul class="legende">
      <li><i style="background:rgba(0,60,50,.25);border:3px solid #003c32"></i>Wildnisgebiet Königsbrücker Heide</li>
      <li><i style="background:rgba(138,90,140,.25);border:3px solid #8a5a8c"></i>NSG Gohrischheide und Elbniederterrasse Zeithain</li>
      <li><i style="background:#c77700;height:5px"></i>Besucherpfad / Radrundweg</li>
      <li><i style="background:#ffc842;border:3px solid #003c32;border-radius:50%;width:18px;height:18px"></i>Aussichtsturm / Ausflugsziel</li>
    </ul>
    <h2 style="font-size:1.3rem" id="ausflugsziele">Pfade in der Königsbrücker Heide</h2>
    <ul class="links"><li><a href="#karte">Radrundweg Königsbrücker Heide</a></li><li><a href="#karte">Biberpfad</a></li><li><a href="#karte">Turmpfad zum Haselberg</a></li><li><a href="#karte">Zochauer Heidepfad</a></li></ul>
    <h2 style="font-size:1.3rem;margin-top:1.2rem">Pfade in der Gohrischheide</h2>
    <ul class="links"><li><a href="#karte">Radrundweg Gohrischheide</a></li><li><a href="#karte">Heidepfad Spansberg</a></li></ul>
    <ul class="downloads"><li><a class="download" href="downloads/muster-faltblatt-biberpfad.pdf" download><span class="download__icon">PDF</span><span><b>Faltblatt Biberpfad (Muster)</b><small>Wanderkarte zum Download</small></span></a></li></ul>
  </div>
</div>
</main>"""
write("karte.html", layout("karte.html", "Besucherpfade und Karte", karte, active="karte.html",
      extra_head='<link rel="stylesheet" href="vendor/leaflet.css">',
      extra_js='<script src="vendor/leaflet.js" defer></script><script src="js/karte.js" defer></script>'))

# ---------- Veranstaltungen ----------
def vt(tag, mon, titel, text, ort, gebiet, art):
    return f"""<li class="termin" data-gebiet="{gebiet}"><div class="datum" aria-hidden="true"><b>{tag}</b><span>{mon}</span></div>
<div><h3><span class="visually-hidden">{tag}. {mon} 2026: </span>{titel}</h3><p>{text}</p><span class="tag">{ort}</span><span class="tag">{art}</span><span class="platzhalter">Beispieltermin</span></div>
<a class="btn" href="#online-shop" aria-label="{titel} – zur Anmeldung">Anmelden</a></li>"""
veranst = f"""
<main id="inhalt">
<div class="seitenkopf"><div class="wrap">
  <nav class="brotkrumen" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li><a href="veranstaltungen.html">Besuchen &amp; Erleben</a></li><li aria-current="page">Veranstaltungen</li></ol></nav>
  <h1>Veranstaltungen und Führungen</h1>
</div></div>
<div class="wrap inhalt">
  <div>
    <p class="lead">Ein großer Teil der Schutzgebiete ist nur mit Führung zugänglich. Die Naturschutzgebietsverwaltung bietet Wanderungen, Busführungen und Angebote für Familien, Kitas und Schulen an.</p>
    <div class="infobox"><h2>Hinweis zum Demonstrator</h2><p>Die Termine auf dieser Seite sind Beispiele zur Darstellung der Komponente. Im Echtbetrieb werden sie aus dem Veranstaltungsmodul bzw. dem Online-Shop („Teilnehmen &amp; Buchen“) gespeist.</p></div>
    <h2 class="zwischen">Termine im Herbst</h2>
    <ul class="filter" aria-label="Nach Gebiet filtern">
      <li><button type="button" data-filter="alle" aria-pressed="true">Alle</button></li>
      <li><button type="button" data-filter="kh" aria-pressed="false">Königsbrücker Heide</button></li>
      <li><button type="button" data-filter="gh" aria-pressed="false">Gohrischheide</button></li>
    </ul>
    <p id="filter-status" class="visually-hidden" role="status" aria-live="polite"></p>
    <ul class="termine termine--liste">
      {vt("17","Okt","Herbstwanderung am Biberpfad","Geführte Wanderung, ca. 3 Stunden, für Familien geeignet.","Königsbrücker Heide","kh","Wanderung")}
      {vt("24","Okt","Busführung Königsbrücker Heide","Rundfahrt durch das gesperrte Gelände mit Halt an Aussichtspunkten.","Königsbrücker Heide","kh","Busführung")}
      {vt("31","Okt","Turmpfad zum Haselberg","Wanderung zum Haselbergturm mit Blick über die Heide.","Königsbrücker Heide","kh","Wanderung")}
      {vt("07","Nov","Heidewanderung Gohrischheide","Wanderung zum Aussichtsturm in der Gohrischheide.","Gohrischheide","gh","Wanderung")}
      {vt("14","Nov","Busführung Gohrischheide","Rundfahrt mit Erläuterungen zur Gebietsentwicklung.","Gohrischheide","gh","Busführung")}
    </ul>
    <h2 class="zwischen" id="online-shop" style="margin-top:2.5rem">Teilnehmen &amp; Buchen</h2>
    <p>Die Anmeldung erfolgt über den in die Website eingebetteten Online-Shop. Es gelten die AGB und Teilnahmebedingungen der NSG-Verwaltung. <span class="platzhalter">Shop-Einbindung im Demonstrator nicht aktiv</span></p>
    <ul class="downloads">
      <li><a class="download" href="downloads/muster-jahresprogramm.pdf" download><span class="download__icon">PDF</span><span><b>Jahresprogramm (Muster)</b><small>PDF, 1 Seite</small></span></a></li>
    </ul>
  </div>
  <aside class="seitenleiste" aria-label="Weiterführend">
    <img src="img/pfad-800.jpg" alt="Wanderin auf einem Sandweg durch Kiefernwald" style="border-radius:18px" width="800" height="533">
    <p class="bildnachweis" style="margin-top:-1rem">Foto: Bybbisch94, CC BY-SA 4.0</p>
    <div class="kasten"><h2>Für Kitas &amp; Schulen</h2><p>Buchbare Angebote der Umwelt- und Wildnisbildung, auch mit dem „BiberBus für Kids“.</p><ul class="links"><li><a href="#online-shop">Anfrage stellen</a></li></ul></div>
  </aside>
</div>
</main>"""
write("veranstaltungen.html", layout("veranstaltungen.html", "Veranstaltungen", veranst, active="veranstaltungen.html"))

# ---------- Leichte Sprache ----------
SYM_WEG = '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M26 60c4-14 14-18 8-30-4-8 2-16 6-26" stroke="#003c32" stroke-width="7" fill="none" stroke-linecap="round"/></svg>'
SYM_STOP = '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="28" fill="#c0392b"/><rect x="14" y="27" width="36" height="10" fill="#fff"/></svg>'
SYM_MENSCH = '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="24" cy="14" r="7" fill="#003c32"/><circle cx="42" cy="14" r="7" fill="#003c32"/><path d="M14 58V32c0-6 4-10 10-10s10 4 10 10v26M32 58V32c0-6 4-10 10-10s10 4 10 10v26" fill="#003c32"/></svg>'
ls = f"""
<main id="inhalt">
<div class="seitenkopf"><div class="wrap">
  <nav class="brotkrumen" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li aria-current="page">Leichte Sprache</li></ol></nav>
  <h1>Die Königsbrücker Heide in Leichter Sprache</h1>
</div></div>
<div class="wrap" style="padding-top:2.5rem;padding-bottom:3rem">
  <p><span class="ls-logo">Leichte Sprache · Muster</span> <span class="platzhalter">Text vor Veröffentlichung durch Prüfgruppe prüfen lassen</span></p>
  <div class="ls">
    <div class="ls-block"><img src="img/hero-heide-800.jpg" alt="Heide mit lila Blüten" width="120" height="120"><div><h2>Was ist die Königsbrücker Heide?</h2><p>Die Königsbrücker Heide ist ein großes Natur-Gebiet.</p><p>Es liegt in Sachsen.<br>In der Nähe von der Stadt Königsbrück.</p></div></div>
    <div class="ls-block"><div class="ls-symbol">{SYM_MENSCH}</div><div><h2>Was war früher dort?</h2><p>Früher haben dort Soldaten geübt.<br>Das war fast 100 Jahre lang.</p><p>Heute dürfen die Pflanzen und Tiere dort frei wachsen.<br>Die Menschen greifen nicht ein.<br>Das nennt man: Wildnis.</p></div></div>
    <div class="ls-block"><div class="ls-symbol">{SYM_STOP}</div><div><h2>Das ist wichtig</h2><p>Im Boden kann noch gefährliche Munition liegen.</p><p>Darum dürfen Sie viele Teile vom Gebiet <strong>nicht</strong> betreten.</p></div></div>
    <div class="ls-block"><div class="ls-symbol">{SYM_WEG}</div><div><h2>Wo dürfen Sie gehen?</h2><p>Es gibt besondere Wege für Besucher.<br>Auf diesen Wegen dürfen Sie gehen.<br>Oder mit dem Fahrrad fahren.</p><p>Sie können auch mit einer Führung gehen.<br>Dann erklärt Ihnen jemand die Natur.</p><p><a class="btn btn--gruen" href="veranstaltungen.html">Zu den Führungen</a></p></div></div>
  </div>
</div>
</main>"""
write("leichte-sprache.html", layout("leichte-sprache.html", "Leichte Sprache", ls, active="leichte-sprache.html"))

# ---------- English ----------
en = """
<main id="inhalt">
<section class="hero" aria-label="Header image">
  <div class="hero__bild"><img src="../img/gohrisch-1.jpg" srcset="../img/gohrisch-1-800.jpg 800w, ../img/gohrisch-1.jpg 1600w" sizes="100vw" alt="Wide open heathland under a cloudy sky in the Gohrischheide" width="1600" height="1067"></div>
  <span class="hero__credit">Photo: Staubi59, CC BY-SA 4.0</span>
  <div class="blase" lang="en">
    <h2>Where nature can be nature again</h2>
    <p>A former military training area now develops without human intervention.</p>
    <a class="pfeil" href="../karte.html">Explore the map</a>
  </div>
</section>
<section class="willkommen">
  <div class="wrap">
    <h1>Welcome to Königsbrück Heath and Gohrischheide</h1>
    <div class="willkommen__grid">
      <ul class="pillen" aria-label="Quick links">
        <li><a class="pille" href="../karte.html">Trails &amp; interactive map</a></li>
        <li><a class="pille" href="../veranstaltungen.html">Guided tours</a></li>
        <li><a class="pille" href="#visit">Rules for visitors</a></li>
      </ul>
      <div>
        <p class="lead">North of the town of Königsbrück in Saxony lies one of the largest nature reserves in the state. For almost a century the area was used for military training. Today the landscape is left to develop freely.</p>
        <p>Near Zeithain on the River Elbe, the Gohrischheide and Elbniederterrasse Zeithain nature reserve protects dry heathland and open sandy areas. Both reserves are managed by the same reserve administration.</p>
      </div>
    </div>
  </div>
</section>
<section class="teaser">
  <div class="wrap teaser__grid">
    <article class="karte" id="discover"><img src="../img/offenland-800.jpg" alt="Open heathland with birch trees" width="800" height="533"><h3>Discover</h3><p>Around 6,932 hectares of protected land, recognised as a wilderness area (IUCN category Ib) and part of the Natura 2000 network.</p><p class="bildnachweis">Photo: Bybbisch94, CC BY-SA 4.0</p></article>
    <article class="karte" id="visit"><img src="../img/heideweg-800.jpg" alt="Sandy path through a light pine forest" width="800" height="533"><h3>Visit</h3><p>Large parts of the area must not be entered because of remaining munitions. Please stay on the marked visitor trails at all times.</p><p class="bildnachweis">Photo: Bybbisch94, CC BY-SA 4.0</p></article>
    <article class="karte" id="learn"><img src="../img/wiedehopf-800.jpg" alt="Hoopoe perched on a branch" width="800" height="533"><h3>Learn</h3><p>Research and monitoring, environmental education for schools and a junior ranger programme. <span class="platzhalter">Sample text</span></p><p class="bildnachweis">Photo: Jonaskreische, CC BY-SA 4.0</p></article>
  </div>
</section>
</main>"""
write("en/index.html", layout("en/index.html", "Welcome", en, lang="en", desc="NNL demonstrator: English start page"))

# ---------- Hinweise ----------
hin = """
<main id="inhalt">
<div class="seitenkopf"><div class="wrap">
  <nav class="brotkrumen" aria-label="Brotkrumen"><ol><li><a href="index.html">Startseite</a></li><li aria-current="page">Über diesen Demonstrator</li></ol></nav>
  <h1>Über diesen Demonstrator</h1>
</div></div>
<div class="wrap inhalt">
  <article>
    <p class="lead">Diese Website ist ein funktionsfähiger Web-Demonstrator im Corporate Design der Nationalen Naturlandschaften. PROGRESSIVE digital – Kock, Rietz GbR hat ihn eigenständig für die Vergabe 2026-VG-NG17-0001 (Relaunch der Website der NSG-Verwaltung Königsbrücker Heide / Gohrischheide) erstellt. Er ist keine offizielle Website der NSG-Verwaltung oder des Staatsbetriebs Sachsenforst.</p>
    <h2 class="zwischen">Umgesetzte Seitentypen</h2>
    <ul class="links"><li><a href="index.html">Startseite mit Titelbild, Dialogelement, Schnelleinstieg, Teasern, Warnbanner und Veranstaltungen</a></li><li><a href="wildnisgebiet.html">Inhaltsseite mit Text, Bild, Kennzahlen, Infobox, Akkordeon und Downloads</a></li><li><a href="karte.html">Kartenseite mit OpenStreetMap, Gebietsflächen, Pfaden und Aussichtstürmen</a></li><li><a href="veranstaltungen.html">Veranstaltungsseite mit Filter</a></li><li><a href="leichte-sprache.html">Seite in Leichter Sprache (Muster)</a></li><li><a href="en/index.html">Englische Sprachvariante</a></li></ul>
    <h2 class="zwischen" id="schrift">Schrift</h2>
    <p>Die Hausschrift der Nationalen Naturlandschaften ist die lizenzpflichtige FS Me. Das CD-Manual schließt Tahoma als Ersatzschrift für Websites ausdrücklich aus. Die Vergabestelle hat in der Antwort auf Bieterfrage 15 bestätigt, dass ein Demonstrator mit einer frei lizenzierten Schrift anerkannt wird. Wir verwenden deshalb Atkinson Hyperlegible Next (SIL Open Font License), eine Schrift, die wie die FS Me auf Lesbarkeit für Menschen mit Sehbeeinträchtigung ausgelegt ist. Im Projekt wird die FS Me als Webfont mit Lizenz des Auftraggebers eingebunden; der Austausch betrifft nur eine Variable im Stylesheet.</p>
    <h2 class="zwischen" id="logos">Logos</h2>
    <p>Die NNL-Dachmarke im Fußbereich stammt von nationale-naturlandschaften.de. Die Positionen für das Logo des Staatsbetriebs Sachsenforst sowie für die Logos von Wildnisgebiet und NSG sind gemäß Sitemap angelegt und mit Platzhaltern in der NNL-Kreis-Systematik belegt. Die Originaldateien stellt der Auftraggeber bereit.</p>
    <h2 class="zwischen">Bild- und Datennachweis</h2>
    <p>Fotos von Wikimedia Commons: Sonnentau25 (Königsbrücker Heide, CC BY-SA 4.0), Bybbisch94 (Zochauer Heidepfad, CC BY-SA 4.0), Jonaskreische (Wiedehopf, CC BY-SA 4.0), Staubi59 (Gohrischheide, CC BY-SA 4.0), Dr. Bernd Gross (NSG Königsbrücker Heide, CC BY-SA 3.0). Die Bilder wurden für das Web verkleinert. Karten- und Gebietsdaten: © OpenStreetMap-Mitwirkende, ODbL. Sachangaben: Wikipedia „Königsbrücker Heide“ sowie die Sitemap der Vergabeunterlagen, Stand 07.10.2026. Als Platzhalter gekennzeichnete Inhalte und Beispieltermine sind keine Angaben der NSG-Verwaltung.</p>
    <h2 class="zwischen" id="barrierefreiheit">Barrierefreiheit</h2>
    <p>Semantisches HTML mit Landmarks, Sprunglink, sichtbarem Tastaturfokus, Kontrasten nach WCAG 2.1 AA, skalierbarer Schrift, Hochkontrastmodus, Vorlesefunktion über die Sprachausgabe des Browsers sowie Alternativtexten. Die Darstellung funktioniert ab 320 Pixel Breite.</p>
    <h2 class="zwischen" id="datenschutz">Datenschutz</h2>
    <p>Der Demonstrator setzt keine Cookies und kein Tracking ein. Schrift und Skripte werden lokal ausgeliefert. Beim Aufruf der Kartenseite lädt der Browser Kartenkacheln von tile.openstreetmap.org. Hosting: GitHub Pages.</p>
    <h2 class="zwischen" id="impressum">Impressum</h2>
    <p>PROGRESSIVE digital – Kock, Rietz GbR<br>Hospeltstr. 65-67, 50825 Köln<br>kock@progressivedigital.de · progressivedigital.de</p>
  </article>
  <aside class="seitenleiste"><div class="kasten"><h2>Vergabe</h2><p>2026-VG-NG17-0001<br>Relaunch Website NSG-Verwaltung<br>Staatsbetrieb Sachsenforst</p><p style="margin:0">Stand des Demonstrators: 07.10.2026</p></div></aside>
</div>
</main>"""
write("hinweise.html", layout("hinweise.html", "Über diesen Demonstrator", hin))
print("ok")
