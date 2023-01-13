from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def __str__(self):
        return self.title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def __str__(self):
        return self.title


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
