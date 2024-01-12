from django.urls import path

from . import views
from .views import UserRegistrationView, PasswordsChangeView, password_change_done
# from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('user_login/', views.user_login, name='user-login'),
  path('register/', UserRegistrationView.as_view(), name='user-register'),
  path('edit_profile/', views.edit_profile, name='edit-profile'),
  path('password/', PasswordsChangeView.as_view(
    template_name='accounts/registration/change_password.html'), name='change-password'),
  path('password_change_done/', views.password_change_done, name='password-change-done' ),


  path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
