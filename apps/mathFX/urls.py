from django.urls import path
from . import views

app_name = "MathFX"

urlpatterns = [
    path("", views.index, name="try"),
    path('integral/<str:const>/<str:func>/<str:n1>/<str:n2>',
         views.calculate_integral, name="Integral"),
    path('integral/<str:const>/<str:func>/',
         views.calculate_undefined_integral, name="UndefinedIntegral"),
    path('derivative/<str:const>/<str:func>/', views.calculate_derivative, name="takeDerivativeOpt"),
    path('derivative/<str:const>/<str:func>/<int:sequence>', views.calculate_derivative,
         name="takeDerivative"),

]
