from django.urls import path
from .views import *

urlpatterns = [
    path('content_home/', content_home, name="content_home"),
]