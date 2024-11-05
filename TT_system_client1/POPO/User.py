class User:
    def __init__(self, user_id=None, username=None, password=None):
        self.user_id = user_id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(id={self.user_id}, username='{self.username}')"
