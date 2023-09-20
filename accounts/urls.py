from django.urls import path

from . import views
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, password_change_done
# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('user_login/', views.user_login, name='user-login'),
  path('register/', UserRegistrationView.as_view(), name='user-register'),
  path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
  path('password/', PasswordsChangeView.as_view(
    template_name='accounts/registration/change_password.html'), name='change-password'),
  path('password_change_done/', views.password_change_done, name='password-change-done' ),

]
