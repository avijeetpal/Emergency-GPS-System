from flask import Flask
import MySQLdb.cursors
import re

login = Flask(__name__)

@login.route('/')
def index():
    return render_template('.\frontend\login.html')

@login.route('/register')
def register():
    return "Hello"

@login.route('/login')
def login():
    return "Hello"

if __name__ == "__main__":
    login.run(debug=True)

