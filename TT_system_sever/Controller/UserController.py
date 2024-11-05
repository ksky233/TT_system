from flask import Blueprint, request, jsonify
from TT_system_sever.Service.UserService import UserService

user_bp = Blueprint('user', __name__)
userService = UserService()

@user_bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if userService.getByNameAndPwd(username, password):
        return jsonify({"message": "用户已存在"}), 400

    userService.registerUser(username, password)
    return jsonify({"message": "注册成功"}), 201

# @user_bp.route('/login', methods=['POST'])
# def login():
#     username = request.json.get('username')
#     password = request.json.get('password')
#
#     if username not in users or users[username] != password:
#         return jsonify({"message": "用户名或密码错误"}), 401
#
#     return jsonify({"message": "登录成功"}), 200
