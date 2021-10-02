from django.db import models
from .validators import validate_file_extension

# Create your models here.
class ArtPost(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=1000, blank=True)
  art = models.FileField(upload_to='images/',validators=[validate_file_extension])
