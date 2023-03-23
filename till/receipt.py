class Receipt:
    def __init__(self):
      self.receipt = []

    def add_order(self, order):
      self.order = order

    def print_receipt(self):
       items = self.order.list_items()
       for item in items:
          self.receipt.append(f"{item[0]:24}{item[1]} x {item[2]}\n")
       tax = f"{'Tax':24}${self.order.calc_tax():.2f}\n"
       self.receipt.append(tax)
       return ''.join(self.receipt)