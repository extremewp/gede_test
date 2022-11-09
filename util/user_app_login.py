import json
import random

import ddddocr
import requests
import yaml
import pytest
from base.base_api import BaseApi
from util import test_user_app_login_yaml


class UserAppLogin:
    def __init__(self):
        self.ba = BaseApi()

    #     登录密码正确并获取token
    def user_app_login(self):
        res = self.ba.base_api(**yaml.safe_load(open('../data/user_app_login.yml'))['user_app_login'])
        with open('../data/token.yml', 'w') as f:
            data = {"token": res['body']['token']}
            yaml.safe_dump(data=data, stream=f)
        return res

        #     登录密码错误

    def user_app_login_password_file(self):
        res = self.ba.base_api(
            **yaml.safe_load(open('../data/user_app_login.yml'))['test_user_app_login_password_file'])
        return res

        # 登录手机号不足11

    def user_app_login_python_file(self):
        res = self.ba.base_api(**yaml.safe_load(open('../data/user_app_login.yml'))['test_user_app_login_python_file'])
        return res

    def getLoginGraphicVerificationCode(self):
        res = self.ba.base_api(**yaml.safe_load(open('../data/user_app_login.yml'))['test_user_app_login_python_file'])
        return res

        # 获取图文验证码

    def test_getLoginGraphicVerificationCode(self, mobile=None):
        url = "https://gatetest.googutwine.com/user/userLogin/getLoginGraphicVerificationCode"
        if mobile == None:
            mobile = random.choice(['195%08d' % x for x in range(10)])
        else:
            mobile = mobile
        date = {"header": {"app_id": "10000001", "time_stamp": "1665730574364",
                           "transaction_type": "listUserEvaluationBill",
                           "token": "7e17728f09d7a24a83960687a03c9f63",
                           "resources_id": "-999", "message_id": "1665730574364",
                           "imei": "671554c651cc966e7b9b12d693c2fb30", "terminal": "2", "version": "2.0.0"},
                "body": {"mobile": mobile}}
        header = {'Content-Type': 'application/json;charset=UTF-8'
                  }
        date = json.dumps(date)
        res = requests.post(url=url, data=date, headers=header)
        with open('../data/txyzm.jpg', 'wb') as f:
            f.write(res.content)

        # 获取图形验证码内容

    def test_duquyanzhengmaneirong(self, mobile):
        self.test_getLoginGraphicVerificationCode(mobile)
        ocr = ddddocr.DdddOcr()
        with open("../data/txyzm.jpg", "rb") as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        url = "https://gatetest.googutwine.com/user/userLogin/sendValidateCodeByLogin"
        date = {"header": {"app_id": "10000001", "time_stamp": "1665730574364",
                           "transaction_type": "listUserEvaluationBill", "token": "7e17728f09d7a24a83960687a03c9f63",
                           "resources_id": "-999", "message_id": "1665730574364",
                           "imei": "671554c651cc966e7b9b12d693c2fb30", "terminal": "2", "version": "2.0.0"},
                "body": {"mobile": mobile, "graphic_verification_code": res}}
        header = {'Content-Type': 'application/json;charset=UTF-8'
                  }
        date = json.dumps(date)
        res = requests.post(url=url, data=date, headers=header)
        return res.json()
