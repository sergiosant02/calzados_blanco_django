from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from shop.models import ProductCategory, Product, ProductImage, FirstProductSpecification

# Create your views here.


def shop(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    for product in products:
        first_spec = FirstProductSpecification.objects.filter(product=product).first()
        images = list(ProductImage.objects.filter(Q(product=product) | Q(first=first_spec)))
        if len(images) > 0:
            product.image = images[0]
    
    return render(request, 'shop/shop.html', {'categories': categories, 'products': products})

def details(request, id):
    product = get_object_or_404(Product, pk=id)
    print(product)
    first_spec = FirstProductSpecification.objects.filter(product=product).first()
    images = list(ProductImage.objects.filter(Q(product=product) | Q(first=first_spec)))
    if len(images) > 0:
        product.images = images
    return render(request, 'shop/details.html', {'product': product})