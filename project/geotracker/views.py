from django.shortcuts import render
from django.http import HttpResponse
from .models import Fan
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import mongoengine as mclient
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):

    context = {
        "mclient": mclient
    }
    # get users location if authenticated
    if request.user.is_authenticated:
        Fan.objects(user=str(request.user)).modify(set__currentPosition=[41.01, 5.02], image='http://localhost:8000/media/%s' % request.user.profile.image, upsert=True)

    return render(request, 'geotracker/home.html', context)

def share(request):
    return render(request, 'geotracker/share.html')
