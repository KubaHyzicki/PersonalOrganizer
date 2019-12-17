#!/usr/bin/python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from .models import *

app = Flask(__name__)
app.config.from_object('config.Config')

class Database:
    # def __init__(self):
    #     host = app.config['HOST']
    #     user = app.config['DB_USER']
    #     password = app.config['DB_PASS']
    #     db_name = app.config['DB_NAME']
    #     self.db = SQLAlchemy()
    #     self.db.init_app(app)

    def load(self, user, password):
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
            firstName=args.firstName,
            permissions=args.permissions)
        userRecord.set_password(args.password)
        self.db.session.add(userRecord)
        self.db.session.commit()

    def getAllUsers(self):
        users = User.query.all()
        return users

    def getUser(self, args):
        try:
            user = User.query.get(args["ID_user"])
            return user
        except KeyError: pass
        try:
            user = User.query.filter(User.email==args["email"]).first()
            return user
        except KeyError: pass
        return None

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

############################---EventsCategories---############################
    def addEventsCategory(self, args):
        eventCategoryRecord = EventsCategories(
            name=args.name,
            description=args.description,
            weight=args.weight,
            colour=args.colour)
        self.db.session.add(eventCategoryRecord)
        self.db.session.commit()

    def getAllEventsCategories(self):
        eventsCategory = EventsCategories.query.all()
        return str(eventsCategory)

    def getEventsCategory(self, args):
        eventsCategory = EventsCategories.query.get(args["ID_EventCategory"])
        return eventsCategory

    def removeEventsCategory(self, args):
        EventsCategories.query.filter(EventsCategories.ID_EventCategory == args["ID_EventCategory"]).\
            delete()

    def editEventsCategory(self, data):
        eventsCategory = EventsCategories.query.get(data["ID_EventCategory"])
        eventsCategory.update(data)
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

db = Database()

@app.route('/login',methods=['POST'])
def login():
    email=request.form.get("email")
    password=request.form.get("password")

    loginDB = Database()
    loginDB.load(app.config['ADMIN_DB_USER'],app.config['ADMIN_DB_PASS'])
    user = loginDB.getUser({"email":email})

    if not user:
        return "INCORRECT USERNAME"

    elif not user.check_password(password):
        return "INCORRECT PASSWORD"
    else:
        if user.get_permissions() == None:
            user = app.config['CLIENT_DB_USER']
            password = app.config['CLIENT_DB_PASS']
        elif user.get_permissions() == 'admin':
            user = app.config['ADMIN_DB_USER']
            password = app.config['ADMIN_DB_PASS']
        db.load(user, password)
        return "logged as {}".format(user)

@app.route('/logout')
def logout():
    del db
    db = Database()

############################---Api Endpoints---############################
@app.route('/')
def default():
    return "hello"

@app.route('/addUser', methods=['POST'])
def addUser():
    db.addUser()
    return 'Commited!'

@app.route('/getAllUsers')
def getAllUsers():
    users = db.getAllUsers()
    return str(users)

@app.route('/getUser', methods=['GET'])
def getUser():
    user = db.getUser(request.form.to_dict())
    return str(user)

@app.route('/removeUser', methods=['POST'])
def removeUser():
    db.removeUser({'ID_user':request.form['ID_user']})
    return 'Commited!'

@app.route('/editUser', methods=['POST'])
def editUser():
    db.editUser(request.form.to_dict())
    return 'Commited!'

@app.route('/addEvent', methods=['POST'])
def addEvent():
    db.addEvent()
    return 'Commited!'

@app.route('/getAllEvents')
def getAllEvents():
    events = db.getAllEvents()
    return str(events)

@app.route('/getEvent', methods=['GET'])
def getEvent():
    event = db.getEvent(request.form.to_dict())
    return str(event)

@app.route('/removeEvent', methods=['POST'])
def removeEvent():
    db.removeEvent({'ID_Event':request.form['ID_Event']})
    return 'Commited!'

@app.route('/editEvent', methods=['POST'])
def editEvent():
    db.editEvent(request.form.to_dict())
    return 'Commited!'

@app.route('/addCategory', methods=['POST'])
def addCategory():
    db.addCategory()
    return 'Commited!'

@app.route('/getAllCategories')
def getAllCategories():
    categories = db.getAllCategories()
    return str(categories)

@app.route('/getCategory', methods=['GET'])
def getCategory():
    category = db.getCategory(request.form.to_dict())
    return str(category)

@app.route('/removeCategory', methods=['POST'])
def removeCategory():
    db.removeCategory({'ID_category':request.form['ID_category']})
    return 'Commited!'

@app.route('/editCategory', methods=['POST'])
def editCategory():
    db.editCategory(request.form.to_dict())
    return 'Commited!'

@app.route('/addAlarm', methods=['POST'])
def addAlarm():
    db.addAlarm()
    return 'Commited!'

@app.route('/getAllAlarms')
def getAllAlarms():
    alarms = db.getAllAlarms()
    return str(alarms)

@app.route('/getAlarm', methods=['GET'])
def getAlarm():
    alarm = db.getAlarm(request.form.to_dict())
    return str(alarm)

@app.route('/removeAlarm', methods=['POST'])
def removeAlarm():
    db.removeAlarm({'ID_Alarm':request.form['ID_Alarm']})
    return 'Commited!'

@app.route('/editAlarm', methods=['POST'])
def editAlarm():
    db.editAlarm(request.form.to_dict())
    return 'Commited!'

@app.route('/addAlarmType', methods=['POST'])
def addAlarmType():
    db.addAlarmType()
    return 'Commited!'

@app.route('/getAllAlarmTypes')
def getAllAlarmTypes():
    alarmTypes = db.getAllAlarmTypes()
    return str(alarmTypes)

@app.route('/getAlarmType', methods=['GET'])
def getAlarmType():
    alarmType = db.getAlarmType(request.form.to_dict())
    return str(alarmType)

@app.route('/removeAlarmType', methods=['POST'])
def removeAlarmType():
    db.removeAlarmType({'ID_AlarmType':request.form['ID_AlarmType']})
    return 'Commited!'

@app.route('/editAlarmType', methods=['POST'])
def editAlarmType():
    db.editAlarmType(request.form.to_dict())
    return 'Commited!'

@app.route('/addEventsCategory', methods=['POST'])
def addEventsCategory():
    db.addEventsCategory()
    return 'Commited!'

@app.route('/getAllEventsCategories')
def getAllEventsCategories():
    eventsCategories = db.getAllEventsCategories()
    return str(eventsCategories)

@app.route('/getEventsCategory', methods=['GET'])
def getEventsCategory():
    eventsCategory = db.getEventsCategory(request.form.to_dict())
    return str(eventsCategory)

@app.route('/removeEventsCategory', methods=['POST'])
def removeEventsCategory():
    db.removeEventsCategory({'ID_EventCateg':request.form['ID_EventCateg']})
    return 'Commited!'

@app.route('/editEventsCategory', methods=['POST'])
def editEventsCategory():
    db.editEventsCategory(request.form.to_dict())
    return 'Commited!'