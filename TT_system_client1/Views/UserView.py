import tkinter as tk

from TT_system_sever.POPO.AppState import AppState
from .BaseView import BaseView


class UserView(BaseView):
    def __init__(self, master, switch_to_index):
        super().__init__(master)
        self.switch_to_index = switch_to_index
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="个人信息")
        label.pack(pady=20)

        label = tk.Label(self, text=f"用户 ID: {AppState().getContextUser().user_id}")
        label.pack(pady=20)

        button_back = tk.Button(self, text="返回", command=self.switch_to_index)
        button_back.pack(pady=10)
