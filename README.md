# Sai Auto Consultant website

Website for Sai Auto Consultant, Pandesara, Surat (est. 1999): new and pre-owned two-wheelers and four-wheelers, vehicle insurance and RTO services.

Pages: Home, About Us, Our Services, Visit Us.

## Edit and rebuild

Page content lives in `build.py`, styles in `assets/styles.css` and animations in `assets/main.js`.

```bash
python3 build.py
```

This writes the finished website to `dist/` (and a preview copy to `preview/`, which is not committed).
Set `SITE_URL` in `build.py` to the live domain so the SEO tags and sitemap point to it.

## Deploy on Vercel

Import this repository in Vercel and set **Root Directory** to `dist`. No build command is needed.
