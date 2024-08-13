from django.urls import path
from cars.views import CarView
from cars import views

app_name = 'cars'

urlpatterns = [
    path('cars/', CarView.as_view(), name='cars_view'),
    path('cars/add/', views.add_car_view, name='add_car_view'),
]