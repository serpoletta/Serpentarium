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
		self.setWindowTitle('START')
		self.move(400, 200)
		
		# Создание layout
		vbox = QtGui.QVBoxLayout()
		
		# Создание и добавление в layout заголовка и кнопок
		title = QtGui.QLabel('Начать?')
		title.setAlignment(QtCore.Qt.AlignCenter)
		vbox.addWidget(title)
		
		buttonYes = QtGui.QPushButton('Да')
		buttonYes.clicked.connect(functools.partial(self.buttonClicked))
		
		buttonNo = QtGui.QPushButton('Нет')
		buttonNo.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		vbox.addWidget(buttonYes)
		vbox.addWidget(buttonNo)
		
		# Включение layout в окно
		self.setLayout(vbox)
		
	# Функция, вызываемая по клику на кнопку.
	def buttonClicked(self):
		command = '/usr/bin/python3 ./example1.py'
		p=Popen(command, stdout=PIPE, shell=True)

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
