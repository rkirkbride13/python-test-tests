class Receipt:
    def __init__(self):
      self.receipt = []

    def add_order(self, order):
      self.order = order

    def print_receipt(self, tax):
       self.__compile_receipt(tax)
       return ''.join(self.receipt)
    
    # Private methods
    def __compile_receipt(self, tax):
       self.__format_header()
       self.__format_items()
       self.__format_tax(tax)
       self.__format_total(tax) 
    
    def __format_items(self):
       items = self.order.list_items()
       for item in items:
          self.receipt.append(f"{item[0]:24}{item[1]} x {item[2]}\n")

    def __format_tax(self, tax):
       tax = f"{'Tax':24}${self.order.calc_tax(tax):.2f}\n"
       self.receipt.append(tax)

    def __format_total(self, tax):
       total = f"{'Total':24}${self.order.calc_bill(tax):.2f}\n"
       self.receipt.append(total)

    def __format_header(self):
       self.receipt.append(f"{self.order.get_date()}\n")
       self.receipt.append(f"{self.order.get_name()}\n")