import requests
import json
apiKey = 'c010don48v6sc26qk7s0'

symbol = 'AAPL'
print('hello')
r = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=' + symbol +'&token=' + apiKey)

r = requests.get('https://finnhub.io/api/v1/search?q=AAPL&token=c010don48v6sc26qk7s0')

x = json.loads(r.text)

print(x['result'][0]['description'])


class Requests():
    def __init__(self, code, params={}):
        self.params = params
        self.url = 'https://finnhub.io/api/v1/'
        self.code = code.upper()
        self.apiKey = 'c010don48v6sc26qk7s0'

    def getName(self):
        r = requests.get(self.url + 'search?q=' + self.code + '&token=' + self.apiKey)
        lod = json.loads(r.text)
        return lod['result'][0]['description'].split()[0]

        def getCode(self):
            r = requests.get(self.url + 'search?q=' + self.code + '&token=' + self.apiKey)
            lod = json.loads(r.text)
            return lod['result'][0]['displaySymbol']