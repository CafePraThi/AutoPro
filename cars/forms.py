from django import forms
from cars.models import Brands, Car

class CarForms(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brands.objects.all())
    factor_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        new_car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factor_year = self.cleaned_data['factor_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo']
        )
        new_car.save()
        return new_car