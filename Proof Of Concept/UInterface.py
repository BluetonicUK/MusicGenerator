# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:27:18 2021

@author: johnn
"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from FoxDot1 import *
from FoxDot import *



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Music Generator")
window.setFixedSize(500, 600)
window.setStyleSheet("background: #161219; ")


grid = QGridLayout()




def clickPlay():
    player()

def clickStop(self):
    Clock.clear()

def startRecording(self):
    Server.record()
    


def display():
    #display logo
    image = QPixmap("logo/logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignTop)
    logo.setStyleSheet("margin-left: 135px;")
    

    playButton = createButton("Play")
    stopButton = createButton("Stop")
    recordButton = createButton("Record")
    stopRecordButton = createButton("Stop Recording")
    wavePlotButton = createButton("WavePlot")
    spectogramButton = createButton("Spectogram")
    harmonicsButton = createButton("Harmonics and Percussive")
    
    playButton.clicked.connect(clickPlay)
    stopButton.clicked.connect(clickStop)
    #playButton.setEnabled(False)
                         

    grid.addWidget(logo, 0, 0)
    grid.addWidget(playButton, 1, 0)
    grid.addWidget(stopButton, 2, 0)
    grid.addWidget(recordButton, 3, 0)
    grid.addWidget(stopRecordButton, 4, 0)
    grid.addWidget(wavePlotButton, 5, 0)
    grid.addWidget(spectogramButton, 6, 0)
    grid.addWidget(harmonicsButton, 7, 0)
    
def createButton(text):
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet("border: 2px solid '#9d07de';" +
                     "border-radius: 15px;" + 
                     "font-size: 20px;" + 
                     "color: 'white'; " + 
                     "padding: 10px 0;}" +                     
                     "*:hover{background: #9d07de;}"
                     )
    return button


def show():
    display()
    window.setLayout(grid)
    window.show()
    sys.exit(app.exec())
    
show()




                     
