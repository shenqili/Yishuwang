"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django import forms
#from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    email = forms.EmailField(label='e-mail',widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'e-mail'}))
    password1 = forms.CharField(label='Password',
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    password2= forms.CharField(label='confirm',
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

def register(request):
    if request.method=='POST':
        errors=[]
        registerForm=RegisterForm(request.POST)

        if not registerForm.is_valid():
            return render(request, "myauth/register.html",{'form':registerForm,'errors':errors})
        username = registerForm.cleaned_data['username']
        email = registerForm.cleaned_data['email']
        password1 = registerForm.cleaned_data['password1']
        password2= registerForm.cleaned_data['password2']
        if password1!=password2:
            errors.append("两次输入的密码不一致!")
            return render(request, "myauth/register.html",{'form':registerForm,'errors':errors})
        #filterResult=User.objects.filter(username=username)
        #if len(filterResult)>0:
        #    errors.append("用户名已存在")
        #    return render(request, "myauth/register.html",{'form':registerForm,'errors':errors})
        user = User.objects.create_user(username,email,password1)
        user.save()
        #登录前需要先验证
        newUser=auth.authenticate(username=username,password=password1)
        if newUser is not None:
            auth.login(request, newUser)
            return HttpResponseRedirect("/")
    else:
        registerForm=RegisterForm();
        return render(request, "myauth/register.html",{'form':registerForm,})

    return render(request, "myauth/register.html")


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'myauth/index.html',
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
        'myauth/contact.html',
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
        'myauth/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
