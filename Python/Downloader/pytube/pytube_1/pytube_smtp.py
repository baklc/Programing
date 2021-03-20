import time
import os
from pytube import YouTube
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re

countnum = 0
email_user = ''
email_send = ''
email_password = ''
def youtubedownloader(url):

    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download()

    filename = re.sub("[\/:*?\"<>|.]", "", str(yt.title))

    directory = os.getcwd()
    print(filename)
    filepath = (directory + "\\" + filename + ".mp3")
    renamefilepath = directory + "\\" + yt.title + ".mp4"

    try:
        os.rename(renamefilepath, filepath)
    except:
        pass
    print('successful rename')

    return [filename, filepath]


def mailsend(filename, filepath):

    subject = filename

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # 본문 내용 입력
    body = "youtube audio downloader"
    msg.attach(MIMEText(body,'plain'))

    ############### ↓ 첨부파일이 없다면 삭제 가능  ↓ ########################
    # 첨부파일 경로/이름 지정하기
    filename= filepath
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment", filename= os.path.basename(filename))
    msg.attach(part)
    ############### ↑ 첨부파일이 없다면 삭제 가능  ↑ ########################

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()
    print('mail sent')
    time.sleep(2)
    os.remove(filepath)

writeurl = input("url을 적으시오")
downloadlist = youtubedownloader(writeurl)
filename1 = downloadlist[0]
filepath1 = downloadlist[1]
print(filename1)
print(filepath1)
mailsend(filename1,filepath1)