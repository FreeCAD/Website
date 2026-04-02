/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
Copy to clipboard button for code blocks:
- Display and update button text after copy.
- Handle different generated markup (highlight, tables).
*/


// Button labels with Hugo i18n at build time.
const LABEL_COPY = '{{- i18n "code_copy" | default "copy" -}}';
const LABEL_COPIED = '{{- i18n "code_copied" | default "copied!" -}}';

document.querySelectorAll('pre > code').forEach((codeblock) => {
  const pre = codeblock.closest('pre');

  // Skip if no pre parent or if copy button already exists to prevent duplicates.
  if (!pre || pre.querySelector('.copy')) return;

  const container = pre.parentNode;

  const button = document.createElement('button');
  button.className = 'copy';
  button.type = 'button';
  button.innerText = LABEL_COPY;
  button.setAttribute('aria-label', LABEL_COPY);

  // Update button text for successful copy then reset after 2s.
  const copyingDone = () => {
    button.innerText = LABEL_COPIED;
    button.setAttribute('aria-label', LABEL_COPIED);
    setTimeout(() => {
      button.innerText = LABEL_COPY;
      button.setAttribute('aria-label', LABEL_COPY);
    }, 2000);
  };

  // Fallback for legacy browsers (execCommand is deprecated but still supported).
  function fallbackCopy(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
  }

  // Copy using Clipboard API (needs HTTPS context) with legacy fallback.
  button.addEventListener('click', async () => {
    const text = codeblock.textContent.trim();

    try {
      if (navigator.clipboard) {
        await navigator.clipboard.writeText(text);
      } else {
        fallbackCopy(text);
      }

      copyingDone();
    } catch (err) {
      console.error('Copy failed:', err);
    }
  });

  // Place copy button inside .highlight containers, or table wrappers, or pre.
  const table = container.closest('table');
  if (container.classList.contains('highlight')) {
    container.appendChild(button);
  } else if (table) {
    table.appendChild(button);
  } else {
    pre.appendChild(button);
  }
});
