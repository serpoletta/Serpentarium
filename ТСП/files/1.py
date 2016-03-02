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
		self.setWindowTitle('k->k+1')
		self.move(400, 200)
		
		# Создание layout
		self.vbox = QtGui.QVBoxLayout()
		
		# Создание и добавление в layout заголовка
		self.title = QtGui.QLabel('Выберите количество запусков:')
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.vbox.addWidget(self.title)
		
		# Создание области ввода
		self.nEdit = QtGui.QLineEdit('3')
		self.nEdit.setValidator(QtGui.QIntValidator(1, 20))
		self.vbox.addWidget(self.nEdit)
		
		# Создание кнопки
		self.button = QtGui.QPushButton('Запуск')
		self.button.clicked.connect(functools.partial(self.buttonClicked))
		
		# Включение в layout
		self.vbox.addWidget(self.button)
		
		# Включение layout в окно
		self.setLayout(self.vbox)
		
	# Функция, вызываемая по клику на кнопку. Nt=1 - переход к следующему элементу 
	# осуществляется после выполнения предыдущего заданное пользователем количество раз.
	def buttonClicked(self):
		n = int(self.nEdit.text())
		command = '/usr/bin/python3 ./example1.py'
		for i in range(0,n):
			p=Popen(command, stdout=PIPE, shell=True)

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
