/*
 * MD Service Trans — Cookie-Consent-Manager
 * TTDSG §25 / DSGVO-konform: Opt-in, gleichwertige Buttons, granulare Kategorien,
 * jederzeit widerrufbar, nichts Nicht-Notwendiges lädt vor Zustimmung.
 *
 * Nutzung für künftige Integrationen (Google Analytics, Maps, Google-Bewertungen-Widget,
 * Meta-Pixel etc.):
 *   window.cookieConsent.onConsentChange(function (consent) {
 *     if (consent.statistics) { / * z. B. GA-Skript hier laden * / }
 *     if (consent.external)   { / * z. B. Google Maps / Bewertungen-Embed laden * / }
 *     if (consent.marketing)  { / * z. B. Meta-Pixel hier laden * / }
 *   });
 * Der Callback wird sofort beim Registrieren aufgerufen (falls bereits eine
 * Entscheidung vorliegt) und erneut bei jeder Änderung der Einstellungen.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'mdst_cookie_consent_v1';
  var listeners = [];

  var CATEGORIES = [
    {
      key: 'necessary',
      title: 'Technisch notwendig',
      locked: true,
      description: 'Für den Betrieb der Website erforderlich (z. B. Speicherung Ihrer Cookie-Auswahl). Kann nicht deaktiviert werden.'
    },
    {
      key: 'statistics',
      title: 'Statistik',
      locked: false,
      description: 'Hilft uns zu verstehen, wie die Website genutzt wird (z. B. Google Analytics). Wird nur mit Ihrer Zustimmung geladen.'
    },
    {
      key: 'external',
      title: 'Externe Inhalte (Karten, Bewertungen)',
      locked: false,
      description: 'Einbettung z. B. einer Google-Karte oder unseres Google-Bewertungen-Widgets. Dabei kann Ihre IP-Adresse an Google übertragen werden.'
    },
    {
      key: 'marketing',
      title: 'Marketing',
      locked: false,
      description: 'Für Werbe- und Reichweitenmessung (z. B. Meta/Facebook-Pixel). Wird nur mit Ihrer Zustimmung geladen.'
    }
  ];

  function readConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (typeof parsed !== 'object' || parsed === null) return null;
      return parsed;
    } catch (e) {
      return null;
    }
  }

  function writeConsent(consent) {
    consent.necessary = true;
    consent.timestamp = new Date().toISOString();
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(consent));
    } catch (e) { /* localStorage nicht verfügbar — Banner erscheint dann bei jedem Besuch erneut */ }
    listeners.forEach(function (cb) { cb(consent); });
  }

  function allOf(value) {
    var c = { necessary: true };
    CATEGORIES.forEach(function (cat) { if (!cat.locked) c[cat.key] = value; });
    return c;
  }

  // ---- UI ----

  var root, banner, modal, lastFocused;

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      if (k === 'text') node.textContent = attrs[k];
      else if (k === 'html') node.innerHTML = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) node.appendChild(c); });
    return node;
  }

  function buildBanner() {
    var text = el('p', { class: 'cc-text' },
      [document.createTextNode(
        'Wir verwenden nur technisch notwendige Cookies. Sobald wir Statistik-, Karten- oder Marketing-Dienste einbinden, entscheiden Sie hier, was Sie erlauben. Details in unserer ')]
    );
    var link = el('a', { href: 'datenschutz.html', class: 'cc-link', text: 'Datenschutzerklärung' });
    text.appendChild(link);
    text.appendChild(document.createTextNode('.'));

    var btnReject = el('button', { type: 'button', class: 'btn btn-outline-navy cc-btn' , text: 'Nur notwendige'});
    var btnSettings = el('button', { type: 'button', class: 'btn btn-outline-navy cc-btn', text: 'Einstellungen' });
    var btnAccept = el('button', { type: 'button', class: 'btn btn-primary cc-btn', text: 'Alle akzeptieren' });

    btnReject.addEventListener('click', function () { writeConsent(allOf(false)); hideBanner(); });
    btnAccept.addEventListener('click', function () { writeConsent(allOf(true)); hideBanner(); });
    btnSettings.addEventListener('click', openSettings);

    var actions = el('div', { class: 'cc-actions' }, [btnReject, btnSettings, btnAccept]);
    return el('div', { class: 'cc-banner', role: 'dialog', 'aria-live': 'polite', 'aria-label': 'Cookie-Hinweis', id: 'cookie-banner' }, [text, actions]);
  }

  function buildModal() {
    var overlay = el('div', { class: 'cc-overlay', id: 'cookie-modal-overlay' });
    var dialog = el('div', {
      class: 'cc-modal', role: 'dialog', 'aria-modal': 'true',
      'aria-labelledby': 'cc-modal-title', id: 'cookie-modal'
    });

    var closeBtn = el('button', { type: 'button', class: 'cc-close', 'aria-label': 'Schließen' });
    closeBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';
    closeBtn.addEventListener('click', closeSettings);

    var title = el('h3', { id: 'cc-modal-title', text: 'Cookie-Einstellungen' });
    var intro = el('p', { class: 'cc-text', text: 'Wählen Sie aus, welche Kategorien Sie zulassen möchten. Notwendige Cookies sind immer aktiv.' });

    var list = el('div', { class: 'cc-categories' });
    var current = readConsent() || allOf(false);

    CATEGORIES.forEach(function (cat) {
      var row = el('div', { class: 'cc-category' });
      var head = el('div', { class: 'cc-category-head' });
      var label = el('label', { class: 'cc-switch-label', for: 'cc-toggle-' + cat.key });
      var input = el('input', { type: 'checkbox', id: 'cc-toggle-' + cat.key, class: 'cc-switch-input' });
      input.checked = cat.locked ? true : !!current[cat.key];
      if (cat.locked) input.disabled = true;
      var switchSpan = el('span', { class: 'cc-switch', 'aria-hidden': 'true' });
      var titleSpan = el('span', { class: 'cc-category-title', text: cat.title });
      label.appendChild(input);
      label.appendChild(switchSpan);
      label.appendChild(titleSpan);
      head.appendChild(label);
      row.appendChild(head);
      row.appendChild(el('p', { class: 'cc-category-desc', text: cat.description }));
      row.dataset.key = cat.key;
      list.appendChild(row);
    });

    var btnRejectAll = el('button', { type: 'button', class: 'btn btn-outline-navy cc-btn', text: 'Nur notwendige' });
    var btnSave = el('button', { type: 'button', class: 'btn btn-outline-navy cc-btn', text: 'Auswahl speichern' });
    var btnAcceptAll = el('button', { type: 'button', class: 'btn btn-primary cc-btn', text: 'Alle akzeptieren' });

    btnRejectAll.addEventListener('click', function () { writeConsent(allOf(false)); closeSettings(); hideBanner(); });
    btnAcceptAll.addEventListener('click', function () { writeConsent(allOf(true)); closeSettings(); hideBanner(); });
    btnSave.addEventListener('click', function () {
      var consent = { necessary: true };
      CATEGORIES.forEach(function (cat) {
        if (cat.locked) { consent[cat.key] = true; return; }
        var input = document.getElementById('cc-toggle-' + cat.key);
        consent[cat.key] = !!(input && input.checked);
      });
      writeConsent(consent);
      closeSettings();
      hideBanner();
    });

    var actions = el('div', { class: 'cc-actions cc-modal-actions' }, [btnRejectAll, btnSave, btnAcceptAll]);

    dialog.appendChild(closeBtn);
    dialog.appendChild(title);
    dialog.appendChild(intro);
    dialog.appendChild(list);
    dialog.appendChild(actions);
    overlay.appendChild(dialog);

    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeSettings(); });
    dialog.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeSettings(); return; }
      if (e.key === 'Tab') trapFocus(e, dialog);
    });

    return overlay;
  }

  function trapFocus(e, container) {
    var focusable = container.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    if (!focusable.length) return;
    var first = focusable[0], last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  function showBanner() {
    if (!banner) return;
    banner.classList.add('cc-visible');
  }
  function hideBanner() {
    if (!banner) return;
    banner.classList.remove('cc-visible');
  }

  function openSettings() {
    lastFocused = document.activeElement;
    modal.classList.add('cc-visible');
    document.body.classList.add('cc-modal-open');
    var firstFocusable = modal.querySelector('.cc-close');
    if (firstFocusable) firstFocusable.focus();
  }
  function closeSettings() {
    modal.classList.remove('cc-visible');
    document.body.classList.remove('cc-modal-open');
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  function init() {
    root = el('div', { class: 'cc-root' });
    banner = buildBanner();
    modal = buildModal();
    root.appendChild(banner);
    root.appendChild(modal);
    document.body.appendChild(root);

    var existing = readConsent();
    if (!existing) {
      showBanner();
    } else {
      listeners.forEach(function (cb) { cb(existing); });
    }

    // Reopen link (e.g. footer "Cookie-Einstellungen")
    document.querySelectorAll('[data-cookie-settings]').forEach(function (btn) {
      btn.addEventListener('click', function (e) { e.preventDefault(); openSettings(); });
    });
  }

  window.cookieConsent = {
    getConsent: readConsent,
    onConsentChange: function (cb) {
      listeners.push(cb);
      var existing = readConsent();
      if (existing) cb(existing);
    },
    openSettings: function () {
      if (!modal) { document.addEventListener('DOMContentLoaded', function () { openSettings(); }); }
      else openSettings();
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
