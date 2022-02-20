from flask import session
from services.xp import get_access_token

import requests as rq


def render_auth():    
    headers = {
        'Authorization': session.get('xp_token'),
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'PostmanRuntime/7.29.0'
    }
    cookies = session.get('xp_cookies')

    return headers, cookies


def get(url: str, **kwargs):
    headers, cookies = render_auth()

    resp = rq.get(url, headers=headers, cookies=cookies, **kwargs)
    
    if resp.status_code == 401:
        get_access_token()

    resp = rq.get(url, headers=headers, cookies=cookies, **kwargs)

    return resp


def post(url: str, **kwargs):
    headers, cookies = render_auth()

    resp = rq.post(url, headers=headers, cookies=cookies, **kwargs)
    
    if resp.status_code == 401:
        get_access_token()

    resp = rq.post(url, headers=headers, cookies=cookies, **kwargs)

    return resp
