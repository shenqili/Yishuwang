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
class book(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    name_book = models.CharField(max_length=30)
    grade_book = models.CharField(max_length=30)
    discount_book = models.IntegerField(default=3)
    major_book = models.CharField(max_length=30)
    photo_book = models.FileField(upload_to='upload/')

    def __str__(self):
        return self.name_book
