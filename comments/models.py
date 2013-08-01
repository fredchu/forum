from django.db import models
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.CharField(max_length=10, error_messages={
        'blank': 'comment is required'
    })

    content.validators[-1].message = 'Your comment must be less than 10 characters.'