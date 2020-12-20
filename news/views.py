from django.shortcuts import render
from .models import Article


def news_home(request):
    news = Article.objects.all().order_by('-date')
    # news = Article.objects.all().order_by('-date')[:0]
    return render(request, 'news/news_home.html', {'news': news})