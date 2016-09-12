from django.conf.urls import url

from mailinglist import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<list_id>\d+)/$', views.mlist, name='mlist'),
    url(r'^(?P<list_id>\d+)/subscribe/$', views.subscribe, name='subscribe'),
]

