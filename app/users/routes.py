from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from app.database import *
from . import users_routes
#from .forms import RegisterForm, LoginForm


# @users_blueprint.route('/register', methods=['GET', 'POST'])
# def register():
#     # If the User is already logged in, don't allow them to try to register
#     if current_user.is_authenticated:
#         flash('Already registered!  Redirecting to your User Profile page...')
#         return redirect(url_for('users.profile'))

#     form = RegisterForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         new_user = User(form.email.data, form.password.data)
#         new_user.authenticated = True
#         db.session.add(new_user)
#         db.session.commit()
#         login_user(new_user)
#         flash('Thanks for registering, {}!'.format(new_user.email))
#         return redirect(url_for('users.profile'))
#     return render_template('users/register.html', form=form)


@users_routes.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return 'already logged in'

    # form = LoginForm()
# not ready yet
#     if request.method == 'GET':
#         return render_template('users/login.html', form=form)

    email = request.form['email']
    password = request.form['password']
    user = database_obj.getUser({'email':email})
    if user and user.check_password(password):
        login_user(user)
        print('logged in user {}'.format(email))
        return redirect(url_for('default'))
    else:
        return 'Invalid pass or email'
    #if form.validate_on_submit():



@users_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return Response('Logged out')








############################---Login---############################
# @login_manager.user_loader
# def load_user(user_id):
#     return database_obj.getUser({'ID_user':user_id})

# @app.route('/login', methods=['POST'])
# def login():
#     email = request.form['email']
#     password = request.form['password']
#     user = database_obj.getUser({'email':email}) 
#     if user.check_password(password):
#         load_user(user)
#         if request.args.get("next"):
#             return redirect(next)
#         else:
#             return redirect(url_for('ciastkoTest'))
#     else:
#         return 'Invalid pass or email'


# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return Response('Logged out')


@users_routes.route('/testLogin')
@login_required
def testLogin():
    print("logged")
    return "logged"

############################---User---############################
@users_routes.route('/addUser', methods=['POST'])
def addUser():
    database_obj.addUser()
    return 'Commited!'

@users_routes.route('/getAllUsers')
def getAllUsers():
    users = database_obj.getAllUsers()
    return str(users)

@users_routes.route('/getUser', methods=['GET'])
def getUser():
    user = database_obj.getUser(request.form.to_dict())
    return str(user)

@users_routes.route('/removeUser', methods=['POST'])
def removeUser():
    database_obj.removeUser({'ID_user':request.form['ID_user']})
    return 'Commited!'

@users_routes.route('/editUser', methods=['POST'])
def editUser():
    database_obj.editUser(request.form.to_dict())
    return 'Commited!'

############################---Event---############################
@users_routes.route('/addEvent', methods=['POST'])
def addEvent():
    database_obj.addEvent()
    return 'Commited!'

@users_routes.route('/getAllEvents')
def getAllEvents():
    events = database_obj.getAllEvents()
    return str(events)

@users_routes.route('/getEvent', methods=['GET'])
def getEvent():
    event = database_obj.getEvent(request.form.to_dict())
    return str(event)

@users_routes.route('/removeEvent', methods=['POST'])
def removeEvent():
    database_obj.removeEvent({'ID_Event':request.form['ID_Event']})
    return 'Commited!'

@users_routes.route('/editEvent', methods=['POST'])
def editEvent():
    database_obj.editEvent(request.form.to_dict())
    return 'Commited!'

############################---Category---############################
@users_routes.route('/addCategory', methods=['POST'])
def addCategory():
    database_obj.addCategory()
    return 'Commited!'

@users_routes.route('/getAllCategories')
def getAllCategories():
    categories = database_obj.getAllCategories()
    return str(categories)

@users_routes.route('/getCategory', methods=['GET'])
def getCategory():
    category = database_obj.getCategory(request.form.to_dict())
    return str(category)

@users_routes.route('/removeCategory', methods=['POST'])
def removeCategory():
    database_obj.removeCategory({'ID_category':request.form['ID_category']})
    return 'Commited!'

@users_routes.route('/editCategory', methods=['POST'])
def editCategory():
    database_obj.editCategory(request.form.to_dict())
    return 'Commited!'

############################---Alarm---############################
@users_routes.route('/addAlarm', methods=['POST'])
def addAlarm():
    database_obj.addAlarm()
    return 'Commited!'

@users_routes.route('/getAllAlarms')
def getAllAlarms():
    alarms = database_obj.getAllAlarms()
    return str(alarms)

@users_routes.route('/getAlarm', methods=['GET'])
def getAlarm():
    alarm = database_obj.getAlarm(request.form.to_dict())
    return str(alarm)

@users_routes.route('/removeAlarm', methods=['POST'])
def removeAlarm():
    database_obj.removeAlarm({'ID_Alarm':request.form['ID_Alarm']})
    return 'Commited!'

@users_routes.route('/editAlarm', methods=['POST'])
def editAlarm():
    database_obj.editAlarm(request.form.to_dict())
    return 'Commited!'

############################---AlarmType---############################
@users_routes.route('/addAlarmType', methods=['POST'])
def addAlarmType():
    database_obj.addAlarmType()
    return 'Commited!'

@users_routes.route('/getAllAlarmTypes')
def getAllAlarmTypes():
    alarmTypes = database_obj.getAllAlarmTypes()
    return str(alarmTypes)

@users_routes.route('/getAlarmType', methods=['GET'])
def getAlarmType():
    alarmType = database_obj.getAlarmType(request.form.to_dict())
    return str(alarmType)

@users_routes.route('/removeAlarmType', methods=['POST'])
def removeAlarmType():
    database_obj.removeAlarmType({'ID_AlarmType':request.form['ID_AlarmType']})
    return 'Commited!'

@users_routes.route('/editAlarmType', methods=['POST'])
def editAlarmType():
    database_obj.editAlarmType(request.form.to_dict())
    return 'Commited!'

@users_routes.route('/addEventsCategory', methods=['POST'])
def addEventsCategory():
    database_obj.addEventsCategory()
    return 'Commited!'

@users_routes.route('/getAllEventsCategories')
def getAllEventsCategories():
    eventsCategories = database_obj.getAllEventsCategories()
    return str(eventsCategories)

@users_routes.route('/getEventsCategory', methods=['GET'])
def getEventsCategory():
    eventsCategory = database_obj.getEventsCategory(request.form.to_dict())
    return str(eventsCategory)

@users_routes.route('/removeEventsCategory', methods=['POST'])
def removeEventsCategory():
    database_obj.removeEventsCategory({'ID_EventCateg':request.form['ID_EventCateg']})
    return 'Commited!'

@users_routes.route('/editEventsCategory', methods=['POST'])
def editEventsCategory():
    database_obj.editEventsCategory(request.form.to_dict())
    return 'Commited!'