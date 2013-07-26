from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from posts.models import Post
import datetime

from comments.models import Comment


def create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    content = request.POST['content']

    comment = Comment(content=content, post=post)

    comment.save()

    return HttpResponseRedirect('/posts/' + post_id)

def destroy(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    comment.delete()

    return HttpResponseRedirect('/posts/' + post_id)