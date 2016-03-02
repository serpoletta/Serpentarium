#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.move(550, 200)
		self.setWindowTitle('Пример 3')
		
		vbox = QtGui.QVBoxLayout()
		
		ginfo = QtGui.QLabel()
		ginfo.setPixmap(QtGui.QPixmap('cd ./files ./Example.jpg'))
		
		quit = QtGui.QPushButton('Закрыть', self)
		self.connect(quit, QtCore.SIGNAL('clicked()'),
			QtGui.qApp, QtCore.SLOT('quit()'))
		
		vbox.addWidget(ginfo)
		vbox.addWidget(quit)
		
		self.setLayout(vbox)

app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())
