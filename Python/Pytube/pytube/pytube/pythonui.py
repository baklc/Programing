from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from bs4 import BeautifulSoup
import urllib.request as req
import tkinter.font
import os
import pytube
from pytube import YouTube
import glob

import time

playlistoronelink=0
a = ""
downloaddir=""
youtubelist_name = []
youtubelist=[]
soup =''
titlereplaced= ""

def clear():
    global youtubelist_name, youtubelist, a
    youtubelist.clear()
    youtubelist_name.clear()
    a = ""

root = tkinter.Tk()
root.title("YouTube video/mp3 downloader - kimhyilim")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("600x400"+"+{}+{}".format(positionRight, positionDown))

root.resizable(False, False)
font = tkinter.font.Font(family="배달의민족 주아", size=22)
listfont = tkinter.font.Font(family="배달의민족 주아", size=13)
entryfont = tkinter.font.Font(family="배달의민족 주아",size=15)

def everyinfo(x):
    tkinter.messagebox.showinfo("", x)
    frame1_entry.delete(0, END)
    return

def ifnotopen():
    window1_list.insert(END, "")
    window1_list.insert(END, "***만약 아무것도 안뜬다면 잘못된 URL일 수 있음***")

    window1_list.pack()
    frame1_entry.delete(0, END)
    return

def onemp4ormp3(url):
    YouTube(url).streams.first().download()

def calc(event):
    clear()
    global playlistoronelink
    global a
    global soup, titlereplaced
    titlereplaced =""
    numm = 1
    a = frame1_entry.get()
    print(a)
    window1_list.delete(0, END)

    if 'https://www.youtube.com/' not in a:
        everyinfo("url이 올바르지 않습니다.")


    elif 'https://www.youtube.com' in a:
        if 'playlist' in a:

            playlistoronelink=1

            res = req.urlopen(a)

            soup = BeautifulSoup(res, 'html.parser')


            kkkk = soup.find_all('a',dir='ltr')




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
                llll =("{}: {}".format(numm, i))
                numm += 1
                window1_list.insert(END,llll)
                window1_list.pack()
            nextframe_gonextbutton.config(state='normal')
        elif 'watch' in a:
            res = req.urlopen(a)

            soup = BeautifulSoup(res, 'html.parser')

            playlistoronelink=2
            if soup.find_all('span', id="eow-title"):

                for title in soup.find_all('span', id="eow-title"):
                    titlee = title.get_text('\n')


                titlereplace = titlee.replace('\n    ', '')
                titlereplaced = "{}".format(titlereplace.replace('\n  ', ''))

                window1_list.insert(END,titlereplaced)

                window1_list.pack()
                nextframe_gonextbutton.config(state='normal')
            else:
                ifnotopen()

        else:
            everyinfo("url이 올바르지 않습니다.")
    else:
        everyinfo("url이 올바르지 않습니다.")

def download():
    if playlistoronelink == 1:
        print("def download")


def buttonclicked():
    print(playlistoronelink)

def hide():
    print(playlistoronelink)
    if playlistoronelink != 0:
        frame1_entry.config(state="disable")
        window1.pack_forget()
        window2.pack(fill="x")
    else:
        print("적힌게 없음")

window1=Frame(root,relief="raised")    #첫번째 url입력, 판단 하는 윈도우1
window1.pack()
window1_label=tkinter.Label(window1,height=3,text="URL을 입력하시오",font=font)   #윈도우1:: 맨 위의 info
window1_label.pack(side="top")
window1_frame1=Frame(window1, relief="raised")  #윈도우1:: 입력 프레임1
window1_frame1.pack(side="top")
window1_nextframe1=Frame(window1, relief="raised")  #윈도우1:: 다음 윈도우로 넘어가는 버튼을 담은 프레임2
window1_nextframe1.pack(side="bottom", fill="x")
frame1_entry=tkinter.Entry(window1_frame1, width=40, font=entryfont)  #윈도우1:프레임1:: 입력 entry
frame1_entry.bind("<Return>", calc)
frame1_entry.pack(side="left")
frame1_entryhide=Label(window1_frame1,height=5)
frame1_entryhide.pack(side="top")
window1_list=tkinter.Listbox(window1, height=15, width=100, font=listfont)    #윈도우1:: 유튜브 tktle 리스트
window1_list.pack()
nextframe_gonextbutton = Button(window1_nextframe1, text="next"
    ,font=tkinter.font.Font(family="배달의민족 주아",size=20), relief="groove",state="disable")    #윈도우1:프레임2:: 다음으로 넘어가는 버튼
