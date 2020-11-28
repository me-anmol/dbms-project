from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.loginP, name='login'),
    path('desti/<oid>/', views.desti, name='desti'),
    path('register/', views.register, name='register'),
    path('signup/',views.sign, name = 'signup'),
    path('logout', views.logoutp, name ='logout' )
]
