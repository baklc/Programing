import shutil
from bs4 import BeautifulSoup
import urllib.request as req
from pytube import YouTube
import glob
import os.path

from os import rename


urlinput = input("url을 쓰시오")
downloadtype = input("원하는 형식을 쓰시오 || mp4 / mp3")

url = urlinput
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

kkkk = soup.find_all('a',dir='ltr')

a = soup.find_all("a")
gggg = soup.find_all("a")
youtubelist = []
youtubelist_name = []
for i in kkkk:

    href = i.attrs['href']
    text = i.string

    replaceAll = text.replace("\n      ", "")
    replaceAlltwo = replaceAll.replace("\n    ", "")

    # print("https://youtube.com"+href)
    if 'watch' in href:
        youtubelist.append("https://www.youtube/"+href)
        youtubelist_name.append(replaceAlltwo)


lllll = 0
llllll = 0
if downloadtype == "mp3":
    for listsss in youtubelist_name:
        numberlist = youtubelist_name.index(listsss)

        print(youtubelist_name[numberlist], "\n||"  ,youtubelist[numberlist])

        nnnn = youtubelist[numberlist]
        yt = YouTube(nnnn)
        yt.streams.filter(only_audio=True).first().download()
        lllll += 1
        if len(youtubelist_name) == lllll:
            break
else :
    for listssss in youtubelist_name:
        numberlistone = youtubelist_name.index(listssss)

        print(youtubelist_name[numberlistone], "\n||" ,youtubelist[numberlistone])

        nnnnn = youtubelist[numberlistone]
        print(nnnnn)
        YouTube(nnnnn).streams.first().download()
        if len(youtubelist_name) == llllll:
            break

countingnum = 0

files = glob.glob("*.mp4")

if downloadtype == "mp3":
    for x in files:
        if not os.path.isdir(x):
            filename = os.path.splitext(x)
            try:
                os.rename(x,filename[0] + '.mp3')
            except:
                pass

        print("{} converting successful".format(countingnum))
        countingnum += 1