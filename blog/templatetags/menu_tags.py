from django import template

from blog.models import Category, Post

register = template.Library()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all()  # .order_by('name')
    return {'category_list': category}


@register.inclusion_tag('blog/include/tags/recipes_top_tag.html')
def get_last_posts():
    posts = Post.objects.order_by('-pk')[:5]
    return {'last_posts': posts}