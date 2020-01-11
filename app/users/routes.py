from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from app.database import *
from . import users_routes


############################---Registering---############################
@users_routes.route('/register', methods=['GET', 'POST'])
def register():
# not ready yet
#     if request.method == 'GET':
#         return render_template('users/login.html')

    if current_user.is_authenticated:
        return 'already registered'

    data = request.form.to_dict()
    if database_obj.getUser({'email':data['email']}):
        return 'User with given email ({}) already exists!'.format(data['email'])

    database_obj.addUser(data)
    return 'Successfully registered, now You can log in'

############################---Logging---############################
@users_routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return 'already logged in'

# not ready yet
#     if request.method == 'GET':
#         return render_template('users/login.html')

    email = request.form['email']
    password = request.form['password']
    user = database_obj.getUser({'email':email})
    if user and user.check_password(password):
        user._authenticated=True
        login_user(user)
        print('logged in user {}'.format(email))
        return redirect(url_for('default'))
    else:
        return 'Invalid pass or email'

@users_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return "Logged out"

@users_routes.route('/testLogin')
@login_required
def testLogin():
    return "logged"

############################---User---############################
@users_routes.route('/addUser', methods=['POST'])
@login_required
def addUser():
    database_obj.addUser(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getAllUsers')
@login_required
def getAllUsers():
    users = database_obj.getAllUsers()
    return str(users)

@users_routes.route('/getUser', methods=['GET'])
@login_required
def getUser():
    user = database_obj.getUser(request.form.to_dict())
    return str(user)

@users_routes.route('/removeUser', methods=['POST'])
@login_required
def removeUser():
    database_obj.removeUser({'ID_user':request.form['ID_user']})
    return 'Commited!'

@users_routes.route('/editUser', methods=['POST'])
@login_required
def editUser():
    database_obj.editUser(request.form.to_dict())
    return 'Commited!'

############################---Event---############################
@users_routes.route('/addEvent', methods=['POST'])
@login_required
def addEvent():
    database_obj.addEvent(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getAllEvents')
@login_required
def getAllEvents():
    events = database_obj.getAllEvents()
    return str(events)

@users_routes.route('/getEvent', methods=['GET'])
@login_required
def getEvent():
    event = database_obj.getEvent(request.form.to_dict())
    return str(event)

@users_routes.route('/removeEvent', methods=['POST'])
@login_required
def removeEvent():
    database_obj.removeEvent({'ID_Event':request.form['ID_Event']})
    return 'Commited!'

@users_routes.route('/editEvent', methods=['POST'])
@login_required
def editEvent():
    database_obj.editEvent(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getUserEvents', methods=['POST'])
@login_required
def getUserEvents():
    event = database_obj.getUserEvents({'ID_user':current_user.get_id()})
    return str(event)

############################---Category---############################
@users_routes.route('/addCategory', methods=['POST'])
@login_required
def addCategory():
    database_obj.addCategory(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getAllCategories')
@login_required
def getAllCategories():
    categories = database_obj.getAllCategories()
    return str(categories)

@users_routes.route('/getCategory', methods=['GET'])
@login_required
def getCategory():
    category = database_obj.getCategory(request.form.to_dict())
    return str(category)

@users_routes.route('/removeCategory', methods=['POST'])
@login_required
def removeCategory():
    database_obj.removeCategory({'ID_category':request.form['ID_category']})
    return 'Commited!'

@users_routes.route('/editCategory', methods=['POST'])
@login_required
def editCategory():
    database_obj.editCategory(request.form.to_dict())
    return 'Commited!'

############################---Alarm---############################
@users_routes.route('/addAlarm', methods=['POST'])
@login_required
def addAlarm():
    database_obj.addAlarm(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getAllAlarms')
@login_required
def getAllAlarms():
    alarms = database_obj.getAllAlarms()
    return str(alarms)

@users_routes.route('/getAlarm', methods=['GET'])
@login_required
def getAlarm():
    alarm = database_obj.getAlarm(request.form.to_dict())
    return str(alarm)

@users_routes.route('/removeAlarm', methods=['POST'])
@login_required
def removeAlarm():
    database_obj.removeAlarm({'ID_Alarm':request.form['ID_Alarm']})
    return 'Commited!'

@users_routes.route('/editAlarm', methods=['POST'])
@login_required
def editAlarm():
    database_obj.editAlarm(request.form.to_dict())
    return 'Commited!'

############################---AlarmType---############################
@users_routes.route('/addAlarmType', methods=['POST'])
@login_required
def addAlarmType():
    database_obj.addAlarmType(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getAllAlarmTypes')
@login_required
def getAllAlarmTypes():
    alarmTypes = database_obj.getAllAlarmTypes()
    return str(alarmTypes)

@users_routes.route('/getAlarmType', methods=['GET'])
@login_required
def getAlarmType():
    alarmType = database_obj.getAlarmType(request.form.to_dict())
    return str(alarmType)

@users_routes.route('/removeAlarmType', methods=['POST'])
@login_required
def removeAlarmType():
    database_obj.removeAlarmType({'ID_AlarmType':request.form['ID_AlarmType']})
    return 'Commited!'

@users_routes.route('/editAlarmType', methods=['POST'])
@login_required
def editAlarmType():
    database_obj.editAlarmType(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/addEventsCategory', methods=['POST'])
@login_required
def addEventsCategory():
    database_obj.addEventsCategory(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/getAllEventsCategories')
@login_required
def getAllEventsCategories():
    eventsCategories = database_obj.getAllEventsCategories()
    return str(eventsCategories)

@users_routes.route('/getEventsCategory', methods=['GET'])
@login_required
def getEventsCategory():
    eventsCategory = database_obj.getEventsCategory(request.form.to_dict())
    return str(eventsCategory)

@users_routes.route('/removeEventsCategory', methods=['POST'])
@login_required
def removeEventsCategory():
    database_obj.removeEventsCategory({'ID_EventCateg':request.form['ID_EventCateg']})
    return 'Commited!'

@users_routes.route('/editEventsCategory', methods=['POST'])
@login_required
def editEventsCategory():
    database_obj.editEventsCategory(request.form.to_dict())
    return 'Commited!'