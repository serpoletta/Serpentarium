#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import sys
import functools
from subprocess import Popen, PIPE
from PyQt4 import QtGui,QtCore

# Класс основного окна
class MainWindow(QtGui.QWidget):
	def __init__(self, parent=None):
		# Создаем окошко
		QtGui.QWidget.__init__(self, parent)
		self.setWindowTitle('While')
		self.move(400, 200)
		
		# Создаем "сайзер"
		self.vbox = QtGui.QVBoxLayout()
		
		# Создаем и добавляем заголовок и подсказку. Nt=5
		self.title = QtGui.QLabel('Наведите курсор')
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setToolTip('Подсказка видима, пока курсор над надписью')
		self.vbox.addWidget(self.title)
		
		self.buttonQ = QtGui.QPushButton('Выйти')
		self.buttonQ.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		# Добавляем в сайзер-бокс
		self.vbox.addWidget(self.buttonQ)
		
		# Добавляем сайзер-бокс в окно
		self.setLayout(self.vbox)
		
	# Функция, вызываемая по клику на кнопку. 
	def buttonClicked(self):
		command = '/usr/bin/python3 /home/rita/University/4\ семестр/Курсовая/files/example1.py'
		p=Popen(command, stdout=PIPE, shell=True)

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
