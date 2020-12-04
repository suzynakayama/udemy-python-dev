from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi Suzy!'

@app.route('/blog/<username>')
def blog1(username=None):
    return render_template('index.html', name=username)

@app.route('/blog')
def blog():
    return render_template('index.html')

