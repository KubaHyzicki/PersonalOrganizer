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

    def getAllAlarms(self):
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

    def getAllAlarmTypes(self):
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

@app.route('/getAllUsers')
def getAllUsers():
    db = Database()
    users = db.getAllUsers()
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

@app.route('/addEvent', methods=['POST'])
def addEvent():
    db = Database()
    db.addEvent()
    return 'Commited!'

@app.route('/getAllEvents')
def getAllEvents():
    db = Database()
    events = db.getAllEvents()
    return str(events)

@app.route('/getEvent', methods=['GET'])
def getEvent():
    db = Database()
    event = db.getEvent(request.form.to_dict())
    return str(event)

@app.route('/removeEvent', methods=['POST'])
def removeEvent():
    db = Database()
    db.removeEvent({'ID_Event':request.form['ID_Event']})
    return 'Commited!'

@app.route('/editEvent', methods=['POST'])
def editEvent():
    db = Database()
    db.editEvent(request.form.to_dict())
    return 'Commited!'

@app.route('/addCategory', methods=['POST'])
def addCategory():
    db = Database()
    db.addCategory()
    return 'Commited!'

@app.route('/getAllCategories')
def getAllCategories():
    db = Database()
    categories = db.getAllCategories()
    return str(categories)

@app.route('/getCategory', methods=['GET'])
def getCategory():
    db = Database()
    category = db.getCategory(request.form.to_dict())
    return str(category)

@app.route('/removeCategory', methods=['POST'])
def removeCategory():
    db = Database()
    db.removeCategory({'ID_category':request.form['ID_category']})
    return 'Commited!'

@app.route('/editCategory', methods=['POST'])
def editCategory():
    db = Database()
    db.editCategory(request.form.to_dict())
    return 'Commited!'

@app.route('/addAlarm', methods=['POST'])
def addAlarm():
    db = Database()
    db.addAlarm()
    return 'Commited!'

@app.route('/getAllAlarms')
def getAllAlarms():
    db = Database()
    alarms = db.getAllAlarms()
    return str(alarms)

@app.route('/getAlarm', methods=['GET'])
def getAlarm():
    db = Database()
    alarm = db.getAlarm(request.form.to_dict())
    return str(alarm)

@app.route('/removeAlarm', methods=['POST'])
def removeAlarm():
    db = Database()
    db.removeAlarm({'ID_Alarm':request.form['ID_Alarm']})
    return 'Commited!'

@app.route('/editAlarm', methods=['POST'])
def editAlarm():
    db = Database()
    db.editAlarm(request.form.to_dict())
    return 'Commited!'

@app.route('/addAlarmType', methods=['POST'])
def addAlarmType():
    db = Database()
    db.addAlarmType()
    return 'Commited!'

@app.route('/getAllAlarmTypes')
def getAllAlarmTypes():
    db = Database()
    alarmTypes = db.getAllAlarmTypes()
    return str(alarmTypes)

@app.route('/getAlarmType', methods=['GET'])
def getAlarmType():
    db = Database()
    alarmType = db.getAlarmType(request.form.to_dict())
    return str(alarmType)

@app.route('/removeAlarmType', methods=['POST'])
def removeAlarmType():
    db = Database()
    db.removeAlarmType({'ID_AlarmType':request.form['ID_AlarmType']})
    return 'Commited!'

@app.route('/editAlarmType', methods=['POST'])
def editAlarmType():
    db = Database()
    db.editAlarmType(request.form.to_dict())
    return 'Commited!'

@app.route('/addEventsCategory', methods=['POST'])
def addEventsCategory():
    db = Database()
    db.addEventsCategory()
    return 'Commited!'

@app.route('/getAllEventsCategories')
def getAllEventsCategories():
    db = Database()
    eventsCategories = db.getAllEventsCategories()
    return str(eventsCategories)

@app.route('/getEventsCategory', methods=['GET'])
def getEventsCategory():
    db = Database()
    eventsCategory = db.getEventsCategory(request.form.to_dict())
    return str(eventsCategory)

@app.route('/removeEventsCategory', methods=['POST'])
def removeEventsCategory():
    db = Database()
    db.removeEventsCategory({'ID_EventCateg':request.form['ID_EventCateg']})
    return 'Commited!'

@app.route('/editEventsCategory', methods=['POST'])
def editEventsCategory():
    db = Database()
    db.editEventsCategory(request.form.to_dict())
    return 'Commited!'