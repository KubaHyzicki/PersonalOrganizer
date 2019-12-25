#!/usr/bin/python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import flask_login
from .models import *
from .routes import *
from . import database

#app
app = Flask(__name__)
app.config.from_object('{}.Config'.format(config_name))

#flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#database
db = Database()



@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = db.getUser(email)
    if user.check_password(password):
        login_user(user)
        return redirect(request.args.get("next"))
    else:
        return abort(401)



    # email=request.form.get("email")
    # password=request.form.get("password")

    # loginDB = Database()
    # loginDB.load('admin_config')
    # user = loginDB.getUser({"email":email})

    # if not user:
    #     return "INCORRECT USERNAME"

    # elif not user.check_password(password):
    #     return "INCORRECT PASSWORD"
    # else:
    #     if user.get_permissions() == None:
    #         user = app.config['CLIENT_DB_USER']
    #         password = app.config['CLIENT_DB_PASS']
    #     elif user.get_permissions() == 'admin':
    #         user = app.config['ADMIN_DB_USER']
    #         password = app.config['ADMIN_DB_PASS']
    #     db.load(user, password)
    #     return "logged as {}".format(user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')
    # return redirect('/')

# @app.route('/logout')
# def logout():
#     del db
#     db = Database()

############################---Api Endpoints---############################
@app.route('/')
def default():
    return "hello"




@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')