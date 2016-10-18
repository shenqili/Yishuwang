"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django import forms  
from django.contrib.auth.models import User
from django.contrib import auth

class RegisterForm(forms.Form):
    username = forms.CharField(label='username')
    email = forms.EmailField(label='e-mail')
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm',widget=forms.PasswordInput)

def register(request):        
    if request.method=='POST':   
        errors=[]   
        registerForm=RegisterForm(request.POST) 

        if not registerForm.is_valid():  
            return render(request, "app/register.html",{'form':registerForm,'errors':errors})
        username = registerForm.cleaned_data['username']  
        email = registerForm.cleaned_data['email']  
        password1 = registerForm.cleaned_data['password1']  
        password2= registerForm.cleaned_data['password2']
        if password1!=password2:  
            errors.append("两次输入的密码不一致!")  
            return render(request, "app/register.html",{'form':registerForm,'errors':errors})           
        filterResult=User.objects.filter(username=username) 
        if len(filterResult)>0:  
            errors.append("用户名已存在")  
            return render(request, "app/register.html",{'form':registerForm,'errors':errors})   
              
        user = User.objects.create_user(username, email, password1)
        user.isActive=True
        user.isStaff=False
        user.save()   
        #登录前需要先验证  
        newUser=auth.authenticate(username=username,password=password1) 
        if newUser is not None:
            auth.login(request, newUser)
            return HttpResponseRedirect("/")  
    else:
        registerForm=RegisterForm();
        return render(request, "app/register.html",{'form':registerForm,})
      
    return render(request, "app/register.html") 
    
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
