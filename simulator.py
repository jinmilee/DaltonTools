# -*- coding: utf-8 -*-

import sys
import random
import os
from xml.dom import minidom, Node
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QStringList, pyqtSignature
from PyQt4.QtGui import QPixmap

sys.path.insert(0, "lib")
from gui_main_window_simulator_application import Ui_SimulatorApplicationMainWindowGui
from gui_visualizator_window_simulator_application import Ui_SimulatorApplicationVisualizatorWindowGui

# Biblioteca para manipulacao de imagens.
import Image
# Biblioteca para manipulacao de matrizes.
import numpy
# Biblioteca para multiplicacao de matrizes.
from numpy.oldnumeric import matrixmultiply


class UI (QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_ = Ui_SimulatorApplicationMainWindowGui()
        self.ui_.setupUi(self)

        self.connect(self.ui_.pushButton_2, QtCore.SIGNAL('clicked()'),
                self.imagemArquivo)
        self.connect(self.ui_.pushButton_4, QtCore.SIGNAL('clicked()'),
                self.sair)
        self.connect(self.ui_.pushButton_3, QtCore.SIGNAL('clicked()'),
                self.simular)

    def imagemArquivo(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                "Selecione o arquivo", "", "Arquivos BMP (*.bmp)")
        print "fileName: " + str(fileName)
        self.ui_.lineEdit_5.setText(fileName);

    def sair(self):
        quit()

    def simular(self):
        file = self.ui_.lineEdit_5.text()
        p = int(self.ui_.protan.text())/100.0
        d = int(self.ui_.deutan.text())/100.0
        print "File: " + file

        # Abre a imagem e transforma num objeto do tipo Image
        im = Image.open(str(file))
        Simulate(im, p, d).show()

class Simulate ():
    def getIm(self):
        return self.im

    def show(self):
        self.im.show();


    def __init__(self, im, p, d, dots=False):
        self.im = im.copy()
        self.dots = dots

        print "d: " + str(d) + " p: " + str(p)

        matrix_cor = [[1-p, 2.02344*p, -2.52581*p], \
                [0.494207*d, 1-d, 1.24827*d],  \
                [0, 0, 1 ]]
        matrix_cor = numpy.matrix(matrix_cor)

        rgb_to_lms = [[ 17.8824, 43.5161, 4.11935 ], \
                [ 3.45565, 27.1554, 3.86714 ],  \
                [ 0.0299566, 0.184309, 1.46709 ]]
        rgb_to_lms = numpy.matrix(rgb_to_lms)
        rgb_to_lms_i = rgb_to_lms.I

        for i in range(self.im.size[0]):
            if i % 10 == 0:
                if self.dots:
                    print ".",
                else:
                    print "%3d%%" % int((i*100)/self.im.size[0])

            for j in range(self.im.size[1]):

                # Transforma de rgb para lms
                rgb = (numpy.matrix(self.im.getpixel((i,j)))).T
                lms = rgb_to_lms * rgb
                lms = matrix_cor * lms

                # Transformacao novamente para RGB
                rgb = rgb_to_lms_i * lms

                # Altera pixel na imagem.
                self.im.putpixel((i, j), (rgb[0], rgb[1], rgb[2]))

        print " "

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
