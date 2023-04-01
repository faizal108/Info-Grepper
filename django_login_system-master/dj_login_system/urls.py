"""dj_login_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

from users.forms import CustomPasswordResetForm
from . import tools

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('tools/', user_views.tools, name='alltools'),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('web_scrapper/',tools.web_scrapper, name='WebScrapper'),
    path('ipgeo/',tools.ipgeo, name='IPGeo'),
    
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="users/password_reset.html",
        form_class=CustomPasswordResetForm
    ), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_sent.html"
    ), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html"
    ), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html"
    ), name="password_reset_complete"),
]
