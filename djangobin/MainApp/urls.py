from django.conf.urls import url
from MainApp import views

urlpatterns = [
    url(r'^$',views.home,name='home-page'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^single/$',views.single_post,name='single-post'),
    url(r'^user/$',views.single_user,name='single-user'),
]
