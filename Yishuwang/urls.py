"""
Definition of urls for Yishuwang.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import myauth.forms
import myauth.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', myauth.views.home, name='home'),
    url(r'^contact$', myauth.views.contact, name='contact'),
    url(r'^about', myauth.views.about, name='about'),
    url(r'^register', myauth.views.register, name='register'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'myauth/login.html',
            'authentication_form': myauth.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
