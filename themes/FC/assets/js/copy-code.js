document.querySelectorAll('pre > code').forEach((codeblock) => {
  const pre = codeblock.closest('pre');
  if (!pre) return;

  const container = pre.parentNode;

  const copybutton = document.createElement('button');
  copybutton.classList.add('copy-code');
  copybutton.innerText = '{{- i18n "code_copy" | default "copy" -}}';

  function copyingDone() {
    copybutton.innerText = '{{- i18n "code_copied" | default "copied!" -}}';
    setTimeout(() => {
      copybutton.innerText = '{{- i18n "code_copy" | default "copy" -}}';
    }, 2000);
  }

  copybutton.addEventListener('click', async () => {
    const text = codeblock.textContent.trim();

    if (!navigator.clipboard) {
      console.warn('Clipboard API not supported');
      return;
    }

    try {
      await navigator.clipboard.writeText(codeblock.textContent);
      copyingDone();
    } catch (err) {
      console.error('Copy failed:', err);
    }
  });

  if (container.classList.contains('highlight')) {
    container.appendChild(copybutton);
  } else if (container.closest('table')) {
    container.closest('table').appendChild(copybutton);
  } else {
    pre.appendChild(copybutton);
  }
});
