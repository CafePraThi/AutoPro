from django.urls import path
from cars.views import  CarsList, NewCarCreateView

app_name = 'cars'

urlpatterns = [
    path('cars/', CarsList.as_view(), name='cars_view'),
    path('cars/add/', NewCarCreateView.as_view(), name='add_car_view'),
]