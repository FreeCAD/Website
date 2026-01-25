---
title: Vancouver Hackathon Wrap-up
date: 2023-08-14
authors: Chris Hennes
draft: false
categories: event
tags:
- hackathon
cover:
  image:
  caption:
---

As I write this we are just wrapping up the [FreeCAD Hackathon 2023](https://blog.freecad.org/2023/05/24/freecad-hackathon-11-13-august-2023/) in Vancouver, BC. The coffee is gone, the laptop batteries are drained, and everyone present (physically and virtually) is winding up their weekend projects.

The weekend featured a variety of different activities, ranging from presentations from **Dr. Aik-Siong Koh **about his recent work on [a new LGPL'ed 3D constraints solver for assemblies](https://github.com/Ondsel-Development/OndselSolver) and from **Ajinkya Dahale** on his work towards a [custom properties system](https://ondsel.com/blog/build-system-for-custom-data-elements/), to audio conferences via [the Discord channel](https://discord.gg/w2cTKGzccC) with FreeCAD users and developers from across the world, to just a bunch of devs sitting around hacking on FreeCAD and occasionally asking each other for help or input.

### Major Topics

**Version 1.0 Release Roadmap**. The first order of business was to discuss the [Roadmap to v1.0](https://freecad.github.io/DevelopersHandbook/roadmap/). The general consensus was that there are four main focus areas that must be addressed before a 1.0 release:

1. Mitigating the topological naming problem

2. Integrating a default Assembly workbench

3. Creating a unified Material-handling system

4. Improving the basic user experience

We also discussed a need to improve terminology as a sub-focus area for v1.0, which is closely tied to item 4. In fact, nearly all remaining discussion for the weekend focused on one or more of those four items.

**Assembly Workbench**. It came up at FreeCAD Day 2023, it comes up in the forums on a regular basis, and it comes up in discussions with end users: FreeCAD needs a default, built-in Assembly workbench. It does not necessarily have to have every possible sort of workflow, or solve all assembly-related problems, but it should at the least address basic assembly tasks. Ondsel published a [series of blog posts](https://ondsel.com/blog/default-assembly-workbench-7/) detailing that company's analysis of the situation, and in recent months they have been actively working to develop one of the core technologies anticipated for that workbench: a fully 3D constraint solver with a compatible license. The next order of business was to decide which of the various available paths we intend to follow:

1. Integrate the new solver into @realthunder's Assembly 3 Workbench, and then integrate that external workbench directly into FreeCAD. @realthunder seems very enthusiastic about the new solver, so it seems likely that at least the first part of this will happen in very short order.

2. Integrate @zolko's Assembly 4 Workbench into FreeCAD and extend it to include the solver.

3. Develop a new Assembly user interface directly in FreeCAD, taking inspiration from Asm3 and Asm4 and combining those ideas into a simplified, streamlined workbench.

In general it was felt that Assembly 3's user interface was too complex to be integrated on its own, and that Assembly 4's lack of solver presented a significant challenge to direct adoption. Therefore the planned approach is to create a new solver user interface in FreeCAD that provides simplified access to the most common assembly tools, and that provides a standard API for assemblies that external workbench authors can use to be compatible with both that workbench and each other.

**User Interface Colors.** FreeCAD's default background gradient and the color scheme of various UI elements present a nearly unusable interface for those with color vision deficiency, and the low contrast inherent in the current design presents some visual challenges even for those without vision impairment. A group of developers and users met (virtually) to discuss the ongoing research project of theme developer **@Obelisk**, who is attempting to create both a set of new light and dark themes based on existing work from a number of other theme authors, as well as to adapt the color scheme of the "classic" FreeCAD experience to be more friendly to everyone. While we don't expect this work to be without controversy, having a solid technical basis for making these sorts of decisions will help us to move forward with the project.

**Integrating a Rust Library.** A [very appealing project](https://github.com/jbuckmccready/cavalier_contours) from the Rust world led to a discussion about the feasibility of integrating a Rust library into our codebase for use in the Path workbench. There are a variety of pros and cons related mostly to packaging issues (and no, we did _not_ discuss rewriting FreeCAD in Rust!) but the overall consensus was that the upside of the advanced library outweighed the downside of packaging complexity, and that it is worth attempting in this limited application to see how it goes.

**Toponaming Next Steps**. **@JohnAD**, Ondsel Developer and team lead for the TNP mitigation project worked with various developers to work out what the next phase of that project looks like, and published the next set of steps we need to undertake. Things get exciting right about now, as we [actually begin using the system to track element history](https://github.com/FreeCAD/FreeCAD/issues/8432). Help wanted! If you are interested in learning what this TNP thing is all about, and want to assist in the project, [drop me a line](mailto:chennes@freecad.org) and I'll get you an invite to the group Telegram chat.

**Task panel, tree view, and stealing focus (oh my!)**. At the [FreeCAD Day meetup at FOSDEM in Brussels](https://blog.freecad.org/2023/02/06/freecad-day-2023-wrap-up/) earlier this year, a consistent user complaint had to do with interactions between the Task Panel, the Tree View, and various ways that things could go awry when using them. That continued to be an active area of discussion at the event this weekend, with various proposals for helping to mitigate these sorts of problems. There were a number of proposed solutions, but be on the lookout in the coming months for PR's related to a "Speed Bar."

**And more!** Dozens of other smaller discussions cropped up during the event: switching from toolbars to a ribbon, improving the documentation, cleaning up the tracker, not moving our toolbars around(!!), and improving the naming of things, just to name a few.

Thanks to everyone who attended, in person and virtually. I hope that we can have more of these meetups, across the globe, as FreeCAD development moves forward. We don't have any official dates yet for FOSDEM 2024 (likely early February), but you can be assured that FreeCAD developers and users will certainly coordinate a meeting around that event. I have heard of a couple of other groups looking to plan events: if you are interested, please reach out to the [FreeCAD Project Association](https://fpa.freecad.org) -- funding is available!