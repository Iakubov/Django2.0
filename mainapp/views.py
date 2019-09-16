import random

from django.shortcuts import render, get_object_or_404
import json

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def get_products_menu():
    return ProductCategory.objects.all()


def get_hot_product():
    return random.choice(Product.objects.all())


def same_products(hot_product):
    return hot_product.category.product_set.exclude(pk=hot_product.pk)


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all().order_by('product__category')
    else:
        return []


def main(request):
    featured_products = Product.objects.all()[:4]
    context = {
        'page_title': 'Shop',
        'featured_products': featured_products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    hot_product = get_hot_product()
    context = {
        'page_title': 'Products',
        'products_menu': get_products_menu(),
        'basket': get_basket(request),
        'hot_product': hot_product,
        'same_products': same_products(hot_product),
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    pk = int(pk)
    if pk == 0:
        category = {
            'pk': 0,
            'name': 'all'
        }
        category_products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        category_products = category.product_set.all()

    context = {
        'page_title': 'Category page',
        'products_menu': get_products_menu(),
        'category_products': category_products,
        'category': category,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/category_products.html', context)


def product(request, pk):
        product = get_object_or_404(Product, pk=pk)

        context = {
            'page_title': 'Product page',
            'products_menu': get_products_menu(),
            'category': product.category,
            'object': product,
            'basket': get_basket(request),
        }
        return render(request, 'mainapp/product_page.html', context)


def contacts(request):
    with open("mainapp/json/content.json", "r") as file:
        content = json.load(file)

    context = {
        'page_title': 'Contacts',
        'content': content,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contacts.html', context)