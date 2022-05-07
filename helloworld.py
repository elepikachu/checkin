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
import webbrowser
import json

FONT_12 = QFont('Kaiti TC', 15)
VERSION = '杰尼龟每周刷题打卡 v0.0 --by elepikachu'
CONFIG_PATH = 'config.json'
ORIGIN_CONFIG = '{' \
                '"姓名": "巍巍",' \
                '"位置": "米国"' \
                '}'


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
        self.info_dict = read_js()
        if os.path.exists(self.img_route):
            self.use_palette(img_route=self.img_route)

        self.InputWin = QtWidgets.QTextEdit(self)
        self.InputWin.setGeometry(75,100,270,30)
        self.InputWin.setPlaceholderText("输入要做的LC题目，一次一道")
        self.InputWin.setStyleSheet("background:rgb(255,255,255,0.6)")

        self.easy = QtWidgets.QCheckBox(self)
        self.easy.setGeometry(75,140,50,20)
        self.easy.setText("Easy")

        self.mid = QtWidgets.QCheckBox(self)
        self.mid.setGeometry(170, 140, 80, 20)
        self.mid.setText("Middle")

        self.hard = QtWidgets.QCheckBox(self)
        self.hard.setGeometry(275, 140, 50, 20)
        self.hard.setText("Hard")

        self.helpButton = QtWidgets.QPushButton(self)
        self.helpButton.setGeometry(0,0,75,25)
        self.helpButton.setText("Help")
        self.helpButton.setToolTip("打开帮助文档")
        self.helpButton.clicked.connect(self.help_window)

        self.configButton = QtWidgets.QPushButton(self)
        self.configButton.setGeometry(72, 0, 75, 25)
        self.configButton.setText("Config")
        self.configButton.setToolTip("打开配置窗口")
        self.configButton.clicked.connect(self.config_window)

        self.webButton = QtWidgets.QPushButton(self)
        self.webButton.setGeometry(80, 170, 100, 25)
        self.webButton.setText("Open Page")
        self.webButton.setToolTip("打开对应lc网页")
        self.webButton.clicked.connect(self.open_web)

        self.gameButton = QtWidgets.QPushButton(self)
        self.gameButton.setGeometry(200, 170, 100, 25)
        self.gameButton.setText("Game Start")
        self.gameButton.setToolTip("打卡小游戏")
        self.gameButton.clicked.connect(self.close)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setGeometry(325, 0, 75, 25)
        self.exitButton.setText("Exit")
        self.exitButton.setToolTip("关闭程序")
        self.exitButton.clicked.connect(self.close)

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setText(VERSION)
        self.titleLabel.setFont(FONT_12)
        self.titleLabel.setGeometry(75,40,300,20)
        self.titleLabel.setStyleSheet("Color:green")

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setText("----单击更换背景----")
        self.titleLabel.setFont(FONT_12)
        self.titleLabel.setGeometry(150, 510, 150, 20)
        self.titleLabel.setStyleSheet("Color:green")

        self.back1Button = QtWidgets.QPushButton(self)
        self.back1Button.setGeometry(70, 525, 75, 25)
        self.back1Button.setText("Style1")
        self.back1Button.setToolTip("广州遇上西雅图")
        self.back1Button.clicked.connect(self.bk1)

        self.back2Button = QtWidgets.QPushButton(self)
        self.back2Button.setGeometry(170, 525, 75, 25)
        self.back2Button.setText("Sytle2")
        self.back2Button.setToolTip("婧巍填海")
        self.back2Button.clicked.connect(self.bk2)

        self.back3Button = QtWidgets.QPushButton(self)
        self.back3Button.setGeometry(270, 525, 75, 25)
        self.back3Button.setText("Style3")
        self.back3Button.setToolTip("=。=")
        self.back3Button.clicked.connect(self.bk3)

        self.checkButton = QtWidgets.QPushButton(self)
        self.checkButton.setGeometry(120, 555, 75, 25)
        self.checkButton.setText("Check")
        self.checkButton.setToolTip("=。=")
        self.checkButton.clicked.connect(self.bk3)

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setGeometry(220, 555, 75, 25)
        self.submitButton.setText("Submit")
        self.submitButton.setToolTip("=。=")
        self.submitButton.clicked.connect(self.bk3)

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

    def help_window(self):
        windows = Help()
        windows.show_info()

    def config_window(self):
        windows = Config()

    def open_web(self):
        num = self.InputWin.toPlainText().strip()
        page = "https://leetcode-cn.com/problems/" + num
        print(page)
        webbrowser.open(page)


    def bk1(self):
        self.use_palette(img_route="img1.jpeg")
        print("suc")

    def bk2(self):
        self.use_palette(img_route="img2.jpeg")

    def bk3(self):
        self.use_palette(img_route="img3.jpeg")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Warning', 'Are you sure to quit', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Help(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle("帮助文档")
        self.setWindowIcon(QtGui.QIcon('jng.png'))

        self.outBox = QtWidgets.QTextBrowser(self)
        self.outBox.setGeometry(50, 100, 300, 300)
        self.outBox.setStyleSheet("background:rgb(255,255,255,0.6)")
        self.show()

    def show_info(self):
        with open(r'Help.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        self.outBox.setText(text)


class Config(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 600)
        self.setWindowTitle("配置文档")
        self.setWindowIcon(QtGui.QIcon('jng.png'))
        self.info_dict = read_js()

        self.outBox = QtWidgets.QTextEdit(self)
        self.outBox.setGeometry(50, 100, 300, 300)
        self.outBox.setStyleSheet("background:rgb(255,255,255,0.6)")
        self.outBox.setText(str(self.info_dict))

        self.checkButton = QtWidgets.QPushButton(self)
        self.checkButton.setGeometry(100, 500, 75, 25)
        self.checkButton.setText("Config")
        self.checkButton.setToolTip("配置")
        self.checkButton.clicked.connect(self.config)

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setGeometry(250, 500, 75, 25)
        self.submitButton.setText("Reset")
        self.submitButton.setToolTip("重置配置")
        self.submitButton.clicked.connect(self.reset_config)

        self.show()

    def config(self):
        text = self.outBox.toPlainText().strip()
        with open(CONFIG_PATH, 'w') as f:
            f.write(json.dumps(eval(text), ensure_ascii=False))

    def reset_config(self):
        self.outBox.setText(str(ORIGIN_CONFIG))
        with open(CONFIG_PATH, 'w') as f:
            f.write(json.dumps(ORIGIN_CONFIG, ensure_ascii=False))


def read_js(path=CONFIG_PATH):
    with open(path) as load_f:
        return json.load(load_f)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWorld()
    sys.exit(app.exec_())