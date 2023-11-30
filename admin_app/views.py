from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Department, Course
from .forms import AddStudentForm, AddTeacherForm, AddDepartmentForm, AddCourseForm, CourseRegistrationForm, AddCourseOfferingForm, OfferPositionForm
from django.contrib import messages

def admin_dashboard(request):

    total_students = UserProfile.objects.filter(role='student').count()
    total_teachers = UserProfile.objects.filter(role='teacher').count()

    # department = Department.objects.filter(department_head=request.user.username)

    context1 = {
        'total_students': total_students,
        'total_teachers': total_teachers
    }

    try:
        profile = UserProfile.objects.get(user=request.user)
        context = {
            'profile': profile
        }

        if profile.role == 'admin' or request.user.is_staff:
            return render(request, 'admin_app/admin_dashboard.html', context1)
        elif profile.role == 'student':
            return render(request, 'accounts/student_profile.html', context)
        elif profile.position == 'head':
            return render(request, 'accounts/head_profile.html', context)
        elif profile.role == 'teacher' and profile.position == None:
            return render(request, 'accounts/teacher_profile.html', context)
    except UserProfile.DoesNotExist:
        return redirect('add-teacher')


def offer_position(request):
    if request.method == 'POST':
        form = OfferPositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-position')
    else:
        form = OfferPositionForm()
    return render(request, 'admin_app/offer_position.html', {'form': form})

def view_position(request):
    head_profiles = UserProfile.objects.filter(position='head')
    return render(request, 'admin_app/view_position.html', {'head_profiles': head_profiles})




def add_department(request):
    if request.method == 'POST':
        form_department = AddDepartmentForm(request.POST)
        if form_department.is_valid():
            form_department.save()
            return redirect('department-list')
    else:
        form_department = AddDepartmentForm()
    return render(request, 'admin_app/department/add_department.html', {'form_department': form_department})

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
        return render(request, 'admin_app/student/add_student.html', {'form_student': form_student})

def add_teacher(request):
    if request.method == 'POST':
        form_teacher = AddTeacherForm(request.POST)
        if form_teacher.is_valid():
            form_teacher.save()
            return redirect('teacher-list')
    else:
        form_teacher = AddTeacherForm()
        return render(request, 'admin_app/teacher/add_teacher.html', {'form_teacher': form_teacher})


def add_course(request):
    if request.method == 'POST':
        form_course = AddCourseForm(request.POST)
        if form_course.is_valid():
            form_course.save()
            return redirect('course-list')
    else:
        form_course = AddCourseForm()
        return render(request, 'admin_app/course/add_course.html', {'form_course': form_course})

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
    return render(request, 'admin_app/course/course_detail.html', context)

def course_edit(request, course_id):
       course = get_object_or_404(Course, pk=course_id)
       if request.method == 'POST':
           form_course = AddCourseForm(request.POST, instance=course)
           if form_course.is_valid():
               form_course.save()
               return redirect('course-detail', course_id=course_id)
       else:
           form_course = AddCourseForm(instance=course)
       return render(request, 'admin_app/course/course_edit.html', {'form_course': form_course })


def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course-list')
    return render(request, 'admin_app/course/course_delete.html', {'course': course})



# Department list
def department_list(request):
   departments = Department.objects.all()
   number_of_departments = departments.count()

   context = {
       'departments': departments,
      'number_of_departments': number_of_departments,
   }

   return render(request, 'admin_app/department/departments_list.html', context)

