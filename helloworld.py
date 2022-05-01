#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:24:37 2022

@author: elepikachu
"""

import sys
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QFont

FONT_12 = QFont('Kaiti TC', 15)
VERSION = '杰尼龟每周刷题签到 0.0 --by elepikachu'

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle(VERSION)
        self.setWindowIcon(QtGui.QIcon('jng.png'))
        self.setToolTip(VERSION)
        self.img_route = 'background.jpeg'
        if os.path.exists(self.img_route):
            self.use_palette(img_route=self.img_route)

        self.helpButton = QtWidgets.QPushButton(self)
        self.helpButton.setGeometry(0,0,75,25)
        self.helpButton.setText("Help")
        self.helpButton.setToolTip("打开帮助文档")

        self.configButton = QtWidgets.QPushButton(self)
        self.configButton.setGeometry(72, 0, 75, 25)
        self.configButton.setText("Config")
        self.configButton.setToolTip("打开配置窗口")

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setGeometry(325, 0, 75, 25)
        self.exitButton.setText("Exit")
        self.exitButton.setToolTip("关闭程序")
        self.exitButton.clicked.connect(self.close)

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setText(VERSION)
        self.titleLabel.setFont(FONT_12)
        self.titleLabel.setGeometry(75,30,300,20)

        self.outBox = QtWidgets.QTextBrowser(self)
        self.outBox.setGeometry(50, 200, 300, 300)
        self.outBox.setStyleSheet("background:rgb(255,255,255,0.6)")
        self.show()

    def use_palette(self, img_route):
        window_pale = QtGui.QPalette()
        pix = QtGui.QPixmap(img_route)
        pix = pix.scaled(400, 600)
        window_pale.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        self.setPalette(window_pale)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Warning', 'Are you sure to quit', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWorld()
    sys.exit(app.exec_())