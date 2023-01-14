from django.shortcuts import render
from .models import News


def main_page(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News'
    }
    return render(request, template_name='news/main_page.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    context = {
        'news': news,
        'title': 'News by category'
    }
    return render(request, template_name='news/main_page.html', context=context)
