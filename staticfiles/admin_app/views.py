from django.shortcuts import render, redirect
from django.http import HttpResponse
from website.models import Profile
from admin_app.models import Teacher, Student, Course
from .forms import AddProfileForm, AddTeacherForm, AddStudentForm, AddCourseForm
from django.contrib import messages

def admin_dashboard(request):

    total_students = Profile.objects.filter(role='student').count()
    total_teachers = Profile.objects.filter(role='teacher').count()

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers
    }

    if request.user.profile.role == 'admin':
      return render(request, 'admin_app/admin_dashboard.html', context)


# Add profile
def add_profile(request):
   form = AddProfileForm()
   if request.method == 'POST':
      form = AddProfileForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.success(request, 'You successfully added the profile')
         return redirect('home')
      else:
         messages.info(request, 'Invalid form inputs')
         return HttpResponse(status=400)  # Return a response indicating the form is invalid

   else:
      return render(request, 'admin_app/add_profile.html', {'form':form})

# Staff list
def staff_list(request):
   number_of_staff = Teacher.objects.filter(role='teacher').count()
   context = {
      'number_of_staff': number_of_staff,
   }

   return render(request, 'admin_app/staff_list.html', context)

# Student list
def student_list(request):
   number_of_student = Teacher.objects.filter(role='student').count()
   context = {
      'number_of_staff': number_of_student,
   }

   return render(request, 'admin_app/student_list.html', context)

# Course list
def course_list(request):
   number_of_course = Profile.objects.filter(role='student').count()
   context = {
      'number_of_staff': number_of_course
   }

   return render(request, 'admin_app/student_list.html', context)


# Add_teacher
def add_teacher(request):
   form_teacher = AddTeacherForm()

   if request.method == 'POST':
      form_teacher = AddTeacherForm(request.POST)
      if form_teacher.is_valid():
         form_teacher.save()
         messages.success(request, "You successfully added a teacher")
         return redirect('staff-list')
      else:
         messages.info(request, 'There is an error while adding form fields value')
         return redirect('add-teacher')
   else:
      return render(request, 'admin_app/add_teacher.html', { 'form_teacher': form_teacher })

# Add_student
def add_student(request):

   form_student = AddStudentForm()
   if request.method == 'POST':
      form_student = AddStudentForm(request.POST)
      if form_student.is_valid():
         form_student.save()
         messages.success(request, "You successfully added a student")
         return redirect('student-list')
      else:
         messages.info(request, 'There is an error while adding form fields value')
         return redirect('add-student')
   else:
      return render(request, 'admin_app/add_student.html', { 'form_student': form_student })

# Add a course
def add_course(request):

   form_course = AddCourseForm()
   if request.method == 'POST':
      form_course = AddCourseForm(request.POST)
      if form_course.is_valid():
         form_course.save()
         messages.success(request, "You successfully added a student")
         return redirect('course-list')
      else:
         messages.info(request, 'There is an error while adding form fields value')
         return redirect('add-course')
   else:
      return render(request, 'admin_app/add_course.html', { 'form_course': form_course })


# Adding a teacher to a course

# course = Course.objects.get(id=1)
# teacher = Teacher.objects.get(id=1)
# course.teacher.add(teacher)

# # Retrieving all students enrolled in a course
# course = Course.objects.get(id=1)
# students = course.students.all()
