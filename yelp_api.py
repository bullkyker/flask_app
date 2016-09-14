from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

"""
	Created environment variables by using the bash command
	export CONSUMER_KEY = ...
	Additionally you can create a .env file and put the keys in there
	use pip install -U python-dotenv and then add the env commands above
	the keys come from https://www.yelp.com/developers/manage_api_keys
"""
auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    token=os.environ['TOKEN'],
    token_secret=os.environ['TOKEN_SECRET']
)

client = Client(auth)
def yelp_search(param_term, param_city):
	params = {
    'term': param_term,
    'lang': 'en',
    'sort': 2	
	}
	businesses = []
	counter = 1
	response = client.search(param_city, **params)
	
	for business in response.businesses:
		#print(business.name, "Rating ", business.rating)
		businesses.append({
		    "name":business.name, 
		    "rating": business.rating, 
		    "phone": business.phone	
			"image": business.image_url
		})
		if counter >= 3:
			break
		counter += 1
	return businesses
	
# param_term = input("Enter a search term: ")
# param_city = input("Enter a search city: ").upper()
# businesses = yelp_search(param_term, param_city)
# yelp_search(param_term, param_city)

# print(businesses)