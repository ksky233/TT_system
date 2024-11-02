import mysql.connector
from POPO.Result import Result
from Tools import DataTool


class UserMapper:
    def Insert(self, username, password):
        mydb = DataTool.connect_db()
        if not mydb:
            return Result(False, "数据库连接失败")
        try:
            myCursor = mydb.cursor()  # 游标，执行语句，获取结果，保存上下文数据库状态
            # 在 users 表中查询输入的用户名是否已存在
            myCursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if myCursor.fetchone():  # 从游标中获取结果
                mydb.close()
                return Result(False, "用户已存在")
            # 插入新用户数据的 SQL 语句
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            val = (username, password)
            myCursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            return Result(True, "插入成功")
        except mysql.connector.Error as err:
            print("出现问题：{}".format(err))
            if mydb:
                mydb.close()
            return Result(False, "插入失败")

    def getByNameAndPwd(self, username, password):
        mydb = DataTool.connect_db()
        if not mydb:
            return None
        try:
            myCursor = mydb.cursor()
            myCursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = myCursor.fetchone()
            mydb.close()
            return user
        except mysql.connector.Error as err:
            print("出现问题：{}".format(err))
            if mydb:
                mydb.close()
            return None

    def getById(self, id):
        mydb = DataTool.connect_db()
        if not mydb:
            return None
        try:
            myCursor = mydb.cursor()
            myCursor.execute("SELECT * FROM users WHERE id = %s", (id))
            user = myCursor.fetchone()
            mydb.close()
            return user
        except mysql.connector.Error as err:
            print("出现问题: {}".format(err))
            if mydb:
                mydb.close()
            return None
