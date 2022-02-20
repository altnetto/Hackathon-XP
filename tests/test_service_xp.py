from services import xp


def test_get_access_token():
    resp = xp.get_access_token()

    assert resp.status_code == 200
