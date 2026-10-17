# drdlamini.com — GitHub Pages

A dependency-free, responsive personal leadership/speaking site for Dr. Geqigula Dlamini. The site is intentionally plain HTML/CSS/JavaScript so it is fast, easy to edit, and does not depend on a framework or package manager.

## Current structure
- `index.html` — the primary single-page experience with About, Work, Research, Speaking and Contact sections
- `404.html` — custom error page

The previous standalone About, Speaking and Research pages were intentionally removed to keep the site simple. Their essential content now lives on the homepage.

## GitHub deployment
GitHub Pages is configured through the included `.github/workflows/deploy.yml` workflow and publishes from `main`.

`CNAME` is set to `drdlamini.com`.

## Primary CTA
Speaking and collaboration inquiries use:
`mailto:gq@drdlamini.com`

## External links
- LinkedIn: https://www.linkedin.com/in/gdlamini
- Deeply Optimistic: https://deeplyoptimistic.com/
- Dissertation: https://scholarlycommons.pacific.edu/uop_etds/4322/
- YouTube: https://www.youtube.com/watch?v=AJW-Kt0LcdU

## Design principles
- Executive and human, not startup-techy.
- Most visitor needs should be met on the homepage.
- Research supports the broader leadership story rather than defining the whole site.
- Mobile-first navigation and accessible focus behavior.
- Minimal JavaScript and reduced-motion support.
- GA4 (G-6072C87BK0) loads only after analytics consent. Visitors can manage preferences in the footer.
- The Pages build generates `assets/dr-dlamini-speaker-one-sheet.pdf` from `scripts/generate_speaker_one_sheet.py` before deployment.
