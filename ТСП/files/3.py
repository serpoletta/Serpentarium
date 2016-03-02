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
		self.setWindowTitle('If')
		self.move(400, 200)
		
		# Создание layout
		vbox = QtGui.QVBoxLayout()
		
		# Создание и добавление в layout заголовка
		title = QtGui.QLabel('Выберите схему:')
		title.setAlignment(QtCore.Qt.AlignCenter)
		vbox.addWidget(title)
		
		# Создание кнопок
		names = ['1 пример', '2 пример', '2 пример']
		
		for name in names:
			bId = int(name[0])
			button = QtGui.QPushButton(name)
			button.clicked.connect(functools.partial(self.buttonClicked,bId))
			
			# Включение в layout
			vbox.addWidget(button)
		
		# Включение layout в окно
		self.setLayout(vbox)
		
	# Функция, вызываемая по клику на кнопку. Явный if (Nt=3)
	def buttonClicked(self,bId):
		command = ''
		if 1==bId:
			command = '/usr/bin/python3 ./example1.py'
		else:
			command = '/usr/bin/python3 ./example2.py'
		p=Popen(command, stdout=PIPE, shell=True)

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
