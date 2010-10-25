#!/bin/env python

import sys
import random
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QStringList, pyqtSignature
from PyQt4.QtGui import QPixmap
from xml.dom import minidom, Node

sys.path.insert(0, "lib")
from gui_test_application import Ui_TestApplicationGui

ARQUIVO_DE_TESTES = "res/tests.xml"
IMAGES_DIR = "res/test_application_images"

class userAnswers ():
        deutan = 0
        protan = 0
        colorblind = 0
        mono = 0
	normal = 0

        t_deutan = 0
        t_protan = 0
        t_colorblind = 0
        t_mono = 0
	t_normal = 0

        total_tests = 0

        def print_(self):
                print "Colorblind  %s" % self.colorblind
                print "Deutan %s" % self.deutan
                print "Protan %s" % self.protan
                print "Mono %s" % self.mono
		print "Normal %s" % self.normal

                print "Total Colorblind  %s" % self.t_colorblind
                print "Total Deutan %s" % self.t_deutan
                print "Total Protan %s" % self.t_protan
                print "Total Mono %s" % self.t_mono
		print "Total Normal %s" % self.t_normal

                print "Test total: %s" %  self.total_tests
	
	def askToSave(self):
		fileName = QtGui.QFileDialog.getSaveFileName(None, "Salvar como...",".xml", "Arquivo XML (*.xml)")

		if fileName != None:
			fileHandle = open ( fileName, 'w' )
			fileHandle.write ( '<?xml version="1.0" encoding="UTF-8"?>\n' )
			fileHandle.write ( '<teste>\n' )
			fileHandle.write ( '        <variaveis daltonismo="' + str(100*self.colorblind/self.t_colorblind) + '" protan="' + str(100*self.protan/self.t_protan) + '" deutan="' + str(100*self.deutan/self.t_deutan) + '" normalismo="' + str(100*self.normal/self.t_normal) + '"/>\n' )
			fileHandle.write ( '</teste>\n\n' )
			fileHandle.close() 


	def text(self): 
                return self.unify ("<font color='white' size='+2'>" +
                "Resultados: <BR>" + 
                " &nbsp; &nbsp;  Colorblind: " + str(100*self.colorblind/self.t_colorblind) + "% <BR>" + 
                " &nbsp; &nbsp;  Deutan: " + str(100*self.deutan/self.t_deutan) + "% <BR>" + 
                " &nbsp; &nbsp;  Protan: " + str(100*self.protan/self.t_protan) + "% <BR>" + 
                " &nbsp; &nbsp;  Mono: " + str(100*self.mono/self.t_mono) + "% <BR>" + 
                " &nbsp; &nbsp;  Normal: " + str(100*self.normal/self.t_normal) + "% <BR>" + 
                "</font>")
		
	def unify (self, a):
		return a
		
		

class type ():

        answers = None

        def __init__(self, ua):
                self.answers = {}
                self.ua = ua

        def addComplexAnswer(self, kind, weight, response, main_weight):
                a = {}
                a['kind'] = kind
                a['weight'] = weight
                a['main_weight'] = main_weight

                self.answers[response] = a
                print '\t\t\t Expected answer: %s/%s (with #%s/colorblind: %s)' % (a['kind'], response, a['weight'], a['main_weight'])


        def addAnswer(self, kind, response, weight):
                a = {}
                a['kind'] = kind
                a['weight'] = weight

                self.answers[response] = a
                print '\t\t\t Expected answer: %s/%s (with #%s)' % (a['kind'], response, a['weight'])
 
        def verifyAnswer(self, response):

		d = 0
		p = 0
		c = 0
		n = 0
		m = 0
		
                for (name, a) in self.answers.items():
			#print name
                        if a['kind'] == 'deutan':
				if d < int(a['weight']):
					ua.t_deutan = int(ua.t_deutan) + int(a['weight']) - int(d)
					d = int(a['weight'])
                        elif a['kind'] == 'protan':
				if p < int(a['weight']):
					ua.t_protan = ua.t_protan + int(a['weight']) - p
					p = int(a['weight'])
                        elif a['kind'] == 'colorblind':
				if c < int(a['weight']):
                                	ua.t_colorblind = ua.t_colorblind + int(a['weight']) - c
					c = int(a['weight'])
			elif a['kind'] == 'normal':
				if n < int(a['weight']):
                                	ua.t_normal = ua.t_normal + int(a['weight']) - n
					n = int(a['weight'])
                        elif a['kind'] == 'mono':
				if m < int(a['weight']):
					ua.t_mono = ua.t_mono + int(a['weight']) - m
					m = int(a['weight'])


                if self.answers.has_key(str(response)):
                        a = self.answers[str(response)]
		
                        if a['kind'] == 'deutan':
                                ua.deutan = ua.deutan + int(a['weight'])
                        elif a['kind'] == 'protan':
                                ua.protan = ua.protan + int(a['weight'])
                        elif a['kind'] == 'colorblind':
                                ua.colorblind = ua.colorblind + int(a['weight'])
			elif a['kind'] == 'normal':
                                ua.normal = ua.normal + int(a['weight'])
			elif a['kind'] == 'mono':
				ua.mono = ua.mono + int(a['weight'])
				
                        print "Its a valid answer: %s" % self.answers[str(response)]

                        if a.has_key('main_weight'):
                                ua.colorblind = ua.colorblind + int(a['main_weight'])

                else:
			#ua.mono = ua.mono + 1
                        print "Sorry but, Answer not found or not an colorblind kind :(\nValid answers are: "
                        for (name, value) in self.answers.items():
                                print "Value: %s  Data: %s" % (name, value)



