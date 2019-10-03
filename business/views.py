from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')


def analysis(request):
    return render(request, 'wireframe.html')