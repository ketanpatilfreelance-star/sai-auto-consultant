"""Builds the Sai Auto Consultant website.

    python3 build.py

Outputs:
  dist/      -> upload this folder to your host (Netlify, Vercel, Hostinger, cPanel...)
  preview/   -> the same pages packaged for the Claude artifact preview
Set SITE_URL below to the real domain before deploying (used for SEO tags + sitemap).
"""
import json, html, pathlib, shutil

SITE_URL = "https://www.saiautoconsultant.com"   # <- change to the real domain
ROOT = pathlib.Path(__file__).parent
e = html.escape

B = dict(
  name="Sai Auto Consultant", legal="Sai Auto Consultant Pvt Ltd", founded="1999",
  jignesh="+91 98252 43838", jignesh_tel="+919825243838",
  yash="+91 95122 80270", yash_tel="+919512280270", wa="919512280270",
  street="Shop 16, Sukhsagar Residency, Near GIDC Pandesara, Laxmi Narayan Nagar, Pandesaragam",
  locality="Udhana, Surat", city="Surat", region="Gujarat", pin="394221",
  lat=21.1449398, lng=72.8347276,
  maps="https://maps.app.goo.gl/56nSjpUMeZNs8RM7A",
  maps_embed="https://www.google.com/maps?q=21.1449398,72.8347276&z=16&output=embed",
  insta="https://www.instagram.com/sai.auto.consultant",
  review="https://www.google.com/search?q=Sai+Auto+Consultant+Surat",
)

ARR = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M2 8h12M9 3l5 5-5 5"/></svg>'
def btn(label, href, cls="btn-light", ext=False, page=False):
    attrs = ' target="_blank" rel="noopener"' if ext else (' data-page' if page else '')
    return f'<a class="btn {cls}" href="{href}"{attrs}><span>{label}</span><span class="ar">{ARR}{ARR}</span></a>'
STAR = '<svg viewBox="0 0 20 20" fill="currentColor"><path d="M10 1.5l2.6 5.6 6.1.7-4.5 4.2 1.2 6L10 15l-5.4 3 1.2-6L1.3 7.8l6.1-.7z"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'
WA_HELLO = "https://wa.me/" + B["wa"] + "?text=" + "Hello%20Sai%20Auto%20Consultant%2C%20I%20have%20an%20enquiry."

NAV = [("./", "Home", "home"), ("about.html", "About Us", "about"), ("services.html", "Our Services", "services"), ("visit.html", "Visit Us", "visit")]

def header(active):
    items = "".join(f'<li><a data-page href="{h}"{" aria-current=\"page\"" if k==active else ""}>{t}</a></li>' for h,t,k in NAV)
    ditems = "".join(f'<li><a data-page href="{h}">{t}</a></li>' for h,t,k in NAV)
    return f'''
<div class="curtain" aria-hidden="true"><div class="c-in"><img src="assets/img/logo.png" alt=""><div class="yr" hidden>1999</div><small>Sai Auto Consultant · Surat</small></div></div>
<header class="nav">
  <div class="wrap">
    <a class="brand" data-page href="./" aria-label="Sai Auto Consultant, home"><img src="assets/img/logo.png" alt="Sai Auto Consultant logo" width="40" height="40"><span><b>Sai Auto Consultant</b><small>Surat · Since 1999</small></span></a>
    <nav aria-label="Main"><ul class="menu">{items}</ul></nav>
    {btn("Get a free quote", "visit.html#enquire", "btn-light", page=True)}
    <button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><i></i><i></i></button>
  </div>
</header>
<div class="drawer"><ul>{ditems}</ul><div class="meta"><span>Jignesh · {B["jignesh"]}</span><span>Yash · {B["yash"]}</span><span>Mon–Sat · 10:00 AM onwards</span></div></div>'''

