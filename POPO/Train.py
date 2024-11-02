class Train:
    def __init__(self, train_id: str, run_date: str, is_running: bool):
        self.train_id = train_id
        self.run_date = run_date
        self.is_running = is_running

    def __repr__(self):
        return (f"Train(train_id='{self.train_id}', run_date='{self.run_date}', "
                f"is_running={self.is_running})")