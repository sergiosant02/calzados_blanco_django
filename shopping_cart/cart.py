from shop.models import ProductCategory, Product

class Cart:

    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        cart=self.session.get('cart')
        if not cart:
            cart={}
            self.session['cart']=cart
        self.cart=cart

    def delete(self, product: Product):
        if(str(product.id) in self.cart.keys()):
            del self.cart[str(product.id)]
        self.save_cart()

    def add(self, product: Product, quantity=1):
        if(str(product.id) not in self.cart.keys()):
            self.cart[str(product.id)]={"product_id":product.id, "product_name":product.name,"quantity":1, "price":str(product.price), "image":product.image.url}
        else:
            for key, value in self.cart.items():
                if key==str(product.id):
                    value["quantity"] += 1
                    break
        self.save_cart()

    def subtract(self, product: Product, quantity=1):
        if(str(product.id) in self.cart.keys()):
            for key, value in self.cart.items():
                if key==str(product.id):
                    if value["quantity"]>1:
                        value["quantity"] -= 1
                    else:
                        self.delete(product)
                    break
        self.save_cart()
    
    def clear_cart(self):
        self.cart = {}
        self.save_cart()

    def save_cart(self):
        self.session["cart"]=self.cart
        self.session.modified=True