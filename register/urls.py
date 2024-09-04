from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='user_register'),
    path('login/', views.login, name='new'), 
      # Home page route

]
