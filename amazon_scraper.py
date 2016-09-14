# -*- coding: utf-8 -*-
#https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/s/?field-keywords=wild+rice"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all('div', 'a-row')
# def get_amazon(mysearch):
	
	# items = soup.find_all('li', 's-result-item')
	# amazon = []
	# for item in items:
		# name = (item.find('h2').text)
		# price = (item.find('span', 's-price').text)
		# amazon.append({
		    # "name":name, 
		    # "price":price
		# })
	# return amazon
	
# my_amazon= get_amazon("fred")
# print(my_amazon)
for link in links:
	# print(link.text)
	# print(link.price)
	# print(link.get('img'))
	print(link.text)
	#print(link.find('img', 's-access-image').url)