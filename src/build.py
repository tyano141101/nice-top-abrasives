#!/usr/bin/env python3
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from build_part1 import BASE, SRC, SITE, CATS, CAT_ORDER, PRODS, BY_CAT, SITE_URL, FORMSPREE, CSS, JS
from pathlib import Path

OUT = BASE
def w(rel, content):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

# ---------------------------------------------------------------- icons
def icon(slug):
    s = {'fill': 'none', 'stroke': 'currentColor', 'stroke-width': '2.4',
         'stroke-linecap': 'round', 'stroke-linejoin': 'round'}
    inner = {
        'convolute-wheel': '<circle cx="24" cy="24" r="16"/><circle cx="24" cy="24" r="10"/><circle cx="24" cy="24" r="4"/><path d="M24 8v4M24 36v4M8 24h4M36 24h4"/>',
        'unitized-wheel': '<rect x="10" y="10" width="28" height="7" rx="3.5"/><rect x="10" y="20.5" width="28" height="7" rx="3.5"/><rect x="10" y="31" width="28" height="7" rx="3.5"/>',
        'laser-braze-finishing-wheel': '<path d="M8 34c4-10 10-16 16-16s12 6 16 16"/><path d="M24 18V8M18 12l3 4 3-4M33 10l1 4M15 10l-1 4"/><circle cx="24" cy="34" r="2.5"/>',
        'nylon-polishing-wheel': '<circle cx="24" cy="24" r="15"/><circle cx="24" cy="24" r="5"/><path d="M24 9v6M24 33v6M9 24h6M33 24h6M13 13l4 4M31 31l4 4M35 13l-4 4M17 31l-4 4"/>',
        'radial-bristle-disc': '<circle cx="24" cy="24" r="4"/><path d="M24 6v12M24 30v12M6 24h12M30 24h12M11 11l8 8M29 29l8 8M37 11l-8 8M19 29l-8 8"/>',
        'bristle-disc': '<rect x="20" y="6" width="8" height="14" rx="2"/><path d="M14 22h20v6H14z"/><path d="M16 30v10M22 30v12M28 30v10M34 30v8"/>',
        'scouring-pad': '<rect x="8" y="14" width="32" height="20" rx="5"/><circle cx="16" cy="22" r="1.4"/><circle cx="24" cy="26" r="1.4"/><circle cx="32" cy="22" r="1.4"/><circle cx="20" cy="29" r="1.4"/><circle cx="28" cy="29" r="1.4"/>',
    }[slug]
    return f'<svg viewBox="0 0 48 48" fill="{s["fill"]}" stroke="{s["stroke"]}" stroke-width="{s["stroke-width"]}" stroke-linecap="{s["stroke-linecap"]}" stroke-linejoin="{s["stroke-linejoin"]}">{inner}</svg>'

# ---------------------------------------------------------------- chrome
def header(root, active=""):
    def lk(href, label, key):
        cls = ' class="nav-link active"' if active == key else ' class="nav-link"'
        return f'<a{cls} href="{root}{href}">{label}</a>'
    drop = "".join(
        f'<a href="{root}category/{s}.html">{CATS[s]["name"]}<span>{len(BY_CAT[s])} products</span></a>'
        for s in CAT_ORDER)
    return f"""<header class="site-header"><div class="container header-inner">
<a class="logo" href="{root}index.html"><span class="mark">N</span><span>{SITE['brand']}®<small>{SITE['tagline']}</small></span></a>
<button class="menu-toggle" aria-label="Menu">☰</button>
<nav class="nav">
{lk('index.html','Home','home')}
<span class="has-drop"><a class="nav-link{' active' if active=='products' else ''}" href="{root}products/index.html">Products ▾</a><span class="drop">{drop}</span></span>
{lk('applications.html','Applications','applications')}
{lk('about.html','About Us','about')}
{lk('contact.html','Contact','contact')}
<a class="btn-navy" href="{root}contact.html">Get a Quote</a>
</nav></div></header>"""

