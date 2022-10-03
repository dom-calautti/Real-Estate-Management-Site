from datetime import datetime
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'agent_photos/%Y/%m/%d/')
    description = models.TextField(blank=True )
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_MVP = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name

