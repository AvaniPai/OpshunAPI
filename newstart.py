import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/<name>')
def hello_name():
	if name == 'Rusty':
		return 'Good job for drinking your water'
	return 'Hello {}'.format(name)


