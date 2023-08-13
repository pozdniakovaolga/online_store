from django.shortcuts import render
from catalog.models import Product, Contacts, Category
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):  # переопределяем метод
        context_data = super().get_context_data(**kwargs)  # вызываем метод у родительского класса
        print(Product.objects.all().order_by('-date')[:5])  # выводим в консоль последние 5 продуктов
        context_data['object_list'] = Product.objects.all()  # новые данные
        return context_data


class ProductListView(ListView):
    model = Product
    paginate_by = 9  # количество элементов на одну страницу


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'
    contact_data = Contacts.objects.get(pk=1)  # контактные данные
    extra_context = {
        'object': contact_data
    }

    def post(self, request):  # добавляем метод post
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')  # выводим информацию в консоль
        return render(request, 'catalog/contact.html', self.extra_context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'preview', 'category', 'price', 'date', 'last_update')
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):  # переопределяем метод
        context_data = super().get_context_data(**kwargs)  # вызываем метод у родительского класса
        context_data['object_list'] = Category.objects.all()  # новые данные
        return context_data
#
#
# Тот же функционал в FBV
#
#from django.core.files.storage import FileSystemStorage
#from django.shortcuts import render
#from catalog.models import Product, Contacts, Category
#import os
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#
#def index(request):
#    products_list = Product.objects.all()
#    context = {
#        'object_list': products_list
#    }
#    print(Product.objects.all().order_by('-date')[:5])
#    return render(request, 'catalog/index.html', context)
#
#def products(request):
#    products_list = Product.objects.all().order_by('-id')  # получаем отсортированный список всех продуктов
#    paginator = Paginator(products_list, 9)  # передаём классу Paginator список, указываем кол. элементов на одну стр.
#    page = request.GET.get('page')
#    try:
#        prods = paginator.page(page)
#    except PageNotAnInteger:
#        prods = paginator.page(1)
#    except EmptyPage:
#        prods = paginator.page(paginator.num_pages)
#
#    context = {
#        'object_list': prods
#    }
#
#    return render(request, 'catalog/product_list.html', context)
#
#def contact(request):
#    context = Contacts.objects.get(pk=1).__dict__
#    if request.method == 'POST':
#        name = request.POST.get('name')
#        phone = request.POST.get('phone')
#        message = request.POST.get('message')
#        print(f'You have new message from {name}({phone}): {message}')
#    return render(request, 'catalog/contact.html', context)
#
#def add_products(request):
#    categories_list = Category.objects.all()
#    context = {
#        'object_list': categories_list
#    }
#    if request.method == 'POST':
#        title = request.POST.get('title')
#        description = request.POST.get('description')
#        preview = request.POST.get('preview')
#
#        if 'preview' in request.FILES:  # если изображение указано
#            file = request.FILES['preview']
#            fs = FileSystemStorage(location='media/products/')
#            filename = fs.save(file.name, file)
#            preview = "products/"+os.path.basename(fs.url(filename))
#        else:
#            preview = 'products/no_image.png'  # если изображение не указано, используем заглушку
#
#        category = request.POST.get('category')
#        price = request.POST.get('price')
#        date = request.POST.get('date')
#        last_update = request.POST.get('date')
#        Product.objects.create(title=title, description=description, preview=preview, category_id=category, price=price, date=date, last_update=last_update)
#    return render(request, 'catalog/product_form.html', context)
