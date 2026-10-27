---
title: FreeCAD - It IS Rocket Science!
date: 2026-04-03
author: Jo Hinchliffe
draft: false
category: showcase
tags:
  - addon
  - community
  - user story
cover:
  image:
  caption:
---


{{< youtube id=IgRgFM0k-M0 title="Assessing the Accuracy of Aerodynamics Simulation Through CFD and Flight Testing-Karbon" loading=lazy >}}

In full disclosure the author of this post is involved in model, amateur and high power rocketry so forgive their over excitement!

The [National Association of Rocketry](https://www.nar.org/) in the USA has run NARCON a rocketry themed convention for many years and recently has moved to vNARCON moving the majority of activity online. After the event the videos are put online and it's always chock full of useful information and developmental knowledge for the global rocketry community.

In recent years FreeCAD has increased in visibility in rocketry communities, thanks mainly to the [amazing rocketry workbench](https://github.com/davesrocketshop/Rocket) built by fabulous FreeCAD Contributor Davesrocketshop. The Rocket workbench makes it really simple to create complete rocket designs or rocket components from either open databases of known rocketry components or using your own parameters. It's an amazing tool for creating CAD components for 3D printing, laser cutting and more. As part of designing rockets the designer is concerned about stability as well as general flight dynamics, how high can it fly is not only of interest in terms of the information needed for a safe and successful flight.

There are numerous tools that help people somewhat analyse and simulate their rocket designs, [Openrocket](https://openrocket.info/) is an excellent and popular open source tool which has some crossover features and approaches with the FreeCAD Rocketry Workbench. There are also proprietary rocket design tools, primarily RockSim and then there is a free to use closed source windows package called RASAero II. It's been noted that all of these tend to differ slightly in their stability analysis in part due to them using slightly different analytical techniques (Openrocket uses Barrowman methods, Rocksim uses a proprietary extended Barrowman system and RASAero uses a Rogers Modified Barrowman system).

In the above video Ken steps through elegantly how he has used FreeCAD and the [CfdOF Workbench](https://wiki.freecad.org/CfdOF_Workbench) to analyse rocket designs using Computational Fluid Dynamics (CFD). This is incredibly interesting for rocketry people as it offers a completely different approach to stability and drag analysis and has shown some interesting results compared to other methods. Notably there has been a long standing set of community held beliefs around how much drag is created by the addition of different types of launch rail attachments (small lugs or tubes or conformal parts added to the outside of rockets to attach them to the launch rail). Some of these beliefs are based on tiny amounts of wind tunnel data from the 1960's and this data is still being used by some of the rocket analysis tools mentioned above. It's fabulous to see FreeCAD being used to develop deeper understanding and practice in the rocketry community. We wish everyone there blue skies and low winds for happy launching!
