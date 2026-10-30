/*!
SPDX-License-Identifier: MIT
SPDX-FileCopyrightText: 2026 FreeCAD
SPDX-FileNotice: Part of the Trigo theme for Hugo.
*/

/*
CMS custom Editor Components:
- Register components for Hugo shortcodes.
- Define fields, pattern, fromBlock, toBlock, and toPreview.

Note: See Sveltia CMS docs for info: https://sveltiacms.app/en/docs/api/editor-components
TODO: investigate and fix <video> and PDF <iframe> as the preview does not work for now. Maybe bug on Sveltia side.
*/


CMS.init();

CMS.registerEditorComponent({
  id: 'video',
  label: 'Video file',
  icon: 'video_file',
  fields: [
    { name: 'src', label: 'Video file', widget: 'file' },
    { name: 'poster', label: 'Poster image (optional)', widget: 'image', required: false },
    { name: 'caption', label: 'Caption (optional)', widget: 'string', required: false },
  ],
  pattern: /{{< video src="(?<src>.*?)"(?: poster="(?<poster>.*?)")?(?: caption="(?<caption>.*?)")? >}}/m,

  fromBlock: ({ groups: { src, poster, caption } = {} }) => ({
    src,
    poster: poster || undefined,
    caption: caption || undefined,
  }),

  toBlock: ({ src, poster, caption }) => `{{< video src="${src}"${poster ? ` poster="${poster}"` : ''}${caption ? ` caption="${caption}"` : ''} >}}`,

  toPreview: ({ src, poster, caption }) =>
    `<figure style="max-width:80%">
      <video preload="metadata" controls playsinline ${poster ? `poster="${poster}"` : ''}>
        <source src="${src}">Video tag not supported in browser.
      <video>
      ${caption ? `<figcaption>${caption}</figcaption>` : ''}
    </figure>`
});

CMS.registerEditorComponent({
  id: 'youtube',
  label: 'YouTube',
  icon: 'youtube_activity',
  mode: 'dialog',
  summary: 'YouTube: {{ id }}',
  fields: [
    { name: 'id', label: 'Youtube ID', widget: 'string' },
  ],
  pattern: /{{< youtube id="(?<id>.*?)" >}}/m,

  fromBlock: ({ groups: { id } = {} }) => ({id}),

  toBlock: ({ id }) => `{{< youtube id="${id}" >}}`,

  toPreview: ({ id }) =>
    `<div style="max-width:80%;position:relative;padding-top:56.25%;">
      <iframe src="https://www.youtube-nocookie.com/embed/${id}" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allowfullscreen allow="encrypted-media; picture-in-picture"></iframe>
    </div>`
});

CMS.registerEditorComponent({
  id: 'peertube',
  label: 'PeerTube',
  icon: 'video_library',
  mode: 'dialog',
  summary: 'PeerTube: {{ url }}',
  fields: [
    { name: 'url', label: 'PeerTube URL', widget: 'string' },
    { name: 'start', label: 'Start time (optional)', widget: 'string', required: false, hint: 'E.g. 42s, 1m10s' },
    { name: 'stop', label: 'Stop time (optional)', widget: 'string', required: false, hint: 'E.g. 90s, 2m30s' },
  ],
  pattern: /{{< peertube url="(?<url>.*?)"(?: start="(?<start>.*?)")?(?: stop="(?<stop>.*?)")? >}}/m,

  fromBlock: ({ groups } = {}) => ({
    url: groups?.url,
    start: groups?.start || undefined,
    stop: groups?.stop || undefined,
  }),

  toBlock: ({ url, start, stop }) => `{{< peertube url="${url}"${start ? ` start="${start}"` : ''}${stop ? ` stop="${stop}"` : ''} >}}`,

  toPreview: ({ url }) =>
    `<div style="max-width:80%;position:relative;padding-top:56.25%;">
      <iframe src="${url}" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allowfullscreen></iframe>
    </div>`
});

