from django.shortcuts import render
from catalog.models import Product, Contacts, Version
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory


class IndexView(TemplateView):
    """Контроллер просмотра домашней страницы"""
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):  # переопределение метода
        context_data = super().get_context_data(**kwargs)  # вызов метода у родительского класса
        print(Product.objects.all().order_by('-date')[:5])  # вывод в консоль последних 5 продуктов
        context_data['object_list'] = Product.objects.all()  # добавление новых данных
        return context_data


class ContactView(TemplateView):
    """Контроллер просмотра контактов"""
    template_name = 'catalog/contact.html'
    contact_data = Contacts.objects.get(pk=1)  # контактные данные
    extra_context = {
        'object': contact_data
    }

    def post(self, request):  # добавление метода post
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')  # вывод информации в консоль
        return render(request, 'catalog/contact.html', self.extra_context)


class ProductListView(ListView):
    """Контроллер просмотра списка продуктов"""
    model = Product
    paginate_by = 9  # количество элементов на одну страницу


class ProductCreateView(CreateView):
    """Контроллер создания продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    """Контроллер редактирования продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):  # формирование формсета с версиями продукта
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        # проверка на наличие единственной активной версии у продукта
        active_versions = Version.objects.filter(product=self.object, is_active=True)
        if active_versions.count() > 1:
            form.add_error(None, 'Выберите только одну активную версию')
            return self.form_invalid(form)

        return super().form_valid(form)


class ProductDetailView(DetailView):
    """Контроллер просмотра отдельного продукта"""
    model = Product


class ProductDeleteView(DeleteView):
    """Контроллер удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')
