# """
	# git status
	# git add -A
	# git commit -m "This is the message in quotes"
	# git push
	# remember pip freeze
	# https://polar-peak-85361.herokuapp.com/ | https://git.heroku.com/polar-peak-85361.git
# """


#http://stackoverflow.com/questions/16981921/relative-imports-in-python-3
#https://www.crummy.com/software/BeautifulSoup/
#import sys

import os
#from pathlib import Path # if you haven't already done so
#root = str(Path(__file__).resolve().parents[1])
# Or
#   from os.path import dirname, abspath
#   root = dirname(dirname(abspath(__file__)))
#sys.path.append(root)
from weather import get_location
from flask import Flask, render_template, request
from flaskrun import flaskrun
app = None 
app = Flask(__name__)
@app.route("/")
def index():	
	location = None
	local_weather = None
	if(request.values.get('weather'))!=None:
		location = request.values.get('weather')
		local_weather=get_location(location)
		return render_template('index.html', weather=local_weather)
	else:
		return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000)
    Flask(__name__).run(debug = True, host='0.0.0.0', port=port)
	
	#app.run(debug=True)