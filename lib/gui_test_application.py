# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/gui_test_application.ui'
#
# Created: Sat Jun  5 16:32:30 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TestApplicationGui(object):
    def setupUi(self, TestApplicationGui):
        TestApplicationGui.setObjectName("TestApplicationGui")
        TestApplicationGui.resize(522, 582)
        TestApplicationGui.setMinimumSize(QtCore.QSize(522, 582))
        TestApplicationGui.setMaximumSize(QtCore.QSize(582, 582))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Documents and Settings/JLee/Desktop/Icones/Escolhidos/Write-Document_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TestApplicationGui.setWindowIcon(icon)
        TestApplicationGui.setAnimated(True)
        self.widget = QtGui.QWidget(TestApplicationGui)
        self.widget.setObjectName("widget")
        self.line1 = QtGui.QFrame(self.widget)
        self.line1.setGeometry(QtCore.QRect(10, 370, 500, 20))
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.quitBnt = QtGui.QPushButton(self.widget)
        self.quitBnt.setGeometry(QtCore.QRect(258, 520, 115, 26))
        self.quitBnt.setObjectName("quitBnt")
        self.nextBnt = QtGui.QPushButton(self.widget)
        self.nextBnt.setGeometry(QtCore.QRect(383, 520, 115, 26))
        self.nextBnt.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextBnt.setAcceptDrops(True)
        self.nextBnt.setCheckable(False)
        self.nextBnt.setDefault(False)
        self.nextBnt.setObjectName("nextBnt")
        self.frame3 = QtGui.QFrame(self.widget)
        self.frame3.setGeometry(QtCore.QRect(0, 57, 521, 311))
        self.frame3.setAutoFillBackground(False)
        self.frame3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame3.setObjectName("frame3")
        self.img = QtGui.QLabel(self.frame3)
        self.img.setGeometry(QtCore.QRect(120, 13, 281, 276))
        self.img.setTextFormat(QtCore.Qt.RichText)
        self.img.setScaledContents(True)
        self.img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.img.setWordWrap(False)
        self.img.setObjectName("img")
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(29, 480, 471, 24))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.textLabel1 = QtGui.QLabel(self.widget)
        self.textLabel1.setGeometry(QtCore.QRect(26, 384, 471, 80))
        self.textLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName("textLabel1")
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(20, 12, 291, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtGui.QFrame.Plain)
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setObjectName("label_11")
        TestApplicationGui.setCentralWidget(self.widget)
        self.MenuBar = QtGui.QMenuBar(TestApplicationGui)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 522, 23))
        self.MenuBar.setObjectName("MenuBar")
        self.fileMenu = QtGui.QMenu(self.MenuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.helpMenu = QtGui.QMenu(self.MenuBar)
        self.helpMenu.setObjectName("helpMenu")
        TestApplicationGui.setMenuBar(self.MenuBar)
        self.fileExitAction = QtGui.QAction(TestApplicationGui)
        self.fileExitAction.setShortcut("")
        self.fileExitAction.setObjectName("fileExitAction")
        self.helpAboutAction = QtGui.QAction(TestApplicationGui)
        self.helpAboutAction.setShortcut("")
        self.helpAboutAction.setObjectName("helpAboutAction")
        self.fileMenu.addAction(self.fileExitAction)
        self.helpMenu.addAction(self.helpAboutAction)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addSeparator()
        self.MenuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(TestApplicationGui)
        QtCore.QObject.connect(self.fileExitAction, QtCore.SIGNAL("activated()"), TestApplicationGui.close)
        QtCore.QObject.connect(self.helpAboutAction, QtCore.SIGNAL("activated()"), TestApplicationGui.setFocus)
        QtCore.QMetaObject.connectSlotsByName(TestApplicationGui)

    def retranslateUi(self, TestApplicationGui):
        TestApplicationGui.setWindowTitle(QtGui.QApplication.translate("TestApplicationGui", "Ferramenta de Teste", None, QtGui.QApplication.UnicodeUTF8))
        self.quitBnt.setText(QtGui.QApplication.translate("TestApplicationGui", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.quitBnt.setShortcut(QtGui.QApplication.translate("TestApplicationGui", "Alt+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.nextBnt.setText(QtGui.QApplication.translate("TestApplicationGui", "&Next", None, QtGui.QApplication.UnicodeUTF8))
        self.nextBnt.setShortcut(QtGui.QApplication.translate("TestApplicationGui", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.frame3.setStyleSheet(QtGui.QApplication.translate("TestApplicationGui", "background-color: #000", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("TestApplicationGui", "n/a", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("TestApplicationGui", "Ferramenta de Teste", None, QtGui.QApplication.UnicodeUTF8))
        self.fileMenu.setTitle(QtGui.QApplication.translate("TestApplicationGui", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.helpMenu.setTitle(QtGui.QApplication.translate("TestApplicationGui", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setText(QtGui.QApplication.translate("TestApplicationGui", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setIconText(QtGui.QApplication.translate("TestApplicationGui", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setProperty("name", QtGui.QApplication.translate("TestApplicationGui", "fileExitAction", None, QtGui.QApplication.UnicodeUTF8))
        self.helpAboutAction.setText(QtGui.QApplication.translate("TestApplicationGui", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.helpAboutAction.setIconText(QtGui.QApplication.translate("TestApplicationGui", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.helpAboutAction.setProperty("name", QtGui.QApplication.translate("TestApplicationGui", "helpAboutAction", None, QtGui.QApplication.UnicodeUTF8))

