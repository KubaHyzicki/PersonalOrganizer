from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import werkzeug

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__='User'

    ID_user = db.Column(db.Integer, primary_key=True, nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    permissions = db.Column(db.String(255), nullable=False)

    authenticated = False

    def __repr__(self):
        return "<User {}:{}>".format(self.ID_user,self.email)

    def update(self, data):
        for key in data:
            if data[key] and key != "ID_user":
                setattr(self, key, data[key])

    def get_id(self):
        return self.ID_user
    
    def set_password(self, password):
        self.password = werkzeug.security.generate_password_hash(password, method='sha256')
    
    def print_hash(self, password):
        return werkzeug.security.generate_password_hash(password, method='sha256')

    def get_permissions(self):
        return self.permissions

    def check_password(self, password):
        return werkzeug.security.check_password_hash(self.password, password)

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

class Event(db.Model):
    
    __tablename__='Event'

    ID_event = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    participants = db.Column(db.String(255), nullable=False)
    creationDate = db.Column(db.DateTime, nullable=False)
    repeatable = db.Column(db.String(255), nullable=False)
    ID_user = db.Column(db.Integer, db.ForeignKey('User.ID_user'), nullable=False)

    def update(self, data):
        for key in data:
            if data[key] and key != "ID_event":
                setattr(self, key, data[key])

    def __repr__(self):
        return "<Event {}>".format(self.name)

class Category(db.Model):
    
    __tablename__='Category'

    ID_category = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    colour = db.Column(db.Integer, nullable=False)

    def update(self, data):
        for key in data:
            if data[key] and key != "ID_category":
                setattr(self, key, data[key])

    def __repr__(self):
        return "<Category {}>".format(self.name)

class EventsCategories(db.Model):
    
    __tablename__='EventsCategories'

    ID_EventCategory = db.Column(db.Integer, primary_key=True, nullable=False)
    ID_category = db.Column(db.Integer, nullable=False)
    ID_event = db.Column(db.Integer, nullable=False)

    def update(self, data):
        for key in data:
            if data[key] and key != "ID_EventCategory":
                setattr(self, key, data[key])

    def __repr__(self):
        return "<ID_category {} -> ID_event {}>".format(self.ID_category,self.ID_event)

class Alarm(db.Model):
    
    __tablename__='Alarm'

    ID_alarm = db.Column(db.Integer, primary_key=True, nullable=False)
    volume_level = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    whenAlarm = db.Column(db.DateTime, nullable=False)
    alarmMethod = db.Column(db.String(255), db.ForeignKey('AlarmType.alarmMethod'), nullable=False)
    ID_event = db.Column(db.Integer, db.ForeignKey('Event.ID_event'), nullable=False)

    def update(self, data):
        for key in data:
            if data[key] and key != "ID_alarm":
                setattr(self, key, data[key])

    def __repr__(self):
        return "<Alarm {} (id={})>".format(self.whenAlarm, self.ID_alarm)

class AlarmType(db.Model):
    
    __tablename__='AlarmType'

    alarmMethod = db.Column(db.String(255), primary_key=True, nullable=False)

    def update(self, data):
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self):
        return "<AlarmType {}>".format(self.alarmMethod)


def query_to_list(query, include_field_names=True):
    column_names = []
    for i, obj in enumerate(query.all()):
        if i == 0:
            column_names = [c.name for c in obj.__table__.columns]
            if include_field_names:
                yield column_names
        yield obj_to_list(obj, column_names)


def obj_to_list(sa_obj, field_order):
    return [getattr(sa_obj, field_name, None) for field_name in field_order]
