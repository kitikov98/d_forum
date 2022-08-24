from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', RedirectView.as_view(url='/accounts/signup/', permanent=True)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('settings/', views.UserUpdateView.as_view(), name='my_account'),


]