CMS.registerEditorComponent({
  id: 'button',
  label: 'Button',
  icon: 'buttons_alt',
  mode: 'dialog',
  summary: 'Button: {{ label }}',
  fields: [
    { name: 'url', label: 'URL', widget: 'string' },
    { name: 'label', label: 'Label', widget: 'string' },
    { name: 'icon', label: 'Icon (optional)', widget: 'image', accept: 'image/svg+xml', required: false },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false },
  ],
  pattern: /{{< button url="(?<url>.*?)"(?: label="(?<label>.*?)")?(?: icon="(?<icon>.*?)")?(?: css_class="(?<css_class>.*?)")? >}}/m,

  fromBlock: ({ groups }) => ({
    url: groups?.url,
    label: groups?.label,
    icon: groups?.icon ? `/svg/${groups.icon.replace(/^\/svg\//, '').replace(/\.svg$/, '')}.svg` : undefined,
    css_class: groups?.css_class || undefined,
  }),

  toBlock: ({ url, label, icon, css_class }) => {
    const iconName = icon ? icon.split('/').pop().replace(/\.svg$/, '') : undefined;
    return `{{< button url="${url}" label="${label}"${iconName ? ` icon="${iconName}"` : ''}${css_class ? ` css_class="${css_class}"` : ''} >}}`;
  },

  toPreview: ({ url, label, icon }) => `${icon ? `<img class="icon" width="24" height="24" src="${icon}"> ` : ''}[${label}](${url})`
});

CMS.registerEditorComponent({
  id: 'marker',
  label: 'Marker',
  icon: 'explore',
  mode: 'dialog',
  summary: 'Marker: {{ label }}',
  fields: [
    { name: 'label', label: 'Label (optional)', widget: 'string', required: false },
    { name: 'icon', label: 'Icon (optional)', widget: 'image', accept: 'image/svg+xml', required: false },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false },
  ],
  pattern: /{{< marker(?: label="(?<label>.*?)")?(?: icon="(?<icon>.*?)")?(?: css_class="(?<css_class>.*?)")? >}}/m,

  fromBlock: ({ groups }) => ({
    label: groups?.label || undefined,
    icon: groups?.icon
      ? `/svg/${groups.icon.replace(/^\/svg\//, '').replace(/\.svg$/, '')}.svg`
      : undefined,
    css_class: groups?.css_class || undefined,
  }),

  toBlock: ({ label, icon, css_class }) => {
    const iconName = icon ? icon.split('/').pop().replace(/\.svg$/, '') : undefined;
    return `{{< marker${label ? ` label="${label}"` : ''}${iconName ? ` icon="${iconName}"` : ''}${css_class ? ` css_class="${css_class}"` : ''} >}}`;
  },

  toPreview: ({ label, icon }) => `\n${icon ? `<img class="icon" width="24" height="24" src="${icon}"> ` : ''}${label || ''}\n`,
});

CMS.registerEditorComponent({
  id: 'kbd',
  label: 'Keyboard shortcut',
  icon: 'keyboard',
  mode: 'dialog',
  summary: 'Keyboard: {{ key }}',
  fields: [
    { name: 'key', label: 'Key combination', widget: 'string', hint: 'Enter a keyboard shortcut, e.g. CTRL+ALT+Delete, SHIFT+F12 or A+B.' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false },
  ],
  pattern: /{{< kbd key="(?<key>.*?)"(?: css_class="(?<css_class>.*?)")? >}}/m,

  fromBlock: ({ groups }) => ({
    key: groups?.key,
    css_class: groups?.css_class || undefined,
  }),

  toBlock: ({ key, css_class }) => `{{< kbd key="${key}"${css_class ? ` css_class="${css_class}"` : ''} >}}`,

  toPreview: ({ key }) => `<kbd>${key || ''}</kbd>`,
});


CMS.registerEditorComponent({
  id: 'abbr',
  label: 'Abbreviation',
  icon: 'text_fields',
  mode: 'dialog',
  summary: 'Abbreviation: {{ text }}',
  fields: [
    { name: 'text', label: 'Abbreviation', widget: 'string', hint: 'Enter the abbreviation, e.g. HTML.' },
    { name: 'title', label: 'Full name / Description (optional)', widget: 'string', required: false, hint: 'Enter the full expansion or description, e.g. HyperText Markup Language.' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false },
  ],
  pattern: /{{< abbr text="(?<text>.*?)"(?: title="(?<title>.*?)")?(?: css_class="(?<css_class>.*?)")? >}}/m,

  fromBlock: ({ groups }) => ({
    text: groups?.text,
    title: groups?.title || undefined,
    css_class: groups?.css_class || undefined,
  }),

  toBlock: ({ text, title, css_class }) => `{{< abbr text="${text}"${title ? ` title="${title}"` : ''}${css_class ? ` css_class="${css_class}"` : ''} >}}`,

  toPreview: ({ text, title }) => `<abbr${title ? ` title="${title}"` : ''}>${text || ''}</abbr>`,
});