def footer(root):
    prod_links = "".join(f'<a href="{root}category/{s}.html">{CATS[s]["name"]}</a>' for s in CAT_ORDER)
    return f"""<footer><div class="container foot-grid">
<div class="foot-brand"><a class="logo" href="{root}index.html" style="color:#fff"><span class="mark">N</span><span>{SITE['brand']}®<small style="color:#8fa3bd">{SITE['tagline']}</small></span></a>
<p>Manufacturer of non-woven abrasive wheels for deburring, blending, finishing and polishing — serving aerospace, automotive, oil &amp; gas, medical and metal fabrication industries worldwide.</p></div>
<div><h4>Products</h4>{prod_links}</div>
<div><h4>Company</h4><a href="{root}about.html">About Us</a><a href="{root}applications.html">Applications</a><a href="{root}products/index.html">All Products</a><a href="{root}contact.html">Contact</a><a href="{root}contact.html">Get a Quote</a></div>
<div><h4>Contact</h4><a href="mailto:{SITE['email']}">{SITE['email']}</a><a href="tel:{SITE['phone'].replace(' ','')}">{SITE['phone']}</a><a href="tel:{SITE['phone2'].replace(' ','')}">{SITE['phone2']}</a><a>{SITE['address']}</a><a>{SITE['hours']}</a></div>
</div><div class="foot-bottom container"><span>© <span id="year"></span> {SITE['company']} All rights reserved.</span><span>{SITE['brand']}® Abrasives</span></div></footer>"""

def page(root, title, desc, body, active=""):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {SITE['brand']} Abrasives</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'><rect width='48' height='48' rx='10' fill='%230c2b4d'/><text x='24' y='33' font-size='26' text-anchor='middle' fill='%23f26b1d' font-family='Arial' font-weight='bold'>N</text></svg>">
<style>{CSS}</style></head>
<body>{header(root, active)}{body}{footer(root)}<script>{JS}</script></body></html>"""

def cta_banner(root):
    return f"""<div class="container"><div class="cta" style="margin:20px 0 70px">
<div><h2>Need a custom specification?</h2><p>We support OEM/ODM with custom density, grit (S/C or A/O) and dimensions. Send your drawing or target finish — our engineers reply within 24 hours.</p></div>
<a class="btn" href="{root}contact.html">Request a Quote</a></div></div>"""

def crumbs(root, *items):
    inner = ' &nbsp;/&nbsp; '.join(
        f'<a href="{root}{h}">{t}</a>' if h else t for t, h in items)
    return f'<div class="crumbs">{inner}</div>'

# ---------------------------------------------------------------- home
def build_home():
    feat = ""
    for s in ['convolute-wheel', 'unitized-wheel', 'laser-braze-finishing-wheel']:
        c = CATS[s]
        img = f"cat-{s.split('-')[0]}" if s != 'laser-braze-finishing-wheel' else "cat-laser-braze"
        feat += f"""<div class="card"><div class="card-img"><img src="assets/img/{img}.svg" alt="{c['name']}" loading="lazy"></div>
<div class="card-body"><h3>{c['name']}</h3><p>{c['tagline']}.</p>
<div class="card-meta"><span class="count">{len(BY_CAT[s])} products</span><a class="link-more" href="category/{s}.html">View range →</a></div></div></div>"""
    cats = ""
    for s in CAT_ORDER:
        c = CATS[s]
        cats += f"""<div class="card"><div class="card-icon">{icon(s)}</div>
<div class="card-body"><h3>{c['name']}</h3><p>{c['tagline']}.</p>
<div class="card-meta"><span class="count">{len(BY_CAT[s])} products</span><a class="link-more" href="category/{s}.html">View →</a></div></div></div>"""
    apps = ["Aerospace & Aviation", "Oil & Gas Exploration", "Medical Devices", "Automotive Manufacturing",
            "3C & Precision Electronics", "Heavy Machinery", "Metal Fabrication", "Stone Processing", "Jewelry"]
    body = f"""
