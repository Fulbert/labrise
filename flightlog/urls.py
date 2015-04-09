from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'flightlog.views.home', name="flightlog_home"),
    url(r'^new/trip','flightlog.views.add_trip', name="add_trip"),
    url(r'^new/track','flightlog.views.add_track', name="add_track"),

)
