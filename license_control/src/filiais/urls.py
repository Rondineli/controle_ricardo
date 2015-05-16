from django.conf.urls import patterns, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

from .views import (
    BranchCreateView,
    BranchUpdateView,
    BranchDeleteView,
    BranchListView
)

urlpatterns = patterns('',
    url(r'^$',
        BranchListView.as_view(),
        name='list'
    ),
    url(r'^create/$',
        BranchCreateView.as_view(),
        name='create'
    ),
    url(r'^update/(?P<pk>\d+)/$',
        BranchUpdateView.as_view(),
        name='update'
    ),
    url(r'^delete/(?P<pk>\d+)/$',
        BranchDeleteView.as_view(),
        name='delete'
    ),
    # url(r'^controle_financeiro/', include('controle_financeiro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)