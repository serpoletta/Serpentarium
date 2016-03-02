#!/usr/bin/python3

import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
	def __init__(self, parent=None):
		# Создание окна
		QtGui.QWidget.__init__(self, parent)
		self.move(400, 200)
		self.setWindowTitle('STOP')
		
		# Создание кнопки
		quit = QtGui.QPushButton('Выход',self)
		# Явный STOP (Nt=О)
		quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())
