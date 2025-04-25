---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
description: "Please fill the description here"
date: {{ .Date }}
author: "FreeCAD"
draft: true
categories: category
tags:
  - tag
cover:
  image: relative_path_for_cover_image
  caption: "a cover caption"
  alt: "a cover alternative title"
---

# This is a generated news article thanks to the archetype.