from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
import datetime

from posts.models import Post
# from comments.models import Comment

def index(request):
    posts = Post.objects.all()

    print posts

    return render(request, 'posts/index.html', {
        'posts': posts
    })

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'posts/show.html', {
        'post': post
    })

def create_page(request):
    return render(request, 'posts/new.html', {})
    # return HttpResponse('haha create_page page')

def create(request):
    title = request.POST[ 'title' ]
    content = request.POST[ 'content' ]

    post = Post(
        title=title,
        content=content,
        pub_date=datetime.datetime.now()
    )

    post.save()

    return HttpResponseRedirect('/posts/')

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'posts/edit.html', {
        'post': post
    })

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.POST[ 'title' ]:
        post.title = request.POST[ 'title' ]

    if request.POST[ 'content' ]:
        post.content = request.POST[ 'content' ]

    post.save()

    return HttpResponseRedirect('/posts/' + post_id)

def destroy(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    return HttpResponseRedirect('/posts/')