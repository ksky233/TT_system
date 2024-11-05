from flask import Flask
from TT_system_sever.Tools.CreateDB import db


def create_app():
    app = Flask(__name__)
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/tt_system'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 初始化 SQLAlchemy
    db.init_app(app)
    # 注册蓝图
    from TT_system_sever.Controller.UserController import user_bp
    app.register_blueprint(user_bp)

    with app.app_context():
        db.create_all()  # 创建所有表

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
