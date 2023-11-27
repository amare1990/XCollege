from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),
    path('add_department', views.add_department, name='add-department'),

    path('add_course/', views.add_course, name='add-course'),
    path('course_list/', views.course_list, name='course-list'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course-detail'),
    path('course/<int:course_id>/delete', views.course_delete, name='course-delete'),

    path('add_teacher/', views.add_teacher, name='add-teacher'),
    path('add_student/', views.add_student, name='add-student'),

    path('department_list/', views.department_list, name='department-list'),
    path('teacher_list/', views.teacher_list, name='teacher-list'),
    path('student_list/', views.student_list, name='student-list'),
    path('staff_list/', views.staff_list, name='staff-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
