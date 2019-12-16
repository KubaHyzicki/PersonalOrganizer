#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import *

app = Flask(__name__)
app.config.from_object('config.Config')

class Database:
    def __init__(self):
        host = app.config['HOST']
        print
        user = app.config['DB_USER']
        password = app.config['DB_PASS']
        db_name = app.config['DB_NAME']
        self.db = SQLAlchemy()
        self.db.init_app(app)

    def getAllUsers(self):
        users = User.query.all()
        return users

    def getUser(self,args):
        if args.ID_user:
            user = User.query.get(args.ID_user)
        elif args.email:
            user = User.query.filter(User.email==args.email)

    def addUser(self,args):
        userRecord = User(
            lastName=args.lastName,
            email=args.email,
            password=args.password,
            firstName=args.firstName,
            permissions=args.permissions)
        self.db.session.add(userRecord)
        self.db.session.commit()


@app.route('/')
def default():
    return "hello"

@app.route('/viewAllUsers')
def getAllUsers():
    db = Database()
    users = db.getAllUsers()
    return str(users)

@app.route('/addDefaultUser')
def addUser():
    db = Database()
    db.addUser({'lastName':'Ciastek','email':'ciastek@gmail.com','password':'admin','firstName':'Pan','permissions':'client'})
    return 'Commited!'