def footer():
    return f'''
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div><p class="lead">Surat's trusted name in vehicles since 1999.</p></div>
      <div><h4>Pages</h4><ul>{"".join(f'<li><a data-page href="{h}">{t}</a></li>' for h,t,k in NAV)}</ul></div>
      <div><h4>Call</h4><ul><li><a href="tel:{B["jignesh_tel"]}">Jignesh · {B["jignesh"]}</a></li><li><a href="tel:{B["yash_tel"]}">Yash · {B["yash"]}</a></li><li><a href="{WA_HELLO}" target="_blank" rel="noopener">WhatsApp</a></li><li><a href="{B["insta"]}" target="_blank" rel="noopener">Instagram @sai.auto.consultant</a></li></ul></div>
      <div><h4>Showroom</h4><address>Shop 16, Sukhsagar Residency,<br>Near GIDC Pandesara, Udhana,<br>Surat, Gujarat 394221<br><br>Mon–Sat · 10:00 AM onwards<br>Sunday closed</address></div>
    </div>
  </div>
  <div class="wrap"><div class="wordmark" aria-hidden="true">Sai Auto</div></div>
  <div class="wrap"><div class="legal"><span>© <span data-year>2026</span> Sai Auto Consultant · Est. 1999 · All rights reserved</span><span>Surat · Gujarat · India</span></div></div>
</footer>
<a class="fab" href="{WA_HELLO}" target="_blank" rel="noopener" aria-label="Chat with Sai Auto Consultant on WhatsApp">{WA_ICON}</a>'''

def hero(img, eyebrow, lines, lede, cta, short=False, pos="center", stats=""):
    h1 = "".join(f'<span class="ln"><span>{l}</span></span>' for l in lines)
    return f'''
<section class="hero{' short' if short else ''}" style="--pos:{pos}">
  <div class="hero-media"><img src="assets/img/{img}" alt="" fetchpriority="high"></div>
  <div class="wrap hero-inner">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <div class="hero-foot"><p class="lede">{lede}</p><div class="cta">{cta}</div></div>
    {stats}
  </div>
  <div class="scrollcue">Scroll</div>
</section>'''

def owners(long=False):
    j = ("With over two decades in the automotive industry, Jignesh brings unmatched experience in vehicle valuation, dealer relations and customer trust. He built Sai Auto Consultant from the ground up, one honest deal at a time." if long else
         "Over two decades in the automotive trade: vehicle valuation, dealer relations and customer trust.")
    y = ("Yash combines youthful energy with deep industry knowledge, taking Sai Auto Consultant into its next chapter. From customer experience to inventory, he is modernising every part of the business." if long else
         "Brings fresh energy and digital-first thinking to every deal, from customer experience to inventory.")
    return f'''
<div class="owners">
  <article class="owner rv">
    <div class="owner-top"><div class="mono-lg" aria-hidden="true">JS</div><div><h3>Jignesh Solanki</h3><div class="role">Founder &amp; Senior Consultant</div></div></div>
    <blockquote>“In 25 years, our currency has always been trust. That will never change.”</blockquote>
    <p>{j}</p>
    <div class="tel"><a href="tel:{B["jignesh_tel"]}">{B["jignesh"]}</a>{btn("Call", "tel:"+B["jignesh_tel"], "btn-dark")}</div>
  </article>
  <article class="owner rv">
    <div class="owner-top"><div class="mono-lg" aria-hidden="true">YS</div><div><h3>Yash Solanki</h3><div class="role">Co-Owner &amp; Operations Head</div></div></div>
    <blockquote>“We're building on a powerful legacy and taking it to the next generation.”</blockquote>
    <p>{y}</p>
    <div class="tel"><a href="tel:{B["yash_tel"]}">{B["yash"]}</a>{btn("Call", "tel:"+B["yash_tel"], "btn-dark")}</div>
  </article>
</div>'''

def final(title_html, sub):
    return f'''
<section class="sec on-ink final">
  <div class="wrap">
    <p class="eyebrow rv">Ready when you are</p>
    <h2 class="rv" style="margin-top:22px">{title_html}</h2>
    <p class="lede rv" style="margin-top:26px">{sub}</p>
    <div class="cta rv">{btn("Call Jignesh", "tel:"+B["jignesh_tel"])}{btn("Call Yash", "tel:"+B["yash_tel"], "btn-line")}{btn("WhatsApp us", WA_HELLO, "btn-line", ext=True)}</div>
  </div>
</section>'''

DELIVERIES = [("anil-singh-tata-nexon","Mr. Anil Singh","Tata Nexon"),("sunil-mistry-royal-enfield","Mr. Sunil Mistry","Royal Enfield Goan Classic"),
              ("pushpendra-chagal-access-125","Mr. Pushpendra Chagal","Suzuki Access 125 LE"),("guddu-sav-access-125","Mr. Guddu Sav","Suzuki Access 125")]

