import tkinter as tk
from .BaseView import BaseView
from TT_system_sever.Service.UserService import UserService

user_service = UserService()  # 这里一样不能再写服务端逻辑了


class RegisterView(BaseView):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.switch_to_login = switch_to_login
        self.create_widgets()

    def create_widgets(self):
        label_username = tk.Label(self, text="用户名：")
        label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        label_password = tk.Label(self, text="密码：")
        label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        label_confirm_password = tk.Label(self, text="确认密码：")
        label_confirm_password.pack()
        self.entry_confirm_password = tk.Entry(self, show="*")
        self.entry_confirm_password.pack()

        button_register = tk.Button(self, text="注册", command=self.register)
        button_register.pack()

        self.label_status = tk.Label(self, text="")
        self.label_status.pack()

        button_switch = tk.Button(self, text="已有账户? 登录", command=self.switch_to_login)
        button_switch.pack()

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if password != confirm_password:
            self.label_status.config(text="密码不一致。")
            return

        result = user_service.registerUser(username, password)
        self.label_status.config(text=result.get_message())
