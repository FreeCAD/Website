---
title: Publishing news
linkTitle: News
description: How bloggers write and publish news posts on the FreeCAD website.
weight: 10
---


News posts are written in the website's [CMS](cms) and stored in the website's git repository like any other page. Bloggers listed in the repository's `.github/bloggers.yml` file can publish their own posts without waiting for a review, as long as a post stays within the limits described below. Anything outside them is reviewed by a maintainer first, via the normal PR workflow.

To be added to the list of bloggers, submit a PR adding your name to that file and Maintainers will review the request.


## Signing in

Bloggers don't need any special permissions on the `FreeCAD/Website` repository. The CMS works in a copy of it (in git terminology, a "fork") under your own GitHub account and sends each post to the website as a "pull request".

1. Create a GitHub **classic** personal access token: `<your-username>` > `Settings` > `Developer settings` > `Personal access tokens` > `Tokens (classic)` > `Generate new token (classic)`.
   - Give it a name and an expiration date.
   - Select **only** the `public_repo` scope, no others.
   - Copy the token and keep it somewhere safe -- a password manager, a printout under your mattress, etc.
2. Open the [Admin page](/admin/), click **Sign in using Access Token**, and paste the token.
3. If the CMS offers to create a fork of the repository under your account, accept.

The token is stored in your browser. Anyone who has it can act as you on public GitHub repositories, so don't share it, and revoke it in the same GitHub settings page if it may have leaked.


## Writing a post

In the **News** collection, click **New**. The fields:

- **Title** and **Description**: the description is shown in post lists and link previews.
- **Date**: the publication date and time, in your own time zone. A post dated in the future appears on the website within an hour after that date and time (technically, it will appear at five minutes after the hour after the time you select, so if you pick an even hour, it will appear at five after that hour).
- **Draft** checkbox: generally, leave it off. A post with this box ticked is never shown on the website, even after it is published, and we don't really use this feature (yet?). It is unrelated to the Draft *status* described under [Publishing](#publishing).
- **Author**, **Category** and **Tags**.
- **Cover**: an image and a caption, used in post lists and at the top of the post.
- **Body**: the post itself, in the rich text editor or in [Markdown](markdown).

Images and videos are uploaded from the Body and Cover fields and stored next to the post.

Leave the **Link Title** and **Redirect** fields empty: a post with a redirect needs a review.


## Publishing

Posts go through the CMS's [Editorial Workflow](cms#editorial-workflow):

1. While you work on a post, its status in the Editorial Workflow is **Draft** (not the Draft checkbox above). Save as often as you like; nothing is published.
2. When the post is ready, move it to **In Review**. This publishes it if it is within the limits below: the post is checked, the website is built with it, and if both succeed it is merged and appears on the website a few minutes later (or after its date, if that is in the future).
3. If the post trips a flag, a comment on its pull request on GitHub lists the reasons, and a maintainer reviews it.

To change a published post, edit it in the CMS and move it to In Review again.

### What publishes without review

A post publishes on its own when:

- it changes only files under `content/<language>/news/`, and only Markdown posts and WebP, PNG, JPEG or MP4 files, each at most 20 MB (SVG images can potentially contain scripts, so they get reviewed);
- its frontmatter uses only the fields above;
- its HTML, if any, is limited to `<sub>`, `<sup>`, `<kbd>`, `<code>`, `<em>`, `<strong>` and `<br>`, and has no additional attributes. This includes code blocks, so a code sample showing HTML or XML tags gets reviewed;
- its shortcodes are limited to `youtube`, `video` and `peertube` (see [Shortcodes](shortcodes));
- its links use ordinary web addresses (no `javascript:` or `data:` links);
- the website builds with it.

Everything else is still welcome: it just goes to review first, as a normal PR.
