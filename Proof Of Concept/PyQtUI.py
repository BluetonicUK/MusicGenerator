# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:22:06 2021

@author: johnn
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import * 
import sys
from utility import *
from FoxDot1 import *
from FoxDot import *
from pythonosc import udp_client

class PyQtUI(QMainWindow):
    def __init__(self):
        super(PyQtUI, self).__init__()
        self.setGeometry(100, 100, 400, 300) #x,y,w,h
        self.setFixedSize(700, 300)
        self.setWindowTitle("Music Generator")
        self.initUI()
        #self.window()
        #self.show()
        
    def initUI(self):
        self.play = QtWidgets.QPushButton(self)
        self.play.setText("Play")
        self.play.move(50, 50)
        self.play.clicked.connect(self.clickPlay)
        
        
        self.stop = QtWidgets.QPushButton(self)
        self.stop.setText("Stop")
        self.stop.move(170, 50)
        self.stop.clicked.connect(self.clickStop)
        
        self.record = QtWidgets.QPushButton(self)
        self.record.setText("Record")
        self.record.move(290, 50)
        self.record.clicked.connect(self.startRecording)
        
        self.stopRecord = QtWidgets.QPushButton(self)
        self.stopRecord.setText("Stop Record")
        self.stopRecord.move(410, 50)
        self.stopRecord.clicked.connect(self.stopRecording)
              
        self.analyse = QtWidgets.QPushButton(self)
        self.analyse.setText("Analyse")
        self.analyse.move(530, 50)
        self.analyse.setEnabled(False)
        
    def clickPlay(self):
        self.play.setEnabled(False)
        player()
        
        
    def clickStop(self):
        self.play.setEnabled(True)
        Clock.clear()
        
    def startRecording(self):
        # path = r'C:\Users\johnn\Dropbox\FInal Year Project\MusicGenerator\Proof Of Concept\recordings.test.aiff'
        # Server.record(path)
        Server.record()
        
    def stopRecording(self):
        self.analyse.setEnabled(True)
        Server.stopRecording()
    
    def displayInstruments(self, instrument1, instrument2):
        self.ins1 = QtWidgets.QLabel(self)
        self.ins1.setText("Instrument 1: " + instrument1)
        self.ins1.move(50, 100)
        
        self.ins2 = QtWidgets.QLabel(self)
        self.ins2.setText("Instrument 2: " + instrument2)
        self.ins2.move(50, 120)
    
    def displayTempo(self, tempo):
        self.tempo = QtWidgets.QLabel(self)
        self.tempo.setText("Tempo: " + str(tempo) + "bpm")
        self.tempo.move(50, 160)
        
        
    def update(self): 
        self.label.adjustSize()
        
    # def showUI(self):
    #     self.show()



def window():
    app = QApplication(sys.argv)
    win = PyQtUI()
    #win.displayInstruments("bongo", "blh")
    #win.displayTempo(80)
    win.show()
    
    sys.exit(app.exec_())


window()   
