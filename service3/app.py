from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
	weaponsight = ['belomo pk-06', 'vomz pilad p1x42', 'okp-7', 'sobra ekp-8-18']
	weapongrip = ['fortis shift tactical grip', 'kac vertical grip', 'magpul afg grip', 't-5000 pad']
	tacial = ['an/peq-15 tactialdevice', 'la-5 tactical device', 'surefire xc1 flsaklight', 'ncstart blue laster']
	return(random.choice(weaponsight)) + (random.choice(weapongrip)) + (random.choice(tacial))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

