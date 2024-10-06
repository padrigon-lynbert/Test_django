from django.urls import path
# from django.contrib import admin

from . import views

# urlpatterns = [
#     path("admin/", views.index, name="index"),
#     path("home/", include("main.urls"))
# ]

urlpatterns = [
    path("<str:name>", views.index, name="index"),
]