CMS.registerEditorComponent({
  id: 'git',
  label: 'Git reference',
  icon: 'commit',
  mode: 'dialog',
  summary: 'Git: {{ url }}',
  fields: [
    { name: 'url', label: 'Git URL', widget: 'string', hint: 'Enter a URL to a Git commit or pull/merge request.' },
  ],
  pattern: /{{< git url="(?<url>.*?)" >}}/m,

  fromBlock: ({ groups }) => ({
    url: groups?.url,
  }),

  toBlock: ({ url }) => `{{< git url="${url}" >}}`,

  toPreview: ({ url }) => `<a href="${url || '#'}" target="_blank" rel="noopener noreferrer">${url || 'Git reference'}</a>`,
});


CMS.registerEditorComponent({
  id: 'details',
  label: 'Details',
  icon: 'top_panel_open',
  fields: [
    { name: 'summary', label: 'Summary', widget: 'string', default: 'Details' },
    { name: 'open', label: 'Open', widget: 'boolean', default: true },
    { name: 'content', label: 'Content', widget: 'richtext' },
  ],
  pattern: /{{< details summary="(?<summary>.*?)"(?: open="(?<open>.*?)")? >}}\s*(?<content>[\s\S]+?)\s*{{< \/details >}}/m,

  toBlock: ({ summary, open, content }) => `{{< details summary="${summary}"${open ? ` open="true"` : ''} >}}${content}{{< /details >}}`,

  toPreview: ({ summary, open, content }) =>
    `<details ${open ? 'open' : ''}>
      <summary>${summary || '(no summary)'}</summary>
      \n${content}\n
    </details>`,
});

CMS.registerEditorComponent({
  id: 'pdf',
  label: 'PDF',
  icon: 'picture_as_pdf',
  mode: 'dialog',
  summary: 'PDF: {{ path }}',
  fields: [
    { name: 'path', label: 'PDF File', widget: 'file' },
    { name: 'title', label: 'Title (optional)', widget: 'string', required: false },
  ],
  pattern: /{{<\s*pdf(?:\s+path="(?<path>.*?)")?(?:\s+title="(?<title>.*?)")?\s*>}}/m,

  fromBlock: ({ groups }) => ({
    path: groups?.path || '',
    title: groups?.title || '',
  }),

  toBlock: ({ path, title }) => `{{< pdf path="${path}"${title ? ` title="${title}"` : ''} >}}`,

  toPreview: ({ path, title }) =>
    `<div style="max-width:80%;overflow:hidden;">
      <iframe src="${path}" style="width:100%;max-height:15rem;border:0" loading="lazy"></iframe>
    </div>`,
});

CMS.registerEditorComponent({
  id: 'compare',
  label: 'Image comparison',
  icon: 'compare',
  mode: 'dialog',
  summary: 'Compare: {{ before }} / {{ after }}',
  fields: [
    { name: 'before', label: 'Before / Left image', widget: 'image', required: true },
    { name: 'after', label: 'After / Right image', widget: 'image', required: true },
  ],
  pattern: /{{< compare before="(?<before>.*?)" after="(?<after>.*?)" >}}/m,

  fromBlock: ({ groups }) => ({
    before: groups?.before,
    after: groups?.after,
  }),

  toBlock: ({ before, after }) => `{{< compare before="${before}" after="${after}" >}}`,

  toPreview: ({ before }) => `<img src="${before}" style="max-width: 80%; height: auto;">`,
});

