# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/gui_progress_bar.ui'
#
# Created: Sat Jun  5 16:32:32 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProgressBarGui(object):
    def setupUi(self, ProgressBarGui):
        ProgressBarGui.setObjectName("ProgressBarGui")
        ProgressBarGui.resize(446, 249)
        self.progressBar = QtGui.QProgressBar(ProgressBarGui)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 431, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.status_label = QtGui.QLabel(ProgressBarGui)
        self.status_label.setGeometry(QtCore.QRect(10, 90, 421, 16))
        self.status_label.setObjectName("status_label")
        self.pushButton = QtGui.QPushButton(ProgressBarGui)
        self.pushButton.setGeometry(QtCore.QRect(340, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtGui.QLabel(ProgressBarGui)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 581, 81))
        self.label_3.setPixmap(QtGui.QPixmap("../../../../../python-logo.gif"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ProgressBarGui)
        QtCore.QMetaObject.connectSlotsByName(ProgressBarGui)

    def retranslateUi(self, ProgressBarGui):
        ProgressBarGui.setWindowTitle(QtGui.QApplication.translate("ProgressBarGui", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.status_label.setText(QtGui.QApplication.translate("ProgressBarGui", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ProgressBarGui", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

