#
#  filtro.py
#  
#
#  Created by Jinmi Lee on 5/7/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

# Biblioteca para manipulacao de imagens.
import Image
# Biblioteca para manipulacao de matrizes.
import numpy
# Biblioteca para multiplicacao de matrizes.
from numpy.oldnumeric import matrixmultiply

# equalize
import ImageOps
import operator

class FiltroDeImagem:
	"Esta classe e responsavel por fazer filtros em imagem"
	
	debug = False
	x = 0
	cb = None
	 
	def __init__(self, debug=False):

		self.debug = debug

		if debug:
			print "FiltroDeImagem inicializada"
			
		self.x = 0
		self.cb = None
		
	def __equalize(self, h):
		"""
		De: http://effbot.org/zone/pil-histogram-equalization.htm
		"""

		lut = []

		for b in range(0, len(h), 256):

			# step size
			step = reduce(operator.add, h[b:b+256]) / 255

			# create equalization lookup table
			n = 0
			for i in range(256):
				lut.append(n / step)
				n = n + h[i+b]

		return lut

	def callBackPogresso(self, func):
		self.cb = func
		
	def carregarImg(self, path):
		self.img = Image.open(path)
	
	def mostrar(self):
		self.img.show()
		
	def filtrarProtan(self, lms=False, equalizar=False):
		"""
		img -> Image.open object
		"""

		ic = self.img.getdata()
		banda_r = ic.getband(0)
		banda_g = ic.getband(1)
		banda_b = ic.getband(2)

		for i in range(banda_r.size[0]):
			for j in range(banda_r.size[1]):
				if i % 10 == 0:
					self.x = int((i*100)/banda_r.size[0])
					if self.debug:
						print "%3d%%" % self.x
					#if self.cb != None:
						#while self.cb(self.x) != 1:
						#	print "Erro interno!"
	
				r = banda_r.getpixel((i,j))
				g = banda_g.getpixel((i,j))
				b = banda_b.getpixel((i,j))
				
				if lms:
					l = 17.8824*r + 43.5161*g + 4.11935*b
					m = 3.45565*r + 27.1554*g + 3.86714*b
					s = 0.0299566*r + 0.184309*g + 1.46709*b
					r = l
					g = m
					b = s
				
				r_ = r
				g_ = (r+g)/2
				b_ = (r+b)/2
					
				if lms:
					r__ = 0.080944*r_ - 0.130504*g_ + 0.116721*b_
					g__ = -0.0102485*r_ + 0.0540194*g_ - 0.113615*b_
					b__ = -0.000365294*r_ -0.00412163*g_ + 0.693513*b_
				else:
					g__ = g_
					b__ = b_
					r__ = r_

				banda_g.putpixel((i,j), g__)
				banda_b.putpixel((i,j), b__)

		if equalizar:
			lut = self.__equalize(banda_g.histogram())
			banda_g = banda_g.point(lut, None)

			lut = self.__equalize(banda_b.histogram())
			banda_b = banda_b.point(lut, None)

		ic.putband(banda_r, 0)
		ic.putband(banda_g, 1)
		ic.putband(banda_b, 2)

		self.img.putdata(ic)
		
		return self.img


	
	def filtrarDeutan(self, lms=False, equalizar=False):
		"""
		img -> Image.open object
		"""
		
		
		ic = self.img.getdata()
		banda_r = ic.getband(0)
		banda_g = ic.getband(1)
		banda_b = ic.getband(2)

		for i in range(banda_r.size[0]):
			for j in range(banda_r.size[1]):
				if i % 10 == 0:
					self.x = int((i*100)/banda_r.size[0])
					if self.debug:
						print "%3d%%" % self.x
					#if self.cb != None:
					#	while self.cb(self.x) != 1:
					#		print "Erro interno!"

				r = banda_r.getpixel((i,j))
				g = banda_g.getpixel((i,j))
				b = banda_b.getpixel((i,j))
				
				if lms:
					l = 17.8824*r + 43.5161*g + 4.11935*b
					m = 3.45565*r + 27.1554*g + 3.86714*b
					s = 0.0299566*r + 0.184309*g + 1.46709*b
					r = l
					g = m
					b = s
				
				r_ = (r+g)/2
				g_ = g
				b_ = (g+b)/2
			
				if lms:
					r__ = 0.080944*r_ - 0.130504*g_ + 0.116721*b_
					g__ = -0.0102485*r_ + 0.0540194*g_ - 0.113615*b_
					b__ = -0.000365294*r_ -0.00412163*g_ + 0.693513*b_
				else:
					g__ = g_
					b__ = b_
					r__ = r_

				banda_g.putpixel((i,j), g__)
				banda_b.putpixel((i,j), b__)

		if equalizar:
			lut = self.__equalize(banda_g.histogram())
			banda_g = banda_g.point(lut, None)

			lut = self.__equalize(banda_b.histogram())
			banda_b = banda_b.point(lut, None)

		ic.putband(banda_r, 0)
		ic.putband(banda_g, 1)
		ic.putband(banda_b, 2)

		self.img.putdata(ic)
		
		return self.img



	def filtrarNovo(self, lms, equalizar, p, de, d):
		"""
		img -> Image.open object
		"""
		self.p = p
		self.de = de
		self.d = d		

		ic = self.img.getdata()
		banda_r = ic.getband(0)
		banda_g = ic.getband(1)
		banda_b = ic.getband(2)

		for i in range(banda_r.size[0]):
			for j in range(banda_r.size[1]):
				if i % 10 == 0:
					self.x = int((i*100)/banda_r.size[0])
					if self.debug:
						print "%3d%%" % self.x
					#if self.cb != None:
					#	while self.cb(self.x) != 1:
					#		print "Erro interno!"

				r = banda_r.getpixel((i,j))
				g = banda_g.getpixel((i,j))
				b = banda_b.getpixel((i,j))
				
				r_ = ((2-self.de)/2)*r + (self.de/2)*g
				g_ = (self.p/2)*r + ((2-self.p)/2)*g
				b_ = ((self.p/4)*r) + (self.de/4)*g + ((4 - self.p - self.de)/4)*b
			
				banda_r.putpixel((i,j), r_)
				banda_g.putpixel((i,j), g_)
				banda_b.putpixel((i,j), b_)

		if equalizar:
			lut = self.__equalize(banda_r.histogram())
			banda_r = banda_r.point(lut, None)

			lut = self.__equalize(banda_g.histogram())
			banda_g = banda_g.point(lut, None)

			lut = self.__equalize(banda_b.histogram())
			banda_b = banda_b.point(lut, None)

		ic.putband(banda_r, 0)
		ic.putband(banda_g, 1)
		ic.putband(banda_b, 2)

		self.img.putdata(ic)
		
		return self.img

