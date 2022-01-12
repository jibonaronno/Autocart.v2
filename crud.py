import sqlite3
from sqlite3 import Error
from os.path import join, dirname, abspath
from PyQt5.QtCore import QDateTime
from collections import deque

dbfile = join(dirname(abspath(__file__)), 'autocart.db')

class CRUD(object):
    def __init__(self, filename):
        self.filename = filename
        self.OrderStack = deque()
        print(dbfile)

    def openDB(self, filename):
        conn = None
        try:
            conn = sqlite3.connect(filename)
            print("Database Connected.")
        except Error as e:
            print(e)
        return conn

    def openDBHard(self):
        self.con = self.openDB(dbfile)

    def addNewToken(self, data):
        sql = '''INSERT INTO tokens(_date,_time,token,_json) VALUES(?,?,?,?)'''
        cur = self.con.cursor()
        cur.execute(sql, data)
        self.con.commit()
        return cur.lastrowid

    def inventoryItemExist(self, barcode:str):
        if barcode:
            sql = "SELECT * FROM inventory WHERE barcode='" + barcode + "'"
            cur = self.con.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) > 0:
                print(rows[0][1])
                return (3, rows[0][1]) # data exist
            else:
                return (0, "") # data not exist
        return (1, "") # parameter error

    def inventoryGetItem(self, barcode:str):
        if barcode:
            sql = "SELECT * FROM inventory WHERE barcode='" + barcode + "'"
            cur = self.con.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) > 0:
                return rows
        return None

    def tokenExist(self, token:str):
        if token:
            sql = "SELECT * FROM tokens WHERE token='" + token + "'"
            cur = self.con.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) > 0:
                if rows[0][3] == "":
                    return 2
                else:
                    return 3
            else:
                return 0
        return 1

    def updateToken(self):
        pass


    def insert_meter_data(self, data):
        #sql = '''INSERT INTO meter_data(datetime,content,devid) VALUES('11-30-2021 21:52:00', '12.343', '0x001')'''
        sql = '''INSERT INTO meter_data(datetime,content,devid) VALUES(?,?,?)'''
        cur = self.con.cursor()
        cur.execute(sql, data)
        self.con.commit()
        return cur.lastrowid

    def getListByDateRange(self, startd:QDateTime, endd:QDateTime, devid=None):
        #print(startd.date().toString("MM-dd-yyyy") + " " + startd.time().toString('HH:mm:ss'))
        #print(startd.toString("MM-dd-yyyy HH:mm:ss"))
        sql = ""
        data = []
        if devid:
            sql = "SELECT * FROM meter_data WHERE datetime BETWEEN '" + startd.toString("MM-dd-yyyy HH:mm:ss") + "' AND '" + endd.toString("MM-dd-yyyy HH:mm:ss") + "'" + "AND devid="+ str(devid)
        else:
            sql = "SELECT * FROM meter_data WHERE datetime BETWEEN '"+ startd.toString("MM-dd-yyyy HH:mm:ss") + "' AND '" + endd.toString("MM-dd-yyyy HH:mm:ss") + "'"
        cur = self.con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            dtms = row[0].split(" ")
            data.append([dtms[0], dtms[1], row[2], row[1]])
        return data

    def insert_meter_data_hard(self):
        try:
            self.insert_meter_data(['11-30-2021 21:52:00', '12.343', '0x001'])
        except Error as e:
            print(e)

    def addRecord(self):
        pass
