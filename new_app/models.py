from django.db import models

# Create your models here.

class Blogger(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    image = models.FileField(upload_to='blogger_image/')
