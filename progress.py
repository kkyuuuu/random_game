#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：random_game 
@File ：progress.py
@Date ：2023-04-18 오전 11:06 
'''

from PySide2.QtWidgets import QProgressBar
from PySide2.QtGui import Qt
import worker

class ProgressBar(QProgressBar):

	def __init__(self, parent, user):
		super(ProgressBar, self).__init__()
		self.parent = parent
		self.user = user
		self.hit_damage = parent._HIT_DAMAGE
		self.restore_hp = parent._RESTORE_HP
		self.ui()
		self.init()

	def init(self):
		self.work = None

	def ui(self):
		self.setMinimumHeight(50)
		self.setMinimum(0)
		self.setMaximum(self.parent._MAX_HP)
		self.setValue(self.parent._MAX_HP)
		self.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		self.setTextVisible(True)
		self.setFormat("{} HP: {}".format(self.user, str(self.value())))
		self.setStyleSheet("""
		ProgressBar {
			text-align: center;
			color: black;     
		}
		ProgressBar::chunk {
			background-color: #F44336;
		}
		""")

	def start(self):
		self.work = worker.Worker(self)
		self.work.DAMAGE.connect(self.set_result)
		self.work.start()

	def stop(self):
		self.work.stop()

	def set_result(self, value):
		if value == 0:
			self.parent.result.append(self.user)
			self.parent.set_result()

		self.setValue(value)
		self.setFormat("{} HP: {}".format(self.user, str(self.value())))