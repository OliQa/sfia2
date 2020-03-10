from flask import Flask
import random



app = Flask(__name__)


@app.route('/')
def index():
	weapon = ['m4al', 'ak-47', 'ak-74', 'adar2-15', 'hk 416a5']
	return(random.choice(weapon))


if __name__ =='__main__':
	app.run(debug=True, host='0.0.0.0')

