from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import UserProfile, Department, Course
from .forms import AddStudentForm, AddTeacherForm, AddDepartmentForm, AddCourseForm
from django.contrib import messages
from django.core.exceptions import ValidationError

def admin_dashboard(request):

    total_students = UserProfile.objects.filter(role='student').count()
    total_teachers = UserProfile.objects.filter(role='teacher').count()

    department = Department.objects.filter(department_head=request.user.username)

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers
    }

    if request.user.is_staff:
      return render(request, 'admin_app/admin_dashboard.html', context)
    elif request.user.username == department.department_head:
        return render(request, 'admin_app/heads_page.html', {'department': department })
    else:
        return render(request, 'website/courses-list.html')

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
            user_instance = form_student.save(commit=False)
            if UserProfile.objects.filter(user=user_instance.user).exists():
                messages.error(request, 'This user profile has already been registered')
                return redirect('student-list')
            else:
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

def course_edit(request, course_id):
       course = get_object_or_404(Course, pk=course_id)
       if request.method == 'POST':
           form_course = AddCourseForm(request.POST, instance=course)
           if form_course.is_valid():
               form_course.save()
               return redirect('course-detail', course_id=course_id)
       else:
           form_course = AddCourseForm(instance=course)
       return render(request, 'admin_app/course_edit.html', {'form_course': form_course })


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

def department_edit(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        form_department = AddDepartmentForm(request.POST, instance=department)
        if form_department.is_valid():
            form_department.save()
            return redirect('department-detail', department_id=department_id)
    else:
        form_department = AddDepartmentForm(instance=department)
    return render(request, 'admin_app/department_edit.html', {'form_department': form_department })

def department_detail(request, department_id):
    department = Department.objects.get(pk=department_id)

    context = {
      'department':department
   }
    return render(request, 'admin_app/department_detail.html', context)

def department_delete(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        department.delete()
        messages.info(request, "Deleted successfully!")
        return redirect('department-list')
    return render(request, 'admin_app/department_delete.html', {'department': department })

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

def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(UserProfile, pk=teacher_id)
    if request.method == 'POST':
        form_teacher = AddTeacherForm(request.POST, instance=teacher)
        if form_teacher.is_valid():
            form_teacher.save()
            return redirect('teacher-detail', teacher_id=teacher_id)
    else:
        form_teacher = AddTeacherForm(instance=teacher)
    return render(request, 'admin_app/teacher_edit.html', {'form_teacher': form_teacher })

def teacher_detail(request, teacher_id):
    teacher = UserProfile.objects.get(pk=teacher_id)

    context = {
      'teacher':teacher
   }
    return render(request, 'admin_app/teacher_detail.html', context)

def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(UserProfile, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        messages.info(request, "Deleted successfully!")
        return redirect('teacher-list')
    return render(request, 'admin_app/teacher_delete.html', {'teacher': teacher })

# Student list
def student_list(request):

   students = UserProfile.objects.filter(role='student')
   number_of_students = students.count()
   context = {
      'students': students,
      'number_of_students': number_of_students,
   }

   return render(request, 'admin_app/student_list.html', context)

def student_edit(request, student_id):
    student = get_object_or_404(UserProfile, pk=student_id)
    if request.method == 'POST':
        form_student = AddStudentForm(request.POST, instance=student)
        if form_student.is_valid():
            form_student.save()
            return redirect('student-detail', student_id=student_id)
    else:
        form_student = AddStudentForm(instance=student)
    return render(request, 'admin_app/student_edit.html', {'form_student': form_student })

def student_detail(request, student_id):
    student = UserProfile.objects.get(pk=student_id)

    context = {
      'student':student
   }
    return render(request, 'admin_app/student_detail.html', context)

def student_delete(request, student_id):
    student = get_object_or_404(UserProfile, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.info(request, "Deleted successfully!")
        return redirect('student-list')
    return render(request, 'admin_app/student_delete.html', {'student': student })

# course list
def course_list(request):

   courses = Course.objects.all()
   number_of_courses = courses.count()
   context = {
      'courses': courses,
      'number_of_courses': number_of_courses,
   }

   return render(request, 'admin_app/course_list.html', context)



