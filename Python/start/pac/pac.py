import requests

url = 'https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1d'

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
resp = requests.get(url,headers=header)

print(resp)