from inventory import inventory

class Item:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_price(self):
        return inventory['prices'][0][self.name]