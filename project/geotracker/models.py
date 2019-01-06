from django.db import models
from django.contrib.auth.models import User
import mongoengine as mclient
import datetime

class ConcertPost(mclient.DynamicDocument):
    user = mclient.StringField(max_length=255)
    userImage = mclient.StringField(max_length=255)
    artist = mclient.StringField(max_length=255)
    venue = mclient.StringField(max_length=255)
    date = mclient.DateTimeField(default=datetime.datetime.utcnow)
    starttime = mclient.DateTimeField()
    endtime = mclient.DateTimeField()
    meta = {'collection': 'Concerts'}

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
    posts = mclient.EmbeddedDocumentListField(document_type=Post)
    meta = {'collection': 'Fans'}
