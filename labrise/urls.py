from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import settings

urlpatterns = patterns('',
    url(r'^$', 'page.views.home', name='home'),
    url(r'^login/', 'util.views.login', name='login'),

    url(r'^flight/', include('flightlog.urls')),

    # Admin's URL
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)