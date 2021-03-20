import os
import smtplib
import filemanager
from email.mime.text import MIMEText

def main():
    countnum = 0
    sender = 'telegrambotkhl@gmail.com'
    receiver = 'bloodmoon0915@gmail.com'
    password = 'khltelegrambot1225'

    log = open(filemanager.getlogfilepath(filemanager.getlogfilename()), mode='r', encoding='utf-8').read()
    msg = MIMEText(log)
    msg['Subject'] = filemanager.getlogfilename() + str(countnum)
    msg['To'] = receiver


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)

    server.sendmail(sender, receiver, msg.as_string())

    server.quit()
    print('mail_sent')
    os.remove(filemanager.getlogfilepath(filemanager.getlogfilename()))
    countnum =+ 1