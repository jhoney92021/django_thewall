from django.conf.urls import url
from . import views


#main app url is login, so don't forget to preface pages urls with pages on html routing
                    
urlpatterns = [
    url(r'^$', views.index),
]