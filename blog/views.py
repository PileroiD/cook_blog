import random

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog import models


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
