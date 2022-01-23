import os,sys
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
#from barcode import EAN13
#from barcode.writer import ImageWriter
from qtpy.QtCore import Signal, QThread, QObject

class Camera(QObject):
    global camPtr
    global vid
    global img
    signal = Signal(str)
    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        self.thread = QThread()
        self.thread.started.connect(self.loop)
        super().__init__()

    def loop(self):
        try:
            while True:
                _, frm = self.vid.read()
                #frame = imutils.resize(frm, width=640)
                #image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #barcodes = pyzbar.decode(image)
                #img = image
                #self.signal.emit("cropp")
                time.sleep(500)
        except Exception as e:
            print(str(e))

    def startLoop(self):
        self.moveToThread(self.thread)
        self.thread.start()

    def start(self):
        try:
            #camPtr = VideoStream(usePiCamera=True).start()
            camPtr = VideoStream(src=0).start()
            print("Got CamPtr as: ", camPtr)
        except Exception as err:
            print("Got Error while opening Camera interface :", err)
            sys.exit()
        return camPtr

    def capture(self):
        vid = cv2.VideoCapture(0)
        vid.read()
        vid.read()
        vid.read()
        vid.read()
        vid.read()
        vid.read()
        ret, frame = vid.read()
        frame = imutils.resize(frame, width=640)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        vid.release()
        return image

    def Barcode(self):
        frame = self.capture()
        barcodes = pyzbar.decode(frame)
        if len(barcodes) > 0:
            print("barcode found - " + str(len(barcodes)))
        else:
            print("barcode not found")
        for barcode in barcodes:
            pass

    def getBarcode(self, camPtr):
        frame = camPtr.read()
        if frame is not None:
            frame = imutils.resize(frame, width=640)
        return frame
