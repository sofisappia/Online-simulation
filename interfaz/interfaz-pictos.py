#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap 
from PyQt5.QtCore import pyqtSlot, Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(800, 900)
        self.center()
        
        self.setWindowTitle('Interfaz')

        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.setStyleSheet('background-color: black')
        self.show()
        
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)
        layout.setRowStretch(0,5)
        layout.setRowStretch(1,5)
        

    # Create widget
        label01 = QLabel(self)
        pixmap = QPixmap('image01.PNG')
        pixmap.scaled(20,25, aspectRatioMode = Qt.IgnoreAspectRatio)
        label01.setPixmap(pixmap)
        label01.setFixedSize(450,400)
        label01.setAlignment(Qt.AlignCenter)
        label01.setStyleSheet('background-color: gray')
        
        label02 = QLabel(self)
        pixmap02 = QPixmap('image02.PNG') 
        pixmap02.scaled(20,25, aspectRatioMode = Qt.IgnoreAspectRatio)
        label02.setFixedSize(450,400)
        label02.setAlignment(Qt.AlignCenter)
        label02.setPixmap(pixmap02)
        label02.setStyleSheet('background-color: gray')

        
        label03 = QLabel(self)
        pixmap03 = QPixmap('image04.PNG')
        pixmap03.scaled(20,25, aspectRatioMode = Qt.IgnoreAspectRatio)
        label03.setFixedSize(450,400)
        label03.setAlignment(Qt.AlignCenter)
        label03.setPixmap(pixmap03)

        
        label04 = QLabel(self)
        pixmap04 = QPixmap('image03.PNG')
        label04.setFixedSize(450,400)
        label04.setAlignment(Qt.AlignCenter)
        label04.setPixmap(pixmap04)
        
        layout.addWidget(label01,0,0) 
        layout.addWidget(label02,0,1) 
        layout.addWidget(label03,1,0) 
        layout.addWidget(label04,1,1) 
     
 
        self.horizontalGroupBox.setLayout(layout)
    
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
