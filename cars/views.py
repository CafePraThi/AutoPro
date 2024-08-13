from django.http import HttpResponse
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForms
from django.views import View


class CarView(View):
    def get(self, request):
        cars = Car.objects.all()
        search = request.GET.get('search', None)

        if search:
            cars = Car.objects.filter(model_icontains=search).order_by('-id')
            
        return render(request, 'cars.html', {'cars': cars})


def add_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForms(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars:cars_view')

    else:
        new_car_form = CarForms()

    return render(request, 'add_car.html', {'new_car_form': new_car_form})