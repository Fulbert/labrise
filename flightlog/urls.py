from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'flightlog.views.home', name="home"),
    url(r'^new/trip','flightlog.views.new_trip', name="new_trip"),
    url(r'^new/track','flightlog.views.new_track', name="new_track"),

)
