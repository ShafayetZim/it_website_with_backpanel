from .models import *
from django import forms


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = (
            'mail',)

        widgets = {
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = (
            'number',)

        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = (
            'address',)

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'title', 'info')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ContactBgForm(forms.ModelForm):
    class Meta:
        model = ContactBg
        fields = (
            'title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }