from django.conf.urls import url
from MainApp import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^signup/$',views.sign_up_view,name='sign-up'),
    url(r'^single/$',views.single_post,name='single-post'),
    url(r'^user/$',views.single_user,name='single-user'),
    url(r'^all/$',views.all_pastes,name='view-all'),
    #forms
    url(r'^loginform/$',views.login_form,name='login-form-handler'),
    url(r'^signupform/$',views.signup_form,name='signup-form-handler'),
    url(r'^formhandle/$',views.all_pastes,name='view-all'),

]
