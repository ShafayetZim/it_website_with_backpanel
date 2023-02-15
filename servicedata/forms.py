from .models import *
from django import forms


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


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = (
            'title', 'icon')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = (
            'title', 'percentage')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'percentage': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = (
            'title', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'name', 'position', 'image', 'review')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
            'review': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BgServiceForm(forms.ModelForm):
    class Meta:
        model = BgService
        fields = (
            'title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }
