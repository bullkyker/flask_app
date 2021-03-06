"""
	git status
	git add -A
	git commit -m "This is the message in quotes"
	git push
	remember pip freeze
	https://polar-peak-85361.herokuapp.com/ | https://git.heroku.com/polar-peak-85361.git
	heroku apps:rename bullkyker-project
"""


#http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
#https://www.crummy.com/software/BeautifulSoup/
import sys
import os
import tip_bullkyker
import amazon_scraper
#from pathlib import Path # if you haven't already done so
#root = str(Path(__file__).resolve().parents[1])
# Or
#   from os.path import dirname, abspath
#   root = dirname(dirname(abspath(__file__)))
#sys.path.append(root)
from weather import get_location
from flask import Flask, render_template, request
from yelp_api import yelp_search
from ice_cream import icecream
from tip_bullkyker import suggest_tip
from imp import reload
from amazon_scraper import get_amazon
from exchange_symbols import get_symbols
from stock_prices import get_stocks, get_max, get_min
app = Flask(__name__)
@app.route("/")
def index():	
	location = None
	local_weather = None
	term = None
	city = None
	businesses = None
	symbols = get_symbols()
	if(request.values.get('weather'))!=None:
		location = request.values.get('weather')
		local_weather=get_location(location)
		return render_template('index.html', weather=local_weather, exsymbols=symbols)
	elif(request.values.get('topic'))!=None:
		term = request.values.get('topic')
		city = request.values.get('city')
		businesses = yelp_search(term, city)
		return render_template('index.html', searchresult=businesses, exsymbols=symbols)
	elif(request.values.get('icecream'))!=None:
		sundae = icecream()
		return render_template('index.html', icecream=sundae, exsymbols=symbols)
	elif(request.values.get('amount'))!=None:
		tip = request.values.get('amount')
		tip_suggest = suggest_tip(tip)
		reload(tip_bullkyker)
		return render_template('index.html', gottip=tip_suggest, exsymbols=symbols)
	elif(request.values.get('amazontopic'))!=None:
		amazon_search = request.values.get('amazontopic')
		amazon_result = get_amazon(amazon_search)
		reload(amazon_scraper)
		return render_template('index.html', yoursearch=amazon_result, exsymbols=symbols)	
	elif(request.values.get('stocksymbol'))!=None:	
		start = request.values.get('startdate')
		stop = request.values.get('enddate')
		symbol = request.values.get('stocksymbol')
		stock = get_stocks(start, stop, symbol)
		open = get_max(stock, 1)
		high = get_max(stock, 2)
		low = get_min(stock, 3)
		close = get_max(stock, 4)		
		volume = get_max(stock, 5)
		return render_template('index.html', yourstocks=stock, symbol=symbol, open=open, high=high, low=low, close=close, volume=volume)	
	else:		
		return render_template('index.html', exsymbols=symbols)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__  ==  "__main__":
	port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)