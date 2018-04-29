# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import views
from django.conf.urls import include, url


urls = [

    url(r'^$', views.GameListView.as_view(), name='category_list'),

    url(r'^(?P<slug>[\w-]+)/$', views.GameListView.as_view(),
        name='category_detail'),

    url(r'^(?P<slug>[\w-]+)/$', views.GameListView.as_view(),
        name='game_list'),

    url(r'^game/(?P<slug>[\w-]+)/$', views.GameDetailView.as_view(),
        name='game_detail'),

]


urlpatterns = [url(r'^', include(urls, namespace='library'))]
