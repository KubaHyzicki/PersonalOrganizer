from . import app
# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
# import flask_login
from .models import *
# from .routes import *
# from . import database

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