from django.shortcuts import render, redirect
from django.views import View
from catalog.models import Product, Contacts, Version
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory

from catalog.services import get_cashed_category_list


class AccessRightsMixinView(View):
    """Миксин ограничения доступа для неавторизованных пользователей"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('catalog:access_error')
        return super().dispatch(request, *args, **kwargs)


class IndexView(TemplateView):
    """Контроллер просмотра домашней страницы"""
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        print(Product.objects.all().order_by('-date')[:5])  # вывод в консоль последних 5 продуктов
        context_data['object_list'] = Product.objects.all()
        context_data['category_list'] = get_cashed_category_list()
        return context_data


class ContactView(TemplateView):
    """Контроллер просмотра контактов"""
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Contacts.objects.all().order_by('-id')[:1]  # актуальные контактные данные
        return context_data

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


class ProductCreateView(AccessRightsMixinView, CreateView):
    """Контроллер создания продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):  # автоматическое формирование автора продукта
        if form.is_valid():
            product = form.save()
            product.created_by = self.request.user
            product.save()

        return super().form_valid(form)


class ProductUpdateView(AccessRightsMixinView, UpdateView):
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

        # проверка наличия единственной активной версии у продукта
        active_versions = Version.objects.filter(product=self.object, is_active=True)
        if active_versions.count() > 1:
            form.add_error(None, 'Выберите только одну активную версию')
            return self.form_invalid(form)

        return super().form_valid(form)


class ProductDetailView(DetailView):
    """Контроллер просмотра отдельного продукта"""
    model = Product


class ProductDeleteView(AccessRightsMixinView, DeleteView):
    """Контроллер удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class AccessErrorView(TemplateView):
    """Контроллер ошибки доступа"""
    template_name = 'catalog/access_error.html'
