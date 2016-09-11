# -*- coding: utf-8 -*-
#https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/s/?field-keywords=wild+rice"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all('li', 's-result-item')
amazon - []
for item in items:
	name = (item.find('h2').text)
	price = (item.find('span', 's-price').text)
	amazon.append({
		    "name":name, 
		    "price":price

