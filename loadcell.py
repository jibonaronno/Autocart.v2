
from os.path import join, dirname, abspath
from qtpy import uic
from PyQt5.QtWidgets import *

_UI3 = join(dirname(abspath(__file__)), 'weight.ui')

class LoadCell(QWidget):
    def __init__(self):
        QWidget.__init__(self)  # self, *args, **kwargs
        self.widget = uic.loadUi(_UI3, self)
        #self.lcdNumber = QLCDNumber()

    def read(self):
        pass