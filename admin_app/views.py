from django.shortcuts import render, redirect
from django.http import HttpResponse
from website.models import Profile
from .forms import AddProfileForm, AddTeacherForm
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

      if form.is_valid():
         messages.success(request, 'You successfully added the profile')
         return redirect('home')
      else:
         messages.info(request, 'Invalid form inputs')
         return HttpResponse(status=400)  # Return a response indicating the form is invalid

   else:
      return render(request, 'admin_app/add_profile.html', {'form':form})

# Staff list
def staff_list(request):
   number_of_staff = Profile.objects.filter(role='teacher').count()
   context = {
      'number_of_staff': number_of_staff,
   }

   return render(request, 'admin_app/staff_list.html', context)


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

