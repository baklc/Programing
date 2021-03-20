import os, subprocess
from time import sleep
print(os.system('tasklist'))
# os.system('taskkill /f /im python.exe')
while True:
    sleep(2)
    print(os.system('tasklist'))
