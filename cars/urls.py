from django.urls import path
from cars.views import  CarsList, NewCarCreateView, CarDetailView

app_name = 'cars'

urlpatterns = [
    path('cars/', CarsList.as_view(), name='cars_view'),
    path('cars/add/', NewCarCreateView.as_view(), name='add_car_view'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail_view'),
]