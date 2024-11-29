from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination import settings
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations_list = []

    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations_list.append(row)
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list, 10)
    page_obj = paginator.get_page(page_number)    
    context = {
        'bus_stations': page_obj,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
