from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArtPost(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  description = models.TextField(max_length=1000, blank=True)
  hidden = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Art(models.Model):
  art = models.ImageField(upload_to='images/')
  post = models.ForeignKey(ArtPost, on_delete=models.CASCADE)
