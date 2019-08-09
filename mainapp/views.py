from django.shortcuts import render, get_object_or_404
import json
from mainapp.models import Product, ProductCategory


def get_products_menu():
    return ProductCategory.objects.all()


def main(request):
    products = Product.objects.all()
    context = {
        'page_title': 'Shop',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {
        'page_title': 'Products',
        'products_menu': get_products_menu(),
    }
    return render(request, 'mainapp/product.html', context)


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
        'page_title': 'Products',
        'products_menu': get_products_menu(),
        'category_products': category_products,
        'category': category
    }
    return render(request, 'mainapp/category_products.html', context)


def contacts(request):
    with open("mainapp/json/content.json", "r") as file:
        content = json.load(file)

    context = {
        'page_title': 'Contacts',
        'content': content,
    }
    return render(request, 'mainapp/contacts.html', context)