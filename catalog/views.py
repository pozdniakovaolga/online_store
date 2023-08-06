from django.shortcuts import render
from catalog.models import Product, Contacts


def index(request):
    print(Product.objects.all().order_by('-date')[:5])
    return render(request, 'catalog/index.html')


def contact(request):
    contact_info = Contacts.objects.get(pk=1).__dict__
    print (contact_info)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contact.html', contact_info)
