from django.contrib import admin
from django.contrib.auth.models import User
from app.models import book , UserProfile

  
class UserProfileAdmin(admin.ModelAdmin):  
    fields = ('user','description',)  
  
admin.site.register(UserProfile, UserProfileAdmin)

class bookAdmin(admin.ModelAdmin):
    list_dispaly = ('name_book','grade_book')

admin.site.register(book,bookAdmin)



