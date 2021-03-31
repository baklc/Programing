import requests
url = "http://suninatas.com/challenge/web07/web07.asp"
url2 = "http://suninatas.com/challenge/web07/web07_1.asp"
response=requests.post(url)
response2=requests.post(url2,cookies=response.cookies.get_dict())
print(response2.text)