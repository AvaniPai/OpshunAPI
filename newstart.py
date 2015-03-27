from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!This is Avani Speaking!"
@app.route('/<username>')
def specialized(username):
	return "I love you {}!".format(username)

