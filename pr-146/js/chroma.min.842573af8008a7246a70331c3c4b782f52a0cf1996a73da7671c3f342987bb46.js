/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/document.addEventListener("DOMContentLoaded",function(){const e=document.getElementById("chroma-toggle");if(!e)return;e.addEventListener("click",()=>{const e=document.documentElement.classList.toggle("dark");localStorage.setItem("pref-theme",e?"dark":"light")})})