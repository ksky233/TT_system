import tkinter as tk
from .BaseView import BaseView


class OrderView(BaseView):
    def __init__(self, master, switch_to_index):
        super().__init__(master)
        self.switch_to_index = switch_to_index
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="订单查询")
        label.pack(pady=20)

        button_back = tk.Button(self, text="返回", command=self.switch_to_index)
        button_back.pack(pady=10)
