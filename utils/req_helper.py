from flask import session
from services.xp import get_access_token

import requests as rq


def render_auth():    
    headers = {
        'Authorization': session.get('xp_token')
    }

    cookies = session.get('xp_cookies')

    return headers, cookies


def get(url: str, **kwargs):
    headers, cookies = render_auth()

    resp = rq.get(url, headers=headers, cookies=cookies, **kwargs)
    
    if resp.status_code == 403:
        get_access_token()

    resp = rq.get(url, headers=headers, cookies=cookies, **kwargs)

    return resp


def post(url: str, **kwargs):
    headers, cookies = render_auth()

    resp = rq.post(url, headers=headers, cookies=cookies, **kwargs)
    
    if resp.status_code == 403:
        get_access_token()

    resp = rq.post(url, headers=headers, cookies=cookies, **kwargs)

    return resp
