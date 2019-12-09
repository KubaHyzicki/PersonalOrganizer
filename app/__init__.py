from flask import Flask, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from .models import *
import os

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)

db = SQLAlchemy(app)

#login_manager.login_view = "users.login_view"

def addUser(args):
    userRecord = User(
            ID_user='',         #to ma chyba autonumerację
            lastName=args.lastName,
            email=args.email,
            password=args.password,
            firstName=args.firstName,
            permissions=args.permissions)
    db.session.add(userRecord)
    db.session.commit()

def listUsers():
    users = User.query.all()
    print(users)

def getUser(args):
    if args.ID_user:
        user = User.query.get(args.ID_user)
    elif args.email:
        user = User.query.filter(User.email==args.email)

def removeUser(ID_user):
    User.query.filter(User.ID_user == ID_user).\
        delete()
    

print('ciastko')
listUsers()             #no i wywala się, bo nie ma czegoś takiego jak personalOrganizer.db
print('ciastko')
addUser({'lastName':'Ciastek','email':'ciastek@gmail.com','password':'admin','firstName':'Pan','permissions':'client'})
print('ciastko')
listUsers()
print('ciastko')
