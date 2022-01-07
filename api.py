import requests,user_agent,json,flask,bs4
from user_agent import generate_user_agent
from flask import Flask,jsonify
from flask import *
from bs4 import BeautifulSoup
from datetime import date

	
app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>WELCOME TO THE API  SIDRAELEZZ TELEGRAM : @SidraTools</h1>"


@app.route('/info/tiktok/', methods=['GET'])
def tiktok():
	username = str(request.args.get('username'))
	url = 'https://server1.majhcc.xyz/api/tk/get_user_info?username='+str(username)
	response = requests.get(url)
	if 'error' in response.text :
		return jsonify('eror')
	else :
		account= json.loads(response.text)  
		info={
		"name":account["info"]["name"],
		"following": account["info"]["followingCount"],
		"followers": account["info"]["followerCount"]}
		return jsonify(info)

if __name__ == "__main__":
	app.run()
    
