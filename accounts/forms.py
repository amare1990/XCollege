from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].help_text = None
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].help_text = None
    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].help_text = None

    self.fields['username'].widget.attrs['autocomplete'] = 'off'
    self.fields['password1'].widget.attrs['autocomplete'] = 'off'
    self.fields['password2'].widget.attrs['autocomplete'] = 'off'

# Edit profile form
# class EditProfileForm(UserChangeForm):
#   first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#   last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#   username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#   last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#   # is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
#   # is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
#   # is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
#   date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

#   class Meta:
#     model = User
#     fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'date_joined')

# Password change form
class PasswordChangingForm(PasswordChangeForm):
  old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

  class Meta:
    model = User
    fields = ('old_password', 'new_password1', 'new_password2')


from django import forms
from django.contrib.auth.forms import UserChangeForm
from admin_app.models import UserProfile
from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Add fields from the UserProfile model
    role = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Add other fields from the UserProfile model as needed

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields.pop('password')  # Remove the 'password' field if it exists

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        # Save the UserProfile fields
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.role = self.cleaned_data['role']
        user_profile.department = self.cleaned_data['department']
        # Save other fields from the UserProfile model as needed
        if commit:
            user.save()
            user_profile.save()
        return user
