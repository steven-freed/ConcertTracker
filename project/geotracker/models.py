from django.db import models
from django.contrib.auth.models import User
import mongoengine as mclient

class Post(mclient.EmbeddedDocument):
    artist = mclient.StringField(max_length=255)
    venue = mclient.StringField(max_length=255)
    date = mclient.DateTimeField(auto_now_add=True)
    starttime = mclient.DateTimeField()
    endtime = mclient.DateTimeField()

class Fan(mclient.DynamicDocument):
    _id = mclient.ObjectIdField()
    user = mclient.StringField(max_length=255)
    currentPosition = mclient.PointField()
    friends = mclient.ListField(mclient.StringField(max_length=100))
    posts = mclient.ListField()
    meta = {'collection': 'Fans'}
