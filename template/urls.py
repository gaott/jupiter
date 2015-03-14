from django.conf.urls import patterns, include
from django.contrib import admin
from django.contrib.auth import login, logout

from template import settings
from template.TestView import testTable


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', login, {'template_name':'login.html'}),
    (r'^accounts/logout/$', logout, {'next_page': "/accounts/login/"}),
    
    ('^$', testTable),
    ('^/$', testTable),
    
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "css/"}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "js/"}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + "img/"}),
)
