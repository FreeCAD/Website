---
title: Design Guide
description: Guidelines for designers and developers about FreeCAD design.
weight: 5
---


FreeCAD is a highly modular, complex piece of design software which has been developed for over [20 years](https://wiki.freecad.org/History) by volunteer contributors from across the globe. Due to the nature of this organic growth, individuals have injected their own ideas and implementations without following a uniform design language for how the application should present itself to users as well as flow through its many features. As a result user feedback regarding aesthetic and usability were generally poor, despite a robust set of features.

This *Design Guide* is intended to present developers/designers a series of concepts and guidelines through which they may expand, extend and improve FreeCAD through improved user interactions and general consistency of appearance, structure, and behavior. As such, this should be considered a living document which may change to meet the needs of developers, designers, and users. It can potentially also help those who write documentation use consistent terminology.

This guide is the product of a Design Working Group consisting of community members; ensuring decisions made regarding the User Interface and User Experience are consistent with the needs of people who actually use FreeCAD in both professional and hobbyist environments. This working group will also be involved with review of interface/experience related changes to FreeCAD to provide input to developers and maintainers regarding the merits and consistency of features which may impact interaction and/or workflows.

*The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt).*


### How to use this guide:

This guide is organized into multiple documents as outlined above, for the purpose of aiding developers in finding relevant content without excess information. Newcomers to FreeCAD, and this Design Guide, should familiarize themselves with the principles and assumptions which were used as the foundation on which these guidelines were built before progressing to more targeted content. The rest of the sections are organized in a manner of logical hierarchy of concepts and guidelines starting with more conceptual matter and moving on towards greater levels of detail.


### Assumptions:

The interface is tailored around a 1920 x 1080 standard resolution.

According to the [*Steam monthly hardware survey*](https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam), over 90% of all computer displays utilize 1920x1080 or higher resolution. The user interface for FreeCAD shall be optimized for this recommended resolution at 100% scaling. This shall be the "reference resolution" for the remainder of this design guide.

**Note:** For operating system specific elements Windows is considered the standard due to market share (70% in 2023). Every effort should be made to maintain a uniform appearance across platforms.

**Note:** Deviations from the prescriptive guidelines in this design document require justification utilizing sound reasoning and require a design review that such deviation(s) are both warranted and fit within the needs of the user without degrading the overall consistency of the user experience.


### TODO

- Interactive Controls (Still under development)

- Colors and Accessibility (Still under development)

- Theme/Styling (Still under development)

- Icons/Art (Still under development)