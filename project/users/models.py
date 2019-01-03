from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

'''
class Post(DynamicDocument):
    user = StringField(max_length=255)
    artist = StringField(max_length=255)
    venue = StringField(max_length=255)
    date = DateTimeField(auto_now_add=True)
    start_time = DateTimeField()
    end_time = DateTimeField()

class Fan(DynamicDocument):
    _id = ObjectIdField()
    user = StringField(max_length=255)
    image = ImageField(default='default.jpeg', upload_to='profile_pics')
    posts = ListField(
        model_container=Post,
    )
'''
