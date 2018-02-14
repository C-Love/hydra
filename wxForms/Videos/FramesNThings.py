# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.wizard

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu15 = wx.Menu()
		self.m_menuItem38 = wx.MenuItem( self.m_menu15, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu15.AppendItem( self.m_menuItem38 )
		
		self.m_menuItem39 = wx.MenuItem( self.m_menu15, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu15.AppendItem( self.m_menuItem39 )
		
		self.m_menuItem40 = wx.MenuItem( self.m_menu15, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu15.AppendItem( self.m_menuItem40 )
		
		self.m_menubar2.Append( self.m_menu15, u"MyMenu" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		fgSizer3.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyWizard1
###########################################################################

class MyWizard1 ( wx.wizard.Wizard ):
	
	def __init__( self, parent ):
		wx.wizard.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_pages = []
		
		self.m_wizPage11 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage11 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_wizPage11, wx.ID_ANY, u"I will show you how \n to do this thing very well. \nLet me help you.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_wizPage11.SetSizer( bSizer3 )
		self.m_wizPage11.Layout()
		bSizer3.Fit( self.m_wizPage11 )
		self.m_wizPage15 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage15 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_wizPage15, wx.ID_ANY, u"Stop! \n\nWho would cross the \nbridge of death must answer me \nthese questions 3. \nEre the other side he see.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer7.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button4 = wx.Button( self.m_wizPage15, wx.ID_ANY, u"Ask me the questions Bridgekeeper.", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_wizPage15.SetSizer( bSizer7 )
		self.m_wizPage15.Layout()
		bSizer7.Fit( self.m_wizPage15 )
		self.m_wizPage12 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage12 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self.m_wizPage12, wx.ID_ANY, u"First, what is your name?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_wizPage12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_wizPage12.SetSizer( bSizer4 )
		self.m_wizPage12.Layout()
		bSizer4.Fit( self.m_wizPage12 )
		self.m_wizPage13 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage13 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self.m_wizPage13, wx.ID_ANY, u"What is your quest?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer5.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.m_wizPage13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_wizPage13.SetSizer( bSizer5 )
		self.m_wizPage13.Layout()
		bSizer5.Fit( self.m_wizPage13 )
		self.m_wizPage14 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage14 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_wizPage14, wx.ID_ANY, u"What is the airspeed\n velocity of an \nunladen swallow?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer6.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_radioBtn1 = wx.RadioButton( self.m_wizPage14, wx.ID_ANY, u"African Swallow", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_radioBtn2 = wx.RadioButton( self.m_wizPage14, wx.ID_ANY, u"European Swallow", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		
		self.m_wizPage14.SetSizer( bSizer6 )
		self.m_wizPage14.Layout()
		bSizer6.Fit( self.m_wizPage14 )
		self.m_wizPage16 = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.m_wizPage16 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( self.m_wizPage16, wx.ID_ANY, u"What! I don't know that.", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_wizPage16.SetSizer( bSizer8 )
		self.m_wizPage16.Layout()
		bSizer8.Fit( self.m_wizPage16 )
		self.Centre( wx.BOTH )
		
	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyMenuBar3
###########################################################################

class MyMenuBar3 ( wx.MenuBar ):
	
	def __init__( self ):
		wx.MenuBar.__init__ ( self, style = 0 )
		
		self.m_menu10 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu10.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu10.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu10.AppendItem( self.m_menuItem3 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu10.AppendItem( self.m_menuItem4 )
		
		self.m_menu9 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu9.AppendItem( self.m_menuItem5 )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu9.AppendItem( self.m_menuItem6 )
		
		self.m_menuItem7 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu9.AppendItem( self.m_menuItem7 )
		
		self.m_menuItem8 = wx.MenuItem( self.m_menu9, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu9.AppendItem( self.m_menuItem8 )
		
		self.m_menu10.AppendSubMenu( self.m_menu9, u"MyMenu" )
		
		self.Append( self.m_menu10, u"MyMenu" ) 
		
		self.m_menu11 = wx.Menu()
		self.m_menuItem9 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem9 )
		
		self.m_menuItem10 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem10 )
		
		self.m_menuItem11 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem11 )
		
		self.m_menu11.AppendSeparator()
		
		self.m_menuItem12 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem12 )
		
		self.m_menuItem13 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem13 )
		
		self.m_menu11.AppendSeparator()
		
		self.m_menu121 = wx.Menu()
		self.m_menuItem16 = wx.MenuItem( self.m_menu121, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu121.AppendItem( self.m_menuItem16 )
		
		self.m_menuItem17 = wx.MenuItem( self.m_menu121, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu121.AppendItem( self.m_menuItem17 )
		
		self.m_menuItem18 = wx.MenuItem( self.m_menu121, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu121.AppendItem( self.m_menuItem18 )
		
		self.m_menu11.AppendSubMenu( self.m_menu121, u"MyMenu" )
		
		self.m_menu111 = wx.Menu()
		self.m_menuItem14 = wx.MenuItem( self.m_menu111, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu111.AppendItem( self.m_menuItem14 )
		
		self.m_menuItem15 = wx.MenuItem( self.m_menu111, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu111.AppendItem( self.m_menuItem15 )
		
		self.m_menu11.AppendSubMenu( self.m_menu111, u"MyMenu" )
		
		self.Append( self.m_menu11, u"MyMenu" ) 
		
		self.m_menu12 = wx.Menu()
		self.m_menuItem19 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu12.AppendItem( self.m_menuItem19 )
		
		self.m_menuItem20 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu12.AppendItem( self.m_menuItem20 )
		
		self.m_menuItem21 = wx.MenuItem( self.m_menu12, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu12.AppendItem( self.m_menuItem21 )
		
		self.Append( self.m_menu12, u"MyMenu" ) 
		
		self.m_menu13 = wx.Menu()
		self.m_menu131 = wx.Menu()
		self.m_menuItem27 = wx.MenuItem( self.m_menu131, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu131.AppendItem( self.m_menuItem27 )
		
		self.m_menuItem28 = wx.MenuItem( self.m_menu131, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu131.AppendItem( self.m_menuItem28 )
		
		self.m_menuItem29 = wx.MenuItem( self.m_menu131, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu131.AppendItem( self.m_menuItem29 )
		
		self.m_menuItem30 = wx.MenuItem( self.m_menu131, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu131.AppendItem( self.m_menuItem30 )
		
		self.m_menu13.AppendSubMenu( self.m_menu131, u"MyMenu" )
		
		self.m_menu141 = wx.Menu()
		self.m_menuItem24 = wx.MenuItem( self.m_menu141, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu141.AppendItem( self.m_menuItem24 )
		
		self.m_menuItem25 = wx.MenuItem( self.m_menu141, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu141.AppendItem( self.m_menuItem25 )
		
		self.m_menuItem26 = wx.MenuItem( self.m_menu141, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu141.AppendItem( self.m_menuItem26 )
		
		self.m_menu13.AppendSubMenu( self.m_menu141, u"MyMenu" )
		
		self.m_menu16 = wx.Menu()
		self.m_menuItem22 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.AppendItem( self.m_menuItem22 )
		
		self.m_menuItem23 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.AppendItem( self.m_menuItem23 )
		
		self.m_menu13.AppendSubMenu( self.m_menu16, u"MyMenu" )
		
		self.Append( self.m_menu13, u"MyMenu" ) 
		
		self.m_menu14 = wx.Menu()
		self.m_menuItem31 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem31 )
		
		self.m_menuItem32 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem32 )
		
		self.m_menuItem33 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem33 )
		
		self.m_menuItem34 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem34 )
		
		self.m_menuItem35 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem35 )
		
		self.m_menuItem36 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem36 )
		
		self.m_menuItem37 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.AppendItem( self.m_menuItem37 )
		
		self.Append( self.m_menu14, u"MyMenu" ) 
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyToolBar1
###########################################################################

class MyToolBar1 ( wx.ToolBar ):
	
	def __init__( self, parent ):
		wx.ToolBar.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TB_HORIZONTAL )
		
		self.m_infoCtrl2 = wx.InfoBar( self )
		self.m_infoCtrl2.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.m_infoCtrl2.SetEffectDuration( 500 )
		self.AddControl( self.m_infoCtrl2 ) 
		self.m_tool11 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool12 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool13 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.MyToolBar1.AddSeparator()
		
		self.MyToolBar1.AddSeparator()
		
		self.MyToolBar1.AddSeparator()
		
		self.m_tool14 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool15 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool16 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool17 = self.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		
		self.Realize()
	
	def __del__( self ):
		pass
	

