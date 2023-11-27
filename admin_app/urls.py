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
    path('course/<int:course_id>/edit/', views.course_edit, name='course-edit'),

    path('add_teacher/', views.add_teacher, name='add-teacher'),
    path('add_student/', views.add_student, name='add-student'),

    path('department_list/', views.department_list, name='department-list'),
    path('teacher_list/', views.teacher_list, name='teacher-list'),
    path('teacher/<int:teacher_id>/detail/', views.teacher_detail, name='teacher-detail'),
    path('teacher/<int:teacher_id>/edit/', views.teacher_edit, name='teacher-edit'),
    path('teacher/<int:teacher_id>/delete/', views.teacher_delete, name='teacher-delete'),

    path('student_list/', views.student_list, name='student-list'),
    path('student/<int:student_id>/detail/', views.student_detail, name='student-detail'),
    path('student/<int:student_id>/edit/', views.student_edit, name='student-edit'),
    path('student/<int:student_id>/delete/', views.student_delete, name='student-delete'),

    path('staff_list/', views.staff_list, name='staff-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
