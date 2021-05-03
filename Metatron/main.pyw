# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import datetime
import threading
import time
import json
import urllib.request
import sys
import codecs
import webbrowser

#from lib import functions
#from lib import gl
app = QtWidgets.QApplication([])

win = uic.loadUi("ui/metatronsight.ui") #specify the location of your .ui file
def GetValue(self, row, col):
    return self.data[row][col]

def openurl(self):
    #obj = event.GetEventObject()
    #url1=obj.GetCellValue(event.GetRow(),1)
    item = self.table.itemAt(row, 2)
    win.label.setText(item)

    #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    oid="608be70b8a6e8c0f51a65b46"
    url="http://192.168.0.15:3000/meta/"+oid
    webbrowser.open(url)
def cell_was_clicked( row, column):
    #print("Row %d and Column %d was clicked" % (row, column))
    item = win.tableWidget.itemAt(2, 2)
    win.label.setText(str(item.text()))
    #win.label.setText("Row %d and Column %d was clicked" % (row, column))
def setjson():
    url = 'http://192.168.0.15:3000/jsapi/json'
    res = urllib.request.urlopen(url)
    # json_loads() でPythonオブジェクトに変換
    data = json.loads(res.read().decode('utf-8'))
    #s=res.read().decode('utf-8')
    i = 0
    j = 0
    win.tableWidget.setRowCount(100)
    # set column count
    win.tableWidget.setColumnCount(2)
    #win.tableWidget.itemDoubleClicked.connect(openurl)
    win.tableWidget.cellClicked.connect(cell_was_clicked)
    #win.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    for item in data:
        win.label.setText(str(item["title"]))
        Data = QTableWidgetItem(str(item["title"]))
        j = 0
        win.tableWidget.setItem(i, j, Data)
        Data2 = QTableWidgetItem(str(item["link"]))
        j = 1
        win.tableWidget.setItem(i, j, Data2)


        i = i + 1
    win.tableWidget.resizeColumnToContents(0)
    win.tableWidget.resizeColumnToContents(1)
def setTable(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    # test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    # contents = test_data.read()
    # ファイルをクローズする
    # test_data.close()
    #f = open('data/test2.txt', 'r')
    #jsonData = json.load(f)
    #f.close()
    # tableData0=contents

    d = data
    print(d)
    i = 0
    j = 0
    # for i, (key, value) in enumerate(d["events"].items()):
    # set row count
    win.tableWidget.setRowCount(10)
    # set column count
    win.tableWidget.setColumnCount(4)
    win.tableWidget.itemDoubleClicked.connect(show_hensyu)
    # currentQTableWidgetItem.row()

    for item in d:
        # print(str(i)+":"+item["title"])
        Data = QTableWidgetItem(str(item["title"]))
        j = 0
        win.tableWidget.setItem(i, j, Data)

        j = 1
        Data2 = QTableWidgetItem(str(item["body"]))
        win.tableWidget.setItem(i, j, Data2)

        j = 2

        if not item.get('date'):
            print('NULL')
        else:
            Data2 = QTableWidgetItem(str(item["date"]))
            win.tableWidget.setItem(i, j, Data2)

        j = 3
        Data2 = QTableWidgetItem(str(item["amount"]))
        win.tableWidget.setItem(i, j, Data2)
        i = i + 1
    win.tableWidget.resizeColumnToContents(0)
    win.tableWidget.resizeColumnToContents(2)
win.resize(1024,750)
win.show()
setjson()
#gl.main()
sys.exit(app.exec())
