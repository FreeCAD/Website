/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/function updateCalendarSkin(){const e=document.getElementById("open-web-calendar");if(!e)return;const s=document.documentElement.classList.contains("dark"),o=s?"dark":"terrace",t=new URL(e.src);t.searchParams.set("skin",o);const n=t.toString();e.src!==n&&(e.src=n)}document.addEventListener("DOMContentLoaded",updateCalendarSkin);const observer=new MutationObserver(updateCalendarSkin);observer.observe(document.documentElement,{attributes:!0,attributeFilter:["class"]})