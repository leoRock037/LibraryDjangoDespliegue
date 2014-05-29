from django.conf.urls import *
from apps.sales import views

urlpatterns = patterns('',
    url(r'^charge/$', views.charge, name="charge"),
)