#!/usr/bin/python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from .models import *

app = Flask(__name__)
app.config.from_object('config.Config')

class Database:
    def __init__(self):
        host = app.config['HOST']
        user = app.config['DB_USER']
        password = app.config['DB_PASS']
        db_name = app.config['DB_NAME']
        self.db = SQLAlchemy()
        self.db.init_app(app)

############################---User---############################
    def addUser(self, args):
        userRecord = User(
            lastName=args.lastName,
            email=args.email,
            password=args.password,
            firstName=args.firstName,
            permissions=args.permissions)
        self.db.session.add(userRecord)
        self.db.session.commit()

    def getAllUsers(self):
        users = User.query.all()
        return users

    def getUser(self, args):
        if args["ID_user"]:
            user = User.query.get(args["ID_user"])
        elif args["email"]:
            user = User.query.filter(User.email==args["email"])
        return user

    def removeUser(self, args):
        User.query.filter(User.ID_user == args["ID_user"]).\
            delete()

    def editUser(self, data):
        user = User.query.get(data["ID_user"])
        user.update(data)
        self.db.session.commit()

############################---Event---############################
    def addEvent(self, args):
        eventRecord = Event(
            name=args.name,
            status=args.status,
            description=args.description,
            participants=args.participants,
            creationDate=args.creationDate,
            repeatable=args.repeatable,
            ID_user=args.ID_user)
        self.db.session.add(eventRecord)
        self.db.session.commit()

    def getAllEvents(self):
        events = Event.query.all()
        return str(events)

    def getEvent(self, args):
        event = Event.query.get(args["ID_event"])
        return event

    def removeEvent(self, args):
        Event.query.filter(Event.ID_event == args["ID_event"]).\
            delete()

    def editEvent(self, data):
        event = Event.query.get(data["ID_event"])
        event.update(data)
        self.db.session.commit()

############################---Category---############################
    def addCategory(self, args):
        categoryRecord = Category(
            name=args.name,
            description=args.description,
            weight=args.weight,
            colour=args.colour)
        self.db.session.add(categoryRecord)
        self.db.session.commit()

    def getAllCategories(self):
        category = Category.query.all()
        return str(category)

    def getCategory(self, args):
        category = Category.query.get(args["ID_category"])
        return category

    def removeCategory(self, args):
        Category.query.filter(Category.ID_category == args["ID_category"]).\
            delete()

    def editCategory(self, data):
        category = Category.query.get(data["ID_category"])
        category.update(data)
        self.db.session.commit()

############################---Alarm---############################
    def addAlarm(self, args):
        alarmRecord = Alarm(
            volume_level=args.volume_level,
            active=args.active,
            whenAlarm=args.whenAlarm,
            alarmMethod=args.alarmMethod,
            ID_event=args.ID_event)
        self.db.session.add(alarmRecord)
        self.db.session.commit()

    def getAllCategories(self):
        alarm = Alarm.query.all()
        return str(alarm)

    def getAlarm(self, args):
        alarm = Alarm.query.get(args["ID_alarm"])
        return alarm

    def removeAlarm(self, args):
        Alarm.query.filter(Alarm.ID_alarm == args["ID_alarm"]).\
            delete()

    def editAlarm(self, data):
        alarm = Alarm.query.get(data["ID_alarm"])
        alarm.update(data)
        self.db.session.commit()

############################---AlarmType---############################
    def addAlarmType(self, args):
        alarmTypeRecord = AlarmType(
            alarmMethod=args.alarmMethod)
        self.db.session.add(alarmTypeRecord)
        self.db.session.commit()

    def getAllCategories(self):
        alarmType = AlarmType.query.all()
        return str(alarmType)

    def getAlarmType(self, args):
        alarmType = AlarmType.query.get(args["ID_alarmType"])
        return alarmType

    def removeAlarmType(self, args):
        AlarmType.query.filter(AlarmType.ID_alarmType == args["ID_alarmType"]).\
            delete()

    def editAlarmType(self, data):
        alarmType = AlarmType.query.get(data["ID_alarmType"])
        alarmType.update(data)
        self.db.session.commit()

############################---Api Endpoints---############################
@app.route('/')
def default():
    return "hello"

@app.route('/addUser', methods=['POST'])
def addUser():
    db = Database()
    db.addUser()
    return 'Commited!'

@app.route('/viewAllUsers')
def getAllUsers():
    db = Database()
    users = db.getAllUsers()
    # list=""                   #wyświetlanie listy ID
    # for user in users:
    #     list+=str(user.ID_user) + ' ' + str(user.password) + ' ' + str(user.firstName) + '\n'
    # return list
    return str(users)

@app.route('/getUser', methods=['GET'])
def getUser():
    db = Database()
    user = db.getUser(request.form.to_dict())
    return str(user)

@app.route('/removeUser', methods=['POST'])
def removeUser():
    db = Database()
    db.removeUser({'ID_user':request.form['ID_user']})
    return 'Commited!'

@app.route('/editUser', methods=['POST'])
def editUser():
    db = Database()
    db.editUser(request.form.to_dict())
    return 'Commited!'