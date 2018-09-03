#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Timer, Thread, Event
import threading
import sys, time, random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPalette, QFont
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

        self.time_ON = 0.1
        self.time_OFF = 0.075
        
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

    def createImgWidget(self, letter):
        label = QLabel(self)
        label.setText(letter)
        palette = QPalette()
        palette.setColor(QPalette.Text, Qt.gray)
        label.setPalette(palette)
        font = QFont("Times", 50, QFont.Bold)
        label.setFont(font)
        label.setFixedSize(400,400)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('background-color: gray')
        return label

        
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 2)
        layout.setRowStretch(0,5)
        layout.setRowStretch(1,5)
        
        self.label01 = self.createImgWidget('A')
        self.label02 = self.createImgWidget('B')
        self.label03 = self.createImgWidget('C')
        self.label04 = self.createImgWidget('D')
        

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

    def set_label_bkg(self, label, color, font_size):
        bg_color = 'background-color: '+color
        palette = QPalette()
        label.setStyleSheet(bg_color)
        palette.setColor(QPalette.Text, Qt.white)
        label.setPalette(palette)
        font = QFont("Times", font_size, QFont.Bold)
        label.setFont(font)

    def animate(self):
        threading.Thread(target=self.animate_).start()

    def animate_(self):
        ''' Print markers in "time,flashing,stim_code,stim_type" fashion
            flashing: 1 if matrix ON, 0 otherwise
            stim_code: number of picto flashing (1-4), 0 if no picto flashing
            stim_type: 1 if target flashing, 0 otherwise'''
        img_idx = [1, 2, 3, 4]
        th = Event()
        th.wait(2)
        #filename = 
        file = open('trial_00.txt', 'w')
        file.write(datetime.now().strftime("%a, %d %B %Y %H:%M:%S")+'\n')

        for img in range(4): # target picto
           # file.write('Target picto: ' + str(img+1)+' '+datetime.now().strftime('%H:%M:%S.%f')[:-5]+'\n')
            if(img == 0):
                self.set_label_bkg(self.label01, 'blue', 50)
                th.wait(1.5)
                self.set_label_bkg(self.label01, 'gray', 50)
            elif(img == 1):
                self.set_label_bkg(self.label02, 'blue', 50)
                th.wait(1.5)
                self.set_label_bkg(self.label02, 'gray', 50)
            elif(img == 2):
                self.set_label_bkg(self.label03, 'blue', 50)
                th.wait(1.5)
                self.set_label_bkg(self.label03, 'gray', 50)
            elif(img == 3):
                self.set_label_bkg(self.label04, 'blue', 50)
                th.wait(1.5)
                self.set_label_bkg(self.label04, 'gray', 50)

            for rep in range(10): #repetitions
                random.shuffle(img_idx)
                for i in range(len(img_idx)): #Trial
                    if(img_idx[i] == 1):
                        self.set_label_bkg(self.label01, 'white', 150)
                        if img+1  == 1:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,1,1'+'\n')
                        else:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,1,0'+'\n')
                        th.wait(self.time_ON )
                        self.set_label_bkg(self.label01, 'gray', 50)
                        file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',0,0,0'+'\n')
                        th.wait(self.time_OFF)
                    elif(img_idx[i] == 2):
                        self.set_label_bkg(self.label02, 'white', 150)
                        if img+1 == 2:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,2,1'+'\n')
                        else:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,2,0'+'\n')
                        th.wait(self.time_ON )
                        self.set_label_bkg(self.label02, 'gray', 50)
                        file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',0,0,0'+'\n')
                        th.wait(self.time_OFF)
                    elif(img_idx[i] == 3):
                        self.set_label_bkg(self.label03, 'white', 150)
                        if img+1 == 3:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,3,1'+'\n')
                        else:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,3,0'+'\n')                        
                        th.wait(self.time_ON )
                        self.set_label_bkg(self.label03, 'gray', 50)
                        file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',0,0,0'+'\n')
                        th.wait(self.time_OFF)
                    elif(img_idx[i] == 4):
                        self.set_label_bkg(self.label04, 'white', 150)
                        if img+1 == 4:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,4,1'+'\n')
                        else:
                            file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',1,4,0'+'\n')                        
                        th.wait(self.time_ON )
                        self.set_label_bkg(self.label04, 'gray', 50)
                        file.write(datetime.now().strftime('%H:%M:%S.%f')[:-5]+',0,0,0'+'\n')
                        th.wait(self.time_OFF)
            th.wait(2.5) #blank matrix          
      
        file.close()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    ex.animate()
    
    sys.exit(app.exec_())
