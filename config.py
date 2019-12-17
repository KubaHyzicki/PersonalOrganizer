import os

class Config(object):
    HOST = os.getenv('HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    ADMIN_DB_USER = os.getenv('ADMIN_DB_USER')
    ADMIN_DB_PASS = os.getenv('ADMIN_DB_PASS')
    CLIENT_DB_USER = os.getenv('CLIENT_DB_USER')
    CLIENT_DB_PASS = os.getenv('CLIENT_DB_PASS')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'mysql://' + str(DB_USER) + ':' + str(DB_PASS) + '@localhost/' + str(DB_NAME)
    DEBUG = True