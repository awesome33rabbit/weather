from pymysql import *

class MysqlPython:
    def __init__(self,
                host='localhost',
                user='root',
                password='123456',
                port=3306,
                database='weather_data',
                charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.database = database

    def open(self):
        self.db = connect(host=self.host,
                          user=self.user,
                          password=self.password,
                          port=self.port,
                          database=self.database,
                          charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def execute_database(self, sql):
        try:
            self.open()
            self.cur.execute(sql)
            self.db.commit()
            # print('OK')
        except Exception as e:
            self.db.rollback()
            print('Failed', e)
        self.close()