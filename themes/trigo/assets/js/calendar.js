/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Calendar skin toggle script on Community:
- Change Open Web Calendar skin on theme chroma-toggle.
*/


function updateCalendarSkin() {
  const iframe = document.getElementById('open-web-calendar');
  if (!iframe) return;

  const isDark = document.documentElement.classList.contains('dark');
  const skin = isDark ? 'dark' : 'terrace';

  const url = new URL(iframe.src);
  url.searchParams.set('skin', skin);

  const newSrc = url.toString();
  if (iframe.src !== newSrc) {
    iframe.src = newSrc;
  }
}

document.addEventListener('DOMContentLoaded', updateCalendarSkin);

const observer = new MutationObserver(updateCalendarSkin);

observer.observe(document.documentElement, {
  attributes: true,
  attributeFilter: ['class']
});