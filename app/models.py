from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__='User'

    ID_user = db.Column(db.Integer, primary_key=True, nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    permissions = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.email)
    
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

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

    def __repr__(self):
        return "<Event {}>".format(self.name)

class Category(db.Model):
    
    __tablename__='Category'

    ID_categ = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    colour = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Category {}>".format(self.name)

class Alarm(db.Model):
    
    __tablename__='Alarm'

    ID_alarm = db.Column(db.Integer, primary_key=True, nullable=False)
    volume_level = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    whenAlarm = db.Column(db.DateTime, nullable=False)
    alarmMethod = db.Column(db.String(255), db.ForeignKey('AlarmType.alarmMethod'), nullable=False)
    ID_event = db.Column(db.Integer, db.ForeignKey('Event.ID_event'), nullable=False)

    def __repr__(self):
        return "<Alarm {} (id={})>".format(self.whenAlarm, self.ID_alarm)

class AlarmType(db.Model):
    
    __tablename__='AlarmType'

    alarmMethod = db.Column(db.String(255), primary_key=True, nullable=False)

    def __repr__(self):
        return "<AlarmType {}>".format(self.alarmMethod)


def query_to_list(query, include_field_names=True):
    """Turns a SQLAlchemy query into a list of data values."""
    column_names = []
    for i, obj in enumerate(query.all()):
        if i == 0:
            column_names = [c.name for c in obj.__table__.columns]
            if include_field_names:
                yield column_names
        yield obj_to_list(obj, column_names)


def obj_to_list(sa_obj, field_order):
    """Takes a SQLAlchemy object - returns a list of all its data"""
    return [getattr(sa_obj, field_name, None) for field_name in field_order]
