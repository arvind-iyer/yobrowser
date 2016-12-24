#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit

class Handler:
    def back_clicked(self, button):
        browserholder.go_back()

    def refresh_clicked(self, button):
        browserholder.reload()

    def enterkey_clicked(self, button):
        browserholder.load_uri(urlentry.get_text())

builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")

browserholder = WebKit.WebView()
browserholder.set_editable(False)
#browserholder.load_html_string("<b>Yeezus</b>", "file://")
browserholder.load_uri("http://www.google.com")

urlentry = builder.get_object("entry1")
urlentry.set_text("https://google.com")

scrolled_window = builder.get_object("scrolledwindow1")
scrolled_window.add(browserholder)

browserholder.show()

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

