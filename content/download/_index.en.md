---
title: "Download"
description: "Launch Into Design!"
date: 2024-05-22T08:04:23+12:00
author: "FreeCAD"
cover:
  image: 4.webp
  caption: "a cover caption"
  alt: "a cover alternative title"
menus:
  main:
    weight: 3
  footer:
    weight: 3
params:
  subtitle: "Current stable version"
  platforms:
    - id: windows
      label: Windows
      order: 1
      downloads:
        - key: msi
          label: Windows x86_64 Installer
          alt: WINDOWS-MSI
        - key: zip
          label: Windows x86_64 Portable
          alt: WINDOWS-ZIP
    - id: mac
      label: macOS
      order: 2
      downloads:
        - key: x86
          label: macOS Intel x86
          alt: MACOS-X86
        - key: arm
          label: macOS Apple Silicon
          alt: MACOS-ARM
    - id: linux
      label: GNU/Linux
      order: 3
      downloads:
        - key: x86
          label: GNU/Linux x86_64 AppImage
          alt: LINUX-X86
        - key: arm
          label: GNU/Linux AArch64 AppImage
          alt: LINUX-AARCH64
---

{{< box text-align="justify" background="var(--tone)" >}}

{{< column content="![A image text alt text](4.webp 'An image caption')" />}}

{{< column >}}

## Column shortcode in first box shortcode

This is a text in first column of the second box with `text-align="justify" background="var(--tone)"`. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{{< /column >}}

{{< /box >}}


{{< box title="Title of the second box shortcode with `text-align=\"center\"`, `background=\"gold\"` and `color=\"red\"`" text-align="center" background="gold" color="red" >}}

{{< column >}}

## First column shortcode in second box shortcode

This is a text in the first column shortcode of the second box shortcode with `text-align="center"`.

{{< /column >}}

{{< column content="![An image in the second column of the second box alt text](4.webp 'An image in the second column shortcode of the second box shortcode caption')" />}}

{{< /box >}}