# ------------------------------------------------------------------ HOME
home_stats = f'''
<div class="stats">
  <div class="stat"><b><span data-count data-years>27</span>+</b><span>Years of experience</span></div>
  <div class="stat"><b>2</b><span>Owners, father &amp; son</span></div>
  <div class="stat"><b>2W + 4W</b><span>All vehicle types</span></div>
  <div class="stat"><b><span data-count="5" data-dec="1">5.0</span></b><span>Google rating</span></div>
</div>'''
HOME = hero("hero-sedan.webp", "Surat's trusted vehicle dealer · Est. 1999",
            ["Your vehicle", "journey, <em>handled</em>", "since 1999."],
            "Two-wheelers and four-wheelers, new and pre-owned. Buying, selling, insurance and RTO work, all under one roof in Pandesara, Surat.",
            btn("Explore services", "services.html", page=True) + btn("Call Jignesh · 98252 43838", "tel:"+B["jignesh_tel"], "btn-line"),
            pos="center 60%", stats=home_stats) + f'''
<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Why Sai Auto Consultant</p>
    <p class="statement">A family business built on <em>decades</em> of honest dealing. Jignesh Solanki started it in 1999, one honest deal at a time. Today his son Yash carries it into the next generation.</p>
    <div class="sign-off rv"><span class="mono">S</span><span><span data-years>27</span> years of trust · Sales, insurance and RTO under one roof</span></div>
  </div>
</section>

<section class="expand">
  <figure><img src="assets/img/rider-highway.webp" alt="A rider on an open highway at sunset" loading="lazy">
    <figcaption><p>From scooters to SUVs, the right vehicle at the right price.</p><span>Two-wheelers · Four-wheelers</span></figcaption></figure>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head rv"><div><p class="eyebrow">What we do</p><h2>Every vehicle need,<br><em>handled.</em></h2></div>{btn("View all services", "services.html", "btn-dark", page=True)}</div>
    <div class="rows">
      <a class="row rv" data-page href="services.html#new" data-img="new"><span class="n">01</span><h3>New vehicle sales</h3><p>The latest two- and four-wheelers from all major brands, at the best prices.</p><span class="go">{ARR}</span></a>
      <a class="row rv" data-page href="services.html#pre-owned" data-img="used"><span class="n">02</span><h3>Buy &amp; sell pre-owned</h3><p>Fair valuations, transparent deals and certified used vehicles.</p><span class="go">{ARR}</span></a>
      <a class="row rv" data-page href="services.html#insurance" data-img="ins"><span class="n">03</span><h3>Insurance &amp; RTO</h3><p>End-to-end policy handling, renewals, claims and documentation.</p><span class="go">{ARR}</span></a>
    </div>
  </div>
  <div class="peek" aria-hidden="true"><img data-key="new" src="assets/img/sedan-road.webp" alt=""><img data-key="used" src="assets/img/sportbike.webp" alt=""><img data-key="ins" src="assets/img/suv-white.webp" alt=""></div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="head rv"><div><p class="eyebrow">The people behind Sai Auto</p><h2>Family. Expertise.<br><em>Trust.</em></h2></div><p class="lede">Two generations at one desk. You deal with the owners directly, from the first call to the RC in your name.</p></div>
    {owners()}
  </div>
</section>

<section class="sec on-ink">
  <div class="wrap review">
    <div class="score rv"><b><span data-count="5" data-dec="1">5.0</span></b><div class="stars" aria-label="5 out of 5 stars">{STAR*5}</div><small>Google rating</small></div>
    <div class="rv"><blockquote>“Exceptional service and complete transparency. Jignesh bhai and Yash bhai made the entire process, from vehicle selection to registration, absolutely seamless. Truly Surat's best auto consultant.”</blockquote><cite>Google review · Verified customer</cite>
      <div style="margin-top:34px">{btn("Leave a Google review", B["review"], "btn-line", ext=True)}</div></div>
  </div>
</section>

<section class="sec" style="padding-bottom:clamp(60px,8vw,110px)">
  <div class="wrap"><div class="head rv"><div><p class="eyebrow">Happy customers</p><h2>Delivered with<br>a <em>smile.</em></h2></div><p class="lede">Real keys, real customers. A few recent handovers from our showroom.</p></div></div>
  <div class="hscroll"><div class="track">
    {"".join(f'<figure class="card"><div class="ph"><img src="assets/img/delivery-{f}.webp" alt="{e(n)} taking delivery of a {e(v)} from Sai Auto Consultant" loading="lazy"></div><figcaption><b>{e(n)}</b><span>{e(v)}</span></figcaption></figure>' for f,n,v in DELIVERIES)}
    <div class="card note"><p>Your handover could be next.</p>{btn("Follow on Instagram", B["insta"], "btn-light", ext=True)}</div>
  </div></div>
</section>

<section class="band sec">
  <div class="bg"><img src="assets/img/sedan-dark.webp" alt="" loading="lazy"></div>
  <div class="wrap">
    <p class="eyebrow rv">Stay protected</p>
    <h2 class="rv" style="margin-top:20px">Accidents don't come <em>with a warning.</em></h2>
    <p class="lede rv" style="margin-top:24px">From scooters to SUVs, trucks to autos, we insure every kind of vehicle at the lowest premiums. New policies, instant renewals and hassle-free claims.</p>
    <div class="ticks rv"><span>Two-wheelers</span><span>Cars &amp; SUVs</span><span>Trucks</span><span>Autos</span><span>Renewals</span><span>Claims</span></div>
    <div class="cta rv">{btn("Get an insurance quote", "visit.html#enquire", page=True)}{btn("WhatsApp Yash", WA_HELLO, "btn-line", ext=True)}</div>
  </div>
</section>

<div class="marq" aria-hidden="true"><div class="marq-in">{"".join(f"<span>{t}</span>" for t in ["New vehicles","Pre-owned","Insurance","RTO services","Two-wheelers","Four-wheelers"]*2)}</div></div>

<section class="sec">
  <div class="wrap split">
    <div class="frame rv"><img src="assets/img/office.webp" alt="Inside the Sai Auto Consultant office in Pandesara, Surat" loading="lazy"><span class="tag">Our office · Pandesara</span></div>
    <div class="rv">
      <p class="eyebrow">Find us in Surat</p>
      <h2 style="margin-block:20px 26px">Walk into<br>our <em>showroom.</em></h2>
      <div class="body-copy"><p><strong>Shop 16, Sukhsagar Residency,</strong> Near GIDC Pandesara, Laxmi Narayan Nagar, Pandesaragam, Udhana, Surat, Gujarat 394221.</p><p>Monday to Saturday, 10:00 AM onwards. No appointment needed.</p></div>
      <div class="cta" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:34px">{btn("Get directions", B["maps"], "btn-dark", ext=True)}{btn("Visit page", "visit.html", "btn-line", page=True)}</div>
    </div>
  </div>
</section>
''' + final("Let's find your <em>next ride.</em>", "Call us today or walk into our Surat showroom. No appointment needed.")

