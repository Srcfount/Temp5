# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import sys
# import glob
# import time
#
# import importlib
# import importlib.util
#
# import wx
# import wx.adv
# import wx.aui
# import wx.dataview
import wx

from Allimp import *
import platform

import GUI.MainMenu2 as MM
import GUI.MainTool as MT
import GUI.AuiPanel.PAui as PA
import GUI.BG2 as BG
import GUI.proman as pro

from Config.Init import *

_ = wx.GetTranslation

class MainWin(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title=u'',size=(-1,-1),name=u'main')

        # Get Program Config ===================

        self.config = wx.GetApp().GetConfig()

        wx.SystemOptions.SetOption("msw.remap", 2)

        label = self.config.Read(u'Winname')
        self.SetLabel(label)
        #self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.newmenu = True

        if platform.system() == 'Windows':
            fntis = self.config.Read(u'Font').split(',')
            ifont = wx.Font(int(fntis[0]), int(fntis[1]), int(fntis[2]), int(fntis[3]), eval(fntis[4]), faceName=fntis[5])
            self.SetFont(ifont)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        # If like Back Gorund or Aui Center =============================
        if eval(self.config.Read('BGActive')):
            #self.BGrnd(self.config.Read('Background'))
            self.BGrnd(self.config.Read('BGActive.WinBG'))
        # If like use login =============================================
        if os.path.isfile(Src_aui+"login_pane.py"):
            import Src.AUI.login_pane as Lg
            dlg = wx.Dialog(self, -1, style=0)
            pnl = Lg.MyPanel1(dlg)
            dlg.SetSize((300,150))
            disply = wx.GetDisplaySize()
            dlg.SetPosition((disply[0] / 2 - 150, disply[1] / 2 - 75))
            dlg.ShowModal()
            if pnl.user == -1:
                exit()
            else:
                userid = pnl.user
            dlg.Destroy()
        else:
            userid = 1


        # Menu of Program Toolbar and Status ==========================
        if self.config.Read("Menu") == '1':
            self.menu = MM.AppMenu(userid)
            #self.menu.m.userid = userid
            if len(self.menu.GetMenus()) != 0:
                #self.SetMenuBar(menu)
                self.UpdateMenu(self.menu, self.menu.GetMenus())

            if self.config.Read('Toolbar') == '1':
                #self.Toolbar()
                self.ToolBar2()
                TBBG = self.config.Read("TBGColor").split(',')[1]
                self.tb.SetBackgroundColour(wx.SystemSettings.GetColour(int(TBBG)))
            elif self.config.Read('Toolbar') == '2':
                self.ToolPnl()

            self.MakeStatus()


        STBG = self.config.Read("SBGColor").split(',')[1]
        self.GetStatusBar().SetBackgroundColour(wx.SystemSettings.GetColour(int(STBG)))

        # All Panel Aui=======================
        self.APnls2()

        #self.BGrnd(BakGrnd)
        if userid == 1:
            self.Bind(wx.EVT_RIGHT_DOWN, self.domouse)
            self.Bind(wx.EVT_CONTEXT_MENU, self.setmenu)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #self.Bind(wx.EVT_UPDATE_UI,self.Refreshwin)

        self.m_mgr.Update()
        self.Centre(wx.BOTH)

    def __del__(self):
        if platform.system() == 'windows':
            self.m_mgr.UnInit()


    def OnClose(self, event):
        if 'timer' in dir(self):
            if self.timer.IsRunning():
                self.timer.Stop()
                del self.timer
        self.Destroy()

    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        self.SetStatusText(st, self.stnbr)

    def MakeStatus(self):
        lststat = eval(self.config.Read('Status'))
        i = 1
        Wthlst = [-1]

        statusBar = self.CreateStatusBar(len(lststat) + 1,
                                         wx.STB_ELLIPSIZE_END | wx.STB_ELLIPSIZE_MIDDLE | wx.STB_SHOW_TIPS | wx.STB_SIZEGRIP,
                                         wx.ID_ANY)

        # statusBar.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))
        for st in lststat:
            if st == 'time':
                # Timer in status ============================================
                self.timer = wx.PyTimer(self.Notify)
                self.timer.Start(1000)
                Wthlst.append(90)
            elif st == 'date':
                t = time.localtime(time.time())
                self.SetStatusText(time.strftime("%d-%b-%Y", t), i)
                Wthlst.append(90)
            elif st == 'path':
                ipath = os.getcwd() #  self.config.Read('AppPath')
                #print(ipath)
                self.SetStatusText(ipath,i)
                Wthlst.append(-1)
            #else:
            #    self.SetStatusText(st, i)
            #    Wthlst.append(-1)
            i += 1
        self.SetStatusBar(statusBar)

        self.stnbr = len(Wthlst) - 1
        self.SetStatusWidths(Wthlst)
        self.SetStatusBarPane(0)
        if 'time' in lststat:
            self.Notify()


    def domouse(self, event):
        self.setmenu(event)

    def setmenu(self, event):
        self.MnuDic = {1: [_(u'Menu Change'), 9999], 2: [_(u'Toolbar Change'), 9998], 3: [_(u'Panes Change'), 9997], 4: [u'', 0],
                       5: [_(u'Databases...'), 9996], 6: [_(u'Programs...'), 9995], 7: [_(u'Add Tools...'), 9994], 8: [u'', 0],
                       9: [_(u'MLA Design...'), 9993], 10: [u'', 0], 11: [_(u'Settings...'), 9992]}
        self.m1 = wx.Menu()

        self.itms = []
        i = 0
        for itm in self.MnuDic:
            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=itm)
            if self.MnuDic[itm][0] == u'':
                self.m1.AppendSeparator()
            else:
                # self.itms.append( wx.MenuItem(self.m1, wx.ID_ANY, MnuDic[itm][0], wx.EmptyString) )
                self.m1.Append(itm, self.MnuDic[itm][0])
                #self.Bind(wx.EVT_MENU, self.OnPopupOne, id=MnuDic[itm][1])
                i = i + 1

        self.PopupMenu(self.m1)
        self.m1.Destroy()

    def OnPopupOne(self, event):
        pmid = event.GetId()
        a = pro.DoProgram2(self.MnuDic[pmid][1], '')
        win1 = wx.Frame(self, -1)
        a.main(win1)

    def OnMenu(self, event):
        self.mid = event.GetId()
        a = pro.DoProgram2(self.mid, '')
        win1 = wx.Frame(self, -1)
        a.main(win1)

    def OnTool(self, event):
        self.tid = event.GetId()
        a = pro.DoProgram2(self.tid, '')
        win1 = wx.Frame(self, -1)
        a.main(win1)

    def ToolBar2(self):
        #self.tb = self.CreateToolBar(wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT)
        self.tb = MT.MyToolbar(self,wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT|wx.TB_TEXT)
        self.tb.data = MT.ToolData()
        #print(self.tb.data.ToolBarList())
        tsize = (24, 24)  # <<<=====use Config
        self.tb.SetToolBitmapSize(tsize)
        tbdata = self.tb.data.ToolBarList()
        #print(tbdata)
        self.tb.CreatTool(tbdata)
        self.SetToolBar(self.tb)
        if len(tbdata) > 0:
            self.Bind(wx.EVT_TOOL_RANGE, self.OnTool, id=tbdata[1][0][0], id2=tbdata[len(tbdata)][-1][0])


    def ToolPnl(self):
        self.tool = []
        MTBL = MT.ToolData()
        MLT = MTBL.ToolBarList()
        i = 0
        for T in MLT:

            MTB = MT.MyAuiToolbar(self)
            MyTL = MTB.data

            self.tool.append( MTB.CreatTool(MLT[T]) )
            self.tool[i].SetToolBitmapSize(wx.Size(24, 24)) #<<<=== use Config
            self.tool[i].Realize()
            self.m_mgr.AddPane(self.tool[i], wx.aui.AuiPaneInfo().Name("tb"+str(i)).Caption("Toolbar").
                           ToolbarPane().Top().LeftDockable(True).RightDockable(False))
            self.Bind(wx.EVT_TOOL_RANGE, self.OnTool, id=self.tool[i].mytb[0].GetId(), id2=self.tool[i].mytb[-1].GetId())
            i += 1


    def APnls2(self):
        StartPane = eval(self.config.Read('Panes'))
        self.Pnls = []
        ML = PA.MyLstPnl2()

        for pnl in ML.lstpnl:
            #if pnl[1]+'.py' in MLA.GetAuiPnl():
            if pnl[6] in ML.PrP.keys():
                ii = importlib.import_module('Src.AUI.' +  ML.PrP[pnl[6]].replace('.py',''))
                mp = ii.MyPanel1(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
                self.Pnls.append(mp)
                PInfo = ML.GetAuiInfo(pnl[1])
                self.m_mgr.AddPane(mp, PInfo)
                if pnl[1] in StartPane:
                    self.m_mgr.GetPane(pnl[1]).Show()
                else:
                    self.m_mgr.GetPane(pnl[1]).Hide()

    def BGrnd(self,BGF):
        self.bmpwin = BG.BGPanel(self,BGF)
        self.m_mgr.AddPane( self.bmpwin, wx.aui.AuiPaneInfo() .CaptionVisible( False ) .Center() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.Size( 800,600 )) )


    def NewMenu(self):
        self.newmenu = True
        self.barMenu = wx.MenuBar()
        self.SetMenuBar(self.barMenu)
        return self.barMenu

    def UpdateMenu(self,imenu,menu):
        self.SetMenuBar(imenu)

        frstitm = menu[0][0].GetMenuItems()
        lastitm = menu[-1][0].GetMenuItems()
        if len(frstitm) != 0:
            h = frstitm[0].GetId()
            #h1 = lastitm[-1].GetId()
            #print(h,h1)
            #self.Bind(wx.EVT_MENU_RANGE, self.OnMenu, id=h1, id2=h.GetId())
            self.Bind(wx.EVT_MENU_RANGE, self.OnMenu, id=101, id2=9999)

    def NewToolBar(self):
        self.toolbar = MT.MyToolbar()
        self.SetToolBar()

    def Refreshwin(self):
        self.Refresh()
        self.Update()
        #self.UpdateWindowUI(wx.UPDATE_UI_FROMIDLE)