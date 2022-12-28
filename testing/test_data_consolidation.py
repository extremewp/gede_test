from base.aes_util import AesUtil
from base.mysql_new_util import MysqlNewUtil
from base.mysql_used_util import MysqlUsedUtil


class TestMysqlTest:
    def test_select_new_user(self):
        sql = "select phone from user where 1=1 "
        try:
            date = MysqlNewUtil().mysql_new_reade(sql)
        except:
            print('查询user中phone')
        list_new_user = []
        for date in date:
            if date['phone'] != None:
                date = AesUtil().aes_decrypt(date['phone'])
                list_new_user.append(date)
        return list_new_user

    # 对比老用户是否存在新系统数据库表中
    def test_select_used_user(self):
        list_new_user = self.test_mysql()
        for list_new_user in list_new_user:
            sql = "select  phone from user where phone = " + list_new_user
            used_user = MysqlUsedUtil().mysql_used_reade(sql)
            if used_user == None:
                assert False
                print("没有到该手机号" + list_new_user)
            else:
                assert True
