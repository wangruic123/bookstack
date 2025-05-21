# common/selectDB.py
import pymysql
from common.config import ConfigLoader
from common.log import logger


class DBClient:
    def __init__(self):
        config = ConfigLoader().get_db_config()
        self.conn = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database='testdb',
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute_query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()