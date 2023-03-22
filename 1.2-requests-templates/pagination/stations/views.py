from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get('page',1))

    stations:list = []
    with open(settings.BUS_STATION_CSV, 'r', ) as file:
        for row in csv.DictReader(file, ):
            stations.append({'Name':row['Name'], 'Street':row['Street'],'District':row['District']})

    pagi = Paginator(stations, 10)
    context = {
         'bus_stations': pagi.get_page(page_num),
         #'page': pagi.get_page(page_num), # не полял зачем увеличивать колличество передаваемых данных когда уже передается объек  достаточный для пагинации
    }
    return render(request, 'stations/index.html', context)
