#!/bin/env python

import random
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QStringList, pyqtSignature
from PyQt4.QtGui import QPixmap
from xml.dom import minidom, Node

sys.path.insert(0, "../lib")
from gui_progress_bar import Ui_ProgressBarGui


class ProgressBar (QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
        	self.ui_ = Ui_ProgressBarGui()
        	self.ui_.setupUi(self)

       		self.connect(self.ui_.pushButton, QtCore.SIGNAL('clicked()'),
				self.sair)
	
	def sair(self):
		quit()

	def setPercentagem(self, x):
		self.ui_.progressBar.setValue(x)
		#self.repaint()

	def setTotal (self, y):
		print y

	def setLabel (self, txt):
		print ">>> " + str(txt)
		self.ui_.status_label.setText(str(txt))
		self.repaint()
		return 1

	def getLabel (self):
		return self.ui_.status_label.text

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)

	ui = ProgressBar()

        ui.ui_.progressBar.setRange(0, 100)
        ui.ui_.progressBar.reset()
	ui.ui_.progressBar.setValue(10)

	ui.setLabel("huhu")

	ui.show()
	sys.exit(app.exec_())
