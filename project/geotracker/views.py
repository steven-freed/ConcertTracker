from django.shortcuts import render
from django.http import HttpResponse
from .models import Fan, Post, ConcertPost
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import mongoengine as mclient
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
import json

'''
    Class that allows for objects to be json serializable
'''
class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)

def home(request):

    concerts = []

    # gets all concertpost objects from mongo
    for c in ConcertPost.objects:
        new_o = Object()
        new_o.user = c.user
        new_o.userImage = c.userImage
        new_o.artist = c.artist
        new_o.venue = c.venue
        new_o.date = '%s' % c.date
        new_o.starttime = '%s' % c.starttime
        new_o.endtime = '%s' % c.endtime
        concerts.append(new_o.toJSON());

    context = {
        "concerts": concerts
    }

    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        new_location = [data['longitude'],data['latitude']]
        Fan.objects(user=str(request.user)).modify(set__currentPosition=new_location, upsert=True)

    return render(request, 'geotracker/home.html', context)

def share(request):

    if request.method == 'POST':
        new_post = Post(
        artist=request.POST.get('artist'),
        venue=request.POST.get('venue'),
        date=str(datetime.datetime.now()),
        starttime=request.POST.get('start_time'),
        endtime=request.POST.get('end_time')
        )
        new_concert = ConcertPost(
        user=str(request.user),
        userImage=str("/media/%s" % request.user.profile.image),
        artist=request.POST.get('artist'),
        venue=request.POST.get('venue'),
        date=str(datetime.datetime.now()),
        starttime=request.POST.get('start_time'),
        endtime=request.POST.get('end_time')
        )
        Fan.objects(user=str(request.user)).update(add_to_set__posts=[new_post])
        new_concert.save()
        messages.success(request, f'Your concert has been shared 🤘')

    return render(request, 'geotracker/share.html')
