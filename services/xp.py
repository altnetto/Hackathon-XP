import requests as rq
import system_variables as sv


TOKEN_URL = sv.TOKEN_URL


def get_access_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'PostmanRuntime/7.29.0'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': sv.XP_CLIENT_ID,
        'client_secret': sv.XP_SECRET_KEY
    }

    resp = rq.post(TOKEN_URL,
                   headers=headers,
                   data=data)

    return resp
