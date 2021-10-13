import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Window(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Stopwatch.")
        self.setGeometry(100,100,800,800)
        self.uiComponents()
        self.show()
    
    def uiComponents(self):
        self.count = 0
        self.flag = False
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,500)
        self.label.setStyleSheet("border : 6px solid red")
        self.label.setText(str(self.count))
        self.label.setFont(QFont('Arial',125))
        self.label.setAlignment(Qt.AlignCenter)
        #Start Button
        start = QPushButton("Start" , self)
        start.setGeometry(0,500,800,100)
        start.pressed.connect(self.Start)
            #Pause Button
        pause = QPushButton("Pause" , self)
        pause.setGeometry(0,600,800,100)
        pause.pressed.connect(self.Pause)
            #Rest Button
        reset = QPushButton("Reset" ,self)
        reset.setGeometry(0,700,800,100)
        reset.pressed.connect(self.Reset)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(10)



    def showTime(self) :
        if self.flag :
            self.count += 1
        text = str(self.count/100)
        self.label.setText(text)
        
    def Start(self) :
        self.flag = True
    def Pause(self) :
        self.flag = False
    def Reset(self) :
        self.count = 0
        self.flag = False
        self.label.setText(str(self.count))
   


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())