<section class="hero"><div class="hero-inner">
<h1>Professional Non-Woven Abrasive Wheels Manufacturer</h1>
<p>{SITE['company']} ({SITE['brand']}®) researches, develops and manufactures convolute wheels, unitized wheels, bristle discs, laser-braze finishing wheels and more — delivering efficient, reliable surface finishing for industries worldwide.</p>
<div class="hero-cta"><a class="btn" href="products/index.html">Browse Products</a><a class="btn-outline" href="contact.html">Get a Quote</a></div>
<div class="hero-chips"><span>20+ Years Experience</span><span>60 Products</span><span>OEM / ODM Support</span><span>24/7 Online Support</span></div>
</div></section>
<section class="stats"><div class="stats-inner">
<div class="stat"><b>20+</b><span>Years in abrasives</span></div>
<div class="stat"><b>7</b><span>Product categories</span></div>
<div class="stat"><b>60</b><span>Products in catalog</span></div>
<div class="stat"><b>24/7</b><span>Online support</span></div>
</div></section>
<section class="section"><div class="container">
<div class="sec-head"><span class="kicker">Featured lines</span><h2>Engineered for Demanding Finishing Jobs</h2><p>Three flagship product lines trusted by automotive, aerospace and oil &amp; gas manufacturers.</p></div>
<div class="grid3">{feat}</div></div></section>
<section class="section alt"><div class="container">
<div class="sec-head"><span class="kicker">Full catalog</span><h2>Our Product Range</h2><p>Seven non-woven abrasive product families with complete specifications and stable performance.</p></div>
<div class="grid4">{cats}</div></div></section>
<section class="section"><div class="container">
<div class="sec-head"><span class="kicker">Industries</span><h2>Serving Industries Worldwide</h2></div>
<div class="chips">{''.join(f'<span class="chip">{a}</span>' for a in apps)}</div>
</div></section>
<section class="section alt"><div class="container">
<div class="sec-head"><span class="kicker">Why {SITE['brand']}</span><h2>Quality Driven by Innovation</h2></div>
<div class="why-grid">
<div class="why"><div class="n">1</div><h3>R&amp;D Capability</h3><p>Continuous improvement of abrasive formulations and web construction for longer life and consistent finish.</p></div>
<div class="why"><div class="n">2</div><h3>Stable Performance</h3><p>Complete specifications with tight process control — every batch finishes like the last one.</p></div>
<div class="why"><div class="n">3</div><h3>Deep Customization</h3><p>Custom density, grit (silicon carbide or aluminum oxide) and dimensions, plus full OEM/ODM service.</p></div>
<div class="why"><div class="n">4</div><h3>Responsive Service</h3><p>Engineering support for application matching and 24/7 online response for global customers.</p></div>
</div></div></section>
{cta_banner('')}
"""
    w("index.html", page("", f"{SITE['company']} — Manufacturer of Non-Woven Abrasive Wheels",
        f"{SITE['brand']}® by {SITE['company']}: convolute wheels, unitized wheels, bristle discs, laser braze finishing wheels, nylon polishing wheels and scouring pads for global B2B buyers.", body, "home"))

# ---------------------------------------------------------------- products hub
def build_hub():
    cards = ""
    for s in CAT_ORDER:
        c = CATS[s]
        cards += f"""<div class="card"><div class="card-icon">{icon(s)}</div>
<div class="card-body"><h3>{c['name']}</h3><p>{c['description'][:150]}…</p>
<div class="card-meta"><span class="count">{len(BY_CAT[s])} products</span><a class="link-more" href="../category/{s}.html">View range →</a></div></div></div>"""
    body = f"""
<section class="page-hero"><div class="container">{crumbs('../', ('Home','index.html'), ('Products', None))}
<h1>All Products</h1><p>Seven non-woven abrasive product families — {len(PRODS)} products with complete specifications. Click a category to browse sizes, grits and materials.</p></div></section>
<section class="section"><div class="container"><div class="grid3">{cards}</div></div></section>
{cta_banner('../')}
"""
    w("products/index.html", page("../", "All Products", "Complete catalog of non-woven abrasive wheels: convolute, unitized, bristle discs, laser braze finishing wheels and more.", body, "products"))

# ---------------------------------------------------------------- category pages
def build_category(s):
    c = CATS[s]; prods = BY_CAT[s]
    cards = ""
    for p in prods:
        chips = "".join(f"<span>{v}</span>" for _, v in p["specs"][:3])
        cards += f"""<div class="prod-card"><h3>{p['name']}</h3><p class="blurb">{p['blurb']}</p>
<div class="spec-chips">{chips}</div>
<div class="prod-actions"><a href="../product/{p['slug']}.html">Details →</a><a class="inq" href="../contact.html?product={p['slug']}">Inquire</a></div></div>"""
    apps = "".join(f'<span class="chip">{a}</span>' for a in c["applications"])
    body = f"""
<section class="page-hero"><div class="container">{crumbs('../', ('Home','index.html'), ('Products','products/index.html'), (c['name'], None))}
<div class="cat-head"><div class="card-icon">{icon(s)}</div><div><h1>{c['name']}</h1><p>{c['tagline']}. {len(prods)} products.</p></div></div></div></section>
<section class="section"><div class="container">
<p style="max-width:820px">{c['description']}</p>
<div class="spec-box"><b>Materials &amp; options:</b> {c['materials']}</div>
<h3 style="color:var(--navy);margin-bottom:12px">Typical applications</h3>
<div class="chips" style="justify-content:flex-start;margin-bottom:10px">{apps}</div>
<div class="filter-bar"><input id="prodFilter" type="text" placeholder="Filter products by name, size or grit…"></div>
<div class="prod-grid">{cards}</div>
</div></section>
{cta_banner('../')}
"""
    w(f"category/{s}.html", page("../", c["name"], c["tagline"] + ". " + c["description"][:140], body, "products"))

# ---------------------------------------------------------------- product pages
def build_product(p):
    c = CATS[p["category"]]
    rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in p["specs"])
    apps = "".join(f'<span class="chip">{a}</span>' for a in c["applications"][:6])
    rel = [x for x in BY_CAT[p["category"]] if x["slug"] != p["slug"]][:3]
    rel_html = "".join(
        f"""<div class="prod-card"><h3>{x['name']}</h3><p class="blurb">{x['blurb']}</p>
