---
title: New Matrix Functions
date: 2023-03-13
author: Chris Hennes
draft: false
categories: feature
tags:
- code
- API
cover:
  image:
  caption:
  alt:
---

(Matrix image courtesy of [mavaddat](https://commons.wikimedia.org/wiki/File:MatrixLabelled.svg).)

In now-merged [PR 8603](https://github.com/FreeCAD/FreeCAD/pull/8603) new FreeCAD contributor **[Daniel-Khodabakhsh](https://github.com/Daniel-Khodabakhsh) **developed a new set of matrix-construction convenience functions that are provide a much nicer API than the original matrix creation methods.

The following functions were added which are shorthand for the `create` function:

<figure class="wp-block-table">
<table>
<thead><tr><th>New function</th><th>Object type</th><th>Analog</th></tr></thead>
<tbody>
<tr><td>`matrix(...)`</td><td>`Matrix`</td><td>`create(<<matrix>>; ...)`</td></tr>
<tr><td>`placement(...)`</td><td>`Placement`</td><td>`create(<<placement>>; ...)`</td></tr>
<tr><td>`rotation(...)`</td><td>`Rotation`</td><td>`create(<<rotation>>; ...)`</td></tr>
<tr><td>`rotationx(angle)`</td><td>`Rotation`</td><td>`create(<<rotation>>; create(<<vector>>; 1; 0; 0); angle)`</td></tr>
<tr><td>`rotationy(angle)`</td><td>`Rotation`</td><td>`create(<<rotation>>; create(<<vector>>; 0; 1; 0); angle)`</td></tr>
<tr><td>`rotationz(angle)`</td><td>`Rotation`</td><td>`create(<<rotation>>; create(<<vector>>; 0; 0; 1); angle)`</td></tr>
<tr><td>`translationm(x; y; z)`</td><td>`Matrix`</td><td>`create(<<matrix>>; 1; 0; 0; x; 0; 1; 0; y; 0; 0; 1; z; 0; 0; 0; 1)`</td></tr>
<tr><td>`vector(...)`</td><td>`Vector`</td><td>`create(<<vector>>; ...)`</td></tr>
</tbody>
</table>
</figure>

The following matrix functions were also added. These functions are following the same pattern previously established by the existing `minvert` and `mscale`.

<figure class="wp-block-table">
<table>
<thead><tr><th>New function</th><th>Description</th></tr></thead>
<tbody>
<tr><td>`mrotate`</td><td>Rotate given object.</td></tr>
<tr><td>`mrotatex`</td><td>Rotate given object around the X-axis.</td></tr>
<tr><td>`mrotatey`</td><td>Rotate given object around the Y-axis.</td></tr>
<tr><td>`mrotatez`</td><td>Rotate given object around the Z-axis.</td></tr>
<tr><td>`mtranslate`</td><td>Translate given object (`Rotation` objects will be returned as a `Placement` object)</td></tr>
</tbody>
</table>
</figure>

These functions return the same type of object which was supplied with the exception of `mtranslate`.

The functions can be chained together like so:

<pre class="wp-block-preformatted">=mtranslate(mrotatex(placement(vector(1; 2; 3); rotation(0; 0; 0)); 45); 1; 2; 3)</pre>

Thanks to Daniel-Khodabakhsh for this valuable contribution to FreeCAD's Expression API.