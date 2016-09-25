from pandas.io.data import DataReader
#from pandas_datareader import data, wb
from googlefinance import getQuotes
import json
from datetime import datetime
import pandas 
import time
import urllib.request
import urllib
import math

from dateutil.parser import parse #http://stackoverflow.com/questions/2265357/parse-date-string-and-change-format

def get_max(good, col):	
	max = 0
	for row in good:
		open = row[col]
		#if is_number(open):
		if float(open) >= float(max):
			max = open
	return max
def get_min(good, col):	
	min = 10000000
	for row in good:
		open = row[col]
		#if is_number(open):
		if float(open) <= float(min):
			min = open
	return min
def get_average(good, col):	
	count = 0
	avg = 0
	for row in good:
		my_avg = row[col]
		avg = avg + float(my_avg)
		count += 1	
	return round((avg/count),2)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
	
def get_stocks(start, stop, symbol):
	start1 = start.replace('%2F','-')
	start2 = parse(start1)
	start2 = start2.strftime('%Y-%m-%d')
	stop1 = stop.replace('%2F','-')
	stop2 = parse(stop1)
	stop2 = stop2.strftime('%Y-%m-%d')
	ibm = DataReader(symbol,  'google', start2, stop2)	
	ibm = str(ibm).split()
	#print(ibm)
	layout = []
	my_length = int(len(ibm))	
	for X in range(0, my_length, 6):
		row = []		
		for item in ibm[X:6 + X ]:			
			if item != '...':
				row.append(item)
		if len(row) == 6 and row[0] != 'Open':
			layout.append(row)	
	averages =[]
	averages.append("Averages")
	avg_open = get_average(layout, 1)
	avg_high = get_average(layout, 2)
	avg_low = get_average(layout, 3)
	avg_close = get_average(layout, 4)
	avg_vol = get_average(layout, 5)
	averages.append(avg_open)
	averages.append(avg_high)
	averages.append(avg_low)
	averages.append(avg_close)
	averages.append(avg_vol)
	layout.append(averages)
	return layout
	
	
# stocks = get_stocks('09%2F07%2F2016', '09%2F30%2F2016', 'GOOG')
# print(stocks)