from django.contrib import admin
from cars.models import Car, Brands

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brands, BrandsAdmin)