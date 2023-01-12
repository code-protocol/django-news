from django.shortcuts import render
from .models import News


def main_page(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News'
    }
    return render(request, template_name='news/main_page.html', context=context)
