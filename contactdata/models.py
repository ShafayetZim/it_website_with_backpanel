from django.db import models
from datetime import date
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class ContactBg(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='contact/bg')

    def __str__(self):
        return self.title


class Phone(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class Email(models.Model):
    mail = models.EmailField()

    def __str__(self):
        return self.mail


class Office(models.Model):
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.address


class Contact(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=300)

    def __str__(self):
        return self.title
