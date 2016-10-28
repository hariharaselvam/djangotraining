from django.conf.urls import url
from .views import *
urlpatterns = [
   
   
    url(r'^list/', twitter_view, name="twitter_view"),
    url(r'^timeline/', timeline_view, name="timeline_view"),
  
]