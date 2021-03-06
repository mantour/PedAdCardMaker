# -*- coding: utf-8 -*-
"""Subclass of MainFrame, which is generated by wxFormBuilder."""

import wx
import frame

# Implementing MainFrame
class AdCardMakerMainFrame( frame.MainFrame ):
    def __init__( self, parent , makeCard):
        frame.MainFrame.__init__( self, parent )
        self.makeCard = makeCard
        self.parent = parent
    
    # Handlers for MainFrame events.
    def quitApp( self, event ):
        # TODO: Implement quitApp
        self.Destroy()
    def run( self, event ):
        # TODO: Implement runMakeCard
        data = {}
        inputFileList = [self.inputFilePicker1.GetPath(),
                         self.inputFilePicker2.GetPath(),
                         self.inputFilePicker3.GetPath()]
        inputFileList = [ file for file in inputFileList if file ]
        data["filenamelist"] = inputFileList 
        data["sheetname"] = self.sheetNameInput.GetValue()
        data["outputfile"] = self.outputFilePicker.GetPath()
        data["datelabel"] = self.datePicker.GetValue().Format(format="%Y/%m/%d(W%w)").replace("W0","W7")
        message = self.makeCard(**data)
        self.messageCtrl.SetValue(message)
        
        
