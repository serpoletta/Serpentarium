#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

'''
"Учебно-макетное представление, в виде программного кода на языке Python, принципов теории схем программ по курсу 'ТВП и С'"

Краткие названия: "Теория схем программ", "ТСП"
Версия: 1.1
Код схем переработан для публикации в научном журнале.
Код основной программы доработан (в публикацию не входит).
Код примеров изменен (в публикацию не входит).

Автор: Маргарита Морозова
КФУ ИВМиИТ, 2 курс, 09-308
Научный руководитель: к.т.н. Георгиев В.О.
2015
'''

import sys
import functools
from subprocess import Popen, PIPE
from PyQt4 import QtGui,QtCore

# Класс основного окна
class MainWindow(QtGui.QWidget):
	def __init__(self, parent=None):
		# Создаем окошко
		QtGui.QWidget.__init__(self, parent)
		
		self.setWindowTitle('Схемы интерпретации сценария диалога')
		self.resize(400, 300)
		
		# Создаем "сайзер"
		grid = QtGui.QGridLayout()
		
		# Создаем и добавляем заголовки
		title = QtGui.QLabel('Схемы интерпретации сценария')
		titleFont = QtGui.QFont('Nimbus Sans L', 18, QtGui.QFont.Light)
		title.setAlignment(QtCore.Qt.AlignCenter)
		title.setFont(titleFont)
		
		subtitle = QtGui.QLabel('  Выберите схему:')
		
		grid.addWidget(title,   0,0,3,0)
		grid.addWidget(subtitle,1,0,3,0)
		
		
		# Создаем кнопочки
		names = ['Nt=0', 'Nt=1', 'Nt=2',
				 'Nt=3', 'Nt=4', 'Nt=5',
				 'Nt=6', 'Nt=7', 'Nt=8',
				 ]
		
		pos = [(2, 0), (2, 1), (2, 2),
			(3, 0), (3, 1), (3, 2),
			(4, 0), (4, 1), (4, 2)
			]
				
		j = 0
		# Не царское это дело - вручную одинаковые кнопочки создавать
		for name in names:
			bId = int(name[-1])
			button = QtGui.QPushButton(name)
			button.clicked.connect(functools.partial(self.buttonClicked,bId))
			
			# Добавляем в сайзер-таблицу
			grid.addWidget(button, pos[j][0], pos[j][1])
			
			j = j + 1
		
		# Добавляем сайзер-таблицу в окно
		self.setLayout(grid)
		
	# Функция, вызываемая по клику на кнопку. Создает окошко для номера схемы
	def buttonClicked(self,bId):
		self.ntWindow = NTxInfoWindow(bId)
		self.ntWindow.show()

# Класс окна с информацией о схеме
class NTxInfoWindow(QtGui.QWidget):
	def __init__(self, schemeId, parent=None):
		# Создаем и оформляем окошко
		QtGui.QWidget.__init__(self, parent)
		
		# self здесь - это очень важно! Иначе объект убивается сборщиком мусора
		title = 'Схема Nt=' + str(schemeId)
		self.setWindowTitle(title)
		self.move(200, 100)
		
		# Читаем данные с диска (а вот и работа со сценариями)
		ntxInfo = NTxInfo(schemeId)
		
		# Прописываем элементы, которые будут в окне
		
		# Заголовок
		title = QtGui.QLabel(ntxInfo.title)
		titleFont = QtGui.QFont('Nimbus Sans L', 16, QtGui.QFont.Light)
		title.setAlignment(QtCore.Qt.AlignCenter)
		title.setFont(titleFont)
		
		# Текст, схема
		info = QtGui.QLabel('\n'.join(ntxInfo.info))
		#info = QtGui.QTextEdit('\n'.join(ntxInfo.info)) - если понадобится
		ginfo = QtGui.QLabel()
		ginfo.setPixmap(QtGui.QPixmap(ntxInfo.ginfo))
		#ginfo.resize(300,250)
		
		# Код примера
		code = QtGui.QTextEdit()
		code.setText(''.join(ntxInfo.code))
		code.setReadOnly(True)
		code.setLineWrapMode(1)
		#code.setFont(titleFont)
		
		# Кнопка запуска примера (запускает файл из подпапки files по коду схемы)
		exampleButton = QtGui.QPushButton('Пуск!')
		
		exampleButton.clicked.connect(functools.partial(self.buttonClicked,schemeId)) #(lambda: system(command))
		
		# Прописываем layout
		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		
		vbox.addWidget(title)
		vbox.addWidget(info)
		vbox.addWidget(ginfo)
		vbox.addWidget(code) 
		vbox.addWidget(exampleButton)
		
		# внутрь можно засовывать другие layout'ы vbox.addLayout(hbox)
		self.setLayout(vbox)
	
	def buttonClicked(self,schemeId):
		command = '/usr/bin/python3 ./files/' + str(schemeId) + '.py'
		p=Popen(command, stdout=PIPE, shell=True)
