from django.urls import path

from . import views
from .views import UserRegistrationView

urlpatterns = [
  path('user_login/', views.user_login, name='user-login'),
  path('register/', UserRegistrationView.as_view(), name='user-register'),

]
