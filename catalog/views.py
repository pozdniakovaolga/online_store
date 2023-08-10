from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from catalog.models import Product, Contacts, Category
import os


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


def add_products(request):
    categories_list = Category.objects.all()
    context = {
        'object_list': categories_list
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        preview = request.POST.get('preview')

        if 'preview' in request.FILES:  # если изображение указано
            file = request.FILES['preview']
            fs = FileSystemStorage(location='media/products/')
            filename = fs.save(file.name, file)
            preview = "products/"+os.path.basename(fs.url(filename))
        else:
            preview = 'products/no_image.png'  # если изображение не указано, используем заглушку

        category = request.POST.get('category')
        price = request.POST.get('price')
        date = request.POST.get('date')
        last_update = request.POST.get('date')
        Product.objects.create(title=title, description=description, preview=preview, category_id=category, price=price, date=date, last_update=last_update)
    return render(request, 'catalog/add_products.html', context)
