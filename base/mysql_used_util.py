import pymysql


class MysqlUsedUtil:

    def __init__(self):
        self.db = pymysql.connect(
            host="10.20.80.127",
            port=3306,
            user="root",
            password="NjdlZjg2TEyNDE8h3wZmNl",
            database="googutwine_db",
            cursorclass=pymysql.cursors.DictCursor
        )

    def mysql_used_reade(self, sql):
        result = self.db.cursor()
        # execute执行sql
        result.execute(sql)
        response = result.fetchall()
        # 提交
        return response

    def mysql_used_execute(self, sql):
        try:
            self.db.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def __del__(self):
        self.db.close()
