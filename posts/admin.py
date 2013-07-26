from django.contrib import admin
from posts.models import Post
from comments.models import Comment

class CommentAdmin( admin.ModelAdmin ):
    pass

class PostAdmin( admin.ModelAdmin ):
    pass

admin.site.register( Post, PostAdmin )
admin.site.register( Comment, CommentAdmin )