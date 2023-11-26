# forms.py
from django import forms
from .models import UserProfile

class StudentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'role', 'department', 'academic_year', 'semester']
        # You can customize the form fields and widgets as needed

class TeacherForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'role', 'department', 'title']
        # You can customize the form fields and widgets as needed
