---
title: A Research Grade Open Source Microscope
date: 2023-02-13
authors: Chris Hennes
draft: false
categories: showcase
tags:
- user story
- 3D printing
- research
- microscope
cover:
  image: PUMA_Frontice.png
  caption: Puma Microscope
---

The PUMA microscope is a low cost, modular, 3D printed, open source microscope designed in FreeCAD. Its modular nature allows re-use of many components to reconfigure the scope into a multitude of possible forms, from a basic mirror-illuminated simple microscope (middle) to a complex scope for serious research applications (right) - while still being fully portable!

_This guest article is by Dr Paul J. Tadrous, MB, BS, MSc, PhD. Dr Tadrous is a retired clinical pathologist in the UK. Although retired from clinical practice he continues to be active in research into microscopy, image processing, analysis and machine vision at TadPath Diagnostics, London, UK. **Contact**: [email](ptadrous@tadpath.co.uk), [YouTube](https://youtube.com/@PUMAMicroscope), and [Twitter](https://twitter.com/Paul_Tadrous). _

_If you are interested in writing an article for FreeCAD News, contact Chris Hennes at chennes@freecad.org._

## Introduction

![Puma Figure 1](PUMA_Figure_1.png "Puma Figure 1")

Figure 1. Sample images taken with PUMA configured to various optical modalities. A) Standard transillumination of stained plant cells in mitosis showing chromosomes. B) Unstained human buccal (inner cheek) cells with full aperture transillumination. C) Same specimen but with optical Schlieren phase contrast using a normal (i.e. non-phase) microscope objective. D) Same specimen but showing full phase contrast calculated from 4 Schlieren images. E) Dark ground microscopy of an unstained section of oak leaf. F) and G) Epi-illumination of a silicon chip die showing individual transistors (F) and a set of logic gates (G). H) Human striated muscle seen with crossed polarisation illumination, I) Thin section of a flower bud containing pollen grains, stained with fluorescein and imaged with epi-fluorescence.