nextframe_gonextbutton.config(command=lambda: hide())
nextframe_gonextbutton.pack(side="right")












window2=Frame(root, relief="raised")   #저장경로, 파일 형식

def gotowindow1():
    window1_list.delete(0, END)
    frame1_entry.config(state="normal")
    window1.pack()
    window2.pack_forget()
    frame1_entry.delete(0, END)
    global youtubelist_name2,youtubelist_name,youtubelist,mp3ormp4,a,playlistoronelink,downloaddir
    youtubelist=[]
    youtubelist_name2=[]
    youtubelist_name=[]
    mp3ormp4=0
    checkbutton1.deselect()
    checkbutton2.deselect()
    playlistoronelink = 0
    a = ""
    downloaddir = ""
    return
window2_top=Frame(window2, relief="raised")
window2_top.pack(side="top",fill="x")
window2_backtowindow1button=Button(window2_top,text="Home",command=gotowindow1, font=
                      tkinter.font.Font(family="배달의민족 주아",size=30))
window2_backtowindow1button.pack(side="left")
window2_frame1=Frame(window2, relief="raised")
window2_frame1.pack(side="top")
window2_emptylabel2=Label(window2_frame1)
window2_emptylabel2.pack()

window2_frame2=Frame(window2, relief="raised",)
window2_frame2.pack(side="top",fill="y")

window2_emptylabel1=Label(window2_frame2, height=2)
window2_emptylabel1.pack()



youtubelist_name2=youtubelist_name
downloaddir=""
def showdir():
    root.dirName = filedialog.askdirectory()
    print(root.dirName)
    global downloaddir
    downloaddir=root.dirName
    window2_label.config(text=downloaddir)
    window2_label.pack()


window2_button=Button(window2_frame1,text="push",command=showdir)
window2_button.pack(side="right")
window2_label=Label(window2_frame1,width=20,bd=3,relief="groove")
window2_label.pack(side="right")

###mp3, mp4 설정 창
mp3ormp4=0

def defcheck1():
    global mp3ormp4
    checkbutton1.select()
    checkbutton2.deselect()
    mp3ormp4=1

def defcheck2():
    global mp3ormp4
    checkbutton2.select()
    checkbutton1.deselect()
    mp3ormp4=2


checkbutton1=tkinter.Checkbutton(window2_frame2, text="mp3",command=defcheck1)
checkbutton2=tkinter.Checkbutton(window2_frame2, text="mp4",command=defcheck2)



checkbutton1.pack(side="top")
checkbutton2.pack(side="top")
window2_emptylabel3=Label(window2_frame2, height=5)
window2_emptylabel3.pack(side="top")
###download 창

