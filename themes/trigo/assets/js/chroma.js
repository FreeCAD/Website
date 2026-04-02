/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Theme Chroma toggle:
- Toggle .dark class on chroma-toggle button click.
- Save preference to localStorage.
*/


document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("chroma-toggle");
  if (!button) return;

  button.addEventListener("click", () => {
    const dark = document.documentElement.classList.toggle("dark");
    localStorage.setItem("pref-theme", dark ? "dark" : "light");
  });
});