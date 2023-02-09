from django.db import models
from datetime import date
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/blog')
    date = models.DateField(default=date.today)
    view = models.CharField(max_length=200)
    desc = RichTextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def comment(self):
        pass


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_fk")
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/comment')
    date = models.DateField(default=date.today)
    comment = RichTextField()

    def __str__(self):
        return self.name


class BgBlog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/bg')

    def __str__(self):
        return self.title
