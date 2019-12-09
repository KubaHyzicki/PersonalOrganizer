import os

class Config(object):
    appDir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'someRandomCakeKey'
    DATABASE='personalOrganizer.db'
    DATABASE_PATH = os.path.join(appDir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

    DEBUG = True
