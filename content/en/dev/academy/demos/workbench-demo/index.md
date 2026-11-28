---
title: Demo - Minimal Workbench
description:
weight: 2
---

The smallest useful FreeCAD workbench: registers a new entry in the Workbench selector, contributes one command to a toolbar and menu, and prints a message to the Report view when the command is clicked.

Every file in this demo is dedicated to the public domain under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/). Copy and adapt freely.

## Directory layout

```
MinimalWorkbench/
├─ package.xml
└─ freecad/
   └─ MinimalWorkbench/
      ├─ resources/
      │  └─ icons/
      │     └─ Logo.svg
      ├─ __init__.py
      ├─ init_gui.py
      └─ commands.py
```

The top-level `MinimalWorkbench/` is your git repository root. The `freecad/` directory has no `__init__.py` because `freecad` is a [namespace package](https://peps.python.org/pep-0420/) shared with every other addon on the user's system. Your addon lives in `freecad/<YourAddonName>/`, and *that* directory has a normal `__init__.py`. See [Addon layout](layout) for background.

## The files

### `package.xml`

The [Addon Manifest](manifest) declares your addon's name, version, license, and content. For a workbench it must include a `<workbench>` content item whose `<classname>` matches the class registered in `init_gui.py`.

Source: [`package.xml`](Source/package.xml)

### `freecad/MinimalWorkbench/__init__.py`

Nearly empty. It only has to exist so that `freecad/MinimalWorkbench/` is treated as a proper Python package (as opposed to the enclosing `freecad/`, which is intentionally *not* a package).

Source: [`__init__.py`](Source/freecad/MinimalWorkbench/__init__.py)

### `freecad/MinimalWorkbench/init_gui.py`

The file FreeCAD runs when starting the GUI. It:

- Defines `MinimalWorkbench`, a subclass of `FreeCADGui.Workbench`.
- Sets `MenuText`, `ToolTip`, and `Icon` (what the user sees in the Workbench selector). Note that in a "real" addon we encourage [translating these strings](translate). The `Icon` attribute must be an absolute path resolved at class-definition time, so the file computes it from `__file__` rather than relying on a later `addIconPath` call.
- Defines `Initialize()`, which imports the `Commands` module (whose import side-effect is registering the command) and appends the command to a toolbar and menu.
- Returns `"Gui::PythonWorkbench"` from `GetClassName()`, which is required for Python workbenches. Do not modify that return string!
- Registers the workbench instance via `FreeCADGui.addWorkbench()`.

Source: [`init_gui.py`](Source/freecad/MinimalWorkbench/init_gui.py)

### `freecad/MinimalWorkbench/commands.py`

Defines `HelloCommand`, a class with:

- `GetResources()`: returns a dictionary with `MenuText` and `ToolTip` (and optionally `Pixmap` and `Accel`).
- `IsActive()`: returns `True` whenever the command should be enabled. Return `False` to grey out the toolbar button.
- `Activated()`: the code that runs when the user clicks the toolbar button.

At module import time the file calls `FreeCADGui.addCommand("Minimal_Hello", HelloCommand())`, registering the command by name so `init_gui.py` can refer to it.

Source: [`commands.py`](Source/freecad/MinimalWorkbench/commands.py)

## Trying it out

1. Install the addon by downloading [`MinimalWorkbench.zip`](MinimalWorkbench.zip) and extracting it into your FreeCAD user `Mod/` directory. To install from source instead, or to symlink for live edits, follow [Installing your addon locally](install).
2. Start FreeCAD. "Minimal" should appear in the Workbench selector.
3. Switch to the Minimal workbench. A single-button "Minimal" toolbar appears. Click it, and "Hello from the Minimal workbench!" will appear in the Report view.

## Where to go next

- [Workbench registration](workbenches) for a deeper walk-through of the Workbench class.
- [Gui Commands](commands) for more on commands, toolbars, and menus.
- [Icons & resources](icons) for how to give your commands and workbench real SVG icons.
