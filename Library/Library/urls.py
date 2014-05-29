from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('apps.books.urls')),
    
    url(r'^login/', 'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),

 	


)
