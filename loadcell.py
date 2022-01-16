
from os.path import join, dirname, abspath

import pandas
from qtpy import uic
from qtpy.QtCore import Slot, QTimer, QThread, Signal, QObject, Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from crud import CRUD
import pandas as pd

_UI3 = join(dirname(abspath(__file__)), 'weight.ui')

class LoadCell(QWidget):
    def __init__(self):
        QWidget.__init__(self)  # self, *args, **kwargs
        self.widget = uic.loadUi(_UI3, self)
        self.lcdNumber = QLCDNumber()

    def read(self):
        pass