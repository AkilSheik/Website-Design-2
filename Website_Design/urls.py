"""Defines URL patterns for Website_Design"""
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    #home page
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^index',views.index,name='index'),
    url(r'^-link',views.index,name='index'),
    url(r'^500',views.500,name='500')
]
urlpatterns += staticfiles_urlpatterns()
