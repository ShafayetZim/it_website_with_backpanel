from .models import *
from django import forms


class PricingCreateForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = (
            'title', 'price', 'discount', 'icon', 'support')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
            'support': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BgPricingCreateForm(forms.ModelForm):
    class Meta:
        model = BgPricing
        fields = (
            'title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }