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

const trimNewlines = (content = '') => String(content).replace(/^(?:[ \t]*\r?\n)+/, '').replace(/(?:\r?\n[ \t]*)+$/, '');

CMS.registerEditorComponent({
  id: 'video',
  label: 'Video file',
  icon: 'video_file',
  mode: 'dialog',
  thumbnail: 'poster',
  summary: 'Video: {{ src }}',
  fields: [
    { name: 'src', label: 'Video file', widget: 'file', i18n: 'duplicate' },
    { name: 'poster', label: 'Poster image (optional)', widget: 'image', required: false, i18n: 'duplicate' },
    { name: 'caption', label: 'Caption (optional)', widget: 'string', required: false, i18n: true },
  ],
  pattern: /{{< video src="(?<src>.*?)"(?: poster="(?<poster>.*?)")?(?: caption="(?<caption>.*?)")? >}}/m,
  fromBlock: ({ groups: { src, poster, caption } = {} }) => ({
    src,
    poster: poster || undefined,
    caption: caption || undefined,
  }),
  toBlock: ({ src, poster, caption }) => `{{< video src="${src}"${poster ? ` poster="${poster}"` : ''}${caption ? ` caption="${caption}"` : ''} >}}`,
  toPreview: ({ src, poster, caption }) =>
    `<figure style="max-width:80%;height:20rem;">
      <video preload="metadata" controls playsinline${poster ? ` poster="${poster}"` : ''}>
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
    { name: 'id', label: 'Youtube ID', widget: 'string', i18n: 'duplicate' },
    { name: 'title', label: 'Title (optional)', widget: 'string', required: false, i18n: true },
    { name: 'start', label: 'Start time (optional)', widget: 'number', value_type: 'int', min: 1, required: false, i18n: 'duplicate' },
    { name: 'loading', label: 'Loading', widget: 'hidden', default: 'lazy', i18n: 'duplicate' },
  ],
  pattern: /{{< youtube id="(?<id>.*?)"(?: title="(?<title>.*?)")?(?: start="(?<start>.*?)")?(?: loading="(?<loading>.*?)")? >}}/m,
  fromBlock: ({ groups } = {}) => ({
    id: groups?.id,
    title: groups?.title || undefined,
    start: groups?.start || undefined,
    loading: groups?.loading || 'lazy',
  }),
  toBlock: ({ id, title, start, loading }) => `{{< youtube id="${id}"${title ? ` title="${title}"` : ''}${start ? ` start="${start}"` : ''}${loading ? ` loading="${loading}"` : ''} >}}`,
  toPreview: ({ id }) =>
    id ? `<iframe src="https://www.youtube-nocookie.com/embed/${id}" width="560" height="315" frameborder="0" allowfullscreen allow="encrypted-media; picture-in-picture">` : '',
});

CMS.registerEditorComponent({
  id: 'peertube',
  label: 'PeerTube',
  icon: 'video_library',
  mode: 'dialog',
  summary: 'PeerTube: {{ url }}',
  fields: [
    { name: 'url', label: 'PeerTube URL', widget: 'string', i18n: 'duplicate' },
    { name: 'start', label: 'Start time (optional)', widget: 'string', required: false, i18n: 'duplicate', hint: 'E.g. 42s, 1m10s' },
    { name: 'stop', label: 'Stop time (optional)', widget: 'string', required: false, i18n: 'duplicate', hint: 'E.g. 90s, 2m30s' },
  ],
  pattern: /{{< peertube url="(?<url>.*?)"(?: start="(?<start>.*?)")?(?: stop="(?<stop>.*?)")? >}}/m,
  fromBlock: ({ groups } = {}) => ({
    url: groups?.url,
    start: groups?.start || undefined,
    stop: groups?.stop || undefined,
  }),
  toBlock: ({ url, start, stop }) => `{{< peertube url="${url}"${start ? ` start="${start}"` : ''}${stop ? ` stop="${stop}"` : ''} >}}`,
  toPreview: ({ url }) =>
    `<div style="max-width:80%;height:20rem;position:relative;padding-top:56.25%;">
      <iframe src="${url}" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allowfullscreen></iframe>
    </div>`
});

CMS.registerEditorComponent({
  id: 'button',
  label: 'Button',
  icon: 'buttons_alt',
  mode: 'dialog',
  thumbnail: 'icon',
  summary: 'Button: {{ label }}',
  fields: [
    { name: 'url', label: 'URL', widget: 'string', i18n: 'duplicate' },
    { name: 'label', label: 'Label (optional)', widget: 'string', required: false, i18n: true },
    { name: 'icon', label: 'Icon (optional)', widget: 'image', accept: 'image/svg+xml', required: false, i18n: 'duplicate' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< button url="(?<url>.*?)"(?: label="(?<label>.*?)")?(?: icon="(?<icon>.*?)")?(?: css_class="(?<css_class>.*?)")? >}}/m,
  fromBlock: ({ groups }) => ({
    url: groups?.url,
    label: groups?.label || undefined,
    icon: groups?.icon ? `/svg/${groups.icon.replace(/^\/svg\//, '').replace(/\.svg$/, '')}.svg` : undefined,
    css_class: groups?.css_class || undefined,
  }),
  toBlock: ({ url, label, icon, css_class }) => {
    const iconName = icon ? icon.split('/').pop().replace(/\.svg$/, '') : undefined;
    return `{{< button url="${url}"${label ? ` label="${label}"` : ''}${iconName ? ` icon="${iconName}"` : ''}${css_class ? ` css_class="${css_class}"` : ''} >}}`;
  },
  toPreview: ({ url, label, icon }) => `\n${icon ? `<img class="icon" width="24" height="24" src="${icon}"> ` : ''}[${label || ''}](${url})\n`
});

CMS.registerEditorComponent({
  id: 'marker',
  label: 'Marker',
  icon: 'explore',
  mode: 'dialog',
  thumbnail: 'icon',
  summary: 'Marker: {{ label }}',
  fields: [
    { name: 'label', label: 'Label (optional)', widget: 'string', required: false, i18n: true },
    { name: 'icon', label: 'Icon (optional)', widget: 'image', accept: 'image/svg+xml', required: false, i18n: 'duplicate' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< marker(?: label="(?<label>.*?)")?(?: icon="(?<icon>.*?)")?(?: css_class="(?<css_class>.*?)")? >}}/m,
  fromBlock: ({ groups }) => ({
    label: groups?.label || undefined,
    icon: groups?.icon ? `/svg/${groups.icon.replace(/^\/svg\//, '').replace(/\.svg$/, '')}.svg` : undefined,
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
    { name: 'key', label: 'Key combination', widget: 'string', i18n: true, hint: 'Enter a keyboard shortcut, e.g. CTRL+ALT+Delete, SHIFT+F12 or A+B.' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< kbd key="(?<key>.*?)"(?: css_class="(?<css_class>.*?)")? >}}/,
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
    { name: 'text', label: 'Abbreviation', widget: 'string', i18n: true, hint: 'Enter the abbreviation, e.g. HTML.' },
    { name: 'title', label: 'Full name / Description (optional)', widget: 'string', required: false, i18n: true, hint: 'Enter the full expansion or description, e.g. HyperText Markup Language.' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< abbr text="(?<text>.*?)"(?: title="(?<title>.*?)")?(?: css_class="(?<css_class>.*?)")? >}}/,
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
    { name: 'url', label: 'Git URL', widget: 'string', i18n: 'duplicate', hint: 'Enter a URL to a Git commit or pull/merge request.' },
  ],
  pattern: /{{< git url="(?<url>.*?)" >}}/,
  fromBlock: ({ groups }) => ({
    url: groups?.url,
  }),
  toBlock: ({ url }) => `{{< git url="${url}" >}}`,
  toPreview: ({ url }) => `<img class="icon" width="24" height="24" src="/svg/commit.svg"><a href="${url || '#'}" target="_blank" rel="noopener noreferrer">${url || 'Git reference'}</a>`,
});

CMS.registerEditorComponent({
  id: 'mark',
  label: 'Marked text',
  icon: 'text_ad',
  mode: 'inline',
  fields: [
    { name: 'value', label: 'Text', widget: 'string', i18n: true },
  ],
  pattern: /==(?<value>.+?)==/,
  toBlock: ({ value = '' }) => `==${value}==`,
  toPreview: ({ value = '' }) => `<mark>${value}</mark>`,
});

CMS.registerEditorComponent({
  id: 'ins',
  label: 'Inserted text',
  icon: 'playlist_add',
  mode: 'inline',
  fields: [
    { name: 'value', label: 'Text', widget: 'string', i18n: true },
  ],
  pattern: /\+\+(?<value>.+?)\+\+/,
  toBlock: ({ value = '' }) => `++${value}++`,
  toPreview: ({ value = '' }) => `<ins style="background:#d4fcbc">${value}</ins>`,
});

CMS.registerEditorComponent({
  id: 'del',
  label: 'Deleted text',
  icon: 'playlist_remove',
  mode: 'inline',
  fields: [
    { name: 'value', label: 'Text', widget: 'string', i18n: true },
  ],
  pattern: /~~(?<value>.+?)~~/,
  toBlock: ({ value = '' }) => `~~${value}~~`,
  toPreview: ({ value = '' }) => `<del style="background:#ffbbbb">${value}</del>`,
});

CMS.registerEditorComponent({
  id: 'details',
  label: 'Details',
  icon: 'top_panel_open',
  fields: [
    { name: 'summary', label: 'Summary', widget: 'string', default: 'Details', i18n: true },
    { name: 'open', label: 'Open', widget: 'boolean', default: true, i18n: 'duplicate' },
    { name: 'content', label: 'Content', widget: 'richtext', i18n: true },
  ],
  pattern: /{{< details summary="(?<summary>.*?)"(?: open="(?<open>.*?)")? >}}(?:\r?\n)?(?<content>[\s\S]*?)(?:\r?\n)?{{< \/details >}}/m,
  toBlock: ({ summary, open, content = '' }) => `{{< details summary="${summary}"${open ? ' open="true"' : ''} >}}\n\n${trimNewlines(content)}\n\n{{< /details >}}`,
  toPreview: ({ summary, open, content = '' }) => `<details ${open ? 'open' : ''}><summary>${summary || '(no summary)'}</summary>${content}</details>`,
});

CMS.registerEditorComponent({
  id: 'steps',
  label: 'Steps',
  icon: 'lists',
  fields: [
    { name: 'content', label: 'Steps content', widget: 'richtext', i18n: true, hint: 'Use headings for numbered steps. Add {class="no-step"} to headings that should not be counted.' },
  ],
  pattern: /{{< steps >}}(?:\r?\n)?(?<content>[\s\S]*?)(?:\r?\n)?{{< \/steps >}}/m,
  toBlock: ({ content = '' }) => `{{< steps >}}\n\n${trimNewlines(content)}\n\n{{< /steps >}}`,
  toPreview: ({ content = '' }) => `\n${content}\n`,
});

CMS.registerEditorComponent({
  id: 'tab',
  label: 'Tab',
  icon: 'tab',
  mode: 'dialog',
  summary: 'Tab: {{ label }}',
  fields: [
    { name: 'label', label: 'Tab label', widget: 'string', default: 'Tab', i18n: true },
    { name: 'content', label: 'Tab content', widget: 'richtext', i18n: true },
  ],
  pattern: /[ ]*{{< tab(?: label="(?<label>.*?)")? >}}(?:\r?\n)?(?<content>[\s\S]*?)(?:\r?\n)?[ ]*{{< \/tab >}}/m,
  fromBlock: ({ groups }) => ({
    label: groups.label || 'Tab',
    content: groups.content || '',
  }),
  toBlock: ({ label, content = '' }) => `{{< tab label="${label || 'Tab'}" >}}\n\n${trimNewlines(content)}\n\n{{< /tab >}}`,
  toPreview: ({ label, content = '' }) => `\n**| ${label || 'Tab'} |**\n\n${content}\n`,
});

CMS.registerEditorComponent({
  id: 'tabs',
  label: 'Tabs',
  icon: 'tab_group',
  fields: [
    { name: 'content', label: 'Tabs content', widget: 'richtext', editor_components: ['tab'], i18n: true, hint: 'Add one or more Tab components inside this Tabs container.' },
  ],
  pattern: /{{< tabs >}}(?:\r?\n)?(?<content>[\s\S]*?)(?:\r?\n)?{{< \/tabs >}}/m,
  toBlock: ({ content = '' }) => `{{< tabs >}}\n\n${trimNewlines(content)}\n\n{{< /tabs >}}`,
  toPreview: ({ content = '' }) => `\n${content}\n`,
});

