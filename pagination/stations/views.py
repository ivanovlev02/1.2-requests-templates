import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stat = []
    with open('data-398-2018-08-30.csv', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stat.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    page_number = int(request.GET.get('page', 1))
    pagination = Paginator(stat, 10)
    page = pagination.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)