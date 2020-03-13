from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
	response = requests.get('http://service4:5000')
	loadout = response.text
	return render_template('index.html', loadout=loadout)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


