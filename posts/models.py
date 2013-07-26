from django.db import models
from django import forms

class Post(models.Model):
    # title = models.CharField(max_length=3, validators=[validators.MaxLengthValidator(3)])
    title = models.CharField(max_length=3)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')