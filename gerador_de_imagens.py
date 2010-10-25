#!/usr/bin/python

import os
import sys
sys.path.insert(0, "lib")
from correcao_engine import CorrecaoEngine, NewCorrecaoEngine

comb = [0, 25, 50, 75, 100]

def main():
	# 10 imagens

	l = os.listdir("imgs_read")

	for method in [1, 2]:

		for i in l:
			print i

			da = 100
			n = 0
			for y in comb:
				corrige(da, 0, y, n, i, method)
				simula(da, 0, y, n)

			for y in comb[1:]:
				corrige(da, y, 0, n, i, method)
				simula(da, y, 0, n)

def corrige(da, de, p, n, f, method):
	print "Corrigindo..."
	print "   daltonismo: " + str(da)
	print "       deutan: " + str(de)
	print "       protan: " + str(p)
	print "   normalismo: " + str(n)
	if method == 2:
		e = NewCorrecaoEngine(da, de, p, n, ['imgs_read/' + f], True, True, False)
	else:
		e = CorrecaoEngine(da, de, p, n, ['imgs_read/' + f], True, True, False)
	
	resultado = e.start(None)


def simula(da, de, p, n):
	print "Simulando..."
	print "   daltonismo: " + str(da)
	print "       deutan: " + str(de)
	print "       protan: " + str(p)
	print "   normalismo: " + str(n)
	
	# original -> corrigir p/ p e d -> simular p/ p e d

	# Simulada: 

	#	-> 0% 0%  (p, d)
	#    25% 0%
  #    50% 0%
	#    75% 0%
  #    100% 0%
	#		 0% 25%
	#		 0% 50%
	#		 0% 75%
	#		 0% 100%

	# 1 metodo: com e sem histograma
	# 2 metodo: com e sem histograma

main()
