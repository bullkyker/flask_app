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
import argparse
from dateutil.parser import parse #http://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

def get_stocks(start, stop, symbol):
	start1 = start.replace('%2F','-')
	start2 = parse(start1)
	start2 = start2.strftime('%Y-%m-%d')
	stop1 = stop.replace('%2F','-')
	stop2 = parse(stop1)
	stop2 = stop2.strftime('%Y-%m-%d')
	ibm = DataReader(symbol,  'google', start2, stop2)	
	return(str(ibm).split())
#stocks = get_stocks('09%2F07%2F2016', '09%2F30%2F2016', 'GOOG')
#stocks = str(stocks)
#print(stocks)
