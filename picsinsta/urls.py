"""picsinsta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path
from gram import views


urlpatterns = [
  re_path('admin/', admin.site.urls),
  # re_path('',include('insta.urls')),
  re_path('',include('gram.urls')),
  re_path('register/',views.register_user,name='register'),
  re_path('accounts/login/',views.login_user,name='login'),
  re_path('logout/', views.logout_user, name='logout'),
  re_path('tinymce/', include('tinymce.urls')),
  # re_path(r'accounts/', include('registration.backends.simple.urls')),
  #   #url(r'logout/', views.LogoutView.as_view(), {"next_page": 'accounts/login'})
  # re_path(r'logout/', views.logout_then_login),
]
