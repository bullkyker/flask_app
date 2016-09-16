from pandas.io.data import DataReader
#from pandas_datareader import data, wb
from googlefinance import getQuotes
import json
from datetime import datetime
import pandas 
import time
import urllib.request
import urllib
import re
	
stocks = ["GIB","AAPL", "GOOG", "TSLA", "AEM", "AFL", "ALL", "F", "CAT", "C", "CAB", "DAL"]

#print(json.dumps(getQuotes(stocks), indent = 3))

#print(stock_data[0])

# def print_stock_prices(stocks):
	# stock_data = getQuotes(stocks)
	# for stock in stock_data:
		# print("The price of {} is: ${}".format(stock['StockSymbol'],stock['LastTradePrice']))
		
# print_stock_prices(stocks)
ibm = DataReader('GIB',  'yahoo', datetime(2016,6,1), datetime(2016,9,1))
print(ibm)
# def get_quote(symbol):
    # base_url = 'http://finance.google.com/finance?q='
    # content = urllib.request.urlopen(base_url + symbol).read().decode('utf-8')
    # m = re.search('id="ref_694653_l".*?>(.*?)<', content)
    # if not m:
        # quote = m.group(1)
    # else:
        # quote = 'no quote available for: ' + symbol
    # return quote
# print(get_quote('aapl'))