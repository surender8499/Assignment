from django.contrib.admin import options
from django.db import models


# Create your models here.

class Members(models.Model):

    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
