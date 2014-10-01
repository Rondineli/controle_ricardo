from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import settings


admin.autodiscover()

from .views import (
    LicensingCreateView,
    LicensingUpdateView,
    LicensingDeleteView,
    LicensingHomeView
)

urlpatterns = patterns('',
    url(r'^$',
        LicensingHomeView.as_view(),
        name='home'),
    url(r'^create/$',
        LicensingCreateView.as_view(),
        name='create'
    ),
    url(r'^update/(?P<pk>\d+)/$',
        LicensingUpdateView.as_view(),
        name='update'
    ),
    url(r'^delete/(?P<pk>\d+)/$',
        LicensingDeleteView.as_view(),
        name='delete'
    ),
    # url(r'^controle_financeiro/', include('controle_financeiro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout', {
            'template_name': 'registration/logout.html'
        }
    ),

    url(r'^', include('django.contrib.auth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
