from base.mysql_util import MysqlUtil


class TestMysqlTest:
    def test_mysql(self):
        sql = "select phone from user where 1=1"
        date = MysqlUtil().mysql_reade(sql)
        return date