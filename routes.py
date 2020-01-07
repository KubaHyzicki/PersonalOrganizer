
# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
# import flask_login
from .models import *
# from .routes import *
# from . import database

dbEndpoints = Blueprint('dbEndpoints', __name__,)


@dbEndpoints.route('/addUser', methods=['POST'])
def addUser():
    db.addUser()
    return 'Commited!'

@dbEndpoints.route('/getAllUsers')
def getAllUsers():
    users = db.getAllUsers()
    return str(users)

@dbEndpoints.route('/getUser', methods=['GET'])
def getUser():
    user = db.getUser(request.form.to_dict())
    return str(user)

@dbEndpoints.route('/removeUser', methods=['POST'])
def removeUser():
    db.removeUser({'ID_user':request.form['ID_user']})
    return 'Commited!'

@dbEndpoints.route('/editUser', methods=['POST'])
def editUser():
    db.editUser(request.form.to_dict())
    return 'Commited!'

@dbEndpoints.route('/addEvent', methods=['POST'])
def addEvent():
    db.addEvent()
    return 'Commited!'

@dbEndpoints.route('/getAllEvents')
def getAllEvents():
    events = db.getAllEvents()
    return str(events)

@dbEndpoints.route('/getEvent', methods=['GET'])
def getEvent():
    event = db.getEvent(request.form.to_dict())
    return str(event)

@dbEndpoints.route('/removeEvent', methods=['POST'])
def removeEvent():
    db.removeEvent({'ID_Event':request.form['ID_Event']})
    return 'Commited!'

@dbEndpoints.route('/editEvent', methods=['POST'])
def editEvent():
    db.editEvent(request.form.to_dict())
    return 'Commited!'

@dbEndpoints.route('/addCategory', methods=['POST'])
def addCategory():
    db.addCategory()
    return 'Commited!'

@dbEndpoints.route('/getAllCategories')
def getAllCategories():
    categories = db.getAllCategories()
    return str(categories)

@dbEndpoints.route('/getCategory', methods=['GET'])
def getCategory():
    category = db.getCategory(request.form.to_dict())
    return str(category)

@dbEndpoints.route('/removeCategory', methods=['POST'])
def removeCategory():
    db.removeCategory({'ID_category':request.form['ID_category']})
    return 'Commited!'

@dbEndpoints.route('/editCategory', methods=['POST'])
def editCategory():
    db.editCategory(request.form.to_dict())
    return 'Commited!'

@dbEndpoints.route('/addAlarm', methods=['POST'])
def addAlarm():
    db.addAlarm()
    return 'Commited!'

@dbEndpoints.route('/getAllAlarms')
def getAllAlarms():
    alarms = db.getAllAlarms()
    return str(alarms)

@dbEndpoints.route('/getAlarm', methods=['GET'])
def getAlarm():
    alarm = db.getAlarm(request.form.to_dict())
    return str(alarm)

@dbEndpoints.route('/removeAlarm', methods=['POST'])
def removeAlarm():
    db.removeAlarm({'ID_Alarm':request.form['ID_Alarm']})
    return 'Commited!'

@dbEndpoints.route('/editAlarm', methods=['POST'])
def editAlarm():
    db.editAlarm(request.form.to_dict())
    return 'Commited!'

@dbEndpoints.route('/addAlarmType', methods=['POST'])
def addAlarmType():
    db.addAlarmType()
    return 'Commited!'

@dbEndpoints.route('/getAllAlarmTypes')
def getAllAlarmTypes():
    alarmTypes = db.getAllAlarmTypes()
    return str(alarmTypes)

@dbEndpoints.route('/getAlarmType', methods=['GET'])
def getAlarmType():
    alarmType = db.getAlarmType(request.form.to_dict())
    return str(alarmType)

@dbEndpoints.route('/removeAlarmType', methods=['POST'])
def removeAlarmType():
    db.removeAlarmType({'ID_AlarmType':request.form['ID_AlarmType']})
    return 'Commited!'

@dbEndpoints.route('/editAlarmType', methods=['POST'])
def editAlarmType():
    db.editAlarmType(request.form.to_dict())
    return 'Commited!'

@dbEndpoints.route('/addEventsCategory', methods=['POST'])
def addEventsCategory():
    db.addEventsCategory()
    return 'Commited!'

@dbEndpoints.route('/getAllEventsCategories')
def getAllEventsCategories():
    eventsCategories = db.getAllEventsCategories()
    return str(eventsCategories)

@dbEndpoints.route('/getEventsCategory', methods=['GET'])
def getEventsCategory():
    eventsCategory = db.getEventsCategory(request.form.to_dict())
    return str(eventsCategory)

@dbEndpoints.route('/removeEventsCategory', methods=['POST'])
def removeEventsCategory():
    db.removeEventsCategory({'ID_EventCateg':request.form['ID_EventCateg']})
    return 'Commited!'

@dbEndpoints.route('/editEventsCategory', methods=['POST'])
def editEventsCategory():
    db.editEventsCategory(request.form.to_dict())
    return 'Commited!'