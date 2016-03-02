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
		self.setWindowTitle('Repeat-until')
		self.move(400, 200)
		
		# Создание layout
		self.vbox = QtGui.QVBoxLayout()
		
		# Создание и добавление в layout CheckBox'а
		self.cb = QtGui.QCheckBox('Разрешить завершение работы', self)
		self.vbox.addWidget(self.cb)
		
		# Создание кнопки
		self.button = QtGui.QPushButton('Выход')
		self.button.clicked.connect(functools.partial(self.buttonClicked))
		
		# Включение в layout
		self.vbox.addWidget(self.button)
		
		# Включение layout в окно
		self.setLayout(self.vbox)
	
	# Nt=6 - неявная. Семантически программа работает до тех пор, 
	# пока не будет отмечен CheckBox (repeat-until), но синтаксически это не реализовывается циклом.
	def closeEvent(self,event):
		if not self.cb.isChecked():
			event.ignore()
		else:
			event.accept()
	
	# Функция, вызываемая по клику на кнопку. 
	def buttonClicked(self):
		self.close()

# Запуск программы
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

sys.exit(app.exec_())
