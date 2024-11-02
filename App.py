import tkinter as tk
from Views.LoginView import LoginView
from Views.IndexView import IndexView
from Views.TicketView import TicketView
from Views.OrderView import OrderView
from Views.UserView import UserView
from Views.RegisterView import RegisterView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("高级软件开发大作业，火车订票系统")
        self.geometry("400x400")
        self.current_view = None
        self.show_login_view()

    def show_login_view(self):
        if self.current_view:
            self.current_view.destroy() # 传入可跳转的view，Login成功跳转Index，或点击按钮跳转register
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


if __name__ == "__main__":
    app = App()
    app.mainloop()
