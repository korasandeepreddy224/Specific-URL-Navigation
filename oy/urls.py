from django.urls import path
from oy.views import *


app_name='dog'
urlpatterns = [
    path('dog/',dog,name='dog')
]