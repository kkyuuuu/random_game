#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：random_game 
@File ：random_game.py
@Date ：2023-04-18 오전 11:06 
'''

import sys
from PySide2.QtWidgets import QMainWindow, QWidget,	QVBoxLayout, QHBoxLayout,\
	QLineEdit, QPushButton, QApplication
import progress

class Window(QMainWindow):

	_MAX_HP = 50000
	_HIT_DAMAGE = -1000
	_RESTORE_HP = 750

	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		self.ui()
		self.connections()
		self.init()

	def init(self):
		# progress instance list
		self.progress_list = []
		# result str
		self.result = []

	def connections(self):
		self.lineEdit.returnPressed.connect(self.insert_progress_bar)
		self.pb_start.clicked.connect(self.start)
		self.pb_reset.clicked.connect(self.reset)

	def set_result(self):
		if len(self.progress_list) == len(self.result):
			txt = ''
			for idx, user in enumerate(reversed(self.result)):
				txt += '{}: {} / '.format(str(idx + 1), user)
			self.status.showMessage(txt)

	def insert_progress_bar(self):
		cls = progress.ProgressBar(self, self.lineEdit.text())
		self.progress_layout.addWidget(cls)
		self.progress_list.append(cls)
		self.lineEdit.selectAll()

	def start(self):
		self.pb_start.setEnabled(False)
		for cls in self.progress_list:
			cls.start()

	def _stop(self):
		for cls in self.progress_list:
			cls.stop()

	def _clear(self):
		self.progress_list = []
		self.result = []
		self.clear_layout(self.progress_layout)

	def _restore_ui(self):
		self.resize(800, 30)
		self.adjustSize()
		self.pb_start.setEnabled(True)
		self.lineEdit.clear()
		self.status.showMessage('')

	def reset(self):
		self._stop()
		self._clear()
		self._restore_ui()

	def clear_layout(self, layout):
		while layout.count():
			item = layout.takeAt(0)
			widget = item.widget()
			if widget is not None:
				widget.deleteLater()
			else:
				self.clear_layout(item.layout())

	def ui(self):
		self.setWindowTitle('Random Game')
		self.centralwidget = QWidget(self)
		self.status = self.statusBar()
		self.main_layout = QVBoxLayout(self.centralwidget)
		self.resize(800, 30)

		self.button_layout = QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.lineEdit = QLineEdit()
		self.lineEdit.setMinimumHeight(30)
		self.lineEdit.setMinimumWidth(800)
		self.lineEdit.setPlaceholderText(r'Enter your nickname and enter')
		self.button_layout.addWidget(self.lineEdit)

		self.pb_start = QPushButton('Start')
		self.pb_start.setMinimumHeight(30)
		self.pb_reset = QPushButton('Reset')
		self.pb_reset.setMinimumHeight(30)
		self.button_layout.addWidget(self.pb_start)
		self.button_layout.addWidget(self.pb_reset)
		self.lineEdit.setFocus()

		self.progress_layout = QVBoxLayout()
		self.main_layout.addLayout(self.progress_layout)
		self.setCentralWidget(self.centralwidget)
		self.adjustSize()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())
