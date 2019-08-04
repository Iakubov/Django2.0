from django.shortcuts import render
import json
from mainapp.models import Product

# Create your views here.


def main(request):
    products = Product.objects.all()
    context = {
        'page_title': 'Shop',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {
        'page_title': 'Products'
    }
    return render(request, 'mainapp/product.html', context)


def contacts(request):
    with open("mainapp/json/content.json", "r") as file:
        content = json.load(file)

    context = {
        'page_title': 'Contacts',
        'content': content,
    }
    return render(request, 'mainapp/contacts.html', context)