class test ():

        name = None
        type = None
        question = None
        uri = None
        preservePosition = False

        def __init__(self, ua):
                self.type = type(ua)
                self.preservePosition = False
                
        def setQuestion(self, question):
                self.question = question

        def getQuestion(self):
                return self.question
        
        def setImage(self, uri):
                self.uri = uri

        def getImage(self):
                return self.uri

        def verifyAnswer(self, answer):
                return self.type.verifyAnswer(answer)

        def setPreservePosition(self, bool):
                self.preservePosition = bool

        def getPreservePosition(self):
                return self.preservePosition


class tests ():
        def __init__(self, ua):
                # Parser xml file
                self.doc = minidom.parse(ARQUIVO_DE_TESTES)
                # Init the tests array
                self.tests = []
                # Init the actual test
                self.actual = 0
                # User answer
                self.ua = ua
                # Tests Order
                self.order = []

                # Insert tests.
                node = self.doc.documentElement
                for child in node.childNodes:
                        self.insert(child)

                self.select_order()


        def select_order(self):
                print "Teste: " + str(len(self.tests))
                total = 0                
                pos = 0


                for i in range(0, len(self.tests)):
                        self.order.insert(len(self.order), -1)


                for i in self.tests:
                        print "Hein?"
                        if i.getPreservePosition() == True:
                                print "Han?"
                                self.order[pos] = i
                                pos = pos + 1
                        else:
                                total = total + 1

                for i in self.tests:
                        if i.getPreservePosition() == False:
                                #rand_pos = 0
                                rand_pos = random.randrange(0, total, 2)
                                while self.order[rand_pos] != -1:
                                        rand_pos = rand_pos + 1
                                        if rand_pos >= len(self.tests):
                                                rand_pos = 0
                                        print "bonga! rand_pos: " + str(rand_pos)

                                self.order[rand_pos] = i

                print "+++>>> "  + str(self.order)

                self.tests = self.order


        def insert (self, node):
                if node.nodeType == Node.ELEMENT_NODE:
                        print 'Element name: %s' % node.nodeName
                        t = test(self.ua)
                        self.tests.insert(len(self.tests), t)
                        # List attributes.
                        for (name, value) in node.attributes.items():
                                #print '\tAttr -- Name: %s  Value: %s' % (name, unicode(value))

                                if name == 'image':
                                        t.setImage(value)
                                if name == 'question':
                                        t.setQuestion(value)
                                if name == 'preservePosition':
                                        t.setPreservePosition(bool(value))
                                        print "asdfasdfasdfas: "  + str(t.getPreservePosition())

                        for child in node.childNodes:
                                if child.nodeType == Node.ELEMENT_NODE:
                                        print '\tSub element name: %s' % child.nodeName
                                        main_weight_ = None
                                        main_response_ = None
                                        main_kind_ = child.nodeName
                                        for (name, value) in child.attributes.items():
                                                if name == 'weigth':
                                                        main_weight_ = value
                                                if name == 'answer':
                                                        main_response_ = value

                                                print '\t\tAttr -- Name: %s  Value: %s' % (name, value)
                                        for kind in child.childNodes:
                                                # protans/deutans saves weigth and correct values.
                                                kind_ = None
                                                weight_ = None
                                                response_ = None

                                                if kind.nodeType == Node.ELEMENT_NODE:
                                                        print '\t\tSub  Sub element name: %s' % kind.nodeName
                                                        kind_ =  kind.nodeName
                                                        for (name, value) in kind.attributes.items():
                                                                if name == 'weigth':
                                                                        weight_ = value
                                                                if name == 'answer':
                                                                        response_ = value         
                                                                print '\t\t\tAttr -- Name: %s  Value: %s' % (name, value)

                                                        t.type.addComplexAnswer(kind_, weight_, response_, main_weight_)
                                        if main_weight_ != None and main_response_ != None and main_kind_ != None:
                                                t.type.addAnswer(main_kind_, main_response_, main_weight_)

        def getImage (self):
                return self.testes[self.actual].getImage()

        def getNext (self):
                self.actual = self.actual + 1
                return self.tests[self.actual]

        def getActual (self):
                return self.tests[self.actual]

        def getPos (self):
                return self.actual

        def getLen (self):
                return len(self.tests)

