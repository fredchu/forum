from django.conf.urls import patterns, include, url
from posts import views
from comments import views as comments_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

print comments_views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<post_id>\d+)/$', views.show, name='show' ),
    # url(r'^new$', views.create_page, name='create_page'),
    # url(r'^$', views.create, name='create'),
    # url(r'^(?P<post_id>\d+)/edit$', views.edit, name='edit'),
    # url(r'^(?P<post_id>\d+)$', views.update, name='update'),
    # url(r'^(?P<post_id>\d+)$', views.destroy, name='destroy'),

    url(r'^$', views.index, name='index'),
    url(r'^pages/(?P<page>\d+)$', views.index_pages, name='index_page'),
    url(r'^(?P<post_id>\d+)/$', views.show, name='show' ),
    url(r'^new$', views.create_page, name='create_page'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<post_id>\d+)/edit$', views.edit, name='edit'),
    url(r'^(?P<post_id>\d+)/update$', views.update, name='update'),
    url(r'^(?P<post_id>\d+)/destroy$', views.destroy, name='destroy'),

    url(r'^(?P<post_id>\d+)/comments/create$', comments_views.create, name='comments_create' ),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/destroy$', comments_views.destroy, name='comments_destroy' ),
)
