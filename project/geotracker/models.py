from django.db import models
from django.contrib.auth.models import User
'''
class Fan(models.Model):
    fan = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
'''
