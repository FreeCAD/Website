/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Automatically open <details> elements for navigation:
- Support direct links (e.g. #section-id).
- Handle page load and hash changes.
*/


// Open details element with current URL hash match.
const openTargetDetails = () => {
  if (!location.hash) return;

  const id = location.hash.slice(1);
  if (!id) return;
  const decoded = decodeURIComponent(id);
  const el = document.getElementById(decoded);

  // Only open with details target.
  if (el instanceof HTMLDetailsElement) {
    el.open = true;
    el.scrollIntoView({ block: 'start' });
  }
};

// Run on initial page load.
document.addEventListener('DOMContentLoaded', openTargetDetails);

// Run with hash change (e.g. in-page navigation).
window.addEventListener('hashchange', openTargetDetails);