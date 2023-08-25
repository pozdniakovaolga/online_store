from django.contrib import admin

from catalog.models import Category, Product, Contacts, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'title', 'product', 'is_active',)
    list_filter = ('product',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_delivery', 'phone_seo', 'email',)
    list_editable = ('phone_delivery', 'phone_seo', 'email',)