#		stdoutdata, stderrdata = p.communicate()
#		errorCode=p.returncode

# Класс для хранения и чтения информации о схеме
class NTxInfo(QtGui.QWidget):
	# Здесь мы читаем информацию с диска
	def __read__(self,schemeId):
		
		# Читаем заголовок и информацию из специального файла
		infoFile = open('./files/' + str(schemeId) + '.txt', 'r')
		
		title = infoFile.readline()
		self.setTitle(title)
		
		info = infoFile.readlines()
		self.setInfo(info)
		
		infoFile.close()
		
		# Вставляем графическую схему - адрес файла с ней
		self.setGinfo('./files/' + str(schemeId) + '.png')
		
		# Читаем код примера - из специального файла
		codeFile = open('./files/' + str(schemeId) + '.py', 'r')
		code = codeFile.readlines()
		
		codeFile.close()
		self.setCode(code)
		
		# Пример - запуск программы
		self.setExample('')
	
	
	def __init__(self, schemeId, parent=None):
		self.__read__(schemeId) # Читаем с диска значения атрибутов
	
	# Аттрибуты
	
	# Заголовок
	def getTitle(self):
		return self._title
	
	def setTitle(self, title):
		self._title = title
	
	title = property(getTitle, setTitle)
	# Информация
	def getInfo(self):
		return self._info
	
	def setInfo(self, info):
		self._info = info
	
	info = property(getInfo, setInfo)
	
	def getGinfo(self):
		return self._ginfo
	
	def setGinfo(self, ginfo):
		self._ginfo = ginfo
	
	ginfo = property(getGinfo, setGinfo)
	
	# Пример
	def getExample(self):
		return self._example
	
	def setExample(self, example):
		self._example = example
	
	example = property(getExample, setExample)
	
	# Код примера
	def getCode(self):
		return self._code
	
	def setCode(self, code):
		self._code = code
	
	code = property(getCode, setCode)


# Создаем окно main Window
# Список аргументов программной строки - в sys
app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()



# Вызываем основной цикл. Как только он завершится - вызовется sys.exit()
sys.exit(app.exec_())


'''
http://tekhnosfera.com/tehnologicheskie-printsipy-sozdaniya-dialogovyh-sistem-stsenarnogo-tipa-s-ispolzovaniem-kontseptsii-programmnyh-transform - здесь лежат типовые схемы
0) Nt=О. Финальная конструкция "STOP" (завершение диалога).

1) Nt=1. Схема выбора "к .—> к + 1" ("следующий").

2) Nt=2. Последовательная интерпретация элементов.

3) Nt=3. Схема типа "if - then - else".

4) Nt=4. Схема типа "case", предусматривающая выбор альтернативных шагов диалога, в зависимости от списка условий В.

5) Nt=5. Схема типа "while - do".

6) Nt=6. Схема типа "repeat - until".

7) Nt=7. Схема типа "CALL". 

8) Nt=8 Начальная конструкция "START"
'''
