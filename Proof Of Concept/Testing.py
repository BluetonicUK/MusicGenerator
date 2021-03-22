# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:27:18 2021

@author: johnn
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from FoxDot1 import *
from FoxDot import *






class Testing(QMainWindow):
    
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Music Generator")
    window.setFixedSize(500, 600)
    window.setStyleSheet("background: #161219; ")
    
    
    grid = QGridLayout()
    
    def __init__(self):
        super(Testing, self).__init__()
        self.window = QWidget()
        self.window.setWindowTitle("Music Generator")
        self.window.setFixedSize(500, 600)
        self.window.setStyleSheet("background: #161219; ")
        
        
        
        
        self.display()
        
        


    def clickPlay(self):
        player()
    
    def clickStop(self):
        Clock.clear()
    
    def startRecording(self):
        Server.record()

    
    
    
    def display(self):
        
        self.grid = QGridLayout()
        #display logo
        image = QPixmap("logo/logo.png")
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignTop)
        logo.setStyleSheet("margin-left: 135px;")
        
    
        self.playButton = createButton("Play")
        self.stopButton = createButton("Stop")
        self.recordButton = createButton("Record")
        self.stopRecordButton = createButton("Stop Recording")
        self.wavePlotButton = createButton("WavePlot")
        self.spectogramButton = createButton("Spectogram")
        self.harmonicsButton = createButton("Harmonics and Percussive")
        
        self.playButton.clicked.connect(self.clickPlay)
        self.stopButton.clicked.connect(self.clickStop)
        #playButton.setEnabled(False)
                             
    
        self.grid.addWidget(logo, 0, 0)
        self.grid.addWidget(self.playButton, 1, 0)
        self.grid.addWidget(self.stopButton, 2, 0)
        self.grid.addWidget(self.recordButton, 3, 0)
        self.grid.addWidget(self.stopRecordButton, 4, 0)
        self.grid.addWidget(self.wavePlotButton, 5, 0)
        self.grid.addWidget(self.spectogramButton, 6, 0)
        self.grid.addWidget(self.harmonicsButton, 7, 0)
        
        return self.grid
        
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

    window = Testing()
    app = QApplication(sys.argv)
    grid = window.display()
    window.setLayout(grid)
    window.show()
    sys.exit(app.exec())
    
show()




                     
