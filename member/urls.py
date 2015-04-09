from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

	# Utils URL
	url(r'^logout/', 'member.views.logout_manager', name='logout'),
    url(r'^register/', 'member.views.register', name='register'),

	# Home URL
    url(r'^(?P<user_pk>\d+)$', 'member.views.show_member', name='show_member'),

    # Gears' URL
    url(r'^add/gear','member.views.add_gear', name='add_gear_to_pilot'),
    url(r'^add/organization','member.views.add_organization', name='add_organization_to_pilot')
)