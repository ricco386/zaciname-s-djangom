from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'konferencia.views.home', name='home'),
    url(r'^ml/', include('mailinglist.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
