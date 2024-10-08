from cars.models import Car, CarInventory
from cars.forms import CarForms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


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
    

@method_decorator(login_required, name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForms
    template_name = 'add_car.html'
    success_url = '/cars/'


@method_decorator(login_required, name='dispatch')
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required, name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForms
    template_name = 'update_car.html'

    def get_success_url(self):
        return reverse_lazy('cars:car_detail_view', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars/'


def api_inventory_view(request):
    inventorys = CarInventory.objects.all()
    data = [{'id': inventory.id, 'cars_count': inventory.cars_count, 'cars_value': inventory.cars_value, 'created_at': inventory.created_at } for inventory in inventorys]
    return JsonResponse(data, safe=False)


@csrf_exempt
def api_inventory_detail(request, pk):
    inventory = get_object_or_404(CarInventory, pk=pk)
    data = {'id': inventory.id, 'cars_count': inventory.cars_count, 'cars_value': inventory.cars_value, 'created_at': inventory.created_at }
    return JsonResponse(data, safe=False)