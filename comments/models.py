from django.db import models
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.CharField(max_length=140)