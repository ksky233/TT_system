from datetime import datetime
from decimal import Decimal


class Order:
    def __init__(self, order_id: int, user_id: int, ticket_id: int,
                 purchase_time: datetime, order_status: str):
        self.order_id = order_id
        self.user_id = user_id
        self.ticket_id = ticket_id
        self.purchase_time = purchase_time
        self.order_status = order_status

    def __repr__(self):
        return (f"Order(order_id={self.order_id}, user_id={self.user_id}, "
                f"ticket_id={self.ticket_id}, purchase_time='{self.purchase_time}', "
                f"order_status='{self.order_status}')")
