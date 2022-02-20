import requests as rq

from flask import Blueprint, request


bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.post('/login')
def login_user():
    # try:
    #     data = request.json()
    pass


@bp_user.get('/')
def get_all_users():
    # return User.query.all()
    return 'Hello world'
