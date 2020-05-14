class Cart:
    def __init__(self, products):
        self.products = products
    def show_products(self):
        for i in self.products:
            print(i.name,i.price)