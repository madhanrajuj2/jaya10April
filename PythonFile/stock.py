import urllib2
import json
import time

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    
    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        u = urllib2.urlopen(url)
        content = u.read()
        
        obj = json.loads(content[3:])
        return obj[0]
        
        
if __name__ == "__main__":
    c = GoogleFinanceAPI()
    
    while 1:
        quote = c.get("MSFT","NASDAQ") #NSE:RELIANCE
        print quote
        time.sleep(30)
		
#https://www.quora.com/Is-there-a-real-time-stock-market-data-feed-API-for-NSE-BSE-Mcx-to-implement-in-our-custom-software
#http://digitalpbk.com/stock/google-finance-get-stock-quote-realtime