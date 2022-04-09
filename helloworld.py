#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:24:37 2022

@author: elepikachu
"""

import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 220) 
        self.setWindowTitle('杰尼龟')
        self.setWindowIcon(QtGui.QIcon('jng.png'))
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWorld()
    sys.exit(app.exec_())