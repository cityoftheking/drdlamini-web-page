# drdlamini.com — GitHub Pages V1

A dependency-free, responsive personal leadership/speaking site for Dr. Geqigula Dlamini. It is intentionally plain HTML/CSS/JavaScript so the site is fast, easy to edit, and does not depend on a framework or package manager.

## Pages
- `index.html` — home / positioning
- `about.html` — biography and leadership philosophy
- `speaking.html` — speaking themes, featured keynote, YouTube embed
- `research.html` — dissertation and human-centered AI research
- `404.html` — custom error page

## Before launch
1. Follow `ASSET-MAP.md` and add the final photography/logo.
2. Search the repository for `hero-portrait.svg`, `speaking-stage.svg`, and `journey.svg` to confirm the fallbacks can remain.
3. If you add a public resume PDF, place it at `assets/docs/GQ-Dlamini-Resume.pdf` and add a link where desired. Avoid publishing a home address or private phone number in a public PDF.

## GitHub deployment
1. In **Settings → Pages**, set **Source** to **GitHub Actions**.
2. Push to `main`. The included `.github/workflows/deploy.yml` will publish the site.
3. In **Settings → Pages → Custom domain**, enter `drdlamini.com`.
4. Configure the DNS at your domain provider using GitHub Pages' current custom-domain instructions, then enable **Enforce HTTPS** after the certificate is issued.

`CNAME` is already set to `drdlamini.com`.

## Primary CTA
Every primary booking CTA uses:
`mailto:g_dlamini@u.pacific.edu`

## External links
- LinkedIn: https://www.linkedin.com/in/gdlamini
- Deeply Optimistic: https://deeplyoptimistic.com/
- Dissertation: https://scholarlycommons.pacific.edu/uop_etds/4322/
- YouTube: https://www.youtube.com/watch?v=AJW-Kt0LcdU

## Design principles
- Executive and human, not startup-techy.
- Research as evidence of breadth—not the entire identity.
- Mobile-first navigation and accessible focus behavior.
- Minimal JavaScript and reduced-motion support.
- No analytics or third-party tracking included by default.
