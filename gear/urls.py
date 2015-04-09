from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	url(r'^$','gear.views.home', name='gear_home'),
    url(r'^show/(?P<gear_pk>\d+)$', 'gear.views.show_gear', name='show_gear'),
    url(r'^show/brand/(?P<brand_pk>\d+)$', 'gear.views.show_brand', name='show_brand'),
)