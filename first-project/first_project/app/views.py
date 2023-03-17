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
    current_time = datetime.utcnow()
    msg = f'Текущее время: {current_time}'
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages,
        'message': [msg]
    }
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст

    return render(request, template_name, context)


def workdir_view(request):
    dir_list = os.listdir()
    msg = [item for item in os.listdir() ]
    msg.insert(0,'Содержимое рабочей директории:')
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
        'message': msg
    }
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст

    return render(request, template_name, context)
    #return HttpResponse(msg)
