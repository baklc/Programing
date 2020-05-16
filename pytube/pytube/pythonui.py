from tkinter import *
import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup
import urllib.request as req
import tkinter.font

import pytube
from pytube import YouTube

import time
playlistoronelink=0
a = ""

root = tkinter.Tk()
root.title("YUN DAE HEE")
root.geometry("640x480+100+100")
root.resizable(False, False)
font = tkinter.font.Font(family="배달의민족 주아", size=20)
listfont = tkinter.font.Font(family="배달의민족 주아", size=10)
entryfont = tkinter.font.Font(size=10)

def urlnottrue():
    print("다시입력하시오")
    tkinter.messagebox.showinfo("", "url이 올바르지 않습니다.")
    entry.delete(0, END)
    return

def ifnotopen():
    llist.insert(END, "")
    llist.insert(END, "***만약 아무것도 안뜬다면 잘못된 URL일 수 있음***")

    llist.pack()
    entry.delete(0, END)
    return

def onemp4ormp3(url):
    YouTube(url).streams.first().download()

def calc(event):
    youtubelist = []

    youtubelist_name = []

    global a
    numm = 1
    a = entry.get()
    print(a)
    llist.delete(0,END)

    if 'https://www.youtube.com/' not in a:
        urlnottrue()


    elif 'https://www.youtube.com' in a:
        if 'playlist' in a:

            playlistoronelink=1

            res = req.urlopen(a)

            soup = BeautifulSoup(res, 'html.parser')


            kkkk = soup.find_all('a',dir='ltr')

            a = soup.find_all("a")
            gggg = soup.find_all("a")

            for i in kkkk:

                href = i.attrs['href']
                text = i.string

                replaceAll = text.replace("\n      ", "")
                replaceAlltwo = replaceAll.replace("\n    ", "")

                # print("https://youtube.com"+href)
                if 'watch' in href:
                    youtubelist.append("https://www.youtube/"+href)
                    youtubelist_name.append(replaceAlltwo)
            if len(youtubelist_name) == 0:
                ifnotopen()


            for i in youtubelist_name:
                print("{}: {}".format(numm, i))
                numm += 1
            listchecknum=1
            for i in youtubelist_name:
                listname = "{} : {}".format(listchecknum,i)
                llist.insert(END,listname)
                listchecknum= listchecknum + 1
            llist.pack()
        elif 'watch' in a:
            res = req.urlopen(a)

            soup = BeautifulSoup(res, 'html.parser')

            playlistoronelink=2
            if soup.find_all('span', id="eow-title"):

                for title in soup.find_all('span', id="eow-title"):
                    titlee = title.get_text('\n')


                titlereplace = titlee.replace('\n    ', '')


                llist.insert(END,titlereplace)
                llist.pack()
            else:
                ifnotopen()

        else:
            urlnottrue()
    else:
        urlnottrue()

def download():
    if playlistoronelink == 1:
        print("def download")


def buttonclicked():
    print(playlistoronelink)


label=tkinter.Label(root,width=10,height=3,text="URL을 입력하시오",font=font)
label.grid()

entry=tkinter.Entry(root,width=10,font=entryfont)
entry.bind("<Return>", calc)
entry.grid()


button2= tkinter.Button(root,text="push",overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
button2.grid()


llist=tkinter.Listbox(root,height=6,width=100,font=listfont)
llist.grid()

button = tkinter.Button(root, overrelief="solid", width=15, command=buttonclicked, repeatdelay=1000, repeatinterval=100)

button.grid()



root.mainloop()



