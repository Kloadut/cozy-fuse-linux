# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Thu Aug  7 16:45:45 2014
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import os
# end wxGlade


class CozyFrame(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CozyFrame.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.label_informations = wx.StaticText(self.panel_3, wx.ID_ANY, _("Fill bellow fields with your Cozy informations to start the file synchronization."))
        self.static_line_3 = wx.StaticLine(self.panel_3, wx.ID_ANY)
        self.label_cozy_url = wx.StaticText(self.panel_3, wx.ID_ANY, _("URL of your Cozy"))
        self.text_cozy_url = wx.TextCtrl(self.panel_3, wx.ID_ANY, _("https://mycozy.cozycloud.cc"), style=wx.TE_AUTO_URL)
        self.label_cozy_password = wx.StaticText(self.panel_3, wx.ID_ANY, _("Password of your Cozy"))
        self.text_cozy_password = wx.TextCtrl(self.panel_3, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.label_device_name = wx.StaticText(self.panel_3, wx.ID_ANY, _("Device name"))
        self.text_device_name = wx.TextCtrl(self.panel_3, wx.ID_ANY, _("myhost-1234"))
        self.label_sync_folder = wx.StaticText(self.panel_3, wx.ID_ANY, _("Synchronized folder"))
        self.text_sync_folder = wx.TextCtrl(self.panel_3, wx.ID_ANY, _("/home/user/sync"))
        self.button_select_folder = wx.Button(self.panel_3, wx.ID_OPEN, "")
        self.static_line_2 = wx.StaticLine(self.panel_3, wx.ID_ANY)
        self.button_discard = wx.Button(self.panel_3, wx.ID_CANCEL, "")
        self.button_save = wx.Button(self.panel_3, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.select_sync_folder, self.button_select_folder)
        self.Bind(wx.EVT_BUTTON, self.discard_configuration_changes, self.button_discard)
        self.Bind(wx.EVT_BUTTON, self.save_configuration_changes, self.button_save)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: CozyFrame.__set_properties
        self.SetTitle(_("Cozy client configuration"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("icon/icon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((400, 430))
        self.label_cozy_url.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_cozy_url.SetToolTipString(_("Indicate the complete URL of your Cozy, do not forget to prepend \"http://\" or \"https://\""))
        self.label_cozy_password.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_cozy_password.SetToolTipString(_("This is your Cozy password, used to connect to your Cozy"))
        self.label_device_name.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_device_name.SetToolTipString(_("The name of this device to sync. It must contain only lowercase characters, dashes or numbers (e.g. \"my-laptop\")"))
        self.label_sync_folder.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_sync_folder.SetToolTipString(_("The folder where your files will appear into. It must be an empty one."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CozyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 2, 0, 0)
        sizer_2.Add((30, 20), 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_informations, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.static_line_3, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_cozy_url, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_4.Add(self.text_cozy_url, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_cozy_password, 0, wx.EXPAND, 0)
        sizer_4.Add(self.text_cozy_password, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_device_name, 0, wx.EXPAND, 0)
        sizer_4.Add(self.text_device_name, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.label_sync_folder, 0, wx.EXPAND, 0)
        sizer_4.Add(self.text_sync_folder, 0, wx.EXPAND, 0)
        sizer_4.Add(self.button_select_folder, 0, wx.ALIGN_RIGHT, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_4.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.button_discard, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.button_save, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_4)
        sizer_2.Add(self.panel_3, 1, wx.EXPAND, 0)
        sizer_2.Add((30, 20), 0, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def SetMainTray(self, tray):
        self.tray = tray

    def select_sync_folder(self, event):  # wxGlade: CozyFrame.<event_handler>
        dialog = wx.DirDialog(None, _("Choose an empty folder for the synchronization"))
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            if os.listdir(path) == []:
                self.text_sync_folder.SetValue(dialog.GetPath())
            else:
                from CozyError import CozyError
                error = CozyError(None, wx.ID_ANY, "")
                error.error_message.SetLabel(_("The chosen folder is not empty, please choose another one"))
                error.Show()
        event.Skip()

    def discard_configuration_changes(self, event):  # wxGlade: CozyFrame.<event_handler>
        print "Event handler 'discard_configuration_changes' not implemented!"
        event.Skip()

    def save_configuration_changes(self, event):  # wxGlade: CozyFrame.<event_handler>
        print "Event handler 'save_configuration_changes' not implemented!"
        event.Skip()

# end of class CozyFrame
