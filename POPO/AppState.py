# 单例模式管理全局属性
from POPO.User import User

class AppState:
    _instance = None
    contextUser = None  # 定义上下文用户属性

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
        return cls._instance

    def setContextUser(self, contextUser):
        if self.contextUser is None:
            self.contextUser = contextUser

    def getContextUser(self):
        return self.contextUser


    # def set_user_id(self, user_id):
    #     self.user_id = user_id  # 设置用户 ID
    #
    # def get_user_id(self):
    #     return self.user_id  # 获取用户 ID
