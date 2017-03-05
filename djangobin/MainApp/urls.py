from django.conf.urls import url
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.base_view.as_view(template_name='home.html'),name='home'),
    url(r'^all/$',views.base_view.as_view(template_name='all-posts.html'),name='view-all'),
    url(r'^(?P<pk>[-\w]+)/$', views.post_detail_view.as_view(template_name='detail-view.html'), name='detail'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^signup/$',views.sign_up_view,name='sign-up'),
    url(r'^single/$',views.single_post,name='single-post'),
    url(r'^user/$',views.single_user,name='single-user'),
    #forms
    url(r'^loginform/$',views.login_form,name='login-form-handler'),
    url(r'^signupform/$',views.signup_form,name='signup-form-handler'),
    url(r'^postformhandle/$',views.post_form_upload,name='post-form'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
