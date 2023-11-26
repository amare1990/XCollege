from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile, Department
from .forms import AddStudentForm, AddTeacherForm, AddDepartmentForm
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



