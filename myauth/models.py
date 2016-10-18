"""
Definition of models.
"""

from django.db import models  
from django.contrib.auth.models import User  
from django.db.models.signals import post_save  
  
class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    description = models.TextField(max_length=51200)   
  
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
  
post_save.connect(create_user_profile, sender=User)
