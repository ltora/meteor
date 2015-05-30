import time
import wx
from random import randint

class View(wx.Panel):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
    def on_size(self, event):
        event.Skip()
        self.Refresh()
    def on_paint(self, event):
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.Clear()
        dc.DrawLine(0, 0, w, h)
        dc.SetPen(wx.Pen(wx.RED, 5))
        dc.DrawCircle(w / 2, h / 2, 100)

        dc.SetPen(wx.Pen(wx.RED,1))
        dc.DrawPointPoint((200,140))
        
        start = time.time()
        for j in xrange(400):
            for i in xrange(400):
                dc.SetPen(wx.Pen(wx.Colour(randint(0,255),randint(0,255),randint(0,255)),1))
                dc.DrawPointPoint((i,j))

        #print "setting up..."
        #xy = []
        #p = []
        #for j in xrange(400):
        #    for i in xrange(400):
        #        p.append(wx.Pen(wx.Colour(randint(0,255),randint(0,255),randint(0,255)),1))
        #        xy.append((i,j))

        #start = time.time()
        #dc.DrawPointList(xy, pens=p)
        print "drawing took %f sec" % (time.time()-start)


class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('My Title')
        self.SetClientSize((500, 500))
        self.Center()
        self.view = View(self)

def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()