class ui (QtGui.QMainWindow):
        def __init__(self, parent=None):

        	QtGui.QWidget.__init__(self, parent)
        	self.ui_ = Ui_TestApplicationGui()
        	self.ui_.setupUi(self)

		self.t = t
                self.ua = ua

                print "actual: " + str(t.getActual()) + " // " + str(t.order)
                self.drawImage(t.getActual().getImage());
                self.setPergunta(self.t.getActual().getQuestion())

		self.connect(self.ui_.nextBnt, QtCore.SIGNAL('clicked()'),
				self.next)
                self.connect(self.ui_.quitBnt, QtCore.SIGNAL('clicked()'), self.fileExit)

#        def __init__(self, t, ua, parent=None, name=None, fl=0):
                #Ui_Projeto_Piloto.__init__(self, parent, name, fl)
                #self.setupUi(self)
                #self.t = t
                #self.ua = ua

                #print "actual: " + str(t.getActual()) + " // " + str(t.order)
                #self.drawImage(t.getActual().getImage());
                #self.setPergunta(self.t.getActual().getQuestion())

                #self.connect(self.nextBnt, SIGNAL('clicked()'), self.next)
                #self.connect(self.quitBnt, SIGNAL('clicked()'), self.fileExit)

        def fileExit(self):
                quit()

        def drawImage (self, uri):
                uri = IMAGES_DIR + "/" + str(uri)
                image = QPixmap()
                image.load(uri)
                self.ui_.img.setPixmap(image)

                print uri

        def finaliza (self):
#                self.ui_.img.setText(self.ua.text())
                self.ui_.img.setText(""
				+ "<font size=\"+4\">Obrigado!</font><BR><BR>"
				+ self.ua.text()
				+ "<BR><BR> Voce deseja salvar o teste?"
				)

		self.disconnect(self.ui_.nextBnt, QtCore.SIGNAL('clicked()'),
				self.next)
		self.connect(self.ui_.nextBnt, QtCore.SIGNAL('clicked()'),
				self.ua.askToSave)

		self.ui_.nextBnt.setText("Salvar teste")
		#self.ui_.nextBnt.setDisabled(False)


		
                print self.ua.print_()

        def setPergunta (self, question):
                self.ui_.textLabel1.setText(question)

        def next (self):
                self.ua.total_tests = self.ua.total_tests + 1

                # Validade de answer
                self.t.getActual().verifyAnswer(
                        self.ui_.lineEdit.text()
                )

                # Setup the next test if applicapable, if not
                # just show the results

                if self.ui_.nextBnt.text() == 'Fi&nalizar':
                        self.finaliza()
                        #self.ui_.nextBnt.setDisabled(True)
                        self.ui_.lineEdit.hide()
                        self.ui_.textLabel1.hide()
                
                        self.ui_.line1.hide()
                        return

                self.t.getNext()

                self.drawImage(self.t.getActual().getImage())
                self.setPergunta(self.t.getActual().getQuestion())


                # Debug and clean up the interface.
                print " > Pos: " + str(self.t.getPos())
                print " > Len: " + str(self.t.getLen()-1)

                if self.t.getPos() == self.t.getLen()-1:
                        self.ui_.nextBnt.setText("Fi&nalizar")

                print "Text: " + str(self.ui_.lineEdit.text())
                self.ui_.lineEdit.setText("")


                

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)

        # User answers
        ua = userAnswers()

        # Load xml into computer memory.
        t = tests(ua)
        
        # Show up interface.
	f = ui()

	f.t = t 
	t.ua = ua
        # Start application.
        #app.setMainWidget(f)
        #app.exec_loop()
	f.show()
	sys.exit(app.exec_())





