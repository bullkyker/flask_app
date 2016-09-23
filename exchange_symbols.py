from bs4 import BeautifulSoup
import requests


def get_symbols():
	url = "https://www.google.com/finance?start=0&num=3000&q=%5B(exchange%20%3D%3D%20%22NASDAQ%22)%20%26%20(last_price%20%3E%200.1)%20%26%20(last_price%20%3C%201500)%5D&restype=company&noIL=1"	
	headers = {'User-Agent': 'Mozilla/5.0'}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.text, "html.parser")	
	items = soup.find_all('td', 'symbol')
	symbols = []
	
	for item in items:		
		title = None		
		if item.find('a'):
			title = item.find('a').text
		if title!= None:
			symbols.append(title)
	symbols.sort()	
	return symbols
# symbols = get_symbols()
# for symbol in symbols:	
	# print(symbol)