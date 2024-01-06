from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Department, Course, Assessment, Mark
from .forms import AddStudentForm, AddTeacherForm, AddDepartmentForm, AddCourseForm, CourseRegistrationForm, AddCourseOfferingForm, OfferPositionForm, AddMarksForm, AssessmentForm, AcademicYear, EditTeacherForm
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def letter_grade(total_marks):
    grade = ''
    if total_marks >= 90:
            grade= 'A+'
    elif total_marks >=85:
        grade = 'A'
    elif total_marks >= 80:
        grade = 'A-'
    elif total_marks >= 75:
        grade = 'B+'
    elif total_marks >= 70:
        grade = 'B'
    elif total_marks >= 65:
        grade = 'B-'
    elif total_marks >= 60:
        grade = 'C+'
    elif total_marks >= 50:
        grade = 'C'
    elif total_marks >= 45:
        grade = 'C-'
    elif total_marks >= 40:
        grade = 'D'
    else:
        grade = 'F'

    return grade


def admin_dashboard(request):
    total_students = UserProfile.objects.filter(role='student').count()
    total_teachers = UserProfile.objects.filter(role='teacher').count()

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
        elif profile.role == 'teacher' and profile.position is None:
            return render(request, 'accounts/teacher_profile.html', context)
        else:
            return HttpResponse("Unauthorized access")
    except UserProfile.DoesNotExist:
        return redirect('add-teacher')


def offer_position(request):
    if request.method == 'POST':
        form = OfferPositionForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            teachers = form.cleaned_data['teachers']
            # Custom logic to filter teachers based on the selected position and department
            # For example:
            # if position == 'department_head':
            filtered_teachers = teachers.filter(department=department)
            # elif position == 'school_dean':
            # filtered_teachers = teachers.filter(school=department.school)  # Assuming school is a field in UserProfile
            # Add similar logic for other positions
            # else:
            # filtered_teachers = teachers
            # form.save()
            return redirect('view-position')
    else:
        form = OfferPositionForm()
    return render(request, 'admin_app/offer_position.html', {'form': form})

def view_position(request):
    department_head_profiles = UserProfile.objects.filter(position='head')
    school_dean_profiles = UserProfile.objects.filter(position='school dean')
    college_dean_profiles = UserProfile.objects.filter(position='college dean')
    program_coordinator_profiles = UserProfile.objects.filter(position='program coordinator')
    chair_profiles = UserProfile.objects.filter(position='chair')

    return render(request, 'admin_app/view_position.html', {
        'department_head_profiles': department_head_profiles,
        'school_dean_profiles': school_dean_profiles,
        'college_dean_profiles': college_dean_profiles,
        'program_coordinator_profiles': program_coordinator_profiles,
        'chair_profiles': chair_profiles,
    })

def add_department(request):
    if request.method == 'POST':
        form_department = AddDepartmentForm(request.POST)
        if form_department.is_valid():
            form_department.save()
            return redirect('department-list')
        else:
            messages.error(request, "You didn't fill the form proporly!")
            return redirect('add-department')
    else:
        form_department = AddDepartmentForm()
        return render(request, 'admin_app/department/add_department.html', {'form_department': form_department})

def add_student(request):
    if request.method == 'POST':
        form_student = AddStudentForm(request.POST, request.FILES)
        if form_student.is_valid():
            user_instance = form_student.save(commit=False)
            if UserProfile.objects.filter(user=user_instance.user).exists():
                messages.error(request, 'This user profile has already been registered')
                return redirect('student-list')
            else:
                form_student.save()
                return redirect('student-list')
        else:
            messages.error(request, "Invalid form")
    else:
        form_student = AddStudentForm()
        return render(request, 'admin_app/student/add_student.html', {'form_student': form_student})

def add_teacher(request):
    if request.method == 'POST':
        form_teacher = AddTeacherForm(request.POST, request.FILES)
        if form_teacher.is_valid():
            user_instance = form_teacher.save(commit=False)
            if UserProfile.objects.filter(user=user_instance).exists():
                messages.error(request, 'This user profile already exists')
                return redirect('teacher-list')
            else:
                form_teacher.save()
                return redirect('teacher-list')
        else:
            messages.error(request, "You didn't fill the form successfully!")
            # return render(request, 'admin_app/teacher/add_teacher.html', {'form_teacher': form_teacher})
    else:
        form_teacher = AddTeacherForm()
        return render(request, 'admin_app/teacher/add_teacher.html', {'form_teacher': form_teacher})

