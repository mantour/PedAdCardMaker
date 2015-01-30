# -*- coding: utf-8 -*-
'''
Created on 2015/1/4

@author: sam
'''
import wx
import core
from frontend import AdCardMakerMainFrame

class MainApp(wx.App):
    def OnInit(self):
        frame = AdCardMakerMainFrame(None, core.main)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()