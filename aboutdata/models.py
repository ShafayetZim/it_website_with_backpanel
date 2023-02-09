from django.db import models
from datetime import date
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class BgAbout(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about/bg')

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Feature(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Progressbar(models.Model):
    name = models.CharField(max_length=200)
    percentage = models.FloatField(max_length=10)

    def __str__(self):
        return self.name


class ExperienceBg(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='about/experience')

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.FloatField(max_length=10)
    icon = models.ImageField(upload_to='about/experience')

    def __str__(self):
        return self.title


class Process(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='about/process')

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about/team')

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='about/partner')
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name
