class Result:
    def __init__(self, success=False, message=None):
        self.success = success
        self.message = message

    def is_success(self):
        return self.success

    def get_message(self):
        return self.message