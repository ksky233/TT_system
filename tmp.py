import tkinter as tk
from Service.UserService import UserService

user_service = UserService()


# 定义注册函数
def register():
    # 获取输入的用户名
    username = entry_username.get()
    # 获取输入的密码
    password = entry_password.get()
    # 获取输入的确认密码
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        # 在状态标签上显示提示信息
        label_status.config(text="密码不一致。")
        return

    result = user_service.registerUser(username, password)
    if result.is_success():
        label_status.config(text=result.get_message())
    else:
        label_status.config(text=result.get_message())


# 定义登录函数
def login():
    # 获取输入的登录用户名
    username = entry_login_username.get()
    # 获取输入的登录密码
    password = entry_login_password.get()

    result = user_service.checkLogin(username, password)
    if result.is_success():
        label_status.config(text=result.get_message())
    else:
        label_status.config(text=result.get_message())


# 创建主窗口
root = tk.Tk()
# 设置窗口标题
root.title("注册与登录")

# 创建“用户名：”标签并添加到窗口
label_username = tk.Label(root, text="用户名：")
label_username.pack()
# 创建用户名输入框并添加到窗口
entry_username = tk.Entry(root)
entry_username.pack()

# 创建“密码：”标签并添加到窗口
label_password = tk.Label(root, text="密码：")
label_password.pack()
# 创建密码输入框并添加到窗口，输入内容显示为星号
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# 创建“确认密码：”标签并添加到窗口
label_confirm_password = tk.Label(root, text="确认密码：")
label_confirm_password.pack()
# 创建确认密码输入框并添加到窗口，输入内容显示为星号
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.pack()

# 创建“注册”按钮并添加到窗口，点击时调用 register 函数
button_register = tk.Button(root, text="注册", command=register)
button_register.pack()

# 创建“登录用户名：”标签并添加到窗口
label_login_username = tk.Label(root, text="登录用户名：")
label_login_username.pack()
# 创建登录用户名输入框并添加到窗口
entry_login_username = tk.Entry(root)
entry_login_username.pack()

# 创建“登录密码：”标签并添加到窗口
label_login_password = tk.Label(root, text="登录密码：")
label_login_password.pack()
# 创建登录密码输入框并添加到窗口，输入内容显示为星号
entry_login_password = tk.Entry(root, show="*")
entry_login_password.pack()

# 创建“登录”按钮并添加到窗口，点击时调用 login 函数
button_login = tk.Button(root, text="登录", command=login)
button_login.pack()

# 创建状态标签并添加到窗口
label_status = tk.Label(root, text="")
label_status.pack()

# 设置窗口尺寸为 400x400
root.geometry("400x400")

# 进入主循环，等待用户操作
root.mainloop()
