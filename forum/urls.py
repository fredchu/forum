from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^forum/', include('forum.foo.urls')),

    url(r'^$', 'posts.views.index', name='home'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    # url(r'^comments/', include('comments.urls'), namespace = 'comments'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
