from django.shortcuts import render
from django.http import HttpResponse
from .models import Fan
from mongoengine import *

def home(request):
    # context = {
    #    'fans': Fan.objects.all()
    #}
    context = {
        'locations': ''
    }

    # get users location if authenticated
    if request.user.is_authenticated:
        Fan.objects(user=str(request.user)).modify(set__currentPosition=[41.01, 5.02], upsert=True)

    return render(request, 'geotracker/home.html', context)

def about(request):
    return render(request, 'geotracker/about.html')
