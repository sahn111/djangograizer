from django.urls import path

from . import views

app_name = "cattle"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cattle>", views.get_cattle, name="cattle"),
    path("weight/", views.get_weight, name="weight"),
    path("save/", views.create_item, name="save"),
    path("stable/", views.get_stable, name="stable"),

]