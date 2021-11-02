from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
  avatar = models.ImageField(upload_to='avatars/', default='avatars/default.svg')
  bio = models.TextField(max_length=1000, blank=True)
  friends = models.ManyToManyField('self', related_name='friends', blank=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
