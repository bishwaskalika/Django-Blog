from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.posts_create, name='index'),
    url(r'^(?P<id>\d+)/$', views.posts_detail),
    url(r'^list/$', views.posts_list, name='index'),
    url(r'^update/$', views.posts_update, name='index'),
    url(r'^delete/$', views.posts_delete, name='index'),

]
