# Encoding: utf-8
# Language: russian

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.Gdk import Screen


button_c = Gtk.Button(label = "C")
button_bs = Gtk.Button(label = "\u2b05")
button_plus = Gtk.Button(label = "+")
button_mc = Gtk.Button(label = "MC")
button_7 = Gtk.Button(label = "7")
button_8 = Gtk.Button(label = "8")
button_9 = Gtk.Button(label = "9")
button_minus = Gtk.Button(label = "-")
button_sqrt = Gtk.Button()
button_sqrt.set_property("label", "\u221A")
button_mr = Gtk.Button(label = "MR")
button_4 = Gtk.Button(label = "4")
button_5 = Gtk.Button(label = "5")
button_6 = Gtk.Button(label = "6")
button_multi = Gtk.Button(label = "*")
button_1divx = Gtk.Button(label = "1/x")
button_ms = Gtk.Button(label = "MS")
button_1 = Gtk.Button(label = "1")
button_2 = Gtk.Button(label = "2")
button_3 = Gtk.Button(label = "3")
button_div = Gtk.Button(label = "/")
button_powxy = Gtk.Button()
button_powxy.set_property("label", "x\u02b8")
button_mplus = Gtk.Button(label = "M+")
button_0 = Gtk.Button(label = "0")
button_00 = Gtk.Button(label = "00")
button_comma = Gtk.Button(label = ",")
button_eq = Gtk.Button(label = "=")
button_proc = Gtk.Button(label = "%")
button_minusplus = Gtk.Button(label = "-/+")


mainDisplay = Gtk.Entry(text="0", xalign=1, max_width_chars=14,
                        can_focus=False, hexpand=True, editable=False)
mainDisplay.set_property("name", "main_display")

memoryDisplay = Gtk.Entry(text="", xalign=0, width_chars=2,
                          max_width_chars=2, has_frame=True,
                          can_focus=False, editable=False)
memoryDisplay.set_property("name", "memory_display")

menuBar = Gtk.MenuBar()
menuBar.set_pack_direction(Gtk.PackDirection.LTR)

editMenuGroup = Gtk.MenuItem(label="Правка")
menuBar.add(editMenuGroup)

viewMenuGroup = Gtk.MenuItem(label="Вид")
menuBar.add(viewMenuGroup)

helpMenuGroup = Gtk.MenuItem(label="Cправка")
menuBar.add(helpMenuGroup)

css_provider = Gtk.CssProvider()
css_provider.load_from_path("pyculator.css")
style_context = Gtk.StyleContext()
style_context.add_provider_for_screen(Screen.get_default(), 
                                      css_provider,
                                      Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
                                      

                                      
class MainWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self)
        self.set_property("resizable", False)
        self.set_property("title", "pyCulator")
        self.set_property("border_width", 10)
        self.set_property("window_position", Gtk.WindowPosition.CENTER)

        self.connect("delete-event", Gtk.main_quit)
        
        mainContainer = Gtk.Box()
        mainContainer.set_property("orientation", Gtk.Orientation.VERTICAL)
        
        self.add(mainContainer)
        
        menuOverlay = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                              halign=Gtk.Align.START)
        displayOverlay = Gtk.Grid(halign=Gtk.Align.FILL, margin=2)
        buttonOverlay = Gtk.Grid(column_spacing=2, row_spacing=2)
 
        menuOverlay.pack_start(menuBar, True, True, 0)
        
        displayOverlay.attach(memoryDisplay, 0, 0, 1, 1)
        displayOverlay.attach(mainDisplay, 1, 0, 12, 1)

        buttonOverlay.attach(button_c, 0, 0, 1, 1)
        buttonOverlay.attach(button_powxy, 1, 0, 1, 1)
        buttonOverlay.attach(button_proc, 2, 0, 1, 1)
        buttonOverlay.attach(button_1divx, 3, 0, 1, 1)
        buttonOverlay.attach(button_plus, 4, 0, 1, 1)
        buttonOverlay.attach(button_sqrt, 5, 0, 1, 1)
        buttonOverlay.attach(button_mc, 0, 1, 1, 1)
        buttonOverlay.attach(button_7, 1, 1, 1, 1)
        buttonOverlay.attach(button_8, 2, 1, 1, 1)
        buttonOverlay.attach(button_9, 3, 1, 1, 1)
        buttonOverlay.attach(button_minus, 4, 1, 1, 1)
        buttonOverlay.attach(button_bs, 5, 1, 1, 1)
        buttonOverlay.attach(button_mr, 0, 2, 1, 1)
        buttonOverlay.attach(button_4, 1, 2, 1, 1)
        buttonOverlay.attach(button_5, 2, 2, 1, 1)
        buttonOverlay.attach(button_6, 3, 2, 1, 1)
        buttonOverlay.attach(button_multi, 4, 2, 1, 1)
        buttonOverlay.attach(button_minusplus, 5, 2, 1, 1)
        buttonOverlay.attach(button_ms, 0, 3, 1, 1)
        buttonOverlay.attach(button_1, 1, 3, 1, 1)
        buttonOverlay.attach(button_2, 2, 3, 1, 1)
        buttonOverlay.attach(button_3, 3, 3, 1, 1)
        buttonOverlay.attach(button_div, 4, 3, 1, 1)
        buttonOverlay.attach(button_eq, 5, 3, 1, 2)
        buttonOverlay.attach(button_mplus, 0, 4, 1, 1)
        buttonOverlay.attach(button_0, 1, 4, 1, 1)
        buttonOverlay.attach(button_comma, 2, 4, 1, 1)
        buttonOverlay.attach(button_00, 3, 4, 2, 1)
        
        mainContainer.pack_start(menuOverlay, True, True, 0)
        mainContainer.pack_start(displayOverlay, True, True, 0)
        mainContainer.pack_start(buttonOverlay, True, True, 0)
