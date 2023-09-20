from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# User registration form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Password change view
class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  # form_class = PasswordChangeForm
  success_url = reverse_lazy('password-change-done')
  # success_url = reverse_lazy('user-login')
# Password change done!
def password_change_done(request):
  return render(request, 'accounts/registration/password_change_done.html', {})


# User login
def user_login(request):

  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Bingo! %s' % ( user.first_name))
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


