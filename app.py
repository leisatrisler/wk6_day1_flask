from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    name = 'Brian'
    #name.append('Staton')
@app.route('/test')
def test():
    return 'this is a test!'
