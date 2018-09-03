#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Timer, Thread, Event
import threading
import sys, time, random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import (pyqtSlot, Qt, QByteArray, QPropertyAnimation,
                          pyqtProperty, QState,QStateMachine)


class App(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.label01
        self.label02
        self.label03
        self.label04
        
    def initUI(self):               
        
        self.resize(800, 900)
        self.center()
        
        self.setWindowTitle('Interfaz')
        self.setStyleSheet('background-color: black')
        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)

        self.setLayout(windowLayout)
        #self.set_label_bkg(self.label01, 'white')
        self.show()

    def createImgWidget(self, img):
        label = QLabel(self)
        pixmap = QPixmap(img)
        pixmap.scaled(20,25, aspectRatioMode = Qt.IgnoreAspectRatio)
        label.setPixmap(pixmap)
        label.setFixedSize(450,400)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('background-color: black')
        return label

        
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)
        layout.setRowStretch(0,5)
        layout.setRowStretch(1,5)
        
        self.label01 = self.createImgWidget('image01.PNG')
        self.label02 = self.createImgWidget('image02.PNG')
        self.label03 = self.createImgWidget('image04.PNG')
        self.label04 = self.createImgWidget('image03.PNG')
        

        layout.addWidget(self.label01,0,0) 
        layout.addWidget(self.label02,0,1) 
        layout.addWidget(self.label03,1,0) 
        layout.addWidget(self.label04,1,1) 
     
 
        self.horizontalGroupBox.setLayout(layout)
    
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_label_bkg(self, label, color):
        bg_color = 'background-color: '+color
        label.setStyleSheet(bg_color)

    def animate(self):
        threading.Thread(target=self.animate_).start()

    def animate_(self):
        img_idx = [1, 2, 3, 4]
        th = Event()
        th.wait(2)
        #filename = 
        file = open('trial_00.txt', 'w')
        file.write(datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))

        for img in range(4): # target picto
            if(img == 0):
                self.set_label_bkg(self.label01, 'blue')
                th.wait(1.5)
                self.set_label_bkg(self.label01, 'black')
            elif(img == 1):
                self.set_label_bkg(self.label02, 'blue')
                th.wait(1.5)
                self.set_label_bkg(self.label02, 'black')
            elif(img == 2):
                self.set_label_bkg(self.label03, 'blue')
                th.wait(1.5)
                self.set_label_bkg(self.label03, 'black')
            elif(img == 3):
                self.set_label_bkg(self.label04, 'blue')
                th.wait(1.5)
                self.set_label_bkg(self.label04, 'black')

            for rep in range(2): #repetitions
                random.shuffle(img_idx)
                for i in range(len(img_idx)): #Trial
                    if(img_idx[i] == 1):
                        self.set_label_bkg(self.label01, 'white')
                        th.wait(0.25)
                        self.set_label_bkg(self.label01, 'black')
                        th.wait(0.075)
                    elif(img_idx[i] == 2):
                        self.set_label_bkg(self.label02, 'white')
                        th.wait(0.25)
                        self.set_label_bkg(self.label02, 'black')
                        th.wait(0.075)
                    elif(img_idx[i] == 3):
                        self.set_label_bkg(self.label03, 'white')
                        th.wait(0.25)
                        self.set_label_bkg(self.label03, 'black')
                        th.wait(0.075)
                    elif(img_idx[i] == 4):
                        self.set_label_bkg(self.label04, 'white')
                        th.wait(0.25)
                        self.set_label_bkg(self.label04, 'black')
                        th.wait(0.075)
            th.wait(2.5) #blank matrix          
      
        file.close()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    ex.animate()
    
    sys.exit(app.exec_())
