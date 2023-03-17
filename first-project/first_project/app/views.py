import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages,
        'tittle': '',
        'message':[]
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages,
        'tittle': 'Текущее время:',
        'message': [datetime.utcnow()]
    }
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст

    return render(request, template_name, context)


def workdir_view(request):

    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages,
        'tittle':'Содержимое рабочей директории:',
        'message': os.listdir()
    }
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст

    return render(request, template_name, context)
    #return HttpResponse(msg)
