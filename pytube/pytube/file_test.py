import win32con, win32api, os

file = 'test.txt'
os.remove(file)

f=open(file,'w')
f.write("hello")
f.close()

#make the file hidden
win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_HIDDEN)