from .models import *
from django import forms


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = (
            'title', 'info', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list border'}),
        }


class PortfolioDetailsForm(forms.ModelForm):
    class Meta:
        model = PortfolioDetails
        fields = (
            'code', 'title', 'image1', 'image2', 'date', 'category', 'client', 'website', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_code'}),
            'image1': forms.FileInput(attrs={'class': 'rounded_list border'}),
            'image2': forms.FileInput(attrs={'class': 'rounded_list border'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BgPortfolioForm(forms.ModelForm):
    class Meta:
        model = BgPortfolio
        fields = (
            'title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }
