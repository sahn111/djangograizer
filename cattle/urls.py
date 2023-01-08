from django.urls import path

from . import views

app_name = "cattle"
urlpatterns = [
    path("", views.index, name="index")
]