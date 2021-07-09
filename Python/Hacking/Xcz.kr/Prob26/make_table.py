import requests
file = open("strings.txt","w")
url="http://xcz.kr/START/prob/prob26.php"
cookie={'PHPSESSID':'xxxxxxxxxxxxxxxxxxxxxxxxxx'}
for j in range(32,127):
    for k in range(32, 127):
        n=chr(j)+chr(k)
        r=requests.post(url,cookies=cookie,data={'encode':n,'submit':'submit'})
        t=r.text
        l=(t[t.find("ENCODE"):t.find('</font></br></br>')])
        file.write(n+" "+l)
file.close()