from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html', {'title': 'Home page !!!'})


def about(request):
    return render(request, 'main/about.html')


def my_test(request):
    data = {
        'title': 'Test page !!!',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/my_test.html', data)


def my_test_http_response(request):

    return HttpResponse('<h4>My test "HttpResponse"</h4>')
