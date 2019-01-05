from django.shortcuts import render
from django.http import HttpResponse
from .models import Fan, Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import mongoengine as mclient
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
import json

def home(request):

    context = {
        "mclient": mclient
    }

    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        new_location = [data['longitude'],data['latitude']]
        Fan.objects(user=str(request.user)).modify(set__currentPosition=new_location, upsert=True)
        print(new_location)

    return render(request, 'geotracker/home.html', context)

def share(request):

    if request.method == 'POST':
        new_post = Post()
        new_post.artist = request.POST.get('artist')
        new_post.venue = request.POST.get('venue')
        new_post.date = str(datetime.datetime.now())
        new_post.starttime = request.POST.get('start_time')
        new_post.endtime = request.POST.get('end_time')
        Fan.objects(user=str(request.user)).update(add_to_set__posts=[new_post])
        messages.success(request, f'Your concert has been shared 🤘')

    return render(request, 'geotracker/share.html')
