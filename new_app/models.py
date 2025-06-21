from django.db import models

# Create your models here.

class Blogger(models.Model):
    Name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
