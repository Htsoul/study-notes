# 爬取b站粉丝的用户名
import requests

url = 'https://api.bilibili.com/x/relation/followers?vmid=420446594&pn=1&ps=20&order=desc'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url,headers=headers)

data = dict(resp.json())
resp.close()
""" with open(file='data.json', mode='w', encoding='utf-8') as f:
    f.write(data)
    f.close() """

for i in data['data']['list']:
    print(i['uname'])


