import tkinter as tk
from .BaseView import BaseView
from Service.UserService import UserService

userService = UserService()


class LoginView(BaseView):
    def __init__(self, master, switch_to_register, switch_to_index, set_context_user_id):
        super().__init__(master)
        # 赋予各种回调方法
        self.switch_to_index = switch_to_index
        self.switch_to_register = switch_to_register  # 这里传递
        self.set_context_user_id = set_context_user_id

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

        result = userService.checkLogin(user_id, password)
        if result.is_success():
            self.label_status.config(text=result.get_message())
            self.set_context_user_id(user_id)  # 调用父类的设置方法，传递id（这里可以修改成传递user对象）
            self.switch_to_index()  # 回调进入index页面的函数参数，容器摧毁当前页面，重新进入新页面
        else:
            self.label_status.config(text=result.get_message())
