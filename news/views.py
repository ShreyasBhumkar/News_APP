from django.shortcuts import render


def greet(request):
    return render(request, 'news/index.html')
