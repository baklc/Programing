from bs4 import BeautifulSoup
import requests
import urllib.request as req
def urlinput(urlnum):
    url = 'https://www.yongin.ms.kr/b2520.brd/0'+str(urlnum)+'..71ba9f4?shell=/index.shell:11'
    res = req.urlopen(url)

    soup = BeautifulSoup(res, 'html.parser')
    llss = []
    soupp = soup.find_all('script')
    checksoup = soupp[11]
    for i in checksoup:
        for ii in i:
            llss.append(ii)
    llssjoin = ''.join(llss)
    llsssplit = llssjoin.split('\n')
    for i in llsssplit:
        if '	' in i:
            if '[[' in i:
                print('-------------------')
                repl = i.replace('\t','')

                listindex = repl.find('"","",""],"')
                listindexx = repl.find('shell')
                deltext = repl[listindex:len(repl)]
                deltexttwo = repl[0:listindexx]
                delfinishtext = repl.replace(deltexttwo+'shell=/index.shell:11","","','')
                llast = deltext.replace('"","",""],"','')
                delfinishtexttwo = delfinishtext.replace('\\n',' ')
                last = delfinishtexttwo[0:1]

                if llast == ',':
                    print('can\'t find')

                else:
                    print(llast.replace('"],','').replace('"]];',''))

                if last == ' ':
                    print(delfinishtexttwo[1:31])
                else:
                    print(delfinishtexttwo[0:30])
for i in range(1,8):
    print('\n\n\n'+str(i)+'page\n')
    urlinput(i)