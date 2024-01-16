from .models import Product, ProductCategory, FirstProductSpecification, SecondProductSpecification

class ProductManager():
    def __init__(self, product: Product):
        self.product = product
        
    @property
    def get_stock(self, firts_spec_id, second_spec_id):
        if second_spec_id:
            return SecondProductSpecification.objects.filter(id=second_spec_id).first().stock
        elif firts_spec_id:
            return FirstProductSpecification.objects.filter(id=firts_spec_id).first().stock
        else:
            return self.product.stock
        
    @property
    def get_price(self, firts_spec_id, second_spec_id):
        if second_spec_id:
            return SecondProductSpecification.objects.filter(id=second_spec_id).first().price
        elif firts_spec_id:
            return FirstProductSpecification.objects.filter(id=firts_spec_id).first().price
        else:
            return self.product.price
        
    
    def sell(self, firts_spec_id, second_spec_id):
        if second_spec_id:
            second = SecondProductSpecification.objects.filter(id=second_spec_id).first()
            second.stock -= 1
            second.save()
        elif firts_spec_id:
            first = FirstProductSpecification.objects.filter(id=firts_spec_id).first()
            first.stock -= 1
            first.save()
        else:
            self.product.stock -= 1
            self.product.save()
            
    def get_all_product_specs(self):
        first = FirstProductSpecification.objects.filter(product=self.product)
        second = SecondProductSpecification.objects.filter(first_spec__in=first)
        return (self.product, first, second)
    
    