#!/bin/env python

import sys
sys.path.insert(0, "lib")

import os
from PyQt4 import *
from PyQt4 import QtGui
from PyQt4.QtCore import QStringList, pyqtSignature
from PyQt4.QtGui import QPixmap
from progressBar import ProgressBar
import sys
import random
from xml.dom import minidom, Node

# Biblioteca para manipulacao de imagens.
import Image
from filtro import FiltroDeImagem
from fuzzy import Fuzzy


class NewCorrecaoEngine ():
	def __init__ (self, da, de, p, n, listaDeArquivos, rgb, histograma, pb=True):
		self.da = float(da)/float(100) 
		self.de = float(de)/float(100) 
		self.p =  float(p)/float(100)
		self.n =  float(n)/float(100)
		self.listaDeArquivos = listaDeArquivos
		self.lms = not rgb
		self.equalizar = histograma

		if pb:
			self.pb = ProgressBar()

		print "Iniciado correacao... da: " + str(self.da)
		self.resultado = []

		if self.pb:
			self.pb.setTotal(len(listaDeArquivos))
		##

	def start(self, quandoTermina):
		if self.pb:
			self.pb.show()
		i = 0


		while (i<len(self.listaDeArquivos)):
			arquivo = self.listaDeArquivos[i]
			label = str(str(arquivo).split('/')[-1])

			im3 = Image.open(str(arquivo))

			if self.pb:
				self.pb.setLabel('[1/1] Aplicando filtor unico em ' +str(label))
			filtro1 = FiltroDeImagem(debug=False)
			filtro1.carregarImg(str(arquivo))
			filtro1.callBackPogresso(self.percentagem)
			im1 = filtro1.filtrarNovo(self.lms, self.equalizar, self.p, self.de, self.da)


			# Filtro 1 { Protan }
			#self.pb.setLabel('[1/6] Aplicando filtro Protan em ' + str(label))
			#filtro1 = FiltroDeImagem(debug=False)
			#filtro1.carregarImg(str(arquivo))
			#filtro1.callBackPogresso(self.percentagem)
			#im1 = filtro1.filtrarProtan(equalizar = self.equalizar, lms = self.lms)

			# Filtro 2 { Deutan }
			#self.pb.setLabel('[2/6] Aplicando filtro Deutan em ' + str(label))
			#filtro2 = FiltroDeImagem(debug=False)
			#filtro2.carregarImg(str(arquivo))
			#filtro2.callBackPogresso(self.percentagem)
			#im2 = filtro2.filtrarDeutan(equalizar = self.equalizar, lms = self.lms)

			# Fuzzy 1
			#fuz1 = Fuzzy(False,self.p,self.de,self.da,self.n)
			#self.pb.setLabel('[3/6] Aplicando filtro Fuzzy 1 em ' + str(label))
			#fuz1.callBackProgresso(self.percentagem)
			#im1 = fuz1.multiplicaProtan(im1)

			# Fuzzy 2
			#fuz2 = Fuzzy(False,self.p,self.de,self.da,self.n)
			#self.pb.setLabel('[4/6] Aplicando filtro Fuzzy 2 em ' + str(label))
			#fuz1.callBackProgresso(self.percentagem)
			#im2 = fuz1.multiplicaDeutan(im2)


			#self.pb.setLabel('[5/6] Aplicando filtro Fuzzy 3 em ' + str(label))
			#fuz1.callBackProgresso(self.percentagem)
			#im3 = fuz1.multiplicaNormal(im3)

			# Soma da matrizes
			#self.pb.setLabel('[6/6] Aplicando soma de matrizes em ' + str(label))
			#fuz1.callBackProgresso(self.percentagem)
			#im4 = Image.open(str(arquivo))
			#im4 = fuz1.soma(im1, im2, im3, im4)

			im1.save("default_output/" + str(i) + ".bmp", "BMP")

			self.resultado.append((label, str(arquivo), "default_output/" + str(i) + ".bmp"))

			i = i + 1

		return self.resultado

	def percentagem(self, x):
		if self.pb:
			return self.pb.setPercentagem(x)
		else:
			return 0
	

class CorrecaoEngine ():
	def __init__ (self, da, de, p, n, listaDeArquivos, rgb, histograma, pb=True):
		self.da = float(da)/float(100) 
		self.de = float(de)/float(100) 
		self.p =  float(p)/float(100)
		self.n =  float(n)/float(100)
		self.listaDeArquivos = listaDeArquivos
		self.lms = not rgb
		self.equalizar = histograma

		if pb:
			self.pb = ProgressBar()
			self.pb.setTotal(len(listaDeArquivos))
		else:
			self.pb = None

		print "Iniciado correacao... da: " + str(self.da)
		self.resultado = []

		##

	def start(self, quandoTermina):
		if self.pb:
			self.pb.show()
		i = 0
		while (i<len(self.listaDeArquivos)):
			arquivo = self.listaDeArquivos[i]
			label = str(str(arquivo).split('/')[-1])

			im3 = Image.open(str(arquivo))

			# Filtro 1 { Protan }
			if self.pb:
				self.pb.setLabel('[1/6] Aplicando filtro Protan em ' + str(label))
			filtro1 = FiltroDeImagem(debug=False)
			filtro1.carregarImg(str(arquivo))
			filtro1.callBackPogresso(self.percentagem)
			im1 = filtro1.filtrarProtan(equalizar = self.equalizar, lms = self.lms)

			# Filtro 2 { Deutan }
			if self.pb:
				self.pb.setLabel('[2/6] Aplicando filtro Deutan em ' + str(label))
			filtro2 = FiltroDeImagem(debug=False)
			filtro2.carregarImg(str(arquivo))
			filtro2.callBackPogresso(self.percentagem)
			im2 = filtro2.filtrarDeutan(equalizar = self.equalizar, lms = self.lms)

			# Fuzzy 1
			fuz1 = Fuzzy(False,self.p,self.de,self.da,self.n)
			if self.pb:
				self.pb.setLabel('[3/6] Aplicando filtro Fuzzy 1 em ' + str(label))
			fuz1.callBackProgresso(self.percentagem)
			im1 = fuz1.multiplicaProtan(im1)

			# Fuzzy 2
			#fuz2 = Fuzzy(False,self.p,self.de,self.da,self.n)
			if self.pb:
				self.pb.setLabel('[4/6] Aplicando filtro Fuzzy 2 em ' + str(label))
			fuz1.callBackProgresso(self.percentagem)
			im2 = fuz1.multiplicaDeutan(im2)


			if self.pb:
				self.pb.setLabel('[5/6] Aplicando filtro Fuzzy 3 em ' + str(label))
			fuz1.callBackProgresso(self.percentagem)
			im3 = fuz1.multiplicaNormal(im3)

			# Soma da matrizes
			if self.pb:
				self.pb.setLabel('[6/6] Aplicando soma de matrizes em ' + str(label))
			fuz1.callBackProgresso(self.percentagem)
			im4 = Image.open(str(arquivo))
			im4 = fuz1.soma(im1, im2, im3, im4)

			im4.save("default_output/" + str(i) + ".bmp", "BMP")

			self.resultado.append((label, str(arquivo), "default_output/" + str(i) + ".bmp"))

			i = i + 1


		#quandoTermina(self.resultado)
		#self.pb.hide()
		return self.resultado

	def percentagem(self, x):
		if self.pb:
			return self.pb.setPercentagem(x)
		else:
			return 0
		
		


