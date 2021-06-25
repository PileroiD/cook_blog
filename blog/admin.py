from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models


# admin.site.register(models.Category)
# admin.site.register(models.Tag)
# admin.site.register(models.Post)
# admin.site.register(models.Recipe)
admin.site.register(models.Comments)


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Категории"""
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    """Тэги"""
    prepopulated_fields = {'slug': ('name',)}


class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    """Посты"""
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'created_at', 'category', 'author', 'get_photo')
    list_display_links = ('id', 'title')
    inlines = [RecipeInLine]

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='50px' >")
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Рецепты"""
    list_display = ('id', 'name', 'prep_time', 'cook_time', 'post')
    list_display_links = ('id', 'name')
