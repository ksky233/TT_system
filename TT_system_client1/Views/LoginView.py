import tkinter as tk

from TT_system_client1.POPO.AppState import AppState
from TT_system_client1.POPO.User import User
from .BaseView import BaseView


# userService = UserService() 客户端页面信息的获取，不能再直接使用服务端的业务了，需要发送网络请求


class LoginView(BaseView):
    def __init__(self, master, switch_to_register, switch_to_index):
        super().__init__(master)
        # 赋予各种回调方法
        self.switch_to_index = switch_to_index
        self.switch_to_register = switch_to_register  # 这里传递

        # 页面构建方法
        self.create_widgets()

    def create_widgets(self):
        label_login_user_id = tk.Label(self, text="登录账户：")
        label_login_user_id.pack()
        self.entry_login_user_id = tk.Entry(self)
        self.entry_login_user_id.pack()

        label_login_password = tk.Label(self, text="登录密码：")
        label_login_password.pack()
        self.entry_login_password = tk.Entry(self, show="*")
        self.entry_login_password.pack()

        button_login = tk.Button(self, text="登录", command=self.login)
        button_login.pack()

        self.label_status = tk.Label(self, text="")
        self.label_status.pack()

        button_switch = tk.Button(self, text="没有账户? 注册", command=self.switch_to_register)
        button_switch.pack()

    def login(self):
        user_id = self.entry_login_user_id.get()
        password = self.entry_login_password.get()

        # result = userService.checkLogin(user_id, password) 这里不能再直接用服务端方法向数据库请求数据了，应该使用网络请求
        if password:  # 这里的数据暂时写死
            self.label_status.config(text="result.get_message()")
            AppState().setContextUser(User(user_id, None, password))  # 这里的状态共享是属于客户端的
            self.switch_to_index()  # 回调进入index页面的函数参数，容器摧毁当前页面，重新进入新页面
        else:
            self.label_status.config(text="result.get_message()")
