import json

import requests

from base.header import Header
from base.sign_api import SignApi
from base.url import Url


class BaseApi:
    def __init__(self):
        self.sa = SignApi()
        self.hd = Header()
        self.url = Url()

    def base_api(self, **data):
        ip = "https://gatetest.googutwine.com"
        method = data['method']
        header = data['header']
        data_header = self.hd.header(data['url'])
        data['data']['header'] = data_header
        date_time = data['data']['header']['time_stamp']
        date = json.dumps(data['data'])
        url = self.url.url(ip, data['url'], self.sa.sign_api(date, date_time))
        if method == 'post':
            res = requests.post(url=url, data=date, headers=header)
        else:
            res = requests.get(url=url, params=date, headers=header)
        return res.json()
