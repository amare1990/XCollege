from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserProfile, Department, Course
from .forms import AddStudentForm, AddTeacherForm, AddDepartmentForm, AddCourseForm
from django.contrib import messages

def admin_dashboard(request):

    total_students = UserProfile.objects.filter(role='student').count()
    total_teachers = UserProfile.objects.filter(role='teacher').count()

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers
    }

    if request.user.is_staff:
      return render(request, 'admin_app/admin_dashboard.html', context)

def add_department(request):
    if request.method == 'POST':
        form_department = AddDepartmentForm(request.POST)
        if form_department.is_valid():
            form_department.save()
            return redirect('department-list')
    else:
        form_department = AddDepartmentForm()
    return render(request, 'admin_app/add_department.html', {'form_department': form_department})

def add_student(request):
    if request.method == 'POST':
        form_student = AddStudentForm(request.POST)
        if form_student.is_valid():
            form_student.save()
            return redirect('student-list')
    else:
        form_student = AddStudentForm()
        return render(request, 'admin_app/add_student.html', {'form_student': form_student})

def add_teacher(request):
    if request.method == 'POST':
        form_teacher = AddTeacherForm(request.POST)
        if form_teacher.is_valid():
            form_teacher.save()
            return redirect('teacher-list')
    else:
        form_teacher = AddTeacherForm()
        return render(request, 'admin_app/add_teacher.html', {'form_teacher': form_teacher})


def add_course(request):
    if request.method == 'POST':
        form_course = AddCourseForm(request.POST)
        if form_course.is_valid():
            form_course.save()
            return redirect('course-list')
    else:
        form_course = AddCourseForm()
        return render(request, 'admin_app/add_course.html', {'form_course': form_course})

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    students_registered = course.students.all()
    number_of_students_registered = students_registered.count()
    teachers_taught = course.teachers.all()
    number_of_teachers_registered = teachers_taught.count()
    department = course.department

    context = {
    #   'course_name': course.name,
      'number_of_students_registered': number_of_students_registered,
      'number_of_teachers_registered': number_of_teachers_registered,
      'students_registered': students_registered,
      'teachers_taught': number_of_teachers_registered,
      'department': department,
      'course': course
   }
    return render(request, 'admin_app/course_detail.html', context)

def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course-list')
    return render(request, 'admin_app/course_delete.html', {'course': course})



# Department list
def department_list(request):
   departments = Department.objects.all()
   number_of_departments = departments.count()

   context = {
       'departments': departments,
      'number_of_departments': number_of_departments,
   }

   return render(request, 'admin_app/departments_list.html', context)

# Staff list
def staff_list(request):
   number_of_staff = UserProfile.objects.filter(role='staff').count()
   context = {
      'number_of_staff': number_of_staff,
   }

   return render(request, 'admin_app/staff_list.html', context)

# Teachers list
def teacher_list(request):

   teachers = UserProfile.objects.filter(role='teacher')
   number_of_teachers = teachers.count()
   context = {
      'teachers': teachers,
      'number_of_teachers': number_of_teachers,
   }

   return render(request, 'admin_app/teacher_list.html', context)

# Student list
def student_list(request):

   students = UserProfile.objects.filter(role='student')
   number_of_students = students.count()
   context = {
      'students': students,
      'number_of_students': number_of_students,
   }

   return render(request, 'admin_app/student_list.html', context)

# course list
def course_list(request):

   courses = Course.objects.all()
   number_of_courses = courses.count()
   context = {
      'courses': courses,
      'number_of_courses': number_of_courses,
   }

   return render(request, 'admin_app/course_list.html', context)



