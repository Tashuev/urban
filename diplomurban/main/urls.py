from django.urls import path
from . import views
urlpatterns = [
    path('glav', views.index),
    path('about', views.about),
]