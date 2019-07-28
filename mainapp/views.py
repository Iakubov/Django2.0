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

    content = [
        {
            "city": "Los Angeles",
            "phone": "8-800-800-800",
            "email": "los-a@gmail.com",
            "adress": "LA",
        },
        {
            "city": "Houston",
            "phone": "8-555-555-555",
            "email": "houston@gmail.com",
            "adress": "HU",
        },
        {
            "city": "Austin",
            "phone": "8-9990-80990-8090",
            "email": "austin@gmail.com",
            "adress": "AU",
        },
    ]

    context = {
        'page_title': 'Contacts',
        'content': content,
    }

    return render(request, 'mainapp/contacts.html', context, content)