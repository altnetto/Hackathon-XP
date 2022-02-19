from flask import Blueprint
from models import User


bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.get('/')
def get_all_users():
    # return User.query.all()
    return 'Hello world'
