# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
import datetime
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Post

def index(request):
    return index_pages(request, 1)

def index_pages(request, page):
    postsPaginator = Paginator(Post.objects.all(), 4, orphans=2)

    try:
        posts = postsPaginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        posts = postsPaginator.page(1)

    return render(request, 'posts/index.html', {
        'posts': posts
    })

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = enumerate( post.comment_set.all())

    return render(request, 'posts/show.html', {
        'post': post,
        'comments': comments
    })

def create_page(request):
    return render(request, 'posts/new.html', {})

def create(request):
    title = request.POST['title'].strip()
    content = request.POST['content'].strip()

    post = Post(
        title=title,
        content=content
    )

    try:
        post.full_clean()
    except ValidationError as err:
        return render(request, 'posts/new.html', {
            'ori': {
                'title': title,
                'content': content
            },
            'err': err.message_dict
        })

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
    elif len( request.POST[ 'title' ]) == 0:
        post.title = ''

    if request.POST[ 'content' ]:
        post.content = request.POST[ 'content' ]
    elif len( request.POST[ 'content' ]) == 0:
        post.content = ''

    try:
        post.full_clean()
    except ValidationError as err:
        return render(request, 'posts/edit.html', {
            'ori': {
                'title': post.title,
                'content': post.content
            },
            'post': post,
            'err': err.message_dict
        })

    post.save()

    return HttpResponseRedirect('/posts/' + post_id)

def destroy(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    return HttpResponseRedirect('/posts/')