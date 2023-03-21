
class Account:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return self.transactions
    
    def latest_balance(self):
        return sum([transaction.amount for transaction in self.transactions])