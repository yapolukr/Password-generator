from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
    path('about', views.about, name='about'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('current', views.currenttodos, name='currentpasswords'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),
]