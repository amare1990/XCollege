from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),
    path('position/offer/', views.offer_position, name='offer-position'),
    path('position/view/', views.view_position, name='view-position'),
    path('add_department', views.add_department, name='add-department'),
    path('department_list/', views.department_list, name='department-list'),
    path('department/<int:department_id>/edit', views.department_edit, name='department-edit'),
    path('department/<int:department_id>/detail', views.department_detail, name='department-detail'),
    path('department/<int:department_id>/delete', views.department_delete, name='department-delete'),

    path('add_course/', views.add_course, name='add-course'),
    path('course_list/', views.course_list, name='course-list'),
    path('course_detail/<str:course_code>/', views.course_detail, name='course-detail'),
    path('course/<str:course_code>/delete', views.course_delete, name='course-delete'),
    path('course/<str:course_code>/edit/', views.course_edit, name='course-edit'),
    path('my_all_department_courses/', views.my_all_department_courses, name='my-all-department-courses'),

    path('add_teacher/', views.add_teacher, name='add-teacher'),
    path('add_student/', views.add_student, name='add-student'),

    path('teacher_list/', views.teacher_list, name='teacher-list'),
    path('teacher/<int:teacher_id>/detail/', views.teacher_detail, name='teacher-detail'),
    path('teacher/<int:teacher_id>/edit/', views.teacher_edit, name='teacher-edit'),
    path('teacher/<int:teacher_id>/delete/', views.teacher_delete, name='teacher-delete'),
    path('teacher/teacher_courses/', views.teacher_courses, name='teacher-courses'),

    path('add_assessment/', views.add_assessment, name='add-assessment'),
    path('assessments/', views.assessments, name='assessments'),
    path('fill_mark/<str:course_code>/', views.add_mark, name='add-mark'),
    path('mark_list/<str:course_code>/', views.mark_list, name='mark-list'),
    path('view_result/<str:course_code>/', views.view_result, name='view-result'),

    path('student_list/', views.student_list, name='student-list'),
    path('student/<int:student_id>/detail/', views.student_detail, name='student-detail'),
    path('student/<int:student_id>/edit/', views.student_edit, name='student-edit'),
    path('student/<int:student_id>/delete/', views.student_delete, name='student-delete'),
    path('student/register/', views.course_registration, name='course-register'),
    path('student/student_courses/', views.student_courses, name='student-courses'),

    path('head/course_offer/', views.add_course_offering, name='course-offer'),
    path('head/course_offering_view/', views.course_offering_view, name='course-offering-view'),
    path('head/course/<str:course_code>/unoffer/', views.remove_course_offering, name='remove-offering'),
    path('head/department_students/', views.my_all_department_students, name='department-students'),

    path('staff_list/', views.staff_list, name='staff-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
