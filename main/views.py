from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def my_test(request):
    return render(request, 'main/my_test.html')


def my_test_http_response(request):
    return HttpResponse('<h4>My test "HttpResponse"</h4>')
