from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'space.views.home', name="map_home"),
)
