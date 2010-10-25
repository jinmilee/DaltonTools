#!/bin/env python

import os
import sys
import random

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QStringList, pyqtSignature
from PyQt4.QtGui import QPixmap
from xml.dom import minidom, Node

sys.path.insert(0, "lib")
from correcao_engine import CorrecaoEngine, NewCorrecaoEngine

from gui_correct_application_main_window import Ui_CorrectApplicationGui
from gui_visualizator_window_correct_application import Ui_CorrectApplicationVisualizatorWindow


class UI (QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
        	self.ui_ = Ui_CorrectApplicationGui()
        	self.ui_.setupUi(self)

		self.connect(self.ui_.pushButton, QtCore.SIGNAL('clicked()'),
				self.lerDadosDoArquivo)
		self.connect(self.ui_.pushButton_2, QtCore.SIGNAL('clicked()'),
				self.selecionarImagens)
		self.connect(self.ui_.pushButton_4, QtCore.SIGNAL('clicked()'),
				self.sair)	
		self.connect(self.ui_.pushButton_3, QtCore.SIGNAL('clicked()'),
				self.corrigir)

		self.connect(self.ui_.metodo, QtCore.SIGNAL('currentIndexChanged(const QString)'),
				self.metodoChanged)

		#self.connect(self.ui_.quitBnt, QtCore.SIGNAL('clicked()'), self.fileExit)

		self.listaDeArquivos = None

	def metodoChanged(self, value):
		if value == "Metodo 2":
			print "Desabilitando"
			self.ui_.lineEdit_2.setReadOnly(True)
			self.ui_.lineEdit_2.setDisabled(True)
			self.ui_.lineEdit_2.setText("100")
			self.ui_.lineEdit_6.setReadOnly(True)
			self.ui_.lineEdit_6.setDisabled(True)
			self.ui_.lineEdit_6.setText("0")
			self.ui_.groupBox_2.setDisabled(True)
			#self.ui_.groupBox_3.setDisabled(True)
			self.ui_.radioButton_3.setChecked(True)
			#self.ui_.radioButton_5.setChecked(True)
		else:
			self.ui_.lineEdit_2.setReadOnly(False)
			self.ui_.lineEdit_2.setDisabled(False)
			self.ui_.lineEdit_2.setText("100")
			self.ui_.lineEdit_6.setReadOnly(False)
			self.ui_.lineEdit_6.setDisabled(False)
			self.ui_.lineEdit_6.setText("0")
			self.ui_.groupBox_2.setDisabled(False)
			#self.ui_.groupBox_3.setDisabled(False)

			print "Habilitando"

	def lerDadosDoArquivo(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self, "Selecione o arquivo", "", "Arquivos XML (*.xml)")
		print "fileName: " + str(fileName)
		if fileName != None:
			print str(fileName)
			mdom = minidom.parse(str(fileName))

			node = mdom.documentElement

			for child in node.childNodes:
				if node.nodeType == Node.ELEMENT_NODE and child.nodeName == "variaveis":
					da, de, p, n = None, None, None, None
					print 'Element name: %s' % child.nodeName
					for (name, value) in child.attributes.items():
						print 'Element name: %s %s' % (name, value)
						if name == 'daltonismo':
							da = value
						if name == 'deutan':
							de = value
						if name == 'protan':
							p = value
						if name == 'normalismo':
							n = value

					self.ui_.lineEdit_2.setText(da)
					self.ui_.lineEdit_3.setText(p)
					self.ui_.lineEdit_4.setText(de)
					self.ui_.lineEdit_6.setText(n)


	def selecionarImagens(self):
		fileNames = QtGui.QFileDialog.getOpenFileNames(self, "Selecione as imagens", "", 
					"Arquivos de Imagem (*.bmp *.gif *.jpg *.jpeg *.tiff *.png);;Todos os arquivos (*)"
					)
		self.path = str(fileNames[0])
		i = 1
		while (i<len(fileNames)):
			self.path = self.path + "; " + str(fileNames[i])
			i = i + 1

		self.ui_.lineEdit_5.setText(self.path)
		
		self.listaDeArquivos = fileNames

	def sair(self):
		quit()

	def corrigir(self):
		if self.listaDeArquivos == None:
			print "Todos os campos devem ser preenchidos"
			self.sair()

		self.da = int(self.ui_.lineEdit_2.text())
		self.p = int(self.ui_.lineEdit_3.text())
		self.de = int(self.ui_.lineEdit_4.text())
		self.n = int(self.ui_.lineEdit_6.text())

		self.rgb = self.ui_.radioButton_3.isChecked()
		self.histograma = self.ui_.radioButton_5.isChecked()

		print "Corrigindo..."
		print "Usar Modelo de cor RGB? " + str(self.rgb)
		print "Fazer equalizacao do histograma? " + str(self.histograma)
		print "Utlizando imagens (Total: " + str(len(self.listaDeArquivos)) + "): " + self.path
		print "Utilizando parametros: "
		print "   daltonismo: " + str(self.da)
		print "       deutan: " + str(self.de)
		print "       protan: " + str(self.p)
		print "   normalismo: " + str(self.n)
		print "Comecando..." 

		if str(self.ui_.metodo.currentText()) == "Metodo 2":
			e = NewCorrecaoEngine(self.da, self.de, self.p, self.n, self.listaDeArquivos, self.rgb, self.histograma)
		else:
			e = CorrecaoEngine(self.da, self.de, self.p, self.n, self.listaDeArquivos, self.rgb, self.histograma)

		self.resultado = e.start(None)
		self.correcaoTerminada(self.resultado)





	def correcaoTerminada(self, resultado):
		self.res = Resposta()
		self.res.show()
		self.res.ui_.da.setText(str(self.da))
		self.res.ui_.de.setText(str(self.de))
		self.res.ui_.p.setText(str(self.p))
		self.res.ui_.n.setText(str(self.n))
		self.res.ui_.n.setText(str(self.n))
		self.res.imagens = resultado

		if self.rgb == True:
			padrao = "RGB"
		else:
			padrao = "LMS"

		if self.histograma == True:
			hist = "Sim"
		else:
			hist = "Nao"

		self.res.ui_.rgb.setText(str(padrao))
		self.res.ui_.histograma.setText(str(hist))
		
		self.res.ui_.tableWidget.setRowCount(len(resultado));
		self.res.ui_.tableWidget.setColumnCount(2);

		j = 0
		while j < len(resultado):
			a1 = QtGui.QTableWidgetItem()
			a2 = QtGui.QTableWidgetItem()


			x1 = QtGui.QPixmap(str(resultado[j][1]))
			x2 = QtGui.QPixmap(str(resultado[j][2]))
			i1 = QtGui.QIcon(x1)
			i2 = QtGui.QIcon(x2)

			a1.setIcon(i1)
			a2.setIcon(i2)
	
			print "res 1: " + str(resultado[j][1])
			print "res 2: " + str(resultado[j][2])

			self.res.ui_.tableWidget.setItem(j, 0, a1)
			self.res.ui_.tableWidget.setItem(j, 1, a2)

			j = j + 1

		self.res.ui_.tableWidget.show()
		self.res.ui_.tableWidget.resizeColumnsToContents()
		self.res.ui_.tableWidget.resizeRowsToContents()
		self.res.ui_.tableWidget.show()



		print "Janela? " + str(self.resultado)


class Resposta (QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
        	self.ui_ = Ui_CorrectApplicationVisualizatorWindow()
        	self.ui_.setupUi(self)

       		self.connect(self.ui_.pushButton, QtCore.SIGNAL('clicked()'),
				self.sair)

		self.connect(self.ui_.pushButton_2, QtCore.SIGNAL('clicked()'),
				self.salvarTudo)

		self.imagens = None

	
	def sair(self):
		self.close()


	def salvarTudo(self):

		if self.imagens == None:
			return

			
		dirName = QtGui.QFileDialog.getExistingDirectory()
		print dirName

		j = 0
		while j < len(self.imagens):
			orig = self.imagens[j][2]
			arquivo = self.imagens[j][2].split("/")[-1]
			arquivo = dirName + "/" + arquivo
			
			print "Orig: " + str(orig)
			print "Arqu: " + str(arquivo)

			orig = str(orig)
			arquivo = str(arquivo)

			#orig = orig.replace("/","\\")
			#arquivo = arquivo.replace("/","\\")

			orig = orig.replace("\\","\\\\")
			arquivo = arquivo.replace("\\","\\\\")


			#os.system("xcopy /K /X /I " + str(orig) + " \"" + str(arquivo) + "\"")
			#os.system("copy " + str(orig) + " \"" + str(arquivo) + "\"")
			#os.system ("copy %s %s" % (str(orig), str(arquivo)))
			#os.system ("cp %s %s" % (str(orig), str(arquivo)))
			os.system ("cp %s %s" % (str(orig), str(arquivo)))
			print "Coisa 1: " + str(orig)
			print "Coisa 2: " + str(arquivo)

			
			j = j + 1

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)

	ui = UI()


	ui.show()
	sys.exit(app.exec_())
