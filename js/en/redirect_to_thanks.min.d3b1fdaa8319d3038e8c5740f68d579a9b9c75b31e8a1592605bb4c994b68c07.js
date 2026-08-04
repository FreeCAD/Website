/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/const THANKS_PAGE="/Website/donate/thanks/";document.querySelectorAll(".link-thanks").forEach(e=>{e.addEventListener("click",()=>{setTimeout(()=>{window.location.assign(THANKS_PAGE)},1500)})})