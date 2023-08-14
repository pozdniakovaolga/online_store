from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from news.models import Article
from pytils.translit import slugify


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview', 'date',)
    success_url = reverse_lazy('news:list')

    def form_valid(self, form):  # динамическое формирование slug name для заголовка при создании статьи
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)[:20]
            new_article.save()

        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    paginate_by = 3  # количество элементов на одну страницу

    def get_queryset(self, *args, **kwargs):  # ограничение на вывод статей (только опубликованные)
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):  # добавление счетчика просмотров
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body', 'preview', 'date',)

    def form_valid(self, form):  # динамическое изменение slug name для заголовка при редактировании статьи
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)[:20]
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):  # после редактирования перенаправление на просмотр статьи
        return reverse("news:view", kwargs={"slug": self.object.slug})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news:list')
