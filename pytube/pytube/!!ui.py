import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import urllib.request as req
from pytube import YouTube
import glob
import os
import win32con, win32api



#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("untitled.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
        self.lineedit_Test.returnPressed.connect(self.printTextFunction)

    #btn_1이 눌리면 작동할 함수
    def button1Function(self) :
        print("btn_1 Clicked")

    #btn_2가 눌리면 작동할 함수
    def button2Function(self) :
        print("btn_2 Clicked")

    def printTextFunction(self) :
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        numddd = self.lineedit_Test.text()

        file = 'test.txt'
        os.remove(file)
        f = open(file, 'w')
        f.write(numddd)
        f.close()


        win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_HIDDEN)




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


file = 'test.txt'
f = open(file, 'r')
line = f.readline()
print(line)
f.close()

