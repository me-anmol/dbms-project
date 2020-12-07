from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.loginP, name='login'),
    path('desti/<oid>/', views.desti, name='desti'),
    path('register/', views.register, name='register'),
    path('signup/',views.sign, name = 'signup'),
    path('logout/', views.logoutp, name ='logout' ),
    path('book/<oid>', views.book, name ='book' ),
    path('phone', views.changePhone, name ='phone' ),
    path('account/',views.account, name = 'account'),
    path('address/',views.changeAddress,name ='address')
]
