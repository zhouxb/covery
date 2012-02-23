from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    address = models.TextField()

def create(sender, instance, signal, *args, **kwargs):
    user = instance
    try:
        UserProfile.objects.get(user=user)
    except:
        UserProfile.objects.create(user=user)

post_save.connect(create, sender=User)

