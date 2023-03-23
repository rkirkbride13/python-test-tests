from inventory import inventory

class Item:

    def set_name(self, name):
        if name in inventory['prices'][0]:
            self.name = name
        else:
            raise Exception('This item does not exist on the menu')

    def get_name(self):
        return self.name

    def get_price(self):
        return inventory['prices'][0][self.name]
