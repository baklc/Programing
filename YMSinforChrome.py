
from multiprocessing import Pool
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip


options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe',options=options)
driver.implicitly_wait(2)

def yonginmiddle(urlnumber):


    alltextlist=[]
    checklist = []
    textchecklist = []
    numm=1

    driver.get('https://www.yongin.ms.kr/b2520.brd/0'+str(urlnumber)+'..196c4ed9?shell=/index.shell:11')

    print(urlnumber,'페이지')

    a = driver.find_elements_by_class_name('cell4pline')

    for i in a:
        checklist.append(i.text)


    for i in checklist:
        if i == '':
            del checklist[checklist.index(i)]


    for i in checklist:
        if len(i) > 10:
            textchecklist.append(i)
        else:
            continue

    for i in textchecklist:
        maybealltext = str(urlnumber)+'페이지'+str(numm)+'번째 게시물'+i
        print(maybealltext)
        alltextlist.append(maybealltext)
        numm += 1
    urlnumber += 1
    if not textchecklist:
        print('empty')
    else:
        print('not empty')
    print(alltextlist)

    driver.close()
    return alltextlist

if __name__ == '__main__':
    globallist = []

    urlnumberlist = []
    start = time.time()

    driver.get('https://www.yongin.ms.kr/b2520.brd/01..196c4ed9?shell=/index.shell:11')

    add = driver.find_elements_by_class_name('pg_menu')

    print(len(add))
    for i in range(1, len(add) + 1):
        urlnumberlist.append(i)

    print(urlnumberlist)
    pool = Pool(processes=len(add))
    globallist.append(pool.map(yonginmiddle,urlnumberlist))
    pool.close()
    pool.join()
    print('end')
    print("time :", time.time() - start)
    for i in globallist:
        for l in i:
            print('||||||\n\n\n')
            for ll in l:
                print(ll)