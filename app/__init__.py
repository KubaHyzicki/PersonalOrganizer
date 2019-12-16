#!/usr/bin/python3

from flask import Flask
import pymysql
import os

app = Flask(__name__)
app.config.from_object('config.Config')

class Database:
    def __init__(self):
        host = app.config['HOST']
        print
        user = app.config['DB_USER']
        password = app.config['DB_PASS']
        db = app.config['DB_NAME']
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def get_users(self):
        self.cur.execute("SELECT * FROM User")
        result = self.cur.fetchall()
        print("ciastko {}".format(result))
        return result

    def add_user(self):
        query="INSERT INTO User (lastname,email,password,firstName,permissions) VALUES ('Ciastek','ciastek@gmail.com','admin','Pan','client')"
        self.cur.execute(query)
        self.con.commit()

#db = Database()

@app.route('/')
def default():
    return "hello"
@app.route('/viewAllUsers')
def viewAllUsers():
    db = Database()
    print('ciastko added')
    users = db.get_users()
    return str(users)
@app.route('/addDefaultUser')
def addUser():
    db = Database()
    db.add_user()
    return 'Commited!'