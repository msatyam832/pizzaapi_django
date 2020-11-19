
from django.conf.urls import url
from .import views

urlpatterns = [ 
    url(r'^api/Pizza$', views.pizza_list),
    url(r'^api/Pizza/(?P<pk>[0-9]+)$', views.pizza_detail),
]