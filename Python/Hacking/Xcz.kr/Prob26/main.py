import requests
url="http://xcz.kr/START/prob/prob26.php"
cookie={'PHPSESSID':'asmpopirigsnh6f1j4mcnnlk80'}
file=open("split4_C","r")
file1=open("strings.txt","r")
ch=open("str_ch","r").readlines()
cr=open("str_cr","r").readlines()
l=file.readlines()
result=[]
c="$(@P"
for i in cr:
    tr=0
    if i[:2]==c[:2]:
        # print(ch[cr.index(i)][:2]+" "+i,end="")
        for j in range(32, 127):
            n=(ch[cr.index(i)][:2])+chr(j)
            r = requests.post(url, cookies=cookie, data={'encode': n, 'submit': 'submit'})
            t = r.text
            l = (t[t.find("ENCODE"):t.find('</font></br></br>')])
            if l.find(c[:4])>0:
                result.append(ch[cr.index(i)][:2]+chr(j))
                print(l)
                print(ch[cr.index(i)][:2]+chr(j)[:3])
                tr=1
                break
    if tr==1:
        break

for i in result:
    print(i[:3],end="")