# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AdCardMaker_v0.2_by_朱彥儒", pos = wx.DefaultPosition, size = wx.Size( 320,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 350,350 ), wx.DefaultSize )
		
		MainFgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		MainFgSizer.SetFlexibleDirection( wx.BOTH )
		MainFgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.selectDateLabel = wx.StaticText( self, wx.ID_ANY, u"Select Date", wx.DefaultPosition, wx.Size( 80,12 ), wx.ALIGN_RIGHT )
		self.selectDateLabel.Wrap( -1 )
		MainFgSizer.Add( self.selectDateLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.datePicker = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		MainFgSizer.Add( self.datePicker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.InputFilesLabel = wx.StaticText( self, wx.ID_ANY, u"Input Files", wx.DefaultPosition, wx.Size( 80,12 ), wx.ALIGN_RIGHT )
		self.InputFilesLabel.Wrap( -1 )
		self.InputFilesLabel.SetMinSize( wx.Size( 80,12 ) )
		
		MainFgSizer.Add( self.InputFilesLabel, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( -1,120 ) ) 
		self.inputFilePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bSizer1.Add( self.inputFilePicker1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.inputFilePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bSizer1.Add( self.inputFilePicker2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.inputFilePicker3 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bSizer1.Add( self.inputFilePicker3, 1, wx.ALL, 5 )
		
		
		MainFgSizer.Add( bSizer1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sheetNameLabel = wx.StaticText( self, wx.ID_ANY, u"Sheet Name", wx.DefaultPosition, wx.Size( 80,12 ), wx.ALIGN_RIGHT )
		self.sheetNameLabel.Wrap( -1 )
		MainFgSizer.Add( self.sheetNameLabel, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sheetNameInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		MainFgSizer.Add( self.sheetNameInput, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.OutputFileLabel = wx.StaticText( self, wx.ID_ANY, u"Save as", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.OutputFileLabel.Wrap( -1 )
		MainFgSizer.Add( self.OutputFileLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.outputFilePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		MainFgSizer.Add( self.outputFilePicker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		MainFgSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ok_button = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.ok_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.close_button = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.close_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		MainFgSizer.Add( bSizer2, 1, 0, 5 )
		
		
		MainFgSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.messageCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.messageCtrl.SetFont( wx.Font( 14, 70, 90, 92, False, wx.EmptyString ) )
		self.messageCtrl.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.messageCtrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		MainFgSizer.Add( self.messageCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( MainFgSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.quitApp )
		self.ok_button.Bind( wx.EVT_BUTTON, self.run )
		self.close_button.Bind( wx.EVT_BUTTON, self.quitApp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def quitApp( self, event ):
		event.Skip()
	
	def run( self, event ):
		event.Skip()
	
	

