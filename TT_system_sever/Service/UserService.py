from TT_system_sever.Mapper.UserMapper import UserMapper
from TT_system_sever.POPO.Result import Result


class UserService:
    def __init__(self):
        self.useMapper = UserMapper()

    def registerUser(self, username, password):
        return self.useMapper.insert(username, password)

    def checkLogin(self, username, password):
        user = self.useMapper.get_by_name_and_pwd(username, password)
        if user:
            return Result(True, "登录成功")
        else:
            return Result(False, "用户名或密码错误")

    def getById(self, userId):
        return self.useMapper.get_by_id(userId)

    def getByNameAndPwd(self, userName, pwd):
        return self.useMapper.get_by_name_and_pwd(userName, pwd)
