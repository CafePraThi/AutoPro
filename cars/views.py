from django.http import HttpResponse
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForms
from django.views import View
from django.views.generic import ListView, CreateView


class CarsList(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
    

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForms
    template_name = 'add_car.html'
    success_url = '/cars/'