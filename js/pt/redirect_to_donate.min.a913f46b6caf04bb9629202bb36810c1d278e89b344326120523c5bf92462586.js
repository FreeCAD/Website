/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/const DONATE_PAGE="/Website/pt/donate/";document.querySelectorAll(".link-donate").forEach(e=>{e.addEventListener("click",()=>{setTimeout(()=>{window.location.assign(DONATE_PAGE)},1500)})})