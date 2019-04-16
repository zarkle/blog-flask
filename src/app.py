from flask import Flask, render_template, request, session
from src.models.user import User
from .common.database import Database


app = Flask(__name__)
# app.secret_key('key')


@app.route('/')
def home():
    return render_template('login.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    import pdb; pdb.set_trace()

    return render_template('profile.html', email=email)

if __name__ == "__main__":
    app.run()
