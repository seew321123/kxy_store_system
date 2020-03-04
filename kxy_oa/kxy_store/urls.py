from django.urls import path
from django.conf.urls import url
from . import views

app_name='kxy_store'
urlpatterns = [
    path('', views.index, name='index'),
    path('stores/', views.stores, name='stores'),
    url(r'^stores/(?P<store_id>\d+)/$',views.store,name='store'),
    url(r'^search/(?P<store_id>\d+)/$', views.search, name='search'),
    url(r'^edit/(?P<product_id>\d+)/$', views.edit, name='edit'),
    url(r'^add/(?P<store_id>\d+)/$', views.add, name='add'),
    url(r'^delete/(?P<product_id>\d+)/$', views.delete, name='delete'),
]