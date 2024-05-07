from django.urls import path

from . import views

app_name = "MathFX"

urlpatterns = [
    path("", views.index, name="try"),

]