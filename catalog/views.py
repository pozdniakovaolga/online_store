from django.shortcuts import render
from catalog.models import Product, Contacts


def index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    print(Product.objects.all().order_by('-date')[:5])
    return render(request, 'catalog/index.html', context)


def contact(request):
    context = Contacts.objects.get(pk=1).__dict__
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contact.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/products.html', context)
