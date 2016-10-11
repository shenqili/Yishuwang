from django.contrib import admin  
from .models import UserProfile  
  
class UserProfileAdmin(admin.ModelAdmin):  
    fields = ('user','description',)  
  
admin.site.register(UserProfile, UserProfileAdmin)