# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:22:06 2021

@author: johnn
"""
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import * 
import sys
from utility import *
from FoxDot1 import *
from FoxDot import *
from pythonosc import udp_client
from glob import glob
from Analysis import Analysis

class PyQtUI(QMainWindow):
    def __init__(self):
        super(PyQtUI, self).__init__()
        #self.setGeometry(100, 100, 700, 300) #x,y,w,h
        self.setFixedSize(600, 500)
        self.setWindowTitle("Music Generator")
        self.initUI()
        self.setStyleSheet("background: #161219;")
        #self.window()
        #self.show()
  
        
    def initUI(self):
    
        self.play = QtWidgets.QPushButton(self)
        self.play.setText("Play")
        self.play.move(50, 50)
        self.play.clicked.connect(self.clickPlay)

        self.stop = QtWidgets.QPushButton(self)
        self.stop.setText("Stop")
        self.stop.move(50, 90)
        self.stop.clicked.connect(self.clickStop)
        
        self.record = QtWidgets.QPushButton(self)
        self.record.setText("Record")
        self.record.move(50, 130)
        self.record.clicked.connect(self.startRecording)
        
        self.stopRecord = QtWidgets.QPushButton(self)
        self.stopRecord.setText("Stop Record")
        self.stopRecord.move(50, 170)
        self.stopRecord.clicked.connect(self.stopRecording)
              
        self.analyseWave = QtWidgets.QPushButton(self)
        self.analyseWave.setText("Waveplot")
        self.analyseWave.move(50, 210)
        self.analyseWave.setEnabled(False)
        self.analyseWave.clicked.connect(self.displayWaveplot)
        
        self.analyseHandP = QtWidgets.QPushButton(self)
        self.analyseHandP.setText("Harmonics")
        self.analyseHandP.move(50, 250)
        self.analyseHandP.setEnabled(False)
        self.analyseHandP.clicked.connect(self.displayHarmonicsPercussion)
        
        self.analyseSpectogram = QtWidgets.QPushButton(self)
        self.analyseSpectogram.setText("Spectogram")
        self.analyseSpectogram.move(50, 290)
        self.analyseSpectogram.setEnabled(False)
        self.analyseSpectogram.clicked.connect(self.displaySpectogram)
        
        self.playLabel = QtWidgets.QLabel(self)
        self.playLabel.setText("")
        self.playLabel.move(75, 20)
        
        
        
    def clickPlay(self):
        self.play.setEnabled(False)
        self.playLabel.setText("Playing...")
        player()
        
        
    def clickStop(self):
        self.play.setEnabled(True)
        self.playLabel.setText("Stopped")
        Clock.clear()
        
    def startRecording(self):
        # path = r'C:\Users\johnn\Dropbox\FInal Year Project\MusicGenerator\Proof Of Concept\recordings.test.aiff'
        # Server.record(path)
        Server.record()
        
    def stopRecording(self):
        self.analyseWave.setEnabled(True)
        self.analyseHandP.setEnabled(True)
        self.analyseSpectogram.setEnabled(True)
        Server.stopRecording()
    
    def displayWaveplot(self):
        directory = r'C:\Users\johnn\anaconda3\Lib\site-packages\FoxDot\rec'
        audio_files = glob(directory + '/*.aiff')
        analysis = Analysis(audio_files[len(audio_files) - 1])
        
        image = analysis.displayWaveGraph()
        image.show()
        
        # label = QLabel(self)

        # pixmap = QPixmap(image)
        
        # label.setPixmap(pixmap)     
        # self.setCentralWidget(label)
        # self.label.move(500, 200)
        
    def displayHarmonicsPercussion(self):
        directory = r'C:\Users\johnn\anaconda3\Lib\site-packages\FoxDot\rec'
        audio_files = glob(directory + '/*.aiff')
        analysis = Analysis(audio_files[len(audio_files) - 1])       
        image = analysis.displayHarmonicsPercussive()
        image.show()
    
    def displaySpectogram(self):
        directory = r'C:\Users\johnn\anaconda3\Lib\site-packages\FoxDot\rec'
        audio_files = glob(directory + '/*.aiff')
        analysis = Analysis(audio_files[len(audio_files) - 1])       
        image = analysis.displaySTFT()
        image.show()
        
    
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
