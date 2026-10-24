# Nice Top® Abrasives — B2B Independent Site

Static B2B inquiry-type website for Tianjin Pengyu New Material Co., Ltd.
(Nice Top® non-woven abrasive wheels), deployed with GitHub Pages.

- 72 pages: home, products hub, 7 category pages, 60 product detail pages,
  applications, about, contact (inquiry form), sitemap.xml
- Pure static HTML + CSS + JS — no build step, no server needed
- To rebuild after editing content: edit `src/products.json`, then run
  `python3 src/build.py`

## Before production launch

1. Replace the 4 SVG placeholder images in `assets/img/` with real
   factory/product photos.
2. Wire the inquiry form in `contact.html` to a real endpoint (e.g. Formspree).
3. Set the real domain in `src/build.py` (`SITE_URL`) and rebuild so
   `sitemap.xml` is correct.
4. Submit `sitemap.xml` to Google Search Console.
