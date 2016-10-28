from django.conf.urls import url
from .views import hello_world, HelloWorld, list_products
urlpatterns = [
   
    url(r'^hello_world/', HelloWorld.as_view(), name="hello_world"),
    url(r'^list/', list_products, name="list_products"),
  
]