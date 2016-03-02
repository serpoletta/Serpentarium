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
		self.setWindowTitle('CALL')
		self.setGeometry(600,150,400,200)
		self.move(400, 200)
		
		# Создание layout
		vbox = QtGui.QVBoxLayout()
		 
		# Создание и добавление в layout заголовка, поля и кнопки
		self.title = QtGui.QLabel('Введите команду:')
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		vbox.addWidget(self.title)
		
		self.cmdEdit = QtGui.QLineEdit('/usr/bin/python3 ./example1.py')
		
		self.button = QtGui.QPushButton('Выполнить!')
		self.button.clicked.connect(self.buttonClicked)
		
		# Включение в layout
		
		vbox.addWidget(self.cmdEdit)
		vbox.addWidget(self.button)
		
		# Включение layout в окно
		self.setLayout(vbox)
		
	# Функция, вызываемая по клику на кнопку. Явный CALL (Nt=7)
	def buttonClicked(self):
		command = self.cmdEdit.text()
		p=Popen(command, stdout=PIPE, shell=True)

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
