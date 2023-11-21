from django.urls import path 
from django.urls import path
from m3  import views
from django.views.generic import TemplateView
from m3 import views,models
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from m3 import forms
app_name='m3'
urlpatterns =  [ 
   path("",TemplateView.as_view(template_name="pages/home.html"),name="home",),
]