from flask import Flask
import random
import string
import requests


app = Flask(__name__)


@app.route('/')
def index():
	response = requests.get('http://service2:5000')
	weapon = response.text
	response = requests.get('http://service3:5000')
	sight = response.text
	return str(weapon + sight)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

