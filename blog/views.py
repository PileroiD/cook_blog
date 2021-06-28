import random

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from blog import models
from blog.forms import CommentForm
from blog.models import Comments


class HomeView(ListView):
    model = models.Post
    paginate_by = 8
    template_name = 'blog/home.html'
    extra_context = {
        'random_post': random.choice(models.Post.objects.all()),
        'categories': models.Category.objects.all(),
    }


class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.select_related('category').filter(category__slug=self.kwargs.get('slug'))


class PostDetailView(DetailView):
    model = models.Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    extra_context = {'form': CommentForm()}


class CreateComment(CreateView):
    model = Comments
    form_class = CommentForm
    success_url = '/'

    def form_valid(self, form):
        # print('========================')
        # print(form.instance.post_id) -> None
        # print(self.kwargs.get('pk')) -> post id
        # print(self.object.__class__) -> <class 'NoneType'>
        # print('========================')

        form.instance.post_id = self.kwargs.get('pk')  # создаем инстанцию модели коментариев ( Comments ) и привязываем к ней id поста из которого был отправлен отзыв
        # print(form.instance.post_id) -> post id
        # print(form.instance) -> Comments object (None)
        # print('========================')
        # print(form) -> html формы
        # print('========================')

        self.object = form.save()
        # print('========================')
        # print(form.save()) -> Comments object (post id)
        # print('========================')

        # print('========================')
        # print(self.object) -> Comments object (post id)
        # print(super().form_valid(form)) -> <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/">
        # print('========================')

        return super().form_valid(form)  # перенаправляем на какой-то урл

    def get_success_url(self):
        return self.object.post.get_absolute_url()