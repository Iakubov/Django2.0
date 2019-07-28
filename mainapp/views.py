from django.shortcuts import render

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
    context = {
        'page_title': 'Contacts'
    }

    return render(request, 'mainapp/contacts.html', context)