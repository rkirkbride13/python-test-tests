class Order:
    
    def __init__(self):
        self.order = []

    def set_name(self, name = '-'):
        self.name = name

    def get_name(self):
        return self.name
    
    def add_item(self, new_item):
        item_already_ordered = False
        for item in self.order:
            if new_item.get_name() in item:
                item[1] += 1
                item_already_ordered = True
        if not item_already_ordered:
            self.order.append([new_item.get_name(), 1, new_item.get_price()])

    def list_items(self):
        return self.order

    def item_total(self):
        item_total = 0
        for item in self.order:
            item_total += item[1] * item[2]
        return item_total

    def calc_tax(self, tax):
        return round(self.item_total() * tax/100, 2)
    
    def calc_bill(self, tax):
        total = self.item_total() + self.calc_tax(tax)
        return round(total, 2)