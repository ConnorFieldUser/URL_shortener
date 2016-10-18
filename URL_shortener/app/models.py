from django.db import models

# from datetime import datetime, timedelta

# Create your models here.

# class Click(models.Model):

# bookmark fk

# modified time


class Bookmark(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    url = models.CharField(max_length=60)
    newrl = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')
    private = models.BooleanField()
