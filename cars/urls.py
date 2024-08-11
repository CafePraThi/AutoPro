from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('cars/', views.cars_view, name='cars_view'),
    path('cars/add/', views.add_car_view, name='add_car_view'),
]