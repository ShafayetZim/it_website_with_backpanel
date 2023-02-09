from django.db import models
from datetime import date
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class BgPortfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/bg')

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/portfolio')

    def __str__(self):
        return self.title


class PortfolioDetails(models.Model):
    code = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="portfolio_fk")
    title = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='portfolio/details')
    image2 = models.ImageField(upload_to='portfolio/details')
    date = models.DateField(default=date.today)
    category = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    desc = RichTextField()

    def __str__(self):
        return self.title
