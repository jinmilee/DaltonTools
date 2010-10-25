#
#  fuzzy.py
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

import lmsrgb

class Fuzzy:
	""" Implementa tudo relacionado a fuzzy """
	
	debug = False
	x1 = 0
	x2 = 0
	cb = None
	
	def __init__(self, debug=False, protan=0, deutan=0, daltonico=0, normalidade=0):
		self.debug = debug
		
		if debug:
			print "Fuzzy inicializado"
			

		print "::Filtro::      Protan: " + str(protan)
		print "::Filtro::      Deutan: " + str(deutan)
		print "::Filtro::  Daltonismo: " + str(daltonico)
		print "::Filtro:: Normalidade: " + str(normalidade)

		#self.x1 = daltonico<protan?daltonico:protan
		if daltonico<protan:
			self.x1 = daltonico
		else:
			self.x1 = protan

		#self.x2 = daltonico<deutan?daltonico:deutan
		if daltonico<deutan:
			self.x2 = daltonico
		else:
			self.x2 = deutan


		# TODO: Verificar este grau
		if normalidade<(1-daltonico):
			self.x3 = normalidade 
		else:
			self.x3 = 1-daltonico

		print "::Filtro:: -> x1:" + str(self.x1) + " x1:" + str(self.x1) + " x2:" + str(self.x2) + " x3:" + str(self.x3)
		try:
			self.xp = self.x1/(self.x1 + self.x2 + self.x3)
		except:
			self.xp = 1

		try:
			self.xd = self.x2/(self.x1 + self.x2 + self.x3)
		except:
			self.xd = 1

		try:
			self.xn = self.x3/(self.x1 + self.x2 + self.x3)
		except:
			self.xn = 1

		self.cb = None
		
	def callBackProgresso(self, func):
		self.cb = func
		
	def multiplicaProtan(self, img, lms=False):
		""" self.x1 * protan """

		if self.xp == 1:
			return img

		ic = img.getdata()
		banda_r = ic.getband(0)
		banda_g = ic.getband(1)
		banda_b = ic.getband(2)

		for i in range(banda_r.size[0]):
			for j in range(banda_r.size[1]):
				reportar_progresso(i, int((i*100)/banda_r.size[0]), self.debug, self.cb)

				r = banda_r.getpixel((i,j))
				g = banda_g.getpixel((i,j))
				b = banda_b.getpixel((i,j))
				
				if lms:
					x, y, z = rgb2lms(r, g, b)
				else:
					x, y, z = r, g, b
				
				x = x*self.xp
				y = y*self.xp
				z = z*self.xp

				if lms:
					x, y, z = lms2rgb(x, y, z)
	
				banda_r.putpixel((i,j), int(x))
				banda_g.putpixel((i,j), int(y))
				banda_b.putpixel((i,j), int(z))

		ic.putband(banda_r, 0)
		ic.putband(banda_g, 1)
		ic.putband(banda_b, 2)

		img.putdata(ic)
		
		return img

	def multiplicaDeutan(self, img, lms=False):
		""" self.x2 * deutan """


		if self.xd == 1:
			return img


		ic = img.getdata()
		banda_r = ic.getband(0)
		banda_g = ic.getband(1)
		banda_b = ic.getband(2)

		for i in range(banda_r.size[0]):
			for j in range(banda_r.size[1]):
				reportar_progresso(i, int((i*100)/banda_r.size[0]), self.debug, self.cb)

				r = banda_r.getpixel((i,j))
				g = banda_g.getpixel((i,j))
				b = banda_b.getpixel((i,j))
				
				if lms:
					x, y, z = rgb2lms(r, g, b)
				else:
					x, y, z = r, g, b
				
				x = x*self.xd
				y = y*self.xd
				z = z*self.xd
					
				if lms:
					x, y, z = lms2rgb(x, y, z)
	
				banda_r.putpixel((i,j), x)
				banda_g.putpixel((i,j), y)
				banda_b.putpixel((i,j), z)

		ic.putband(banda_r, 0)
		ic.putband(banda_g, 1)
		ic.putband(banda_b, 2)

		img.putdata(ic)
		
		return img

	def multiplicaNormal(self, img, lms=False):
		""" self.x3 * normal """

		if self.xn == 1:
			return img


		ic = img.getdata()
		banda_r = ic.getband(0)
		banda_g = ic.getband(1)
		banda_b = ic.getband(2)

		for i in range(banda_r.size[0]):
			for j in range(banda_r.size[1]):
				reportar_progresso(i, int((i*100)/banda_r.size[0]), self.debug, self.cb)

				r = banda_r.getpixel((i,j))
				g = banda_g.getpixel((i,j))
				b = banda_b.getpixel((i,j))
				
				if lms:
					x, y, z = rgb2lms(r, g, b)
				else:
					x, y, z = r, g, b
				
				x = x*self.xn
				y = y*self.xn
				z = z*self.xn
					
				if lms:
					x, y, z = lms2rgb(x, y, z)
	
				banda_r.putpixel((i,j), x)
				banda_g.putpixel((i,j), y)
				banda_b.putpixel((i,j), z)

		ic.putband(banda_r, 0)
		ic.putband(banda_g, 1)
		ic.putband(banda_b, 2)

		img.putdata(ic)
		
		return img
	
	def soma(self, img1, img2, img3, img4, lms=False):
	
		ic1 = img1.getdata()
		ic2 = img2.getdata()
		ic3 = img3.getdata()
		
		banda_r1 = ic1.getband(0)
		banda_g1 = ic1.getband(1)
		banda_b1 = ic1.getband(2)

		banda_r2 = ic2.getband(0)
		banda_g2 = ic2.getband(1)
		banda_b2 = ic2.getband(2)

		banda_r3 = ic3.getband(0)
		banda_g3 = ic3.getband(1)
		banda_b3 = ic3.getband(2)

		for i in range(banda_r1.size[0]):
			for j in range(banda_r1.size[1]):
				reportar_progresso(i, int((i*100)/banda_r1.size[0]), self.debug, self.cb)

				r1 = banda_r1.getpixel((i,j))
				g1 = banda_g1.getpixel((i,j))
				b1 = banda_b1.getpixel((i,j))
				
				r2 = banda_r2.getpixel((i,j))
				g2 = banda_g2.getpixel((i,j))
				b2 = banda_b2.getpixel((i,j))

				r3 = banda_r3.getpixel((i,j))
				g3 = banda_g3.getpixel((i,j))
				b3 = banda_b3.getpixel((i,j))

				if lms:
					x1, y1, z1 = rgb2lms(r1, g1, b1)
					x2, y2, z2 = rgb2lms(r2, g2, b2)
					x3, y3, z3 = rgb2lms(r3, g3, b3)
				else:
					x1, y1, z1 = r1, g1, b1
					x2, y2, z2 = r2, g2, b2
					x3, y3, z3 = r3, g3, b3

				x = x1 + x2 + x3
				y = y1 + y2 + y3
				z = z1 + z2 + z3
				

				if x > 255:
					print "Opa, passou de 255!"
					x = 255
				if y > 255:
					print "Opa, passou de 255!"
					y = 255
				if z > 255:
					print "Opa, passou de 255!"
					z = 255
					
					
				if lms:
					x, y, z = lms2rgb(x, y, z)
	
				banda_r3.putpixel((i,j), x)
				banda_g3.putpixel((i,j), y)
				banda_b3.putpixel((i,j), z)

		ic3.putband(banda_r3, 0)
		ic3.putband(banda_g3, 1)
		ic3.putband(banda_b3, 2)

		img4.putdata(ic3)
		
		return img4

	
	
def reportar_progresso(i, x, debug, cb):
	if i % 10 == 0:
		if debug:
			print "%3d%%" % x
		if cb != None:
			cb(x)

	
