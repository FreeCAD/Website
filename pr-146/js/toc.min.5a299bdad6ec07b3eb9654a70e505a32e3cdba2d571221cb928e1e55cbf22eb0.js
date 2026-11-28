/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/document.addEventListener("DOMContentLoaded",()=>{const e=document.querySelectorAll("#TableOfContents a");if(!e.length)return;const n=Array.from(e).map(e=>document.getElementById(e.getAttribute("href").slice(1))).filter(Boolean),s=new Map(Array.from(e).map(e=>[e.getAttribute("href").slice(1),e]));let t=null;const o=new IntersectionObserver(n=>{if(n.forEach(e=>{e.isIntersecting&&(t=e.target.id)}),t){e.forEach(e=>e.classList.remove("toc-active"));const n=s.get(t);n&&n.classList.add("toc-active")}},{rootMargin:"-60px 0px -60% 0px",threshold:.1});n.forEach(e=>o.observe(e))})