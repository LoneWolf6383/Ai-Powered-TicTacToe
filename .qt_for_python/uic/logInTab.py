# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\NAMASIVAAYAM\Documents\Mini Project 3rd Sem\Namas TicTacToe No SQL\python Files\UI files(PYQT5)\logInTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logInTab = QtWidgets.QTabWidget(self.centralwidget)
        self.logInTab.setGeometry(QtCore.QRect(70, 160, 1751, 911))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.logInTab.setFont(font)
        self.logInTab.setTabPosition(QtWidgets.QTabWidget.North)
        self.logInTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.logInTab.setUsesScrollButtons(False)
        self.logInTab.setDocumentMode(True)
        self.logInTab.setTabsClosable(False)
        self.logInTab.setMovable(True)
        self.logInTab.setTabBarAutoHide(False)
        self.logInTab.setObjectName("logInTab")
        self.existingUserTab = QtWidgets.QWidget()
        self.existingUserTab.setObjectName("existingUserTab")
        self.passwdInput = QtWidgets.QLineEdit(self.existingUserTab)
        self.passwdInput.setGeometry(QtCore.QRect(760, 290, 521, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.passwdInput.setFont(font)
        self.passwdInput.setText("")
        self.passwdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdInput.setObjectName("passwdInput")
        self.userIdInput = QtWidgets.QLineEdit(self.existingUserTab)
        self.userIdInput.setGeometry(QtCore.QRect(760, 200, 521, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.userIdInput.setFont(font)
        self.userIdInput.setObjectName("userIdInput")
        self.passwdLabel = QtWidgets.QLabel(self.existingUserTab)
        self.passwdLabel.setGeometry(QtCore.QRect(410, 280, 331, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.passwdLabel.setFont(font)
        self.passwdLabel.setObjectName("passwdLabel")
        self.userIdLabel = QtWidgets.QLabel(self.existingUserTab)
        self.userIdLabel.setGeometry(QtCore.QRect(410, 200, 331, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.userIdLabel.setFont(font)
        self.userIdLabel.setObjectName("userIdLabel")
        self.checkLogInLabel = QtWidgets.QLabel(self.existingUserTab)
        self.checkLogInLabel.setGeometry(QtCore.QRect(760, 370, 861, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.checkLogInLabel.setFont(font)
        self.checkLogInLabel.setText("")
        self.checkLogInLabel.setObjectName("checkLogInLabel")
        self.checkUserIdLabel = QtWidgets.QLabel(self.existingUserTab)
        self.checkUserIdLabel.setGeometry(QtCore.QRect(1310, 200, 421, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.checkUserIdLabel.setFont(font)
        self.checkUserIdLabel.setText("")
        self.checkUserIdLabel.setObjectName("checkUserIdLabel")
        self.checkPasswdLabel = QtWidgets.QLabel(self.existingUserTab)
        self.checkPasswdLabel.setGeometry(QtCore.QRect(1310, 290, 421, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.checkPasswdLabel.setFont(font)
        self.checkPasswdLabel.setText("")
        self.checkPasswdLabel.setObjectName("checkPasswdLabel")
        self.logInButton = QtWidgets.QPushButton(self.existingUserTab)
        self.logInButton.setGeometry(QtCore.QRect(1120, 430, 151, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.logInButton.setFont(font)
        self.logInButton.setObjectName("logInButton")
        self.logInTab.addTab(self.existingUserTab, "")
        self.newUserTab = QtWidgets.QWidget()
        self.newUserTab.setObjectName("newUserTab")
        self.newPasswdInput = QtWidgets.QLineEdit(self.newUserTab)
        self.newPasswdInput.setGeometry(QtCore.QRect(720, 540, 521, 61))
        self.newPasswdInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswdInput.setObjectName("newPasswdInput")
        self.newUserIdInput = QtWidgets.QLineEdit(self.newUserTab)
        self.newUserIdInput.setGeometry(QtCore.QRect(720, 450, 521, 61))
        self.newUserIdInput.setObjectName("newUserIdInput")
        self.newPasswdLabel = QtWidgets.QLabel(self.newUserTab)
        self.newPasswdLabel.setGeometry(QtCore.QRect(370, 530, 331, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.newPasswdLabel.setFont(font)
        self.newPasswdLabel.setObjectName("newPasswdLabel")
        self.newUserIdLabel = QtWidgets.QLabel(self.newUserTab)
        self.newUserIdLabel.setGeometry(QtCore.QRect(370, 450, 331, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.newUserIdLabel.setFont(font)
        self.newUserIdLabel.setObjectName("newUserIdLabel")
        self.rollNoInput = QtWidgets.QLineEdit(self.newUserTab)
        self.rollNoInput.setGeometry(QtCore.QRect(720, 360, 521, 61))
        self.rollNoInput.setObjectName("rollNoInput")
        self.nameInput = QtWidgets.QLineEdit(self.newUserTab)
        self.nameInput.setGeometry(QtCore.QRect(720, 270, 521, 61))
        self.nameInput.setObjectName("nameInput")
        self.nameLabel = QtWidgets.QLabel(self.newUserTab)
        self.nameLabel.setGeometry(QtCore.QRect(370, 270, 331, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.rollNoLabel = QtWidgets.QLabel(self.newUserTab)
        self.rollNoLabel.setGeometry(QtCore.QRect(370, 350, 331, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.rollNoLabel.setFont(font)
        self.rollNoLabel.setObjectName("rollNoLabel")
        self.createAccButton = QtWidgets.QPushButton(self.newUserTab)
        self.createAccButton.setGeometry(QtCore.QRect(1030, 620, 201, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.createAccButton.setFont(font)
        self.createAccButton.setObjectName("createAccButton")
        self.checkCreationLabel = QtWidgets.QLabel(self.newUserTab)
        self.checkCreationLabel.setGeometry(QtCore.QRect(380, 630, 621, 61))
        self.checkCreationLabel.setText("")
        self.checkCreationLabel.setObjectName("checkCreationLabel")
        self.logInTab.addTab(self.newUserTab, "")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(1530, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(1260, 100, 91, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.timeOutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeOutputLabel.setGeometry(QtCore.QRect(1360, 100, 141, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(13)
        self.timeOutputLabel.setFont(font)
        self.timeOutputLabel.setObjectName("timeOutputLabel")
        self.dateOutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateOutputLabel.setGeometry(QtCore.QRect(1630, 100, 191, 51))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.dateOutputLabel.setFont(font)
        self.dateOutputLabel.setObjectName("dateOutputLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.logInTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.passwdLabel.setText(_translate("MainWindow", "Password               :"))
        self.userIdLabel.setText(_translate("MainWindow", "User Id                      :"))
        self.logInButton.setText(_translate("MainWindow", "Log In"))
        self.logInTab.setTabText(self.logInTab.indexOf(self.existingUserTab), _translate("MainWindow", "Existing User"))
        self.newPasswdLabel.setText(_translate("MainWindow", "Password      :"))
        self.newUserIdLabel.setText(_translate("MainWindow", "User Id            :"))
        self.nameLabel.setText(_translate("MainWindow", "Name                 :"))
        self.rollNoLabel.setText(_translate("MainWindow", "Roll No           :"))
        self.createAccButton.setText(_translate("MainWindow", "Create Account"))
        self.logInTab.setTabText(self.logInTab.indexOf(self.newUserTab), _translate("MainWindow", "New User"))
        self.dateLabel.setText(_translate("MainWindow", "DATE:"))
        self.timeLabel.setText(_translate("MainWindow", "TIME:"))
        self.timeOutputLabel.setText(_translate("MainWindow", "TextLabel"))
        self.dateOutputLabel.setText(_translate("MainWindow", "TextLabel"))