# ------------------------------------------------------------------ ABOUT
TIMELINE = [("1999","Sai Auto Consultant founded by Jignesh Solanki in Surat."),("2005","Expanded into four-wheeler sales and pre-owned vehicles."),
            ("2012","Launched full RTO documentation services for clients."),("2018","Added insurance advisory to the portfolio."),
            ("2022","Yash Solanki joins as Co-Owner and the digital transformation begins."),("2025","Serving thousands of happy customers across South Gujarat.")]
ABOUT = hero("sedan-road.webp", "Our story", ["<span data-years>27</span> years of wheels,", "trust &amp; <em>family.</em>"],
             "What started as one man's passion for automobiles has grown into Surat's most trusted multi-brand vehicle dealership.",
             btn("Meet the owners", "#owners") , short=True, pos="center 55%") + f'''
<section class="sec">
  <div class="wrap split">
    <div class="rv">
      <p class="eyebrow">Our journey</p>
      <h2 style="margin-block:20px 30px">Two generations.<br><em>One promise.</em></h2>
      <div class="body-copy">
        <p>Sai Auto Consultant was founded in 1999 by <strong>Jignesh Solanki</strong>, a man whose love for vehicles was matched only by his commitment to honest business. Over 25 years, a humble consulting practice grew into a full-service vehicle dealership serving thousands of customers across Surat and South Gujarat.</p>
        <p>Today his son <strong>Yash Solanki</strong> carries the legacy forward, bringing fresh energy, digital-first thinking and the same integrity that defined day one. Together they handle new vehicle sales, pre-owned buying and selling, insurance advisory and RTO documentation.</p>
        <p><strong>At Sai Auto Consultant, we don't just sell vehicles. We build relationships.</strong></p>
      </div>
    </div>
    <div class="frame rv"><img src="assets/img/office.webp" alt="The Sai Auto Consultant office" loading="lazy"><span class="tag">Est. 1999 · Surat</span></div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="head rv"><div><p class="eyebrow">Our values</p><h2>What <em>drives</em> us.</h2></div></div>
    <div class="values">
      <div class="rv"><span class="k">Honesty first</span><h3>Transparent pricing.</h3><p>No hidden charges. Always.</p></div>
      <div class="rv"><span class="k">People over profit</span><h3>Every client is family.</h3><p>We advise what's right, not what's expensive.</p></div>
      <div class="rv"><span class="k">End-to-end care</span><h3>With you every step.</h3><p>From the test ride to RC registration, we stay with you.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="owners">
  <div class="wrap">
    <div class="head rv"><div><p class="eyebrow">Meet the owners</p><h2>Family. Expertise.<br><em>Trust.</em></h2></div></div>
    {owners(long=True)}
  </div>
</section>

<section class="sec on-ink">
  <div class="wrap">
    <div class="head rv"><div><p class="eyebrow">Heritage</p><h2>Our journey<br>through the <em>years.</em></h2></div></div>
    <div class="tl"><div class="tl-fill"></div>
      {"".join(f'<div class="tl-item"><b>{y}</b><p>{t}</p></div>' for y,t in TIMELINE)}
    </div>
  </div>
</section>
''' + final("Come meet <em>the family.</em>", "Walk into our Pandesara showroom, Monday to Saturday from 10:00 AM.")

