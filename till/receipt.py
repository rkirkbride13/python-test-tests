class Receipt:
    def __init__(self):
      self.receipt = []

    def add_order(self, order):
      self.order = order

    def print_receipt(self):
       items = self.order.list_items()
       for item in items:
          self.receipt.append(f"{item[0]:24}{item[1]} x {item[2]}\n")
       return ''.join(self.receipt)