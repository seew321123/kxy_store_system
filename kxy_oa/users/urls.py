from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
app_name='users'
urlpatterns = [
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
]