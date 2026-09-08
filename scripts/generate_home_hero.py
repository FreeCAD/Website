"""Generate one homepage hero capture with FreeCAD's real 3D viewport.

Set HOMEPAGE_HERO_CAPTURE to ``desktop`` or ``mobile``. Run FreeCAD with an
isolated user configuration (``--user-cfg`` and ``--system-cfg``) because the
capture intentionally changes UI preferences. Each capture runs in its own
process so the Start workbench cannot steal focus on resize.
"""

import os
from pathlib import Path

if os.environ.get("HOMEPAGE_HERO_ISOLATED_CONFIG") != "1":
    raise RuntimeError(
        "Run this generator through scripts/capture_home_hero.sh so FreeCAD uses isolated preferences"
    )

import FreeCAD as App
import FreeCADGui as Gui
import Part
from PySide import QtWidgets


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "themes/trigo/assets/images/home/hero"
MODEL_OUTPUT = OUTPUT_DIR / "freecad-parametric-bracket.FCStd"
UI_OUTPUT = OUTPUT_DIR / "freecad-parametric-bracket-ui-desktop.png"
MOBILE_UI_OUTPUT = OUTPUT_DIR / "freecad-parametric-bracket-ui-mobile.png"
CAPTURE = os.environ.get("HOMEPAGE_HERO_CAPTURE", "desktop")
if CAPTURE not in {"desktop", "mobile"}:
    raise ValueError("HOMEPAGE_HERO_CAPTURE must be 'desktop' or 'mobile'")

view_preferences = App.ParamGet("User parameter:BaseApp/Preferences/View")
view_preferences.SetBool("ShowNaviCube", True)
# AntiAliasing stores FreeCAD's enum value; 3 corresponds to 4x MSAA.
view_preferences.SetInt("AntiAliasing", 3)
view_preferences.SetBool("Simple", False)
view_preferences.SetBool("Gradient", True)
view_preferences.SetBool("UseBackgroundColorMid", True)
view_preferences.SetUnsigned("BackgroundColor", 0xECEFF1FF)
view_preferences.SetUnsigned("BackgroundColor2", 0xD8DDE1FF)
view_preferences.SetUnsigned("BackgroundColor4", 0xF4F5F6FF)
view_preferences.SetUnsigned("BackgroundColor3", 0xC9D0D5FF)
unit_preferences = App.ParamGet("User parameter:BaseApp/Preferences/Units")
unit_preferences.SetInt("UserSchema", 0)
unit_preferences.SetInt("Decimals", 1)
document_preferences = App.ParamGet("User parameter:BaseApp/Preferences/Document")
document_preferences.SetBool("CreateBackupFiles", False)
dock_preferences = App.ParamGet("User parameter:BaseApp/Preferences/DockWindows")
dock_preferences.SetBool("ActivateOverlay", True)
dock_preferences.GetGroup("ComboView").SetBool("Enabled", True)
dock_preferences.GetGroup("TreeView").SetBool("Enabled", False)
dock_preferences.GetGroup("PropertyView").SetBool("Enabled", False)
main_window_preferences = App.ParamGet("User parameter:BaseApp/Preferences/MainWindow")
main_window_preferences.SetString("OverlayActiveStyleSheet", "Freecad Overlay.qss")
view_preferences.SetBool("DockOverlayAutoView", False)
view_preferences.SetBool("DockOverlayActivateOnHover", False)
overlay_left_preferences = App.ParamGet("User parameter:BaseApp/MainWindow/DockWindows/OverlayLeft")
overlay_left_preferences.SetString("Widgets", "Model")
overlay_left_preferences.SetInt("Width", 300)


def rounded_plate(length, width, radius, height):
    core_x = Part.makeBox(length - 2 * radius, width, height, App.Vector(radius, 0, 0))
    core_y = Part.makeBox(length, width - 2 * radius, height, App.Vector(0, radius, 0))
    corners = [
        Part.makeCylinder(radius, height, App.Vector(x, y, 0))
        for x in (radius, length - radius)
        for y in (radius, width - radius)
    ]
    return core_x.fuse(core_y).fuse(corners)


doc = App.newDocument("HomepageHero")

# A parameter-driven clevis bracket: recognizable at a glance and detailed
# enough to communicate real mechanical design without visual clutter.
length, width, base_height = 110.0, 68.0, 8.0
base = rounded_plate(length, width, 7.0, base_height)
for x in (14.0, length - 14.0):
    for y in (14.0, width - 14.0):
        base = base.cut(Part.makeCylinder(4.0, base_height, App.Vector(x, y, 0)))

base_obj = doc.addObject("PartDesign::Feature", "BasePlate")
base_obj.Label = "Mounting base (110 × 68 × 8 mm)"
base_obj.Shape = base
base_obj.addProperty("App::PropertyLength", "Length", "Parameters").Length = length
base_obj.addProperty("App::PropertyLength", "Width", "Parameters").Width = width
base_obj.addProperty("App::PropertyLength", "Thickness", "Parameters").Thickness = base_height

