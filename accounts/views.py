from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from admin_app.models import UserProfile
from admin_app.models import Department
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangeForm
  success_url = reverse_lazy('password-change-done')

def password_change_done(request):
  return render(request, 'accounts/registration/password_change_done.html', {})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                profile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                profile = None
            if profile is not None:
                context = {'profile': profile}
                messages.success(request, 'You have successfully logged in! %s' % (user.first_name))
                if user.is_staff or profile.role == 'admin':
                  return redirect('admin-dashboard')
                elif profile.role == 'student':
                    return render(request, 'accounts/student_profile.html', context)
                elif profile.role == 'teacher' and profile.position is None:
                    return render(request, 'accounts/teacher_profile.html', context)
                elif profile.position == 'head':
                    return render(request, 'accounts/head_profile.html', context)
                elif profile.role is None or profile.position is None:
                    return redirect('home')
            else:
                # Handle the case where the UserProfile does not exist
                messages.error(request, 'User profile does not exist')
                return redirect('home')
        else:
            messages.info(request, 'Either username or password is not correctly entered')
            return redirect('user-login')
    return render(request, 'accounts/registration/login.html', {})


class UserRegistrationView(generic.CreateView):
  form_class = SignUpForm
  template_name ='accounts/registration/register.html'
  success_url= reverse_lazy('user-login')


def edit_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    print('prifile id:  ', profile.id)
    departments = Department.objects.all()
    # show_edit_profile = False
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            # user_profile.profile_picture = request.FILES.get('profile_picture')

            role = request.POST.get('role')
            user_profile.role = role
            if role == 'teacher':
                user_profile.position = request.POST.get('position')
                user_profile.title = request.POST.get('title')
            elif role == 'student':
                user_profile.academic_year = request.POST.get('academic_year')
                user_profile.semester = request.POST.get('semester')

            department_id = request.POST.get('department')
            if department_id is None:
                department = Department.objects.get(pk=department_id)
                user_profile.department = department
            user_profile.bio = request.POST.get('bio')
            user_profile.profile_picture = request.FILES.get('profile_picture')
            user_profile.save()
            return redirect('admin-dashboard')
    else:
        form = EditProfileForm(instance=profile.user)
        # if request.user.userprofile.role == 'admin':
        #     # Check if the userprofile being viewed has not been updated by the admin yet
        #     if not profile.updated_by_admin:
        #         show_edit_profile = True
    return render(request, 'accounts/registration/edit_profile_dynamic.html',
                  {'form': form, 'departments': departments, 'profile': profile})