The **P**ortable, **U**pgradeable, **M**odular, **A**ffordable (**PUMA**) microscope is an advanced open source (GPL v3) microscopy system designed to be built as a DIY project by anyone with access to low cost 3D printing and some basic hand tools [[1](#1)], [[2](#2)], [[3](#3)].

The scope has interchangeable modules that allow multiple imaging modalities including phase contrast, dark field, epi-illumination, polarisation and fluorescence microscopy (figure 1).

![Puma Figure 2](PUMA_Figure_2.png "Puma Figure 2")

Figure 2. The PUMA Abbe condenser (left and centre) allows for high numerical aperture (NA) imaging with a maximum NA of about 1.14 when oiled (about 0.92 dry) for high resolution, high magnification microscopy. An even higher NA illuminator is under development. One of the advantages of this condenser is the easy access it provides to the Fourier aperture of the scope by means of a simple filter slot (the 'Illuminating Aperture Diaphragm' or IAD slot). However, unlike most standard microscopes, PUMA does not restrict its users to simple round 'diaphragm' filters. The filters may be static, 3D printed, filters of custom aperture shape. The filter holders can also accept a 24 mm round glass coverslip on which more complex patterns of colour and shades of grey may be printed (not shown here). However, this 'filter' may instead be an active matrix translucent TFT-screen-based spatial light modulator (SLM) device bringing the advantage of computer control of the Fourier aperture with complex algorithmically calculated patterns of colour, shape and shades of grey (right - see also video 1).

https://videos.files.wordpress.com/VTsFcVJ8/video_1.mp4

Video 1. Demonstration of the PUMA Spatial Light Modulator (SLM). The first part of the video shows the SLM in front of a diffuse lamp and demonstrates a few of the simple apertures in black and white and colour that can be generated with the stock 'PUMA Control' software. These are only a small selection of the possible aperture functions that can be generated because the TFT - which only costs a few dollars - is capable of generating 65536 colours and shades of grey transparency (not just black, while and solid primary colours) and it can produce these in any pattern of over 45200 individually addressable pixel positions in its round field of view. The second part of the video gives a live demonstration showing how the SLM can be electronically switched between open aperture, Schlieren phase contrast and dark ground microscopy while viewing a live specimen under the microscope. Many more complex aperture functions and effects are possible. For more detailed information see this video:

{{< youtube id=yW9H66BlUjU title="How to build the Spatial Light Modulator for the PUMA 3D printed microscope" loading=lazy >}}

It also has some features not usually seen on even high end commercial lab microscopes such as a TFT-screen based spatial light modular (SLM) for Fourier optics effects (figure 2, video 1) and a user-programmable digital heads-up-display (HUD) that is superimposed onto the live optical image seen down the scope (not a digital overlay on a digital image stream) and multi-header capabilities. This HUD may be selectively optically erased in real time using polarisation to allow advanced augmented reality microscopy research, teaching and diagnostic assist applications (video 2).

https://videos.files.wordpress.com/l9lvNuQ1/video_2.mp4

Video 2. The PUMA Heads-Up Display or HUD is based on the same inexpensive TFT module that is used for the SLM. The first part of the video shows the view down the eyepiece with the HUD in action and the user controlling a cursor overlaid on the optical image to make some digital measurements while a timer ticks by in the right of the field of view. The integer number top right is an indication of the lamp current in mA. The second part of the video demonstrates how, using the rotatable polariser in the trinocular port of the PUMA microscope, the HUD overlay can be optically erased (because the HUD image itself is linearly polarised) whilst maintaining visibility of the HUD to a viewer using the top ocular port. This provides a clean (HUD-free) image at the trinocular outlet for image capture and analysis for augmented reality feedback applications. For more detailed information see this video:

{{< youtube id=Scaw8fW-bQM title="Augmented Reality Microscopy and the Trinocular Camera Port" loading=lazy >}}

All the 3D printable parts of the PUMA system were designed in FreeCAD and all the editable parametric FreeCAD models are freely available to download on the project GitHub site [[3](#3)] so anyone can customise the scope to meet their specific project needs.

## Why FreeCAD?

One important enabling factor for ground-breaking science is the ability of the user to understand their apparatus to the point where they can customise it to do their own innovative experiments as well as interpret the results correctly (e.g. they are aware of its limits and potential artefacts in the results). Commercial microscopes are difficult and expensive to customise (let alone to buy and maintain) and the more high tech ones seem to be incorporating more and more 'black box' features full of trade secrets, proprietary mechanisms and closed source software that are not feasible to customise without official company support (that may be quite expensive and the customisations may have corporate restrictions placed on their use or publication to protect intellectual property). Furthermore the researcher only has official company information about how (for example) a software algorithm works so may not be aware of certain factors in their results that might be due to specific coding implementation choices rather than natural responses of the experimental system under study. These are some of the arguments in favour of the use of fully open source software and hardware in scientific research.

Low cost 3D printing makes custom part manufacture affordable for anyone these days. The PUMA microscope project provides fully open source design specs for a high quality standard format microscope and for this to be most useful those designs must be available freely without such corporate restrictions and in a format that is easily (and freely) editable by the user into 3D printable models - not just static STL mesh files.

FreeCAD is free software that can produce such files for free distribution. But there are other well known commercial CAD packages that also have versions available currently free of monetary cost for some restricted uses, so why not use those instead? Well, to me, 'currently free of monetary cost for some restricted uses' is not a sufficient criterion on which to base an open science hardware project because one needs also to consider the future development of the project and the freedom of users to do what they need or want to do with the files and models without undue restrictions being placed on them. A common restriction for the free versions of some commercial CAD packages is that they may only be used for non-commercial purposes, but many researchers in universities work under grants that have tech-transfer clauses that seek to commercialise successful work. This means that either they can't use those restricted CAD packages or they must upgrade to a paid subscription version before they make any money (which they may never do if the commercialisation effort fails) or they must re-do all their models in a truly libre free CAD product if they want to progress to commercialisation.

The lack of open source code and the use of proprietary formats also may limit the use of CAD files generated by such 'free' commercial software either now or, perhaps more importantly, in the future should company policy change. For example, if I chose a 'free' commercial CAD package to make the designs of PUMA parts, the PUMA project could grind to a halt if an existing or new CEO or board of the CAD company decides to change their terms for use of their free versions or if they decide to revoke free use of their product or file formats at some stage in the future or prohibit the porting of their CAD files into other CAD packages without obtaining a paid license from them, and so forth.

With FreeCAD there is no risk of this because not only is it free of monetary cost but it is also libre and open source (including the file formats). Some people have commented that they tried FreeCAD some time ago and found it to be buggy or crashed often so they moved over to this or that other package. I started off with FreeCAD v0.17 a few years ago and, yes, it was a bit 'crashy' back then but I have seen the software make great improvements in stability over the last few years and it has not even reached v.0.3 yet (let alone v.1.0)! So I chose FreeCAD because it fits in with the open source customisable and libre-free nature of the PUMA project and ensures it will stay that way into the future.

## What makes PUMA different to other microscopes?

Compared to other open source microscopes there is no overall 'winner' because they each have their strengths and weaknesses.

PUMA is very well documented with a whole series of detailed 'How To' videos explaining its construction, theory and specs in addition to the documents on the project GitHub page and all editable parametric FreeCAD design files are provided - not fixed STL meshes - with video tutorials on how to edit them:

{{< youtube id=CPHyLTHID6g title="Customising PUMA - part 1: Design and FreeCAD file editing" loading=lazy >}}

PUMA is closer to conventional desktop microscope design compared to the other DIY microscopes and is particularly suited to ergonomical **_direct vision_** as opposed to being a 'camera-only' scope or smartphone-attachment scope.

Compared to their commercial counterparts, PUMA systems are ultra low cost , easy to customise, open source (no trade secrets) and highly portable. All the custom parts are designed in FreeCAD and 3D printable with a low cost printer such as the Ender 3 and all the other parts are generic fixtures and optics that can be bought from accessible online stores like AliExpress, eBay and Amazon. For example, to build a complete epifluorescence PUMA system, including 3D printing, fixtures, fittings, electronics and optics, the cost is typically around $100 USD if full DIY is used. Although commercial fluorescence microscopes would have a sturdier metal construction with more precise mechanical mechanisms and more convenient adjustments compared to the PUMA equivalent, if you are short of the $5000 (and sometimes considerably more) such a scope would cost you brand new then PUMA provides a functional alternative at a fraction of the price - great for home users or labs on a tight budget, esp. if you need multiple scopes for a practical teaching class or special research project.

In addition to diverse functionality and cost savings, PUMA boasts complete portability weighing just a few hundred grams e.g. 875 g (31 oz) for the fluorescence scope (including battery power supply and lamp), and even lighter - about 540 g (19 oz) for the basic transmitted light mirror-illuminated version of the scope (which can be seen in the middle of the frontice picture at the top of this article).

![Puma Figure 3](PUMA_Figure_3.png "Puma Figure 3")

Figure 3. Simultaneous multi-camera recording is possible with PUMA. The figure shows, from two different angles, the same PUMA microscope with its full Köhler illuminator fitted with 3 C-mount cameras for simultaneous recording of the same specimen (e.g. with different filters, magnifications, frame rates, etc.). The cameras are arbitrarily numbered 1 to 3. They do not all need to be of the same type or mounting. For example, video 4 shows an example recording from three different cameras. Although multi-camera adapters are available for commercial microscopes they are expensive.

https://videos.files.wordpress.com/rhHjPGzy/video_3.mp4

Video 3. Deployment of a fully functional (observation-ready) PUMA system in the field. The video shows the PUMA microscope with its full Köhler illuminator, Abbe condenser and LED lamp, PUMA Lite controller (including a 9V battery inside) which fits neatly under the scope for transport, advanced filter block and some microscope sampling accessories. The scope also has a focusing stepper motor attached although the slightly larger PUMA Control Console (illustrated in the frontice picture at the top of this article, on the right) would be necessary to operate that rather than the PUMA Lite. To see how easily and quickly a PUMA system can be 'field stripped' for transport:

{{< youtube id=6Yvc9X9xrKo title="How to Field Strip a PUMA Microscope" loading=lazy >}}

Portability of PUMA is further enhanced by the fact that it is designed as a primary vision microscope - i.e. one where the user looks down an eyepiece. This allows the user to get the full optical resolution and a complete wide field of view of their observations without the need for a smartphone or other computer-camera-monitor-power-supply combo (or 'camera-scopes' for short). Other 3D printed open source camera-scopes may look small and 'portable' until you take all these necessary accessories into full consideration at which point 'luggable' might be a more apt description. One of the biggest issues when using those camera-scopes for making **_observations_** out in the field (as opposed to **_recordings_** - we'll come back to that later) is that what the user can see at the time is restricted to a small field of view on a small portable screen such as a smartphone (if you want to boast portability) that is further limited by available power supply issues. If camera-scopes want to boast great resolution and wide field of view then they need large high resolution display monitors and wide field of view optics - which counters any claim to affordability let alone portability. Remember - for now I am only talking about making real-time observations out in the field - not stitching together many pictures recorded on a portable computer for study later, back at base, with a large desktop monitor. Hence PUMA was designed as a direct vision scope with the ability to use daylight or any suitable external light source so it can give high quality wide field of view real time optical microvision via an eyepiece in a truly portable way. Even the optional LED lamp and on-board microprocessor (an Arduino Nano) for the optional advanced TFT screen functions like the HUD are powered from one or two small domestic 9V batteries or solar rechargeable battery packs. Video 3 shows the deployment in the field of a fully functional complete PUMA system ready to make observations.

https://videos.files.wordpress.com/03Ac7Gxc/video_4.mp4

Video 4. Demonstration of a multi-camera recording of a live single cell organism with different modalities and magnifications, using PUMA.

All this 'direct vision' emphasis doesn't mean that PUMA can't do image recordings - on the contrary, the 'M' in PUMA stands for 'Modular' and there are several modules designed to allow high quality camera recordings - actually with up to three separate cameras recoding in different modalities simultaneously (figure 3, video 4). This is something that, to the best of my knowledge, has not been demonstrated to date with other 3D printed open source microscopes. PUMA can accept standard C-mount and CS-mount cameras as well as eyepiece cameras (including smart phone cameras if suitable adapters are used).


![Puma Figure 4](PUMA_Figure_4.png "Puma Figure 4")

Figure 4. The PUMA Köhler illuminator. Left: Design in FreeCAD exploded to show the various 3D printed components. The illuminator gives easy access to the Köhler field stop which, in many modern microscopes, is called the 'illuminated field diaphragm' or IFD but, as with the PUMA Abbe condenser, this is not restricted to a simple round shape diaphragm with PUMA. Right: From top to bottom we have part of Köhler's original publication highlighting his new IFD 'field stop' invention which, in German, he called the 'Sehfeldblende'; an example picture of a stained human skin biopsy taken with PUMA using this illuminator to show the crisp contrast and uniform illumination it affords - comparable to a modern professional microscope; and a photo of the illuminator fixed to a PUMA microscope with the small 'PUMA Lite' battery power supply. Details of the design, construction and use of this system are provided in this video:

{{< youtube id=XEE-el7vC5k title="How to build, collimate and use the Köhler Illuminator for the PUMA microscope" loading=lazy >}}

Another feature that sets PUMA apart from some other attempts at open source microscopes is its high quality illumination system. Mention has already been made of the Abbe condenser (figure 2). In addition PUMA has it's own portable full Köhler illuminator (figure 4) for even illumination and access to the Köhler field stop for more advanced photomicrography. Furthermore PUMA has a co-axial epi-illuminator module with several options for epi-polarisation and epi-fluorescence microscopy (see results shown in figure 1 and this video for details:

{{< youtube id=cAEB10K8PqI title="Epi-Illumination" loading=lazy >}}

Unlike some commercial portable microscopes that use their own special mini objectives that can only be used with their scopes, PUMA uses Royal Microscopical Society (RMS) standard optics and mechanical specifications so can accept a wide range of standard objectives and eyepieces either generic or from major microscope manufacturer brands.

## So is PUMA the perfect microscope for all?

Of course not! It does have its own limitations and peculiarities. These include that it can only accept one objective at a time - there is no rotatable objective turret. It also suffers from some 'wobble' and focus mechanism hysteresis which makes autofocus impractically slow. These limitations are partly matters of current design and also due to it being constructed of 3D printed plastic instead of precision machine-milled metal mechanisms. The current stage of the PUMA has limited space - it can handle a full standard microscope slide but nothing much bigger than that. It is also currently only of conventional 'upright' design. However, the modular, open source and fully customisable nature of PUMA mean that these obstacles can be addressed by future improvements in the designs and by the development of new modules - something which I am actively working on.

## What does the future hold for PUMA?

![Puma Figure 5](PUMA_Figure_5.png "Puma Figure 5")

Figure 5. Some prototype new modules in development. The final product may look quite different! A) A stabiliser bracket to minimise image vibrations, useful for high magnification image recordings. B) An adapter to allow the standard PUMA mirror illuminator module to direct daylight (or any other suitable plane wavefront illumination source) as input to the full Köhler illuminator.

### New Hardware

I am currently working on a stability bracket to reduce vibrations (figure 5a) and I used this with some success to take the oil immersion pictures of plant chromosomes seen in figure 1. Another recent development is the 'Daylight Köhler adapter' (figure 5b) which allows the full Köhler system to be used with natural daylight for enhanced portable power-saving use. I am also in the early stages of developing a precision motorised XYZ stage for automated tracking and scanning microscopy. All of these are not yet ready for release until thoroughly tested and documented. Further possibilities for the future include a Michelson interferometer module, new illumination modules (such as structured illumination, light sheet, etc.) and an inverted stage system to make PUMA useful for cell culture studies - but work on those modules has not begun at the time of writing this article.

### New Software

One of my aims is to help people do advanced microscopy with PUMA. I already started the PARDUS microscope control system for automated microscopy [[4](#4)] and hope to develop that in in conjunction with PUMA once the PUMA robotic XYZ stage is finalised. I also would like to create more dedicated software for Fourier aperture manipulation with the SLM of the scope but have not started work on that yet. Further software development will occur in conjunction with the educational outreach discussed next.

### Microscopy and image processing education

I would like to make a series of tutorials on the YouTube channel about image processing in microscopy using my free BiaQIm Image Processing Suite [[5](#5)] as a basis for work-along examples and the first video in the series has already been published [[6](#6)].

Most of the basics of microscopy theory have been covered already as 'theory sections' in the PUMA YouTube 'How To' videos published to date. In addition I would like to make a series of more advanced microscopy theory tutorials on topics such as Fourier optics, super-resolution, live cell imaging and deconvolution microscopy using PUMA as the hardware platform to exemplify these subjects.

### Funding for PUMA

All the above future development plans remain aspirational. If and when they can be delivered depends partly on the interest shown by people in the project and a lot on securing the necessary funding. To date (up to January 2023) PUMA has been a totally self-funded project. I intend to keep the PUMA resources free and open source for all but, of course, they are not free to develop and maintain. Buying components for prototyping, making documentation, videos and maintaining websites get more expensive all the time so I have recently set up a Patreon page [[7](#7)] and PayPal links [[8](#8)] to help make the project viable and sustainable into the future and complete all the aspirational developments mentioned above.

## References

[[1](#ref-1-2-3-return)] Tadrous, P. J. (2021). PUMA-An open‐source 3D‐printed direct vision microscope with augmented reality and spatial light modulator functions. Journal of Microscopy, 283(3), 259-280. [https://onlinelibrary.wiley.com/doi/10.1111/jmi.13043](https://onlinelibrary.wiley.com/doi/10.1111/jmi.13043)

[[2](#ref-1-2-3-return)] The PUMA Microscope YouTube Channel [https://youtube.com/@PUMAMicroscope](https://youtube.com/@PUMAMicroscope)

[[3](#ref-1-2-3-return)] The PUMA Microscope GitHub page [https://github.com/TadPath/PUMA](https://github.com/TadPath/PUMA)

[[4](#ref-4-return)] The PARDUS motor control GitHub page [https://github.com/TadPath/PARDUS](https://github.com/TadPath/PARDUS)

[[5](#ref-5-6-return)] My BiaQim Image Processing suite website [https://www.optarc.co.uk/bialith/](https://www.optarc.co.uk/bialith/)

[[6](#ref-5-6-return)] First PUMA image processing tutorial video [https://youtu.be/MZOCSkbz3ko](https://youtu.be/MZOCSkbz3ko)

[[7](#ref-7-8-return)] PUMA Microscope Patreon page: [https://www.patreon.com/PUMAMicroscope](https://www.patreon.com/PUMAMicroscope)

[[8](#ref-7-8-return)] PUMA PayPal donation: [https://www.paypal.com/donate/?hosted_button_id=NPMYJKJATDLQ4](https://www.paypal.com/donate/?hosted_button_id=NPMYJKJATDLQ4)