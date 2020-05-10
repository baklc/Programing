import shutil
from bs4 import BeautifulSoup
import urllib.request as req
from pytube import YouTube
import glob
import os.path
import sys

from os import rename


urlinput = input("url을 쓰시오")

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


for idd in youtubelist_name:
    indddeex = youtubelist_name.index(idd)
    print("\n|| {}번째 영상 : ".format(indddeex),youtubelist_name[indddeex])

exitdd = input("\n 다운로드 하시겠습니까? Yes || No")
if exitdd == 'No' or 'no' or 'n':
    sys.exit()
lllll = 0
llllll = 0


downloadtype = input("원하는 형식을 쓰시오 || mp4 / mp3")

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

        print("\n||",youtubelist_name[numberlistone], "\n||" ,youtubelist[numberlistone])

        nnnnn = youtubelist[numberlistone]
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