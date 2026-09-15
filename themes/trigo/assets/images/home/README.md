# Homepage image provenance

This directory contains prepared homepage artwork. Keep this manifest updated
when an image is replaced or regenerated.

## Workflow artwork

The workflow images are derived from FreeCAD splash-screen artwork added in
[FreeCAD commit `18db68ab`](https://github.com/FreeCAD/FreeCAD/commit/18db68ab848ff95962ab81c3bf977c99291434e6)
and later discussed in
[FreeCAD pull request #32363](https://github.com/FreeCAD/FreeCAD/pull/32363#discussion_r3923137224).
The source repository distributes contributions under LGPL-2.1-or-later.

| Website asset | Upstream source | Model credit | Local transformation |
| --- | --- | --- | --- |
| `workflows/design-clean.png` | [`freecadsplash2.png`](https://github.com/FreeCAD/FreeCAD/blob/e42623bcca66958c20c2d49c12902f21f56186db/src/Gui/Icons/freecadsplash2.png) | Xpendable | Removed the splash frame, logo, labels, and grid; placed the isolated model on a transparent 1200×720 canvas. |
| `workflows/architecture-clean.png` | [`freecadsplash0.png`](https://github.com/FreeCAD/FreeCAD/blob/e42623bcca66958c20c2d49c12902f21f56186db/src/Gui/Icons/freecadsplash0.png) | Stefano Moser | Removed the splash frame, logo, labels, and grid; placed the isolated model on a transparent 1200×720 canvas. |
| `workflows/manufacturing-clean.png` | [`freecadsplash8.png`](https://github.com/FreeCAD/FreeCAD/blob/e42623bcca66958c20c2d49c12902f21f56186db/src/Gui/Icons/freecadsplash8.png) | cyborg_ar | Removed the splash frame, logo, labels, and grid; placed the isolated model on a transparent 1200×720 canvas. |
| `workflows/analysis-clean.png` | [`freecadsplash1.png`](https://github.com/FreeCAD/FreeCAD/blob/e42623bcca66958c20c2d49c12902f21f56186db/src/Gui/Icons/freecadsplash1.png) | NewJoker | Removed the splash frame, logo, labels, and grid; placed the isolated model on a transparent 1200×720 canvas. |

## Hero artwork

The hero model and screenshots were created for this website using
`scripts/generate_home_hero.py`. The generator creates
`hero/freecad-parametric-bracket.FCStd` and captures the desktop or mobile
FreeCAD interface. Run it through the isolated launcher so it cannot overwrite
the user's normal FreeCAD preferences:

```sh
FREECAD_EXECUTABLE=/path/to/FreeCAD scripts/capture_home_hero.sh desktop
FREECAD_EXECUTABLE=/path/to/FreeCAD scripts/capture_home_hero.sh mobile
```

The generator source and website-authored model are MIT-licensed with the
website. The screenshots also depict FreeCAD's LGPL-2.1-or-later interface and
icons.
