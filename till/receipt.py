class Receipt:
    def __init__(self):
      self.receipt = []

    def add_order(self, order):
      self.order = order

    def print_receipt(self, tax):
       self.receipt.append(f"{self.order.get_date()}\n")
       self.receipt.append(f"{self.order.get_name()}\n")
       items = self.order.list_items()
       for item in items:
          self.receipt.append(f"{item[0]:24}{item[1]} x {item[2]}\n")
       tax = f"{'Tax':24}${self.order.calc_tax(tax):.2f}\n"
       self.receipt.append(tax)
       total = f"{'Total':24}${self.order.calc_bill(tax):.2f}\n"
       self.receipt.append(total)
       return ''.join(self.receipt)