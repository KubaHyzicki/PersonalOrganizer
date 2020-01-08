#!/usr/bin/python3

from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

from .models import *
from .database import *

#app
app = Flask(__name__)
app.secret_key = 'super_secret_ciastko_key'
app.config.from_object('config.Config')

#flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users_routes.login"
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

#database
database_obj.load(app)

#blueprints
from .users import users_routes
app.register_blueprint(users_routes)



#basic route, no reason to move it to separate blueprints as it is standalone thing without login requirement
@app.route('/')
def default():
    return "hello"