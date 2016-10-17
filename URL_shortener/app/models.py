from django.db import models

from datetime import datetime, timedelta

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.

# class Click(models.Model):
    # user = models.ManyToManyField(auth.user)

class Bookmark(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)



class Profile(models.Model):

    user = models.OneToOneField('auth.User')
    bookmark = models.ManyToManyField('Bookmark')

    @receiver(post_save, sender='auth.User')
    def create_user_profile(**kwargs):
        created = kwargs.get('created')
        instance = kwargs.get('instance')
        if created:
            Profile.objects.create(user=instance)
