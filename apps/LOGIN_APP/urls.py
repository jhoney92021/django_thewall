from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^process/registration$', views.processRegistration), 
    url(r'^process/login$', views.processLogin), 
    url(r'^process$', views.process), 
    url(r'^success/$', views.success), 
    url(r'^logout/$', views.logout), 
    url(r'^$', views.index),
]