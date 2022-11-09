import base64
import binascii
import time
import random

from Crypto.Cipher import AES

from util.user_app_login import UserAppLogin


class TestUserAppLogin:
    def setup(self):
        self.ua = UserAppLogin()

    def test_uesr_app_login(self):
        self.ua.test_duquyanzhengmaneirong()
        res = self.ua.user_app_login()
        assert res['header']['message'] == '成功'

    def test_user_app_login_password_file(self):
        res = self.ua.user_app_login_password_file()
        assert res['header']['message'] == '验证码失效,请重新发送验证码'

    def test_user_app_login_python_file(self):
        res = self.ua.user_app_login_python_file()
        assert res['header']['message'] == '成功'

    # 获取验证码间隔时间5分钟提示：“操作台频繁” ；
    def test_5_chaozuopinfan(self):
        mobile = 19520409911
        for i in range(2):
            res = self.ua.test_duquyanzhengmaneirong(mobile)
        assert res['header']['message'] == '操作太频繁'

    # 获取五次验证码
    def test_5_zuidashoujihao(self):
        mobile = 19520409912
        for i in range(5):
            time.sleep(300)
            res = self.ua.test_duquyanzhengmaneirong(mobile)
        assert res['header']['message'] == '成功'

    def test(self):
        try:
            a = 1 / 0
            print(a)
        except ZeroDivisionError:
            print(1)
        finally:
            print(2)

    def add_to_16(self, value):
        while len(value.encode('utf-8')) % 16 != 0:
            value += '\x00'  # 补全, 明文和key都必须是16的倍数
        return value.rstrip()

    def test_AESEncrypt(self):
        try:
            num = 1
            print(num)
            f = open("t.txt")  #
        # except (NameError,IOError) as t:  #打印错误信息,只会打印第一个
        except Exception as t:  # 涵盖所有的报错信息，便于排查
            print("你出错了!")
            print(t)

        """offices =[[],[],[]]
        names = ["a","b","c","d","e","f","g","d"]
        for name in names:
            a = random.randint(0,2)
            offices[a].append(name)#
            i = 1
            for office in offices:
                print("分配个数为%d"%(len(office)),"-"*20)    #
                i += 1
                for name in office:
                    print("对象名字：%s"%name)        #print("\n")        #print("-"*20)
"""
