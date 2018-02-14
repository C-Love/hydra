# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import gui

###########################################################################
## Class MainFrame - ClientContact
###########################################################################

class Dialog_Client_Contact ( gui.MainFrame ):

	def __init__(self,parent):
		gui.MainFrame.__init__(slef,parent)
"""	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Client Contact", pos = wx.DefaultPosition, size = wx.Size( 830,707 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )

		fgSizer1 = wx.FlexGridSizer( 5, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 4 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.text_contact_type = wx.StaticText( self, wx.ID_ANY, u"Contact type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_contact_type.Wrap( -1 )
		fgSizer3.Add( self.text_contact_type, 0, wx.ALL, 5 )

		Combo_contact_typeChoices = [ u" ", u"Phone call", u"Voicemail", u"Email", u"Office visit", u"Letter" ]
		self.Combo_contact_type = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, Combo_contact_typeChoices, 0 )
		fgSizer3.Add( self.Combo_contact_type, 0, wx.ALL, 5 )

		self.text_re = wx.StaticText( self, wx.ID_ANY, u"Re:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_re.Wrap( -1 )
		fgSizer3.Add( self.text_re, 0, wx.ALL, 5 )

		self.contact_regarding = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.contact_regarding, 0, wx.ALL, 5 )

		self.text_phone_number = wx.StaticText( self, wx.ID_ANY, u"Phone number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_phone_number.Wrap( -1 )
		fgSizer3.Add( self.text_phone_number, 0, wx.ALL, 5 )

		self.phone_number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.phone_number, 0, wx.ALL, 5 )

		self.text_case_number = wx.StaticText( self, wx.ID_ANY, u"Case number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_case_number.Wrap( -1 )
		fgSizer3.Add( self.text_case_number, 0, wx.ALL, 5 )

		self.MAXIS_case_number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.MAXIS_case_number, 0, wx.ALL, 5 )

		self.text_mnsure_ic_number = wx.StaticText( self, wx.ID_ANY, u"MNSure IC number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_mnsure_ic_number.Wrap( -1 )
		fgSizer3.Add( self.text_mnsure_ic_number, 0, wx.ALL, 5 )

		self.METS_IC_number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.METS_IC_number, 0, wx.ALL, 5 )


		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		choice_contact_dirChoices = [ u"from", u"to" ]
		self.choice_contact_dir = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_contact_dirChoices, 0 )
		self.choice_contact_dir.SetSelection( 0 )
		fgSizer4.Add( self.choice_contact_dir, 0, wx.ALL, 5 )

		Combo_contact_personChoices = [ u" ", u"Client", u"AREP", u"Non-AREP", u"SWKR" ]
		self.Combo_contact_person = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, Combo_contact_personChoices, 0 )
		fgSizer4.Add( self.Combo_contact_person, 0, wx.ALL, 5 )


		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.text_date_of_contact = wx.StaticText( self, wx.ID_ANY, u"Date/Time of Contact:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_date_of_contact.Wrap( -1 )
		fgSizer4.Add( self.text_date_of_contact, 0, wx.ALL, 5 )

		self.date_of_contact = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.date_of_contact, 0, wx.ALL, 5 )

		self.used_interpreter_checkbox = wx.CheckBox( self, wx.ID_ANY, u"Used Interpreter", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.used_interpreter_checkbox, 0, wx.ALL, 5 )


		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )

		self.text_reason_for_contact = wx.StaticText( self, wx.ID_ANY, u"Reason for contact:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_reason_for_contact.Wrap( -1 )
		fgSizer1.Add( self.text_reason_for_contact, 0, wx.ALL, 5 )

		self.reason_for_contact = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.reason_for_contact, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass"""

app = wx.App(False)

frame = Dialog_Client_Contact()
frame.Show(True)

App.MainLoop()
