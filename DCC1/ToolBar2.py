# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os
import string

import wx
import wx.xrc
import wx.dataview as dv

import Database.MenuSet2 as MS
from GUI.MainTool import *
from AI.Generats import GenrDemo

from Config.Init import *
import Res.Allicons as icon

_ = wx.GetTranslation

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 558,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		self.Splt1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME|wx.SP_THIN_SASH )
		#self.Splt1.SetSashGravity( -1 )
		self.Splt1.Bind( wx.EVT_IDLE, self.Splt1OnIdle )

		self.P1 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.MyMenu = MS.GetData(u'Menu2.db', u'')
		self.DoMenu = MS.SetData(u'', u'', u'')
		self.Ttype = 'N'

		self.lbl0 = wx.StaticText( self.P1, wx.ID_ANY, _(u"List of toolbar:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl0.Wrap( -1 )

		Vsz2.Add( self.lbl0, 0, wx.ALL|wx.EXPAND, 5 )

		# self.DVC1 = wx.dataview.DataViewCtrl( self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.Col1 = self.DVC1.AppendTextColumn( u"Name ToolBar", 0, wx.DATAVIEW_CELL_INERT, 178, wx.ALIGN_LEFT, wx.DATAVIEW_COL_RESIZABLE )
		# self.Col2 = self.DVC1.AppendTextColumn( u"ID", 1, wx.DATAVIEW_CELL_INERT, 45, wx.ALIGN_LEFT, wx.DATAVIEW_COL_RESIZABLE )
		self.TTC1 = dv.TreeListCtrl(self.P1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)  # wx.TR_DEFAULT_STYLE
		self.TTC1.AppendColumn(_(u'Toolbar ID'), wx.COL_WIDTH_DEFAULT + 95, wx.ALIGN_LEFT, wx.COL_RESIZABLE)
		self.TTC1.AppendColumn(_(u'Toolbar Name'), wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE)

		Vsz2.Add( self.TTC1, 1, wx.ALL|wx.EXPAND, 5 )

		Hsz0 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn1 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_OTHER ) )
		self.btn1.SetBitmap(icon.add.GetBitmap())
		self.btn1.SetToolTip(_(u"Add"))
		Hsz0.Add( self.btn1, 0, wx.ALL, 5 )

		self.btn2 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_OTHER ) )
		self.btn2.SetBitmap(icon.edit_button.GetBitmap())
		self.btn2.SetToolTip(_(u"Edit"))
		Hsz0.Add( self.btn2, 0, wx.ALL, 5 )

		self.btn3 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn3.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_OTHER ) )
		self.btn3.SetBitmap(icon.delete.GetBitmap())
		self.btn3.SetToolTip(_(u"Delete"))
		Hsz0.Add( self.btn3, 0, wx.ALL, 5 )

		self.btn4 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn4.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_OTHER ) )
		self.btn4.SetBitmap(icon.separator.GetBitmap())
		self.btn4.SetToolTip(_(u"Seperator"))
		Hsz0.Add( self.btn4, 0, wx.ALL, 5 )

		self.btn5 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn5.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_OTHER ) )
		self.btn5.SetBitmap(icon.update.GetBitmap())
		self.btn5.SetToolTip(_(u"Update"))
		Hsz0.Add( self.btn5, 0, wx.ALL, 5 )

		self.btn6 = wx.BitmapButton( self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		#self.btn6.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REDO, wx.ART_OTHER ) )
		self.btn6.SetBitmap(icon.information.GetBitmap())
		self.btn6.SetToolTip(_(u"Info"))
		Hsz0.Add( self.btn6, 0, wx.ALL, 5 )

		self.btn7 = wx.BitmapButton(self.P1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
		                            wx.BU_AUTODRAW | 0)

		# self.btn7.SetBitmap(wx.Bitmap(ICON16_PATH + u'accept_button.png', wx.BITMAP_TYPE_ANY))
		self.btn7.SetBitmap(icon.accept_button.GetBitmap())
		self.btn7.SetToolTip(_(u"Apply"))
		Hsz0.Add(self.btn7, 0, wx.ALL, 5)


		Vsz2.Add( Hsz0, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.P1.SetSizer( Vsz2 )
		self.P1.Layout()
		Vsz2.Fit( self.P1 )
		self.P2 = wx.Panel( self.Splt1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		self.titr = wx.StaticText( self.P2, wx.ID_ANY, _(u"Group:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr.Wrap( -1 )

		Vsz3.Add( self.titr, 0, wx.ALL|wx.EXPAND, 5 )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.grup = wx.SpinCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 9, 1 )
		Hsz1.Add( self.grup, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl1 = wx.StaticText( self.P2, wx.ID_ANY, _(u"ID"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz1.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbl2 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Access"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Hsz1.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		Hsz1.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.codgnr = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.codgnr.SetToolTip(_(u'Code generator'))
		Hsz1.Add( self.codgnr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Name"), wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld3 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Icon"), wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl4.Wrap( -1 )

		Hsz3.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.IcnFile1 = wx.FilePickerCtrl( self.P2, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), u"*.png;*.bmp;*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz3.Add( self.IcnFile1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz3, 1, wx.EXPAND, 5 )

		self.btmp1 = wx.StaticBitmap( self.P2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz3.Add( self.btmp1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )



		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl6 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Short text"), wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl6.Wrap( -1 )

		Hsz5.Add( self.lbl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld4 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz5, 1, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl7 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Long text"), wx.DefaultPosition, wx.Size( 54,-1 ), 0 )
		self.lbl7.Wrap( -1 )

		Hsz6.Add( self.lbl7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld6 = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz6.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz6, 1, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl5 = wx.StaticText(self.P2, wx.ID_ANY, _(u"Type Toolbar"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl5.Wrap(-1)

		Hsz4.Add(self.lbl5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Rd1 = wx.RadioButton(self.P2, wx.ID_ANY, u"Normal", wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz4.Add(self.Rd1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Rd2 = wx.RadioButton(self.P2, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz4.Add(self.Rd2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Rd3 = wx.RadioButton(self.P2, wx.ID_ANY, u"Radio", wx.DefaultPosition, wx.DefaultSize, 0)
		Hsz4.Add(self.Rd3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsz3.Add(Hsz4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

		# Hsz7 = wx.BoxSizer( wx.HORIZONTAL )
		#
		# self.chk1 = wx.CheckBox( self.P2, wx.ID_ANY, _(u"Disable"), wx.DefaultPosition, wx.DefaultSize, 0 )
		# Hsz7.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		# self.chk2 = wx.CheckBox( self.P2, wx.ID_ANY, _(u"Hide"), wx.DefaultPosition, wx.DefaultSize, 0 )
		# Hsz7.Add( self.chk2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		#
		#
		# Vsz3.Add( Hsz7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lin1 = wx.StaticLine( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Vsz3.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )

		Hsz8 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl8 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Program:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )

		Hsz8.Add( self.lbl8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.probtn = wx.Button( self.P2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.probtn.SetToolTip( _(u"list of program can changed" ) )

		Hsz8.Add( self.probtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz8, 1, wx.EXPAND, 5 )

		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.prgfld = wx.TextCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz4.Add( self.prgfld, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl9 = wx.StaticText( self.P2, wx.ID_ANY, _(u"Directory:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl9.Wrap( -1 )

		Vsz4.Add( self.lbl9, 0, wx.ALL, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND, 5 )


		self.P2.SetSizer( Vsz3 )
		self.P2.Layout()
		Vsz3.Fit( self.P2 )
		self.Splt1.SplitVertically( self.P1, self.P2, 255 )
		Vsz1.Add( self.Splt1, 1, wx.EXPAND, 5 )

		self.fillitem()


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		#self.DVC1.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.slctmnu, id = wx.ID_ANY )
		self.TTC1.Bind(dv.EVT_DATAVIEW_SELECTION_CHANGED, self.actitm)
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.edtit )
		self.btn3.Bind( wx.EVT_BUTTON, self.delit )
		self.btn4.Bind( wx.EVT_BUTTON, self.adlin )
		self.btn5.Bind( wx.EVT_BUTTON, self.updat )
		self.btn6.Bind( wx.EVT_BUTTON, self.info )
		self.btn7.Bind(wx.EVT_BUTTON, self.aplit)
		self.grup.Bind(wx.EVT_SPINCTRL, self.chggrp)
		self.codgnr.Bind( wx.EVT_BUTTON, self.gnrcod )
		self.IcnFile1.Bind( wx.EVT_FILEPICKER_CHANGED, self.chgicn )
		self.Rd1.Bind( wx.EVT_RADIOBUTTON, self.slctyp )
		self.Rd2.Bind( wx.EVT_RADIOBUTTON, self.slctyp )
		self.Rd3.Bind( wx.EVT_RADIOBUTTON, self.slctyp )
		#self.chk1.Bind( wx.EVT_CHECKBOX, self.disbl )
		#self.chk2.Bind( wx.EVT_CHECKBOX, self.hidit )
		self.probtn.Bind( wx.EVT_BUTTON, self.prglst )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fillitem(self):
		isz = (16, 16)
		il = wx.ImageList(isz[0], isz[1])
		fldridx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
		fldropenidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))

		self.TTC1.SetImageList(il)
		self.il = il

		# broot = self.TTC1.AddRoot(u'Toolbar')
		root1 = self.TTC1.GetRootItem()
		broot = self.TTC1.AppendItem(root1, u'Tool Bar')

		self.altol = self.MyMenu.GetAllTB("left join handler on toolbar.handlerid = handler.handlerid \
	                                       left join access on toolbar.acclvlid = access.acclvlid \
										  where access.userid = 1 "
		                                  )
		dictool = self.regrouptoolbar(self.altol)

		for t in dictool:
			gritm = self.TTC1.AppendItem(broot, str(t))
			self.TTC1.SetItemText(gritm, 0, str(t))

			for i in dictool[t]:

				if i[1] == None or i[1] == '':
					#slcticn = il.Add(wx.Bitmap(ICON16_PATH + "separator.png", wx.BITMAP_TYPE_ANY))
					slcticn = il.Add(icon.separator.GetBitmap())
					ditm = self.TTC1.AppendItem(gritm, u'---')
					self.TTC1.SetItemText(ditm, 0, str(i[0]))
					self.TTC1.SetItemText(ditm, 1, u'---')

					self.TTC1.SetItemImage(ditm, fldridx, wx.TreeItemIcon_Normal)  # wx.NO_IMAGE
					self.TTC1.SetItemImage(ditm, slcticn, wx.TreeItemIcon_Selected)

				else:
					ibitmp = wx.Bitmap(ICONS_TOOL + i[2], wx.BITMAP_TYPE_ANY)

					#slcticn = il.Add(wx.Bitmap(ICONS_TOOL + i[2], wx.BITMAP_TYPE_ANY))
					slcticn = il.Add(self.Scalebitmap(ibitmp))
					bitm = self.TTC1.AppendItem(gritm, i[1])
					self.TTC1.SetItemText(bitm, 0, str(i[0]))
					self.TTC1.SetItemText(bitm, 1, i[1])

					self.TTC1.SetItemImage(bitm, fldridx, wx.TreeItemIcon_Normal)  # wx.NO_IMAGE
					self.TTC1.SetItemImage(bitm, slcticn, wx.TreeItemIcon_Selected)

	def Scalebitmap(self, mybitmap):
		myimage = mybitmap.ConvertToImage()
		return myimage.Scale(16,16).ConvertToBitmap()

	def regrouptoolbar(self, tooldata):
		result = {}

		for item in tooldata:
			if item[0] // 100 not in result:
				newitm = [(item[0], item[1], item[2], item[3], item[8])]
				result[item[0] // 100] = newitm
			else:
				result[item[0] // 100].append((item[0], item[1], item[2], item[3], item[8]))
		# print(result)
		return result

	def actitm(self, event):
		#self.slctitm = event.GetEventObject().GetItemText(event.GetItem())
		ps = self.TTC1.GetSelections()
		if len(ps) > 0:

			for itm in self.altol:
				if not self.TTC1.GetItemText(ps[0], 0).isdigit():
					pass
				elif int(self.TTC1.GetItemText(ps[0], 0)) == itm[0]:

					self.mydata = itm
					if itm[1] == None:
						data = [itm[0], u'-----', u'separator', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'',u'', u'FFFF', 1]
						self.setfield(data)
						self.IcnFile1.SetPath(u'')
						self.btmp1.SetBitmap(wx.NullBitmap)
						self.Allinactive(1)
					else:
						#print(self.mydata)
						self.Allinactive(0)
						self.setfield(self.mydata)
				elif int(self.TTC1.GetItemText(ps[0], 0)) < 9:
					#data = [int(self.TTC1.GetItemText(ps[0], 0))*100,u'',u'image.png', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'',u'', u'FFFF', 1]
					#self.setfield(data)
					self.Allinactive(0)
					self.grup.SetValue(int(self.TTC1.GetItemText(ps[0], 0)))
					self.fld1.SetValue('')
					self.fld2.SetValue('')
					self.fld3.SetValue('')
					self.IcnFile1.SetPath('')
					self.btmp1.SetBitmap(wx.NullBitmap)
					self.fld4.SetValue('')
					self.fld6.SetValue('')
		pass

	def setfield(self, Data):
		self.grup.SetValue(Data[0]//100)
		self.fld1.SetValue(str(Data[0]))
		self.fld2.SetValue(Data[6])
		self.fld3.SetValue(Data[1])
		self.IcnFile1.SetPath(ICONS_TOOL+Data[2])
		if Data[2] == u'separator' or Data[2] == None:
			self.btmp1.SetBitmap(icon.separator.GetBitmap())
		elif Data[2] == u'image.png':
			self.btmp1.SetBitmap(icon.image.GetBitmap())
		else:
			self.btmp1.SetBitmap(wx.Bitmap(self.IcnFile1.GetPath(), wx.BITMAP_TYPE_ANY))
		#self.btmp1.SetBitmap(wx.Bitmap(self.IcnFile1.GetPath(), wx.BITMAP_TYPE_ANY))
		self.fld4.SetValue(Data[3])
		self.fld6.SetValue(Data[4])

		if Data[7] == 'N':
			self.Rd1.SetValue(1)
		elif Data[7] == 'C':
			self.Rd2.SetValue(1)
		elif Data[7] == 'R':
			self.Rd3.SetValue(1)
		#else:
			#print(Data[7])
		# Radio Button Here
		# if Data[16] != 'FFFF':
		# 	self.chk2.SetValue(1)
		# if Data[17] != 1:
		# 	self.chk1.SetValue(1)

		self.prgfld.SetValue(Data[9]+'.py')
		self.lbl9.SetLabel(_("Directory :")+Src_prg)

	def getfield(self):
		D0 = self.grup.GetValue()
		D1 = self.fld1.GetValue()
		D2 = self.fld2.GetValue()
		D3 = self.fld3.GetValue()
		D4 = self.IcnFile1.GetPath()
		#DR = 1 Radio Select
		D5 = self.fld4.GetValue()
		D6 = self.fld6.GetValue()
		D7 = 0 #self.chk1.GetValue()
		D8 = 0 #self.chk2.GetValue()
		D9 = self.prgfld.GetValue()
		return D0,D1,D2,D3,D4,D5,D6,D7,D8,D9

	def Allinactive(self,do):
		if do:
			self.grup.Disable()
			self.fld1.Disable()
			self.fld2.Disable()
			self.fld3.Disable()
			self.IcnFile1.Disable()
			self.fld4.Disable()
			self.fld6.Disable()
			self.Rd1.Disable()
			self.Rd2.Disable()
			self.Rd3.Disable()
			#self.chk1.Disable()
			#self.chk2.Disable()
			self.prgfld.Disable()
		else:
			self.grup.Enable()
			self.fld1.Enable()
			self.fld2.Enable()
			self.fld3.Enable()
			self.IcnFile1.Enable()
			self.fld4.Enable()
			self.fld6.Enable()
			self.Rd1.Enable()
			self.Rd2.Enable()
			self.Rd3.Enable()
			#self.chk1.Enable()
			#self.chk2.Enable()
			self.prgfld.Enable()

	def rclkitm(self, event):
		event.Skip()

	def slctmnu( self, event ):
		event.Skip()

	def addit( self, event ):
		grp = self.grup.GetValue()
		# print(grp)
		data = [grp * 100, u'', u'image.png', u'', u'', u'', u'', u'N', u'', u'', u'', u'', u'', u'', u'', u'', u'FFFF', 1]

		self.setfield(data)
		self.fld1.SetValue(u'')
		event.Skip()

	def edtit( self, event ):
		thsdata = self.getfield()

		if int(thsdata[1]) // 100 != int(thsdata[0]):
			wx.MessageBox(
				_('Please press Add button and then press [...] generator cod button. Group and cod NOT match'))
			return 1
		else:
			icn = thsdata[4].split("\\")[-1]
			hnd = thsdata[9].replace('.py', '')
			# if hnd == '':
			#	hndlrid = 99000
			# else:
			hndlrid = self.findhandler(hnd)
			#	hndlrid = 10001

			if thsdata[7]:
				disen = 0
			else:
				disen = 1
			if thsdata[8]:
				shwid = '0000'
			else:
				shwid = 'FFFF'
			Data1 = [thsdata[3], icn, thsdata[5], thsdata[6], hndlrid, thsdata[2], self.Ttype]
			self.DoMenu.Table = u"toolbar"
			self.DoMenu.Upditem(u'toolname = ? , toolicon = ? , shrttxt = ? , lngtxt = ? , \
					                handlerid = ? , acclvlid = ?, tooltype = ? where  toolid = %d ' % int(thsdata[1]), Data1)

			Data2 = [1, shwid, disen]
			self.DoMenu.Table = u'access'
			self.DoMenu.Upditem(u'userid = ? , acclvl = ?, disenable = ? where acclvlid = "%s" ' % thsdata[1], Data2)

			wx.MessageBox(_(u"successful change Toolbar in program"))

			self.EdtTool(thsdata, icn)

			self.TTC1.DeleteAllItems()
			self.fillitem()
			self.Refresh()
		event.Skip()

	def delit( self, event ):
		thsdata = self.getfield()
		# print(thsdata)

		self.DoMenu.Table = u"toolbar"
		self.DoMenu.Delitem(u"toolbar.toolid = %d " % int(thsdata[1]))
		self.DoMenu.Table = u"access"
		self.DoMenu.Delitem(u'access.acclvlid = "%s" ' % thsdata[2])
		self.DelTool(thsdata)
		wx.MessageBox(_(u"successful delete Toolbar at program"))

		self.TTC1.DeleteAllItems()
		self.fillitem()
		self.Refresh()
		event.Skip()


	def adlin( self, event ):
		d = self.grup.GetValue()

		lstcod = self.MyMenu.GetAllTB(" Where toolbar.toolid/100 = %d" % d)
		if len(lstcod) <= 1:
			wx.MessageBox(_(u"Please First Add 1 item then use line separator"))
		else:
			icod = lstcod[-1][0] + 1
			iData1 = [icod]
			self.DoMenu.Table = u"toolbar"
			self.DoMenu.Additem(u'toolid ', iData1)
			self.config = wx.GetApp().GetConfig()
			TBP = self.config.Read('Toolbar')
			mw = self.FindWindowByName('main')
			if TBP == '1':
				tb = mw.GetToolBar()
				#tb.AddSeparator()
				tb.InsertSeparator(self.GetToolPos(tb,icod))
				tb.Realize()
			elif TBP == '2':
				tb = mw.tool[d - 1]
				tb.AddSeparator()
				tb.Realize()
			else:
				print('we have error in option')

		self.TTC1.DeleteAllItems()
		self.fillitem()
		self.Refresh()
		event.Skip()

	def updat( self, event ):
		self.TTC1.DeleteAllItems()
		self.fillitem()
		self.Refresh()

		mw = self.FindWindowByName('main')

		mw.Refresh()
		mw.Layout()
		event.Skip()

	def info( self, event ):
		print(self.mydata)
		event.Skip()

	def aplit(self, event ):
		ThsData = self.getfield()
		#print(ThsData)
		if ThsData[4].split('\\')[-1] == 'image.png' or ThsData[4] == '':
			wx.MessageBox(_("You must choose an image for tool, Please select a correct image."))
			return 1
		if ThsData[3] == '' or ThsData[2] == '' or ThsData[1] == '':
			wx.MessageBox(_("Please fill the name ,id  and access field, this fields must could not be empty."))
			return 1
		GrpTl = self.MyMenu.GetAllTB(" Where toolid/100 = %d "% int(ThsData[0]) )
		if GrpTl == []:
			GrpTl = [(self.grup.GetValue()*100,'')]
			#print(GrpTl[-1][0])
		if GrpTl[-1][0] != int(ThsData[1]):

			if int(ThsData[1])//100 != int(ThsData[0]):
				wx.MessageBox(_('Please press Add button and then press [...] generator cod button. Group and cod NOT match'))
				return 1
			else:
				icn = ThsData[4].split('\\')[-1]
				#print(icn)
				#self.chkicnpath(ThsData[4])
				hnd = ThsData[9].replace('.py', '')
				hndlrid = self.findhandler(hnd)
				if hndlrid == -1:
					self.prgdir = self.DemoGenerate()
					print(ThsData,(int(ThsData[1])//10)*100)
					hndlrid = 10000+(int(ThsData[1])//10)*100
					iData3 = [hndlrid,'Demo',self.prgdir,'-1',-1,(int(ThsData[1])//10)*100]
					self.DoMenu.Table = u"handler"
					self.DoMenu.Additem(u"handlerid, prgname, prgdir, paramtr, public, prgno",iData3)

				iData1 = [ThsData[1],ThsData[3],icn,ThsData[5],ThsData[6],hndlrid,ThsData[2],self.Ttype]
				self.DoMenu.Table = u"toolbar"
				self.DoMenu.Additem(u'toolid, toolname, toolicon, shrttxt, lngtxt, handlerid, acclvlid, tooltype', iData1)
				if ThsData[7]:
					disen = 0
				else:
					disen = 1
				if ThsData[8]:
					shwid = '0000'
				else:
					shwid = 'FFFF'
				iData2 = [ThsData[2],1,shwid,disen]
				self.DoMenu.Table = u"access"
				self.DoMenu.Additem(u'acclvlid, userid, acclvl, disenable', iData2)

				#print(ThsData[9].replace('.py', ''))
				self.AddTool(ThsData,iData1)
				wx.MessageBox(_(u"successful add Toolbar to program"))

				self.TTC1.DeleteAllItems()
				self.fillitem()
				self.Refresh()

				#iData3 = []
				#self.DoMenu.Table = u"handler"
				#self.DoMenu.Additem(u"handlerid, prgname, prgdir, paramtr, public, prgno",iData3)
		event.Skip()

	def chggrp(self, event):
		grp = self.grup.GetValue()
		if self.fld1.GetValue() != '':
			if int(self.fld1.GetValue())/100 != grp:
				wx.MessageBox(_('Please press Add button and then press [...] generator cod button. Group and cod NOT match'))
				self.grup.SetValue(int(self.fld1.GetValue())/100)

	def gnrcod( self, event ):
		d = self.grup.GetValue()
		lstcod = self.MyMenu.GetAllTB(" Where toolbar.toolid/100 = %d " % d)
		if lstcod == []:
			tbid = (d * 100) + 1
			cd = 'tb'
			accid = str(tbid)[0] + str(tbid)[-1] + cd
		else:
			tbid = lstcod[-1][0] + 1
			cd = lstcod[0][1][0].lower() + lstcod[0][1][-1].lower()
			accid = str(tbid)[0] + str(tbid)[-1] + cd

		if self.fld1.GetValue() == '':
			self.fld1.SetValue(str(tbid))

		if self.fld2.GetValue() == '':
			self.fld2.SetValue(accid)
		event.Skip()

	def chgicn( self, event ):
		if ICONS_TOOL[1:] not in self.IcnFile1.GetPath():
			#print(self.IcnFile1.GetPath(),ICONS_TOOL)
			CopyIcon(self.IcnFile1.GetPath(),'Toolbar')
		self.btmp1.SetBitmap(wx.Bitmap(self.IcnFile1.GetPath(), wx.BITMAP_TYPE_ANY))
		event.Skip()

	def slctyp( self, event ):
		if self.Rd1.GetValue():
			self.Ttype = 'N'
		elif self.Rd2.GetValue():
			self.Ttype = 'C'
		elif self.Rd3.GetValue():
			self.Ttype = 'R'
		else:
			self.Ttype = 'S'

		event.Skip()

	# def disbl( self, event ):
	# 	event.Skip()
	#
	# def hidit( self, event ):
	# 	event.Skip()

	def findhandler(self, hndlrnm):
		if hndlrnm == '':
			if len(self.MyMenu.getHndlr("Demo")) > 0:
				codid, self.prgdir = self.MyMenu.getHndlr("Demo")[0]
			else:
				codid = -1
			return codid
		else:
			codid , self.prgdir = self.MyMenu.getHndlr(hndlrnm)[0]
			return codid

	def finddir(self, data):
		# print(data)
		aldir = self.MyMenu.AllGuiDir()
		for dr in aldir:
			if data in dr:
				# print(dr)
				return dr[1]
		return ''

	def DemoGenerate(self):
		if self.finddir(Src_prg) != '':
			dircod = self.finddir(Src_prg)
			return dircod
		else:
			#dircod = '1' + self.fld1.GetValue()  # +'1'
			dircod = '1' + '0' + str(self.grup.GetValue()) + '1'
			self.iSrc_prg = self.MyMenu.GetImpCod('1000')[0][0]
			self.iSrc_dir = self.MyMenu.GetDirCod('1000')[0][0]
			mydir = Src_prg+'TB'

			self.DoMenu.Table = u'Guidir'
			self.DoMenu.Additem(u' Dir, prgdir, hdddir', ( mydir.replace(Src_prg,self.iSrc_prg) , dircod, self.iSrc_dir+'TB'))
			if not os.path.isdir(mydir):
				os.mkdir(mydir)
			os.chdir(mydir)
			# print(mydir)
			if not os.path.isfile(mydir + SLASH + u'__init__.py'):
				with open(u'__init__.py', u'w+') as f:
					f.write('')
			# print(mydir)
			GenrDemo(mydir)
			if not os.path.isfile(Src_gui + u"SamPnl.py"):
				shutil.copy(GUI_PATH + 'API' + SLASH + 'SamPnl.py', Src_gui)
			return dircod

	def prglst( self, event ):
		if wx.FindWindowByName(u'Program Develop') == None:
			#print(self.mydata)
			if self.prgfld.GetValue() != '' and self.prgfld.GetValue() != '.py':
				import DCC1.ProgDev2 as DP
				ifrm = wx.Frame(self, -1, style=wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)
				pnl = DP.MyPanel1(ifrm,[self.GetParent(),self.prgfld.GetValue().replace('.py',''),self.mydata[5]])
				ifrm.SetSize((555, 500))
				ifrm.SetTitle(u'Program Develop')
				ifrm.Show()
				#print( ifrm.TransferDataFromWindow() )

		else:
			wx.MessageBox(_("Double Program: Please Close Program Develop then Do this item"))
		event.Skip()

	def Splt1OnIdle( self, event ):
		self.Splt1.SetSashPosition( 255 )
		self.Splt1.Unbind( wx.EVT_IDLE )

	def AddTool(self, D, iD):
			self.config = wx.GetApp().GetConfig()
			TBP = self.config.Read('Toolbar')
			if TBP == '1':
				mw = self.FindWindowByName('main')
				tb = mw.GetToolBar()
				ppos = self.GetToolPos(tb,int(D[1])-1)
				#ppos = tb.GetToolPos(int(D[1]) - 1)
				#print(ppos,tb.GetToolPos(int(D[1]) - 1))
				TTT = self.GetToolType()
				if ppos != -1:
					tb.InsertTool(ppos + 1, int(D[1]), str(D[3]), wx.Bitmap(ICONS_TOOL + iD[2]), wx.NullBitmap,
					              TTT, str(D[5]),
					              str(D[6]))
				else:
					tb.AddTool(int(D[1]), str(D[3]), wx.Bitmap(ICONS_TOOL + iD[2]), wx.NullBitmap, TTT,
					           str(D[5]), str(D[6]))
				tb.Realize()
			elif TBP == '2':
				mw = self.FindWindowByName('main')
				# print(D, iD, len(mw.tool))
				if len(mw.tool) < D[0]:
					MTB = MyAuiToolbar(mw)
					MyTL = [iD]
					mw.tool.append(MTB.CreatTool(MyTL))

					mw.tool[-1].SetToolBitmapSize(wx.Size(24, 24))
					mw.tool[-1].Realize()
					mw.m_mgr.AddPane(mw.tool[-1], wx.aui.AuiPaneInfo().Name("tb" + str(D[0])).Caption("Toolbar").
					                 ToolbarPane().Top().LeftDockable(True).RightDockable(False))
				# MyAuiToolbar.CreatTool(tbData)
				else:
					tb = mw.tool[D[0] - 1]
					# print(tb)
					# ppos  = tb.FindTool(int(D[1])-1)
					# print(ppos)
					TTT = self.GetToolType()
					tb.AddTool(int(D[1]), str(D[3]), wx.Bitmap(ICONS_TOOL + iD[2]), wx.NullBitmap, TTT,
					           str(D[5]), str(D[6]), None)
					tb.Realize()

			else:
				print('some wrong')

	def EdtTool(self, D, icn):
			self.config = wx.GetApp().GetConfig()
			TBP = self.config.Read('Toolbar')
			mw = self.FindWindowByName('main')
			if TBP == '1':
				tb = mw.GetToolBar()
				# ppos = tb.GetToolPos(int(D[1]) - 1)
				ttb = tb.FindById(int(D[1]))
				ttb.SetLabel(D[3])
				tb.SetToolNormalBitmap(int(D[1]), wx.Bitmap(ICONS_TOOL + icn))
				tb.SetToolShortHelp(int(D[1]), str(D[5]))
				tb.SetToolLongHelp(int(D[1]), str(D[6]))

			elif TBP == '2':
				if len(mw.tool) == 0:
					wx.MessageBox(_(u'Please select toolbar or create it'))
				else:
					tb = mw.tool[D[0] - 1]
					tb.SetToolLabel(int(D[1]), D[3])
					tb.SetToolBitmap(int(D[1]), wx.Bitmap(ICONS_TOOL + icn))
					tb.SetToolShortHelp(int(D[1]), str(D[5]))
					tb.SetToolLongHelp(int(D[1]), str(D[6]))

	def DelTool(self, D):
			self.config = wx.GetApp().GetConfig()
			TBP = self.config.Read('Toolbar')
			# print(TBP)
			mw = self.FindWindowByName('main')
			if TBP == '1':
				# print(mw)
				tb = mw.GetToolBar()
				thstool = tb.FindById(int(D[1]))
				#print(thstool)
				#tb.DeleteTool(int(D[1]))
				if thstool != None:
					thstool.GetToolBar().DeleteTool(int(D[1]))
				else:
					tb.RemoveTool(int(D[1]))

			else:
				tb = mw.tool[D[0] - 1]
				# print(tb)
				itb = tb.FindTool(int(D[1]))
				tb.DeleteTool(int(D[1]))
			tb.Realize()

	def GetToolType(self):
		if self.Ttype == 'N':
			return wx.ITEM_NORMAL
		elif self.Ttype == 'C':
			return wx.ITEM_CHECK
		elif self.Ttype == 'R':
			return wx.ITEM_RADIO
		else:
			return wx.ITEM_SEPARATOR

	def GetToolPos(self,tb,id):
		lstid = 101
		for i in range(tb.GetToolsCount()):
			tpos = tb.GetToolByPos(i)
			if tpos.IsButton():
				lstid = tpos.GetId()
				if lstid == id:
					return i
			if tpos.IsSeparator():
				if lstid//100 == id//100:
					return i
		return -1

