import tkinter as tk

from TT_system_client1.Views.LoginView import LoginView
from TT_system_client1.Views.IndexView import IndexView
from TT_system_client1.Views.TicketView import TicketView
from TT_system_client1.Views.OrderView import OrderView
from TT_system_client1.Views.UserView import UserView
from TT_system_client1.Views.RegisterView import RegisterView

'''
一个显示页面的函数，包含回调函数作为参数，当这个页面完成其逻辑需要跳转时，就调用这个回调函数进行跳转
例如：
App构造时，调用self.show_login_view()，将当前页面设置为self.current_view = LoginView显示登陆页面，
程序进入到LoginView(self, self.show_register_view, self.show_index_view)并且执行业务逻辑，
当登录页面业务完成后，里面会调用某回调函数，例如show_index_view，这时App就执行 def show_index_view(self):函数
在此函数中App继续摧毁当前页面，重新显示IndexView，并开始其内部逻辑，同时IndexView也有必要的回调函数
以此类推，来管理整个App的页面
'''



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("高级软件开发大作业，火车订票系统")
        self.user_id = None  # 存储用户 ID，通过页面构建函数的参数传递给不同页面
        self.geometry("400x400")
        self.current_view = None
        self.show_login_view()  # 构造App后直接调用登录View

    #  -----------------页面跳转回调函数
    def show_login_view(self):  # self.show_register_view是一个函数参数
        if self.current_view:
            self.current_view.destroy()  # 传入跳转view的函数，Login成功跳转Index，或点击按钮跳转register
        self.current_view = LoginView(self, self.show_register_view, self.show_index_view)
        self.current_view.pack(fill="both", expand=True)  # fill 填充方向x，y expand填充方式，铺满

    def show_register_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = RegisterView(self, self.show_login_view)
        self.current_view.pack(fill="both", expand=True)

    def show_index_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = IndexView(self, self.show_ticket_view, self.show_order_view, self.show_user_view)
        self.current_view.pack(fill="both", expand=True)

    def show_ticket_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = TicketView(self, self.show_index_view)
        self.current_view.pack(fill="both", expand=True)

    def show_order_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = OrderView(self, self.show_index_view)
        self.current_view.pack(fill="both", expand=True)

    def show_user_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = UserView(self, self.show_index_view)
        self.current_view.pack(fill="both", expand=True)

    #  -----------------业务逻辑回调函数
    def set_context_user_id(self, user_id):
        self.user_id = user_id
        print(f"用户 ID 已设置为: {self.user_id}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
