from .models import *
from django import forms


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'title', 'info')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = (
            'name', 'info')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProgressbarForm(forms.ModelForm):
    class Meta:
        model = Progressbar
        fields = (
            'name', 'percentage')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'percentage': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = (
            'name', 'website', 'logo')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'name', 'position', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = (
            'title', 'quantity', 'icon')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = (
            'title', 'quantity', 'icon')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class ExperienceBgForm(forms.ModelForm):
    class Meta:
        model = ExperienceBg
        fields = (
            'title', 'icon')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class BgAboutForm(forms.ModelForm):
    class Meta:
        model = BgAbout
        fields = (
            'title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }
