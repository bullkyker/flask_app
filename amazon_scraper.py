# -*- coding: utf-8 -*-
#https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup
import requests


def get_amazon(mysearch):
	url = "https://www.amazon.com/s/?field-keywords="
	url += mysearch.replace(' ', '+')
	headers = {'User-Agent': 'Mozilla/5.0'}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.text, "html.parser")	
	items = soup.find_all('li', 's-result-item')
	amazon = []
	counter = 1
	for item in items:		
		title = None
		price = None
		image = None
		link = None
		if item.find('h2'):
			title = item.find('h2').text
		if item.find('span', 's-price'):
			price = item.find('span', 's-price').text
		if item.find('img', 's-access-image'):			
			image = item.find('img', 's-access-image').attrs.get('src')
		if item.find('a', 'a-link-normal'):			
			link = item.find('a', 'a-link-normal').get('href')
		amazon.append({
		    "name": title, 
		    "price": price,
			"image": image,
			"link": link
		})
		counter += 1
		if counter > 3:
			break # return only 3
return amazon
