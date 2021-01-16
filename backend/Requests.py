import requests
apiKey = 'c010don48v6sc26qk7s0'

symbol = 'AAPL'

r = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=' + symbol +'&token=' + apiKey)

print(r.json())