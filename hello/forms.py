from django import forms
from .models import Greeting, StoreData


class GreetingForm(forms.ModelForm):
    class Meta:
        model = Greeting
        fields = ['fullname', 'industry', 'SKUNum', 'BarcodeNum', 'Month']
        required_css_class = 'bold'


class StoreDataForm(forms.ModelForm):
    class Meta:
        model = StoreData
        fields = ['month']
