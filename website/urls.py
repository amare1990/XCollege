from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('admission/', views.admission, name='admission'),
  path('academics/cs_bsc/', views.csBSc, name='cs-bsc'),
  path('academics/se_bsc/', views.seBSc, name='se-bsc'),
  path('academics/cs_msc/', views.csMSc, name='cs-msc'),
  path('academics/se_msc/', views.seMSc, name='se-msc'),
  path('academics/courses/', views.courses, name='courses-list'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact-us'),
]