lug_shapes = []
for y in (16.0, 44.0):
    upright = Part.makeBox(46.0, 8.0, 35.0, App.Vector(32.0, y, base_height))
    crown = Part.makeCylinder(23.0, 8.0, App.Vector(55.0, y, 43.0), App.Vector(0, 1, 0))
    lug = upright.fuse(crown)
    bore = Part.makeCylinder(11.0, 8.0, App.Vector(55.0, y, 43.0), App.Vector(0, 1, 0))
    lug_shapes.append(lug.cut(bore))

lugs_obj = doc.addObject("PartDesign::Feature", "BearingLugs")
lugs_obj.Label = "Parametric bearing lugs"
lugs_obj.Shape = lug_shapes[0].fuse(lug_shapes[1])
lugs_obj.addProperty("App::PropertyLength", "BoreDiameter", "Parameters").BoreDiameter = 22.0
lugs_obj.addProperty("App::PropertyLength", "LugSpacing", "Parameters").LugSpacing = 28.0

gusset_objects = []
for y in (16.0, 52.0):
    gusset = Part.makePolygon(
        [App.Vector(32, y, base_height), App.Vector(18, y, base_height), App.Vector(32, y, 31), App.Vector(32, y, base_height)]
    )
    face = Part.Face(gusset)
    obj = doc.addObject("PartDesign::Feature", f"Gusset{int(y)}")
    obj.Label = "Structural gusset"
    obj.Shape = face.extrude(App.Vector(0, -8 if y > width / 2 else 8, 0))
    gusset_objects.append(obj)

pin = Part.makeCylinder(9.0, 54.0, App.Vector(55.0, 7.0, 43.0), App.Vector(0, 1, 0))
pin_obj = doc.addObject("PartDesign::Feature", "Pin")
pin_obj.Label = "Removable pivot pin (Ø18 mm)"
pin_obj.Shape = pin
pin_obj.addProperty("App::PropertyLength", "Diameter", "Parameters").Diameter = 18.0

doc.recompute()
doc.saveAs(str(MODEL_OUTPUT))

base_obj.ViewObject.ShapeColor = (0.72, 0.76, 0.82)
base_obj.ViewObject.LineColor = (0.12, 0.16, 0.22)
lugs_obj.ViewObject.ShapeColor = (0.82, 0.85, 0.90)
lugs_obj.ViewObject.LineColor = (0.10, 0.14, 0.20)
for obj in gusset_objects:
    obj.ViewObject.ShapeColor = (0.28, 0.58, 0.82)
pin_obj.ViewObject.ShapeColor = (0.20, 0.52, 0.82)

view = Gui.activeDocument().activeView()
Gui.activateWorkbench("PartDesignWorkbench")
main_window = Gui.getMainWindow()
main_window.menuBar().hide()
main_window.statusBar().hide()

kept_toolbars = {
    "Workbench",
    "View",
    "Part Design Modeling Features",
    "Part Design Dress-Up Features",
}
for toolbar in main_window.findChildren(QtWidgets.QToolBar):
    toolbar.setVisible(toolbar.windowTitle() in kept_toolbars)

combo_view = main_window.findChild(QtWidgets.QDockWidget, "Combo View")
if combo_view is None:
    combo_view = main_window.findChild(QtWidgets.QDockWidget, "Model")
if combo_view:
    combo_view.show()
    combo_view.setMinimumWidth(300)

for dock in main_window.findChildren(QtWidgets.QDockWidget):
    if dock is not combo_view:
        dock.hide()

Gui.Selection.clearSelection()
Gui.Selection.addSelection(pin_obj, "Edge1")
view.setAnimationEnabled(False)
view.setCornerCrossSize(0)
Gui.updateGui()
view.setCameraOrientation((0.424708, 0.175920, 0.339851, 0.820473))
view.fitAll(0.84)
view.redraw()
Gui.updateGui()

mdi_area = main_window.findChild(QtWidgets.QMdiArea)
if mdi_area:
    document_window = None
    for subwindow in mdi_area.subWindowList():
        if "start" in subwindow.windowTitle().lower():
            subwindow.close()
            subwindow.deleteLater()
        else:
            document_window = subwindow
    if document_window:
        mdi_area.setViewMode(QtWidgets.QMdiArea.TabbedView)
        mdi_area.setActiveSubWindow(document_window)
Gui.updateGui()

if mdi_area:
    for tab_bar in mdi_area.findChildren(QtWidgets.QTabBar):
        tab_bar.hide()
Gui.updateGui()

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def capture_interface(path, width, height, fit_factor):
    main_window.resize(width, height)
    if mdi_area:
        for subwindow in mdi_area.subWindowList():
            if "start" in subwindow.windowTitle().lower():
                subwindow.close()
                subwindow.deleteLater()
        if document_window:
            mdi_area.setViewMode(QtWidgets.QMdiArea.TabbedView)
            mdi_area.setActiveSubWindow(document_window)
    view.fitAll(fit_factor)
    view.redraw()
    for _ in range(3):
        Gui.updateGui()
    main_window.grab().save(str(path))


if CAPTURE == "desktop":
    capture_interface(UI_OUTPUT, 1600, 900, 0.88)
else:
    capture_interface(MOBILE_UI_OUTPUT, 1000, 680, 0.88)
App.closeDocument(doc.Name)
main_window.close()
