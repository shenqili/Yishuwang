"""
Definition of urls for Yishuwang.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^search$',app.views.search,name='search'),
    url(r'^detail$',app.views.detail,name='detail'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^register$', app.views.register, name='register'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
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
    url(r'^upload_book/(?P<book_grade>\d)/(?P<book_major>.*)',app.views.upload_book),
    url(r'^upload_book_choice$',app.views.upload_book_choice),
    url(r'^user_book_detail$',app.views.user_book_detail),
    url(r'^delete_book/(?P<book_id>\d+)',app.views.delete_book),
    url(r'^personal_inf/(?P<c_user>\w+)$',app.views.personal_inf, name='personalinf'),
    url(r'^public_inf/(?P<c_user>\w+)$',app.views.public_inf, name='publicinf'),
    
    url(r'^password_change/$', django.contrib.auth.views.password_change,
        {
            'template_name': 'registration/password_change_form.html',
            'post_change_redirect': 'password_change_done'
        },
        name='password_change'),
    url(r'^password_change/done/$', django.contrib.auth.views.password_change_done,
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
    url(r'^password_reset/$', django.contrib.auth.views.password_reset,
        {
            'template_name': 'registration/password_reset_form.html',
            'email_template_name': 'registration/password_reset_email.html',
            'subject_template_name': 'registration/password_reset_subject.html',
            'post_reset_redirect': 'password_reset_done'
        },
        name='password_reset'),
    url(r'^password_reset/done/$', django.contrib.auth.views.password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django.contrib.auth.views.password_reset_confirm,
        {
            'template_name': 'registration/password_reset_confirm.html',
            'post_reset_redirect': 'password_reset_complete'
        },
        name='password_reset_confirm'),
    url(r'^reset/done/$', django.contrib.auth.views.password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^need_book$',app.views.need_book),
    url(r'^delete_need_book/(?P<book_id>\d+)',app.views.delete_need_book),
    url(r'(?P<book_id>\d+)',app.views.book_detail),

  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
