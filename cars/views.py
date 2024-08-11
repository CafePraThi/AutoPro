from django.http import HttpResponse
from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search', None)

    if search:
        cars = Car.objects.filter(model_icontains=search).order_by('-id')
        
    
    print(cars)

    return render(request, 'cars.html', {'cars': cars})