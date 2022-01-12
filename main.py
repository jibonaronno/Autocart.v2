#!/usr/bin/python3
# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''
REFS
QLineEdit Reference
https://www.tutorialspoint.com/pyqt/pyqt_qlineedit_widget.htm
'''

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
from PyQt5.QtWidgets import QLabel, QLineEdit, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QListWidget, QListWidgetItem
import qtmodern.styles
import qtmodern.windows
from qrcode import QRCode
from mqttlisten import MqttListen
from crud import CRUD
from datetime import datetime

_UI = join(dirname(abspath(__file__)), 'mainwindow.ui')

class Object(object):
    pass

class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widget = uic.loadUi(_UI, self)
        qcode = QRCode()
        qrtext = qcode.genQrFromNow()
        qcode.genSvgFile(qrtext) #("013012155011")
        print(qrtext)
        self.repaint()
        self.db = CRUD("autocart.db")
        self.db.openDBHard()
        strdate = datetime.today().strftime('%m-%d-%Y')
        strtime = datetime.today().strftime('%H:%M:%S')
        self.db.addNewToken([strdate, strtime, qrtext, ""])
        #te = self.db.tokenExist(qrtext)
        #print("Token Exist ? = " + str(te))

        try:
            mqtt = MqttListen()
            mqtt.Subscribe()
        except Exception as e:
            print(str(e))

        #self.label02 = QLabel()
        #self.text_token = QLineEdit()
        #self.barcodeEdit = QLineEdit()
        self.text_token.returnPressed.connect(self.findToken)
        self.barcodeEdit.returnPressed.connect(self.addItem)

        self.objItems = Object()
        self.objItems.token = ""
        self.objItems.items = []

    def addItem(self):
        txt = self.barcodeEdit.text()
        te, itm = self.db.inventoryItemExist(txt)
        if te > 0:
            self.label02.setText("Item Exist : " + itm)
            row = self.db.inventoryGetItem(txt)
            #print(row)
            if len(row[0]) > 4:
                self.objItems.items.append(row[0])
                #print(row[0])
            ridx = 0
            cidx = 0
            self.tableWidget.setRowCount(len(self.objItems.items))
            print(self.objItems.items[0])
            for roww in self.objItems.items:
                self.tableWidget.setItem(ridx, 3, QTableWidgetItem(str(roww[1])))
                self.tableWidget.setItem(ridx, 0, QTableWidgetItem(str(roww[2])))
                self.tableWidget.setItem(ridx, 1, QTableWidgetItem(str(roww[0])))
                self.tableWidget.setItem(ridx, 2, QTableWidgetItem(str(roww[3])))
                self.tableWidget.setItem(ridx, 4, QTableWidgetItem(str(roww[5])))
                self.tableWidget.setItem(ridx, 5, QTableWidgetItem(str(1)))
                self.tableWidget.setItem(ridx, 6, QTableWidgetItem(str(roww[5])))
                ridx += 1


    def findToken(self):
        txt = self.text_token.text()
        te = self.db.tokenExist(txt)
        if te > 1:
            print("Token Exist : " + str(te))
        if te == 2:
            self.label02.setText("Processing Token : " + txt)
        elif te == 3:
            self.label02.setText("Passed Token : " + txt)
        elif te == 0:
            self.label02.setText("Token Does Not Exist : " + txt)

    @Slot()
    def on_btnNextToken_clicked(self):
        qcode = QRCode()
        qrtext = qcode.genQrFromNow()
        qcode.genSvgFile(qrtext)  # ("013012155011")
        print(qrtext)
        self.repaint()
        strdate = datetime.today().strftime('%m-%d-%Y')
        strtime = datetime.today().strftime('%H:%M:%S')
        self.db.addNewToken([strdate, strtime, qrtext, ""])

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