<div class="prod-actions"><a href="{x['slug']}.html">Details →</a><a class="inq" href="../contact.html?product={x['slug']}">Inquire</a></div></div>"""
        for x in rel)
    body = f"""
<section class="page-hero"><div class="container">{crumbs('../', ('Home','index.html'), ('Products','products/index.html'), (c['name'], f'category/{p["category"]}.html'), (p['name'], None))}
<h1 style="font-size:30px">{p['name']}</h1><p>{c['name']} · {SITE['brand']}® Abrasives</p></div></section>
<section class="section"><div class="container"><div class="pd-layout">
<div class="pd-main">
<p class="blurb">{p['blurb']}</p>
<h3 style="color:var(--navy);margin-bottom:12px">Specifications</h3>
<table class="specs">{rows}</table>
<h3 style="color:var(--navy);margin-bottom:12px">Typical applications</h3>
<div class="chips" style="justify-content:flex-start">{apps}</div>
<div class="rel"><h3>Related products</h3><div class="prod-grid" style="grid-template-columns:repeat(3,1fr)">{rel_html}</div></div>
</div>
<div class="pd-side"><div class="inq-card"><h3>Request a Quote</h3>
<p>Get pricing, lead time and custom specifications for <b>{p['name']}</b>. Our engineers reply within 24 hours.</p>
<a class="btn" href="../contact.html?product={p['slug']}">Inquire Now</a></div></div>
</div></div></section>
{cta_banner('../')}
"""
    w(f"product/{p['slug']}.html",
      page("../", p["name"], p["blurb"] + f" {c['name']} by {SITE['brand']} Abrasives.", body, "products"))

# ---------------------------------------------------------------- static pages
APPS_DETAIL = [
    ("Aerospace & Aviation", "Turbine blade blending, precision component finishing and edge radiusing with convolute and unitized wheels."),
    ("Oil & Gas Exploration", "Ultra-high hardness unitized wheels for mud-motor rotors, drill pipe, tubing and downhole tools."),
    ("Medical Devices", "Fine finishing of surgical instruments and implant preparation with unitized and bristle products."),
    ("Automotive Manufacturing", "Robotic laser-braze seam finishing on body-in-white lines with LB finishing wheels."),
    ("3C & Precision Electronics", "Delicate deburring and surface conditioning with fine-grit bristle discs."),
    ("Heavy Machinery", "Weld blending, descaling and maintenance finishing with unitized wheels and bristle discs."),
    ("Metal Fabrication", "Deburring, edge breaking and satin finishing across the full non-woven wheel range."),
    ("Stone Processing", "Surface conditioning and finishing with conformable non-woven abrasives."),
    ("Jewelry", "Detail polishing and mirror finishing with assorted radial bristle disc kits."),
]

def build_applications():
    cards = "".join(
        f'<div class="why"><div class="n">{i+1}</div><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(APPS_DETAIL))
    body = f"""
<section class="page-hero"><div class="container">{crumbs('', ('Home','index.html'), ('Applications', None))}
<h1>Applications</h1><p>Non-woven abrasive solutions engineered for the finishing challenges of nine industries.</p></div></section>
<section class="section"><div class="container"><div class="why-grid" style="grid-template-columns:repeat(3,1fr)">{cards}</div></div></section>
{cta_banner('')}
"""
    w("applications.html", page("", "Applications", "Aerospace, automotive, oil & gas, medical and more — industries served by Nice Top non-woven abrasive wheels.", body, "applications"))

def build_about():
    facts = "".join(f"<li><b>{k}</b>{v}</li>" for k, v in [
        ("Company", SITE["company"]), ("Brand", SITE["brand"] + "®"),
        ("Location", SITE["address"]), ("Experience", "20+ years in the abrasives industry"),
        ("Business", "R&D and manufacturing of non-woven abrasive wheels"),
        ("Customization", "Density, grit (S/C & A/O), dimensions; OEM/ODM supported"),
        ("Support", "24/7 online support; engineering application assistance"),
    ])
    body = f"""
