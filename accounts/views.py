from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from admin_app.models import UserProfile

# User registration form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Password change view
class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  success_url = reverse_lazy('password-change-done')

def password_change_done(request):
  return render(request, 'accounts/registration/password_change_done.html', {})


# User login
def user_login(request):

  # profile = UserProfile.objects.get(user=request.user.id)

  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      profile = get_object_or_404(UserProfile, user=request.user.id)
      context = {
            'profile': profile
        }
      messages.success(request, 'Bingo! %s' % ( user.first_name))
      if user.is_staff or profile.role == 'admin':
        # return redirect('home')
        return redirect('admin-dashboard')
      elif profile.role == 'student':
        return render(request, 'accounts/student_profile.html', context)
      elif profile.role == 'teacher' and profile.position == None:
        return render(request, 'accounts/teacher_profile.html', context)
      elif profile.position == 'head':
        return render(request, 'accounts/head_profile.html', context)
      elif profile.role == None or profile.position == None:
        return redirect('home')

    else:
      messages.info(request, 'Either username or passowrd is not corectly entered!')
      return redirect('user-login')
  return render(request, 'accounts/registration/login.html', {})


# User Registration
class UserRegistrationView(generic.CreateView):
  form_class = SignUpForm
  template_name ='accounts/registration/register.html'
  success_url= reverse_lazy('user-login')

# User Profile editing
class UserEditView(generic.UpdateView):
  form_class = EditProfileForm
  template_name ='accounts/registration/edit_profile.html'
  success_url= reverse_lazy('home')

  def get_object(self) :
    return self.request.user