# ------------------------------------------------------------------ SERVICES
SVC = [("new","New vehicle sales","Browse the latest two-wheelers and four-wheelers from all major brands. Expert advice, best prices and seamless delivery.","sedan-road.webp","New Vehicle Purchase"),
       ("pre-owned","Buy old vehicles","Selling your old vehicle? We give fair, transparent market-price evaluations and instant purchase. No haggling, no hassle.","sedan-dark.webp","Sell My Vehicle"),
       ("second-hand","Sell second-hand vehicles","Looking for a quality pre-owned vehicle? Browse our curated inventory of certified used two-wheelers and four-wheelers.","sportbike.webp","Buy Used Vehicle"),
       ("two-wheelers","Two-wheeler specialist","Bikes, scooters and mopeds. All brands, all budgets. New or used, we have the right two-wheeler for you.","bike-red.webp","New Vehicle Purchase"),
       ("four-wheelers","Four-wheeler specialist","From hatchbacks to SUVs, we deal in all major car brands, new and pre-owned, with full documentation support.","suv-white.webp","New Vehicle Purchase"),
       ("insurance","Insurance services","New policy, renewal or claim assistance. We handle all vehicle insurance paperwork so you don't have to.","hero-sedan.webp","Insurance Help"),
       ("rto","RTO services","End-to-end RTO assistance: ownership transfers, NOC, RC renewal, fitness certificates and more.","rider-highway.webp","RTO Service")]
SERVICES = hero("sportbike.webp", "What we offer", ["Every vehicle service", "you'll <em>ever need.</em>"],
                "Two-wheelers, four-wheelers, new, old, insured, registered. We handle it all under one roof.",
                btn("Enquire now", "visit.html#enquire", page=True) + btn("Call Yash · 95122 80270", "tel:"+B["yash_tel"], "btn-line"),
                short=True, pos="center 60%") + f'''
<section class="sec">
  <div class="wrap">
    {"".join(f'<article class="svc rv" id="{k}"><div class="n">0{i}</div><div><h3>{t}</h3><p style="margin-top:18px">{d}</p><a class="link" data-page href="visit.html#enquire">Enquire now {ARR}</a></div><div class="thumb"><img src="assets/img/{img}" alt="" loading="lazy"></div></article>' for i,(k,t,d,img,_) in enumerate(SVC,1))}
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="head rv"><div><p class="eyebrow">Two ways to ride</p><h2>Pick your <em>wheels.</em></h2></div></div>
    <div class="duo">
      <a class="panel rv" data-page href="visit.html#enquire"><img src="assets/img/bike-red.webp" alt="A red sports motorcycle" loading="lazy"><p class="eyebrow" style="color:inherit">All brands · All models</p><h3>Two-wheelers</h3><p>Bikes, scooters and mopeds at the best prices. Find your perfect ride.</p><span class="link">Explore {ARR}</span></a>
      <a class="panel rv" data-page href="visit.html#enquire"><img src="assets/img/suv-white.webp" alt="A white SUV on a desert road" loading="lazy"><p class="eyebrow" style="color:inherit">New &amp; pre-owned</p><h3>Four-wheelers</h3><p>Hatchbacks, sedans and SUVs from all major brands, with complete documentation.</p><span class="link">Explore {ARR}</span></a>
    </div>
  </div>
</section>
''' + final("Ready to make <em>a move?</em>", "Call us today or walk into our Surat showroom. No appointment needed.")

