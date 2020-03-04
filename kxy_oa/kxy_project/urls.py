from django.urls import path
from django.conf.urls import url
from . import views

app_name='kxy_project'
urlpatterns = [
    path('', views.project, name='project'),
    path('my_project/', views.my_project, name='my_project'),
    path('new_project/', views.new_project, name='new_project'),
    path('new_project/', views.new_project, name='new_project'),
    url(r'^project_detail/(?P<project_id>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^delete_project/(?P<project_id>\d+)/$', views.delete_project, name='delete_project'),
]