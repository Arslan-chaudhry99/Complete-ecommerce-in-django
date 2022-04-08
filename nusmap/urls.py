from django.urls import path
from nusmap import views

urlpatterns = [
   
   path('', views.home, name="home"),
   path('collections', views.collections, name="collections"),
   path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
  
]