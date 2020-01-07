#!/usr/bin/python3

from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from .models import *
from .database import *

#app
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config.from_object('config.Config')

#flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#database
database_obj.load(app)

#routes
from .routes import *
app.register_blueprint(dbEndpoints)




@login_manager.user_loader
def load_user(user_id):
    return database_obj.getUser({'ID_user':user_id})

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = database_obj.getUser({'email':email}) 
    if user.check_password(password):
        load_user(user)
        if request.args.get("next"):
            return redirect(next)
        else:
            return redirect(url_for('ciastkoTest'))
    else:
        return abort(401)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')
    # return redirect('/')

@app.route('/')
def default():
    return "hello"

@app.route('/ciastkoTest')
def ciastkoTest():
    return "ciastkoTest successfull"

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')