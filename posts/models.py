from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')