def department_edit(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        form_department = AddDepartmentForm(request.POST, instance=department)
        if form_department.is_valid():
            form_department.save()
            return redirect('department-detail', department_id=department_id)
    else:
        form_department = AddDepartmentForm(instance=department)
    return render(request, 'admin_app/department/department_edit.html', {'form_department': form_department })

def department_detail(request, department_id):
    department = Department.objects.get(pk=department_id)

    context = {
      'department':department
   }
    return render(request, 'admin_app/department/department_detail.html', context)

def department_delete(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        department.delete()
        messages.info(request, "Deleted successfully!")
        return redirect('department-list')
    return render(request, 'admin_app/department/department_delete.html', {'department': department })

# Staff list
def staff_list(request):
   number_of_staff = UserProfile.objects.filter(role='staff').count()
   context = {
      'number_of_staff': number_of_staff,
   }

   return render(request, 'admin_app/staff/staff_list.html', context)

# Teachers list
def teacher_list(request):

   teachers = UserProfile.objects.filter(role='teacher')
   number_of_teachers = teachers.count()
   context = {
      'teachers': teachers,
      'number_of_teachers': number_of_teachers,
   }

   return render(request, 'admin_app/teacher/teacher_list.html', context)

def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(UserProfile, pk=teacher_id)
    if request.method == 'POST':
        form_teacher = AddTeacherForm(request.POST, instance=teacher)
        if form_teacher.is_valid():
            form_teacher.save()
            return redirect('teacher-detail', teacher_id=teacher_id)
    else:
        form_teacher = AddTeacherForm(instance=teacher)
    return render(request, 'admin_app/teacher/teacher_edit.html', {'form_teacher': form_teacher })

def teacher_detail(request, teacher_id):
    teacher = UserProfile.objects.get(pk=teacher_id)

    context = {
      'teacher':teacher
   }
    return render(request, 'admin_app/teacher/teacher_detail.html', context)

def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(UserProfile, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        messages.info(request, "Deleted successfully!")
        return redirect('teacher-list')
    return render(request, 'admin_app/teacher/teacher_delete.html', {'teacher': teacher })



def teacher_courses(request):
    user_profile = UserProfile.objects.get(user=request.user)
    courses_taught = user_profile.courses_taught.all()

    context = {
        'profile': user_profile,
        'courses': courses_taught
    }

    return render(request, 'admin_app/course/teacher_courses.html', context)

# Student list
def student_list(request):

   students = UserProfile.objects.filter(role='student')
   number_of_students = students.count()
   context = {
      'students': students,
      'number_of_students': number_of_students,
   }

   return render(request, 'admin_app/student/student_list.html', context)

def student_edit(request, student_id):
    student = get_object_or_404(UserProfile, pk=student_id)
    if request.method == 'POST':
        form_student = AddStudentForm(request.POST, instance=student)
        if form_student.is_valid():
            form_student.save()
            return redirect('student-detail', student_id=student_id)
    else:
        form_student = AddStudentForm(instance=student)
    return render(request, 'admin_app/student/student_edit.html', {'form_student': form_student })

def student_detail(request, student_id):
    student = UserProfile.objects.get(pk=student_id)

    context = {
      'student':student
   }
    return render(request, 'admin_app/student/student_detail.html', context)

def student_delete(request, student_id):
    student = get_object_or_404(UserProfile, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.info(request, "Deleted successfully!")
        return redirect('student-list')
    return render(request, 'admin_app/student/student_delete.html', {'student': student })

# course list
def course_list(request):

   courses = Course.objects.all()
   number_of_courses = courses.count()
   context = {
      'courses': courses,
      'number_of_courses': number_of_courses,
   }

   return render(request, 'admin_app/course/course_list.html', context)



def course_registration(request):
    if request.method == 'POST':
        form_course_registration = CourseRegistrationForm(request.POST)
        if form_course_registration.is_valid():
            selected_courses = form_course_registration.cleaned_data['courses']
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.courses_registered.add(*selected_courses)
            return redirect('student-courses')
    else:
        form_course_registration = CourseRegistrationForm()

    return render(request, 'admin_app/course/course_registration.html', {'form_course_registration': form_course_registration})


def add_course_offering(request):
    if request.method == 'POST':
        form = AddCourseOfferingForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            academic_year = form.cleaned_data['academic_year']
            semester = form.cleaned_data['semester']
            teachers = form.cleaned_data['teachers']
            course.academic_year = academic_year
            course.semester = semester
            course.teachers.set(teachers)
            course.save()
            return redirect('teacher-courses')
    else:
        form = AddCourseOfferingForm()

    return render(request, 'admin_app/head/add_course_offering.html', {'form': form})




def student_courses(request):
    user_profile = UserProfile.objects.get(user=request.user)
    registered_courses = user_profile.courses_registered.all()

    context = {
        'profile': user_profile,
        'courses': registered_courses
    }

    return render(request, 'admin_app/course/student_courses.html', context)

def add_course_offering(request):
    if request.method == 'POST':
        form = AddCourseOfferingForm(request.POST)
        if form.is_valid():
            selected_course = form.cleaned_data['course']
            # academic_year = form.cleaned_data['academic_year']
            # semester = form.cleaned_data['semester']
            teachers = form.cleaned_data['teachers']
            # selected_course.academic_year = academic_year
            # selected_course.semester = semester
            selected_course.teachers.set(teachers)
            selected_course.save()
            return redirect('course-offering-view')
    else:
        form = AddCourseOfferingForm()

    return render(request, 'admin_app/head/add_course_offering.html', {'form': form})


def course_offering_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    department = user_profile.department

    courses_with_teachers = Course.objects.filter(department=department).prefetch_related('teachers').all()
    return render(request, 'admin_app/head/course_offering_view.html', {'courses_with_teachers': courses_with_teachers,
                                                                        'profile':user_profile })
