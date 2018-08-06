#Modules
import requests
import json
import pandas as ps

class Bitfinex_Pub:
    
    def __init__(self):
        '''Tradeable base currencies'''
        self.base = ["btc", "eth"]
        self.fiat = ["JPY", "EUR", "USD", "GBP"]
        self.url1 = "https://api.bitfinex.com/v1/"
        self.url = "https://api.bitfinex.com/v2/"
    def symbols(self): 
        '''Get list of current pairs
           Ratelimit: 5 req/min'''      
        param = "symbols"
        response = requests.request("GET", self.url1 + param)
        response = json.loads(response.text)
        response_new = []
        
        #find more elegant solution to exclude fiat currency pairs
        for pair in response:
            if "jpy" in pair or "eur" in pair or "usd" in pair or "GBP" in pair:
                pass
            else:
                response_new.append(pair)
        return response_new

    def symbols_v2(self):
        '''Prepare symbols for v2 api-> add t to pairs string '''
        symbols_2 = []
        data = self.symbols()
        
        for pair in data:
            symbols_2.append("t" + pair.upper())
            
        symbols_2 = ",".join(symbols_2)
        return symbols_2
    
    def tickers(self, c_pairs):
        '''Get current market data on currency pairs'''
        param = "tickers?symbols=" 
        response = requests.request("GET", self.url + param + c_pairs ) 
        return response.text