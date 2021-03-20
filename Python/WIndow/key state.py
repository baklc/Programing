from tkinter import *
import keyboard
import win32con, win32api
import tkinter
import tkinter.font
import os
import inspect

def image_change(text_change, text_change2):
    root = Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
    y_plus = (((root.winfo_screenheight() - root.winfo_reqheight()) / 4))
    root.geometry("+%d+%d" % (x, y+y_plus))
    root.geometry("200x200")
    root.wm_attributes("-topmost", 1)
    root.overrideredirect(1)

    canvas = tkinter.Canvas(root, width=200, height=200, highlightthickness=0, borderwidth=0)
    canvas.configure(background="black")

    font1 = tkinter.font.Font(family="배달의민족 주아", size=43)

    canvas.create_arc(0, 0, 70, 70, start=90, fill="gray40", outline="gray40")  # Left, Top # Gray Oval
    canvas.create_oval(130, 0, 200, 70, fill="gray40", outline="gray40")  # Light, Top # Gray Oval
    canvas.create_oval(0, 130, 70, 200, fill="gray40", outline="gray40")  # Left, Bottom # Gray Oval
    canvas.create_oval(130, 130, 200, 200, fill="gray40", outline="gray40")  # Light, Bottom # Gray Oval

    canvas.create_oval(12, 12, 82, 82, fill="black", outline="black")  # Left, Top # Black Oval
    canvas.create_oval(12, 118, 82, 188, fill="black", outline="black")  # Left, Bottom # Black Oval
    canvas.create_oval(118, 12, 188, 82, fill="black", outline="black")  # Light, Top # Black Oval
    canvas.create_oval(118, 118, 188, 188, fill="black", outline="black")  # Light, Bottom # Black Oval

    canvas.create_rectangle(35, 0, 165, 15, fill="gray40", outline="gray40")  # Left to Light, Top # Gray Rectangle
    canvas.create_rectangle(0, 35, 15, 165, fill="gray40", outline="gray40")  # Left, Top to Bottom # Gray Rectangle
    canvas.create_rectangle(185, 35, 200, 165, fill="gray40", outline="gray40")  # Light, Top to Bottom # Gray Rectangle
    canvas.create_rectangle(35, 185, 165, 200, fill="gray40", outline="gray40")  # Left to Light, Bottom # Gray Rectangle

    canvas.create_rectangle(35, 15, 165, 185, fill="black", outline="black")
    canvas.create_rectangle(15, 35, 185, 165, fill="black", outline="black")

    canvas.create_rectangle(15, 92.5, 185, 107.5, fill="gray40", outline="gray40")



    canvas.create_text(100, 150, text=text_change2, font=font1, fill="gray40")

    canvas.master.wm_attributes("-transparentcolor", "black")
    canvas.pack()


    root.after(300, lambda: root.destroy())
    root.mainloop()

def taskkill_func():
    root = Tk()
    root.wm_attributes("-topmost", 1)
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2


    y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2)
    y_plus = (((root.winfo_screenheight() - root.winfo_reqheight()) / 4))
    root.geometry("+%d+%d" % (x, y + y_plus))
    root.geometry("600x200")
    root.resizable(True, True)
    label2 = Label(root, text=inspect.getfile(inspect.currentframe()).replace('/', '\\'))
    label1 = Label(root, text=os.path.basename(inspect.getfile(inspect.currentframe()).replace('/', '\\')))
    label3 = Label(root, text="")
    label4 = Label(root, text="종료하면 num lk, caps lk 안뜸", fg="red")
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    def close():
        root.destroy()
    def exit():
        sys.exit()
    btn1 = Button(root, width=10, text="현재창 종료", command=close)
    btn1.place(x=200, y=150)
    btn2 = Button(root, width=10, text="전체 종료", command=exit)
    btn2.place(x=330, y=150)
    root.mainloop()


while True:
    if keyboard.is_pressed('capslock'):
        caps_status = win32api.GetKeyState(win32con.VK_CAPITAL)
        if caps_status==0:
            print('CapsLock is on')
            image_change("caps lk", "on")
        else:
            print('CapsLock is off')
            image_change("caps lk", "off")
    if keyboard.is_pressed('numlock'):
        num_status = win32api.GetKeyState(win32con.VK_NUMLOCK)
        if num_status==0:
            print('NumLock is on')
            image_change("num lk", "on")
        else:
            print('NumLock is off')
            image_change("num lk", "off")

    if keyboard.is_pressed('ctrl + win + v'):
        taskkill_func()
        print('exit&close tab')
