from django.urls import path
from cars.views import  CarsList, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView, api_inventory_view, api_inventory_detail


app_name = 'cars'

urlpatterns = [
    path('cars/', CarsList.as_view(), name='cars_view'),
    path('cars/add/', NewCarCreateView.as_view(), name='add_car_view'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail_view'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='update_car_view'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='delete_car_view'),

    path('api/inventory/', api_inventory_view, name='api_inventory_view'),
    path('api/inventory/<int:pk>', api_inventory_detail, name='api_inventory_detail'),
]