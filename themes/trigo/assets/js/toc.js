/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Table of Contents position highlight:
- Automatically add .toc-active class to headings based on content seen by user.
*/


document.addEventListener("DOMContentLoaded", () => {
  const tocLinks = document.querySelectorAll('#TableOfContents a');
  if (!tocLinks.length) return;

  const headings = Array.from(tocLinks)
    .map(link => document.getElementById(link.getAttribute("href").slice(1)))
    .filter(Boolean);

  const linkMap = new Map(
    Array.from(tocLinks).map(link => [link.getAttribute("href").slice(1), link])
  );

  let activeId = null;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          activeId = entry.target.id;
        }
      });

      if (activeId) {
        tocLinks.forEach(link => link.classList.remove("toc-active"));
        const activeLink = linkMap.get(activeId);
        if (activeLink) activeLink.classList.add("toc-active");
      }
    },
    // trigger when heading enters upper viewport
    {
      rootMargin: "-60px 0px -60% 0px", // do not count sticky header height
      threshold: 0.1
    }
  );

  headings.forEach(h => observer.observe(h));
});