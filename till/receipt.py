class Receipt:
    def __init__(self):
      self.receipt = []

    def add_order(self, order):
      self.order = order

    def print_receipt(self):
       items = self.order.list_items()[0]
       return f"{items[0]:24}{items[1]} x {items[2]}\n"