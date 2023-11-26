from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),
    path('add_profile/', views.add_profile, name='add-profile'),
    path('staff_list/', views.staff_list, name='staff-list'),
    path('student_list/', views.student_list, name='student-list'),
    path('course_list/', views.course_list, name='course-list'),
    path('add_teacher/', views.add_teacher, name='add-teacher'),
    path('add_student/', views.add_student, name='add-student'),
    path('add_course/', views.add_course, name='add-course'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
