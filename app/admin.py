from django.contrib import admin
from django.contrib.auth.models import User
from app.models import book , UserProfile , NeedBook

  
class UserProfileAdmin(admin.ModelAdmin):  
    fields = ('user','description','school','major','contact')  
  
admin.site.register(UserProfile, UserProfileAdmin)

class bookAdmin(admin.ModelAdmin):
    list_dispaly = ('name_book','grade_book')

admin.site.register(book,bookAdmin)

class NeedBookAdmin(admin.ModelAdmin):
    list_dispaly = ('need_book_name')

admin.site.register(NeedBook,NeedBookAdmin)



