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
class PasswordChangingForm(PasswordChangeForm):
  old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

  class Meta:
    model = User
    fields = ('old_password', 'new_password1', 'new_password2')


class EditProfileForm(forms.ModelForm):
    # Fields from the User model
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    # Fields from the UserProfile model
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=False)
    title = forms.ChoiceField(choices=UserProfile.TITLE_CHOICES, required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'title', 'department', 'bio']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # Customize form initialization if needed

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.role = self.cleaned_data['role']
        user_profile.title = self.cleaned_data['title']
        user_profile.department = self.cleaned_data['department']
        user_profile.bio = self.cleaned_data['bio']
        user_profile.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            user.save()
            user_profile.save()
        return user, user_profile
