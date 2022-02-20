from os import getenv

XP_CLIENT_ID = getenv('XP_CLIENT_ID', 'R80PE1wk2iANgLAMmbujczei8GuTxLc3iunqVe4oYCcCH79P')
XP_SECRET_KEY = getenv('XP_SECRET_KEY', 'ixEimckSrWVRP2oVlrTbqeoEo7G1Zn13AFqyL8NSmNHiXpZNiVQk9038azYAZSxf')
TOKEN_URL = getenv('XP_MAIN_URL', 'https://openapi.xpi.com.br/oauth2/v1/access-token')
MAIN_URL = getenv('MAIN_URL', 'https://openapi.xpi.com.br/openbanking')
