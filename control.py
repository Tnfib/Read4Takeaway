from PyQt5 import QtWidgets  # Import the PyQt4 module we'll need
import sys

from model import init
import controll_ui

import user_ui
# from playsound import playsound
# import os  # For listing directory methods


noti_sound = 'ressources/noti_sound.mp3'


class UserOP(QtWidgets.QMainWindow, user_ui.Ui_Abholung):
    """docstring for UserOP"""
    def __init__(self, onsite_bills, online_bills):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically

        self.onsite_bills = onsite_bills
        self.online_bills = online_bills

    def refresh_online_list(self):
        current_list = self.online_bills.tolist()
        self.online_list_view.clear()
        for item in current_list:
            self.online_list_view.addItem(item)

    def refresh_onsite_list(self):
        current_list = self.onsite_bills.tolist()
        self.onsite_list_view.clear()
        for item in current_list:
            self.onsite_list_view.addItem(item)

        # self.onsite_list_view


class CounterOP(QtWidgets.QMainWindow, controll_ui.Ui_controll_ui):
    def __init__(self, onsite_bills, online_bills, user_view):
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined

        self.onsite_bills = onsite_bills
        self.online_bills = online_bills
        self.user_view = user_view
        self.connect_elements()

        self.MISSING_NUMBER_ERROR = "Bitte Nummer eingeben"
        self.DUPLICATE_NUMBER_ERROR = "Diese Nummer wurde bereits eingegeben"
        self.REMOVE_NOT_EXISTING = "Diese Nummer existiert nicht"
        self.refresh_view('online')
        self.refresh_view('onsite')
        # self.frame_2 =None
        # self.btnBrowse.clicked.connect(self.browse_folder)  # When the button is pressed
        # Execute browse_folder function

    def alert(self, msg, string):
        # assert False, 'please implemenent'
        msgboxwarning = QtWidgets.QMessageBox()
        msgboxwarning.setText(msg + ' ' + str(string))
        msgboxwarning.exec_()
        return

    def refresh_view(self, view_type):

        if view_type == 'onsite':
            current_list = self.onsite_bills.tolist()
            self.onsite_list_view.clear()

            for item in current_list:
                self.onsite_list_view.addItem(item)
            self.user_view.refresh_onsite_list()
        else:
            # onsite
            current_list = self.online_bills.tolist()
            self.online_list_view.clear()

            for item in current_list:
                self.online_list_view.addItem(item)
            self.user_view.refresh_online_list()

    def connect_elements(self):
        self.btn_onsite_ready.clicked.connect(self.onsite_ready)
        self.btn_onsite_remove.clicked.connect(self.onsite_remove)
        self.btn_onsite_reset.clicked.connect(self.onsite_reset)

        self.btn_online_ready.clicked.connect(self.online_ready)
        self.btn_online_remove.clicked.connect(self.online_remove)
        self.btn_online_reset.clicked.connect(self.online_reset)

    def onsite_ready(self):
        # print (self.txtf_onsite_add.toPlainText())
        if self.txtf_onsite_add  == "":
            self.alert(self.MISSING_NUMBER_ERROR, '')
        failed_cases, success_cases = self.onsite_bills.add(self.txtf_onsite_add.toPlainText())

        self.txtf_onsite_add.clear()
        self.refresh_view('onsite')
        if len(failed_cases) > 0:
            self.alert(self.DUPLICATE_NUMBER_ERROR, failed_cases)
        # if len(success_cases) >0:
        #     playsound(noti_sound)

    def onsite_remove(self):
        items_to_remove = ''
        for i in self.onsite_list_view.selectedItems():
            items_to_remove += i.text()
            items_to_remove += ' '
        # [items_to_remove = for i in self.onsite_list_view.selectedItems().text()

        # if self.txtf_onsite_remove  == "":
        #     self.alert(self.MISSING_NUMBER_ERROR,'')
        failed_cases = self.onsite_bills.remove(items_to_remove)
        # self.txtf_onsite_remove.clear()
        self.refresh_view('onsite')
        if len(failed_cases) > 0:
            self.alert(self.REMOVE_NOT_EXISTING, failed_cases)

    def onsite_reset(self):
        self.onsite_bills.reset()
        self.onsite_list_view.clear()
        self.user_view.onsite_list_view.clear()

    def online_ready(self):
        # if self.txtf_online_add  == "":
        #     self.alert(self.MISSING_NUMBER_ERROR, '')
        failed_cases, success_cases = self.online_bills.add(
            self.txtf_online_add.toPlainText())
        self.txtf_online_add.clear()
        self.refresh_view('online')
        # if len(success_cases) >0:
        #     playsound(noti_sound)
        if len(failed_cases) > 0:
            self.alert(self.DUPLICATE_NUMBER_ERROR, failed_cases)

    def online_remove(self):
        # if self.txtf_online_remove  == "":
        #     self.alert(self.MISSING_NUMBER_ERROR, '')
        # items_to_remove = self.online_list_view.selectedItems()[0].text()
        items_to_remove = ''
        for i in self.online_list_view.selectedItems():
            items_to_remove += i.text()
            items_to_remove += ' '

        failed_cases = self.online_bills.remove(items_to_remove)
        # self.txtf_online_remove.clear()
        self.refresh_view('online')
        if len(failed_cases) > 0:
            self.alert(self.REMOVE_NOT_EXISTING, failed_cases)

    def online_reset(self):
        self.online_bills.reset()
        self.online_list_view.clear()
        self.user_view.online_list_view.clear()