def youtubedownload():
    global titlereplaced
   # print(a)
    print(len(youtubelist_name2))
    lllll=0
    lllllq=0
    if len(youtubelist_name2) != 0:
        print("playlist")
        if mp3ormp4 == 1 and downloaddir:
            print("mp3")
            for listsss in youtubelist_name:
                numberlist = youtubelist_name.index(listsss)

                print(youtubelist_name[numberlist], "\n||", youtubelist[numberlist])

                nnnn = youtubelist[numberlist]
                yt = YouTube(nnnn)
                yt.streams.filter(only_audio=True).first().download(downloaddir)
                lllll += 1
                if len(youtubelist_name) == lllll:
                    break

            specialword = ['\\', '/', ':', '*', '?', "\"", '<', '>', '|']

            for i in youtubelist_name:
                youtubelist_nameindex = youtubelist_name.index(i)
                print(i)
                for ii in specialword:
                    if ii in str(i):
                        incheck = i.replace(ii, '')
                        youtubelist_name[youtubelist_nameindex] = incheck
                        print("True")

            countingnum = 0
            downloaddirreplace = downloaddir.replace('/','\\')+'\\'
            print(downloaddirreplace)
            downloaddirmp3=os.listdir(downloaddir)


            print(youtubelist_name)

            for i in youtubelist_name:
                print(i)
                if i + ".mp3" in downloaddirmp3:
                    continue
                if i + ".mp4" in downloaddirmp3:

                    os.rename(downloaddirreplace + i + ".mp4",
                              downloaddirreplace + i + ".mp3")
                    print("{} converting successful".format(countingnum))
                    countingnum += 1
            print("everything finished")
        elif mp3ormp4 == 2 and downloaddir:
            print("mp4")
            for listsss in youtubelist_name:
                numberlist = youtubelist_name.index(listsss)

                print(youtubelist_name[numberlist], "\n||", youtubelist[numberlist])

                nnnn = youtubelist[numberlist]
                yt = YouTube(nnnn)
                yt.streams.filter().first().download(downloaddir)
                lllllq += 1
                if len(youtubelist_name) == lllllq:
                    break
            print("everything is finished")
        else:
            # print(downloaddir)
            if not downloaddir and mp3ormp4 == 0:
                # print("둘다 선택되지 않음")
                everyinfo("두곳 모드 채워주세요")
            elif mp3ormp4 == 1 or 2 and not downloaddir:
                # print("dir 부분 작성 안됨")
                everyinfo("dir 부분 작성해 주세요")
            else:
                # print("체크박스 체크 안됨")
                everyinfo("체크박스를 체크해주세요")
    elif soup.find_all('span', id="eow-title"):
        print("watch")
        if mp3ormp4 == 1 and downloaddir:
            print("mp3")
            yt = YouTube(a)
            yt.streams.filter(only_audio=True).first().download(downloaddir)

            specialword = ['\\', '/', ':', '*', '?', "\"", '<', '>', '|']

            title = titlereplaced
            print(title)
            for ii in specialword:
                if ii in str(titlereplaced):
                    incheck = titlereplaced.replace(ii, '')
                    titlereplaced = incheck

                    print("True")

            countingnum = 0
            downloaddirreplace = downloaddir.replace('/','\\')+'\\'
            print(downloaddirreplace)
            downloaddirmp3=os.listdir(downloaddir)


            print(youtubelist_name)



            if titlereplaced + ".mp3" in downloaddirmp3:
                return
            if titlereplaced + ".mp4" in downloaddirmp3:
                os.rename(downloaddirreplace + titlereplaced + ".mp4",
                          downloaddirreplace + titlereplaced + ".mp3")
                print("{} converting successful".format(countingnum))
                countingnum += 1

            print("everything is finished")
        elif mp3ormp4 == 2 and downloaddir:
            print("mp4")
            yt = YouTube(a)
            yt.streams.filter().first().download(downloaddir)
            print("everything is finished")
        else:
            # print(downloaddir)
            if not downloaddir and mp3ormp4 == 0:
                # print("둘다 선택되지 않음")
                everyinfo("두곳 모드 채워주세요")
            elif mp3ormp4 == 1 or 2 and not downloaddir:
                # print("dir 부분 작성 안됨")
                everyinfo("dir 부분 작성해 주세요")
            else:
                # print("체크박스 체크 안됨")
                everyinfo("체크박스를 체크해주세요")

            #print(mp3ormp4)

downloadbutton=Button(window2, text="download",command=youtubedownload, font=
                      tkinter.font.Font(size=40))
downloadbutton.pack()

root.mainloop()



#dd