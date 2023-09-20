from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# User registration form
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy

# User login
def user_login(request):

  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Bingo!')
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


