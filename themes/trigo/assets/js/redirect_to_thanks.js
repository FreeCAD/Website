/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Redirect to Thanks page:
*/


const thanks = '{{ with (site.GetPage "thanks") }}{{ .RelPermalink }}{{ else }}#{{ end }}';

document.querySelectorAll('.link-thanks').forEach(link => {
  link.addEventListener('click', () => {
    setTimeout(() => {
      window.location.assign(thanks);
    }, 1500);
  });
});