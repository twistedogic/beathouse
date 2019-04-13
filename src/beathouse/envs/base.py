class Bankroll:
    def __init__(self, start=1000):
        self.start = start
        self.balance = start
        self.history = [start]

    def _reset(self):
        self.balance = self.start
        self.history = [self.start]

    def get_history(self):
        return self.history

    def update(self, change):
        self.balance += change
        self.history.append(self.balance)
        return self.balance
