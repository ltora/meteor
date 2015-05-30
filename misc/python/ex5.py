#!/usr/bin/env python

"""GTK rectangle drawing speed test, GDK vs. Cairo

David Ripton 2008-12-03
MIT license
"""

import time
import random

import gtk

NUM_RECTS = 500

handle_id = None

def main():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)
    window.set_default_size(800, 600)
    vbox = gtk.VBox()
    window.add(vbox)
    area = gtk.DrawingArea()
    vbox.pack_start(area)
    gdk_button = gtk.Button("GDK")
    gdk_button.connect("clicked", on_gdk_button_clicked, area)
    vbox.pack_start(gdk_button, expand=False)
    cairo_button = gtk.Button("Cairo")
    cairo_button.connect("clicked", on_cairo_button_clicked, area)
    vbox.pack_start(cairo_button, expand=False)
    window.show_all()
    gtk.main()

def on_gdk_button_clicked(button, area):
    global handle_id
    if handle_id is not None:
        area.disconnect(handle_id)
    handle_id = area.connect("expose-event", on_area_exposed_gdk)
    area.queue_draw()

def on_cairo_button_clicked(button, area):
    global handle_id
    if handle_id is not None:
        area.disconnect(handle_id)
    handle_id = area.connect("expose-event", on_area_exposed_cairo)
    area.queue_draw()

def on_area_exposed_gdk(area, event):
    t0 = time.time()
    width, height = area.window.get_size()
    colormap = area.get_colormap()
    gc = area.get_style().fg_gc[gtk.STATE_NORMAL]
    for ii in xrange(NUM_RECTS):
        r = random.randrange(0, 65535 + 1)
        g = random.randrange(0, 65535 + 1)
        b = random.randrange(0, 65535 + 1)
        gc.foreground = colormap.alloc_color(r, g, b)
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        w = random.randrange(0, width - x)
        h = random.randrange(0, height - y)
        area.window.draw_rectangle(gc, True, x, y, w, h)
    t1 = time.time()
    print "gdk drew %d rectangles in %f seconds" % (NUM_RECTS, t1-t0)

def on_area_exposed_cairo(area, event):
    t0 = time.time()
    cr = area.window.cairo_create()
    width, height = area.window.get_size()
    for ii in xrange(NUM_RECTS):
        r = random.random()
        g = random.random()
        b = random.random()
        a = random.random()
        cr.set_source_rgba(r, g, b, a)
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        w = random.randrange(0, width - x)
        h = random.randrange(0, height - y)
        cr.rectangle(x, y, w, h)
        cr.fill()
    t1 = time.time()
    print "cairo drew %d rectangles in %f seconds" % (NUM_RECTS, t1-t0)

if __name__ == "__main__":
    main()

