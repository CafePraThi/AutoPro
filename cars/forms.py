from django import forms
from cars.models import Car
    
class CarForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        def clean_value(self):
            value = self.cleaned_data.get('value')
            if value < 15000:
                self.add_error('value', f'The value of the car must be greater than {value}')
            return value
        
        def clean_factory_year(self):
            factory_year = self.cleaned_data.get('factory_year')
            if len(str(factory_year)) != 4:
                self.add_error('factory_year', 'The factory year must have 4 digits')
            if factory_year < 1900:
                self.add_error('factory_year', f'The factory year must be greater than {factory_year}')
            return factory_year
        
        def clean_model_year(self):
            model_year = self.cleaned_data.get('model_year')
            if len(str(model_year)) != 4:
                self.add_error('model_year', 'The model year must have 4 digits')
            return model_year
        