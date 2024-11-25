from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('glavnaya', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
    path('authorization', views.authorization)
]