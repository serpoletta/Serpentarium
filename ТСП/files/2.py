#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import sys
import functools
from subprocess import Popen, PIPE
from PyQt4 import QtGui,QtCore

# Класс основного окна
class MainWindow(QtGui.QWidget):
	def __init__(self, parent=None):
		# Создание окна
		QtGui.QWidget.__init__(self, parent)
		self.setWindowTitle('Последовательная интерпретация элементов')
		self.move(400, 200)
		
		# Создание layout
		self.vbox = QtGui.QVBoxLayout()
		
		# Создание и добавление в layout заголовка
		self.title = QtGui.QLabel('Перечислите программы:')
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.vbox.addWidget(self.title)
		
		# Создание области ввода
		self.programList = QtGui.QTextEdit('example1.py example2.py example3.py')
		self.vbox.addWidget(self.programList)
		
		# Создание кнопки
		self.button = QtGui.QPushButton('Запуск')
		self.button.clicked.connect(functools.partial(self.buttonClicked))
		
		# Включение в layout
		self.vbox.addWidget(self.button)
		
		# Включение layout в окно
		self.setLayout(self.vbox)
		
	# Функция, вызываемая по клику на кнопку. Nt=2 - заранее задается последовательность выполнения элементов.
	def buttonClicked(self):
		programs = str(self.programList.toPlainText())
		programs = programs.split(' ')
		
		command = '/usr/bin/python3 ./'
		for program in programs:
			p=Popen(command + program, stdout=PIPE, shell=True)

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