def add_course(request):
    if request.method == 'POST':
        form_course = AddCourseForm(request.POST)
        if form_course.is_valid():
            course_code = form_course.cleaned_data['course_code']
            try:
                course = Course.objects.get(course_code=course_code)
                messages.error(request, f"This course code-{course.course_code} has already been added")
                return redirect('add-course')
            except ObjectDoesNotExist:
                form_course.save()
                return redirect('course-list')
        else:
            messages.error(request, "You didn't fill the form successfully!")
            return render(request, 'admin_app/course/add_course.html', {'form_course': form_course})
    else:
        form_course = AddCourseForm()
        return render(request, 'admin_app/course/add_course.html', {'form_course': form_course})

def course_detail(request, course_code):
    course = Course.objects.get(course_code=course_code)
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
      'teachers_taught': teachers_taught,
      'department': department,
      'course': course
   }
    return render(request, 'admin_app/course/course_detail.html', context)

def course_edit(request, course_code):
       course = get_object_or_404(Course, course_code=course_code)
       if request.method == 'POST':
           form_course = AddCourseForm(request.POST, instance=course)
           if form_course.is_valid():
               form_course.save()
               return redirect('course-detail', course_code=course_code)
       else:
           form_course = AddCourseForm(instance=course)
       return render(request, 'admin_app/course/course_edit.html', {'form_course': form_course, 'course':course })


