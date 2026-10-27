---
title: Manyfold - Now with FreeCAD Thumbnails
date: 2026-08-06
author: Jo Hinchliffe
draft: false
category: showcase
tags:
  - community
cover:
  image: james_FC_Manyfold_old_Icons.webp
  caption:
---


[Manyfold](https://manyfold.app/) is an open source self hosted web application which you can use to organise and share your CAD files. There's a public server over at [3Dprint.social](https://3dprint.social/dashboard) and it's well worth taking a look there to get an idea of how the platform looks and operates. It's pretty straightforward in that you can upload project files and mesh files, add descriptions and instructions to the listing and, crucially add one of a nice collection of licenses to your design.

You can also self host the platform and it's [pretty straightforward to get up and running](https://manyfold.app/get-started/installation). It's distributed as a docker container and there are clear instructions here allowing you to set it up easily on a variety of platforms. As well as a plain Docker install, there are instructions to get you up and running on NixOS, Kubernetes, Proxmox, Home Assistant addons and more.

It's an excellent tool and, recently they have added a nice feature which prompted this post, if you add a FreeCAD FCStd file on your self hosted Manyfold instance, it will render the project thumbnail in the file preview! An excellent addition. In the above images the thumbnails contain the older FreeCAD logo as the parts are taken from the FreeCAD parts library where the majority of parts were made with older FreeCAD versions. Be sure to check out the [public Manyfold server](https://3dprint.social/dashboard) and you can follow [Manyfold over on the fediverse.](https://mastodon.social/@manyfold@3dp.chat)
