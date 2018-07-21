
import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import numpy as np
from datetime import datetime
import time


# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.pro.coinbase.com/'
#auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

currency_pairs = ['ETH-EUR', 'ETH-BTC', 'BTC-EUR']

class Arbitrage_bot:
    def __init__(self, c_pairs):
        
        self.c_pair1, self.c_pair2, self.c_pair3 = c_pairs
        self.pairs = [self.c_pair1, self.c_pair2,  self.c_pair3]
        
        self.api_url = 'https://api.pro.coinbase.com/'
        #self.auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)
    
    def bid_ask_quotes(self):
        
        price_arrays = []

        for x in self.pairs:
            quotes = requests.get(api_url + '/products/{}/book'.format(x)).json()
            price_arrays.append(np.array([[quotes["bids"][0][0],quotes["asks"][0][0]]], dtype=float))

        return price_arrays

    def cross_rate_perc(self):
        pair1, pair2, pair3 = self.bid_ask_quotes()

        cross_rate = np.multiply(pair2, pair3)

        return ((cross_rate/pair1) - 1)*100, cross_rate, pair1, datetime.now().isoformat(timespec='microseconds')


test = Arbitrage_bot(currency_pairs)
count= 0
while True:
    
    while True:
        try:
            with open("test3.txt", "a") as f:
                cross_per, cross_rate, pair1, timer = test.cross_rate_perc()


                f.write("{},{},{},{},{},{},{}\n".format(
                    timer,
                    cross_per[0,0],
                    cross_per[0,1],
                    cross_rate[0,0],
                    cross_rate[0,1],
                    pair1[0,0],
                    pair1[0,1],
                    )
                )
            count +=1

        except:
            print("Fuck, they got me!")
        
            
            
            
            
            time.sleep(10)
        print(count)





    









