import tkinter as tk
from Service.UserService import UserService
'''
BaseView 类：基类，用于简化不同视图的创建。
RegisterView 类：包含注册界面及其逻辑，包含切换到登录的按钮。
LoginView 类：包含登录界面及其逻辑，包含切换到注册的按钮。
App 类：主应用程序类，管理当前视图，并处理登录和注册视图之间的切换。
'''
user_service = UserService()


class BaseView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


class RegisterView(BaseView):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.switch_to_login = switch_to_login
        self.create_widgets()

    def create_widgets(self):
        # 创建用户名标签和输入框
        label_username = tk.Label(self, text="用户名：")
        label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        # 创建密码标签和输入框
        label_password = tk.Label(self, text="密码：")
        label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        # 创建确认密码标签和输入框
        label_confirm_password = tk.Label(self, text="确认密码：")
        label_confirm_password.pack()
        self.entry_confirm_password = tk.Entry(self, show="*")
        self.entry_confirm_password.pack()

        # 创建注册按钮
        button_register = tk.Button(self, text="注册", command=self.register)
        button_register.pack()

        # 创建状态标签
        self.label_status = tk.Label(self, text="")
        self.label_status.pack()

        # 创建切换到登录的按钮
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


class LoginView(BaseView):
    def __init__(self, master, switch_to_register):
        super().__init__(master)
        self.switch_to_register = switch_to_register
        self.create_widgets()

    def create_widgets(self):
        # 创建登录用户名标签和输入框
        label_login_username = tk.Label(self, text="登录用户名：")
        label_login_username.pack()
        self.entry_login_username = tk.Entry(self)
        self.entry_login_username.pack()

        # 创建登录密码标签和输入框
        label_login_password = tk.Label(self, text="登录密码：")
        label_login_password.pack()
        self.entry_login_password = tk.Entry(self, show="*")
        self.entry_login_password.pack()

        # 创建登录按钮
        button_login = tk.Button(self, text="登录", command=self.login)
        button_login.pack()

        # 创建状态标签
        self.label_status = tk.Label(self, text="")
        self.label_status.pack()

        # 创建切换到注册的按钮
        button_switch = tk.Button(self, text="没有账户? 注册", command=self.switch_to_register)
        button_switch.pack()

    def login(self):
        username = self.entry_login_username.get()
        password = self.entry_login_password.get()

        result = user_service.checkLogin(username, password)
        self.label_status.config(text=result.get_message())


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("注册与登录")
        self.geometry("400x400")
        self.current_view = None
        self.show_login_view()

    def show_login_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = LoginView(self, self.show_register_view)
        self.current_view.pack(fill="both", expand=True)

    def show_register_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = RegisterView(self, self.show_login_view)
        self.current_view.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