<section class="page-hero"><div class="container">{crumbs('', ('Home','index.html'), ('About Us', None))}
<h1>About Us</h1><p>{SITE['tagline']} — quality driven by technological innovation.</p></div></section>
<section class="section"><div class="container"><div class="about-grid">
<div><h2 style="color:var(--navy);margin-bottom:14px">We deliver efficient, reliable surface finishing</h2>
<p>{SITE['company']}, renowned worldwide for its flagship brand {SITE['brand']}®, specializes in the research, development and manufacturing of abrasive wheel products — dedicated to providing efficient and reliable surface finishing solutions for a wide range of industries.</p>
<p style="margin-top:12px">Our main products include convolute wheels, unitized wheels, bristle discs, radial bristle discs, laser braze finishing wheels and nylon polishing wheels. With complete specifications and stable performance, these products are widely used in weld finishing, deburring, satin finishing, polishing and precision grinding — compatible with automated machinery, industrial robots and hand tools.</p>
<ul class="fact-list">{facts}</ul></div>
<div><img src="assets/img/hero-home.svg" alt="Factory" loading="lazy"></div>
</div></div></section>
{cta_banner('')}
"""
    w("about.html", page("", "About Us", f"About {SITE['company']} ({SITE['brand']}®) — 20+ years manufacturing non-woven abrasive wheels.", body, "about"))

def build_contact():
    opts = "".join(f'<option value="{p["slug"]}">{p["name"]}</option>' for p in PRODS)
    body = f"""
<section class="page-hero"><div class="container">{crumbs('', ('Home','index.html'), ('Contact', None))}
<h1>Contact Us &amp; Get a Quote</h1><p>Tell us your application or target finish — our engineers reply within 24 hours.</p></div></section>
<section class="section"><div class="container"><div class="form-grid">
<form class="inquiry" action="{FORMSPREE}" method="POST">
<div class="f-row"><div class="f-group"><label>Your Name <span class="req">*</span></label><input name="name" required></div>
<div class="f-group"><label>Email <span class="req">*</span></label><input name="email" type="email" required></div></div>
<div class="f-row"><div class="f-group"><label>Company</label><input name="company"></div>
<div class="f-group"><label>Country</label><input name="country"></div></div>
<div class="f-group"><label>Product of Interest</label><select id="f_product" name="product"><option value="">— Select a product —</option>{opts}</select></div>
<div class="f-group"><label>Estimated Quantity</label><input name="quantity" placeholder="e.g. 500 pcs / monthly"></div>
<div class="f-group"><label>Message <span class="req">*</span></label><textarea name="message" required placeholder="Target material, finish requirements, or custom specifications…"></textarea></div>
<button class="btn" type="submit">Send Inquiry</button>
<p class="form-note">Prefer email? Write to <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
</form>
<div>
<div class="info-card"><h3>📧 Email</h3><p>{SITE['email']}<br>{SITE['email2']}</p></div>
<div class="info-card"><h3>📞 Phone / WhatsApp</h3><p>{SITE['phone']}<br>{SITE['phone2']}</p></div>
<div class="info-card"><h3>📍 Address</h3><p>{SITE['address']}</p></div>
<div class="info-card"><h3>🕘 Working Hours</h3><p>{SITE['hours']}</p></div>
</div></div></div></section>
"""
    w("contact.html", page("", "Contact Us", f"Contact {SITE['company']} for quotes on non-woven abrasive wheels — reply within 24 hours.", body, "contact"))

# ---------------------------------------------------------------- sitemap
def build_sitemap():
    urls = ["", "products/index.html", "applications.html", "about.html", "contact.html"]
    urls += [f"category/{s}.html" for s in CAT_ORDER]
    urls += [f"product/{p['slug']}.html" for p in PRODS]
    items = "\n".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>" for u in urls)
    w("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>')

# ---------------------------------------------------------------- main
def main():
    for d in ["category", "product", "products", "assets/css", "assets/js"]:
        (OUT / d).mkdir(parents=True, exist_ok=True)
    (OUT / "assets/css/style.css").write_text(CSS, encoding="utf-8")
    (OUT / "assets/js/main.js").write_text(JS, encoding="utf-8")
    build_home(); build_hub()
    for s in CAT_ORDER: build_category(s)
    for p in PRODS: build_product(p)
    build_applications(); build_about(); build_contact(); build_sitemap()
    n = len(list(OUT.rglob("*.html")))
    print(f"Built {n} HTML pages + sitemap.xml")

if __name__ == "__main__":
    main()
