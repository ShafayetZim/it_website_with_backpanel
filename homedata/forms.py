from .models import *
from django import forms


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'title', 'image', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'title', 'info', 'icon', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title', 'image', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = (
            'title', 'image', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = (
            'title', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = (
            'title', 'icon')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
        }
