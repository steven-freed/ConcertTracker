from django.shortcuts import render
from django.http import HttpResponse
from .models import Fan, Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import mongoengine as mclient
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

def home(request):

    context = {
        "mclient": mclient
    }
    # get users location if authenticated
    if request.user.is_authenticated:
        Fan.objects(user=str(request.user)).modify(set__currentPosition=[41.01, 5.02], image='http://localhost:8000/media/%s' % request.user.profile.image, upsert=True)

    return render(request, 'geotracker/home.html', context)

def share(request):

    if request.method == 'POST':
        print(request.POST.get('artist'))
        new_post = Post()
        new_post.artist = request.POST.get('artist')
        new_post.venue = request.POST.get('venue')
        new_post.date = str(datetime.datetime.now())
        new_post.starttime = request.POST.get('start_time')
        new_post.endtime = request.POST.get('end_time')
        Fan.objects(user=str(request.user)).update(add_to_set__posts=[new_post])

    return render(request, 'geotracker/share.html')
