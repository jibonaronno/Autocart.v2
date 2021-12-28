#!/usr/bin/python3
# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import enum
from os.path import join, dirname, abspath
import queue
import serial
import serial.tools.list_ports as port_list
from qtpy import uic
from qtpy.QtCore import Slot, QTimer, QThread, Signal, QObject, Qt
from qtpy.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QDialog, QTableWidgetItem, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QListWidget, QListWidgetItem
import qtmodern.styles
import qtmodern.windows
from qrcode import QRCode
from mqttlisten import MqttListen
from crud import CRUD

_UI = join(dirname(abspath(__file__)), 'mainwindow.ui')

class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widget = uic.loadUi(_UI, self)
        qcode = QRCode()
        qcode.genSvgFile(qcode.genQrFromNow()) #("013012155011")
        print(qcode.genQrFromNow())
        self.repaint()
        self.db = CRUD("flow.db")
        self.db.openDBHard()

        mqtt = MqttListen()
        mqtt.Subscribe()

    def paintEvent(self, event:QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        qp.drawPixmap(20, 10, 200, 200, QPixmap("qrcode.svg"))
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # qtmodern.styles.dark(app)
    qtmodern.styles.light(app)
    mw_class_instance = MainWindow()
    mw = qtmodern.windows.ModernWindow(mw_class_instance)
    #mw.showFullScreen()
    mw.showNormal()
    sys.exit(app.exec_())
