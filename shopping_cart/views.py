from django.shortcuts import render
from .cart import Cart
from shop.models import Product, ProductCategory
from django.shortcuts import redirect
# Create your views here.

def add_product(request, product_id):
    cart = Cart(request=request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("shop")

def delete_product(request, product_id):
    cart = Cart(request=request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)
    return redirect("shop")

def subtract_product(request, product_id):
    cart = Cart(request=request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product=product)
    return redirect("shop")

def clear_cart(request):
    cart = Cart(request=request)
    cart.clear_cart()
    return redirect("shop")