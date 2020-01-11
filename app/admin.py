from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'name')
    search_fields = ('name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register your models here.
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Cart)
admin.site.register(models.Category)
admin.site.register(models.UserProfile)