import os,sys
from imutils.video import VideoStream
#from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
#from barcode import EAN13
#from barcode.writer import ImageWriter

class Camera(object):
    global camPtr
    def __init__(self):
        pass

    def start(self):
        camPtr = None
        try:
            #camPtr = VideoStream(usePiCamera=True).start()
            camPtr = VideoStream(src=0).start()
            print("Got CamPtr as: ", camPtr)
        except Exception as err:
            print("Got Error while opening Camera interface :", err)
            sys.exit()
        return camPtr

    def getBarcode(self, camPtr):
        frame = camPtr.read()
        if frame is not None:
            frame = imutils.resize(frame, width=640)
        return frame
