import tkinter as tk
from .BaseView import BaseView


class IndexView(BaseView):
    def __init__(self, master, switch_to_ticket, switch_to_order, switch_to_user):
        super().__init__(master)
        self.switch_to_ticket = switch_to_ticket
        self.switch_to_order = switch_to_order
        self.switch_to_user = switch_to_user
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="请选择业务操作")
        label.pack(pady=20)

        button_ticket = tk.Button(self, text="购票业务", command=self.switch_to_ticket)
        button_ticket.pack(pady=10)

        button_order = tk.Button(self, text="订单查询", command=self.switch_to_order)
        button_order.pack(pady=10)

        button_user = tk.Button(self, text="个人信息", command=self.switch_to_user)
        button_user.pack(pady=10)
