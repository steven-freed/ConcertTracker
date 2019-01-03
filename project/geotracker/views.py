from django.shortcuts import render
from django.http import HttpResponse
#from .models import Fan

locations = [
    {
        'user': 'steve',
        'longitude': 47.00000124,
        'latitude': 140.234540
    },
    {
        'user': 'amanda',
        'longitude': 140.00000124,
        'latitude': -40.234540
    },
    {
        'user': 'scott',
        'longitude': 61.545124,
        'latitude': 130.234540
    }
]

def home(request):
    # context = {
    #    'fans': Fan.objects.all()
    #}
    context = {
        'locations': locations
    }
    return render(request, 'geotracker/home.html', context)

def about(request):
    return HttpResponse(request, '<h1>About</h1>')
