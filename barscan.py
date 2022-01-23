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

class Camera(object):
    global camPtr
    global vid
    def __init__(self):
        pass

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
        vid.read()
        vid.read()
        vid.read()
        vid.read()
        vid.release()
        return frame

    def Barcode(self):
        frame = self.capture()
        barcodes = pyzbar.decode(frame)
        if len(barcodes) > 0:
            print("barcode found")
        else:
            print("barcode not found")
        for barcode in barcodes:
            pass

    def getBarcode(self, camPtr):
        frame = camPtr.read()
        if frame is not None:
            frame = imutils.resize(frame, width=640)
        return frame
