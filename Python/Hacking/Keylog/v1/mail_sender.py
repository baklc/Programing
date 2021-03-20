import smtplib
import filemanager
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def main():
    sender = '' #Bot_Email
    receiver = '' #My_Email
    username = 'telegrambot'
    password = 'telegrambot'

    subject = 'hello'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # 본문 내용 입력
    body = 'helloddd'
    msg.attach(MIMEText(body, 'plain'))

    log = open(filemanager.getlogfilepath(filemanager.getlogfilename()), mode='r', encoding='utf-8').read().encode()


    ############### ↓ 첨부파일이 없다면 삭제 가능  ↓ ########################
    # 첨부파일 경로/이름 지정하기
    filename = filemanager.getlogfilepath(filemanager.getlogfilename())
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)

    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)

    server.sendmail(sender, receiver, text)
    server.quit()
    print('fdsfds')