import tkinter as tk
from .BaseView import BaseView
from Service.UserService import UserService

user_service = UserService()

class LoginView(BaseView):
    def __init__(self, master, switch_to_register, switch_to_index):
        super().__init__(master)
        self.switch_to_index = switch_to_index
        self.switch_to_register = switch_to_register
        self.create_widgets()

    def create_widgets(self):
        label_login_username = tk.Label(self, text="登录用户名：")
        label_login_username.pack()
        self.entry_login_username = tk.Entry(self)
        self.entry_login_username.pack()

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
        username = self.entry_login_username.get()
        password = self.entry_login_password.get()

        result = user_service.checkLogin(username, password)
        if result.is_success():
            self.label_status.config(text=result.get_message())
            self.switch_to_index()
        else:
            self.label_status.config(text=result.get_message())
