from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'entries.views.home', name='entries_home'),
    
    url(r'^project/$', 'entries.views.project', name='project'),
    url(r'^project/(?P<id>\d{1,9})/$', 'entries.views.project', name='project'),

)

