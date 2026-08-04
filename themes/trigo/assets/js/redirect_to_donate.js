/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Redirect to Donate page:
*/


const DONATE_PAGE = '{{ with (site.GetPage "donate") }}{{ .RelPermalink }}{{ else }}#{{ end }}';

document.querySelectorAll('.link-donate').forEach(link => {
  link.addEventListener('click', () => {
    setTimeout(() => {
      window.location.assign(DONATE_PAGE);
    }, 1500);
  });
});