# 创建 SQLAlchemy 实例
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


'''
问题：在App_Server中创建SQLAlchemy和Flask实例，然后在其他文件中导入，报错多实例
可能的原因：如果在某些导入过程中，文件被多次加载，Flask 可能会认为有多个 SQLAlchemy 实例。
解决方案：把SQLAlchemy单独放在此文件中，让App_Server在内的其他全部文件，都导入这个DB
备注：
前面的做法，看起来整个项目根本没用多个数据库或者Flask，但就是报错多实例。这才是最奇怪的点
'''