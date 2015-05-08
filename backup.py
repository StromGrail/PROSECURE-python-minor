from PyQt4 import QtCore, QtGui
import SimpleHTTPServer
import SocketServer
import smtplib, os
import time
import threading
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import socket
import sys
import select
from communication import send, receive
import client

#go to line 546 to hostname



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
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/networking.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton_7 = QtGui.QPushButton(self.tab)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_4.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_4.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.gridLayout_4.addWidget(self.textBrowser_2, 0, 0, 1, 4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 3, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 3, 1, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.tab)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_4.addWidget(self.lineEdit_15, 3, 2, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.tab)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_4.addWidget(self.lineEdit_14, 2, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.Email = QtGui.QWidget()
        self.Email.setObjectName(_fromUtf8("Email"))
        self.gridLayout = QtGui.QGridLayout(self.Email)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.Email)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.le_mail_username = QtGui.QLineEdit(self.Email)
        self.le_mail_username.setObjectName(_fromUtf8("le_mail_username"))
        self.horizontalLayout_2.addWidget(self.le_mail_username)
        self.label_4 = QtGui.QLabel(self.Email)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.le_mail_pass = QtGui.QLineEdit(self.Email)
        self.le_mail_pass.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_mail_pass.setInputMask(_fromUtf8(""))
        self.le_mail_pass.setObjectName(_fromUtf8("le_mail_pass"))
        self.horizontalLayout_2.addWidget(self.le_mail_pass)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.Email)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.le_mail_from = QtGui.QLineEdit(self.Email)
        self.le_mail_from.setObjectName(_fromUtf8("le_mail_from"))
        self.horizontalLayout_3.addWidget(self.le_mail_from)
        self.label_5 = QtGui.QLabel(self.Email)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.le_mail_to = QtGui.QLineEdit(self.Email)
        self.le_mail_to.setObjectName(_fromUtf8("le_mail_to"))
        self.horizontalLayout_3.addWidget(self.le_mail_to)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.Email)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.le_mail_sub = QtGui.QLineEdit(self.Email)
        self.le_mail_sub.setObjectName(_fromUtf8("le_mail_sub"))
        self.horizontalLayout_4.addWidget(self.le_mail_sub)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.Email)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem1 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.pte_mail_msg = QtGui.QPlainTextEdit(self.Email)
        self.pte_mail_msg.setObjectName(_fromUtf8("pte_mail_msg"))
        self.gridLayout.addWidget(self.pte_mail_msg, 4, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(431, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_mail_send = QtGui.QPushButton(self.Email)
        self.btn_mail_send.setObjectName(_fromUtf8("btn_mail_send"))
        self.horizontalLayout.addWidget(self.btn_mail_send)
        self.btn_mail_clear = QtGui.QPushButton(self.Email)
        self.btn_mail_clear.setObjectName(_fromUtf8("btn_mail_clear"))
        self.horizontalLayout.addWidget(self.btn_mail_clear)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.tabWidget.addTab(self.Email, _fromUtf8(""))
        self.File = QtGui.QWidget()
        self.File.setObjectName(_fromUtf8("File"))
        self.gridLayout_3 = QtGui.QGridLayout(self.File)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_11 = QtGui.QLabel(self.File)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.lineEdit_8 = QtGui.QLineEdit(self.File)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_6.addWidget(self.lineEdit_8)
        self.label_12 = QtGui.QLabel(self.File)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.lineEdit_9 = QtGui.QLineEdit(self.File)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalLayout_6.addWidget(self.lineEdit_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_13 = QtGui.QLabel(self.File)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lineEdit_10 = QtGui.QLineEdit(self.File)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.horizontalLayout_7.addWidget(self.lineEdit_10)
        self.label_15 = QtGui.QLabel(self.File)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_7.addWidget(self.label_15)
        self.lineEdit_12 = QtGui.QLineEdit(self.File)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.horizontalLayout_7.addWidget(self.lineEdit_12)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_16 = QtGui.QLabel(self.File)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_8.addWidget(self.label_16)
        self.lineEdit_13 = QtGui.QLineEdit(self.File)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.horizontalLayout_8.addWidget(self.lineEdit_13)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lineEdit_11 = QtGui.QLineEdit(self.File)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.horizontalLayout_9.addWidget(self.lineEdit_11)
        self.pushButton_8 = QtGui.QPushButton(self.File)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.progressBar = QtGui.QProgressBar(self.File)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_10.addWidget(self.progressBar)
        self.pushButton_9 = QtGui.QPushButton(self.File)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.tabWidget.addTab(self.File, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(293, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 1, 4)
        spacerItem4 = QtGui.QSpacerItem(352, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 5)
        self.pushButton_4 = QtGui.QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 5, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 6, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 7, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 8)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFie = QtGui.QMenu(self.menubar)
        self.menuFie.setObjectName(_fromUtf8("menuFie"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_Tools = QtGui.QMenu(self.menubar)
        self.menu_Tools.setObjectName(_fromUtf8("menu_Tools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionStart_Server = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/upcoming-work.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_Server.setIcon(icon1)
        self.actionStart_Server.setObjectName(_fromUtf8("actionStart_Server"))
        self.actionStop_Server = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/busy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Server.setIcon(icon2)
        self.actionStop_Server.setObjectName(_fromUtf8("actionStop_Server"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/sign-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/contact.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/lightbulb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionStart_Server_2 = QtGui.QAction(MainWindow)
        self.actionStart_Server_2.setIcon(icon1)
        self.actionStart_Server_2.setObjectName(_fromUtf8("actionStart_Server_2"))
        self.actionSetting = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/LanApp/images/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetting.setIcon(icon6)
        self.actionSetting.setObjectName(_fromUtf8("actionSetting"))
        self.actionStop_server = QtGui.QAction(MainWindow)
        self.actionStop_server.setIcon(icon2)
        self.actionStop_server.setObjectName(_fromUtf8("actionStop_server"))
        self.actionHelp_2 = QtGui.QAction(MainWindow)
        self.actionHelp_2.setIcon(icon5)
        self.actionHelp_2.setObjectName(_fromUtf8("actionHelp_2"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setIcon(icon3)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionContacts = QtGui.QAction(MainWindow)
        self.actionContacts.setIcon(icon4)
        self.actionContacts.setObjectName(_fromUtf8("actionContacts"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setIcon(icon6)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionContacts_2 = QtGui.QAction(MainWindow)
        self.actionContacts_2.setIcon(icon4)
        self.actionContacts_2.setObjectName(_fromUtf8("actionContacts_2"))
        self.menuFie.addSeparator()
        self.menuFie.addAction(self.actionStart_Server)
        self.menuFie.addAction(self.actionStop_Server)
        self.menuFie.addSeparator()
        self.menuFie.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionAbout)
        self.menu_Help.addAction(self.actionHelp)
        self.menu_Tools.addAction(self.actionSettings)
        self.menu_Tools.addAction(self.actionContacts_2)
        self.menubar.addAction(self.menuFie.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionStart_Server_2)
        self.toolBar.addAction(self.actionStop_server)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSetting)
        self.toolBar.addAction(self.actionContacts)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit_2)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionExit_2, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.btn_mail_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pte_mail_msg.clear)
        QtCore.QObject.connect(self.btn_mail_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_mail_sub.clear)
        QtCore.QObject.connect(self.btn_mail_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_mail_to.clear)
        QtCore.QObject.connect(self.btn_mail_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_mail_pass.clear)
        QtCore.QObject.connect(self.btn_mail_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_mail_from.clear)
        QtCore.QObject.connect(self.btn_mail_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_mail_username.clear)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser_2.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.clear)
        QtCore.QObject.connect(self.btn_mail_send, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.starthttpserver)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stophttpserver)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_file)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fileserver_client)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.chat)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lan App", None))
        self.pushButton_7.setText(_translate("MainWindow", "Send", None))
        self.pushButton_6.setText(_translate("MainWindow", "Clear", None))
        self.label_9.setText(_translate("MainWindow", "Type Here:", None))
        self.pushButton.setText(_translate("MainWindow", "Connect", None))
        self.lineEdit_15.setText(_translate("MainWindow", "Enter Host name here..", None))
        self.lineEdit_14.setText(_translate("MainWindow", "Enter username here..", None))
        self.label_10.setText(_translate("MainWindow", "Enter username and hostname :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Chat Client", None))
        self.label.setText(_translate("MainWindow", "Username : ", None))
        self.label_4.setText(_translate("MainWindow", "Password :", None))
        self.label_2.setText(_translate("MainWindow", "From : ", None))
        self.label_5.setText(_translate("MainWindow", "To : ", None))
        self.label_3.setText(_translate("MainWindow", "Subject : ", None))
        self.label_6.setText(_translate("MainWindow", "Message Here :", None))
        self.btn_mail_send.setText(_translate("MainWindow", "Send", None))
        self.btn_mail_clear.setText(_translate("MainWindow", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Email), _translate("MainWindow", "Instant Mail", None))
        self.label_11.setText(_translate("MainWindow", "Host : ", None))
        self.label_12.setText(_translate("MainWindow", "Port :", None))
        self.label_13.setText(_translate("MainWindow", "User Name : ", None))
        self.label_15.setText(_translate("MainWindow", "Password : ", None))
        self.label_16.setText(_translate("MainWindow", "FileName : ", None))
        self.lineEdit_11.setText(_translate("MainWindow", "Please Choose FileName To Save...", None))
        self.pushButton_8.setText(_translate("MainWindow", "Save As", None))
        self.pushButton_9.setText(_translate("MainWindow", "Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.File), _translate("MainWindow", "File Sharing", None))
        self.label_7.setText(_translate("MainWindow", "Host : ", None))
        self.label_8.setText(_translate("MainWindow", "Port : ", None))
        self.pushButton_4.setText(_translate("MainWindow", "Start Server", None))
        self.pushButton_3.setText(_translate("MainWindow", "Stop Server", None))
        self.pushButton_5.setText(_translate("MainWindow", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Http Server", None))
        self.menuFie.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.menu_Tools.setTitle(_translate("MainWindow", "&Tools", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionStart_Server.setText(_translate("MainWindow", "Start Server", None))
        self.actionStop_Server.setText(_translate("MainWindow", "Stop Server", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About ", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionStart_Server_2.setText(_translate("MainWindow", "Start Server", None))
        self.actionStart_Server_2.setToolTip(_translate("MainWindow", "start server", None))
        self.actionSetting.setText(_translate("MainWindow", "Setting", None))
        self.actionSetting.setToolTip(_translate("MainWindow", "Setting", None))
        self.actionStop_server.setText(_translate("MainWindow", "stop server", None))
        self.actionHelp_2.setText(_translate("MainWindow", "Help", None))
        self.actionHelp_2.setToolTip(_translate("MainWindow", "Help", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setToolTip(_translate("MainWindow", "Exit", None))
        self.actionContacts.setText(_translate("MainWindow", "contacts", None))
        self.actionContacts.setToolTip(_translate("MainWindow", "contacts", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionContacts_2.setText(_translate("MainWindow", "contacts", None))
        self.lineEdit_7.setText("8000")
        self.lineEdit_6.setText("0.0.0.0")
        self.lineEdit_9.setText("5000")
        self.lineEdit_8.setText("192.168.1.0")
        self.lineEdit_10.setText("--Not Coded Yet--Not Require---")
        self.lineEdit_12.setText("--Not Coded Yet--Not Require---")
        self.textBrowser.setText("Please Wait while server is starting.....!")
        self.le_mail_pass.setEchoMode(QtGui.QLineEdit.Password)

    def save_file(self):
        self.filename = str(QtGui.QFileDialog.getSaveFileName(self.window,str(self.lineEdit_11.text())))
        self.lineEdit_11.setText(self.filename)

    def fileserver_client(self):
        port = int(str(self.lineEdit_9.text()))
        host = str(self.lineEdit_8.text())
        self.progressBar.setProperty("value", 0)
        s = socket.socket()
        s.connect((host, port))
        filename_save = self.filename
        filename=str(self.lineEdit_13.text())
        if filename != 'Please Choose FileName To Save...':
            s.send(filename)
            data = s.recv(1024)
            if data[:6] == 'EXISTS':
                filesize = long(data[6:])
                message = 'Y'
                if message == 'Y':
                    s.send("OK")
                    f = open(filename_save, 'wb')
                    data = s.recv(1024)
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize:
                        data = s.recv(1024)
                        totalRecv += len(data)
                        f.write(data)
                        percent = totalRecv/float(filesize)*100
                        self.progressBar.setProperty("value",percent)

                    self.progressBar.setProperty("value",100)
                    f.close()
                    self.lineEdit_13.setText("Download Completed!")
            else:
               self.lineEdit_13.setText("File Not Exists!")

        s.close()




    def starthttpserver(self):

        PORT = int(str(self.lineEdit_7.text()))
        HOST = str(self.lineEdit_6.text())
        try:
            self.handler = MyHandler
            self.server = SocketServer.TCPServer((HOST,PORT), self.handler)
            os.chdir('html_server')
            self.t = threading.Thread(target=self.server.serve_forever)
            self.t.daemon=True
            self.t.start()
            time.sleep(10)


        except:
            self.textBrowser.setText('Something Wrong Try Again!')

        else:
           self.textBrowser.setText(str('Server Started......! At HOST :'+HOST+" PORT: "+str(PORT))+" In Directory :"+str(os.getcwd()))

    def stophttpserver(self):
        try:
            self.server.socket.close()
            #self.t._block
            
        except:
            print "OOPS! Something Wrong!"
        else:

            self.textBrowser.setText('Server Stoped!.......!')

    def send(self):
        fromaddr = str(self.le_mail_from.text())
        toaddr = str(self.le_mail_to.text())
        subject =str( self.le_mail_sub.text())
        text = str(self.pte_mail_msg.toPlainText())
        username = str(self.le_mail_username.text())
        password = str(self.le_mail_pass.text())
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
        #Modify According to your smtp server,By Default Gmail is Selected
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.ehlo()
            print username
           # print password
            print fromaddr
            print toaddr
            print msg.as_string
            server.login(username, password)
            server.sendmail(fromaddr, toaddr, msg.as_string())

        except Exception:
            message='Connection Failed'+str(sys.exc_info()[0])
            self.pte_mail_msg.setPlainText(message)

        else:
            self.pte_mail_msg.setPlainText("Mail Send Sucessfully!")
        finally:
            server.quit()

    def chat(self):
    	user_name = str(self.textEdit.toPlainText())
    	client = ChatClient(user_name,'127.0.0.1', 5000)
    	client.cmdloop()


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        print (str(self.headers))
        print (str(self.address_string())+": "+str(self.date_time_string()))
        print (str(self.default_request_version))
        print("Path :"+str(self.path))
        print("Command :"+str(self.command))
        print("Address :"+str(self.client_address))
        print("Request : "+str(self.requestline))
        #ui.textBrowser.setPlainText("TESTED")


class ChatClient(object):
    """ A simple command line chat client using select """

    def __init__(self, name, host='0.0.0.0', port=5000):
        self.name = name
        # Quit flag
        self.flag = False
        self.port = int(port)
        self.host = host
        # Initial prompt
        self.prompt='[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print 'Connected to chat server@%d' % self.port
            # Send my name...
            name_chrome=self.name
            send(self.sock,'NAME: ' + self.name) 
            data = receive(self.sock)
            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error, e:
            print 'Could not connect to chat server @%d' % self.port
            sys.exit(1)

    BUFSIZ = 1024

    def cmdloop(self):

        while not self.flag:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()

                # Wait for input from stdin & socket
                inputready, outputready,exceptrdy = select.select([0, self.sock], [],[])
                
                for i in inputready:
                    if i == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif i == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print 'Shutting down.'
                            self.flag = True
                            break
                        else:
                            f=open('p.html','a')
                            sys.stdout.write(data + '\n')
                            f.write('\n'+name_chrome+' ==  '+data+'\n\n')
                            sys.stdout.flush()
                            
            except KeyboardInterrupt:
                print 'Interrupted.'
                f=open('p.html','a')
                f.write('</font></div></body></html>')
                f.close()
                self.sock.close()
                break
            

import LanApp_rc
import sys

if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)

#for chrome extension

name_chrome='new'  
f=open('p.html','w')
f.write('<html><head><title>Reading from text files</title></head><body bgcolor="#E6E6FA"><div><font color="blue">')

# Create and display the splash screen
splash_pix = QPixmap('splashscreen.png')
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()
app.processEvents()

# Simulate something that takes time
time.sleep(4)

mainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
splash.finish(mainWindow)
sys.exit(app.exec_())