# ------------------------------------------------------------------ VISIT
def visit(deploy):
    mapinner = (f'<iframe src="{B["maps_embed"]}" title="Map showing Sai Auto Consultant, Pandesara, Surat" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>' if deploy
                else '<img src="assets/img/rider-highway.webp" alt="">')
    pin = "" if deploy else f'<div class="pinwrap"><span class="coord">21.1449° N · 72.8347° E</span><h3 style="font-size:clamp(34px,3.6vw,52px)">Pandesara, Udhana,<br><em>Surat 394221</em></h3><div>{btn("Open in Google Maps", B["maps"], "btn-light", ext=True)}</div></div>'
    return hero("storefront.webp" if False else "sedan-dark.webp", "Find us", ["Come visit Surat's", "most trusted <em>auto consultant.</em>"],
                "Our showroom in Udhana, Surat is open six days a week. Walk in, no appointment needed.",
                btn("Get directions", B["maps"], ext=True) + btn("Send an enquiry", "#enquire", "btn-line"), short=True) + f'''
<section class="sec tight">
  <div class="wrap">
    <div class="info-grid">
      <div class="info rv"><span class="k">Our location</span><address>Shop 16, Sukhsagar Residency,<br>Near GIDC Pandesara,<br>Laxmi Narayan Nagar, Pandesaragam,<br>Udhana, Surat, Gujarat 394221</address><div class="push">{btn("Open in Google Maps", B["maps"], "btn-dark", ext=True)}</div></div>
      <div class="info rv"><span class="k">Call us</span><div class="ppl"><div><b>Jignesh Solanki</b><a href="tel:{B["jignesh_tel"]}">{B["jignesh"]}</a></div><div><b>Yash Solanki</b><a href="tel:{B["yash_tel"]}">{B["yash"]}</a></div></div><div class="push">{btn("Chat on WhatsApp", WA_HELLO, "btn-dark", ext=True)}</div></div>
      <div class="info rv"><span class="k">Working hours</span><p class="big">Monday – Saturday<br><em>10:00 AM onwards</em></p><p style="color:var(--mute)">Sunday closed</p></div>
    </div>
    <div class="mapbox rv" style="margin-top:clamp(16px,2vw,24px)">{mapinner}{pin}</div>
  </div>
</section>

<section class="sec alt" id="enquire">
  <div class="wrap split">
    <div class="rv">
      <p class="eyebrow">Send an enquiry</p>
      <h2 style="margin-block:20px 26px">Tell us how<br>we can <em>help.</em></h2>
      <p class="lede">Fill this in and we'll turn it into a WhatsApp message to Yash. We usually reply within minutes.</p>
      <div class="frame wide" style="margin-top:40px"><img src="assets/img/delivery-anil-singh-tata-nexon.webp" alt="A Sai Auto Consultant customer taking delivery of a Tata Nexon" loading="lazy"><span class="tag">A recent handover</span></div>
    </div>
    <form class="enq rv" id="enquiry" novalidate>
      <div class="two">
        <label class="fld" for="f-name"><input id="f-name" name="name" placeholder=" " autocomplete="name" required><span>Full name *</span></label>
        <label class="fld" for="f-phone"><input id="f-phone" name="phone" type="tel" inputmode="tel" placeholder=" " autocomplete="tel" required><span>Phone number *</span></label>
      </div>
      <label class="fld" for="f-email"><input id="f-email" name="email" type="email" placeholder=" " autocomplete="email"><span>Email address</span></label>
      <label class="fld static" for="f-interest"><select id="f-interest" name="interest"><option>New Vehicle Purchase</option><option>Sell My Vehicle</option><option>Buy Used Vehicle</option><option>Insurance Help</option><option>RTO Service</option><option>General Enquiry</option></select><span>I'm interested in *</span></label>
      <fieldset style="border:0;padding:0;margin:0"><legend class="eyebrow" style="margin-bottom:12px">Vehicle type</legend>
        <div class="chips"><label for="vt1"><input type="radio" id="vt1" name="vtype" value="Two-Wheeler" checked><span>Two-wheeler</span></label><label for="vt2"><input type="radio" id="vt2" name="vtype" value="Four-Wheeler"><span>Four-wheeler</span></label><label for="vt3"><input type="radio" id="vt3" name="vtype" value="Both"><span>Both</span></label></div></fieldset>
      <label class="fld" for="f-msg"><textarea id="f-msg" name="message" placeholder=" " rows="3"></textarea><span>Message</span></label>
      <div class="err" id="enq-err" role="alert"></div>
      <div>{'<button class="btn btn-dark" type="submit"><span>Prepare my enquiry</span><span class="ar">'+ARR+ARR+'</span></button>'}</div>
      <div class="ready" id="enq-ready" hidden><pre id="enq-text"></pre><div class="cta"><a class="btn btn-dark btn-plain" id="enq-wa" href="#" target="_blank" rel="noopener">Send on WhatsApp</a><button class="btn btn-line btn-plain" type="button" id="enq-copy">Copy message</button></div></div>
    </form>
  </div>
</section>

<section class="sec on-ink">
  <div class="wrap split rev">
    <div class="frame wide rv"><img src="assets/img/delivery-sunil-mistry-royal-enfield.webp" alt="Royal Enfield delivery at Sai Auto Consultant" loading="lazy"></div>
    <div class="rv"><p class="eyebrow">Catch us on Instagram</p><h2 style="margin-block:20px 26px">Our showroom,<br><em>your feed.</em></h2><p class="lede">New arrivals, happy customers, behind-the-scenes and exclusive deals.</p><div style="margin-top:34px">{btn("Follow @sai.auto.consultant", B["insta"], ext=True)}</div></div>
  </div>
</section>
'''

