from datetime import datetime
from decimal import Decimal


class Ticket:
    def __init__(self, ticket_id: int, begin_station: str, end_station: str,
                 begin_time: datetime, end_time: datetime, price: Decimal,
                 ticket_num: int, train_id: str, user_id: int):
        self.ticket_id = ticket_id
        self.begin_station = begin_station
        self.end_station = end_station
        self.begin_time = begin_time
        self.end_time = end_time
        self.price = price
        self.ticket_num = ticket_num
        self.train_id = train_id
        self.user_id = user_id

    def __repr__(self):
        return (f"Ticket(ticket_id={self.ticket_id}, "
                f"begin_station='{self.begin_station}', end_station='{self.end_station}', "
                f"begin_time='{self.begin_time}', end_time='{self.end_time}', "
                f"price={self.price}, ticket_num={self.ticket_num}, "
                f"train_id='{self.train_id}', user_id={self.user_id})")
