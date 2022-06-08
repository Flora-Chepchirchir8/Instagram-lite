from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
 re_path (r'^$',views.display_home,name='home'),
 re_path (r'^posts/',views.new_post, name='post'),
 re_path (r'comment/<int:id>', views.add_comment, name='comment'),
 re_path (r'search/',views.search, name='search'),
 re_path (r'profile/',views.show_profile, name='profile'),
 re_path ('update/<int:id>',views.update_profile,name='update_profile'),
 re_path (r'signup/', views.signup, name='signup'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)