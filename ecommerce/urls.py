"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from products.api_views import *
from products.views import hello_world, HelloWorld, list_products

from rest_framework.routers import SimpleRouter
from django.conf import settings

router = SimpleRouter()
router.register('users',UserViewSet)
router.register('category',CategoryViewSet)
router.register('stat',StatViewSet)
router.register('product',ProductViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^products/', include('products.urls')),

    url(r'^tweets/', include('tweets.urls')),

    url(r'^categories/', 
    	CategoryViewSet.as_view(
    		{
    			'get':'list',
    			'post':'create',
    		}
    	), 
    	name='category-list'
    ),

    url(
    	r'^categories/(?P<pk>[0-9]+)/$', 
    	CategoryViewSet.as_view(
    		{
    			'patch':'partial_update',
    			'delete':'destroy',
    		}
    	), 
    	name='category-detail'
    ),

    url(r'^api/v1/', include(router.urls))
]

#urlpatterns+= router.urls

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/',include(debug_toolbar.urls)),
	]
