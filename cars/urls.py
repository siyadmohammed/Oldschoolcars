from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('userreg/', views.userreg),
    path('userlogin/', views.userlogin),
    ]