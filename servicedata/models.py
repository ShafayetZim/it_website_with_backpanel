from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class Service(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=300)
    icon = models.ImageField(upload_to='service/service')
    desc = RichTextField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='service/bg')

    def __str__(self):
        return self.title


class Progress(models.Model):
    title = models.CharField(max_length=200)
    percentage = models.FloatField(max_length=10)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service/review')
    review = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class BgService(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service/bg')

    def __str__(self):
        return self.title
