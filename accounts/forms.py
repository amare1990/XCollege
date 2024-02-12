from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from admin_app.models import UserProfile, Department


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

# Password change form
# class PasswordChangingForm(PasswordChangeForm):
#   old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
#   new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
#   new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

#   class Meta:
#     model = User
#     fields = ('old_password', 'new_password1', 'new_password2')


# class EditProfileForm(forms.ModelForm):
#     # Fields from the User model
#     username = forms.CharField(max_length=150, required=True)
#     email = forms.EmailField(max_length=254, required=True)
#     first_name = forms.CharField(max_length=30, required=False)
#     last_name = forms.CharField(max_length=150, required=False)

#     # Fields from the UserProfile model
#     role = forms.ChoiceField(choices=[('', '---------')] + list(UserProfile.ROLE_CHOICES), required=False)
#     title = forms.ChoiceField(choices=[('', '---------')] + list(UserProfile.TITLE_CHOICES), required=False)
#     position = forms.ChoiceField(choices=[('', '---------')] + list(UserProfile.POSITION), required=False)
#     # position = [('', '---------')] + list(UserProfile.POSITION)
#     department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
#     academic_year = forms.ChoiceField(choices=[('', '---------')] + list(UserProfile.year), required=False)
#     semester = forms.ChoiceField(choices=[('', '---------')] + list(UserProfile.SEMESTER), required=False)
#     bio = forms.CharField(widget=forms.Textarea, required=False)
#     profile_picture = forms.ImageField(required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'role', 'title', 'department', 'bio']

#     def __init__(self, *args, **kwargs):
#         super(EditProfileForm, self).__init__(*args, **kwargs)
#         user_profile = self.instance.userprofile  # Assuming UserProfile is related to User
#         if user_profile.role == 'student':
#             self.fields.pop('title')
#             self.fields.pop('position')
#         elif user_profile.role == 'teacher':
#             self.fields.pop('academic_year')
#             self.fields.pop('semester')

#     def save(self, commit=True):
#         user = super(EditProfileForm, self).save(commit=False)
#         user_profile, created = UserProfile.objects.get_or_create(user=user)
#         user_profile.role = self.cleaned_data['role']
#         if user_profile.role == 'teacher':
#            user_profile.title = self.cleaned_data['title']
#         user_profile.department = self.cleaned_data['department']
#         user_profile.bio = self.cleaned_data['bio']
#         if user_profile.role == 'teacher':
#            user_profile.position = self.cleaned_data['position']
#         if user_profile.role == 'student':
#           user_profile.academic_year = self.cleaned_data['academic_year']
#           user_profile.semester = self.cleaned_data['semester']
#         user_profile.profile_picture = self.cleaned_data['profile_picture']
#         if commit:
#             user.save()
#             user_profile.save()
#         return user, user_profile

class EditProfileForm(forms.ModelForm):
    # Fields from the User model
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    # Fields from the UserProfile model
    role = forms.CharField(max_length=20, required=True)
    title = forms.CharField(max_length=100, required=False)
    department = forms.CharField(max_length=50)
    academic_year = forms.CharField(max_length=20, required=False)
    semester = forms.CharField(max_length=20, required=False)
    position = forms.CharField(max_length=100, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # if user and (user.is_superuser or user.userprofile.role == 'admin'):
        #     # Include the 'role' field for admin users
        #     self.fields['role'] = forms.CharField(max_length=20, required=True)
        if self.instance:
            user_profile = self.instance.userprofile
            if user_profile:
                if 'role' in self.fields:  # Check if the 'role' field is present
                    self.fields['role'].initial = user_profile.role
                self.fields['title'].initial = user_profile.title
                self.fields['department'].initial = user_profile.department
                self.fields['academic_year'].initial = user_profile.academic_year
                self.fields['semester'].initial = user_profile.semester
                self.fields['position'].initial = user_profile.position
                self.fields['bio'].initial = user_profile.bio
                self.fields['profile_picture'].initial = user_profile.profile_picture
