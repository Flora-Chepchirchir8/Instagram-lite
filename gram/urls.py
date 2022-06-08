from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path (r'^$',views.display_home,name='home'),
    re_path(r'like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    re_path(r'profile/(\d+)', views.profile, name='profile'),
    re_path(r'new/profile', views.add_profile, name='add_profile'),
    re_path(r'search/', views.search, name='search_results'),
    re_path(r'comment/(?P<pk>\d+)',views.user_comments,name='comment'),
    re_path(r'follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),
#  re_path (r'^posts/',views.new_post, name='post'),
#  re_path (r'comment/<int:id>', views.add_comment, name='comment'),
#  re_path (r'search/',views.search, name='search'),
#  re_path (r'profile/',views.show_profile, name='profile'),
#  re_path ('update/<int:id>',views.update_profile,name='update_profile'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)