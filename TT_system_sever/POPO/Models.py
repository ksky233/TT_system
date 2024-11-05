from TT_system_sever.Tools.CreateDB import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)


class Train(db.Model):
    __tablename__ = 'train'

    train_id = db.Column(db.String(20), primary_key=True)
    run_date = db.Column(db.Date, nullable=False)
    day_tk_num = db.Column(db.Integer, default=120)  # 默认每列车一天跑一趟
    begin_station = db.Column(db.String(255), nullable=False)
    end_station = db.Column(db.String(255), nullable=False)
    sit_num = db.Column(db.Integer, default=100)  # 默认每列车100座位


class Ticket(db.Model):
    __tablename__ = 'ticket'

    ticket_id = db.Column(db.Integer, primary_key=True)
    begin_station = db.Column(db.String(50), nullable=False)
    end_station = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(8, 2), nullable=False)
    train_id = db.Column(db.String(20), db.ForeignKey('train.train_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sit_type = db.Column(db.Integer, nullable=False)  # 1有座，0无座


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.ticket_id'), nullable=False)
    purchase_time = db.Column(db.DateTime, nullable=False)
    order_status = db.Column(db.String(20), nullable=False)  # '1'：完成，'0'：异常
