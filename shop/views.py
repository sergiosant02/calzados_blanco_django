from django.shortcuts import render

from shop.models import ProductCategory, Product

# Create your views here.


def shop(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'categories': categories, 'products': products})