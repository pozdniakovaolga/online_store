from django import forms

from news.models import Article


class ArticleForm(forms.ModelForm):
    """Форма для создания/редактирования статьи"""
    class Meta:
        model = Article
        fields = "__all__"

    def __init__(self, *args, **kwargs):  # стилизация формы
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'
