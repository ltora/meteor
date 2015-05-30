import wx
import wx.lib.scrolledpanel

class GUI(wx.Frame):

    def __init__(self,parent,id,title):
        #First retrieve the screen size of the device
        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0] - 200
        screenHeight = screenSize[1] - 200

        #Create a frame
        wx.Frame.__init__(self,parent,id,title,size=(screenWidth,screenHeight), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        panel1 = wx.Panel(self,size=(screenWidth,28), pos=(0,0), style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour('#FDDF99')
        _ = wx.StaticText(panel1, -1, "This is panel 1...")
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,screenHeight), pos=(0,28), style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')

        #bSizer = wx.BoxSizer( wx.VERTICAL )

        #for i in range(100):
        #    _ = wx.Button(panel2, label="Button %d" % i, pos=(0,50+i*50), size=(-1,40))
        #    bSizer.Add(_, 0, wx.ALL, 5)
        #panel2.SetSizer( bSizer )

        dc = wx.AutoBufferedPaintDC(panel2)
        dc.SetPen(wx.Pen(wx.RED, 5))
        dc.DrawCircle(screenWidth/2,screenHeight/2,100)
        panel2.Refresh()


if __name__=='__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="Test")
    frame.Show()
    app.MainLoop()

