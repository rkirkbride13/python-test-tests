class Statement:
    def __init__(self, account):
        self.header = "date || credit || debit || balance\n"
        self.account = account

    def format_transactions(self):
        return [self._format_transaction(transaction, i) for i, transaction in enumerate(self.account.get_transactions())]

    def print_statement(self):
        formatted_statement = self.format_transactions() + [self.header]
        return ''.join(formatted_statement[::-1])[0:-1]

    def _format_transaction(self, transaction, transaction_index):
        balance = self.account.balance_at(transaction_index)
        return f"{transaction.format_date()} || {transaction.format_amount()} || {balance:.2f}\n"
