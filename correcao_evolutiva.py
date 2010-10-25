#!/usr/bin/python

from simulador import Simulate
import getopt
import sys
import Image
import random
from operator import itemgetter, attrgetter

# Biblioteca para manipulacao de matrizes.
import numpy
# Biblioteca para multiplicacao de matrizes.
from numpy.oldnumeric import matrixmultiply

MAX_NUMBER_OF_EVOLUTIONS = 10
NUMBERS_OF_ELEMENTS_DICE = 3


def load_population(pop):
    #from pop import popMatrix
    popMatrix = [[[1.0, 0.0, 0.0],[0.0, 1.0, 0.0],[0.0, 0.0, 1.0]],
            [[0.4, 0.2, 0.4], [0.3, 0.3, 0.4], [0.1, 0.5, 0.4]],
            [[0.1, 0.1, 0.1], [0.1, 0.3, 0.4], [0.3, 0.1, 0.4]],
            [[0.1, 0.1, 0.1], [0.2, 0.3, 0.4], [0.3, 0.2, 0.4]]]
    return popMatrix

def load_colorblinds(colorblind):
    return [[1.0, 0.0], [0.5, 0.0]]

def calculate_gamut(im):
    #print "Gamut: " + str(len(im.getcolors(11024)))
    return len(im.getcolors(1048576))

def op(im, matrix):

    new_im = im.copy()

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            # Transforma de rgb para lms
            rgb = (numpy.matrix(im.getpixel((i,j)))).T
            rgb = matrix * rgb

            # Altera pixel na imagem.
            new_im.putpixel((i, j), (rgb[0], rgb[1], rgb[2]))

    return new_im

def evolute_main(pop, colorblind, image):
    print "Population file: " + pop
    print "Colorblinds files: " + colorblind
    print "Image: " + image

    im = Image.open(str(image))
    popMatrix = load_population(pop)
    colorblindMatrix = load_colorblinds(colorblind)

    values = {}

    for i in colorblindMatrix:
        (individualPerFitness, individualPerMatrix) = startEvolution(im.copy(), popMatrix, i[0], i[1])
        values[str(i)] = individualPerFitness

    #sorted_colorblindMatrix = sorted(colorblindMatrix, key=itemgetter(0))
    for i in colorblindMatrix:
        print "Best for: " + str(i)
        print str(values[str(i)])

def operator(matrix):
    return matrix

def evolute(popMatrix):
    new_popMatrix = []
    for i in popMatrix:
        new_popMatrix.append(i)
        new_popMatrix.append(operator(i))

    return new_popMatrix

def dice(popMatrix):
    res = []
    new_popMatrix = list(popMatrix)

    if NUMBERS_OF_ELEMENTS_DICE > len(popMatrix):
        print "internal error: try with a bigger matrix population"
        sys.exit(0)

    for i in range(NUMBERS_OF_ELEMENTS_DICE):
        pos = int(random.randint(0, len(new_popMatrix)-1))
        print "Pos: " + str(pos) + " - " + str(len(new_popMatrix))
        res.append(new_popMatrix[pos])
        new_popMatrix.remove(new_popMatrix[pos])

    return res

def selection(popMatrix, popPerMatrix, p, d, im):
    size = len(popMatrix)
    score = {}
    strongers = {}

    #print "SELECTION, size: " + str(size)

    for i in range(size):
        score[str(popMatrix[i])] = 0

    opa = 0
    epa = 0

    for i in range(size):
        opa = opa + 1
        if not popPerMatrix.has_key(str(popMatrix[i])):
            img_op = op(im, popMatrix[i])
            img_op = Simulate(img_op, p, d, True).getIm()
            gamu = calculate_gamut(img_op)
            popPerMatrix[str(popMatrix[i])] = [gamu]

        for j in dice(popMatrix):
            epa = epa + 1
            if not popPerMatrix.has_key(str(j)):
                img_op = op(im, j)
                img_op = Simulate(img_op, p, d, True).getIm()
                gamu = calculate_gamut(img_op)
                popPerMatrix[str(j)] = [gamu]

            if int(popPerMatrix[str(j)][0]) < int(popPerMatrix[str(popMatrix[i])][0]):
                score[str(popMatrix[i])] = int(score[str(popMatrix[i])]) + 1
            #else:
            #    score[str(j)] = int(score[str(j)]) + 1

    total = 0
    for i in score:
        total = total + score[str(i)]

    #print "Total: " + str(total)
    #print "Score: " + str(score)
    #print "Epa: " + str(epa) + " Opa: " + str(opa)

    top = sorted(score.iteritems(), key=itemgetter(1), reverse=True)
    new_popMatrix = []
    for i in range(size/2):
        new_popMatrix.append(eval(top[i][0]))

    return new_popMatrix

def startEvolution(im, popMatrix, p, d):
    popPerFitnes = {}
    popPerMatrix = {}
    popMatrix = list(popMatrix)

    cb_c = {}

    tried = 0
    goodResultFound = False

    if popMatrix is None:
        print "Problem with popMatrix"
        sys.exit(-1)
    else:
        print str(popMatrix)

    while goodResultFound or tried < MAX_NUMBER_OF_EVOLUTIONS:
        tried = tried + 1

        for j in popMatrix:
            #s = Simulate(im, p, d, True)
            #print "      Orig Gamut: " + str(calculate_gamut(im))
            #new_im = s.getIm()
            #new_im = im.copy()
            #print " Simulated Gamut: " + str(calculate_gamut(new_im))
            img_op = op(im.copy(), j)
            img_op = Simulate(img_op, p, d, True).getIm()
            gamu = calculate_gamut(img_op)
            print "Opted Sim. Gamut: " + str(gamu)

            if 0:
                im.show()
                new_im.show()
                img_op.show()

            if not popPerFitnes.has_key(gamu):
                    popPerFitnes[gamu] = []
            if not popPerMatrix.has_key(str(j)):
                    popPerMatrix[str(j)] = []

            popPerFitnes[gamu].append(j)
            popPerMatrix[str(j)].append(gamu)

        new_popMatrix = evolute(popMatrix)
        popMatrix = selection(new_popMatrix, popPerMatrix, p, d, im)

    return (popPerFitnes, popPerMatrix)



if __name__ == "__main__":
    optlist, args = getopt.getopt(sys.argv[1:], 'p:c:i:')
    colorblind = None
    population = None
    image = None

    for a in optlist:
        if a[0] ==  '-p':
            population = a[1]
        if a[0] == '-c':
            colorblind = a[1]
        if a[0] == '-i':
            image = a[1]

    print str(optlist)
    if colorblind == None or population == None or image == None:
        print "Invalid usage"
        sys.exit(-1)

    evolute_main(population, colorblind, image)
