from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'entries.views.home', name='entries_home'),
    
    url(r'^(?P<onderdeel>\w+)/$', 'entries.views.form', name='form'),
    url(r'^(?P<onderdeel>\w+)/(?P<id>\d{1,9})/$', 'entries.views.form', name='form'),

    #url(r'^deeltaak/$', 'entries.views.deeltaak', name='deeltaak'),
    #url(r'^deeltaak/(?P<id>\d{1,9})/$', 'entries.views.deeltaak', name='deeltaak'),
)

