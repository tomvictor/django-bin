from django.conf.urls import url,include
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #APis
    url(r'^api/', include('MainApp.api.urls', namespace='restapi')),
    #forms
    url(r'^loginform/$',views.login_form,name='login-form-handler'),
    url(r'^signupform/$',views.signup_form,name='signup-form-handler'),
    url(r'^postformhandle/$',views.post_form_upload,name='post-form'),
    url(r'^$',views.base_view.as_view(template_name='home.html'),name='home'),
    url(r'^search/$',views.base_view.as_view(template_name='all-posts.html'),name='view-all'),
    url(r'^all/$',views.base_view.as_view(template_name='infiscroll.html'),name='infiscroll'),
    # url(r'^private/$',views.privatePosts.as_view(template_name='private-posts.html'),name='view-private'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^signup/$',views.sign_up_view,name='sign-up'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail_view.as_view(template_name='detail-view.html'), name='detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
