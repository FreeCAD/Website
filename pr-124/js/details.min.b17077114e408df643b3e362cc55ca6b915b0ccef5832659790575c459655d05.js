/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/const openTargetDetails=()=>{if(!location.hash)return;const t=location.hash.slice(1);if(!t)return;const n=decodeURIComponent(t),e=document.getElementById(n);e instanceof HTMLDetailsElement&&(e.open=!0,e.scrollIntoView({block:"start"}))};document.addEventListener("DOMContentLoaded",openTargetDetails),window.addEventListener("hashchange",openTargetDetails)