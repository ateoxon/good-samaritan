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

class ReserveDrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ('status', 'receiver')
        #fields = ('status',)


class ReserveFoodForm(forms.ModelForm):
    class Meta:
        model = Foods
        #fields = ('status',)
        fields = ('status', 'receiver')


class ReserveMiscObjectForm(forms.ModelForm):
    class Meta:
        model = MiscObjects
        #fields = ('status',)
        fields = ('status', 'receiver')
