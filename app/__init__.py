from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
print(app.config)


# import all the routes from the routes file into the curent package
from app import routes
