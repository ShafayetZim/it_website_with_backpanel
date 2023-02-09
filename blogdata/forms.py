from .models import *
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title', 'info', 'image', 'date', 'view', 'desc', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'view': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'blog', 'name', 'image', 'date', 'comment')

        widgets = {
            'blog': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_blog'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BgBlogForm(forms.ModelForm):
    class Meta:
        model = BgBlog
        fields = (
            'title', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }
