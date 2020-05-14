from product import Product
from cart import Cart

p1 = Product("product1",1000)
p2 = Product("product2",2000)
p3 = Product("product3",3000)
products=[p1,p2,p3]
c1 = Cart(products)
c1.show_products()