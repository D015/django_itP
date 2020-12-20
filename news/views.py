from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def news_home(request):
    # news = Article.objects.all().order_by('-date')[:0]
    news = Article.objects.all().order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Form with error'
    form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
