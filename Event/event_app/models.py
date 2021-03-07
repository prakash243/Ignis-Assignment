from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=254)
    data = models.CharField(max_length=254)
    date_time = models.DateTimeField(auto_now_add=False)
    location = models.CharField(max_length=254)
    image = models.ImageField(upload_to='upload/images',default='https://dummyimage.com/300x400/e0bfe0/202129.jpg&text=Event', blank=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name

class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_id = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.liked_id
