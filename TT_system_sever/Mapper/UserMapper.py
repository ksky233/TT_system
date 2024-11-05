import mysql.connector

from TT_system_sever.Tools.CreateDB import db
from TT_system_sever.POPO.Models import User
from TT_system_sever.POPO.Result import Result


class UserMapper:
    @staticmethod
    def insert(username, password):
        # 检查用户是否存在
        if User.query.filter_by(username=username).first():
            return Result(False, "用户已存在")

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        try:
            db.session.commit()
            return Result(True, "插入成功")
        except Exception as e:
            db.session.rollback()
            print(f"出现问题：{e}")
            return Result(False, "插入失败")

    @staticmethod
    def get_by_name_and_pwd(username, password):
        user = User.query.filter_by(username=username, password=password).first()
        return user

    @staticmethod
    def get_by_id(user_id):
        user = User.query.get(user_id)
        return user
