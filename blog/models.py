from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории"""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Url', max_length=100)
    parent = TreeForeignKey("self", related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Тэги"""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Url', max_length=100)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Post(models.Model):
    """Посты"""
    title = models.CharField('Наименование поста', max_length=200)
    slug = models.SlugField(max_length=250)
    text = models.TextField('Контент')
    created_at = models.DateTimeField('Дата создания поста', auto_now_add=True)
    image = models.ImageField('Фото', upload_to='articles/')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, related_name='post',
                                 null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', related_name='post')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.category.slug, 'post_slug': self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название рецепта')
    serves = models.CharField(max_length=50, verbose_name='Сервис')
    prep_time = models.PositiveIntegerField(default=0, verbose_name='Время готовки')
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField(verbose_name='Ингридиенты')
    directions = models.TextField(verbose_name='Направление еды')
    post = models.ForeignKey(Post, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Comments(models.Model):
    """Комментарии"""
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=100, verbose_name='Email')
    website = models.CharField(max_length=150, verbose_name='WebSite')
    massage = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


