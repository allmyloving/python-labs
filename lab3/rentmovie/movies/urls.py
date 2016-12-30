from django.conf.urls import url

from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<movie_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<movie_id>[0-9]+)/delete/$', views.delete, name='delete'),
]
