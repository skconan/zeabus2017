#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Jan  1 19:37:34 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(666, 705)
        MainWindow.setMinimumSize(QtCore.QSize(666, 705))
        MainWindow.setMaximumSize(QtCore.QSize(666, 705))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 671))
        self.tabWidget.setMinimumSize(QtCore.QSize(641, 671))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(40, 230, 1251, 331))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtGui.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 70, 164, 118))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_7 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 441, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 70, 172, 118))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton_8 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.lineEdit = QtGui.QLineEdit(self.tab_4)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(10, 300, 601, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.layoutWidget_3 = QtGui.QWidget(self.tab_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(290, 30, 210, 253))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.checkBox_9 = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.verticalLayout_5.addWidget(self.checkBox_9)
        self.checkBox_10 = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.verticalLayout_5.addWidget(self.checkBox_10)
        self.checkBox_11 = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.verticalLayout_5.addWidget(self.checkBox_11)
        self.checkBox_12 = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.verticalLayout_5.addWidget(self.checkBox_12)
        self.checkBox_13 = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.verticalLayout_5.addWidget(self.checkBox_13)
        self.layoutWidget2 = QtGui.QWidget(self.tab_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 30, 144, 253))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkBox = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.checkBox_5 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.checkBox_6 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.verticalLayout_4.addWidget(self.checkBox_6)
        self.checkBox_7 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.verticalLayout_4.addWidget(self.checkBox_7)
        self.checkBox_8 = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.verticalLayout_4.addWidget(self.checkBox_8)
        self.layoutWidget3 = QtGui.QWidget(self.tab_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 410, 541, 29))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_14 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.horizontalLayout.addWidget(self.pushButton_15)
        self.pushButton_23 = QtGui.QPushButton(self.layoutWidget3)
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.horizontalLayout.addWidget(self.pushButton_23)
        self.label_5 = QtGui.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(20, 570, 591, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(270, 450, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.layoutWidget4 = QtGui.QWidget(self.tab_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 480, 541, 29))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_17 = QtGui.QPushButton(self.layoutWidget4)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.horizontalLayout_2.addWidget(self.pushButton_17)
        self.pushButton_21 = QtGui.QPushButton(self.layoutWidget4)
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.horizontalLayout_2.addWidget(self.pushButton_21)
        self.pushButton_25 = QtGui.QPushButton(self.layoutWidget4)
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.horizontalLayout_2.addWidget(self.pushButton_25)
        self.layoutWidget5 = QtGui.QWidget(self.tab_4)
        self.layoutWidget5.setGeometry(QtCore.QRect(170, 370, 276, 29))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_20 = QtGui.QPushButton(self.layoutWidget5)
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.horizontalLayout_3.addWidget(self.pushButton_20)
        self.pushButton_19 = QtGui.QPushButton(self.layoutWidget5)
        self.pushButton_19.setEnabled(True)
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.horizontalLayout_3.addWidget(self.pushButton_19)
        self.layoutWidget6 = QtGui.QWidget(self.tab_4)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 330, 601, 29))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButton_13 = QtGui.QPushButton(self.layoutWidget6)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.horizontalLayout_8.addWidget(self.pushButton_13)
        self.pushButton_31 = QtGui.QPushButton(self.layoutWidget6)
        self.pushButton_31.setEnabled(True)
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.horizontalLayout_8.addWidget(self.pushButton_31)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 240, 601, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.layoutWidget7 = QtGui.QWidget(self.tab_5)
        self.layoutWidget7.setGeometry(QtCore.QRect(30, 40, 189, 192))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.checkBox_14 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.verticalLayout_6.addWidget(self.checkBox_14)
        self.checkBox_15 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.verticalLayout_6.addWidget(self.checkBox_15)
        self.checkBox_16 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.verticalLayout_6.addWidget(self.checkBox_16)
        self.checkBox_17 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.verticalLayout_6.addWidget(self.checkBox_17)
        self.checkBox_18 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_18.setObjectName(_fromUtf8("checkBox_18"))
        self.verticalLayout_6.addWidget(self.checkBox_18)
        self.checkBox_19 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_19.setObjectName(_fromUtf8("checkBox_19"))
        self.verticalLayout_6.addWidget(self.checkBox_19)
        self.checkBox_20 = QtGui.QCheckBox(self.layoutWidget7)
        self.checkBox_20.setObjectName(_fromUtf8("checkBox_20"))
        self.verticalLayout_6.addWidget(self.checkBox_20)
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(30, 570, 591, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_24 = QtGui.QPushButton(self.tab_5)
        self.pushButton_24.setGeometry(QtCore.QRect(230, 320, 181, 27))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.label_8 = QtGui.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(300, 380, 66, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.layoutWidget8 = QtGui.QWidget(self.tab_5)
        self.layoutWidget8.setGeometry(QtCore.QRect(30, 410, 581, 29))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_22 = QtGui.QPushButton(self.layoutWidget8)
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.horizontalLayout_4.addWidget(self.pushButton_22)
        self.pushButton_18 = QtGui.QPushButton(self.layoutWidget8)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.horizontalLayout_4.addWidget(self.pushButton_18)
        self.pushButton_26 = QtGui.QPushButton(self.layoutWidget8)
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.horizontalLayout_4.addWidget(self.pushButton_26)
        self.layoutWidget9 = QtGui.QWidget(self.tab_5)
        self.layoutWidget9.setGeometry(QtCore.QRect(20, 280, 601, 29))
        self.layoutWidget9.setObjectName(_fromUtf8("layoutWidget9"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pushButton_16 = QtGui.QPushButton(self.layoutWidget9)
        self.pushButton_16.setEnabled(True)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.horizontalLayout_7.addWidget(self.pushButton_16)
        self.pushButton_30 = QtGui.QPushButton(self.layoutWidget9)
        self.pushButton_30.setEnabled(True)
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.horizontalLayout_7.addWidget(self.pushButton_30)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.layoutWidget_4 = QtGui.QWidget(self.tab_6)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 20, 189, 192))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.checkBox_21 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_21.setObjectName(_fromUtf8("checkBox_21"))
        self.verticalLayout_7.addWidget(self.checkBox_21)
        self.checkBox_22 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_22.setObjectName(_fromUtf8("checkBox_22"))
        self.verticalLayout_7.addWidget(self.checkBox_22)
        self.checkBox_23 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_23.setObjectName(_fromUtf8("checkBox_23"))
        self.verticalLayout_7.addWidget(self.checkBox_23)
        self.checkBox_24 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_24.setObjectName(_fromUtf8("checkBox_24"))
        self.verticalLayout_7.addWidget(self.checkBox_24)
        self.checkBox_25 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_25.setObjectName(_fromUtf8("checkBox_25"))
        self.verticalLayout_7.addWidget(self.checkBox_25)
        self.checkBox_26 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_26.setObjectName(_fromUtf8("checkBox_26"))
        self.verticalLayout_7.addWidget(self.checkBox_26)
        self.checkBox_27 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_27.setObjectName(_fromUtf8("checkBox_27"))
        self.verticalLayout_7.addWidget(self.checkBox_27)
        self.label_9 = QtGui.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(40, 390, 131, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(250, 440, 171, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 440, 113, 27))
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 220, 551, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.layoutWidget_5 = QtGui.QWidget(self.tab_6)
        self.layoutWidget_5.setGeometry(QtCore.QRect(330, 20, 189, 192))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.checkBox_28 = QtGui.QCheckBox(self.layoutWidget_5)
        self.checkBox_28.setEnabled(False)
        self.checkBox_28.setObjectName(_fromUtf8("checkBox_28"))
        self.verticalLayout_8.addWidget(self.checkBox_28)
        self.checkBox_29 = QtGui.QCheckBox(self.layoutWidget_5)
        self.checkBox_29.setEnabled(False)
        self.checkBox_29.setObjectName(_fromUtf8("checkBox_29"))
        self.verticalLayout_8.addWidget(self.checkBox_29)
        self.checkBox_30 = QtGui.QCheckBox(self.layoutWidget_5)
        self.checkBox_30.setEnabled(False)
        self.checkBox_30.setObjectName(_fromUtf8("checkBox_30"))
        self.verticalLayout_8.addWidget(self.checkBox_30)
        self.checkBox_31 = QtGui.QCheckBox(self.layoutWidget_5)
        self.checkBox_31.setEnabled(False)
        self.checkBox_31.setObjectName(_fromUtf8("checkBox_31"))
        self.verticalLayout_8.addWidget(self.checkBox_31)
        self.checkBox_32 = QtGui.QCheckBox(self.layoutWidget_5)
        self.checkBox_32.setEnabled(False)
        self.checkBox_32.setObjectName(_fromUtf8("checkBox_32"))
        self.verticalLayout_8.addWidget(self.checkBox_32)
        self.layoutWidget10 = QtGui.QWidget(self.tab_6)
        self.layoutWidget10.setGeometry(QtCore.QRect(30, 410, 515, 24))
        self.layoutWidget10.setObjectName(_fromUtf8("layoutWidget10"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton = QtGui.QRadioButton(self.layoutWidget10)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget10)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.layoutWidget10)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_5.addWidget(self.radioButton_3)
        self.layoutWidget11 = QtGui.QWidget(self.tab_6)
        self.layoutWidget11.setGeometry(QtCore.QRect(20, 270, 561, 29))
        self.layoutWidget11.setObjectName(_fromUtf8("layoutWidget11"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_27 = QtGui.QPushButton(self.layoutWidget11)
        self.pushButton_27.setEnabled(True)
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.horizontalLayout_6.addWidget(self.pushButton_27)
        self.pushButton_29 = QtGui.QPushButton(self.layoutWidget11)
        self.pushButton_29.setEnabled(True)
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.horizontalLayout_6.addWidget(self.pushButton_29)
        self.label_16 = QtGui.QLabel(self.tab_6)
        self.label_16.setGeometry(QtCore.QRect(40, 580, 511, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.layoutWidget_6 = QtGui.QWidget(self.tab_6)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 310, 561, 29))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.pushButton_32 = QtGui.QPushButton(self.layoutWidget_6)
        self.pushButton_32.setEnabled(True)
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.horizontalLayout_9.addWidget(self.pushButton_32)
        self.pushButton_33 = QtGui.QPushButton(self.layoutWidget_6)
        self.pushButton_33.setEnabled(True)
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.horizontalLayout_9.addWidget(self.pushButton_33)
        self.pushButton_34 = QtGui.QPushButton(self.tab_6)
        self.pushButton_34.setGeometry(QtCore.QRect(180, 480, 241, 27))
        self.pushButton_34.setObjectName(_fromUtf8("pushButton_34"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.label_15 = QtGui.QLabel(self.tab_7)
        self.label_15.setGeometry(QtCore.QRect(300, 170, 131, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.progressBar = QtGui.QProgressBar(self.tab_7)
        self.progressBar.setGeometry(QtCore.QRect(60, 200, 531, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton_28 = QtGui.QPushButton(self.tab_7)
        self.pushButton_28.setEnabled(True)
        self.pushButton_28.setGeometry(QtCore.QRect(240, 20, 141, 27))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.label_14 = QtGui.QLabel(self.tab_7)
        self.label_14.setGeometry(QtCore.QRect(70, 140, 281, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_12 = QtGui.QLabel(self.tab_7)
        self.label_12.setGeometry(QtCore.QRect(70, 80, 281, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_7)
        self.label_13.setGeometry(QtCore.QRect(70, 110, 281, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_11 = QtGui.QLabel(self.tab_7)
        self.label_11.setGeometry(QtCore.QRect(250, 50, 131, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.videoFrame = QtGui.QLabel(self.tab)
        self.videoFrame.setGeometry(QtCore.QRect(20, 60, 261, 191))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.videoFrame_2 = QtGui.QLabel(self.tab)
        self.videoFrame_2.setGeometry(QtCore.QRect(350, 60, 261, 191))
        self.videoFrame_2.setObjectName(_fromUtf8("videoFrame_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(250, 20, 131, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.videoFrame_3 = QtGui.QLabel(self.tab)
        self.videoFrame_3.setGeometry(QtCore.QRect(20, 250, 261, 191))
        self.videoFrame_3.setObjectName(_fromUtf8("videoFrame_3"))
        self.videoFrame_4 = QtGui.QLabel(self.tab)
        self.videoFrame_4.setGeometry(QtCore.QRect(350, 250, 261, 191))
        self.videoFrame_4.setObjectName(_fromUtf8("videoFrame_4"))
        self.videoFrame_5 = QtGui.QLabel(self.tab)
        self.videoFrame_5.setGeometry(QtCore.QRect(20, 450, 261, 191))
        self.videoFrame_5.setObjectName(_fromUtf8("videoFrame_5"))
        self.videoFrame_6 = QtGui.QLabel(self.tab)
        self.videoFrame_6.setGeometry(QtCore.QRect(350, 450, 261, 191))
        self.videoFrame_6.setObjectName(_fromUtf8("videoFrame_6"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 161, 27))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 20, 149, 151))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_12 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_11 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.verticalLayout.addWidget(self.pushButton_11)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Zeabus GUI", None))
        # self.label.setText(_translate("MainWindow", "Client Side", None))
        self.pushButton_5.setText(_translate("MainWindow", "1. start minimal.launch", None))
        self.pushButton_3.setText(_translate("MainWindow", "3. Start Flight Display", None))
        self.pushButton_7.setText(_translate("MainWindow", "5. Start PID", None))
        self.label_3.setText(_translate("MainWindow", "please read the instruction in README.md before proceeding", None))
        # self.label_2.setText(_translate("MainWindow", "Vehicle Side", None))
        self.pushButton_8.setText(_translate("MainWindow", "2. start localization", None))
        self.pushButton_9.setText(_translate("MainWindow", "4. start thruster", None))
        self.pushButton_10.setText(_translate("MainWindow", "6. open camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "boeing - general", None))
        self.checkBox_9.setText(_translate("MainWindow", "Thruster controller (bit 13)", None))
        self.checkBox_10.setText(_translate("MainWindow", "GPIO (bit 12)", None))
        self.checkBox_11.setText(_translate("MainWindow", "lamp 1 (bit 14)", None))
        self.checkBox_12.setText(_translate("MainWindow", "lamp 2 (bit 15)", None))
        self.checkBox_13.setText(_translate("MainWindow", "pneumatic (bit 9)", None))
        self.checkBox.setText(_translate("MainWindow", "Thruster 1 (bit 1)", None))
        self.checkBox_2.setText(_translate("MainWindow", "Thruster 2 (bit 2)", None))
        self.checkBox_3.setText(_translate("MainWindow", "Thruster 3 (bit 3)", None))
        self.checkBox_4.setText(_translate("MainWindow", "Thruster 4 (bit 4)", None))
        self.checkBox_5.setText(_translate("MainWindow", "Thruster 5 (bit 5)", None))
        self.checkBox_6.setText(_translate("MainWindow", "Thruster 6 (bit 6)", None))
        self.checkBox_7.setText(_translate("MainWindow", "Thruster 7 (bit 7)", None))
        self.checkBox_8.setText(_translate("MainWindow", "Thruster 8 (bit 8)", None))
        self.pushButton_14.setText(_translate("MainWindow", "emergency cut off thruster", None))
        self.pushButton_15.setText(_translate("MainWindow", "stop thruster", None))
        self.pushButton_23.setText(_translate("MainWindow", "stop all in power board", None))
        self.label_5.setText(_translate("MainWindow", "Status: stand by", None))
        self.label_7.setText(_translate("MainWindow", "utilities", None))
        self.pushButton_17.setText(_translate("MainWindow", "start service caller", None))
        self.pushButton_21.setText(_translate("MainWindow", "start Rviz", None))
        self.pushButton_25.setText(_translate("MainWindow", "start imu visualization", None))
        self.pushButton_20.setText(_translate("MainWindow", "start all thruster", None))
        self.pushButton_19.setText(_translate("MainWindow", "full option mode", None))
        self.pushButton_13.setText(_translate("MainWindow", "commit", None))
        self.pushButton_31.setText(_translate("MainWindow", "refresh power board bit", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "airbus - power board", None))
        self.checkBox_14.setText(_translate("MainWindow", "sonar (bit 3)", None))
        self.checkBox_15.setText(_translate("MainWindow", "altimeter (bit 4)", None))
        self.checkBox_16.setText(_translate("MainWindow", "DSP (bit 5)", None))
        self.checkBox_17.setText(_translate("MainWindow", "DVL (bit 6)", None))
        self.checkBox_18.setText(_translate("MainWindow", "LNA (bit 7)", None))
        self.checkBox_19.setText(_translate("MainWindow", "IMU - Microstrain (bit 8)", None))
        self.checkBox_20.setText(_translate("MainWindow", "IMU - FOG (bit 10)", None))
        self.label_6.setText(_translate("MainWindow", "Status: stand by", None))
        self.pushButton_24.setText(_translate("MainWindow", "stop all in sensor board", None))
        self.label_8.setText(_translate("MainWindow", "utilities", None))
        self.pushButton_22.setText(_translate("MainWindow", "start Rviz", None))
        self.pushButton_18.setText(_translate("MainWindow", "start service caller", None))
        self.pushButton_26.setText(_translate("MainWindow", "imu visualization", None))
        self.pushButton_16.setText(_translate("MainWindow", "commit", None))
        self.pushButton_30.setText(_translate("MainWindow", "refresh sensor board bit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "airbus - sensors board", None))
        self.checkBox_21.setText(_translate("MainWindow", "sink 0", None))
        self.checkBox_22.setText(_translate("MainWindow", "sink 1", None))
        self.checkBox_23.setText(_translate("MainWindow", "sink 2", None))
        self.checkBox_24.setText(_translate("MainWindow", "sink 3", None))
        self.checkBox_25.setText(_translate("MainWindow", "sink 4", None))
        self.checkBox_26.setText(_translate("MainWindow", "sink 5", None))
        self.checkBox_27.setText(_translate("MainWindow", "sink 6", None))
        self.label_9.setText(_translate("MainWindow", "Barometer mode", None))
        self.label_10.setText(_translate("MainWindow", "window size (max=128)", None))
        self.checkBox_28.setText(_translate("MainWindow", "led 0(green)", None))
        self.checkBox_29.setText(_translate("MainWindow", "led 1(red)", None))
        self.checkBox_30.setText(_translate("MainWindow", "led 2", None))
        self.checkBox_31.setText(_translate("MainWindow", "led 3(white)", None))
        self.checkBox_32.setText(_translate("MainWindow", "led 4", None))
        self.radioButton.setText(_translate("MainWindow", "Normal_on demand", None))
        self.radioButton_2.setText(_translate("MainWindow", "Full speed", None))
        self.radioButton_3.setText(_translate("MainWindow", "Full speed with moving average", None))
        self.pushButton_27.setText(_translate("MainWindow", "commit gpio board", None))
        self.pushButton_29.setText(_translate("MainWindow", "refresh current bit from gpio", None))
        self.label_16.setText(_translate("MainWindow", "Status: stand by", None))
        self.pushButton_32.setText(_translate("MainWindow", "start all sink", None))
        self.pushButton_33.setText(_translate("MainWindow", "stop all sink", None))
        self.pushButton_34.setText(_translate("MainWindow", "commit barometer mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "airbus - GPIO board/battery", None))
        self.label_15.setText(_translate("MainWindow", "Charge", None))
        self.pushButton_28.setText(_translate("MainWindow", "refresh battery", None))
        self.label_14.setText(_translate("MainWindow", "Temperature: N/A", None))
        self.label_12.setText(_translate("MainWindow", "Voltage: N/A", None))
        self.label_13.setText(_translate("MainWindow", "Current: N/A", None))
        self.label_11.setText(_translate("MainWindow", "Battery Info", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "airbus - battery", None))
        self.videoFrame.setText(_translate("MainWindow", "Video0 is disabled", None))
        self.videoFrame_2.setText(_translate("MainWindow", "Video1 is disabled", None))
        self.pushButton.setText(_translate("MainWindow", "enable Cameras", None))
        self.videoFrame_3.setText(_translate("MainWindow", "Video2 is disabled", None))
        self.videoFrame_4.setText(_translate("MainWindow", "Video3 is disabled", None))
        self.videoFrame_5.setText(_translate("MainWindow", "Video4 is disabled", None))
        self.videoFrame_6.setText(_translate("MainWindow", "Video5 is disabled", None))
        self.pushButton_2.setText(_translate("MainWindow", "enable Color Picker", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Camera", None))
        self.label_4.setText(_translate("MainWindow", "Indoor test", None))
        self.pushButton_12.setText(_translate("MainWindow", "Start Joy F710", None))
        self.pushButton_6.setText(_translate("MainWindow", "Start Joy extream", None))
        self.pushButton_4.setText(_translate("MainWindow", "Start Simulation", None))
        self.pushButton_11.setText(_translate("MainWindow", "Start Rviz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "indoor test", None))

