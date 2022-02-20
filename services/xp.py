import requests as rq
import system_variables as sv


MAIN_URL = sv.XP_MAIN_URL


def get_access_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': sv.XP_CLIENT_ID,
        'client_secret': sv.XP_SECRET_KEY
    }

    resp = rq.post(f'{MAIN_URL}access-token',
                   headers=headers,
                   data=data)

    return resp
