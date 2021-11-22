from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('notices/', views.notices, name='notices'),
    path('map/', views.map, name='map'),
    path('calendar/', views.calendar, name='calendar'),
    path('gallery/', views.gallery, name='gallery'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    
]