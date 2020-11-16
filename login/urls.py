from django.contrib import auth
from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_home, name='home'),
    path('web/', views.my_web, name='web'),
    path('save_data/', views.save_data, name='save_data'),
]