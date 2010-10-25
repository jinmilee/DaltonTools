# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/gui_visualizator_window_simulator_application.ui'
#
# Created: Sat Jun  5 16:32:31 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SimulatorApplicationVisualizatorWindowGui(object):
    def setupUi(self, SimulatorApplicationVisualizatorWindowGui):
        SimulatorApplicationVisualizatorWindowGui.setObjectName("SimulatorApplicationVisualizatorWindowGui")
        SimulatorApplicationVisualizatorWindowGui.resize(771, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Documents and Settings/JLee/Desktop/Icones/xeyes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimulatorApplicationVisualizatorWindowGui.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(SimulatorApplicationVisualizatorWindowGui)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 241, 51))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 19, 131, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tipo = QtGui.QLabel(self.groupBox)
        self.tipo.setGeometry(QtCore.QRect(90, 19, 46, 20))
        self.tipo.setObjectName("tipo")
        self.pushButton = QtGui.QPushButton(SimulatorApplicationVisualizatorWindowGui)
        self.pushButton.setGeometry(QtCore.QRect(680, 560, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtGui.QTableWidget(SimulatorApplicationVisualizatorWindowGui)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 731, 461))
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setIconSize(QtCore.QSize(600, 600))
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_2 = QtGui.QPushButton(SimulatorApplicationVisualizatorWindowGui)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 560, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Documents and Settings/JLee/Desktop/Icones/button-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(SimulatorApplicationVisualizatorWindowGui)
        QtCore.QMetaObject.connectSlotsByName(SimulatorApplicationVisualizatorWindowGui)

    def retranslateUi(self, SimulatorApplicationVisualizatorWindowGui):
        SimulatorApplicationVisualizatorWindowGui.setWindowTitle(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Visualizador de Imagens", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Tipo do Daltonismo", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Daltonismo:", None, QtGui.QApplication.UnicodeUTF8))
        self.tipo.setText(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Fechar", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Imagem Original", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Imagem Simulada", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("SimulatorApplicationVisualizatorWindowGui", "Salvar", None, QtGui.QApplication.UnicodeUTF8))

