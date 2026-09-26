const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-btn');
const navLinks = document.querySelector('.nav-links');
const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 18);
updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });
menuButton?.addEventListener('click', () => { const open = navLinks?.classList.toggle('open'); menuButton.setAttribute('aria-expanded', String(Boolean(open))); });
navLinks?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { navLinks.classList.remove('open'); menuButton?.setAttribute('aria-expanded', 'false'); }));
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduced && 'IntersectionObserver' in window) { const observer = new IntersectionObserver(entries => { entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('in'); observer.unobserve(entry.target); } }); }, { threshold: 0.12 }); document.querySelectorAll('.reveal').forEach(el => observer.observe(el)); } else { document.querySelectorAll('.reveal').forEach(el => el.classList.add('in')); }
document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });


// Google Analytics 4 — loaded only after explicit visitor consent.
(() => {
  const GA_MEASUREMENT_ID = 'G-6072C87BK0';
  const CONSENT_KEY = 'drdlamini-analytics-consent';
  const banner = document.querySelector('[data-cookie-banner]');
  const acceptButton = document.querySelector('[data-cookie-accept]');
  const declineButton = document.querySelector('[data-cookie-decline]');
  const preferenceButtons = document.querySelectorAll('[data-cookie-preferences]');
  let analyticsLoaded = false;

  const loadAnalytics = () => {
    if (analyticsLoaded || document.querySelector('script[data-ga4]')) return;
    analyticsLoaded = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_MEASUREMENT_ID, {
      anonymize_ip: true
    });

    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_MEASUREMENT_ID);
    script.dataset.ga4 = 'true';
    document.head.appendChild(script);
  };

  const showBanner = () => {
    if (!banner) return;
    banner.hidden = false;
    acceptButton?.focus({ preventScroll: true });
  };

  const hideBanner = () => {
    if (banner) banner.hidden = true;
  };

  const savePreference = (value) => {
    try { localStorage.setItem(CONSENT_KEY, value); } catch (error) {}
  };

  const readPreference = () => {
    try { return localStorage.getItem(CONSENT_KEY); } catch (error) { return null; }
  };

  const setPreference = (value) => {
    savePreference(value);
    if (value === 'granted') loadAnalytics();
    hideBanner();
  };

  acceptButton?.addEventListener('click', () => setPreference('granted'));
  declineButton?.addEventListener('click', () => setPreference('denied'));

  preferenceButtons.forEach(button => button.addEventListener('click', () => {
    showBanner();
  }));

  const savedPreference = readPreference();
  if (savedPreference === 'granted') {
    loadAnalytics();
  } else if (savedPreference !== 'denied') {
    showBanner();
  }
})();
