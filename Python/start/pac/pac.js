const http = require('http')
url = 'https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1d'
http.request(url,(req,res)=>{
    console.log(res);
})