from cgitb import text
from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=64, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def get_absolute_url(self):
        return reverse('chat:profile', kwargs={'pk': self.pk })

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Chat(models.Model):
    room_name = models.CharField(max_length=64, blank=False)
    users = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('chat:room', kwargs={'room_name': self.room_name })

    def __str__(self):
        return self.room_name

