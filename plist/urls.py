from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokemon/(?P<pk>[0-9]+)/$', views.pokemon_detail, name='pokemon_detail'),
    url(r'^$', views.pokemon_list, name='post_list'),
    url(r'^pokemon/new/$', views.pokemon_new, name='pokemon_new'),
    url(r'^pokemon/(?P<pk>[0-9]+)/edit/$', views.pokemon_edit, name='pokemon_edit'),
]
