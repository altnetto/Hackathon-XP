import requests as rq

from flask import Blueprint, request


bp_bank = Blueprint('bank', __name__, url_prefix='/bank')


