from django.shortcuts import render
import json

# Create your views here.


def main(request):
    context = {
        'page_title': 'Shop',
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {
        'page_title': 'Products'
    }
    return render(request, 'mainapp/product.html', context)


def contacts(request):
    with open("geekshop/content.json", "r") as file:
        content = json.load(file)

    context = {
        'page_title': 'Contacts',
        'content': content,
    }
    return render(request, 'mainapp/contacts.html', context)