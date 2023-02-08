from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class Pricing(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)
    icon = models.ImageField(upload_to='pricing')
    support = RichTextField()

    def __str__(self):
        return self.title


class BgPricing(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pricing/bg')

    def __str__(self):
        return self.title