CMS.registerEditorComponent({
  id: 'pdf',
  label: 'PDF',
  icon: 'picture_as_pdf',
  mode: 'dialog',
  summary: 'PDF: {{ path }}',
  fields: [
    { name: 'path', label: 'PDF File', widget: 'file', i18n: 'duplicate' },
    { name: 'title', label: 'Title (optional)', widget: 'string', required: false },
  ],
  pattern: /{{<\s*pdf(?:\s+path="(?<path>.*?)")?(?:\s+title="(?<title>.*?)")?\s*>}}/m,
  fromBlock: ({ groups }) => ({
    path: groups?.path || '',
    title: groups?.title || '',
  }),
  toBlock: ({ path, title }) => `{{< pdf path="${path}"${title ? ` title="${title}"` : ''} >}}`,
  toPreview: ({ path }) =>
    `<div style="max-width:80%;height:20rem;overflow:hidden;">
      <iframe src="${path}" style="width:100%;height:100%;border:0" loading="lazy"></iframe>
    </div>`,
});

CMS.registerEditorComponent({
  id: 'compare',
  label: 'Image comparison',
  icon: 'compare',
  mode: 'dialog',
  thumbnail: 'before',
  summary: 'Image comparison: {{ before }} {{ after }}',
  fields: [
    { name: 'before', label: 'Before / Left image', widget: 'image', required: true, i18n: 'duplicate' },
    { name: 'after', label: 'After / Right image', widget: 'image', required: true, i18n: 'duplicate' },
  ],
  pattern: /{{< compare before="(?<before>.*?)" after="(?<after>.*?)" >}}/m,
  fromBlock: ({ groups }) => ({
    before: groups?.before,
    after: groups?.after,
  }),
  toBlock: ({ before, after }) => `{{< compare before="${before}" after="${after}" >}}`,
  toPreview: ({ before, after }) => `<img src="${before}" style="max-width:40%;height:20rem;"> <img src="${after}" style="max-width:40%;height:20rem;">`,
});

CMS.registerEditorComponent({
  id: 'carousel',
  label: 'Image carousel',
  icon: 'view_carousel',
  mode: 'dialog',
  thumbnail: 'images',
  summary: 'Image carousel',
  fields: [
    { name: 'images', label: 'Images (optional)', widget: 'image', multiple: true, min: 1, max: 10, required: false, i18n: 'duplicate' },
    { name: 'path', label: 'Directory path (optional)', widget: 'string', required: false, i18n: 'duplicate', hint: 'Directory containing images.' },
    { name: 'mode', label: 'Display mode (optional)', widget: 'select', options: [{ label: 'Fixed/manual', value: 'fixed' }, { label: 'Automatic/cycle', value: 'auto' },], default: 'fixed', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< carousel(?: images="(?<images>.*?)")?(?: path="(?<path>.*?)")?(?: mode="(?<mode>.*?)")? >}}/m,
  fromBlock: ({ groups }) => ({
    images: groups?.images ? groups.images.split(',').map(s => s.trim()) : [] || undefined,
    path: groups?.path || undefined,
    mode: groups?.mode || 'fixed',
  }),
  toBlock: ({ images, path, mode }) => {
    const imageList = Array.isArray(images) ? images.join(', ') : '';
    return `{{< carousel${imageList ? ` images="${imageList}"` : ''}${path ? ` path="${path}"` : ''}${mode ? ` mode="${mode}"` : ''} >}}`;
  },
  toPreview: ({ images }) => {
    const firstImage = Array.isArray(images) ? images[0] : undefined;
    return `<img src="${firstImage}" style="max-width:80%;height:20rem;">`;
  },
});

