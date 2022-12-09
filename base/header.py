import time

import yaml

class Header:
    def __init__(self):
        self.a = yaml.safe_load(open("../data/token.yml"))
    def header(self, url):
        a = url.split('?')[0]
        transaction_type = a.split('/')[-1]
        app_id = "10000001"
        time_stamp = str(round(time.time() * 1000))
        token = yaml.safe_load(open('../data/token.yml'))['token']
        resources_id = -999
        message_id = time_stamp
        imei = '671554c651cc966e7b9b12d693c2fb30'
        terminal = '2'
        version = '2.0.0'
        header = {"app_id": app_id, "time_stamp": time_stamp, "transaction_type": transaction_type,
                  "token": token, "resources_id": resources_id, "message_id": message_id,
                  "imei": imei, "terminal": terminal, "version": version}
        print(self.a)
        return header
