from django import forms
from website.models import Profile
from .models import Teacher, Student, Course

class AddProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['user', 'bio', 'role', 'profile_picture']

    widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'})
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

# Add student
class AddStudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['user', 'academic_year', 'semester', 'bio', 'role']

    widgets = {
          'user': forms.Select(attrs={'class': 'form-control'}),
          'academic_year': forms.Select(attrs={'class': 'form-control'}),
          'semester': forms.Select(attrs={'class': 'form-control'}),
          'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
          'role': forms.Select(attrs={'class': 'form-control'}),
      }

# Add course
class AddCourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'teacher', 'students']

    widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control'}),
          'teacher': forms.Select(attrs={'class': 'form-control'}),
          'students': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
      }
