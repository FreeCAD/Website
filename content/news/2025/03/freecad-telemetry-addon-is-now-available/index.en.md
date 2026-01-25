---
title: FreeCAD Telemetry Addon is now available
date: 2025-03-30
authors: Aleksandr Prokudin
draft: false
categories: announcement
tags:
- FPA
cover:
  image:
  caption:
---

Chris Hennes developed an _opt-in_ [Telemetry addon](https://github.com/FreeCAD/FreeCAD-Telemetry) to help the development team make good decisions and help answer questions like:

- How many people are affected by a given bug?

- How many people are running an addon that may be affected by an API change?

- Which platforms are the most popular and should receive the most development support?

- How many people are using a specific translation and would benefit from improving it?

- How long should we maintain support and documentation for older releases?

- How can we improve the default user experience based on how users customize FreeCAD?

- What grant applications should get priority?

To assist with that, the addon transmits select information about your copy of FreeCAD back to a central server.

The addon recently passed initial beta testing. If you are interested in helping developers gain more actionable data, please install it. That's all you need to do.

{{< youtube id=OluDQYR9HlQ title="YouTube video" loading=lazy >}}

## **FAQ**

**Is this an opt-in feature?**

Yes, you need to manually install the addon via the Addon Manager. You may need to update the cache in the Addon Manager first.

**Do you have plans to make this an opt-out feature later on?**

No, we have no such plans.

**What kind of information does it send?**

- FreeCAD preferences, including all customizations

- Essential system information (platform, architecture)

- The list of installed 3rd-party addons

- Data about incorrect shutdowns of FreeCAD

**Does the addon send any personal information?**

No. The addon collects only non-identifying telemetry data. Users get assigned random universally unique identifiers (UUIDs).

**Can I get a copy of the data that the addon collected about my copy of FreeCAD?**

Yes. Please follow [these instructions](https://github.com/FreeCAD/FreeCAD-Telemetry#requesting-a-copy-of-your-data).

**Can I opt out of sending telemetry data?**

Yes. Simply uninstall the addon.

**Can I request the removal of data that the addon sent from my computer?**

Yes. Please follow [these instructions](https://github.com/FreeCAD/FreeCAD-Telemetry#data-removal).

**Is the addon compliant with the GDPR?**

We currently use the [PostHog](https://posthog.com/) service, the data is retained in the EU.

**How can I make sure that the addon does what you claim it does?**

The source code is [available for inspection](https://github.com/FreeCAD/FreeCAD-Telemetry).

Once we collect a sufficient amount of data, we will start publishing it openly for everyone.

**Who is behind this project?**

Collecting useful telemetry data was discussed during a recent bi-monthly FreeCAD developer call. The code was written by Chris Hennes, one of FreeCAD's maintainers. The data is collected and stewarded by [The FreeCAD Project Association AISBL](https://fpa.freecad.org/).