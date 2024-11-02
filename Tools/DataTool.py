import mysql.connector
from POPO.Result import Result


# 连接数据库
def connect_db():
    try:
        # 连接 MySQL 数据库，指定主机、用户名、密码和数据库名
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tt_system"
        )
        return mydb
    except mysql.connector.Error as err:
        print("出现问题：{}".format(err))
        return None
