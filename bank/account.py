
class Account:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if self.latest_balance() < 0:
            raise Exception('Insufficient funds') 
   
    def latest_balance(self):
        return sum([transaction.amount for transaction in self.transactions])
    
    def get_transactions(self):
        return self.transactions
    
    def balance_at(self, transaction_index):
        transactions = self.transactions[0:transaction_index+1]
        return sum([transaction.amount for transaction in transactions])