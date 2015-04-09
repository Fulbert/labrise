from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
#from django.contrib import admin
from django.contrib.gis import admin

from . import settings

urlpatterns = patterns('',

	# Home URL
    url(r'^$', 'page.views.home', name='home'),

    url(r'^member/', include('member.urls')),
    url(r'^gear/', include('gear.urls')),
    url(r'^flight/', include('flightlog.urls')),
    url(r'^map/', include('space.urls')),

    # Account management URL
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Admin's URL
    url(r'^admin/', include(admin.site.urls)),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )