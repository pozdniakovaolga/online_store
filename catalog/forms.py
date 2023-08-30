from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    """Форма для создания/редактирования продукта"""
    class Meta:
        model = Product
        exclude = ('created_by',)

    def __init__(self, *args, **kwargs):  # стилизация формы
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):  # ограничение на использование слов в названии продукта
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        cleaned_data = self.cleaned_data['title']
        for word in prohibited_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Название продукта не может содержать слово: {word}")
        return cleaned_data

    def clean_description(self):  # ограничение на использование слов в описании продукта
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        cleaned_data = self.cleaned_data['description']
        for word in prohibited_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Описание продукта не может содержать слово: {word}")
        return cleaned_data


class VersionForm(forms.ModelForm):
    """Форма для создания/редактирования версии продукта"""
    class Meta:
        model = Version
        fields = "__all__"

    def __init__(self, *args, **kwargs):  # стилизация формы
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
