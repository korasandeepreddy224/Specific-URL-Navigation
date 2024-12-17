from django.urls import path
from py.views import *

app_name='cat'
urlpatterns = [
    path('cat/',cat,name='cat')
]