from django.urls import path

from.views import json_object
urlpatterns = [
    path("", json_object, name="home"),
]