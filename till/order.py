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
