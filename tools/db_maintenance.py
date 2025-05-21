# tools/db_maintenance.py
from common.selectDB import DBClient
from common.log import logger

class DBMaintenance:
    @staticmethod
    def backup_database():
        """执行数据库备份"""
        try:
            client = DBClient()
            backup_sql = "BACKUP DATABASE testdb TO DISK='/backups/testdb.bak'"
            client.execute_query(backup_sql)
            logger.info("数据库备份成功")
        except Exception as e:
            logger.error(f"数据库备份失败：{str(e)}")
            raise

    @staticmethod
    def clean_test_data():
        """清理测试数据"""
        try:
            client = DBClient()
            tables = ["temp_users", "test_vehicles"]
            for table in tables:
                client.execute_query(f"TRUNCATE TABLE {table}")
            logger.info("测试数据清理完成")
        except Exception as e:
            logger.error(f"数据清理失败：{str(e)}")
            raise

if __name__ == "__main__":
    DBMaintenance.backup_database()
    DBMaintenance.clean_test_data()