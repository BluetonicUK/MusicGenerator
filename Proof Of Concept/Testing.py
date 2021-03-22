# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:27:18 2021

@author: johnn
"""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot

from FoxDot1 import *
from FoxDot import *


class CostumWindow(QWidget):
    def __init__(self):
        # Inherit the constructor of QWidget
        super().__init__()

        # Initialices the UI
        self.initUI()
        self.set_layout()

    def initUI(self):
        # Costumize the app
        self.setWindowTitle("Music Generator")
        self.setFixedSize(500, 600)
        self.setStyleSheet("background: #161219; ")

        # Initialize the logo
        image = QPixmap("logo/logo.png")
        self.logo = QLabel()
        self.logo.setPixmap(image)
        self.logo.setAlignment(QtCore.Qt.AlignTop)
        self.logo.setStyleSheet("margin-left: 135px;")

        # Initialize the buttons
        self.playButton = self.createButton("Play")
        self.stopButton = self.createButton("Stop")
        self.recordButton = self.createButton("Record")
        self.stopRecordButton = self.createButton("Stop Recording")
        self.wavePlotButton = self.createButton("WavePlot")
        self.spectogramButton = self.createButton("Spectogram")
        self.harmonicsButton = self.createButton("Harmonics and Percussive")

        # Connect buttons to their function
        self.playButton.clicked.connect(self.clickPlay)
        self.stopButton.clicked.connect(self.clickStop)
        # self.playButton.setEnabled(False)

    def set_layout(self):
        # Set layout
        self.grid = QGridLayout()

        self.grid.addWidget(self.logo, 0, 0)
        self.grid.addWidget(self.playButton, 1, 0)
        self.grid.addWidget(self.stopButton, 2, 0)
        self.grid.addWidget(self.recordButton, 3, 0)
        self.grid.addWidget(self.stopRecordButton, 4, 0)
        self.grid.addWidget(self.wavePlotButton, 5, 0)
        self.grid.addWidget(self.spectogramButton, 6, 0)
        self.grid.addWidget(self.harmonicsButton, 7, 0)

        # Use the grid as the app layout
        self.setLayout(self.grid)

    @staticmethod
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

    @pyqtSlot()
    def clickPlay(self):
        player()

    @pyqtSlot()
    def clickStop(self):
        Clock.clear()

    def startRecording(self):
        Server.record()


def main():
    app = QApplication(sys.argv)
    window = CostumWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
