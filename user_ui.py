# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Abholung(object):
    def setupUi(self, Abholung):
        Abholung.setObjectName("Abholung")
        Abholung.resize(1576, 558)
        Abholung.setStyleSheet("background-color: rgb(7, 7, 7);")
        self.centralwidget = QtWidgets.QWidget(Abholung)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setStyleSheet("border-top-color: rgb(0, 0, 0);\n"
"border-bottom-color: rgb(6, 6, 6);\n"
"gridline-color: rgb(6, 6, 6);\n"
"border-left-color: rgb(9, 9, 9);\n"
"border-top-color: rgb(4, 4, 4);\n"
"gridline-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("border-color: rgb(0,0,0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.onsite_list_view = QtWidgets.QListWidget(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setItalic(True)
        self.onsite_list_view.setFont(font)
        self.onsite_list_view.setStyleSheet("color:white;\n"
"gridline-color: rgb(3, 3, 3);\n"
"border-left-color: rgb(18, 18, 18);\n"
"border-bottom-color: rgb(9, 9, 9);\n"
"border-top-color: rgb(29, 29, 29);\n"
"border-color: rgb(8, 8, 8);")
        self.onsite_list_view.setObjectName("onsite_list_view")
        self.horizontalLayout_2.addWidget(self.onsite_list_view)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.online_list_view = QtWidgets.QListWidget(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(72)
        font.setItalic(True)
        self.online_list_view.setFont(font)
        self.online_list_view.setStyleSheet("color:white;")
        self.online_list_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.online_list_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.online_list_view.setObjectName("online_list_view")
        self.horizontalLayout_3.addWidget(self.online_list_view)
        spacerItem3 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame.raise_()
        self.frame_2.raise_()
        self.line_2.raise_()
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        Abholung.setCentralWidget(self.centralwidget)

        self.retranslateUi(Abholung)
        QtCore.QMetaObject.connectSlotsByName(Abholung)

    def retranslateUi(self, Abholung):
        _translate = QtCore.QCoreApplication.translate
        Abholung.setWindowTitle(_translate("Abholung", "MainWindow"))
        self.label_3.setText(_translate("Abholung", "Bitte Abholen"))
        self.label.setText(_translate("Abholung", "Bestellung vor Ort/Telephone "))
        self.label_2.setText(_translate("Abholung", "Onlinebestellung"))