# ------------------------------------------------------------------ SEO + assembly
PAGES = {
  "home": ("index.html", "", "Sai Auto Consultant | Vehicle Dealer in Surat Since 1999 | New & Used Bikes, Cars, Insurance, RTO",
           "Sai Auto Consultant, Pandesara, Surat: new and pre-owned two-wheelers and four-wheelers, vehicle insurance and RTO services since 1999. Call Jignesh +91 98252 43838.", lambda d: HOME),
  "about": ("about.html", "about.html", "About Us | Sai Auto Consultant, Surat | Family Vehicle Dealer Since 1999",
            "Founded in 1999 by Jignesh Solanki and now run with his son Yash, Sai Auto Consultant is Surat's trusted family vehicle dealership.", lambda d: ABOUT),
  "services": ("services.html", "services.html", "Our Services | Buy, Sell, Insurance & RTO for Bikes and Cars | Sai Auto Consultant Surat",
               "New vehicle sales, used bike and car buying and selling, two- and four-wheeler specialists, vehicle insurance and RTO services in Surat.", lambda d: SERVICES),
  "visit": ("visit.html", "visit.html", "Visit Us | Sai Auto Consultant Showroom, Pandesara, Udhana, Surat",
            "Shop 16, Sukhsagar Residency, Near GIDC Pandesara, Udhana, Surat 394221. Open Monday to Saturday from 10:00 AM. Call +91 98252 43838.", visit),
}

def ld(key, url):
    biz = {"@context":"https://schema.org","@type":"AutoDealer","@id":SITE_URL+"/#business","name":B["name"],"legalName":B["legal"],
      "url":SITE_URL+"/","logo":SITE_URL+"/assets/img/logo.png","image":[SITE_URL+"/assets/img/office.webp",SITE_URL+"/assets/img/storefront.webp"],
      "description":PAGES["home"][3],"foundingDate":"1999",
      "founder":{"@type":"Person","name":"Jignesh Solanki"},"employee":[{"@type":"Person","name":"Jignesh Solanki","jobTitle":"Founder & Senior Consultant"},{"@type":"Person","name":"Yash Solanki","jobTitle":"Co-Owner & Operations Head"}],
      "telephone":B["jignesh_tel"],"contactPoint":[{"@type":"ContactPoint","telephone":B["jignesh_tel"],"contactType":"sales","name":"Jignesh Solanki","areaServed":"IN","availableLanguage":["en","gu","hi"]},{"@type":"ContactPoint","telephone":B["yash_tel"],"contactType":"customer service","name":"Yash Solanki","areaServed":"IN","availableLanguage":["en","gu","hi"]}],
      "address":{"@type":"PostalAddress","streetAddress":"Shop 16, Sukhsagar Residency, Near GIDC Pandesara, Laxmi Narayan Nagar, Pandesaragam","addressLocality":"Udhana, Surat","addressRegion":"Gujarat","postalCode":"394221","addressCountry":"IN"},
      "geo":{"@type":"GeoCoordinates","latitude":B["lat"],"longitude":B["lng"]},"hasMap":B["maps"],
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00"}],
      "areaServed":[{"@type":"City","name":"Surat"},{"@type":"AdministrativeArea","name":"South Gujarat"}],
      "sameAs":[B["insta"]],"priceRange":"₹₹",
      "hasOfferCatalog":{"@type":"OfferCatalog","name":"Vehicle services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":s[1]}} for s in SVC]}}
    out=[biz]
    if key!="home":
        out.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE_URL+"/"},{"@type":"ListItem","position":2,"name":PAGES[key][2].split(" | ")[0],"item":url}]})
    return "".join(f'<script type="application/ld+json">{json.dumps(o,ensure_ascii=False)}</script>\n' for o in out)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600&family=IBM+Plex+Mono:wght@500&family=Instrument+Serif:ital@0;1&display=swap">'