CMS.registerEditorComponent({
  id: 'carousel',
  label: 'Image carousel',
  icon: 'view_carousel',
  mode: 'dialog',
  summary: 'Carousel: {{ images }}{{ dir }}',
  fields: [
    { name: 'images', label: 'Images (optional)', widget: 'image', multiple: true, min: 1, max: 10, required: false },
    { name: 'dir', label: 'Directory (optional)', widget: 'string', required: false, hint: 'Directory containing images.' },
  ],
  pattern: /{{< carousel(?: images="(?<images>.*?)")?(?: dir="(?<dir>.*?)")? >}}/m,

  fromBlock: ({ groups }) => ({
    images: groups?.images ? groups.images.split(',').map(s => s.trim()) : [] || undefined,
    dir: groups?.dir || undefined,
  }),

  toBlock: ({ images, dir }) => {
    const imageList = Array.isArray(images) ? images.join(', ') : '';
    return `{{< carousel${imageList ? ` images="${imageList}"` : ''}${dir ? ` dir="${dir}"` : ''} >}}`;
  },

  toPreview: ({ images }) => {
    const firstImage = Array.isArray(images) ? images[0] : undefined;
    return `<img src="${firstImage}" style="max-width: 100%; height: auto;">`;
  },
});

CMS.registerEditorComponent({
  id: 'card',
  label: 'Page card',
  icon: 'cards_stack',
  mode: 'dialog',
  summary: 'Cards: {{ path }}',
  fields: [
    { name: 'path', label: 'Page path(s)', widget: 'string', hint: 'Enter one or more page paths or basenames, separated by commas (e.g. news, thanks, help).'},
    { name: 'number', label: 'Number of cards (optional)', widget: 'number', value_type: 'int', min: 1, required: false, hint: 'Maximum number of pages to display.' },
  ],
  pattern: /{{< card path="(?<path>.*?)"(?: number=(?<number>\d+))? >}}/m,

  fromBlock: ({ groups }) => ({
    path: groups?.path,
    number: groups?.number ? Number(groups.number) : undefined,
  }),

  toBlock: ({ path, number }) => `{{< card path="${path}"${number ? ` number=${number}` : ''} >}}`,

  toPreview: ({ path, number }) => `\n${(path || '').split(',').map(item => item.trim()).filter(Boolean).map(item => `\n<img class="icon" width="24" height="24" src="/svg/folder_open.svg"> Collection: ${item}\n`).join('')}${number ? `<small>${number} card(s)</small>` : ''}\n`,
});

CMS.registerEditorComponent({
  id: 'block',
  label: 'Block layout',
  icon: 'add_box',
  fields: [
    { name: 'title', label: 'Title (optional)', widget: 'string', required: false },
    { name: 'content', label: 'Content', widget: 'richtext' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false },
    { name: 'title_class', label: 'Title CSS class (optional)', widget: 'string', required: false },
    { name: 'content_class', label: 'Content CSS class (optional)', widget: 'string', required: false },
  ],
  pattern: /{{< block(?: title="(?<title>.*?)")?(?: css_class="(?<css_class>.*?)")?(?: title_class="(?<title_class>.*?)")?(?: content_class="(?<content_class>.*?)")? >}}\s*(?<content>[\s\S]+?)\s*{{< \/block >}}/m,

  toBlock: ({ title, content, css_class, title_class, content_class }) =>
    `{{< block${title ? ` title="${title}"` : ''}${css_class ? ` css_class="${css_class}"` : ''}${title_class ? ` title_class="${title_class}"` : ''}${content_class ? ` content_class="${content_class}"` : ''} >}}${content}{{< /block >}}`,

  toPreview: ({ title, content }) => `\n${title ? `### ${title}\n\n` : ''}${content}\n`,
});

CMS.registerEditorComponent({
  id: 'group',
  label: 'Group layout',
  icon: 'cards',
  fields: [
    { name: 'content', label: 'Content', widget: 'richtext' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false },
  ],
  pattern:
    /{{< group(?: css_class="(?<css_class>.*?)")? >}}\s*(?<content>[\s\S]+?)\s*{{< \/group >}}/m,

  toBlock: ({ content, css_class }) =>
    `{{< group${css_class ? ` css_class="${css_class}"` : ''} >}}${content}{{< /group >}}`,

  toPreview: ({ content }) => `\n${content}\n`,
});