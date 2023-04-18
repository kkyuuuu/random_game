#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：random_game 
@File ：worker.py
@Date ：2023-04-18 오전 11:07 
'''

import time
import random
from PySide2.QtCore import QThread, Signal

class Worker(QThread):

	DAMAGE = Signal(int)

	def __init__(self, parent):
		super(Worker, self).__init__(parent)
		self.parent = parent
		self.value = parent.value()

	def run(self):
		while True:
			time.sleep(0.01)
			rand = random.randint(self.parent.hit_damage, self.parent.restore_hp)
			if self.value < 1:
				self.DAMAGE.emit(0)
				break
			self.value = self.value + rand
			self.DAMAGE.emit(self.value)

	def stop(self):
		self.value = 0
		self.quit()
		time.sleep(0.15)