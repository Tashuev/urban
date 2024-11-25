from django.urls import path
from . import views
urlpatterns = [
   path('news_home', views.news_home)
]