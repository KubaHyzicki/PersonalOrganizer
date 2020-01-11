from flask_sqlalchemy import SQLAlchemy
from .models import *

class Database:
    def load(self,app):
        self.db = SQLAlchemy()
        self.db.init_app(app)

############################---User---############################
    def addUser(self, args):
        userRecord = User(
            lastName=args['lastName'],
            email=args["email"],
            firstName=args["firstName"],
            permissions=args["permissions"])
        userRecord.set_password(args["password"])
        self.db.session.add(userRecord)
        self.db.session.commit()

    def getAllUsers(self):
        users = User.query.all()
        return users

    def getUser(self, args):
        try:
            user = User.query.get(args['ID_user'])
            return user
        except KeyError: pass
        try:
            user = User.query.filter(User.email==args['email']).first()
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
            name=args["name"],
            status=args["status"],
            description=args["description"],
            participants=args["participants"],
            creationDate=args["creationDate"],
            repeatable=args["repeatable"],
            ID_user=args["ID_user"])
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

    def getUserEvents(self, data):
        events = Event.query.filter(Event.ID_user == data["ID_user"]).all()
        return events

############################---Category---############################
    def addCategory(self, args):
        categoryRecord = Category(
            name=args["name"],
            description=args["description"],
            weight=args["weight"],
            colour=args["colour"])
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
            name=args["name"],
            description=args["description"],
            weight=args["weight"],
            colour=args["colour"])
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
            volume_level=args["volume_level"],
            active=args["active"],
            whenAlarm=args["whenAlarm"],
            alarmMethod=args["alarmMethod"],
            ID_event=args["ID_event"])
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
            alarmMethod=args["alarmMethod"])
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


database_obj = Database()