from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class Slider(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/slider')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='home/service')
    desc = RichTextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/project')

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/about')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    desc = RichTextField()

    def __str__(self):
        return self.title


class Speciality(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='home/speciality')

    def __str__(self):
        return self.title
