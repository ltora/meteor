import wx
from wx.lib.floatcanvas import FloatCanvas


class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('My Title')
        self.SetClientSize((500, 500))
        self.Center()
        
        self.Canvas = FloatCanvas.FloatCanvas(self, -1,
                                     size=(500, 500),
                                     ProjectionFun=None,
                                     Debug=0,
                                     BackgroundColor="White",
                                     )


        # add a circle
        cir = FloatCanvas.Circle((10, 10), 100)
        self.Canvas.AddObject(cir)

        # add a rectangle
        rect = FloatCanvas.Rectangle((110, 10), (100, 100), FillColor='Red')
        self.Canvas.AddObject(rect)

        self.Canvas.Draw()

def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()

