from django import forms
from website.models import Profile
from .models import Teacher

class AddProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['user', 'bio', 'role']

    widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }


# Add teacher
class AddTeacherForm(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = ['user', 'title', 'bio', 'role']

    widgets = {
          'user': forms.Select(attrs={'class': 'form-control'}),
          'title': forms.Select(attrs={'class': 'form-control'}),
          'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
          'role': forms.Select(attrs={'class': 'form-control'}),
      }