BOOT = "<script>(function(){var d=document.documentElement;d.classList.add('js');try{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;if(sessionStorage.getItem('sai-pt')==='1'){d.classList.add('pt');sessionStorage.removeItem('sai-pt')}else if(sessionStorage.getItem('sai-intro')!=='1'){d.classList.add('intro')}}catch(e){}})()</script>"
SCRIPTS = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>\n'
           '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>\n'
           '<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>\n'
           '<script src="assets/main.js"></script>')

def page(key, mode):
    fname, path, title, desc, body = PAGES[key]
    url = SITE_URL + "/" + path
    content = header(key) + "\n<main>" + body(mode=="deploy") + "</main>\n" + footer() + "\n" + SCRIPTS
    if mode == "artifact-main":
        return (f'<title>Sai Auto Consultant</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
                f'<meta name="description" content="{e(desc)}">\n{FONTS}\n<link rel="stylesheet" href="assets/styles.css">\n{BOOT}\n{content}\n')
    seo = ""
    if mode == "deploy":
        seo = (f'<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{url}">\n'
               '<meta name="robots" content="index, follow, max-image-preview:large">\n<meta name="theme-color" content="#131518">\n'
               f'<meta name="geo.region" content="IN-GJ"><meta name="geo.placename" content="Surat"><meta name="geo.position" content="{B["lat"]};{B["lng"]}"><meta name="ICBM" content="{B["lat"]}, {B["lng"]}">\n'
               f'<meta property="og:type" content="website"><meta property="og:site_name" content="Sai Auto Consultant"><meta property="og:locale" content="en_IN">\n'
               f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">\n'
               f'<meta property="og:image" content="{SITE_URL}/assets/img/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">\n'
               f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{SITE_URL}/assets/img/og-image.jpg">\n'
               '<link rel="icon" type="image/png" href="assets/img/logo.png"><link rel="apple-touch-icon" href="assets/img/logo.png">\n'
               '<link rel="preload" as="image" href="assets/img/' + {"home":"hero-sedan","about":"sedan-road","services":"sportbike","visit":"sedan-dark"}[key] + '.webp">\n'
               + ld(key, url))
    else:
        seo = f'<meta name="description" content="{e(desc)}">\n'
    return (f'<!doctype html>\n<html lang="en-IN">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{e(title)}</title>\n{seo}{FONTS}\n<link rel="stylesheet" href="assets/styles.css">\n{BOOT}\n</head>\n<body>\n{content}\n</body>\n</html>\n')

for out, mode_main in (("dist","deploy"),("preview","artifact")):
    d = ROOT/out
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(ROOT/"assets", d/"assets")
    for key,(fname,*_) in PAGES.items():
        mode = "deploy" if out=="dist" else ("artifact-main" if key=="home" else "artifact")
        (d/fname).write_text(page(key, mode), encoding="utf-8")

(ROOT/"dist/robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
(ROOT/"dist/sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f'  <url><loc>{SITE_URL}/{p[1]}</loc><changefreq>monthly</changefreq><priority>{"1.0" if k=="home" else "0.8"}</priority></url>\n' for k,p in PAGES.items()) + "</urlset>\n")
shutil.copy(ROOT/"_headers", ROOT/"dist/_headers")
(ROOT/"dist/vercel.json").write_text(json.dumps({"cleanUrls":True,"trailingSlash":False,
  "headers":[{"source":"/assets/img/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=2592000"}]}]},indent=2))
print("Built dist/ and preview/")
