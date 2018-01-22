import requests
from constants import (PHPSESSID)

PROTOCOL = 'http:'

DOMAIN = '.qi' + 'chac' + 'ha.com'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'


def get(path, params):
    headers = { 'User-Agent': USER_AGENT, 'Cookie': 'PHPSESSID=%s;' % PHPSESSID }
    r = requests.get('%s//www%s%s' % (PROTOCOL, DOMAIN, path) , params=params, headers=headers)
    print('send request:', r.url)
    return r