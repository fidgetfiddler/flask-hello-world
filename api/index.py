from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
	return render_template('index.html')


@app.route('/subpage')
def subpage():  # put application's code here
	return render_template('subpage.html')
