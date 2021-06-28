from django.contrib import admin

from contact import models


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('id', 'name')


class AboutImageInLine(admin.StackedInline):
    model = models.ImageAbout
    extra = 1


@admin.register(models.About)
class ContactModelAdmin(admin.ModelAdmin):
    inlines = [AboutImageInLine]


admin.site.register(models.ContactLink)
admin.site.register(models.ImageAbout)
admin.site.register(models.Social)

