
class Product:
    def __init__(self, _name=None, _price=None):
        self.count = 0
        self.name = _name
        self.price = _price
        self.total = 0.0

    def printProduct(self):
        print("\t", self.count, "    ",   self.name, "    ",  self.price, "    ",  self.total)
