from Mapper.UserMapper import UserMapper
from POPO.Result import Result


class UserService:
    def __init__(self):
        self.useMapper = UserMapper()

    def registerUser(self, username, password):
        return self.useMapper.Insert(username, password)

    def checkLogin(self, username, password):
        user = self.useMapper.getByNameAndPwd(username, password)
        if user:
            return Result(True, "登录成功")
        else:
            return Result(False, "用户名或密码错误")
