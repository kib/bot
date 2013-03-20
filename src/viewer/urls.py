from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # Index view (templated)
    url(r'^$', 'viewer.views.index', name='index'),
    # Images view (templated)
    url(r'^images(/(?P<nsfw>))?$', 'viewer.views.images', name='images'),
    # Youtube view (templated)
    url(r'^youtube(/(?P<nsfw>))?$', 'viewer.views.youtube', name='youtube'),
    # single image view
    url(r'^image/(?P<pk>)', 'viewer.views.image', name='image'),
)