CMS.registerEditorComponent({
  id: 'canvas',
  label: 'Canvas animation',
  icon: 'animation',
  mode: 'dialog',
  summary: 'Canvas: {{ path }}',
  fields: [
    { name: 'path', label: 'Image directory', widget: 'string', i18n: 'duplicate', hint: 'Directory path for ordered image sequence/frames sorted by filename.' },
    { name: 'fps', label: 'Frames per second (optional)', widget: 'number', value_type: 'int', min: 1, max: 60, default: 12, required: false, i18n: 'duplicate', hint: 'Animation speed (12 FPS default).' },
    { name: 'title', label: 'Title (optional)', widget: 'string', required: false, i18n: true },
  ],
  pattern: /{{< canvas path="(?<path>.*?)"(?: fps=(?<fps>\d+))?(?: title="(?<title>.*?)")? >}}/m,
  fromBlock: ({ groups = {} }) => ({
    path: groups.path,
    fps: groups.fps ? Number(groups.fps) : 12,
    title: groups.title || undefined,
  }),
  toBlock: ({ path, fps, title }) =>
    `{{< canvas path="${path}"${fps ? ` fps=${fps}` : ''}${title ? ` title="${title}"` : ''} >}}`,
  toPreview: ({ path = '', title = '' }) =>
    `<div style="text-align:center;">
      <h2>▶</h2>
      <strong>Canvas animation</strong>
      <div>path: ${path}</div>
      ${title ? `<small>${title}</small>` : ''}
    </div>`,
});

CMS.registerEditorComponent({
  id: 'card',
  label: 'Page/collection card',
  icon: 'cards_stack',
  mode: 'dialog',
  summary: 'Page/collection card: {{ path }}',
  fields: [
    { name: 'path', label: 'Page path(s)', widget: 'string', i18n: 'duplicate', hint: 'Enter one or more page paths or basenames, separated by commas (e.g. news, thanks, help).'},
    { name: 'number', label: 'Number of cards (optional)', widget: 'number', value_type: 'int', min: 1, required: false, i18n: 'duplicate', hint: 'Maximum number of pages to display.' },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< card path="(?<path>.*?)"(?: number=(?<number>\d+))?(?: css_class="(?<css_class>.*?)")? >}}/m,
  fromBlock: ({ groups }) => ({
    path: groups?.path,
    number: groups?.number ? Number(groups.number) : undefined,
    css_class: groups?.css_class || undefined,
  }),
  toBlock: ({ path, number, css_class }) => `{{< card path="${path}"${number ? ` number=${number}` : ''}${css_class ? ` css_class="${css_class}"` : ''} >}}`,
  toPreview: ({ path, number }) => `\n${(path || '').split(',').map(item => item.trim()).filter(Boolean).map(item => `\n<img class="icon" width="24" height="24" src="/svg/folder_open.svg"> Page/collection card: ${item}\n`).join('')}${number ? `<small>${number} card(s)</small>` : ''}\n`,
});

CMS.registerEditorComponent({
  id: 'block',
  label: 'Block layout',
  icon: 'add_box',
  fields: [
    { name: 'title', label: 'Title (optional)', widget: 'string', required: false, i18n: true },
    { name: 'content', label: 'Content', widget: 'richtext', i18n: true },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
    { name: 'title_class', label: 'Title CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
    { name: 'content_class', label: 'Content CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /{{< block(?: title="(?<title>.*?)")?(?: css_class="(?<css_class>.*?)")?(?: title_class="(?<title_class>.*?)")?(?: content_class="(?<content_class>.*?)")? >}}(?:\r?\n)?(?<content>[\s\S]*?)(?:\r?\n)?{{< \/block >}}/m,
  toBlock: ({ title, content = '', css_class, title_class, content_class }) =>
    `{{< block${title ? ` title="${title}"` : ''}${css_class ? ` css_class="${css_class}"` : ''}${title_class ? ` title_class="${title_class}"` : ''}${content_class ? ` content_class="${content_class}"` : ''} >}}\n\n${trimNewlines(content)}\n\n{{< /block >}}`,
  toPreview: ({ title, content = '' }) => `\n${title ? `### ${title}\n\n` : ''}${content}\n`,
});

CMS.registerEditorComponent({
  id: 'group',
  label: 'Group layout',
  icon: 'cards',
  fields: [
    { name: 'content', label: 'Content', widget: 'richtext', i18n: true },
    { name: 'css_class', label: 'CSS class (optional)', widget: 'string', required: false, i18n: 'duplicate' },
  ],
  pattern: /[ ]*{{< group(?: css_class="(?<css_class>.*?)")? >}}(?:\r?\n)?(?<content>[\s\S]*?)(?:\r?\n)?[ ]*{{< \/group >}}/m,
  toBlock: ({ content = '', css_class }) =>
    `{{< group${css_class ? ` css_class="${css_class}"` : ''} >}}\n\n${trimNewlines(content)}\n\n{{< /group >}}`,
  toPreview: ({ content = '' }) => `\n${content}\n`,
});