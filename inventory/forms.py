from django import forms
from .models import *

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ('description', 'expiry', 'status', 'misc', 'donator')


class FoodForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = ('description', 'expiry', 'status', 'misc', 'donator')


class MiscObjectForm(forms.ModelForm):
    class Meta:
        model = MiscObjects
        fields = ('description', 'expiry', 'status', 'misc', 'donator')
