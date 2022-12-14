"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='/boards/', permanent=True)),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='boards/password_reset.html',
        email_template_name='boards/password_reset_email.html',
        subject_template_name='boards/password_reset_subject.txt'
    ),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='boards/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='boards/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='boards/password_reset_complete.html'),
         name='password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='boards/password_change.html'),
         name='password_change'),
    path('settings/password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='boards/password_change_done.html'),
         name='password_change_done'),


]