def course_delete(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
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


def my_all_department_courses(request):
    user = request.user
    user_profile = user.userprofile
    my_department = user_profile.department
    courses = Course.objects.filter(department=my_department)
    # courses = my_department.courses.objects.all()

    return render(request, 'admin_app/head/my_all_department_courses.html', {'courses': courses})


# Staff list
def staff_list(request):
   number_of_staff = UserProfile.objects.filter(role='staff').count()
   context = {
      'number_of_staff': number_of_staff,
   }

   return render(request, 'admin_app/staff/staff_list.html', context)

# Teachers list
def teacher_list(request):
    if request.user.userprofile.role == 'admin':
       teachers = UserProfile.objects.filter(role='teacher')
    else:
       teachers = UserProfile.objects.filter(role='teacher', department=request.user.userprofile.department)
    number_of_teachers = teachers.count()
    context = {
      'teachers': teachers,
      'number_of_teachers': number_of_teachers,}
    return render(request, 'admin_app/teacher/teacher_list.html', context)

def my_all_department_students(request):
    user = request.user
    user_profile = user.userprofile
    print('userprofile= ', user_profile)
    my_department = user_profile.department
    department_students = UserProfile.objects.filter(role='student', department=my_department)
    print('dept students= ', department_students)

    return render(request, 'admin_app/head/my_all_department_students.html', {'department_students': department_students})

def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(UserProfile, pk=teacher_id)
    if request.method == 'POST':
        form_teacher = EditTeacherForm(request.POST, request.FILES, instance=teacher)
        if form_teacher.is_valid():
            # form_teacher.save(commit=False)
            # teacher.user= request.user
            form_teacher.save()
            return redirect('teacher-detail', teacher_id=teacher_id)
    else:
        form_teacher = AddTeacherForm(instance=teacher)
    return render(request, 'admin_app/teacher/teacher_edit.html', {'form_teacher': form_teacher, 'teacher':teacher })

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

    return render(request, 'admin_app/teacher/teacher_courses.html', context)


def add_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assessments')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = AssessmentForm()
        return render(request, 'admin_app/teacher/add_assessment.html', {'form': form})

def assessments(request):
    assessments = Assessment.objects.all()
    return render(request, 'admin_app/teacher/assessments.html', {'assessments': assessments})

def add_mark(request, course_code):
    course = Course.objects.get(course_code=course_code)
    students = course.students.all()
    assessments = Assessment.objects.all()

    if request.method == 'POST':
        for student in students:
            print('student name= ', student.user.username)
            # print(request.POST.GET('comment'))
            for assessment in assessments:
                marks_field_name = f"marks_{student.id}_{assessment.id}"
                mark = request.POST.get(marks_field_name, 0)
                Mark.objects.create(student=student, assessment=assessment, mark=mark, course=course)
                # mark = Mark.objects.get(student=student, assessment=assessment)
                # mark.comment= comment

        return redirect('mark-list', course_code=course.course_code)
    else:
        form = AddMarksForm()

    return render(request, 'admin_app/teacher/add_mark.html', {'form': form, 'students': students, 'course': course, 'assessments': assessments})

def mark_list(request, course_code):
    selected_course = Course.objects.get(course_code=course_code)
    students = selected_course.students.all()
    assessments = Assessment.objects.all()
    marks_data = []
    grade = ''
    for student in students:
        total_marks = 0
        student_marks = []
        for assessment in assessments:
            marks = Mark.objects.filter(student=student, assessment=assessment)
            if marks.exists():
                mark = marks.first()
                total_marks += mark.mark
                student_marks.append(mark)
            else:
                student_marks.append(None)
        grade = letter_grade(total_marks)

        marks_data.append({'student': student, 'marks': student_marks, 'total_marks': total_marks, 'grade': grade})

    return render(request, 'admin_app/teacher/mark_list.html', {'course': selected_course, 'assessments': assessments, 'marks_data': marks_data})





# Student list
def student_list(request):

   if request.user.userprofile.role == 'admin':
       students = UserProfile.objects.filter(role='student')
   else:
       students = UserProfile.objects.filter(role='student', department=request.user.userprofile.department)

   number_of_students = students.count()
   context = {
      'students': students,
      'number_of_students': number_of_students,
   }

   return render(request, 'admin_app/student/student_list.html', context)

def student_edit(request, student_id):
    student = get_object_or_404(UserProfile, pk=student_id)
    if request.method == 'POST':
        form_student = AddStudentForm(request.POST, request.FILES, instance=student)
        if form_student.is_valid():
            form_student.save()
            return redirect('student-detail', student_id=student_id)
    else:
        form_student = AddStudentForm(instance=student)
    return render(request, 'admin_app/student/student_edit.html', {'form_student': form_student, 'student':student })

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

#    courses = Course.objects.filter(department= request.user.userprofile.department)
   courses = Course.objects.all()
   number_of_courses = courses.count()
   context = {
      'courses': courses,
      'number_of_courses': number_of_courses,
   }

   return render(request, 'admin_app/course/course_list.html', context)



def course_registration(request):
    student_department=request.user.userprofile.department
    if request.method == 'POST':
        form_course_registration = CourseRegistrationForm(student_department, request.POST)
        if form_course_registration.is_valid():
            selected_courses = form_course_registration.cleaned_data['courses']
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.courses_registered.add(*selected_courses)
            return redirect('student-courses')
        else:
            messages.error(request, "You didn't check the courses properly! Please select at least one course!")
            return redirect('course-register')
    else:
        form_course_registration = CourseRegistrationForm(student_department)
        return render(request, 'admin_app/course/course_registration.html', {'form_course_registration': form_course_registration})

def view_result(request, course_code):
    selected_course = Course.objects.get(course_code=course_code)
    userObj = request.user
    print('username= ,', userObj.username)
    marks = Mark.objects.filter(student=userObj.userprofile, course=selected_course)
    # print('Mark assessment queryset= ', mark.assessment)
    # assessments = mark.assessment
    assessments = Assessment.objects.all()
    my_mark = []
    total_mark = 0
    for mark in marks:
        total_mark+= mark.mark
        my_mark.append(mark)

    grade = letter_grade(total_mark)
    return render(request, 'admin_app/student/view_result.html', { 'assessments': assessments,

           'course': selected_course, 'my_mark': my_mark, 'userObj': userObj,
           'total_mark': total_mark,
           'grade': grade})



def add_course_offering(request):
    user = request.user
    head_department = user.userprofile.department
    if request.method == 'POST':
        form = AddCourseOfferingForm(head_department, request.POST)
        if form.is_valid():
            course = Course.objects.filter(department=head_department, id=form.cleaned_data['course'].id).first()
            teachers = form.cleaned_data['teachers']
            course.teachers.set(teachers)
            course.offered = True
            course.save()
            return redirect('course-offering-view')
    else:
        initial_department = Department.objects.get(id=head_department.id)
        form = AddCourseOfferingForm(head_department, initial={'department': initial_department})
    return render(request, 'admin_app/head/add_course_offering.html', {'form': form})

def remove_course_offering(request, course_code):
    course = Course.objects.get(course_code=course_code)
    print('course-codes= ', course)
    course.offered = False
    teachers = {}
    course.teachers.set(teachers)
    course.save()
    return redirect('course-offering-view')

def student_courses(request):
    user_profile = UserProfile.objects.get(user=request.user)
    registered_courses = user_profile.courses_registered.all()

    context = {
        'profile': user_profile,
        'courses': registered_courses
    }

    return render(request, 'admin_app/course/student_courses.html', context)


def course_offering_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    department = user_profile.department

    courses_with_teachers = Course.objects.filter(department=department, offered = True).prefetch_related('teachers').all()
    return render(request, 'admin_app/head/course_offering_view.html', {'courses_with_teachers': courses_with_teachers,
                                                                        'profile':user_profile })
