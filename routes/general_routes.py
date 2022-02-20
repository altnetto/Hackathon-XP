from utils import req_helper as rq
import system_variables as sv

from flask import Blueprint, request, session
from services.xp import get_access_token


bp_general = Blueprint('general', __name__)


@bp_general.get('/users')
def get_users():
    resp = rq.get(sv.MAIN_URL + '/users')

    return resp
