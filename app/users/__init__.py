from flask import Blueprint
users_routes = Blueprint('users_routes', __name__)

from . import routes