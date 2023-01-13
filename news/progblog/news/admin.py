from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
