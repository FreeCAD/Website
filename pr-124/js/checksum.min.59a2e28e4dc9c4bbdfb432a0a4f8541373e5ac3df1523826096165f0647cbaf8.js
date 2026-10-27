/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/document.querySelectorAll(".checksum-button").forEach(e=>{e.addEventListener("click",async t=>{t.preventDefault();try{await navigator.clipboard.writeText(e.dataset.sha256),e.classList.add("copied"),setTimeout(()=>{e.classList.remove("copied")},1500)}catch(e){console.warn("Failed to copy checksum:",e)}})})