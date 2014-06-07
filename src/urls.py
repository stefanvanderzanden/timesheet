from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^login/', 'entries.views.login_view', name='login'),
    url(r'^logout/', 'entries.views.logout_view', name='logout'),

    url(r'^', include('entries.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
