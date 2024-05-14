from django.urls import path
from . import views

app_name = "MathFX"

urlpatterns = [
    path("", views.index, name="try"),
    path('integral/<str:const>/<str:func>/<str:n1>/<str:n2>',
         views.calculate_integral,
         name="Integral")
]